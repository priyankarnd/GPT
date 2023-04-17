import user_response as ur
import openai

first_message = ur.choices[0].message.content
response=openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role":"assistant", "content":first_message},
        {"role":"user",
        "content":"Give me an explanation of one example\
        model for each category that you just gave"}
        ]
)
second_message = response.choices[0].message.content
print(second_message )