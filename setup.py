from setuptools import setup


requires = ["requests>=2.18.0"]

long_description = """
Package for Flask with Serverless Framework
"""

setup(
    name='serverless-flask',
    version='0.0.1',
    description='Package for Flask with Serverless Framework',
    long_description=long_description,
    url='https://github.com/Queue-inc/serverless-flask',
    author='shibatanaoto',
    author_email='shibata@queue-inc.com',
    license='MIT',
    keywords=['flask', 'restful', 'interceptor', 'AOP'],
    packages=[
        "Interceptor",
    ],
    install_requires=requires,
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python'
    ],
)