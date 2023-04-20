from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app, resources=r'/*')

list=[]
status={"food":"green","rubbish":"green"}

@app.route('/')
def test():
    return "test pass"

@app.route('/status', methods=["GET","POST"])
def getStatus():
    return status

@app.route('/food1', methods=["GET","POST"])
def food1():
    status['food']="green"
    return "good"

@app.route('/food2', methods=["GET","POST"])
def food2():
    status['food']="red"
    return "good"

@app.route('/rubbish1', methods=["GET","POST"])
def rubbish1():
    status['rubbish']="green"
    return "good"

@app.route('/rubbish2', methods=["GET","POST"])
def rubbish2():
    status['rubbish']="red"
    return "good"

@app.route('/get', methods=["GET","POST"])
def get():
    return jsonify(list)

@app.route('/take', methods=["POST"])
def take():
    date = (request.get_json())['date']
    fmt = '%Y/%m/%d %H:%M:%S'
    t= time.strptime(date, fmt)
    x= time.strftime("%Y-%m-%d %H:%M:%S",t)
    print("list:",list)
    print(" x",t)
    list.remove(x)
    return "good"


@app.route('/add', methods=["GET","POST"])
def add():
    list.append(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    return "Add Successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)