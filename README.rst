Introduction
============

''w20e.pyramidwsgi.recipe'' is a `zc.buildout`_ recipe that creates a
WSGI script for inclusion in Apache `using mod_wsgi`_. The Apache
config skeleton can also be created (optional).

To create a WSGI config for your Pyramid app, include a section in
your ''buildout.cfg'' like so::

    [wsgi]
    recipe = w20e.pyramidwsgi.recipe
    eggs = ${pyramid:eggs}
    extra-paths = ${pyramid:extra-paths}
    script_name = yourapp
    ini_file = ${buildout:directory}/production.ini
    apache_config = ${buildout:directory}/apache_wsgi.conf

This will create a python script in bin called ''yourapp.wsgi'' which
mod_wsgi can load. You can also use the optional ''extra-paths''
option to specify extra paths that are added to the python system
path. If you provide the optional apache_config option, the Apache
config file will be created. This is a skeleton however, some
parameters need to be filled in.

.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout
.. _mod_wsgi: http://code.google.com/p/modwsgi/
