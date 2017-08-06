from setuptools import setup


setup(
    name='checks-em',
    version='0.1.2',
    py_modules=[
        'checks-em',
    ],
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        checks-em=checks-em:main
    """,
)
