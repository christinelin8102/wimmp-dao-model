from setuptools import setup, find_packages

setup(
    name="daomodel",
    version="0.1.0",
    description="MMP Project of DAO",
    author="WiAdvance",
    install_requires=[
        'SQLAlchemy',
        'Flask-SQLAlchemy'
    ],
    packages=find_packages()
)
