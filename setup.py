import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

README = open('README.rst').read()
CHANGES = ""
version = "1.0.0"

requires = []

setup(name='w20e.pyramidwsgi.recipe',
      version=version,
      description='Pyramid WSGI recipe',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='D.A.Dokter',
      author_email='dokter@w20e.com',
      url='',
      keywords='wsgi pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="w20e.pyramidwsgi.recipe",
      entry_points={'zc.buildout':
                        ['wsgi = w20e.pyramidwsgi.recipe:WSGI',
                         'default = w20e.pyramidwsgi.recipe:WSGI']},
      )
