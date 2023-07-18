
import openai
import os

openai.api_key = os.getenv("OPENAI_KEY")


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0 # this is the degree of randomness of the model
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, temperature, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature # this is the degree of randomness of the model
    )
    return response.choices[0].message["content"]