from setuptools import setup


with open('README') as f:
    long_description = ''.join(f.readlines())


setup(
    name='bresenham',
    version='0.1',
    description="An implementation of Bresenham's line drawing algorithm",
    long_description=long_description,
    author='Petr Viktorin',
    author_email='encukou@gmail.com',
    keywords='bresenham,pixel art',
    license='MIT',
    url='https://github.com/encukou/bresenham',
    py_modules=['bresenham'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        ],
    zip_safe=False,
)
