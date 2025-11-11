# lambda_function.py
import json
import requests # Example dependency

def lambda_handler(event, context):

    response = requests.get('https://regres.in/api/users?page=2')
    return {
        'statusCode': response.status_code,
        'body': response.text[:1000]
    }