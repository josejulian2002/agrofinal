from base_de_datos import bd

class PersonaPedido(bd.Model):
    __tablename__="t_ubicacion"
    ubi_id = bd.Column("ubi_id",bd.Integer,primary_key=True)
    ubi_dir=bd.Column("ubi_dir",bd.String(200))
    ubi_ciudad=bd.Column("ubi_ciudad",bd.String(45))
    ubi_lat=bd.Column("ubi_lat",bd.DECIMAL(10,2))
    ubi_lng=bd.Column("ubi_lng",bd.DECIMAL(10,2))
    usu_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)

    def __init__(self,direccion,ciudad,latitud,longitud,usu_id):
        self.ubi_lat=latitud
        self.ubi_lng=longitud
        self.ubi_ciudad=ciudad
        self.ubi_dir=direccion
        self.usu_id=usu_id
        