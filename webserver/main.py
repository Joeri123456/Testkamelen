from flask import Flask
from flask import render_template
from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route("/me")
def me_api():
    user = {'username': 'joeri de beste', 'theme': 'appelsap', 'image': 'plaatje.jpg'}
    return {
        "username": user['username'],
        "theme": user['theme'],
        "image": user['image']
    }

@app.route('/test2main/')
def test2main(name=None):
    return render_template('test2.html')

@app.route('/test2', methods=['GET'])
def test2():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'jack': 4098, 'sape': 4139}
    print(jsonResp)
    return jsonify(jsonResp)
