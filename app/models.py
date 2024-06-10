from .extensions import db

class Cliente(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    razao = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(140), unique=True, nullable=False)

    def __repr__(self):
        return f'<Cliente {self.razao}>'
