import boto3
import logging
import csv
import math
from botocore.client import ClientError
from botocore.exceptions import ParamValidationError

# establish client with root account (default profile)
session = boto3.Session(profile_name="default")
client = session.client('sts')
org = session.client('organizations')

# paginate through all org accounts
paginator = org.get_paginator('list_accounts')
page_iterator = paginator.paginate()

# get accounts ids for active accounts
account_ids = []
print("Getting full list of accounts from AWS Organizations ...")
for page in page_iterator:
    for account in page['Accounts']:
        if account['Status'] == 'ACTIVE':
            account_ids += {account['Id']}

print("Account list populated!")
print("")
enable_standards = [
    {"StandardsArn": "arn:aws:securityhub:eu-west-2::standards/aws-foundational-security-best-practices/v/1.0.0"},
    {"StandardsArn": "arn:aws:securityhub:eu-west-2::standards/cis-aws-foundations-benchmark/v/3.0.0"}]
disable_standards = [
    'arn:aws:securityhub:eu-west-2:ACCOUNTID:standards/cis-aws-foundations-benchmark/v/1.2.0',
    'arn:aws:securityhub:eu-west-2:ACCOUNTID:standards/cis-aws-foundations-benchmark/v/1.4.0',
    'arn:aws:securityhub:eu-west-2:ACCOUNTID:standards/pci-dss/v/3.2.1',
    'arn:aws:securityhub:eu-west-2:ACCOUNTID:standards/pci-dss/v/4.0.1',
    'arn:aws:securityhub:eu-west-2:ACCOUNTID:standards/nist-800-53/v/5.0.0']

def modify_securityhub_standards(profile,account_id,enable_standards,disable_standards):
    session = boto3.Session(profile_name = profile)
    client = session.client('securityhub', region_name = "eu-west-2")
    try:
        disable_standards_clone = []
        for i in range(len(disable_standards)):
            disable_standards_prefix = disable_standards[i].split("ACCOUNTID")[0]
            disable_standards_suffix = disable_standards[i].split("ACCOUNTID")[1]
            disable_standards_clone.append(disable_standards_prefix + account_id + disable_standards_suffix)
        disable_standards = client.batch_disable_standards(StandardsSubscriptionArns = disable_standards_clone)
        enable_standards = client.batch_enable_standards(StandardsSubscriptionRequests = enable_standards)
    except ClientError as e:
        print(e)

def disable_rules_from_account(profile,account_id):
    # initiates sessions / clients per aws profile (account combined with security audit role)
    session = boto3.Session(profile_name=profile)
    securityhub_client = session.client("securityhub", region_name="eu-west-2")
    print("Created new session and client")
    # loops through list of controls to suppress from csv, and loops through each individual profile to make the changes to
    # securityhub api is rate-limited to 1 request per second, per account
    control_suppression = []
    with open('suppression/cis-aws-foundations-benchmark-v-3.0.0.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            control_suppression.append(row)
    with open('suppression/aws-foundational-security-best-practices-v-1.0.0.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            control_suppression.append(row)
     
    for contents in control_suppression:
        element = contents[0].replace("037376268049",account_id)
        print("Modifying control " + element)
        try:
            print("Trying Account ID " + account_id)
            securityhub_client.update_standards_control(
                StandardsControlArn=element,
                ControlStatus="DISABLED",
                DisabledReason="Not Applicable for this account"
            )
            print("Modified successfully control " + element)
            logging.info(f"Modified SecurityHub Control")
        except ParamValidationError as e:
            raise Exception(
                f"Encountered parameter validation error: {e}"
            )
        except ClientError as e:
            print("- already disabled. Switching to next account")

for account in account_ids:
    if(account == "037376268049"):
        profile = "default"
    else:
        profile = account + "-RO"
    # modify_securityhub_standards(profile,account,enable_standards,disable_standards)
    state = 0
    with open('accounts_changed.txt', 'r') as myfile:
        if account in myfile.read():
            print("Account already modified.")
        else:
            state = 1
    myfile.close()
    print(state)
    if(state == 1):
        disable_rules_from_account(profile,account)
        with open('accounts_changed.txt','a') as myfile:
            myfile.write(account + '\n')