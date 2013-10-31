Design Justifications
=====================

I'm having some challenges writing a utility that mainly stitches
together other programs. In particular my main goals are:

 * ease of installation. I want to be able to tell people to just
   `sudo easy_install cdk`
 * My dependencies are not dependable: `deck.js` isn't a python package at all
   and `asciidoc` isn't setup to be installed.
 * I don't want to have a source tree full of thousands of files I'm
   not authoring.

Complicating things is the difficulty of getting setuptools to include
non-python data files in a known good location. Currently I am:

 * including a couple of package data directories `cdk/data` and
   `cdk/custom`. I'm not checking `cdk/data` into source control, the
   contents can be recreated by running `make getdata`.
 * I'm using the `MANIFEST.in` file to include all the contents of
   `cdk/data` and `cdk/data` in the `sdist` I'm building with `python
   setup.py sdist`.

