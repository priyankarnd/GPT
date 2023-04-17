import mykey
import openai

response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role":"user",
        "content":"What are the \
        different types of machine learning models?"}
        ]
)

print(response.choices[0].message.content)