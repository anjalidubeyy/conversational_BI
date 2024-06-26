from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from connections import llm
from prompts import question_to_query_template
from prompts import query_to_result_template
from connections import sample
from langchain.prompts import PromptTemplate
import json
from connections import collection
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document
from connections import sample
import re 
from connections import collection

#function to turn the natural language
# user question into a MongoDB query
def llmchain_invoke(llm,question_to_query_template,question,sample):
    question_to_query=PromptTemplate(template=question_to_query_template,input_variables=["question","sample"])
    llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.7)
    llm_chain=LLMChain(llm=llm,prompt=question_to_query)
    response=llm_chain.invoke({  #generate response from the llm chain using invoke function
        "question":input,
        "sample":sample
    })
    return response
    
#function to return output from the MongoDB query made by the user 
def generate_response(question,query,result):
    query_to_answer=PromptTemplate(template=query_to_result_template,input_variables=["question","query","context"])
    llm2=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.7)
    llm_chain2=load_qa_chain(llm2,chain_type="stuff",prompt=query_to_answer,document_variable_name="context") #qa chain to answer document related questions
    document=[Document(page_content=str(result))] 
    #wrapping the output of the mongo query in a document format 
    input={
        "question":question,
        "query":query,
        "input_documents":document      #provides the results of the mongo query for relevant context to the llm chain
        }
    message=llm_chain2.invoke(input,return_only_outputs="True")
    return message
    
        
if __name__=="__main__":
    input="What is the total number of clients from Uttar Pradesh whos status is fulfilled?"
    reply=llmchain_invoke(llm,question_to_query_template,input,sample) #the invoke function to turn the question to query 
    print(reply)
    
    query=json.loads(reply['text'])
    print(query)
    
    result=collection.aggregate(query) 
    execute_query=[] #create empty array for storing query results 
    for results in result:
        execute_query.append(results)#adding the results to the array 
    print(execute_query)    

    answer=generate_response(input,query,execute_query) #passes the result of the query to the other function for providing context 
    print(answer["output_text"])
else:
    print("error! failed to extract query")
    
    