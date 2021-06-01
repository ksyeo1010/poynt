import os
import mongoengine


def connect():
    mongoengine.connect(
        db=os.getenv('DB_NAME'),
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
        authentication_source='admin'
    )
