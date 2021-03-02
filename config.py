# Importing LRUcache from celery
from celery.utils.functional import LRUCache


class Config:
    DEBUG = False
    SERVICE_NAME = 'celery_caching'

    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = 6379
    BROKER_URL = "redis://{host}:{port}/0".format(
        host=REDIS_HOST, port=str(REDIS_PORT))
    CELERY_RESULT_BACKEND = BROKER_URL

    # Set the cache with a key limit of 10
    RESOURCE_CACHE = LRUCache(limit=10)


class LocalConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    # Development environment
    DEBUG = False


config_by_name = {
    "local": LocalConfig,
    "dev": DevelopmentConfig,
}