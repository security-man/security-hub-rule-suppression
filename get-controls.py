import boto3
import logging
import csv
import math
import json
from botocore.client import ClientError
from botocore.exceptions import ParamValidationError

# establish client with root account (default profile)
session = boto3.Session(profile_name="default")
client = session.client('securityhub')

standards_paginator = client.get_paginator('get_enabled_standards')
standards_page_iterator = standards_paginator.paginate()

standards_subscriptions_arns = []
for page in standards_page_iterator:
    for i in range(len(page['StandardsSubscriptions'])):
        standards_subscriptions_arns.append(page['StandardsSubscriptions'][i]['StandardsSubscriptionArn'])

for standards_arn in standards_subscriptions_arns:
    controls_paginator = client.get_paginator('describe_standards_controls')
    controls_page_iterator = controls_paginator.paginate(StandardsSubscriptionArn=standards_arn)
    controls_list = []
    with open("benchmarks/" + (standards_arn.split("subscription/")[1]).replace("/","-") + '.json','w') as fp:
        for page in controls_page_iterator:
            for item in page['Controls']:
                controls_list.append(item['StandardsControlArn'])
            json.dump(page['Controls'],fp,indent=4,default=str)
    with open("suppression/" + (standards_arn.split("subscription/")[1]).replace("/","-") + '.csv','w') as csv_f:
        csv_writer = csv.writer(csv_f, delimiter='\n',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(controls_list)
