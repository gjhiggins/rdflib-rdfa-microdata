.. _rdflib_rdfa_microdata.jsonld_parser: an RDFLib plugin JSONLD parser

========================================
RDFa/microdata parser plug-in for RDFLib
========================================

Using the plug-in JSONLD parser with RDFLib
---------------------------------------------

The plugin serializer is automatically registered if installed by
setuptools.

Identify a source of JSON-LD, pass the source to the parser,
manipulate the resulting graph.

.. code-block:: python

    >>> from rdflib import Graph, URIRef, Literal
    >>> test_json = """
    ... {
    ...     "@context": {
    ...         "dcterms": "http://purl.org/dc/terms/",
    ...         "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    ...         "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
    ...     },
    ...     "@id": "http://example.org/about",
    ...     "dcterms:title": {
    ...         "@language": "en",
    ...         "@value": "Someone's Homepage"
    ...     }
    ... }
    ... """
    >>> g = Graph().parse(data=test_json, format='json-ld')
    >>> list(g) == [(URIRef('http://example.org/about'),
    ...     URIRef('http://purl.org/dc/terms/title'),
    ...     Literal(%(u)s"Someone's Homepage", lang=%(u)s'en'))]
    True


Module contents
---------------

.. currentmodule:: rdflib_rdfa_microdata.parser

.. automodule:: rdflib_rdfa_microdata.parser

.. autoclass:: JsonLDParser
   :members: parse

.. autofunction:: to_rdf
