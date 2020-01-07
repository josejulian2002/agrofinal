from base_de_datos import bd

class ChatModel(bd.Model):
    __tablename__="t_chat"
    chat_id = bd.Column("chat_id",bd.Integer,primary_key=True)
    chat_text=bd.Column("chat_text",bd.Text)
    admin_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)
    cli_id = bd.Column(bd.Integer, bd.ForeignKey('t_usuario.usu_id'), nullable=False)

    def __init__(self,texto,admin,client):
       self.chat_text=texto
       self.cli_id=client
       self.admin_id=admin