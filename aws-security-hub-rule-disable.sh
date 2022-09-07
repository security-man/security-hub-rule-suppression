#! /usr/bin/bash
strAutoscaling_5=""
strECS2=""
strIAM_1=""
strECS2_8=""
strECS2_9=""
strAPIGateway_3=""
strCloudTrail_5=""
strElasticBeanstalk_1=""
strIAM_21=""
strRDS_6=""
strEC2_10=""
strEC2_15=""
strELB_2=""
strELB_4=""
strLambda_5=""
strS3_9=""
strS3_11=""
strSecretsManager_2=""
strSSM_1=""
strSecretsManager_1=""
strSecretsManager_4=""
strProfile=""
for var in "$@"
do
    let $strAutoscaling_5="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/AutoScaling.5"
    let $strECS2="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/ECS.2"
    let $strIAM_1="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/IAM.1"
    let $strECS2_8="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/ECS2.8"
    let $strECS2_9="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/ECS2.9"
    let $strAPIGateway_3="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/APIGateway.3"
    let $strCloudTrail_5="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/CloudTrail.5"
    let $strElasticBeanstalk_1="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/ElasticBeanstalk.1"
    let $strIAM_21="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/IAM.21"
    let $strRDS_6="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/RDS.6"
    let $strEC2_10="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/EC2.10"
    let $strEC2_15="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/EC2.15"
    let $strELB_2="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/ELB.2"
    let $strELB_4="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/ELB.4"
    let $strLambda_5="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/Lambda.5"
    let $strS3_9="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/S3.9"
    let $strS3_11="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/S3.11"
    let $strSecretsManager_2="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/SecretsManager.2"
    let $strSSM_1="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/SSM.1"
    let $strSecretsManager_1="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/SecretsManager.1"
    let $strSecretsManager_4="arn:aws:securityhub:eu-west-2:"+$var+":control/aws-foundational-security-best-practices/v/1.0.0/SecretsManager.4"
    let $strProfile=$var
    aws securityhub update-standards-control --standards-control-arn $strAutoscaling_5 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strECS2 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strIAM_1 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strECS2_8 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strECS2_9 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strAPIGateway_3 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strCloudTrail_5 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strElasticBeanstalk_1 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strIAM_21 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strRDS_6 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strEC2_10 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strEC2_15 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strELB_2 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strELB_4 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strLambda_5 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strS3_9 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strS3_11 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strSecretsManager_2 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strSSM_1 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strSecretsManager_1 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
    aws securityhub update-standards-control --standards-control-arn $strSecretsManager_4 --control-status "DISABLED" --disabled-reason "Not applicable for my service" --profile $strProfile
done
