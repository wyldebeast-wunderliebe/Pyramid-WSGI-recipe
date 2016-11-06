import stat
import os
import zc.buildout
from zc.recipe.egg.egg import Eggs
from .templates import WSGI_TEMPLATE, APACHE_SKEL_TEMPLATE


class WSGI(object):

    """Create WSGI script for Pyramid """

    def __init__(self, buildout, name, options):

        self.buildout = buildout
        self.name = name
        self.options = options
        self.egg = zc.recipe.egg.Scripts(buildout, name, options)

    def install(self):

        bin_dir = self.buildout['buildout']['bin-directory']

        egg = Eggs(self.buildout, self.options["recipe"], self.options)
        reqs, ws = egg.working_set()
        path = [pkg.location for pkg in ws]
        extra_paths = self.options.get('extra-paths', '')
        extra_paths = extra_paths.split()
        path.extend(extra_paths)

        template_vars = {
            'python': self.buildout['buildout']['executable'],
            'pypath': ",\n    ".join((repr(p) for p in path)),
            'config': self.options['ini_file'],
            'buildout_dir': self.buildout['buildout']['directory'],
            'script_path': bin_dir,
            'script_name': self.options['script_name']
            }

        wsgi_script = '%s/%s.wsgi' % (bin_dir, self.options['script_name'])

        open(wsgi_script,
             'w').writelines(WSGI_TEMPLATE % template_vars)

        os.chmod(wsgi_script,
                 stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
                 | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP
                 | stat.S_IROTH | stat.S_IXOTH
                )

        if self.options.get('apache_config', None):
            open(self.options['apache_config'],
                 'w').writelines(APACHE_SKEL_TEMPLATE % template_vars)

        return []
