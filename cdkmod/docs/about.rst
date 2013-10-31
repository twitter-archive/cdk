About
=====

tl;dr - using `cdk` write documents in asciidoc and produce elegant single-file slidedecks as
html.

`cdk` is a Python progam to more easily stitch together `Asciidoc
<http://www.methods.co.nz/asciidoc/>`_ and `asciidoc-deckjs
<http://houqp.github.io/asciidoc-deckjs/>`_ which allows asciidoc to create `deck.js
<http://imakewebthings.com/deck.js/>`_ slide decks. This means you can author presentations in
plain text in a markdown-like format and get well behaved attractive presentations in a single html
file.

In addition cdk is opinionated. It uses many plugins from the deck.js ecosystem and provides a few
custom plugins as well. It provides theming support. In general features are oriented around the
kinds of things technical instructors need to do:

 * showing and explaining lots of code
 * organizing and navigating large slide decks
 * minimizing the effort needed to make things look good

