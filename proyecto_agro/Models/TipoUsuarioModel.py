from base_de_datos import bd

class TipoUsuarioModel(bd.Model):
    __tablename__="t_tipo_usuario"
    tipousu_id = bd.Column("tipousu_id",bd.Integer,primary_key=True)
    tipousu_nom=bd.Column("tipousu_nom",bd.String(50))

    def __init__(self,nombre,img):
        self.tipousu_nom=nombre