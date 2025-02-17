from __future__ import print_function
from setuptools import setup


def readme():
    with open('README.rst') as fp:
        return fp.read()

setup(name='sqla_yaml_fixtures',
      description='Load YAML data fixtures for SQLAlchemy',
      version='1.1.1',
      license='MIT',
      author='Eduardo Naufel Schettino',
      author_email='schettino72@gmail.com',
      url='https://github.com/schettino72/sqla_yaml_fixtures',
      keywords=['fixture', 'sqlalchemy'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        ],
      packages=['sqla_yaml_fixtures'],
      install_requires=[
          'SQLAlchemy',
          'PyYAML'
      ],
      long_description=readme(),
      )
