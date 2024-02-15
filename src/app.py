from flask import Flask,request
from conector_oracldb import conect
import os

# from openai import OpenAI

# # Initialiser le client OpenAI
# client = OpenAI(
#     api_key="LL-C665WJ8Kybx2cOggMaVX2HhQeBwyqHXQQM68J77cgIqiLUy5ggJZFWZdGep1huJc",
#     base_url="https://api.llama-api.com"
# )

# # Fonction pour optimiser la requête SQL
# def optimiser_requete(requete_sql):
#     response = client.chat.completions.create(
#         model="llama-13b-chat",
#         messages=[
#             {"role": "system", "content": "Optimize the following SQL query:"},
#             {"role": "user", "content": requete_sql}
#         ]
#     )
#     return response.choices[0].message.content

# # Exemple d'utilisation de la fonction
# requete_sql = "select t3.name, t3.time from train_station as t1 join station as t2 on t1.station_id = t2.id join train as t3 on t3.train_id = t1.train_id where t1.station_id = 1;"
# requete_optimisee = optimiser_requete(requete_sql)
# print(requete_optimisee)  # Imprime simplement le résultat de la requête SQL optimisée

app = Flask(__name__)

conect()
@app.route('/')
def index():
    return f"<h1>connected</h1>"
