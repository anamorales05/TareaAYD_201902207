from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/calc/<NUM>+<NUM2>',methods=['POST'])
def calc(NUM,NUM2):
    var = int(NUM)+int(NUM2)
    return str(var)
    
if __name__=='__main__':
    app.run(debug=False,port=3000)