#! /usr/bin/python

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$12-Mar-2014 3:18:35 PM$"

"""
Species related regex.
"""
from refo import Question, Group
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate
from dbpedia.dsl import IsSpecies, DefinitionOf, FiberOf


"""
class Species(Particle):
    regex = Plus(Pos("DT") | Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("VBD") | Pos("NNPS"))

    def interpret(self, match):
        name = match.words.tokens
       # print name
        return HasKeyword(name)
        #return name
 """  

class WhatIs(QuestionTemplate):
    """
    Ex: "What is an apple?"
    """
    
    regex = Lemma("what") + Lemma("be") + Question(Pos("DT")) + Group(Pos("NNP"), 'species') + Question(Pos("."))
            
    def interpret(self, match):
        label = match.species.tokens
        speciesName = IsSpecies()+ HasKeyword(label)
        print label
        name = DefinitionOf(speciesName)
        return name, "enum"
    

class FiberOfQuestion(QuestionTemplate):
    """
    Ex: "How much fiber in an apple?"
    """

    regex = Lemmas("how much") + Lemma("fiber") + Pos("IN") + Pos("DT") + Group(Pos("NNP"), 'species') + Question(Pos("."))
    
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        fiber = FiberOf(species)
        return fiber, "enum"