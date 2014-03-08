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
from bottle import route, run, template, request
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
    yield u"Try your own question like this: <a href=\"http://pacific-river-6269.herokuapp.com/question/Who is Arnold Schwarzenegger?\">http://pacific-river-6269.herokuapp.com/question/Who is Arnold Schwarzenegger?</a>"
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
    if isinstance(metadata, tuple):
            query_type = metadata[0]
            metadata = metadata[1]
    else:
            query_type = metadata
            metadata = None
    if query is None:
        yield u"<p>Query not generated :(</p>"
   
    yield u"<p>" + query + u"</p>"
    
    if target.startswith("?"):
            target = target[1:]
    if query:
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            if not results["results"]["bindings"]:
                yield u"<p>No answer found :(</p>"
        
       
    for result in results["results"]["bindings"]:
        yield "<p>" + result["x1"]["value"] + "</p>"
    return
   
#   @get("/tryqustion") # or @route('/login')
@bottle.route("/tryquestion")
def tryquestion():
 return '''
    <form action="/tryquestion" method="post">
        Enter you question: <input name="tryquestion" type="text" size="35" />
        <input value="Search" type="submit" />
     </form>
    '''
#@post('/tryqustion') # or @route('/login', method='POST')
@bottle.route("/tryquestion", method="POST")
def answerq():
    q = request.forms.get('tryquestion')
  
    target, query, metadata = dbpedia.get_query(q)
    if isinstance(metadata, tuple):
            query_type = metadata[0]
            metadata = metadata[1]
    else:
            query_type = metadata
            metadata = None
    if query is None:
        yield u"<p>Query not generated :(</p>"
   
    yield u"<p>" + query + u"</p>"
    
    if target.startswith("?"):
            target = target[1:]
    if query:
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            if not results["results"]["bindings"]:
                yield u"<p>No answer found :(</p>"
  
    for result in results["results"]["bindings"]:
       yield "<p>" + result["x1"]["value"] + "</p>"
    return
     
bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

