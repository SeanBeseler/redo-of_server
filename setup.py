from setuptools import setup

dependencies = []
extra_packages = {'test': ['ipython', 'pytest', 'pytest-cov', 'tox']}
setup(
    name='http-server',
    description='Client sends a message to the server. The server responces by echoing the message',
    version='0.1',
    authors='Sean Besler, Alex',
    authors_email='seanwbeseler@gmail.com',
    license='MIT',
    py_modules='server, client',
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={}
)
