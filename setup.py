from setuptools import setup

setup(name='blanket',
      version='0.1',
      description='',
      url='http://github.com/JeffinkoGuru/blanket',
      author='JeffinkoGuru',
      author_email='emailme@jeffinko.guru',
      license='MIT',
      packages=['blanket'],
      install_requires=[
          'Crypto',
          'ecdsa',
      ],
      zip_safe=False)