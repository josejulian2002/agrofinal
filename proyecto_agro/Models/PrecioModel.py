from base_de_datos import bd

class PrecioModel(bd.Model):
    __tablename__="t_precio"
    pre_id = bd.Column("pre_id",bd.Integer,primary_key=True)
    pre_fechin = bd.Column("pre_fechin",bd.DATETIME)
    pre_fechfin = bd.Column("pre_fechfin",bd.DATETIME)
    pre_precio = bd.Column("pre_precio",bd.DATETIME)
    prod_id = bd.Column(bd.Integer, bd.ForeignKey('t_producto.prod_id'), nullable=False)

    def __init__(self,fechin,fechfin,precio,prod_id):
        self.pre_precio=precio
        self.pre_fechfin=fechfin
        self.pre_fechin=fechfin
        self.prod_id=prod_id
