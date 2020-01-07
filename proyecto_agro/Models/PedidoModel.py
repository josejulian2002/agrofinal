from base_de_datos import bd

class PedidoModel(bd.Model):
    __tablename__="t_pedido"
    ped_id = bd.Column("ped_id",bd.Integer,primary_key=True)
    ped_fechin = bd.Column("ped_fechin",bd.DATETIME)
    ped_fechfin = bd.Column("ped_fechfin",bd.DATETIME)
    est_id = bd.Column(bd.Integer, bd.ForeignKey('t_estado.est_id'), nullable=False)
    usu_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)
    tran_id = bd.Column(bd.Integer, bd.ForeignKey('t_transporte.tran_id'), nullable=False)
    tipopa_id = bd.Column(bd.Integer, bd.ForeignKey('t_tipo_pago.tipopa_id'), nullable=False)


    def __init__(self,fechin,fechfin,pre_id,est_id,usu_id,dped_id,tran_id,tipopa_id):
        self.ped_fechin=fechin
        self.ped_fechfin=fechfin
        self.pre_id=pre_id
        self.est_id=est_id
        self.dped_id=dped_id
        self.usu_id=usu_id
        self.tran_id=tran_id
        self.tipopa_id=tipopa_id