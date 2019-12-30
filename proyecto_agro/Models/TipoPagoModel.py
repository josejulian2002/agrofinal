from base_de_datos import bd

class TipoPagoModel(bd.Model):
    __tablename__="t_tipo_pago"
    tipopa_id = bd.Column("tipopa_id",bd.Integer,primary_key=True)
    tipopa_nom=bd.Column("tipopa_nom",bd.String(200))
    tipopa_est=bd.Column("tipopa_est",bd.BOOLEAN)
    

    def __init__(self,nombre,estado):
        self.tipopa_nom=nombre
        self.tipopa_est=estado
        