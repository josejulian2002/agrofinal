from base_de_datos import bd

class ProveedorModel(bd.Model):
    __tablename__="t_proveedor"
    prov_id = bd.Column("prov_id",bd.Integer,primary_key=True)
    prov_nom=bd.Column("prov_nom",bd.String(45))
    prov_ape=bd.Column("prov_ape",bd.String(50))
    prov_fono=bd.Column("prov_fono",bd.String(20))
    prov_dir=bd.Column("prov_dir",bd.String(200))

    def __init__(self,nombre,apellido,fono,direccion):
        self.prov_nom=nombre
        self.prov_ape=apellido
        self.prov_fono=fono
        self.prov_dir=direccion
        