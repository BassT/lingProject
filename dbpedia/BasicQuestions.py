# coding: utf-8

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$4-Apr-2014 11:50:42 PM$"

"""
BasicQuestions related regex
"""

from refo import Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dbpedia.dsl import ExternalLinkOf, DefinitionOf, LocationOf, NameOf

class Thing(Particle):
    regex = Plus(Pos("CD") | Pos("JJ") |Pos("NNS") | Pos("DT") | Pos("NNP") | Pos("IN"))

    def interpret(self, match):
        name = match.words.tokens
        return HasKeyword(name)


class WhatIs(QuestionTemplate):
    """
    Regex for questions about what is a thing
    Ex: "What is York University?"
        "What is University of Toronot?"
        "What is Jumeirah Beach Hotel?"
        "What is Crowne Plaza?"
        "What is 21 Club?"
    """

    regex = Lemma("what") + Lemma("be") + Question(Pos("DT")) + Thing() + Question(Pos("."))

    def interpret(self, match):
        label = DefinitionOf(match.thing)
        return label, "define"


class LinkQuestion(QuestionTemplate):
    """
    Regex for questions about the website for a thing
    Ex: "what is the link of Jumeirah Beach Hotel?"
        "What is the website of InterContinental Hong Kong?"
        "what is the link of York University?"
        "what is the website of University of Toronto?"
        "what is the website of 21 Club?"
        "what is the link of The Ivy?"
    """
        
    regex = (Lemmas("what be") +  Lemma("the") + (Lemma("link") | Lemma("website")) + Pos("IN") + Thing() + Question(Pos("."))) 
    
    def interpret(self, match):
        Link = ExternalLinkOf(match.thing)
        return Link, "enum"
 
    
class LocationOfQuestion(QuestionTemplate):
    """
    Ex: "where in the world is the Eiffel Tower"
        "Where is Jumeirah Beach Hotel?"
        "Where is the location of Marriott London Park Lane?"
        "Show me the location of Jumeirah Beach Hotel?"
        "Give me the location of Jumeirah Beach Hotel?"
    """

                  
    regex = Lemma("where") + Question(Lemmas("in the world")) + Lemma("be") + Question(Pos("DT")) + Thing() + Question(Pos(".")) | \
        (Lemma("where") + Lemma("be") + Thing() + Question(Pos("."))) | \
        (Question(Lemmas("where be")) + Lemma("the") + Lemma("location") + Pos("IN") + Thing() + Question(Pos("."))) | \
        (Question(Lemma("show")|Lemma("give")) + Lemma("me") + Lemma("the") + Lemma("location") + Pos("IN") + Thing() + Question(Pos("."))) 
            

    def interpret(self, match):
        location = LocationOf(match.thing)
        location_name = NameOf(location)

        return location_name, "enum"