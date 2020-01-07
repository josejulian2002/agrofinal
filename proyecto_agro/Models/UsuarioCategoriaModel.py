from base_de_datos import bd

class UsuarioCategoriaModel(bd.Model):
    __tablename__="t_usuario_categoria"
    usucat_id= bd.Column("usucat_id",bd.Integer,primary_key=True)
    usu_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)
    cat_id = bd.Column(bd.Integer, bd.ForeignKey('t_categoria.cat_id'), nullable=False)
    
    def __init__(self,usuario,categoria):
        self.usu_id=usuario
        self.cat_id=categoria    
        