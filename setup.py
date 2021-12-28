#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import re

from os.path import dirname
from setuptools import setup

ROOT = dirname(__file__)

RE_REQUIREMENT = re.compile(r"^\s*-r\s*(?P<filename>.*)$")

RE_MD_CODE_BLOCK = re.compile(r"```(?P<language>\w+)?\n(?P<lines>.*?)```", re.S)
RE_SELF_LINK = re.compile(r"\[(.*?)\]\[\]")
RE_LINK_TO_URL = re.compile(r"\[(?P<text>.*?)\]\((?P<url>.*?)\)")
RE_LINK_TO_REF = re.compile(r"\[(?P<text>.*?)\]\[(?P<ref>.*?)\]")
RE_LINK_REF = re.compile(r"^\[(?P<key>[^!].*?)\]:\s*(?P<url>.*)$", re.M)
RE_TITLE = re.compile(r"^(?P<level>#+)\s*(?P<title>.*)$", re.M)
CUT = "<!-- CUT HERE -->"

RST_TITLE_LEVELS = ["=", "-", "*"]


def md2pypi(filename):
    """
    Load .md (markdown) file and sanitize it for PyPI.
    Remove unsupported github tags:
     - travis ci build badges
    """
    content = io.open(filename).read().split(CUT)[0]

    for match in RE_MD_CODE_BLOCK.finditer(content):
        rst_block = "\n".join(
            [".. code-block:: {language}".format(**match.groupdict()), ""]
            + ["    {0}".format(ln) for ln in match.group("lines").split("\n")]
            + [""]
        )
        content = content.replace(match.group(0), rst_block)

    refs = dict(RE_LINK_REF.findall(content))
    content = RE_LINK_REF.sub(r".. _\g<key>: \g<url>", content)
    content = RE_SELF_LINK.sub(r"`\g<1>`_", content)
    content = RE_LINK_TO_URL.sub(r"`\g<text> <\g<url>>`_", content)

    for match in RE_LINK_TO_REF.finditer(content):
        content = content.replace(
            match.group(0),
            "`{text} <{url}>`_".format(
                text=match.group("text"), url=refs[match.group("ref")]
            ),
        )

    for match in RE_TITLE.finditer(content):
        underchar = RST_TITLE_LEVELS[len(match.group("level")) - 1]
        title = match.group("title")
        underline = underchar * len(title)

        full_title = "\n".join((title, underline))
        content = content.replace(match.group(0), full_title)

    return content


name = "rdflib-rdfa-microdata"
version = __import__("rdflib_rdfa_microdata").__version__


setup(
    name=name,
    version=version,
    description="rdflib extension adding RDFa and HTML microdata parsers",
    long_description=md2pypi("README.md"),
    maintainer="RDFLib Team",
    maintainer_email="rdflib-dev@google.com",
    url="https://github.com/RDFLib/rdflib-rdfa-microdata",
    license="BSD",
    packages=["rdflib_rdfa_microdata"],
    zip_safe=False,
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    test_suite="nose.collector",
    install_requires=[
        "rdflib>=6.0.0",
        "requests",
        "pyrdfa3"],
    dependency_links=[
        "git+https://github.com/RDFLib/pymicrodata.git#egg=pymicrodata"
    ],
    tests_require=["pytest"],
    command_options={
        "build_sphinx": {
            "project": ("setup.py", name),
            "version": ("setup.py", ".".join(version.split(".")[:2])),
            "release": ("setup.py", version),
        }
    },
    entry_points={
        "rdf.plugins.parser": [
            "hturtle = rdflib_rdfa_microdata.hturtle:HTurtleParser",

            "rdfa = rdflib_rdfa_microdata.structureddata:RDFaParser",

            "mdata = rdflib_rdfa_microdata.structureddata:MicrodataParser",

            "microdata = rdflib_rdfa_microdata.structureddata:MicrodataParser",

            # A convenience to use the RDFa 1.0 syntax (although the parse method can
            # be invoked with an rdfa_version keyword, too)
            "rdfa1.0 = rdflib_rdfa_microdata.structureddata:RDFa10Parser",

            # Just for the completeness, if the user uses this
            "rdfa1.1 = rdflib_rdfa_microdata.structureddata:RDFaParser",

            # An HTML file may contain both microdata, rdfa, or turtle. If the user
            # wants them all, the parser below simply invokes all:
            "html = rdflib_rdfa_microdata.structureddata:StructuredDataParser",

            # Some media types are also bound to RDFa
            "application/svg+xml = rdflib_rdfa_microdata.structureddata:RDFaParser",

            "application/xhtml+xml = rdflib_rdfa_microdata.structureddata:RDFaParser",

            "text/html = rdflib_rdfa_microdata.structureddata:StructuredDataParser",
        ],
    },
)
