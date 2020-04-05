from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Market(db.Model):
    """Market"""

    # Create market table 
    ___tablename__ = "markets"

    market_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    homepage_url = db.Column(db.String(100), unique=True)
    funding_total_usd = db.Column(db.Integer)
    status = db.Column(db.String(20))
    country_code = db.Column(db.String(10))
    city = db.Column(db.String(20))
    funding_rounds = db.Column(db.Integer)
    founded_at = db.Column(db.String(20))
    founded_year = db.Column(db.Integer)
    first_funding_at = db.Column(db.Integer)
    last_funding_at = db.Column(db.Integer)


    def __repr__(self):
        """Provide helpful representation when printing"""

        return f'<Market market_id={self.market_id}\
                    homepage_url={self.homepage_url} \
                    funding_total_usd={self.funding_total_usd}\
                    status={self.status}\
                    country_code={self.country_code}\
                    city={self.city}\
                    funding_rounds={self.funding_rounds}\
                    founded_at={self.founded_at}\
                    founded_year={self.founded_year}\
                    first_funding_at={self.first_funding_at}\
                    last_funding_at={self.last_funding_at}\
                    >'













def connect_to_db(app):
    """Connect the database to the Flask app"""
    # Configure to use the Postgres SQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///marketdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
    

if __name__ == "__main__":
    # As a convenience, if you run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print("Connected to DB.")