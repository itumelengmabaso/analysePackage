from setuptools import setup, find_packages

setup(
    name='analysePackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='My analyse python package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/itumelengmabaso/analysePackage',
    author='Itumeleng Mabaso',
    author_email='itumeleng.dineomabaso@gmail.com'
)
