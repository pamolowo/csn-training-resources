import json
import boto3

def lambda_handler(event, context):
    ses_client = boto3.client("ses", region_name="us-west-2")
    
    try:
        body = json.loads(event['body'])
        
        name = body.get('name')
        email = body.get('email')
        phone = body.get('phone')
        position = body.get('position')
        cover_letter = body.get('coverLetter')

        # Create a dynamic subject line based on the position applied for
        subject_line = f"Application Received for {position}"

        email_response = ses_client.send_email(
            Destination={
                "ToAddresses": [email],
            },
            Message={
                "Body": {
                    "Text": {
                        "Data": f"Thank you for your application, {name}!\n\nDetails:\nName: {name}\nEmail: {email}\nPhone: {phone}\nPosition: {position}\nCover Letter: {cover_letter}"
                    },
                },
                "Subject": {
                    "Data": subject_line,
                },
            },
            Source="hello@cloudsecnetwork.com"
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Allow all origins
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',  # Allow POST and GET methods
                'Access-Control-Allow-Headers': 'Content-Type',  # Allow Content-Type header
            },
            'body': json.dumps({
                'message': 'Application submitted successfully!'
            })
        }
        
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
            'body': json.dumps({
                'message': f'Error: {str(e)}'
            })
        }
