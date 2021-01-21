# Ansible Role: Users [![Build Status](https://travis-ci.com/justereseau/ansible-role-users.svg?branch=master)](https://travis-ci.com/justereseau/ansible-role-users)

This role install or remove users on an host, with sudo right, on a **Debian** or a **RedHat** host.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
---
# Users to install
USERS:
users:
  - name: Bob
    username: bob
    public_keys: https://github.com/bob.keys

# Users to remove
USERS_TO_REMOVE:
  - username: alice
```

- `USERS`: The users to install.
    - `name`: The complete name of the user
    - `username`: The login name of the user
    - `public_keys`: A link to a keys file, or the plaintext key

- `USERS_TO_REMOVE`: The user to ensure to be absent.
    - `username`: The login name of the user

## Example Playbook

This is an example of how to use this role:

```yaml
  - hosts: servers
    roles:
      - { role: users,
        USERS:
          - name: Bob
            username: bob
            public_keys: https://github.com/bob.keys
        
        USERS_TO_REMOVE:
          - username: alice
      }
```
