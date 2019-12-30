from base_de_datos import bd

class TipoTransporteModel(bd.Model):
    __tablename__="t_tipo_transporte"
    tipotran_id = bd.Column("tipotran_id",bd.Integer,primary_key=True)
    tipotran_nom=bd.Column("tipotran_nom",bd.String(50))
    tipotran_img=bd.Column("tipotran_img",bd.Text)

    def __init__(self,nombre,img):
        self.tipotran_nom=nombre
        self.tipotran_img=img