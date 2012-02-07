from setuptools import setup, find_packages
import os

version = '0.3'

setup(name='nsi.svgtool',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Leandro Cruz',
      author_email='lmvcruz@gmail.com',
      url='http://nsi.iff.edu.br',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nsi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
