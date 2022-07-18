import redis
from region_config import cfg
import logging
logger = logging.getLogger()

redis_client = redis.Redis(
    host = cfg['redis.host'],
    port = cfg['redis.port'],
    db = cfg['redis.db'],
    password = cfg['redis.password'],
    max_connections = cfg['redis.max_connections'],
    decode_responses=True)

logger.info('redis ping: {}'.format(redis_client.ping()))
