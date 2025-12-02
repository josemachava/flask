from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello eusebio custom domain is dope this is custom domain!'

@app.route('/new')
def world_hello():  # put application's code here
    return 'Hello new route flask api!'

@app.route('/deployment')
def world():  # put application's code here
    return 'Hello new route flask api!'

@app.route('/new/here')
def helloworld():  # put application's code here
    return 'Hello new route flask api!'

if __name__ == '__main__':
    app.run()
