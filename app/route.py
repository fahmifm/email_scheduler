from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Emails, Recipients
from app import db
from werkzeug.exceptions import BadRequest

# Blueprint init
data = Blueprint('data', __name__)


# Error handler
@data.errorhandler(BadRequest)
def handle_bad_request(e):
    response = {
        "status_code": 400,
        "message": "Failed, bad query params",
    }

    return jsonify(response), 400


# endpoint for add email
@data.route('/save_email', methods=['POST'])
def save_email():
    req_data = request.form

    # check request with params
    if req_data:
        event_id = req_data['event_id']
        email_subject = req_data['email_subject']
        email_content = req_data['email_content']
        timestamp = datetime.strptime(req_data['timestamp'], '%d-%m-%Y %H:%M')

        emails = Emails(event_id=event_id, email_subject=email_subject, email_content=email_content, timestamp=timestamp)
        db.session.add(emails)
        db.session.commit()
        print(event_id, email_subject, email_content, timestamp)
    else:
        raise BadRequest()

    response = {
        "status_code": 200,
        "message": "successful",
    }

    return jsonify(response)


# endpoint to add recipient
@data.route('/add_recipient', methods=['POST'])
def add_recipient():
    req_data = request.form

    # check request with params
    if req_data:
        email_address = req_data['email_address']
        event_id = req_data['event_id']
        recipients = Recipients(event_id=event_id, email_address=email_address)
        db.session.add(recipients)
        db.session.commit()
        print(event_id, email_address)
    else:
        raise BadRequest()

    response = {
        "status_code": 200,
        "message": "successful",
    }

    return jsonify(response)