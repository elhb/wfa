#from distutils.core import setup
#from Cython.Build import cythonize
#setup(ext_modules=cythonize(["dbs_analysis/hamming_cython_solution.pyx"]))

from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
 Extension(
     'dbs_analysis.hamming_cython_solution',
     ['dbs_analysis/hamming_cython_solution.pyx']
 )
]


reqs = [line.rstrip() for line in open('requirements.txt')]
packages = find_packages()

setup(name='dbs_analysis',
    version='0.0',
    description="",
    url='https://github.com/elhb/DBS_Analysis',
    author='Erik Borgstroem',
    author_email='erik.borgstrom@scilifelab.se',
    packages=packages,
    setup_requires=["Cython >= 0.25.2"],
    install_requires=reqs,
    scripts=[
        'script/dbs_handle_indetifier',
        'script/dbs_barcode_clustrer',
        'script/dbs_insert_mapper',
        'script/dbs_change_settings',
        'script/dbs_cluster_analyzer',
        'script/dbs_find_alleles'
        ],
    ext_modules=cythonize(extensions)
    )
