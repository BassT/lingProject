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
import os

import quepy
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
dbpedia = quepy.install("dbpedia")

# quepy.set_loglevel("DEBUG")

@bottle.route("/")
def index():
    target, query, metadata = dbpedia.get_query("what is a blowtorch?")
    yield query + "\n"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        yield(result["x1"]["value"])
    return

bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
