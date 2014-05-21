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
default with::

  $ cdk --install-theme=newcircle.zip
  $ cdk --default-theme=newcircle

Note: In practice I may use `lessc` and some helper scripts to make
editing .css easier and to allow packing of images into the .css. See
the included twitter theme at
https://github.com/twitter/cdk/tree/master/cdk/custom/deck.js/themes/twitter

For another example theme contributed by a third-party check out
https://github.com/thenewcircle/cdk-theme
