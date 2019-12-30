from base_de_datos import bd

class ProductoModel(bd.Model):
    __tablename__="t_pedido"
    ped_id = bd.Column("ped_id",bd.Integer,primary_key=True)
    ped_fechin = bd.Column("ped_fechin",bd.DATETIME)
    ped_fechfin = bd.Column("ped_fechfin",bd.DATETIME)
    ped_can = bd.Column("ped_can",bd.DECIMAL(10,2))
    ped_total = bd.Column("ped_total",bd.DECIMAL(10,2))
    pre_id = bd.Column(bd.Integer, bd.ForeignKey('t_precio.pre_id'), nullable=False)
    est_id = bd.Column(bd.Integer, bd.ForeignKey('t_estado.est_id'), nullable=False)
    uni_id = bd.Column(bd.Integer, bd.ForeignKey('t_unidad.uni_id'), nullable=False)
    usu_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)
    tran_id = bd.Column(bd.Integer, bd.ForeignKey('t_transporte.tran_id'), nullable=False)
    tipopa_id = bd.Column(bd.Integer, bd.ForeignKey('t_tipo_pago.tipopa_id'), nullable=False)


    def __init__(self,fechin,fechfin,cantidad,total,pre_id,est_id,uni_id,usu_id,dped_id,tran_id,tipopa_id):
        self.ped_fechin=fechin
        self.ped_fechfin=fechfin
        self.ped_can=cantidad
        self.ped_total=total
        self.pre_id=pre_id
        self.est_id=est_id
        self.uni_id=uni_id
        self.dped_id=dped_id
        self.usu_id=usu_id
        self.tran_id=tran_id
        self.tipopa_id=tipopa_id