from base_de_datos import bd

class EstadoModel(bd.Model):
    __tablename__="t_estado"
    est_id = bd.Column("est_id",bd.Integer,primary_key=True)
    est_nom=bd.Column("est_nom",bd.String(50))

    def __init__(self,nombre):
        self.est_nom=nombre