SOURCES=$(wildcard solved/*.py)
TARGETS=$(SOURCES:solved/%=skel/%)

.PHONY: all skel

all: skel $(TARGETS)

skel:
	install -d $@

skel/%.py: solved/%.py
	sed -e '/#HIDE/,/#SHOW/d' $< > $@

#sync:
#	ssh prog2@linux3.det.ua.pt 'rm -rf ia-tpi1/skel.sessao1/Desktop/'
#	ssh prog2@linux3.det.ua.pt 'install -d ia-tpi1/skel.sessao1/Desktop/'
#	rsync -a skel/* prog2@linux3.det.ua.pt:ia-tpi1/skel.sessao1/Desktop/

