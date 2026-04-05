from setuptools import setup, find_packages

setup(
    name='desktop-tutorial',
    version='0.1.0',
    description='Projeto de exemplo para CI/CD e testes',
    author='Seu Nome',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    install_requires=[],
)