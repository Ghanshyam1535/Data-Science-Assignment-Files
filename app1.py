from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return '''Company Name: ABC Corporation 
              Location: India 
              Contact Detail: 999-999-9999'''

if __name__ == '__main__':
    app.run(host="0.0.0.0")


