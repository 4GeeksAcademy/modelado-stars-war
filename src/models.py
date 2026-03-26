from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import ForeignKey

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

    nave: Mapped[List["Nave"]] = relationship(back_populates="user")
    arma: Mapped[List["Arma"]] = relationship(back_populates="user")
    favorite_arma: Mapped[List["Favorite_arma"]] = relationship(back_populates="user")

    favorite_nave: Mapped[List["Favorite_nave"]] = relationship(back_populates="user")
    

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
    dimension: Mapped[int] = mapped_column(nullable=False)
    favorite_nave: Mapped[List["Favorite_nave"]] = relationship(back_populates="nave")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="nave")
    
    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "description": self.description,
            # do not serialize the password, its a security breach
        }
    


class Arma(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    favorite_arma: Mapped[List["Favorite_arma"]] = relationship(back_populates="arma")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="arma")

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


class Favorite_arma(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="favorite_arma")

    arma_id: Mapped[int] = mapped_column(ForeignKey("arma.id"))
    arma: Mapped["Arma"] = relationship(back_populates="favorite_arma")

   

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class Favorite_nave(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="favorite_nave")

    nave_id: Mapped[int] = mapped_column(ForeignKey("nave.id"))
    nave: Mapped["Nave"] = relationship(back_populates="favorite_nave")
    
    
   

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }
