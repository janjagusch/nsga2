from setuptools import find_packages

try:
    from restricted_pkg import setup
except ImportError:
    from pip._internal import main
    main(['install', 'restricted_pkg'])
    from restricted_pkg import setup


__version__ = '0.1.0'
__project__ = 'fut_squad_evolver'

setup(name=__project__,
      version=__version__,
      description="",
      url="",
      author='Jan-Benedikt Jagusch',
      author_email='jan.jagusch@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={},
      include_package_data=True,
      python_requires='>=3.6',
      install_requires=[
          'numpy==1.16.1',
          'pandas==0.24.1',
          'xlrd==1.2.0',
          'kaggle==1.5.3',
          'flask==1.0.2'
      ],
      zip_safe=False)
