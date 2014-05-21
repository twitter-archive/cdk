
Setting up the Development Environment
======================================

Clone the repo::

  $ git clone https://github.com/twitter/cdk.git

`cd` into the repo directory. The `cdk/data` directory is empty - run ::
  
  $ make getdata

to download the many non-pip-installable external dependencies.

I recommend working in a virtual environment while modifying the
code. You can activate your virtualenv and the install the
requirements in the accompanying `requirements.txt` file::

  (cdk-virtualenv) $ pip install -r requirements.txt

Once you've installed the requirements and downloaded the additional
data, `cdk/__init__.py` is the setuptools entry point. You can run ::

  (cdk-virtualenv) $ python cdk/__init__.py --generate=sample.asc
  (cdk-virtualenv) $ python cdk/__init__.py -o sample.asc
  
to create a basic deck in asciidoc and compile the slide deck.

