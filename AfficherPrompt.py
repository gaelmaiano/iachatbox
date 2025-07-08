import mysql.connector as mysql
import PresenceBdd
def AfficherPrompt(resultat):
    print(resultat)
    reponseUser=input("Cette réponse vous satisfait ?(répondre par OUI ou NON)")
    if "OUI" in reponseUser.upper() :  
        majTable("1",resultat)
    elif "NON" in reponseUser.upper() :  
        majTable("0",resultat)
    question=input("Avez vous une autre question ?")
    if "OUI" in question.upper() :
        PromptUser=input("Quelle est votre question ?")
        if PromptUser is not None :
            PresenceBdd.PresenceBdd(PromptUser)

def majTable(satisfaction,reponse) :
    bdd = mysql.connect(
        host='localhost',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )
    cursor = bdd.cursor()
    query="update questions set satisfaction='"+satisfaction+"' where reponse= '"+reponse+"'"
    cursor.execute(query)
    bdd.commit()
    cursor.close()
    bdd.close()