from google import genai
from google.genai import types
import os

# ---------------------------- GET MODEL INFO ------------------------
# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
# model_info = client.models.get(model="gemini-2.0-flash")
# print(model_info)

print("######################################################################")

# --------------------------- LIST MODELS ---------------------------
# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
# print("List of models that support generateContent:\n")
# for m in client.models.list():
#     for action in m.supported_actions:
#         if action == "generateContent":
#             print(m.name)

# print("List of models that support embedContent:\n")
# for m in client.models.list():
#     for action in m.supported_actions:
#         if action == "embedContent":
#             print(m.name)

print("######################################################################")

# --------------------------- TEXT-2-TEXT ---------------------------
# gemini_client = genai.Client(
#     http_options={"api_version": "v1"}, api_key=os.getenv("GOOGLE_API_KEY")
# )

# response = gemini_client.models.generate_content(
#     model="gemini-2.0-flash-lite", 
#     contents="Which country is the company Welspun from?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
#         system_instruction="You are a java developer.",  # system instructions
#         temperature=0.1
#     )
# )

# print(response.text)


print("######################################################################")

# --------------------------- MULTI-MODAL INPUT ---------------------------
# gemini_client = genai.Client(
#     http_options={"api_version": "v1"}, api_key=os.getenv("GOOGLE_API_KEY")
# )

# with open('D:\\BlueBadge\\images for BB upload\\badge-photo.png', 'rb') as f:
#     image_bytes = f.read()

# response = gemini_client.models.generate_content(
#     model="gemini-2.0-flash-lite", 
#     contents=[
#         types.Part.from_bytes(
#             data=image_bytes,
#             mime_type='image/png'
#         ),
#         'What is this image about?'
#     ],
# )

# print(response.text)


print("######################################################################")

# --------------------------- TEXT-2-TEXT (STREAMING) ---------------------------
# gemini_client = genai.Client(
#     http_options={"api_version": "v1"}, api_key=os.getenv("GOOGLE_API_KEY")
# )

# response = gemini_client.models.generate_content_stream(
#     model="gemini-2.0-flash-lite", 
#     contents="Which country is the company Welspun from?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
#         system_instruction="You are a java developer.",  # system instructions
#         temperature=0.1
#     )
# )

# for chunk in response:
#     print(chunk.text, end='')


print("######################################################################")

# --------------------------- CHAT WITH MEMORY ---------------------------
# Chat functionality is only implemented as part of the SDKs. 
# Behind the scenes, it still uses the generateContent API. 
# For multi-turn conversations, the full conversation history is sent to the model with each follow-up turn.

# gemini_client = genai.Client(
#     http_options={"api_version": "v1"}, api_key=os.getenv("GOOGLE_API_KEY")
# )

# chat = gemini_client.chats.create(model="gemini-2.0-flash-lite")

# response = chat.send_message("I have 2 dogs in my house.")
# print(response.text)

# response = chat.send_message("How many paws are in my house?")
# print(response.text)

# for message in chat.get_history():
#     print(f'role - {message.role}',end=": ")
#     print(message.parts[0].text)


print("######################################################################")

# --------------------------- CHATBOT ---------------------------
gemini_client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
#gemini_client = genai.Client()

chat = gemini_client.chats.create(model='gemini-2.0-flash-lite')

while True:
    prompt = input('> ')
    if prompt == 'exit':
        break
    
    response = chat.send_message(prompt)
    print(response.text)


print("######################################################################")

# --------------------------- CHATBOT WITH STREAMING ---------------------------
# gemini_client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))
# chat = gemini_client.chats.create(model="gemini-2.0-flash-lite")

# response = chat.send_message_stream("I have 2 dogs in my house.")
# for chunk in response:
#     print(chunk.text, end="")

# response = chat.send_message_stream("How many paws are in my house?")
# for chunk in response:
#     print(chunk.text, end="")

# for message in chat.get_history():
#     print(f'role - {message.role}', end=": ")
#     print(message.parts[0].text)