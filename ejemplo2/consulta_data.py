from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Docente

from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de
# la entidad docentes
docentes = session.query(Docente).all() # [docente1, docente2, docente3]

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("Presentación de todos los Docentes")
for s in docentes:
    print("%s" % (s))
    print("---------")

# Obtener todos los registros de
# la tabla docentes que tengan como valor en
# el atributo especifico
docentes_dos = session.query(Docente).filter(Docente.ciudad=="Loja").all()
print(docentes_dos)

print("--------------------------------")

# Obtener todos los registros de·
# la tabla Docente ordenados por el atributo especifico
docentes_tres = session.query(Docente).order_by(Docente.nombre).all()
print(docentes_tres)


print("--------------------------------")
docentes = session.query(Docente).filter(Docente.ciudad=="Loja").order_by(Docente.nombre).all()
print(docentes)

print("--------------------------------")
docentes = session.query(Docente).filter(Docente.ciudad!=None).order_by(Docente.nombre).all()
print(docentes)

print("--------------------------------")
docentes = session.query(Docente).filter(Docente.ciudad=="Loja", Docente.nombre!=None).order_by(Docente.nombre).all()
print(docentes)


print("--------------------------------")
docentes = session.query(Docente).filter(Docente.ciudad.like("%oja%"), Docente.nombre!=None).order_by(Docente.nombre).all()
print(docentes)


print("--------------------------------")
# Uso de and_

docentes = session.query(Docente).filter(and_(Docente.ciudad.like("%oja%"), Docente.nombre!=None)).order_by(Docente.nombre).all()
print(docentes)

print("--------------------------------")
# Uso de in_

docentes = session.query(Docente).filter(Docente.apellido.in_(['Minga', 'Borrero'])).order_by(Docente.nombre).all()

print(docentes)

print("--------------------------------")
# Uso de or_

docentes = session.query(Docente).filter(or_(Docente.apellido=="Minga", Docente.apellido=="García")).order_by(Docente.nombre).all()

print(docentes)
