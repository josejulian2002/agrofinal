from base_de_datos import bd

class ImagenProductoModel(bd.Model):
    __tablename__="t_imagen_producto"
    imgprod_id = bd.Column("imgprod_id",bd.Integer,primary_key=True)
    imgprod_url = bd.Column("imgprod_url",bd.Text)
    prod_id = bd.Column(bd.Integer, bd.ForeignKey('t_producto.prod_id'), nullable=False)

    def __init__(self,url,prod_id):
        self.imgprod_url=url
        self.prod_id=prod_id