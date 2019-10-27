# let's borrow some code and see how it can work for us!

import os
import datetime
from flask import Flask, json, jsonify, request, send_file, send_from_directory
from pywebpush import webpush, WebPushException
#from push_subscription_storage import Subscriber
#from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from flask_sqlalchemy import SQLAlchemy
#Column, Integer, String, Text, DateTime, Boolean
import logging

WEBPUSH_VAPID_PRIVATE_KEY = str(os.environ.get("LJ_PUSH_PRIVKEY"))
vapid_claim_string = json.load(open('./claim.json'))
WEBPUSH_VAPID_PUBLIC_KEY = "BNAVJ63X40KbUEzSXqSW1C7Md9lcpj5TJF9Yk2_1hiaobNmk4Zx5HTcZ4wX-E4m_3gGdvUzz5MQROGDo8MiCr2Q"
print(vapid_claim_string)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///push_subscriptions.db'
db = SQLAlchemy(app)


class Subscriber(db.Model):
    db.__tablename__ = 'subscriber'

    id = db.Column(db.Integer(), primary_key=True, default=None)
    created = db.Column(db.DateTime())
    modified = db.Column(db.DateTime())
    subscription_info = db.Column(db.Text())
    is_active = db.Column(db.Boolean(), default=True)

    @property
    def subscription_info_json(self):
        return json.loads(self.subscription_info)

    @subscription_info_json.setter
    def subscription_info_json(self, value):
        self.subscription_info = json.dumps(value)

#    def __init__(self, **kwargs):
#        name = self.__tablename__
#        db.drop_all()
#        db.create_all()
#        db.session.commit()
#        super().__init__(**kwargs)

@app.route('/<file>')
def flask_root(file='./index.html'):
    return send_file(file)

@app.route('/')
def index():
    return send_file('./index.html')

@app.route('/api/subscribe', methods=['POST'])
def subscribe():
    print(f"Got request! {request.json.get('subscription_info')}")
#    if request.json:
#        print(f"Request received: {request.json}")
    subinfo = request.json.get('subscription_info')
    print(f"subinfo is {type(subinfo)}")
    subscription_info = request.json.get('subscription_info')
    print(f"Requester's info: {subscription_info}")
    # if is_active=False == unsubscribe
    is_active = request.json.get('is_active')
    print(f"Subscriber info type: {type(Subscriber.query.filter(Subscriber.subscription_info ==  str(subscription_info)))}")
    print(f"Subscriber info: {db.session.query(Subscriber).filter(Subscriber.subscription_info==str(subscription_info)).first()}")
    # we assume subscription_info shall be the same
    item = db.session.query(Subscriber).filter(Subscriber.subscription_info==str(subscription_info)).first()
#    print(f"Subscriber's info: {Subscriber.subscription_info}")
    print(f"Requester's info: {subscription_info}")
    if not item:
        item = Subscriber()
        item.created = datetime.datetime.utcnow()
        print("Adding requester as new subscriber...")
        item.subscription_info = str(subscription_info)

    item.is_active = is_active
    item.modified = datetime.datetime.utcnow()
    db.session.add(item)
    db.session.commit()

    return jsonify({"data": {"success": True }})

@app.route('/notify', methods=['POST', 'GET'])
def notify():
    items = Subscriber.query.filter(Subscriber.is_active == True).all()
    print(f"items: {str(items)}")
    [print(type(i.is_active), i.is_active) for i in Subscriber.query.all()]
    count = 0
    print(f"pushing with private key: {WEBPUSH_VAPID_PRIVATE_KEY}")
    print(f"pushing with VAPID claims: {vapid_claim_string}")
    for item in items:
        try:
            webpush(
                subscription_info=json.loads(item.subscription_info.replace("\'", "\"")),
                data="Investigate sea monster at: lat:19.759 lng:-154.9845",
                vapid_private_key=WEBPUSH_VAPID_PRIVATE_KEY,
                vapid_claims=vapid_claim_string
            )
            count += 1
        except WebPushException as ex:
            print("i am too lazy to look at the log for webpush failures right now")
            logging.exception("webpush fail")

    print(f"{Subscriber.query.all()}")
    return "{} notification(s) sent".format(count)

if __name__ == "__main__":
    db.__tablename__ = 'subscriber'

    id = db.Column(db.Integer(), primary_key=True, default=None)
    created = db.Column(db.DateTime())
    modified = db.Column(db.DateTime())
    subscription_info = db.Column(db.Text())
    is_active = db.Column(db.Boolean(), default=True)
    db.drop_all()
    db.create_all()
    db.session.commit()
    app.run(host='0.0.0.0', ssl_context='adhoc')
