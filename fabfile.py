import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, settings
from fabric.decorators import task
from fabtools import vagrant


ID_VM = '3679be6'  # for Vagrant
REPO_URL = 'https://github.com/Ninjamannn/smart_home.git'
BRANCH = 'develop'  # git branch
env.user = 'ubuntu'
PROJECT = '/home/{user}/project'.format(user=env.user)
env.hosts = ['localhost']
env.venvpyton = '/home/{user}/env/iot/bin'.format(user=env.user)
#env.user = USER
#env.key_filename = '/home/alex/vagrant/Server3fabric/.vagrant/machines/env_iot_test_fabric/virtualbox/private_key'


@task
def to_vagrant():
    """
    if you uses Vagrant run: 'fab to_vagrant deploy'
    """
    global PROJECT
    config = vagrant.ssh_config(ID_VM)
    env.hosts = ['{host}:{port}'.format(host=config['HostName'], port=config['Port'])]
    env.user = config['User']
    env.key_filename = config['IdentityFile']  # path to SSH Key
    PROJECT = '/home/{user}/project'.format(user=env.user)
    print('----------------')
    print(env.user)


@task
def uname():
    run('uname -a')


@task
def deploy():
    site_folder = '/home/{user}/project/'.format(user=env.user)
    run('mkdir -p {site_folder}'.format(site_folder=site_folder))
    with cd(site_folder):
        #_get_latest_source()
        _update_virtualenv()
        #_create_or_update_dotenv()
        #_update_static_files()
        #_update_database()


@task
def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run('git clone {REPO_URL} . -b {BRANCH}'.format(REPO_URL=REPO_URL, BRANCH=BRANCH))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('git reset --hard {current_commit}'.format(current_commit=current_commit))


@task
def _update_virtualenv():
    if not exists('{venvpyton}/pip3'.format(venvpyton=env.venvpyton), verbose=True):
        run('sudo apt -y install python3-pip')
        run('sudo pip3 install virtualenv')
        run('virtualenv --no-site-packages -p python3.5 /home/{user}/env/iot'.format(user=env.user))
    run('{venvpyton}/pip3 install -r requirements.txt'.format(venvpyton=env.venvpyton))


@task
def _create_or_update_dotenv():
    append('{PROJECT}/testenv.env'.format(PROJECT=PROJECT), 'DJANGO_DEBUG_FALSE=y')
    append('{PROJECT}/testenv.env'.format(PROJECT=PROJECT), 'SITENAME={host}'.format(host=env.hosts))
    current_contents = run('cat {PROJECT}/testenv.env'.format(PROJECT=PROJECT))
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('{PROJECT}/testenv.env'.format(PROJECT=PROJECT), 'DJANGO_SECRET_KEY={new_secret}'.format(new_secret=new_secret))


@task
def _update_static_files():
    run('{venvpyton}/python {PROJECT}/manage.py collectstatic --noinput'
        .format(venvpyton='/home/vagrant/env/iot/bin', PROJECT=PROJECT))


@task
def _update_database():
    run('{venvpyton}/python manage.py migrate --noinput'.format(venvpyton=env.venvpyton))
