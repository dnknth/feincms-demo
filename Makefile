JSON = pages/fixtures/pages.json.gz
BIN = $(PWD)/.venv3/bin
MANAGE = $(PWD)/manage.py

GETTEXT = /usr/local/opt/gettext
LOCALES  = cms/locale/de/LC_MESSAGES/django.po
LOCALES += pages/locale/de/LC_MESSAGES/django.po
export PATH := $(PATH):$(GETTEXT)/bin


debug: install
	$(MANAGE) migrate
	$(MAKE)   locales
	$(MANAGE) runserver

install: .venv3 db.sqlite3 whoosh_index

db.sqlite3:
	$(MANAGE) migrate
	$(MANAGE) createsuperuser
	$(MANAGE) createinitialrevisions
	$(MANAGE) loaddata pages
	
whoosh_index:
	$(MANAGE) update_index

clean:
	rm -rf */__pycache__

json:
	mkdir -p pages/fixtures
	$(MANAGE) dumpdata pages | gzip -c > $(JSON)
	
tidy: clean
	rm -rf .venv3 db.sqlite3 whoosh_index $(LOCALES:.po=.mo)

.venv3: requirements.txt
	[ -d $@ ] || python3 -m venv $@
	$(BIN)/pip3 install -r $<
	touch $@

locales: $(LOCALES:.po=.mo)

messages: $(LOCALES) $(GETTEXT)
	cd cms   ; $(MANAGE) makemessages -l de
	cd pages ; $(MANAGE) makemessages -l de

%.mo: %.po
	msgfmt -o $@ $<

$(GETTEXT):
	brew install gettext
