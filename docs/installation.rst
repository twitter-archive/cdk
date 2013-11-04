Installing
==========

For users
---------

::

   $ sudo easy_install cdk


For contributors
----------------

Check the source out of github. Notice the `cdk/data` directory is empty - run ::

  make getdata

To download the many (non pip-installable) external dependencies.

`cdk/__init__.py` is the setuptools entry point. You can run ::

  python cdk/__init__.py docs/getting_started.asc

to get the same command.





