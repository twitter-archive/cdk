Changelog
=========

Changes between cdk 1.0.2 and 1.0.1
-----------------------------------

Tox helps me figure out I can support 2.6 but don't support 3.3 if
asciidoc.py doesn't.


Changes between cdk 1.0.1 and 1.0.0
-----------------------------------

I've got users on Python 2.6-3.3 apparently. Addded a bugfix for
Py2.6. Ain't gonna support 3.0, 3.1, 3.2 - don't ask!

Changes between cdk 1.0 and 0.0.3
---------------------------------

I blame @cra for the version bump. He said (I quote roughly) "Nobody
wants to use 0.0.2!"

Added in custom modified version of TOC extension for deckjs that adds
"s" shortcut for viewing/hiding speaker notes. Also fixed it to stop
intercepting CMD/CTRL+key for deckjs shortcuts. CMD-t is already used,
who knew? Hit "h" key in a slide deck to see shortcuts.

Changes between cdk 0.0.2 and 0.0.3
-----------------------------------

UI updates to builtin themes. Added --custom-css flag.

Changes between cdk 0.0.1 and 0.0.2
-----------------------------------

Minor changes. Removed Google Analytics code from default template
(whoops!) and also improved handling of asciidoc `TIP`, `NOTE`,
`CAUTION`, `IMPORTANT` and `WARNING` blocks. See the new
`cdk/custom/icons` directory with a .less file, various png files
(currently just using the images from asciidoc) so that we can base64
these images once instead of repeatedly.


