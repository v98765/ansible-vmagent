Ansible Role: VictoriaMetrics vmagent
=========

Deploy and configure [vmagent](https://victoriametrics.github.io/vmagent.html)

Requirements
------------

Ansible

Role Variables
--------------

All variables which can be overridden are stored in defaults/main.yml

Example Playbook
----------------

```text
---
- hosts: vmagent
  connection: ssh
  become: yes
  roles: 
    - ansible-vmagent
```

License
-------

BSD
