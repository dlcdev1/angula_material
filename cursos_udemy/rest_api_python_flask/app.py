from flask import Flask, render_template
from flask_restful import Api, Resource

from models.hotel import HotelModel
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.route('/')
def index():
    lista = {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}
    return render_template('lista.html', titulo='Hoteis', hoteis=lista['hoteis'])

@app.route('/novo')
def insert():
    return render_template('novo.html', titulo='Inserir novos hoteis')

# @app.before_first_request
# def cria_banco():
#     banco.create_all()
#     dados = Hotel.argumentos.parse_args()
#     hotel = HotelModel(hotel_id, **dados)

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)