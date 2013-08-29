This is an attempt to put together Python packaging best-practices I've learned in an easy-to-use template you can checkout and work on.

## Defining dependencies

Add the required packages to `REQUIREMENTS`, with optional version qualifies:

```
django<1.6
django-filter
```

Some of the requirements might not exist in PyPi, or you want to override the egg used. In this case, you can specify the tarball location in `REQUIREMENTS_LINKS`. For instance, to install my version of `django-filter` from GitHub, I would add:

```
http://github.com/hcarvalhoalves/django-filter/tarball/master#egg=django-filter
```

## Automatic versioning

After cloning this repository, configure `setup.py` to match your project and run:

```
make update
```

This will generate the appropriate `version.py` and `.gitattributes` files using `versioneer.py`. Add those to your repository.

## Development

Create your virtualenv and add your package to it's path by running:

```
python setup.py develop
```

## Releasing a version

There are two possible workflows for releasing:

1. Releasing directly from a working copy:
`make sdist`

2. Releasing from a tag:
`git tag 0.1.2 && make sdist`

3. Installing directly from a tarball (e.g.: GitHub):
`git tag 0.1.2 && git push origin 0.1.2`
`pip install http://github.com/hcarvalhoalves/mypackage/tarball/0.1.2#egg=mypackage`
