import mysql.connector as mysql
import ChatBot
import AfficherPrompt
def PresenceBdd(PromptUser):
   
    bdd = mysql.connect(
        host='localhost',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )
    cursor = bdd.cursor()
    query="SELECT reponse FROM questions where question='"+PromptUser+"'"
    cursor.execute(query)
    resultat = cursor.fetchone()
    if resultat is None :
        ChatBot.ChatBot(PromptUser)
    else:
        AfficherPrompt.AfficherPrompt(resultat[0])
