import os

from flask import Flask
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
user = os.getenv('DB_USER')
print(f'user - {user}')


@app.route('/', methods=['GET'])
def hello_world() -> str:
    return 'Hello World!'


@app.route('/ping/', methods=['GET'])
def ping() -> str:
    return 'Pong!'


@app.route('/write/', methods=['GET'])
def write() -> str:
    try:
        with open('data/data.txt', 'w') as file:
            file.write('Hello')

        return 'Done'
    except Exception as err:
        return str(err)


if __name__ == '__main__':
    print('Server run')
    app.run(host='0.0.0.0', port=8080)
