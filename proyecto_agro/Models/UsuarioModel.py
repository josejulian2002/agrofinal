from base_de_datos import bd
import bcrypt

class UsuarioModel(bd.Model):
    __tablename__="t_usuario"
    usu_id = bd.Column("usu_id",bd.Integer,primary_key=True)
    usu_mail = bd.Column("usu_mail",bd.String(50))
    usu_salt=bd.Column("usu_salt",bd.Text)
    usu_hash=bd.Column("usu_hash",bd.Text)
    usu_nom=bd.Column("usu_nom",bd.String(45))
    usu_ape=bd.Column("usu_ape",bd.String(50))
    usu_fono=bd.Column("usu_fono",bd.String(20))
    tipousu_id=bd.Column(bd.Integer,bd.ForeignKey('t_tipo_usuario.tipousu_id'),nullable=False)

    def __init__(self,correo,password,nombre,apellido,fono,tipousu_id):
        self.usu_mail=correo
        password_convertida= bytes(password,'utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_convertida,salt)
        salt = salt.decode('utf-8')
        hashed = hashed.decode('utf-8')
        self.usu_salt=salt
        self.usu_hash=hashed
        self.usu_nom=nombre
        self.usu_ape=apellido
        self.usu_fono=fono
        self.tipousu_id=tipousu_id