from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    response = supabase.table('your_table_name').insert(data).execute()
    return jsonify(response.data), response.status_code

@app.route('/get', methods=['GET'])
def get_data():
    response = supabase.table('your_table_name').select('*').execute()
    return jsonify(response.data), response.status_code

if __name__ == '__main__':
    app.run(debug=True)