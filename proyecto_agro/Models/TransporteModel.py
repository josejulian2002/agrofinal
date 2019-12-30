from base_de_datos import bd

class TransporteModel(bd.Model):
    __tablename__="t_transporte"
    tran_id = bd.Column("tran_id",bd.Integer,primary_key=True)
    tran_nom=bd.Column("tran_nom",bd.String(45))
    tran_ape=bd.Column("tran_ape",bd.String(50))
    tran_fono=bd.Column("tran_fono",bd.String(20))
    tran_placa=bd.Column("tran_placa",bd.String(200))
    tipotran_id = bd.Column(bd.Integer, bd.ForeignKey('t_tipo_transporte.tipotran_id'), nullable=False)

    def __init__(self,nombre,apellido,fono,placa,tipotran_id):
        self.tran_nom=nombre
        self.tran_ape=apellido
        self.tran_fono=fono
        self.tran_placa=placa
        self.tran_id=tipotran_id
        