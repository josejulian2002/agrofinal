from base_de_datos import bd

class AlmacenModel(bd.Model):
    __tablename__="t_almacen"
    alm_id = bd.Column("alm_id",bd.Integer,primary_key=True)
    alm_cap=bd.Column("alm_cap",bd.String(200))
    alm_est=bd.Column("alm_est",bd.BOOLEAN)
    alm_lat=bd.Column("alm_lat",bd.DECIMAL(10,2))
    alm_lng=bd.Column("alm_lng",bd.DECIMAL(10,2))
    provpro_id = bd.Column(bd.Integer, bd.ForeignKey('t_proveedor_producto.provpro_id'), nullable=False)
    
    def __init__(self,capacidad,estado,lat,lng,provpro_id):
        self.alm_cap=capacidad
        self.alm_est=estado
        self.alm_lat=lat
        self.alm_lng=lng
        self.provpro_id=provpro_id
        
        