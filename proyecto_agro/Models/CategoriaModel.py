from base_de_datos import bd

class CategoriaModel(bd.Model):
    __tablename__="t_categoria"
    cat_id = bd.Column("cat_id",bd.Integer,primary_key=True)
    cat_nom=bd.Column("cat_nom",bd.String(50))

    def __init__(self,nombre):
        self.cat_nom=nombre
        

