from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='my_profile',
    version='0.0.1',
    description='This library will give the details of my profile',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prsrepo/my-profile",
    author='puru',
    author_email='kspreddy94@gmail.com',
    packages=['my_profile'],
    install_requires=[
        'Flask==2.3.2'
    ],
    python_requires='>=3.6'
)
