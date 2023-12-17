class Config(object):
    """基础配置类"""
    SECRET_KEY = 'asuka'
    DEBUG = False
    MONGO_URI = 'mongodb://my_mongo_db:27017'

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    MONGO_URI = 'mongodb://my_mongo_db:27017/Development'


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    MONGO_URI = 'mongodb://my_mongo_db:27017/Test'


class ProductionConfig(Config):
    """生产环境配置"""
    MONGO_URI = 'mongodb://my_mongo_db:27017/Production'
