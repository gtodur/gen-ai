from google import genai
from google.genai import types
import pathlib

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('D:\\BlueBadge\\images for BB upload\\Burp Scanner Report.pdf')

prompt = "Summarize this document in less than 1000 words."
response = client.models.generate_content(
  model="gemini-2.0-flash-lite",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)