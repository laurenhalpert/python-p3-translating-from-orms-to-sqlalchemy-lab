from models import Dog


def create_table(base, engine):
    
    base.metadata.create_all(engine)
    

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    all_dogs= session.query(Dog)
    return [dog for dog in all_dogs]

def find_by_name(session, name):
    query= session.query(Dog).filter(Dog.name.like(f'%{name}%')).all()
    for record in query:
        return record

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).all()
    for record in query:
        return record

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).all()
    for record in query:
        return record

def update_breed(session, dog, breed):
    query = session.query(Dog).update({
        Dog.breed: breed
    })
    return dog