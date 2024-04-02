from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='jr_rocker',
    version='0.0.0',

    description='Personal rocker plugins',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Jose Luis Rivero',
    author_email='jrivero@openrobotics.org',

    packages=['jr_rocker'],
    package_data={'jr_rocker': ['templates/*.em']},

    install_requires=[
        'rocker',
    ],

    entry_points={
        'rocker.extensions': [
            'jr_dev_helpers = jr_rocker.dev_helpers:DevHelpers',
        ]
    },
)
