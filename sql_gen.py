import openai
import mykey

def generate_sql_query(prompt, max_tokens=100, temperature=0.5, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"]):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop
    )
    return response.choices[0].text

generate_sql_query("Get all the users that are older than 25 years old")