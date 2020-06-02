#-*-coding:utf-8-*-

from setuptools import setup
from setuptools import find_packages

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tnflux',
    version='0.9.2',
    keywords='tn wave activity flux',
    description='Caculating the T-N Wave Activity Flux derived by Takaya and Nakamura (JAS,2001).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Lai Sheng<laish12@lzu.edu.cn>, Yongpeng Zhang<zhangyp6603@outlook.com>',
    author_email='laish12@lzu.edu.cn',
    maintainer='Yongpeng Zhang',
    maintainer_email='zhangyp6603@outlook.com',
    url='https://github.com/jokervTv/T-N_Wave-Activity-Flux',
    license='MIT License',
    packages=find_packages(where='.', exclude=(), include=('*',)),
    platforms='any',
    install_requires=[
        'numpy'
    ],
    data_files=[('', [
        'LICENSE',
        'img/eq38.jpg',
        'img/eq38_hor.jpg',
        'img/jan1981.jpg',
        'img/psnh_mon_hist_waf300_198101.jpg'
    ])],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
