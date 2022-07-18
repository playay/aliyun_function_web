from pymongo import MongoClient
from region_config import cfg
import logging
logger = logging.getLogger()

mongo_client = MongoClient(cfg['mongodb.uri']).get_default_database()

logger.info('mongo whatsmyuri: {}'.format(mongo_client.command('whatsmyuri')))