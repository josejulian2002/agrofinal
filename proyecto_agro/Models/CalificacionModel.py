from base_de_datos import bd

class CalificacionModel(bd.Model):
    __tablename__="t_calificacion"
    cal_id = bd.Column("cal_id",bd.Integer,primary_key=True)
    cal_estr=bd.Column("cal_estr",bd.Integer)
    pre_id = bd.Column(bd.Integer, bd.ForeignKey('t_precio.pre_id'), nullable=False)
    ped_id = bd.Column(bd.Integer, bd.ForeignKey('t_pedido.ped_id'), nullable=False)
    
    def __init__(self,estr,pre_id,ped_id):
        self.cal_estr=estr
        self.pre_id=pre_id
        self.ped_id=ped_id
        