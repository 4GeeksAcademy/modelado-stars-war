from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

 
class Nave(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    dimension: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(primary_key=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "description": self.description,
            "tidimensionpo": self.dimension,
            # do not serialize the password, its a security breach
        }
    


class Arma(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(primary_key=True)
    id_nave: Mapped[int] = mapped_column(primary_key=True)
    

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
    

class Location(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planet: Mapped[str] = mapped_column(nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "planet": self.planet,
            # do not serialize the password, its a security breach
        }


class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(primary_key=True)
    id_nave: Mapped[int] = mapped_column(primary_key=True)
    id_location: Mapped[int] = mapped_column(primary_key=True)
    id_arma: Mapped[int] = mapped_column(primary_key=True)
   

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
