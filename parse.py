import xmltodict
import csv
from typing import List
from app.models import Diplomat
from app import db
import re


class Person:

    def __init__(self):
        self.data = Person.data()

    @staticmethod
    def data():
        return csv.reader(open("ambassadors.csv", 'rt'))

    def birth_year(self, value: str):
        if value == "":
            year = None
        else:
            year = value[0:4]
        try:
            return self.validate_year(year)
        except ValueError:
            pass

    def death_year(self, value: str):
        if value == "" or value[-1] == "-":
            year = None
        else:
            year = value[-4:]
        return year

    def validate_year(self, value):
        regexp = re.compile('(-|_)')
        if isinstance(value, str):
            return(int(regexp.sub('0', value)))
        else:
            return value

    def generate(self):
        diplomats = [Diplomat(name=line[3], birth_year=Person().birth_year(line[2]), key_name=line[4]) for line in
                     Person.data()]
        diplomats.pop(0)
        print("here")
        for d in diplomats:
            print(d.birth_year)
            db.session.add(d)
        print("All added, total count {}".format(len(diplomats)))
        db.session.commit()
