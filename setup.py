from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='osman hlongwane python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/osmanhlongwane/mypackage.git',
    author='Osman Hlongwane',
    author_email='osmanhlongwane@gmail.com'
)
