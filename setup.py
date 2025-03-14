#! /usr/bin/env python3

"""
Setup script for plugin demo
"""

from setuptools import setup, find_packages

package_root = '.'

# list of wildcards, intended to capture ancillary files for plugins/helpers/mergers
# TODO make this neater and/or introduce stronger naming conventions
install_wildcards = [
    '*.bed',
    '*.ini',
    '*.json',
    '*.html',
    '*.txt',
    '*.r',
    '*.R',
    'data/*',
    'html/*',
    'resources/*',
    'R/*',
    'r/*',
    'Rscripts/*',
    'templates/*'
]


setup(
    name='djerba_wgts',
    version='0.0.1',
    packages=find_packages(where=package_root),
    package_dir={'' : package_root},
    package_data={
        'djerba_wgts.plugins.snv_indel_demo': install_wildcards,
    },
    install_requires=[
        'configparse',
        'email_validator',
        'jsonschema',
        'lets-plot',
        'mako',
        'markdown',
        'matplotlib',
        'numpy>2',
        'pandas',
        'pdfkit',
        'plotnine',
        'pycairo',
        'pyinstaller',
        'PyPDF2',
        'requests',
        'seaborn',
        'statsmodels',
    ],
    python_requires='>=3.10.6',
    author="Iain Bancarz",
    author_email="ibancarz [at] oicr [dot] on [dot] ca",
    description="Create reports from metadata and workflow output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oicr-gsi/djerba",
    keywords=['cancer', 'bioinformatics'],
    license='GPL 3.0',
)
