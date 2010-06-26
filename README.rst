Flapp is a project template for creating Google AppEngine sites using Flask.
Based on work by Peter Baumgartner.

Getting Started:
1. Make a local copy of secrets.py.example
cp secrets.py.example secrets.py
2. Change the name of the project in app.yaml

To run on App Engine, simply run::

	dev_appserver.py .
	
within this directory.

To run outside of App Engine, either:

- add ``lib`` to your ``PYTHONPATH``, or
- ``pip install -r requirements.pip``

then run::

	python application.py