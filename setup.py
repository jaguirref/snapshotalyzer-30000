from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='Jorge',
    author_email='j.aguirrefdez@icloud.com',
    description="Tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/jaguirref/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)