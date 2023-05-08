import asyncio
from EdgeGPT import Chatbot, ConversationStyle
import json
import sys

with open('./cookies.json', 'r') as f:
    cookies = json.load(f)

print("Hello, GPT Here \nType 'Exit!' to exit \nPlease enter your query:")

def user_query():
    query = input()
    return query

async def main():
    bot = await Chatbot.create(cookies=cookies)
    while True:
        q = user_query()
        if q != "Exit!":            
            ans = await bot.ask(prompt=q, conversation_style=ConversationStyle.precise)
            json_object = json.dumps(ans, indent = 4) 
            final_dict = json.loads(json_object)
            print(final_dict["item"]["messages"][1]["text"])   
            print("Type 'Exit!' to exit the chat")
        elif q == "Exit!":
            await bot.close()
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())

