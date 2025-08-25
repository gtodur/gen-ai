from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import PIL.Image

# ------------------------------- IMAGE GENERATION ---------------------------------------------

# client = genai.Client()

# contents = ('Hi, can you create an image of an F1 car with design involving Indian flag?')

# response = client.models.generate_content(
#     model="gemini-2.0-flash-preview-image-generation",
#     contents=contents,
#     config=types.GenerateContentConfig(
#       response_modalities=['TEXT', 'IMAGE']
#     )
# )

# for part in response.candidates[0].content.parts:
#   if part.text is not None:
#     print(part.text)
#   elif part.inline_data is not None:
#     image = Image.open(BytesIO((part.inline_data.data)))
#     image.save('gemini-native-image.png')
#     image.show()


print('#########################################################################################')

# ------------------------------- EDITING IMAGE ---------------------------------------------

image = PIL.Image.open('gemini-native-image.png')

client = genai.Client()

text_input = ('Hi, This is a picture of an F1 car.'
            'Can you add an Indian F1 driver next to the F1 car?',)

response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=[text_input, image],
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.show()