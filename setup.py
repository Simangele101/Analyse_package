from setuptools import setup, find_packages

setup(
    name='Analyse_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA July 2020 JHB team 7 Sprint Analyse package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/JacCars/Analyse_package',
    author='See readme file',
    author_email='See readme file'
)