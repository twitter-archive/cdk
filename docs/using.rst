Using `cdk`
===========

`cdk` transforms asciidoc documents into single file html slide
decks. You can generate a simple slide deck with ::

    $ cdk --generate=sample.asc

The sample file might look something like::

    = My Presentation

    Author: @somebody

    == My First Slide

    Presentation software for engineers

    [options="incremental"]
    * Content should be simple but presentation stylish.
    * Author slides in plain text (asciidoc)
    * And play them in the browser.

    == My Second Slide

    Use the source!

    [source,python]
    ----
    >>> x = list("Simeon")
    >>> x.lower()
    "simeon"

    ----    

Now run `cdk` on your input file to produce a single html file you can
open in your browser.

::

   $ cdk sample.asc

Open the resulting `sample.html` file in your browser! Hit the space
bar to advance a slide or hit the "h" key to see what other commands
are available to navigate through the deck.

Installing/customizing Themes
=============================

`cdk` has a themes directory that contains the default theme named "plain".

A theme is just a directory with a .css file of the same name. For
example a theme "foo" is just a directory named `foo` with a `foo.css`
file in it.

`cdk` comes with a command to install a theme. All this means is
putting a directory in a zip file - the contents will be
extracted to the `cdk` theme directory. If you name your theme "plain" it
will overwrite the default (but don't do that!)

`cdk` also comes with a flag to pick a theme for a build or to set the
default to always use a theme when building a slide deck.

So basically - you need to make a .zip with a theme. Let's say you
called the theme "newcircle". You could install it and make it the
default with

$ cdk --install-theme=newcircle.zip
$ cdk --default-theme=newcircle


Note: In practice I may use `lessc` and some helper scripts to make
editing .css easier and to allow packing of images into the .css. See
the included twitter theme at
https://github.com/twitter/cdk/tree/master/cdk/custom/deck.js/themes/twitter

For another example theme contributed by a third-party check out
https://github.com/thenewcircle/cdk-theme



Selecting Filters, tweaking sizes
=================================

TODO




