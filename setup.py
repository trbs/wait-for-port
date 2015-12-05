from setuptools import setup
import wait_for_port


setup(
    name='wait_for_port',
    version=wait_for_port.__version__,
    url='http://github.com/trbs/wait_for_port',
    author='trbs',
    author_email='trbs@trbs.net',
    keywords='wait port tcp docker',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT',
    packages=['wait_for_port'],
    entry_points={
        'console_scripts': [
            'wait_for_port = wait_for_port.main:main',
        ]
    },
)
