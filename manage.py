
from flask_script import Manager,Server
from app import create_app

app = create_app('default')

manager = Manager(app)

manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User ) # creates a mini consiole

if __name__ == '__main__':
    manager.run()
