from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    return 'Hello World!'


@app.route('/ping/', methods=['GET'])
def ping() -> str:
    return 'Pong!'


if __name__ == '__main__':
    print('Server run')
    app.run(host='0.0.0.0', port=8080)
