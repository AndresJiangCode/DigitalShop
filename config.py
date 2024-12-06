
class Config:
    SECRET_KEY = 'bhml2023'
    # SQLALCHEMY_TRACK_MODIFICATIONS表示是否追踪对象的修改。
    # 设置为True,会在每次请求结束时检查对象的状态并写入数据库。
    # 该功能可以用于调试和性能优化,但会带来一些开销。
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 初始化配置文件
    @staticmethod
    def init_app(app):
        pass


# 配置数据库和调试模式
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jjh99l6598e13@127.0.0.1:3306/dbdigital'
    DEBUG = True


# 默认配置
config = {
    'default': DevelopmentConfig
}
