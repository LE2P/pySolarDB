from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='pysolardb',
    version='0.1.0',
    description='Package used to access the LE2P solar database SolarDB',
    url='https://github.com/LE2P/pySolarDB/tree/main/pysloardb',
    author='Emmanuel Parfait',
    author_email='manuparfait@gmail.com',
    licence='MIT',
    include_package_data=True,
    packages=['pysolardb'],
    install_requires=['os'
                      'requests>=2.25.1',
                      'json>=2.0.9'
                      ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[

    ]
)