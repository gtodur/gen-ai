from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get('/')
def homepage():
    return {'message': 'Welcome to the webapp'}

@app.get('/generate')
def generate(input:str):
    generatedOutput = pipeline(input)
    return {'generatedOutput': generatedOutput[0]['generated_text']}