Using `cdk`
===========

Author an asciidoc document. For example make a file `hello.asc` ::

    = My Presentation

    == Slide 1

    Some of my favorite colors:

    [options="incremental"]
    * red
    * green
    * blue

    == Slide 2

    And some very important code
    
    [source,python]  
    ----
    >>> print "hello World"
    ----

Run `cdk` on your input file to produce a single html file you can
open in your browser.

::

   $ cdk hello.asc

Open the resulting `hello.html` file in your browser! Hit the space
bar to advance a slide or hit the "h" key to see what other commands
are available to navigate through the deck.

Installing/customizing Themes
=============================

TODO

Selecting Filters, tweaking sizes
=================================

TODO




