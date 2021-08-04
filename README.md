CONTENT

[cloud_user@arminmelchior1c important]$ ls -lart
total 60
drwxrwxr-x.  5 cloud_user cloud_user    69 Jul 21 10:06 lambda
drwxrwxr-x.  6 cloud_user cloud_user   198 Jul 28 12:37 sam-app
drwxrwxr-x.  2 cloud_user cloud_user     6 Aug  4 13:29 python3_sysadmin
drwx------. 35 cloud_user cloud_user  4096 Aug  4 13:31 ..
-rw-rw-r--.  1 cloud_user cloud_user 45975 Aug  4 13:34 cmds_040821.log
-rwxrwxrwx.  1 cloud_user cloud_user  7480 Aug  4 13:40 cmds_root_040821.log

INSTALLED SW:

[cloud_user@arminmelchior1c important]$ aws help
[cloud_user@arminmelchior1c important]$ docker -v
Docker version 20.10.7, build f0df350
[cloud_user@arminmelchior1c important]$ python3 --version
Python 3.6.8
[cloud_user@arminmelchior1c important]$ ansible --version
[DEPRECATION WARNING]: Ansible will require Python 3.8 or newer on the controller starting with Ansible 2.12. Current 
version: 3.6.8 (default, Mar 19 2021, 05:13:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)]. This feature will be removed 
from ansible-core in version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in 
ansible.cfg.
ansible [core 2.11.2] 
  config file = None
  configured module search path = ['/home/cloud_user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/cloud_user/.local/lib/python3.6/site-packages/ansible
  ansible collection location = /home/cloud_user/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/cloud_user/.local/bin/ansible
  python version = 3.6.8 (default, Mar 19 2021, 05:13:41) [GCC 8.4.1 20200928 (Red Hat 8.4.1-1)]
  jinja version = 2.10.1
  libyaml = True
