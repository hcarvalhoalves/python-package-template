update:
	@python setup.py update_files

sdist:
	@python setup.py update_files
	@python setup.py sdist --format=bztar
