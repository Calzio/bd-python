import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
# Conexão com o banco de dados
# sqlite é menor, mais leve, tem segurança menor, servindo mais como um introdutorio
db = create_engine("sqlite:///meubanco.db")

# CREATE_DATABASE meubanco, caso queira mesclar banco de dados com backend, nesse caso não precisou porque o from sqlalchemy import create_engine, mais especifico o create_engine, como está na linha anterior faz isso

Session = sessionmaker(bind=db)
session = Session()

# I/O
# I = input(Entrada)
# O = output(Saída)

os.system("cls || clear")

# Criando tabela
Base = declarative_base()

class Usuario(Base):
    # Definindo nome da tabela
    __tablename__ = "usuarios"

    # Definindo atributos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)

# Salvar no banco de dados
#usuario = Usuario("Marta", "Marta@gmail.com", "123")
usuario = Usuario(senha="123", nome="Marta", email="marta@gmail.com")
session.add(usuario)
session.commit()

# Mostrar conteúdo do banco de dados
lista_usuario = session.query(Usuario).all()

for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")


# RAM
# Persistir - Banco de dados

# SGDB
# SQL - Relacionais
# Comandos criar Banco de dados, Tabelas...
# SELECT * FROM CLIENTES
# INSERT, CREATE TABLE, CREATE DATABASE...

# Backend - SQL

# ORM

# Metodo novo: pip install sqlalchemy

# ORM