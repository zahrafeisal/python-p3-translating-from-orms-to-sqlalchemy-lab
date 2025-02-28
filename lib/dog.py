from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    pass

def get_all(session):
    return [dog for dog in session.query(Dog)]
    pass

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(f'%{name}%')).first()
    pass

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.like(f'%{id}%')).first()
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name.like(f'%{name}%'), Dog.breed.like(f'%{breed}%')).first()
    pass

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})
    pass