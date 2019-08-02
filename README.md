# FeinCMS3 Demo

This is a slightly elaborated demo of [FeinCMS3](https://feincms3.readthedocs.io/en/latest/).
It does not exercise all CMS features, please check out the official [demo](https://github.com/matthiask/feincms3-example/tree/master/app) for details.

## Features

The content model includes only rich text and images, feel free to add.

This demo adds:
- Versioning of content with [django-reversion](https://django-reversion.readthedocs.io/)
- Full text search with [django-haystack](https://django-haystack.readthedocs.io/) and [Whoosh](https://whoosh.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com) templates
- AJAX support

## Usage

Python3 is required. A [Makefile](Makefile) is included for Mac OS with Homebrew. It should also work on Linux & Co. Just type `make` to get started and head over to http://127.0.0.1:8000/.

