#!/usr/bin/env python
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name='addons',
      version='1.0.0',
      description='add ons',
      py_modules=['addons'],
      license='MIT',
      platforms='any',
      install_requires=[
          'peer2peer',
          'pkcrypt',
          'websocket-client2',
          'websocket-client',
          'gevent-websocket',
          'gevent','pyaml','bottle']
      )
