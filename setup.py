import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

VERSION = '0.0.1'

DEPENDENCYLINKS = []
REQUIRES = []


setup(
    name='hotsparser',
    description='Parse Heroes of the Storm Replays',
    keywords='hots',
    version=VERSION,
    author='Bruce Stringer',
    author_email='bruce.stringer@rackspace.com',
    dependency_links=DEPENDENCYLINKS,
    install_requires=REQUIRES,
    entry_points={
        'console_scripts': [
            'hotsparser=manage.py:runserver'
        ]
    },
    tests_require=['tox'],
    packages=find_packages(exclude=['bin', 'ez_setup']),
    include_package_data=True,
    license='Apache License (2.0)',
    classifiers=["Programming Language :: Python"],
    url='http://github.com/HoTSStuff/HotSParser'
)