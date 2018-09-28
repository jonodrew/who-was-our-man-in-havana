from app import db


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://power_user:FCO2018@ec2-35-178-22-37.eu-west-2.compute.amazonaws.com:5432/FCO2018'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class Diplomat(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)
    posts = db.relationship('Post', backref='diplomat', lazy=True)

    def __repr__(self):
        return '<Diplomat {}>'.format(self.name)

class Post(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(150), unique=False, nullable=True)
    diplomat_id = db.Column(db.Integer, db.ForeignKey('diplomat.uid'),
        nullable=False)

    ## TODO: repr
    def __repr__(self):
        return '<Post {}>'.format(self.role)

class Country(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    capital_city = db.Column(db.String(150), nullable=True)
    name = db.Column(db.String(150), nullable=False, unique=True)

    ## TODO: repr