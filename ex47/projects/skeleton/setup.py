try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
'description':'My Project',
'author':'bingoo',
'url':"URL TO GET IT AT."
'download_url':"I don't know"
'author_email':'hibingog@wulallal.com'

}

setup(**config)