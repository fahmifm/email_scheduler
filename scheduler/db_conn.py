from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

db = create_engine('mysql://root:root@localhost/email_db')
db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

emails = Table('emails', metadata, autoload=True)
recipients = Table('recipients', metadata, autoload=True)

# Prepare Object class
class Emails(object):
    pass


class Recipients(object):
    pass


# Map object into class
mapper(Emails, emails)
mapper(Recipients, recipients)

# create session connection
Session = sessionmaker(bind=db)
