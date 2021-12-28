# RDFLib plugin providing RDFa and HTML microdata parsing

This is an implementation of [RDFa](http://www.w3.org/TR/RDFa/)
and [microdata]() parsers for [RDFLib](https://github.com/RDFLib/rdflib).

This implementation will:

- read in an HTML document and create an RDF graph from any parsable RDFa or microdata markup


## Installation

The easiest way to install the RDFLib RDFa-microdata plugin is directly from PyPi using pip by running the command below:

```shell
pip install rdflib-rdfa-microdata
```

Otherwise you can download the source and install it directly by running:

```shell
python setup.py install
```


## Using the plug-in RDFa/microdata parser with RDFLib

The plugin parser and serializer are automatically registered if installed by
setuptools.

```python
>>> from rdflib import Graph, plugin
>>> from rdflib.serializer import Serializer

>>> testrdf = """
... @prefix dcterms: <http://purl.org/dc/terms/> .
... <http://example.org/about>
...     dcterms:title "Someone's Homepage"@en .
... """

>>> g = Graph().parse(data=testrdf, format='n3')

```

<!-- CUT HERE -->
<!-- Text after this comment won't appear on PyPI -->

## Building the Sphinx documentation

If Sphinx is installed, Sphinx documentation can be generated with:

```shell
$ python setup.py build_sphinx
```

The documentation will be created in ./build/sphinx.


## Continuous integration tests

[![Build Status](https://travis-ci.org/RDFLib/rdflib-rdfa-microdata.svg?branch=master)](https://travis-ci.org/RDFLib/rdflib-rdfa-microdata)
