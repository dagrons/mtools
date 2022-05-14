from distutils.core import setup

import setuptools

setup(
    name="mtools",
    version="1.0",
    description="common utilities for malware analysis",
    author="dagrons",
    author_email="heyuehuii@126.com",
    packages = setuptools.find_packages(),
    include_package_data=True,
    package_data = {'': ['malware_classification/trained_models/*', 'malware_sim/trained_models/*']},
    install_requires = [
        'celery==5.1.2',
        'gensim==4.0.1',
        'imageio==2.18.0',
        'mongoengine==0.23.1',
        'numpy',
        'pandas',
        'pefile==2021.5.24',
        'Pillow==9.1.0',
        'py2neo==2021.1.5',
        'Pygments==2.3.1',
        'pymongo==3.11.4',
        'redis==3.5.3',
        'torch==1.11.0',
        'torchsummary==1.5.1',
    ]
)
