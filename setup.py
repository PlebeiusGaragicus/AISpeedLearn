from setuptools import setup, find_packages

from aisl.version import VERSION

setup(
    name='aisl',
    version=VERSION,
    description='AI Speed Learning is a command-line utility for creating AI-generated study and review materials.',
    author='Micah Fullerton',
    author_email='plebeiusgaragicus@gmail.com',
    url='https://github.com/PlebeiusGaragicus/aisl',
    packages=find_packages(),
    install_requires=[
        # List your app's dependencies here
        # 'wheel',
        'torch',
        'transformers',
        'openai',
        'python-dotenv',
        'docopt',
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        # TODO:
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'aisl=aisl:main',
        ],
    },
)