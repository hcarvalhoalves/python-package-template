This is an attempt to put together Python packaging best-practices I've learned in an easy-to-use template you can checkout and work on.

## Dependencies

You put the required packages `REQUIREMENTS`:

```
django<1.6
django-filter
```

Some of the listed packages might not exist in PyPi though. In this case, you can specify the tarball location in `REQUIREMENT_LINKS`. For instance, to install my version of `django-filter` from GitHub, I would add:

```
http://github.com/hcarvalhoalves/django-filter/tarball/master#egg=django-filter
```

## Development

Create your virtualenv and simply `python setup.py develop` your package into it.

## Releasing

The release process using the included `setup.py` and `Makefile` boils down to:

1. Update code and commit:
`git commit -m "Change foo() to bar()"`

2. At any moment, tag the release (optional):
`git tag mypackage-2.0`

3. Build a source distribution:
`make all`

This would create a distribution like `dist/mypackage-2.0.tar.bz2`. If you don't tag the release, we use `git describe` to give it a unique version based on the latest commit hash, so it will turn out as something like `mypackage-1.1-a8c9.tar.bz2` (the last tag + unique hash). As a good practice, `make all` runs the test suite and aborts the build if tests don't pass.
