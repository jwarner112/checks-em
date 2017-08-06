from setuptools import setup


setup(
    name='checksem',
    version='0.1.3',
    py_modules=[
        'checksem',
    ],
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        checksem=checksem:main
    """,
)
