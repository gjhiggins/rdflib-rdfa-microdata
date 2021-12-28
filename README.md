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

Or, direct from the source code repository


```shell
python -m pip install git+https://github.com/RDFLib/rdflib-rdfa-microdata.git#egg=rdflib-rdfa-microdata
```


Otherwise you can download the source and install it directly by running:

```shell
python setup.py install
```


## Using the plug-in RDFa/microdata parser with RDFLib

The plugin parser and serializer are automatically registered if installed by
setuptools.

```python
>>> from rdflib import Graph

>>> testhtml = """
... <p vocab="http://Schema.org/" typeof="PostalAddress"><br>
...   <span property="name">Google Inc.</span><br>
...   P.O. Box <span property="postOfficeBoxNumber">1234</span><br>
...   <span property="addressLocality">Mountain View</span>,<br>
...   <span property="addressRegion">CA</span><br>
...   <span property="postalCode">94043</span><br>
...   <span property="addressCountry">United States</span><br>
... </p>
... """

>>> g = Graph().parse(data=testhtml, format='html')

```

<!-- CUT HERE -->
<!-- Text after this comment won't appear on PyPI -->

## Building the Sphinx documentation

If Sphinx is installed, Sphinx documentation can be generated with:

```shell
$ python setup.py build_sphinx
```

The documentation will be created in ./build/sphinx.

