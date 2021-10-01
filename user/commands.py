import secrets
from getpass import getpass
import click
from user import app
from user.models import User
from database import db_session
from utils import datetime_as_string


@app.cli.command('create')
@click.argument('username')
@click.option('--admin', default=False, is_flag=True, help='This flag mark user as admin')
@click.option('--auto-pass', default=False, is_flag=True, help='This flag generate a random password')
def create_user(username, auto_pass, admin):
    """Create user"""
    try:
        user = User(username=username, is_admin=admin)
        if not auto_pass:
            password = getpass('Password: ')
            confirm_password = getpass('Confirm password: ')
            assert password == confirm_password, 'The passwords not match'
        else:
            password = secrets.token_urlsafe(8)

        user.set_password(password)
        db_session.add(user)
        db_session.commit()

        if auto_pass:
            print('Generated password = ', password)

        print('Successful')
    except Exception as e:
        print(str(e))


@app.cli.command('list')
def list_user():
    """List user"""
    labels = ('id', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin')
    users = User.query.all()
    row_format ="{:>5} {:>10} {:>20} {:>20} {:>10} {:>10}"
    print(row_format.format(*labels))
    for user in users:
        print(row_format.format(
            user.id,
            user.username,
            str(datetime_as_string(user.date_joined) or user.date_joined),
            str(datetime_as_string(user.last_login) or user.last_login),
            str(user.is_active),
            str(user.is_admin)
        ))


@app.cli.command('delete')
@click.argument('id')
def delete_user(id):
    """Delete user"""

    user = User.query.filter_by(id=id)
    if not user.count():
        print('User does not exist!')
        return

    confirm = input('Please, confirm the action (y/n): ')

    if confirm.lower() in ('y', 'yes'):
        user.delete()
        db_session.commit()
        print('Successful')
    else:
        print('Canceled')


@app.cli.command('activation')
@click.argument('id')
@click.option('--activate/--inactivate', required=True)
def toggle_activation_user(id, activate):
    """Inactivate user"""
    user = User.query.get(id)
    if not user:
        print('User does not exist!')
        return
    user.is_active = activate
    db_session.commit()
    print('Successful')



@app.cli.command('newpassword')
@click.argument('id')
@click.option('--auto-pass', default=False, is_flag=True, help='This flag generate a random password')
def new_password(id, auto_pass):
    """Change user password"""

    try:
        user = User.query.get(id)
        if not user:
            print('User does not exist!')
            return

        if not auto_pass:
            password = getpass('Password: ')
            confirm_password = getpass('Confirm password: ')
            assert password == confirm_password, 'The passwords not match'
        else:
            password = secrets.token_urlsafe(8)

        user.set_password(password)
        db_session.commit()

        if auto_pass:
            print('Generated password = ', password)

        print('Successful')
    except Exception as e:
        print(str(e))
