This is an attempt to put together Python packaging best-practices I've learned in an easy-to-use template you can checkout and work on.

## Dependencies

You add the required packages to `REQUIREMENTS`:

```
django<1.6
django-filter
```

Some of the requirements might not exist in PyPi, or you want to override the egg used. In this case, you can specify the tarball location in `REQUIREMENTS_LINKS`. For instance, to install my version of `django-filter` from GitHub, I would add:

```
http://github.com/hcarvalhoalves/django-filter/tarball/master#egg=django-filter
```

## Development

Create your virtualenv and simply `python setup.py develop` your package into it. That's all.

## Releasing

The release process using the included `setup.py` and `Makefile` boils down to:

1. Update code and commit:
`git commit -m "Change foo() to bar()"`

2. At any moment, tag the release (optional):
`git tag mypackage-2.0`

3. Build a source distribution:
`make all`

This would create a distribution like `dist/mypackage-2.0.tar.bz2`. If you don't tag the release, we use `git describe` to give it a unique version based on the latest commit hash, so it will turn out as something like `mypackage-1.1-a8c9.tar.bz2` (the last tag + unique hash). As a good practice, `make all` runs the test suite configured in `setup.py` and aborts building if the tests don't pass.
