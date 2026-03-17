from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mini projects",
    version="0.1",
    author="Toqeer",
    packages=find_packages(),
    install_requires = requirements,
)