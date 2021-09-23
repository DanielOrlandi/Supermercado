from flask import Flask, request, jsonify
import produto_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProduto', methods=['GET'])
def get_produto():
    produto = produto_dao.get_all_produto(connection)
    response = jsonify(produto)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)