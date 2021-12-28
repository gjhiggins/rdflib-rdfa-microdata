from rdflib import logger, Graph
from rdflib.namespace import Namespace

rdfa_example_1 = """<div vocab="http://rdf.data-vocabulary.org/#" typeof="Review">
   <span property="itemreviewed">L’Amourita Pizza</span>
   Reviewed by
   <span property="reviewer">Ulysses Grant</span> on
   <span property="dtreviewed" content="2009-01-06">Jan 6</span>.
   <span property="summary">Delicious, tasty pizza on Eastlake!</span>
   <span property="description">L'Amourita serves up traditional wood-fired
   Neapolitan-style pizza, brought to your table promptly and without fuss.
   An ideal neighborhood pizza joint.</span>
   Rating:
   <span property="rating">4.5</span>
</div>
"""


def test_example_1():
    g = Graph().parse(data=rdfa_example_1, format="text/html")
    assert g is not None


rdfa_example_2 = """<div vocab="http://rdf.data-vocabulary.org/#" typeof="Review">
   <span property="itemreviewed">L’Amourita Pizza</span>
   Reviewed by
   <span property="reviewer">Ulysses Grant</span> on
   <span property="dtreviewed" content="2009-01-06">Jan 6</span>.
   <span property="summary">Delicious, tasty pizza on Eastlake!</span>
   <span property="description">L'Amourita serves up traditional wood-fired
   Neapolitan-style pizza, brought to your table promptly and without fuss.
   An ideal neighborhood pizza joint.</span>
   Rating:
   <span property="rating">4.5</span>;
   Address:
   <span property="vcard:street-address">111 Lake Drive</span>,
   <span property="vcard:locality">WonderCity</span>,
   <span property="vcard:postal-code">5555</span>,
   <span property="vcard:country-name">Australia</span>.
 </div>
"""


def test_example_2():
    g = Graph().parse(data=rdfa_example_2, format="text/html")
    logger.debug(f"g\n{g.serialize(format='ttl')}")
    assert g is not None


rdfa_example_3 = """<div profile="http://google.profile.example.org" typeof="Review">
   <span property="itemreviewed">L’Amourita Pizza</span>
   Reviewed by
   <span property="reviewer">Ulysses Grant</span> on
   <span property="dtreviewed" content="2009-01-06">Jan 6</span>.
   <span property="summary">Delicious, tasty pizza on Eastlake!</span>
   <span property="description">L'Amourita serves up traditional wood-fired
   Neapolitan-style pizza, brought to your table promptly and without fuss.
   An ideal neighborhood pizza joint.</span>
   Rating:
   <span property="rating">4.5</span>;
   Address:
   <span property="vcard:street-address">111 Lake Drive</span>,
   <span property="vcard:locality">WonderCity</span>,
   <span property="vcard:postal-code">5555</span>,
   <span property="vcard:country-name">Australia</span>.
</div>
"""


def test_example_3():
    g = Graph().parse(data=rdfa_example_3, format="text/html")
    assert g is not None


rdfa_example_4 = """<p vocab="http://Schema.org/" typeof="PostalAddress"><br>
  <span property="name">Google Inc.</span><br>
  P.O. Box <span property="postOfficeBoxNumber">1234</span><br>
  <span property="addressLocality">Mountain View</span>,<br>
  <span property="addressRegion">CA</span><br>
  <span property="postalCode">94043</span><br>
  <span property="addressCountry">United States</span><br>
</p>
"""


def test_example_4():
    g = Graph()
    g.bind("sdo", Namespace("http://Schema.org/"))
    g.bind("rdfa", Namespace("http://www.w3.org/ns/rdfa#"))
    g.parse(data=rdfa_example_4, format="text/html")
    assert g is not None


rdfa_example_5 = """<div vocab="http://Schema.org/" typeof="Product">
  <img property="image" src=" productphoto.jpg" alt="image description"/>
  <span property="name">product name</span>
  <div property="review" typeof="Review"> Review:
    <span property="reviewRating" typeof="Rating">
      <span property="ratingValue">5</span> -
    </span>
    <b>‘<span property="name">Review Title</span>‘</b> by
    <span property="author" typeof="Person">
      <span property="name">author name</span>
    </span>, written on
    <meta property="datePublished" content="2006-05-04">May 4 2006
    <div property="reviewBody">review text</div>
    <span property="publisher" typeof="Organization">
      <meta property="name" content="publisher name">
    </span>
  </div>
</div>
"""


def test_example_5():
    g = Graph()
    g.bind("sdo", Namespace("http://Schema.org/"))
    g.bind("rdfa", Namespace("http://www.w3.org/ns/rdfa#"))
    g.parse(data=rdfa_example_5, format="text/html")
    # logger.debug(f"g\n{g.serialize(format='ttl')}")
    assert g is not None


rdfa_example_6 = """<a resource="http://orcid.org/0000-0003-1279-3709" typeof="schema:Person"
  href="http://orcid.org/0000-0003-1279-3709">
  <span property="schema:name">Dr.
    <span property="schema:givenName">Bruce</span>
    <span property="schema:familyName">Banner</span>
  </span>
</a>
"""


def test_example_6():
    g = Graph()
    g.parse(data=rdfa_example_6, format="text/html")
    assert g is not None


# Run these by hand because they require connectivity

# uri = "https://alistapart.com/article/introduction-to-rdfa/"


# def test_example_7():
#     g = Graph()
#     g.parse(location=uri, format="text/html")
#     assert g is not None


# uri = "https://alistapart.com/article/introduction-to-rdfa-ii/"


# def test_example_8():
#     g = Graph()
#     g.parse(location=uri, format="text/html")
#     assert g is not None

    # logger.debug(f"g\n{g.serialize(format='ttl')}")
