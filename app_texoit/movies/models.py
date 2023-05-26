from app_texoit import db


class Movie(db.Model):
    __tablename__= 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    studios = db.Column(db.String(100), nullable=False)
    producers = db.Column(db.Text(100), nullable=False)
    winner = db.Column(db.String(3), nullable=True)

