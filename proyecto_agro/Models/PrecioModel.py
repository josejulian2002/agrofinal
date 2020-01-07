from base_de_datos import bd

class PrecioModel(bd.Model):
    __tablename__="t_precio"
    pre_id = bd.Column("pre_id",bd.Integer,primary_key=True)
    pre_fechin = bd.Column("pre_fechin",bd.DATETIME)
    pre_fechfin = bd.Column("pre_fechfin",bd.DATETIME)
    pre_precio = bd.Column("pre_precio",bd.DATETIME)

    def __init__(self,fechin,fechfin,precio):
        self.pre_precio=precio
        self.pre_fechfin=fechfin
        self.pre_fechin=fechfin
