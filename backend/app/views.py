from flask import request, jsonify
from app import app
from app.services.text2sql_service import generate_sql

@app.route('/generate_sql', methods=['POST'])
def generate_sql_route():
    data = request.get_json()
    table_structure = data.get('table_structure')
    user_query = data.get('query')
    sql_query = generate_sql(table_structure, user_query)
    return jsonify({'sql_query': sql_query})
