from base_de_datos import bd

class UbicacionModel(bd.Model):
    __tablename__="t_ubicacion"
    ubi_id = bd.Column("ubi_id",bd.Integer,primary_key=True)
    ubi_ciud=bd.Column("ubi_ciud",bd.String(45))
    ubi_dir=bd.Column("ubi_dir",bd.String(200))
    ubi_lat=bd.Column("ubi_lat",bd.DECIMAL(10,8))
    ubi_lng=bd.Column("ubi_lng",bd.DECIMAL(10,8))
    ubi_refer=bd.Column("ubi_refer",bd.TEXT)
    usu_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)

    def __init__(self,ciudad,direccion,latitud,longitud,referencia,usu_id):
        self.ubi_ciud=ciudad
        self.ubi_dir=direccion
        self.ubi_lat=latitud
        self.ubi_lng=longitud
        self.ubi_refer=referencia
        self.usu_id=usu_id
