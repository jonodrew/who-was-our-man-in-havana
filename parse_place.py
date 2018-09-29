from app import db
import json
from app.models import Country, Diplomat, Post

class Place:
    def __init__(self):
        self.data = json.loads(open("section_b.json").read())
        self.block_data = json.loads(open("section_a_locations.json").read())

    def is_place(self):
        pass

    def countries(self):
        data = json.loads(open("section_a_locations.json").read())
        country_names = set([data[i].get('country') for i in range(0, len(data))])
        country_names.remove(None)
        print(country_names)
        for c in country_names:
            db.session.add(Country(name=c))
        db.session.commit()

    def roles(self):
        data = json.loads(open("section_a_locations.json").read())
        return set([data[i].get('rs') for i in range(0, len(data))])

    def blocks(self):
        return [self.block_data[i] for i in range(0, len(self.block_data))]

    def generate(self):
        self.countries()
        for block in self.blocks():
            associated_diplomat = Diplomat.query.filter_by(key_name=block.get('persname')).first()
            associated_country = Country.query.filter_by(name=block.get('country')).first()
            p = Post(role=block.get('rs'), country=associated_country, diplomat=associated_diplomat)
            print(p.diplomat, p.country)
            db.session.add(p)
        db.session.commit()