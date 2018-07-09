from celery import Celery
import config

celery = Celery('worker', backend='rpc://', broker='amqp://')
celery.config_from_object(config)