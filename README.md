# Flask Supabase Template

This is a basic template for a Flask application that connects to Supabase.

## Getting Started

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-supabase-template.git
    cd flask-supabase-template
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Rename `.env.sample` to `.env` and enter your Supabase API keys:
    ```sh
    mv .env.sample .env
    ```

5. Run the Flask application:
    ```sh
    python3 app.py
    ```


## Tutorial for students connecting to Supabase

- download Postman and make an account
- make an account on Supabase.com
- create a new project on Supabase
    - name it
    - create a DB password and save it somewhere
    - use default Region
    - in Security, disable RLS  (row level security)
    - use defaults everywhere else
- git clone the code:
    - https://github.com/smithwithatypo/flask-supabase-template
    - change API keys to your Supabase credentials. Find this info on your Supabase project’s Home tab:
        - “Project URL” is your “SUPABASE_URL”
        - “API Key” is your “SUPABASE_KEY”
- in Supabase, go to the Table Editor tab, then create a new table
    - name it “your_table_name”
    - add one column named “message”, then set the Type to “text”
    - ![create table](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/create_table.png)
    - ![add column](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/add_column.png)

- start your Flask app
    - in your terminal, in that directory
        - $ python -m venv venv
        - source venv/bin/activate
        - pip install -r requirements.txt
        - python app.py
- in Postman, send a GET request to the root directory
    - url == “http://127.0.0.1:5000/”
    - ![get postman](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/GET_postman.png)
- in Postman, send a POST request to add a message
    - url == “http://127.0.0.1:5000/add_message”
    - click POST, change your url, click “raw” radio button, click “JSON” from dropdown menu
    - send a JSON:
        - each attribute matches your column names in your table
        - “id” and “created_at” columns will auto-fill with data
        - { “message”: “hello” }
        - ![post raw json](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/POST_raw_json.png)
        - ![post success](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/POST_success.png)
        - ![post supabase](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/POST_supabase.png)
- in Postman, send a GET request to “/message” to see all your messages
    - url == “http://127.0.0.1:5000/messages”
    - select “none” for your Body
    - ![get messages](https://github.com/smithwithatypo/flask-supabase-template/blob/main/images/GET_messages.png)

- Resources
    - Supabase docs:  https://supabase.com/docs/reference/python