from setuptools import setup, find_packages

setup(name="maho",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      scripts=['scripts/maho'])