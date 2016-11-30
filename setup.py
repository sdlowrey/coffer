import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    version = f.read().strip()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().strip()

setup_options = dict(
    name='coffer',
    version=version,
    url='https://github.com/sdlowrey/coffer',
    license='Apache',
    author='Scott Lowrey',
    author_email='sdlowrey@gmail.com',
    description='Store encrypted documents and keys in AWS S3',
    packages=find_packages(exclude=['coffer_test', 'coffer_test/*']),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'coffer=coffer.__main__:main'
        ]
    }
)

setup(**setup_options)
