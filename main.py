from dotenv import  load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()
def main():
    information="""
            Subhas Chandra Bose[g] (23 January 1897 – 18 August 1945) was an Indian anti-colonial nationalist whose defiance of British authority in India made him a hero among many Indians,[h][i][j] but his wartime alliances with Nazi Germany and Fascist Japan left a legacy vexed by authoritarianism,[16][k][l][m] anti-Semitism,[19][n][o][p][q][r][24] and military failure.[s][27][28][t][u] The honorific 'Netaji' (Hindustani: "Respected Leader") was first applied to Bose in Germany in early 1942—by the Indian soldiers of the Indische Legion and by the German and Indian officials in the Special Bureau for India in Berlin. It is now used throughout India.
        Bose was born into wealth and privilege in a large Bengali family in Orissa during the British Raj.
        The early recipient of an Anglo-centric education, he was sent after college to England to take the Indian Civil Service examination. He succeeded with distinction in the vital first exam but demurred at taking the routine final exam, citing nationalism to be the higher calling. Returning to India in 1921, Bose joined the nationalist movement led by Mahatma Gandhi and the Indian National Congress. 
        He followed Jawaharlal Nehru to leadership in a group within the Congress which was less keen on constitutional reform and more open to socialism.[w] Bose became Congress president in 1938. After reelection in 1939, differences arose between him and the Congress leaders, including Gandhi, over the future federation of British India and princely states, but also because discomfort had grown among the Congress leadership over Bose's negotiable attitude to non-violence, and his plans for greater powers for himself.
        After the large majority of the Congress Working Committee members resigned in protest,[34] Bose resigned as president and was eventually ousted from the party."""
    summary_prompt="""given the information {information} which  provided I want you to create:
        1.short summary 
        2.two interesting facts about the person """
    
    ResultPromptTemplate = PromptTemplate(input_variables=["information"], template= summary_prompt ) #reuseable prompt template
    llm =ChatGoogleGenerativeAI(temperature=0.5, model="gemini-2.5-flash")
    chain= ResultPromptTemplate | llm 
    response=chain.invoke(input={"information": information})
    print(response.content)
if __name__ == "__main__":
    main()


