from distutils.core import setup

setup(
    name='DLNValidation',
    version='0.3.1',
    author='Mary Stufflebeam',
    author_email='mary@postmates.com',
    py_modules=['dlnvalidation'],
    url='https://github.com/postmates/DLNValidation',
    license='LICENSE.txt',
    description='Provides validation for the format of USA drivers license numbers',
    long_description=open('README.txt').read(),
    install_requires=[],
)
