import celery
from datetime import datetime, timedelta
from .db_conn import Session, Emails, Recipients
from app.util import Util

util = Util()

@celery.task
def check_email():
    session = Session()
    logger = check_email.get_logger()
    logger.info("Check email")
    now = datetime.now().replace(second=0, microsecond=0)
    data = session.query(Emails.email_subject, Emails.email_content, Recipients.email_address)\
        .join(Recipients, Emails.event_id == Recipients.event_id)\
        .filter(Emails.timestamp.between(
            now, now+timedelta(minutes=1)))
    for i in data:
        print(i)
        send_email.delay(i)


@celery.task
def send_email(data):
    logger = send_email.get_logger()
    logger.info(data)
    util.sendemail(data)