from setuptools import setup, find_packages


setup(
    name='stallion_sdk',
    version='1.0',
    license='MIT',
    author="amirhnajafiz",
    author_email='najafizadeh21@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/amirhnajafiz/stallion-python-sdk',
    keywords='stallion sdk python',
)