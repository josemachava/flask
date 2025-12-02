from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World flask api!'

@app.route('/new')
def hello_world():  # put application's code here
    return 'Hello new route flask api!'

@app.route('/new/here')
def hello_world():  # put application's code here
    return 'Hello new route flask api!'

if __name__ == '__main__':
    app.run()
