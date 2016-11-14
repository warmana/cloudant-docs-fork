# Makefile for Cloudant documentation
#

# You can set these variables from the command line.
BUILDDIR      = ../build
MAINSRCDIR    = ../src
TOOLDIR       = ../tools
BUILDTOOLDIR  = $(TOOLDIR)/marked-it-cli
BUILDTOOL     = $(BUILDTOOLDIR)/bin/marked-it-cli
WEBCONTENTDIR = /var/www/html

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean      to clean the build environment"
	@echo "  html       to make all standalone (local) files, in the '$(BUILDDIR)' directory"
	@echo "  debughtml  to do a verbose build of all standalone (local) files"

.PHONY: clean
clean:
	rm -rf $(BUILDDIR)
	@rm -f linkcheck.txt

.PHONY: html
html:
	make clean
	mkdir $(BUILDDIR)
	node $(BUILDTOOL) $(MAINSRCDIR) --output=$(BUILDDIR) --header-file=$(TOOLDIR)/header --footer-file=$(TOOLDIR)/footer --conref-file=$(TOOLDIR)/conref.yml --toc-xml

.PHONY: debughtml
debughtml:
	make clean
	mkdir $(BUILDDIR)
	node $(BUILDTOOL) $(MAINSRCDIR) --output=$(BUILDDIR) --header-file=$(TOOLDIR)/header --footer-file=$(TOOLDIR)/footer --conref-file=$(TOOLDIR)/conref.yml --toc-xml --verbose

.PHONY: publish
publish:
	rm -rf $(WEBCONTENTDIR)/*
	cp -R $(BUILDDIR) $(WEBCONTENTDIR)/docs

.PHONY: linkcheck
linkcheck:
	@rm -f linkcheck.txt
	wget --spider -r -nd -nv -H -l 10 -D localhost -o linkcheck.txt http://localhost/docs/ 2>/dev/null; true

