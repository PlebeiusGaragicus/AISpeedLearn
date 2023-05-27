import os

import openai

def setup_magic():
    openai.api_key = os.getenv("OPENAI_API_KEY")


def run_prompt(prompt: str) -> str:
    # response = openai.ChatCompletion.create(
    #     model="text-davinci-003",
    #     prompt=prompt,
    #     temperature=0.9,
    #     max_tokens=2048, #??
    #     top_p=1,
    #     frequency_penalty=0.0,
    #     presence_penalty=0.6,
    #     # stop=[" Human:", " AI:"]
    # )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
    )

    print(response)
    return response.choices[0].message.content
