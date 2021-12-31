from setuptools import setup, find_packages

setup(
    name='dar_sys',
    version='0.1.0',
    packages=find_packages(include=['dar_sys', 'dar_sys.*']),
    entry_points={
        'console_scripts': ['start=dar_sys.dar_api:main']
    },
    install_requires=[
        'uvicorn',
        'fastapi',
        'sqlalchemy'
    ]
)

