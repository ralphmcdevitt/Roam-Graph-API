# setup.py
from setuptools import setup, find_packages

setup(
    name="roam_graph_api",
    version="3.3.0",
    packages=find_packages(where="scripts"),
    package_dir={"": "scripts"},
    install_requires=open("requirements.txt").read().splitlines(),
)