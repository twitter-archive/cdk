init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

build:
	python setup.py sdist

cleandata:
	rm -rf cdk/data/*

getdata:
	wget -O asciidoc.tar.gz http://sourceforge.net/projects/asciidoc/files/asciidoc/8.6.8/asciidoc-8.6.8.tar.gz/download
	tar -xzf asciidoc.tar.gz
	mv asciidoc-8.6.8 cdk/data/
	wget -O deckjs.zip https://github.com/imakewebthings/deck.js/archive/4601d4da2bf8c803c9ca55c9d616b568314d3cfa.zip
	unzip deckjs.zip
	mv deck.js-4601d4da2bf8c803c9ca55c9d616b568314d3cfa cdk/data/deck.js
	wget -O deck.ext.js.zip https://github.com/barraq/deck.ext.js/archive/master.zip
	unzip deck.ext.js.zip
	mv deck.ext.js-master cdk/data/deck.ext.js
	wget https://github.com/houqp/deck.split.js/archive/master.zip
	unzip deck.split.js.zip
	mv deck.split.js-master cdk/data/deck.split.js

clean:
	python setup.py clean
	find . -iname '*~' | xargs rm
	rm -rf dist
	rm -rf cdk.egg-info
