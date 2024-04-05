import concurrent.futures
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

file_contents = []

# opens control-suppression-list csv
print("Reading list of controls to suppress ...")
with open('control-suppression-list.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        file_contents.append(row)

def disable_rules_from_account(account_id):
    # initiates sessions / clients per aws profile (account combined with security audit role)
    profile = account_id + "-RO"
    session = boto3.Session(profile_name=profile)
    securityhub_client = session.client("securityhub", region_name="eu-west-2")
    print("Created new session and client")
    # loops through list of controls to suppress from csv, and loops through each individual profile to make the changes to
    # securityhub api is rate-limited to 1 request per second, per account
    for contents in file_contents:
        print("")
        print("Modifying new control " + contents[0])
        print("")
        element = "arn:aws:securityhub:eu-west-2:" + account_id + contents[0]
        try:
            print("Trying Account ID " + account_id)
            securityhub_client.update_standards_control(
                StandardsControlArn=element,
                ControlStatus="DISABLED",
                DisabledReason="Not Applicable for this account"
            )
            print("Modified control " + element)
            logging.info(f"Modified SecurityHub Control")
                
        except ParamValidationError as e:
            raise Exception(
                f"Encountered parameter validation error: {e}"
            )
        except ClientError as e:
            print("- already disabled. Switching to next account")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(disable_rules_from_account,account_ids)