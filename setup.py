# coding: utf8

from setuptools import setup

requires = ["requests>=2.18.0"]

long_description = """
serverless-flask
==========

pip package for flask framework with serverless framework

## Compatibility

This is tested with Python3.6 and Flask 0.11.2, 1.0.0, 1.0.2

## Installation

Command to install

```
pip install serverless-flask
```

## Usage

Define `logger` and `middleware` annotation like below, 

you can throw application log (Now logging level is only DEBUG) and add your custom middleware you define.

※ ) There is one thing to note. The order you annote should be `app.route`, `logger` and `middleware` from the top. If you change this order flask throw Exception. (in the future we wanna modify this restriction)

```
from serverless_flask.interceptor import Interceptor as interceptor

@app.route('/v.1.0/hoge', methods=['POST'])
@interceptor.logger
@interceptor.middleware(func1)
@interceptor.middleware(func2)
def test(*args, **kwargs):
    return jsonify({
            "message": "ok"
        })
```

As you can see in the below code, your custom middleware should have request parameter (but you don't have to use it.).

These functions must return the values with type of dict, list or tuple, otherwise Exception will be thrown.

```
from flask import request

def func1(req: request):
    return {'key': "value"}

def func2(req: request):
    return ['val1', 'val2'] 

# Links
Website: coming soon

Code: https://github.com/Queue-inc/serverless-flask

Company Page: http://www.queue-inc.com
```


"""

setup(
    name='serverless-flask',
    version='0.0.7',
    description='add links to readme',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Queue-inc/serverless-flask',
    author='shibatanaoto',
    author_email='shibata@queue-inc.com',
    license='MIT',
    keywords=['flask', 'restful', 'interceptor', 'AOP'],
    packages=[
        "serverless_flask",
    ],
    install_requires=requires,
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python'
    ],
)