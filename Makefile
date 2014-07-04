datafiles := asciidoc-8.6.8 
datafiles += deck.js
datafiles += deck.ext.js
datafiles += deck.split.js

datadir	:= cdk/data
data	:= $(addprefix $(datadir)/,$(datafiles))

init:
	pip install -r requirements.txt --use-mirrors

test:
	py.test

build: getdata
	python setup.py sdist

getdata: $(datadir) $(data)

$(datadir):
	mkdir -p $@

$(datadir)/asciidoc-8.6.8:
	wget -O asciidoc.tar.gz http://sourceforge.net/projects/asciidoc/files/asciidoc/8.6.8/asciidoc-8.6.8.tar.gz/download
	tar -xzf asciidoc.tar.gz
	mv asciidoc-8.6.8 $@
	rm asciidoc.tar.gz

$(datadir)/deck.js:
	wget -O deckjs.zip https://github.com/imakewebthings/deck.js/archive/4601d4da2bf8c803c9ca55c9d616b568314d3cfa.zip
	unzip deckjs.zip
	mv deck.js-4601d4da2bf8c803c9ca55c9d616b568314d3cfa $@
	rm deckjs.zip

$(datadir)/deck.ext.js:
	wget -O deck.ext.js.zip https://github.com/barraq/deck.ext.js/archive/master.zip
	unzip deck.ext.js.zip
	mv deck.ext.js-master $@
	rm deck.ext.js.zip

$(datadir)/deck.split.js:
	wget -O deck.split.js.zip https://github.com/houqp/deck.split.js/archive/master.zip
	unzip deck.split.js.zip
	mv deck.split.js-master $@
	rm deck.split.js.zip

clean:
	python setup.py clean
	find . -name '*~' -delete
	find . -name '*.pyc' -delete
	rm -rf dist
	rm -rf cdk.egg-info

really-clean: clean cleandata

cleandata:
	rm -rf $(datadir)

.PHONY: init build test getdata clean cleandata really-clean
