from base_de_datos import bd

class ProductoModel(bd.Model):
    __tablename__="t_producto"
    prod_id = bd.Column("prod_id",bd.Integer,primary_key=True)
    prod_nom = bd.Column("prod_nom",bd.String(40))
    prod_desc = bd.Column("prod_desc",bd.String(40))
    cat_id = bd.Column(bd.Integer, bd.ForeignKey('t_categoria.cat_id'), nullable=False)
    dispo_id=bd.Column(bd.Integer,bd.ForeignKey('t_disponibilidad.dispo_id'),nullable=False)

    def __init__(self,nombre,descripcion,cat_id,dispo_id):
        self.prod_nom=nombre
        self.prod_desc=descripcion
        self.cat_id=cat_id
        self.dispo_id=dispo_id
        
