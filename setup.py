from setuptools import setup

setup(name='SimpleFilter',
      version='0.12',
      description='SimpleFilter is a module that provides the tools necessary to build a convolutional classification network.',
      url='https://github.com/dibsonthis/SimpleFilter',
      author='Adib Attie',
      author_email='adib.attie33@gmail.com',
      license='MIT',
      packages=['SimpleFilter'],
      install_requires=[
          'matplotlib', 'Pillow', 'requests',
      ],
      zip_safe=False)
