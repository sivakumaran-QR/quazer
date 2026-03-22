from setuptools import setup, find_packages

setup(
    name="quazer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'quazer=quazer.cli:main',
        ],
    },
)