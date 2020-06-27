from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

about = {}
with open(os.path.join(here, 'achainpy', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name='libachainpy',
    version=os.getenv('BUILD_VERSION', about['__version__']),
    description='Python library for the achain2.0 REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Achain-Dev/Achain2.0/Achain-sdk-python',
    packages=find_packages(),
    test_suite='nose.collector',
    install_requires=[
        'requests',
        'base58>=1.0.3',
        'ecdsa',
        'colander',
        'pytz',
        'six',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'accli = achainpy.command_line:cli',
            'pytest = achainpy.command_line:testachain',
        ],
    })
