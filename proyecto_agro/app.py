from flask import Flask
from flask_restful import Api
from base_de_datos import bd

from Models import CategoriaModel,DetallePedidoModel,DisponibilidadModel,EstadoModel,ImagenProductoModel,PedidoModel,PrecioModel,ProductoModel,ProveedorModel,ProveedorProductoModel,TipoPagoModel,TipoTransporteModel,TipoUsuarioModel,TransporteModel,UbicacionModel,UnidadModel,UsuarioModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost/proyectoagro"
api = Api(app)

@app.route('/')
def inicio():
    return 'La API REST ha escuchado tus suplicas! 😀😱💩'

@app.before_first_request
def creacion_tablas():
    bd.init_app(app)
    # bd.drop_all(app=app)
    bd.create_all(app=app)

if __name__=="__main__":
    app.run(debug=True)

