import AfficherPrompt
from openai import OpenAI
from dotenv import load_dotenv
import os
import mysql.connector as mysql

def ChatBot(PromptUser) :
    
    load_dotenv()
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    MODEL_NAME = "ft:gpt-4.1-nano-2025-04-14:jn-formation::Bqz1DM3f"

    reponse = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
        {"role": "user", "content": PromptUser}
        ]
    )
    ReponseChat=reponse.choices[0].message.content
    AfficherPrompt.AfficherPrompt(ReponseChat)
    MajBdd(PromptUser,ReponseChat)

def MajBdd(PromptUser,Reponse) :
    questions = []
    bdd = mysql.connect(
        host='localhost',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )
    cursor = bdd.cursor()

    cursor = bdd.cursor()
    query = "INSERT INTO questions (question, reponse,satisfaction) VALUES ('"+PromptUser+"', '"+Reponse+"','')" 
    cursor.execute(query)
    bdd.commit()

    cursor.close()
    bdd.close()