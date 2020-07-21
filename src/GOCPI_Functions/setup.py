from setuptools import setup
'Note: To upload new versions 1) cd to GOCPI_Functions 2) python setup.py sdist 3) twine upload dist/*'
'Note: To download 1) pip install --upgrade GOCPI_Functions'
'Note: Make your own python package: https://towardsdatascience.com/make-your-own-python-package-6d08a400fc2d'
'Note: PyPi https://pypi.org/manage/project/gocpi-functions/releases/#modal-close'
setup(name='GOCPI_Functions',
      version='1.3',
      description='User Defined Functions for GOCPI Project',
      packages=['GOCPI_Functions'],
      author_email='connormcdowall@gmail.com',
      zip_safe=False)
