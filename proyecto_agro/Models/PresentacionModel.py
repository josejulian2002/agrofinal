from base_de_datos import bd

class PresentacionModel(bd.Model):
    __tablename__="t_presentacion"
    pres_id = bd.Column("pres_id",bd.Integer,primary_key=True)
    pres_est=bd.Column("pres_est",bd.BOOLEAN)
    pres_can=bd.Column("pres_can",bd.DECIMAL(10,2))
    pres_uni=bd.Column("pres_uni",bd.String(30))
    pre_id = bd.Column(bd.Integer, bd.ForeignKey('t_precio.pre_id'), nullable=False)
    provpro_id = bd.Column(bd.Integer, bd.ForeignKey('t_proveedor_producto.provpro_id'), nullable=False)
   
    def __init__(self,estado,cantidad,unidad,pre_id,provpro_id):
        self.pres_est=estado
        self.pres_can=cantidad
        self.pres_uni=unidad
        self.pre_id=pre_id
        self.provpro_id=provpro_id


