from setuptools import setup


setup(
    name='Flask-Celery3',
    version='0.1',
    license='MIT',
    url='https://github.com/jaapz/flask-celery3',
    author='Jaap Broekhuizen',
    author_email='jaapz.b@gmail.com',
    description='Add Celery3 integration to your Flask apps.',
    py_modules=['flask_celery3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'celery'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
