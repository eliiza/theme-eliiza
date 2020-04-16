from setuptools import setup

setup(name='theme_eliiza',
      version='0.1',
      description='ggplot theme for eliiza graphics',
      url='http://github.com/eliiza/theme-eliiza',
      author='Patrick Robotham',
      author_email='patrick.robotham@eliiza.com.au',
      license='MIT',
      packages=['theme_eliiza'],
      install_requires=[
          'plotnine',
          'matplotlib'
      ],
      include_package_data=True,
      zip_safe=False)