import io

import boto3
import json
import csv
import pandas as pd
from pprint import pprint
'''Connecting to S3'''
s3_client = boto3.client('s3')
# print(s3_client)

'''Create list of buckets'''
bucket_list = s3_client.list_buckets()

'''Print name of first bucket'''
# pprint(bucket_list['Buckets'][0]['Name'], sort_dicts=False)

'''Print list of all bucket names'''
# bucket_count = 0
# for bucket in bucket_list['Buckets']:
#     print(bucket['Name'])
#     bucket_count += 1
# print(bucket_count)

'''Print list of all buckets using enumerate'''
# for index, bucket in enumerate(bucket_list['Buckets'], start=1):
#     print(f'{index}: {bucket["Name"]}')

'''Seeing what is inside a bucket and printing the key names'''
# bucket_name = 'data-eng-resources'
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name)
# pprint(bucket_contents)
#
# for index, key in enumerate(bucket_contents['Contents'], start=1):
#     print(f'{index}: {key["Key"]}')
#

'''another way to model what is inside buckets'''
s3_resource = boto3.resource('s3')

bucket_name = 'data-eng-resources'
# bucket = s3_resource.Bucket(bucket_name)
# contents = bucket.objects.all()
# for object in contents:
    # print(object.key)

'''Getting more information from within a key'''
# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key='python/chatbot-intent.json'
# )
'''Using json to print the body of contents'''
# contents = s3_object['Body'].read()
# contents_dict = json.loads(contents)
# pprint(contents_dict)

'''Getting more information from a key'''
# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key='python/fish-market.csv'
# )
'''Using pandas read csv to read in csv files'''
# pprint(s3_object['Body'])
# df = pd.read_csv(s3_object['Body'])
# print(df)

'''-------------------------Writing to S3-----------------------------------'''

dict_demo = {'name': 'Kieran',
             'age': '25',
             'groceries': [
                            'chocolate',
                            'doughnut',
                            'milk',
                            'pizza'
             ]
             }

# with open('kieran-dict.json', 'w') as jsonfile:
#     json.dump(dict_demo, jsonfile)

'''Uploading files to S3'''
# s3_client.upload_file(
#     Filename='kieran-dict.json',
#     Bucket='data-eng-resources',
#     Key='Data21/kbadesha.json'
# )

# s3_client.put_object(
#     Body=json.dumps(dict_demo),
#     Bucket='data-eng-resources',
#     Key='Data21/Put/kbadesha.json'
# )

'''---------------writing dataframe to S3-----------------------------------'''

# df = pd.DataFrame([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
#
# str_buffer = io.StringIO()
'''Serialise to a buffer not to your local machine'''
# df.to_csv(str_buffer)

# s3_client.put_object(
#     Body=str_buffer.getvalue(),
#     Bucket='data-eng-resources',
#     Key='Data21/CSV/kbadesha.csv'
# )

# s3_resource.Object('data-eng-resources',
#                    'Data21/CSV/kbadesha.csv'
#                    ).put(
#     Body=str_buffer.getvalue()
# )
