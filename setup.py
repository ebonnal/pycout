from setuptools import setup

setup(
    name='pycout',
    version='0.1.2',
    packages=['pycout'],
    package_data={'scimple/scimple_data': ['*']},
    url='http://github.com/EnzoBnl/pycout',
    license='Apache 2.',
    author='Enzo Bonnal',
    author_email='enzobonnal@gmail.com',
    description='Python porting of: cout << "Hello" << " World !" << endl;'
)
