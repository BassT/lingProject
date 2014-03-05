#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Main script for DBpedia quepy.
"""

import sys
import time
import random
import datetime
import bottle
#from bottle import route, run, template
import os

import quepy
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
dbpedia = quepy.install("dbpedia")
bottle.debug(True)

# quepy.set_loglevel("DEBUG")

@bottle.route("/")
def index():
    yield u"<p>Here is a <a href=\"http://bottlepy.org/\">bottle</a> app under construction. This example converts the question 'What is a blowtorch?' to a SPARQL query using <a href=\"http://quepy.machinalis.com/\">quepy</a>, queries dbpedia and returns the results (the RDF literals retrieved by rdfs:comment).</p>"
    target, query, metadata = dbpedia.get_query("what is a blowtorch?")
    yield u"<p>" + query + u"</p>"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        yield "<p>" + result["x1"]["value"] + "</p>"
    return

@bottle.route("/question/<q>")
def question(q):
    yield u"<p>This example converts the question " + q + u"to a SPARQL query using <a href=\"http://quepy.machinalis.com/\">quepy</a>, queries dbpedia and returns the results (the RDF literals retrieved by rdfs:comment).</p>"
    target, query, metadata = dbpedia.get_query(q)
    yield u"<p>" + query + u"</p>"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        yield "<p>" + result["x1"]["value"] + "</p>"
    return
bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

