from base_de_datos import bd

class DetallePedidoModel(bd.Model):
    __tablename__="t_detalle_pedido"
    dped_id = bd.Column("dped_id",bd.Integer,primary_key=True)
    dped_desc=bd.Column("dped_desc",bd.String(100))
    dped_subtotal=bd.Column("dped_subtotal",bd.DECIMAL(10,2))
    dped_total=bd.Column("dped_total",bd.DECIMAL(10,2))
    dped_nro=bd.Column("dped_nro",bd.String(10))
    ped_id = bd.Column(bd.Integer, bd.ForeignKey('t_pedido.ped_id'), nullable=False)
    pre_id = bd.Column(bd.Integer, bd.ForeignKey('t_precio.pre_id'), nullable=False)

    def __init__(self,descripcion,subtotal,nro,total,ped_id,pre_id):
        self.dped_desc=descripcion
        self.dped_subtotal=subtotal
        self.dped_total=total
        self.dped_nro=nro
        self.ped_id=ped_id
        self.pre_id=pre_id