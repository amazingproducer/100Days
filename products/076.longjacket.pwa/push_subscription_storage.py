
# let's borrow some code and see how it can work for us!

import json
from flask import Flask
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# db is SQLAlchemy object
class Subscriber(db.Model):
    __tablename__ = 'subscriber'

    id = Column(Integer(), primary_key=True, default=None)
    created = Column(DateTime())
    modified = Column(DateTime())
    subscription_info = Column(Text())
    is_active = Column(Boolean(), default=True)

    @property
    def subscription_info_json(self):
        return json.loads(self.subscription_info)

    @subscription_info_json.setter
    def subscription_info_json(self, value):
        self.subscription_info = json.dumps(value)
