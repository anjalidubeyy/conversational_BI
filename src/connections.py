from pymongo import MongoClient
from decouple import config
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain


load_dotenv() #to access the api key from the .env file

client=MongoClient("mongodb://localhost:27017/") #database connection
db=client['local']
collection=db['orders_last_month']

if 'orders_last_month' not in db.list_collection_names():  #checking if database connection is successful
    print("collection does not exist ")
print("connection successful")

#setting up the llm
api_key=config("OPENAI_API_KEY")
llm=ChatOpenAI(api_key=api_key,model='gpt-3.5-turbo',temperature=0.7)

file_path="C:\\Users\\anjal\\OneDrive\\Desktop\\CONVERSATIONAL_BI_PROJECT\\docs\\sample_orders.txt" #loading the txt file
with open(file_path,"r") as file:
    sample=file.read()
    

