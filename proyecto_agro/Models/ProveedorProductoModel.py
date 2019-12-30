from base_de_datos import bd

class ProveedorProductoModel(bd.Model):
    __tablename__="t_proveedor_producto"
    provpro_id = bd.Column("provpro_id",bd.Integer,primary_key=True)
    prod_id = bd.Column(bd.Integer, bd.ForeignKey('t_producto.prod_id'), nullable=False)
    prov_id = bd.Column(bd.Integer, bd.ForeignKey('t_proveedor.prov_id'), nullable=False)

    def __init__(self,prod_id,prov_id):
        self.prod_id=prod_id
        self.prov_id=prov_id
        