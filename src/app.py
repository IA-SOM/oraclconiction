# from conector_oracldb import conn
from flask import request, Flask, jsonify, make_response
import oracledb
from openai import OpenAI
import re


con = oracledb.connect(
        user="ziani",
        password="ziani",
        dsn="oracle/freepdb1")

client = OpenAI(
    api_key="LL-C665WJ8Kybx2cOggMaVX2HhQeBwyqHXQQM68J77cgIqiLUy5ggJZFWZdGep1huJc",
    base_url="https://api.llama-api.com"
)

requete_sql = "select t3.name, t3.time from train_station as t1 join station as t2 on t1.station_id = t2.id join train as t3 on t3.train_id = t1.train_id where t1.station_id = 1;"
def optimiser_requete(requete_sql):
    response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": "Optimize the following SQL query format the output query in this  ```   ```  and give me just query optimised :"},
            {"role": "user", "content": requete_sql}
        ]
    )
    return response.choices[0].message.content

# Exemple d'utilisation de la fonction
# requete_optimisee = optimiser_requete(requete_sql)
# print(requete_optimisee)  # Imprime simplement le résultat de la requête SQL optimisée



def extract_optimized_query(output):
    # Define the pattern to match the SQL query within the output string
    pattern = r'```([^`]*)```'
    
    # Use regular expression to find the SQL query
    match = re.search(pattern, output, re.DOTALL)
    
    # If a match is found, return the optimized SQL query
    if match:
        return match.group(1).strip()
    else:
        return None
    

app = Flask(__name__)

@app.route("/submit-query", methods=["POST"])
def submit_query():
    data = request.json
    query = data.get("query")

    if query is None or query.strip() == "":
        return jsonify({"error": "Query parameter is required"}), 400

    # Optimize the query
    optimized_query = extract_optimized_query(str(optimiser_requete(query)))

    return jsonify({"optimized_query": optimized_query}), 200

# @app.route('/api/add_query', methods=['GET', 'POST'])
# def add_query():
#         # Extract the employee data from the form
#         query = request.form['name']
#         request.json.get('query')
  
#         # Insert the employee into the database
#         cur = con.cursor()
#         cur.execute("INSERT INTO query (name) VALUES (:name)",
#                     {'name': query})
#         con.commit()
#         return jsonify({'id': cur.lastrowid}), 201


@app.route('/')
def index():
    return f"<h1>{ extract_optimized_query(str(optimiser_requete(requete_sql)))}</h1>"
if __name__ == "__main__":
    app.secret_key = "samir5636@123"
    app.run(host='0.0.0.0', port=5000, debug=True)
