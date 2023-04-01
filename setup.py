from setuptools import setup

setup(name='GALACTICA CLI',
      version='0.0.1',
      description='CLI interface for GALACTICA',
      author='tengda',
      author_email='tengda@bipt.edu.cn',
      license='MIT',
      packages=['galactica_cli'],
      install_requires=[
          'galai',
      ],
      entry_points={
            'console_scripts': ['galai_cli=galactica_cli.galai_cli:main'],
      },
      zip_safe=False)
