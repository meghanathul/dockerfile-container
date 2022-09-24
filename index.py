from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>This is DockerContainer Project :)'



if __name__ == "__main__":

    app.run(port=5000)