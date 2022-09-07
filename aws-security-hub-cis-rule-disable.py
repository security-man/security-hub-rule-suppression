import argparse
import boto3
import logging
import time
import os
from botocore.client import ClientError
from botocore.exceptions import ParamValidationError

logging.basicConfig(level=logging.DEBUG)

# PCI.SSM.3 EC2 instances should be managed by AWS Systems Manager
# PCI.S3.3 S3 buckets should have cross-region replication enabled

strCIS_1_13=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/1.13"]
strCIS_1_11=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/1.11"]
strCIS_1_22=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/1.22"]
strCIS_2_4=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/2.4"]
strCIS_2_6=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/2.6"]
strCIS_3_3=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.3"]
strCIS_3_10=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.10"]
strCIS_3_11=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.11"]
strCIS_3_12=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.12"]
strCIS_3_13=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.13"]
strCIS_3_14=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.14"]
strCIS_3_1=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.1"]
strCIS_3_2=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.2"]
strCIS_3_4=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.4"]
strCIS_3_5=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.5"]
strCIS_3_6=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.6"]
strCIS_3_7=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.7"]
strCIS_3_8=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.8"]
strCIS_3_9=["arn:aws:securityhub:eu-west-2:","",":control/cis-aws-foundations-benchmark/v/1.2.0/3.9"]

def parse_arguments():
    description = "Arguments to provision a security hub rule suppression to multiple AWS accounts"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--account-ids",
        help="The account ID of the account you wish to create the CF stack in",
        dest="account_ids",
        required=True,
    )
    return parser.parse_args()

def get_args(args=parse_arguments()):
    account_ids = args.account_ids
    return account_ids

def execute_securityhub_commands():

    account_ids=get_args()

    print(account_ids)

    account_ids_split=account_ids.split(",")

    for account_id in account_ids_split:

        print(account_id)

        session = boto3.Session(profile_name=account_id)
        securityhub_client = session.client("securityhub", region_name="eu-west-2")

        strCIS_1_13[1]=account_id
        strCIS_1_11[1]=account_id
        strCIS_1_22[1]=account_id
        strCIS_2_4[1]=account_id
        strCIS_2_6[1]=account_id
        strCIS_3_3[1]=account_id
        strCIS_3_10[1]=account_id
        strCIS_3_11[1]=account_id
        strCIS_3_12[1]=account_id
        strCIS_3_13[1]=account_id
        strCIS_3_14[1]=account_id
        strCIS_3_1[1]=account_id
        strCIS_3_2[1]=account_id
        strCIS_3_4[1]=account_id
        strCIS_3_5[1]=account_id
        strCIS_3_6[1]=account_id
        strCIS_3_7[1]=account_id
        strCIS_3_8[1]=account_id
        strCIS_3_9[1]=account_id

        strCIS_1_13_cat="".join(strCIS_1_13)
        strCIS_1_11_cat="".join(strCIS_1_11)
        strCIS_1_22_cat="".join(strCIS_1_22)
        strCIS_2_4_cat="".join(strCIS_2_4)
        strCIS_2_6_cat="".join(strCIS_2_6)
        strCIS_3_3_cat="".join(strCIS_3_3)
        strCIS_3_10_cat="".join(strCIS_3_10)
        strCIS_3_11_cat="".join(strCIS_3_11)
        strCIS_3_12_cat="".join(strCIS_3_12)
        strCIS_3_13_cat="".join(strCIS_3_13)
        strCIS_3_14_cat="".join(strCIS_3_14)
        strCIS_3_1_cat="".join(strCIS_3_1)
        strCIS_3_2_cat="".join(strCIS_3_2)
        strCIS_3_4_cat="".join(strCIS_3_4)
        strCIS_3_5_cat="".join(strCIS_3_5)
        strCIS_3_6_cat="".join(strCIS_3_6)
        strCIS_3_7_cat="".join(strCIS_3_7)
        strCIS_3_8_cat="".join(strCIS_3_8)
        strCIS_3_9_cat="".join(strCIS_3_9)

        securityHubCatString = [strCIS_1_13_cat,strCIS_1_11_cat,strCIS_1_22_cat,strCIS_2_4_cat,strCIS_2_6_cat,strCIS_3_3_cat,strCIS_3_10_cat,strCIS_3_11_cat,strCIS_3_12_cat,strCIS_3_13_cat,strCIS_3_14_cat,strCIS_3_1_cat,strCIS_3_2_cat,strCIS_3_4_cat,strCIS_3_5_cat,strCIS_3_6_cat,strCIS_3_7_cat,strCIS_3_8_cat,strCIS_3_9_cat]

        for element in securityHubCatString:

            try:

                time.sleep(1)

                print("ELEMENT HERE: " + element)

                securityhub_client.update_standards_control(
                    StandardsControlArn=element,
                    ControlStatus="DISABLED",
                    DisabledReason="Not Applicable for this account"
                )
                logging.info(f"Modified SecurityHub Control")
            except ParamValidationError as e:
                raise Exception(
                    f"Encountered parameter validation error: {e}"
                )
            except ClientError as e:
                raise Exception(f"Failed to create security hub changes: {e}")

execute_securityhub_commands()