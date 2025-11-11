# lambda_function.py
import json
import requests # Example dependency

def lambda_handler(event, context):

    response = requests.get('https://regres.in/api/users?page=2')
    data = response.json()
    return {
        'statusCode': response.status_code,
        'body': data
    }