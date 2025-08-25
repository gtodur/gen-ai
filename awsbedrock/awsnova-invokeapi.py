import boto3
import json
from botocore.config import Config

session = boto3.Session(profile_name='gen-ai')

# Set up the Bedrock Runtime client in your source region (ap-south-1)
bedrock_runtime = session.client(service_name="bedrock-runtime", region_name="ap-south-1",  # Your source region
             config=Config(
                                connect_timeout=3600,
                                read_timeout=3600,
                                retries={"max_attempts": 3}
                            )
)

MODEL_ID = "arn:aws:bedrock:ap-south-1:904368995177:inference-profile/apac.amazon.nova-micro-v1:0"  # Hosted in us-east-1

# Define the messages for the conversation with content as an array of objects

system_prompt = [{"text": "You are a helpful assistant."}]
user_message = [{"role": "user", "content": [{"text": "List the 5 largest companies in the world and their market value."}]}]

# Inference configuration
inference_config = {
    "maxTokens": 50,
    "temperature": 0.7,
    "topP": 0.9,
    "topK": 50
}

# Request body
request_body = {
    "schemaVersion": "messages-v1",
    "system": system_prompt,
    "messages": user_message,
    "inferenceConfig": inference_config
}

try:
    # Invoke the model
    response = bedrock_runtime.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(request_body)
    )

    # Process the response
    response_body = json.loads(response['body'].read())
    print("Response from Nova Micro:")
    print(json.dumps(response_body, indent=2))


except Exception as e:
        print(f"Error invoking model: {str(e)}")