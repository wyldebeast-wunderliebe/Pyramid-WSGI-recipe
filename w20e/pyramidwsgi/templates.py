WSGI_TEMPLATE = """\
#!%(python)s

import sys

sys.path[0:0] = [
    %(pypath)s,
]

INIFILE = "%(config)s"

# init logging
from paste.script.util.logging_config import fileConfig
fileConfig(INIFILE)

from pyramid.paster import get_app
application = get_app(INIFILE, "main")
"""

APACHE_SKEL_TEMPLATE = """\
<VirtualHost *:80>

    # If you use ZODB, proesses should be 1, unless you use ZEO. ZODB can handle
    # only one process. If you run the app in a virtual env, make sure the
    # process runs as the user and group that can actually access and write to
    # the directories the app runs in. Also set the python-path to the python
    # lib of your virtualenv.
    #

    ServerAdmin <your email address>
    ServerName <your virtual host> 

    WSGIScriptAlias / %(script_path)s/%(script_name)s.wsgi
    WSGIDaemonProcess %(script_name)s user=<user that the app runs as> \
      group=<group the app runs as> processes=1 threads=25 \
      python-path=<path to your python lib dir, can be virtualenv>
    WSGIProcessGroup %(script_name)s

    <Directory %(buildout_dir)s>
      Order allow,deny
      Allow from all
    </Directory>

    CustomLog /var/log/apache2/%(script_name)s.log combined

</VirtualHost>
"""
