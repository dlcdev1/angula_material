from flask import Flask
from flask_restful import Api

app = Flask(__name__)

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)