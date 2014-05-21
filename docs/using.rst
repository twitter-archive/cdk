Using `cdk`
===========

`cdk` transforms asciidoc documents into single file html slide
decks.


Generating a Sample Deck
------------------------

You can generate a simple slide deck with ::

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

Building your Slides
--------------------

Now run `cdk` on your input file to produce a single html file you can
open in your browser.

::

   $ cdk -o sample.asc

Whihc will open the resulting `sample.html` file in your browser! Hit
the space bar to advance a slide or hit the "h" key to see what other
commands are available to navigate through the deck.
