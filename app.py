from flask import Flask, request, jsonify
from supabase import create_client
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route('/', methods=['GET'])
def hello_world():
    response = "hello world"
    return response

@app.route('/messages', methods=['GET'])
def get_data():
    response = supabase.table('your_table_name').select('*').execute()
    return jsonify(response.data)

@app.route('/add_message', methods=['POST'])
def add_data():
    data = request.json
    response = supabase.table('your_table_name').insert(data).execute()
    return jsonify(response.data)


if __name__ == '__main__':
    app.run(debug=True)