#!/usr/bin/env python
from setuptools import setup, find_packages


# Parse version number from pyglet/__init__.py:
with open('pyglet/__init__.py') as f:
    info = {}
    for line in f.readlines():
        if line.startswith('version'):
            exec(line, info)
            break


setup_info = dict(
    name='vnc_env',
    version=info['version'],
    author='Jacob Valdez',
    author_email='jacobfv@msn.com',
    url='https://github.com/JacobFV/vnc_env',
    download_url='http://pypi.python.org/pypi/vnc_env',
    project_urls={
        'Documentation': 'https://github.com/JacobFV/vnc_env',
        'Source': 'https://github.com/JacobFV/vnc_env',
        'Tracker': 'https://github.com/JacobFV/vnc_env/issues',
    },
    description='OpenAI gym wrapper for VNC client',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=['vnc_env'],

    python_requires='>=3.6',  # TODO: make sure works on Python 3.6
    install_requires=[
        "numpy",
        "pyVNC",
    ],
    keywords="vnc gym rl environment",
    zip_safe=True,
)

setup(**setup_info)