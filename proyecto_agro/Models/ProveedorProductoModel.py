from base_de_datos import bd

class ProveedorProductoModel(bd.Model):
    __tablename__="t_proveedor_producto"
    provpro_id = bd.Column("provpro_id",bd.Integer,primary_key=True)
    provpro_cant=bd.Column("provpro_cant",bd.DECIMAL(10,2))
    provpro_preciocompra=bd.Column("provpro_preciocompra",bd.DECIMAL(10,2))
    prod_id = bd.Column(bd.Integer, bd.ForeignKey('t_producto.prod_id'), nullable=False)
    prov_id = bd.Column(bd.Integer, bd.ForeignKey('t_proveedor.prov_id'), nullable=False)


    def __init__(self,cantidad,preciocompra,prod_id,prov_id):
        self.provpro_cant=cantidad
        self.provpro_preciocompra=preciocompra
        self.prod_id=prod_id
        self.prov_id=prov_id
        