from setuptools import setup
setup(
    name='Flask-CacheBust',
    version='2.0.0',
    description='Flask extension that cache-busts static files',
    py_modules=['flask_cache_bust'],
    license='MIT',
    url='https://github.com/ChrisTM/Flask-CacheBust',
    install_requires=[
        'Flask',
    ],
)
