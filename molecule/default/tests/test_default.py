import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_creation(host):
    os = host.system_info.distribution
    user = host.user("bob")

    assert user.exists
    assert user.name == 'bob'
    assert user.gecos == 'Bob'
    assert user.home == '/home/bob'
    assert user.shell == '/bin/bash'

    with host.sudo(user.name):
        groups = host.check_output("groups")

    if os == 'debian':
        assert 'sudo' in groups
    elif os == 'redhat':
        assert 'wheel' in groups


def test_user_remove(host):
    user = host.user('alice')
    assert not user.exists
