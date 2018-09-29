import csv
from app.models import Diplomat, Post
from app import db


class Record:
    def __init__(self):
        self.data = csv.reader(open("history.tsv", 'rt'), delimiter='\t')

    def generate(self):
        for record in self.data:
            associated_diplomat = Diplomat.query.filter_by(key_name=record[0]).first()
            p = Post(role=record[3], diplomat=associated_diplomat)
            db.session.add(p)
        print("All posts added to session")
        db.session.commit()

