import asyncio
from EdgeGPT import Chatbot, ConversationStyle
import json
import pandas as pd

df = pd.read_csv('Barrie_And_District.csv')

col_names = "Date, Composite_HPI_SA, Single_Family_HPI_SA, One_Storey_HPI_SA, Two_Storey_HPI_SA, Townhouse_HPI_SA, Apartment_HPI_SA, Composite_Benchmark_SA,\
Single_Family_Benchmark_SA, One_Storey_Benchmark_SA, Two_Storey_Benchmark_SA, Townhouse_Benchmark_SA, Apartment_Benchmark_SA, Location, Population"

with open('./cookies.json', 'r') as f:
    cookies = json.load(f)

async def main():
    bot = await Chatbot.create(cookies=cookies)
    # ans = await bot.ask(prompt=f'In a table with column names: {col_names} and tablename as housing_price, write a SQL query to find which type of SA is maximum\
    #                     in Hamilton between March 2015 and June 2017', conversation_style=ConversationStyle.precise)
    ans = await bot.ask(prompt = f"Read dataframe {df} where column names are {col_names}, types of houses are: \
                        Single_Family, One_Storey, Two_Storey, Townhouse, Apartment, \
                        and tell me which type of house is the most expensive by benchmark \
                        in April 2015. Write the value in this way: 'The answer is:'", conversation_style=ConversationStyle.precise)
    json_object = json.dumps(ans, indent = 4) 
    final_dict = json.loads(json_object)
    print(final_dict["item"]["messages"][1]["text"])
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())