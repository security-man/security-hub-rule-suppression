import argparse
import boto3
import logging
import time
import os
import csv
from botocore.client import ClientError
from botocore.exceptions import ParamValidationError

# setup account input details and define aws profiles
input_switch_statement = input('Choose input type: 1 = comma-separated list of profiles, 2 = path to aws .config file: ')
if input_switch_statement == '1':
    profile_string = input('Specify AWS Profile List: ')
    profile_list = profile_string.split(",")
elif input_switch_statement == '2':
    profile_string = input('Specify .aws config file path: ')
    profile_list = []

    # Using readlines()
    config_file = open(profile_string, 'r')
    file_lines = config_file.readlines()

    # Strips the newline character
    for line in file_lines:
        line_contents = line.split()
        if len(line_contents) > 0:
            if line_contents[0] == '[profile':
                profile_name = line_contents[1].split(']')
                profile_list.append(profile_name[0])
else:
    raise Exception("Sorry, no numbers below zero")

file_contents = []

# opens control-suppression-list csv
with open('control-suppression-list.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        file_contents.append(row)

for contents in file_contents:
    for profile in profile_list:
        session = boto3.Session(profile_name=profile)
        securityhub_client = session.client("securityhub", region_name="eu-west-2")
        element = contents[0] + profile + contents[1]
        # time.sleep(1) # sleeping to prevent throttling

        print(element)

        try:
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
            print("- already disabled")
            # raise Exception(f"Failed to create security hub changes: {e}")


# for single accounts, the following code should be used to prevent throttling
# for profile in profile_list:
#     print("")
#     print("Suppressing rules for Account ID: " + profile)
#     print("")
#     session = boto3.Session(profile_name=profile)
#     securityhub_client = session.client("securityhub", region_name="eu-west-2")

#     for contents in file_contents:
#         try:
#             element = contents[0] + profile + contents[1]
#             time.sleep(1) # sleeping to prevent throttling

#             print(element)

#             securityhub_client.update_standards_control(
#                 StandardsControlArn=element,
#                 ControlStatus="DISABLED",
#                 DisabledReason="Not Applicable for this account"
#             )
#             print("Modified control " + element)
#             logging.info(f"Modified SecurityHub Control")
#         except ParamValidationError as e:
#             raise Exception(
#                 f"Encountered parameter validation error: {e}"
#             )
#         except ClientError as e:
#             print("- already disabled")
#             # raise Exception(f"Failed to create security hub changes: {e}")