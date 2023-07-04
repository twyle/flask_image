from setuptools import find_packages, setup

# For consistent encoding
from codecs import open
from os import path
import toml

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

py_project_path = path.join(HERE, '../pyproject.toml')
with open(py_project_path, 'r') as f:
    toml_str = f.read()
    parsed_toml = toml.loads(toml_str)
    VERSION = parsed_toml['tool']['commitizen']['version']

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


DESCRIPTION = 'A Flask Extension for uploading images.'
key_words = [
    'flask-image', 'flask image upload', 'image upload s3'
]

install_requires = [
    'flask', 'redis==4.6.0', 
    'rq==1.15.1', 'boto3==1.26.165'
]

setup(
    name='flask_image',
    packages=find_packages(
        include=[
            'flask_image',
            'flask_image.exceptions',
            'flask_image.server',
            'flask_image.config',
            'flask_image.aws'
        ]
        ),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    url='https://youtube-wrapper.readthedocs.io/en/latest/index.html',
    author='Lyle Okoth',
    author_email='lyceokoth@gmail.com',
    license='MIT',
    install_requires=install_requires,
    keywords=key_words,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent'
    ],
)
