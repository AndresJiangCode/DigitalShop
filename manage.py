from flask import render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

'''
数据库迁移
迁移命令
1.python manage.py db init
2.python manage.py db migrate
3.python manage.py db upgrade
'''

from app import create_app
from app.models import *

'''
Flask-Script是一个让你的命令行支持自定义命令的工具，
它为Flask程序添加一个命令行解释器。可以让我们的程序从命令行直接执行相应的程序。
'''

# 创建应用
app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


# 每次启动python shell会话都要导入数据库实例和模型，很麻烦。
# 为了避免一直重复导入，我们可以做些配置让Flask-Script的Shell命令自动导入特定的对象。
# 若想把对象添加到导入列表中，我们要为shell命令注册一个make_context回调函数
# 回调函数
def make_shell_context():
    return dict(app=app, db=db)


# 为了导出数据库迁移命令，flask_migrate提供一个MigrateCommand类，可附加到flask_script的manager对象上
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# 404跳转，路由异常显示界面配置
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404


if __name__ == '__main__':
    # 默认端口为5000，如果被占用可在运行配置中修改 -p 端口号
    manager.run()
