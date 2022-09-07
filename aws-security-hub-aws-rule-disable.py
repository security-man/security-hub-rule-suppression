import argparse
import boto3
import logging
import time
import os
from botocore.client import ClientError
from botocore.exceptions import ParamValidationError

logging.basicConfig(level=logging.DEBUG)

strAutoscaling_3=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/AutoScaling.3"]
strAutoscaling_5=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/Autoscaling.5"]
strCloudFormation_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/CloudFormation.1"]
strCodeBuild_5=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/CodeBuild.5"]
strConfig_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/Config.1"]
strECS2=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/ECS.2"]
strIAM_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.1"]
strIAM_3=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.3"]
strIAM_4=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.4"]
strIAM_6=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.6"]
strECR_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/ECR.1"]
strEC2_8=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/EC2.8"]
strEC2_9=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/EC2.9"]
strAPIGateway_3=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/APIGateway.3"]
strCloudTrail_5=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/CloudTrail.5"]
strElasticBeanstalk_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/ElasticBeanstalk.1"]
strIAM_21=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.21"]
strRDS_6=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/RDS.6"]
strEC2_4=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/EC2.4"]
strEC2_10=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/EC2.10"]
strEC2_15=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/EC2.15"]
# strEC2_27=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/EC2.27"]
strELB_2=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/ELB.2"]
strELB_4=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/ELB.4"]
strLambda_5=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/Lambda.5"]
strRDS_4=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/RDS.4"]
strS3_9=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/S3.9"]
strS3_6=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/S3.6"]
strS3_11=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/S3.11"]
strSecretsManager_2=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/SecretsManager.2"]
strSSM_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/SSM.1"]
strSecretsManager_1=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/SecretsManager.1"]
strSecretsManager_4=["arn:aws:securityhub:eu-west-2:","",":subscription/aws-foundational-security-best-practices/v/1.0.0/SecretsManager.4"]

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

        strAutoscaling_3[1]=account_id
        strAutoscaling_5[1]=account_id
        strCloudFormation_1[1]=account_id
        strCodeBuild_5[1]=account_id
        strConfig_1[1]=account_id
        strECS2[1]=account_id
        strIAM_1[1]=account_id
        strIAM_3[1]=account_id
        strIAM_4[1]=account_id
        strIAM_6[1]=account_id
        strECR_1[1]=account_id
        strEC2_8[1]=account_id
        strEC2_9[1]=account_id
        strAPIGateway_3[1]=account_id
        strCloudTrail_5[1]=account_id
        strElasticBeanstalk_1[1]=account_id
        strIAM_21[1]=account_id
        strRDS_6[1]=account_id
        strEC2_4[1]=account_id
        strEC2_10[1]=account_id
        strEC2_15[1]=account_id
        # strEC2_27[1]=account_id
        strELB_2[1]=account_id
        strELB_4[1]=account_id
        strLambda_5[1]=account_id
        strRDS_4[1]=account_id
        strS3_9[1]=account_id
        strS3_6[1]=account_id
        strS3_11[1]=account_id
        strSecretsManager_2[1]=account_id
        strSSM_1[1]=account_id
        strSecretsManager_1[1]=account_id
        strSecretsManager_4[1]=account_id

        strAutoscaling_3_cat="".join(strAutoscaling_3)
        strAutoscaling_5_cat="".join(strAutoscaling_5)
        strCloudFormation_1_cat="".join(strCloudFormation_1)
        strCodeBuild_5_cat="".join(strCodeBuild_5)
        strConfig_1_cat="".join(strConfig_1)
        strECS2_cat="".join(strECS2)
        strIAM_1_cat="".join(strIAM_1)
        strIAM_3_cat="".join(strIAM_3)
        strIAM_4_cat="".join(strIAM_4)
        strIAM_6_cat="".join(strIAM_6)
        strECR_1_cat="".join(strECR_1)
        strEC2_8_cat="".join(strEC2_8)
        strEC2_9_cat="".join(strEC2_9)
        strAPIGateway_3_cat="".join(strAPIGateway_3)
        strCloudTrail_5_cat="".join(strCloudTrail_5)
        strElasticBeanstalk_1_cat="".join(strElasticBeanstalk_1)
        strIAM_21_cat="".join(strIAM_21)
        strRDS_6_cat="".join(strRDS_6)
        strEC2_4_cat="".join(strEC2_4)
        strEC2_10_cat="".join(strEC2_10)
        strEC2_15_cat="".join(strEC2_15)
        # strEC2_27_cat="".join(strEC2_27)
        strELB_2_cat="".join(strELB_2)
        strELB_4_cat="".join(strELB_4)
        strLambda_5_cat="".join(strLambda_5)
        strRDS_4_cat="".join(strRDS_4)
        strS3_9_cat="".join(strS3_9)
        strS3_6_cat="".join(strS3_6)
        strS3_11_cat="".join(strS3_11)
        strSecretsManager_2_cat="".join(strSecretsManager_2)
        strSSM_1_cat="".join(strSSM_1)
        strSecretsManager_1_cat="".join(strSecretsManager_1)
        strSecretsManager_4_cat="".join(strSecretsManager_4)

        securityHubCatString = [strECR_1_cat,strS3_6_cat,strRDS_4_cat,strEC2_4_cat,strIAM_6_cat,strIAM_4_cat,strIAM_3_cat,strConfig_1_cat,strCloudFormation_1_cat,strAutoscaling_3_cat,strAutoscaling_5_cat,strCodeBuild_5_cat,strECS2_cat,strIAM_1_cat,strEC2_8_cat,strEC2_9_cat,strAPIGateway_3_cat,strCloudTrail_5_cat,strElasticBeanstalk_1_cat,strIAM_21_cat,strRDS_6_cat,strEC2_10_cat,strEC2_15_cat,strELB_2_cat,strELB_4_cat,strLambda_5_cat,strS3_9_cat,strS3_11_cat,strSecretsManager_2_cat,strSSM_1_cat,strSecretsManager_1_cat,strSecretsManager_4_cat]

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