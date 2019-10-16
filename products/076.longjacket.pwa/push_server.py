# let's borrow some code and see how it can work for us!

import os
import datetime
from flask import Flask, json, jsonify, request
from pywebpush import webpush, WebPushException
from push_subscription_storage import Subscriber

WEBPUSH_VAPID_PRIVATE_KEY = str(os.environ.get("LJ_PUSH_PRIVKEY"))
vapid_claims = json.load(open('./claim.json'))
WEBPUSH_VAPID_PUBLIC_KEY = "BNAVJ63X40KbUEzSXqSW1C7Md9lcpj5TJF9Yk2_1hiaobNmk4Zx5HTcZ4wX-E4m_3gGdvUzz5MQROGDo8MiCr2Q"
print(vapid_claims)
app = Flask(__name__)
@app.route('/api/subscribe')
def subscribe():
    subscription_info = request.json.get('subscription_info')
    # if is_active=False == unsubscribe
    is_active = request.json.get('is_active')

    # we assume subscription_info shall be the same
    item = Subscriber.query.filter(Subscriber.subscription_info == subscription_info).first()
    if not item:
        item = Subscriber()
        item.created = datetime.datetime.utcnow()
        item.subscription_info = subscription_info

    item.is_active = is_active
    item.modified = datetime.datetime.utcnow()
    db.session.add(item)
    db.session.commit()

    return jsonify({ id: item.id })

@app.route('/notify')
def notify():
    items = Subscriber.query.filter(Subscriber.is_active == True).all()
    count = 0
    for _item in items:
        try:
            webpush(
                subscription_info=_item.subscription_info_json,
                data="Test 123",
                vapid_private_key=WEBPUSH_VAPID_PRIVATE_KEY
                #vapid_claims={
                #    "sub": "mailto:webpush@mydomain.com"
                #}
            )
            count += 1
        except WebPushException as ex:
            logging.exception("webpush fail")


    return "{} notification(s) sent".format(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context='adhoc')
