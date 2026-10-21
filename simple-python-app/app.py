from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>Hello, World!</h1>
    <p>Welcome to my AWS CI/CD project.</p>
    <p>Containerized using Docker. this is a new line added here </p>
    <p>Deployed locally using Docker Desktop. didn't yet deployed to any cd platform for deploy</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
