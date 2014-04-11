# coding: utf-8

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$4-Apr-2014 11:50:42 PM$"

"""
New Basic questions that are not supproted in basic.py
"""

from refo import Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dbpedia.dsl import ExternalLinkOf, DefinitionOf

class Thing(Particle):
    regex = Plus(Pos("CD")| Pos("NN") | Pos("JJ") |Pos("NNS") | Pos("DT") | Pos("NNP") | Pos("NNP") | Pos("NNP") | Pos("IN"))
    
    def interpret(self, match):
        name = match.words.tokens
        return HasKeyword(name)


class WhatIs(QuestionTemplate):
    """
    Regex for questions about what is a thing
    Ex: "What is a car"
        "What is York University?"
        "What is University of Toronot?"
        "What is Jumeirah Beach Hotel?"
    """

    regex = Lemma("what") + Lemma("be") + Question(Pos("DT")) + Thing() + Question(Pos("."))

    def interpret(self, match):
        label = DefinitionOf(match.thing)
        return label, "define"


class LinkQuestion(QuestionTemplate):
    """
    Regex for questions about the website for a thing
    Ex: "what is the link of Jumeirah Beach Hotel?"
        "what is the website of Jumeirah Beach Hotel?"
        "what is the link of York University?"
        "what is the website of University of Toronto?"
    """
        
    regex = (Lemmas("what be") +  Lemma("the") + (Lemma("link") | Lemma("website")) + Pos("IN") + Thing() + Question(Pos("."))) | \
        (Lemmas("what be") +  Lemma("the") + (Lemma("link") | Lemma("website")) + Pos("IN") + Thing() + Lemma("hotel") + Question(Pos(".")))
    
    def interpret(self, match):
        Link = ExternalLinkOf(match.thing)
        return Link, "enum"
    