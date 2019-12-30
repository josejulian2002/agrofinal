from base_de_datos import bd

class UnidadModel(bd.Model):
    __tablename__="t_unidad"
    uni_id = bd.Column("uni_id",bd.Integer,primary_key=True)
    uni_nom=bd.Column("uni_nom",bd.String(50))
    uni_abr=bd.Column("uni_abr",bd.String(50))

    def __init__(self,nombre,abr):
        self.uni_nom=nombre
        self.uni_abr=abr