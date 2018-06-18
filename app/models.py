from app import db


class Dinner(db.Model):

    __tablename__ = "dinner"

    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return "Dinner {}'".format(self.id)

    def __str__(self):
        return "Dinner {} {}".format(self.size, self.date)

