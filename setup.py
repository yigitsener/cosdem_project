from setuptools import setup

setup(name='cosdem',
      version='0.0.1',
      description='Comparing Statistical Differences of Measurements',
      long_description='A Python Package Comparing Statistical Differences of Measurements in Two Equivalent Medical Devices',
      url='http://github.com/yigitsener/cosdem_project',
      author='Yiğit Şener',
      author_email='dataevreni@gmail.com',
      license='MIT',
      packages=['cosdem'],
      install_requires=[
          'numpy',
      ],
      include_package_data=True,
      zip_safe=False)
