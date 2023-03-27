#Motor para conectarnos a la base de datos
#ORM 
import sqlalchemy as db
import persistence.modelos as mod

#Codigo para crear la tabla en Mysql, debes haber creado la base de datos con anticipacion
engine = db.create_engine('mysql+pymysql://root:@localhost:3306/bd_energy_login', echo=True, future=True)

#engine = db.create_engine("mysql://root:''@localhost:3306", echo=True, future=True)
#engine.execute("CREATE DATABASE db_energy_login") #create db
#engine.execute("USE db_energy_login")
mod.Base.metadata.create_all(engine)
