from google import genai
from pydantic import BaseModel
import enum

# -------------------------------- STRUCTURED JSON RESPONSE ------------------------------

# class Car(BaseModel):
#     car_name: str
#     tech_specs: list[str]

# client = genai.Client()
# response = client.models.generate_content(
#     model="gemini-2.0-flash-lite",
#     contents="List 3 popular cars in India in 2025, and include the technical specifications of it.",
#     config={
#         "response_mime_type": "application/json",
#         "response_schema": list[Car],
#     },
# )
# # Use the response as a JSON string.
# print(response.text)



# # Use instantiated objects.
# my_recipes: list[Car] = response.parsed


print('############################################################################')

# -------------------------------- STRUCTURED ENUM RESPONSE ------------------------------

class DayOfWeek(enum.Enum):
  MONDAY = "Monday"
  TUESDAY = "Tuesday"
  WEDNESDAY = "Wednesday"
  THURSDAY = "Thursday"
  FRIDAY = "Friday"
  SATURDAY = "Saturday"
  SUNDAY = "Sunday"

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='On which day will the India"s Independence Day fall on in 2025?',
    config={
        'response_mime_type': 'text/x.enum',
        'response_schema': DayOfWeek,   # or can pass it inline as below
        # 'response_schema': {
        #     "type": "STRING",
        #     "enum": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        # },
    },
)

print(response.text)