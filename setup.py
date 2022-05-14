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
        'celery',
        'gensim',
        'imageio',
        'mongoengine',
        'numpy',
        'pandas',
        'pefile',
        'Pillow',
        'py2neo',
        'Pygments',
        'pymongo',
        'redis',
        'torch',
        'torchsummary',
    ]
)
