from setuptools import setup

setup(
    name='pingthis',
    version='1.0.0',
    packages=['pingthis'],
    entry_points={
        'console_scripts': [
            'pingthis = pingthis.__main__:main'
        ],
    },
    install_requires=[
        'rich',
    ],
    author='eytin',
    description='A simple internal network pinging tool.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Environment :: Console',
    ]
)
