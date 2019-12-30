from base_de_datos import bd

class DisponibilidadModel(bd.Model):
    __tablename__="t_disponibilidad"
    dispo_id = bd.Column("dispo_id",bd.Integer,primary_key=True)
    dispo_est=bd.Column("dispo_est",bd.BOOLEAN)
    dispo_can=bd.Column("dispo_can",bd.DECIMAL(10,2))
    uni_id = bd.Column(bd.Integer, bd.ForeignKey('t_unidad.uni_id'), nullable=False)
   
    def __init__(self,estado,cantidad,unidad):
        self.dispo_est=estado
        self.dispo_can=cantidad
        self.uni_id=unidad


