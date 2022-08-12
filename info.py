from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/info',methods=['GET'])
def info():
    return "Ana Lucia Morales Gonzalez 201902207"

if __name__=='__main__':
    app.run(debug=False,port=4000)