from distutils.core import setup

setup(
    name='DLNValidation',
    version='0.1.2',
    author='Mary Stufflebeam',
    author_email='mary@postmates.com',
    py_modules=['dl_number_validation'],
    url='http://pypi.python.org/pypi/DLNValidation/',
    license='LICENSE.txt',
    description='Provides validation of the format of USA drivers license numbers',
    long_description=open('README.txt').read(),
    install_requires=[],
)
