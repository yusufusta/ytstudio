
from setuptools import setup
import os

required = open(os.path.join(os.getcwd(), "requirements.txt"), "r").read().splitlines()
long_description = open('README.md').read()

setup(
    name='ytstudio',
    version='1.0.0',
    description='Unofficial API for Youtube Studio.',
    long_description=long_description,
    author='Yusuf Usta',
    author_email='yusuf@usta.email',
    maintainer='Yusuf Usta',
    maintainer_email='yusuf@usta.email',
    url='https://github.com/yusufusta/ytstudio',
    license='GPL3',
    packages=['ytstudio'],
    install_requires=required,
    keywords=['youtube', 'youtube-studio', 'ytstudio', 'studio'],
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)