from parse_history import Record
from parse import Person
from parse_place import Place
from app import db

db.drop_all()
print("Dropped")
db.create_all()
print("Created")
Person().generate()
print("Diplomats in the building")
Place().generate()
# Record().generate()
# print("Posts in the mail")
