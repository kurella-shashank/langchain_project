from dotenv import  load_dotenv
import os


load_dotenv()

#from langchain_core.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_ollama import ChatOllama



# or
# react_prompt=PromptTemplate(template=prompt_template,input_variables=["input","agent_scratchpad"])
#agent=create_agent(model=llm,tools=tools)


# def main():
    # information="""
    #         Subhas Chandra Bose[g] (23 January 1897 – 18 August 1945) was an Indian anti-colonial nationalist whose defiance of British authority in India made him a hero among many Indians,[h][i][j] but his wartime alliances with Nazi Germany and Fascist Japan left a legacy vexed by authoritarianism,[16][k][l][m] anti-Semitism,[19][n][o][p][q][r][24] and military failure.[s][27][28][t][u] The honorific 'Netaji' (Hindustani: "Respected Leader") was first applied to Bose in Germany in early 1942—by the Indian soldiers of the Indische Legion and by the German and Indian officials in the Special Bureau for India in Berlin. It is now used throughout India.
    #     Bose was born into wealth and privilege in a large Bengali family in Orissa during the British Raj.
    #     The early recipient of an Anglo-centric education, he was sent after college to England to take the Indian Civil Service examination. He succeeded with distinction in the vital first exam but demurred at taking the routine final exam, citing nationalism to be the higher calling. Returning to India in 1921, Bose joined the nationalist movement led by Mahatma Gandhi and the Indian National Congress. 
    #     He followed Jawaharlal Nehru to leadership in a group within the Congress which was less keen on constitutional reform and more open to socialism.[w] Bose became Congress president in 1938. After reelection in 1939, differences arose between him and the Congress leaders, including Gandhi, over the future federation of British India and princely states, but also because discomfort had grown among the Congress leadership over Bose's negotiable attitude to non-violence, and his plans for greater powers for himself.
    #     After the large majority of the Congress Working Committee members resigned in protest,[34] Bose resigned as president and was eventually ousted from the party."""
    # summary_prompt="""given the information {information} which  provided I want you to create:
    #     1.short summary 
    #     2.two interesting facts about the person """
    
    # ResultPromptTemplate = PromptTemplate(input_variables=["information"], template= summary_prompt ) #reuseable prompt template
    # #llm =ChatGoogleGenerativeAI(temperature=0.5, model="gemini-2.5-flash")
    # llm =ChatOllama(temperature=0.5, model="gemma3:270m")
    # chain= ResultPromptTemplate | llm 
    # response=chain.invoke(input={"information": information})
    # print(response.content)
    #print("happy christmas")
    # result=agent.invoke({"messages":HumanMessage(content="What's the weather in Hyderabad ?")})
    # print(result)

# if __name__ == "__main__":
#     main()


import tavily
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
# from tavily import  TavilyClient
# tavily=TavilyClient()
#from guardrails import Gurad
from langchain_tavily import TavilySearch

# @tool
# def search(query : str) -> str:
#     """
#     Tool call and search based on query
#     """
#     print(f"Thinking for answer to {query}")
#     return tavily.search(query=query)

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tools=[TavilySearch()]
prompt_template="""Answer the following questions as best you can. You have access to the following tools:
{tools}
Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
Thought:{agent_scratchpad}"""
react_prompt=PromptTemplate.from_template(prompt_template)
agent=create_react_agent(llm=llm,tools=tools,prompt=react_prompt) # where the reasoning agent take the  query all to the  llm, it is loop 


agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True) # it may call tool or llm , and it is orcherstator of the above prompt
chain=agent_executor
def main():
 
 result= chain.invoke(input={"input":" Give me 2 job postings related to AI engineer in Hyderabad,India and list there details "})
 print(result)

 print("Welcome to lang Family")
if __name__ == "__main__":
    main()