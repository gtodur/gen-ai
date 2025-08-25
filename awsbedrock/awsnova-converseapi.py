import boto3
import logging
import boto3.session
from botocore.exceptions import ClientError
import json

session = boto3.Session(profile_name='gen-ai')
client = boto3.client("bedrock-runtime")
model_id = 'arn:aws:bedrock:ap-south-1:904368995177:inference-profile/apac.amazon.nova-micro-v1:0'

# Start a conversation with the user message.
user_message = "List the 5 largest companies in the world and their market value."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    print('Calling Amazon Nova model on Bedrock')
    print('--------------------------------------')
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 50, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
