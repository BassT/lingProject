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
from dbpedia.dsl import IsSpecies, FiberOf, CarbsOf, FatOf, ProteinOf, SugarOf, IngredientOf, LabelOf


class FiberOfQuestion(QuestionTemplate):
    """
    Ex: "How much fiber in an Apple?"
        "How much fiber an Apple have"
        "Do Apple have fiber"
    """

    regex = (Lemmas("how much") + Lemma("fiber") + Pos("IN") + Pos("DT") + Group(Pos("NNP"), 'species') + Question(Pos("."))) | \
        (Lemmas("how much") + Lemma("fiber") + Pos("DT") + Group(Pos("NNP"), 'species') + Lemma("have") + Question(Pos("."))) | \
        (Lemma("do") + Group(Pos("NNP"), 'species') + Lemma("have") + Lemma("fiber") + Question(Pos(".")))       
    
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        fiber = FiberOf(species)
        return fiber, "enum"
    
class CarbsOfQuestion(QuestionTemplate):
    """
    Ex: "How much carbs in an apple?"
        "How much carbs an Apple have?"
        "Do Apple have carbs?"
    """

    regex = Lemmas("how much") + Lemma("carbs") + Pos("IN") + Pos("DT") + Group(Pos("NNP"), 'species') + Question(Pos(".")) | \
        (Lemmas("how much") + Lemma("carbs") + Pos("DT") + Group(Pos("NNP"), 'species') + Lemma("have") + Question(Pos("."))) | \
        (Lemma("do") + Group(Pos("NNP"), 'species') + Lemma("have") + Lemma("carbs") + Question(Pos(".")))   
    
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        carbs = CarbsOf(species)
        return carbs, "enum"
    
class FatOfQuestion(QuestionTemplate):
    """
    Ex: "How much fat in an apple?"
        "How much fat an Apple have?"
        "Do Apple have fat?"
    """

    regex = Lemmas("how much") + Lemma("fat") + Pos("IN") + Pos("DT") + Group(Pos("NNP"), 'species') + Question(Pos(".")) | \
        (Lemmas("how much") + Lemma("fat") + Pos("DT") + Group(Pos("NNP"), 'species') + Lemma("have") + Question(Pos("."))) | \
        (Lemma("do") + Group(Pos("NNP"), 'species') + Lemma("have") + Lemma("fat") + Question(Pos(".")))  
    
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        fat = FatOf(species)
        return fat, "enum"
    
class ProteinOfQuestion(QuestionTemplate):
    """
    Ex: "How much protein in an apple?"
        "How much protein an Apple have?"
        "Do Apple have protein?"
    """

    regex = Lemmas("how much") + Lemma("protein") + Pos("IN") + Pos("DT") + Group(Pos("NNP"), 'species') + Question(Pos(".")) | \
        (Lemmas("how much") + Lemma("protein") + Pos("DT") + Group(Pos("NNP"), 'species') + Lemma("have") + Question(Pos("."))) | \
        (Lemma("do") + Group(Pos("NNP"), 'species') + Lemma("have") + Lemma("protein") + Question(Pos(".")))  
    
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        protein = ProteinOf(species)
        return protein, "enum"
    
class SugarOfQuestion(QuestionTemplate):
    """
    Ex: "How much sugar in an Apple?"
        "How much sugar an Apple have?"
        "Do Apple have sugar?"
    """

    regex = Lemmas("how much") + Lemma("sugar") + Pos("IN") + Pos("DT") + Group(Pos("NNP"), 'species') + Question(Pos(".")) | \
        (Lemmas("how much") + Lemma("sugar") + Pos("DT") + Group(Pos("NNP"), 'species') + Lemma("have") + Question(Pos("."))) | \
        (Lemma("do") + Group(Pos("NNP"), 'species') + Lemma("have") + Lemma("sugar") + Question(Pos(".")))  
    
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        suger = SugarOf(species)
        return suger, "enum"
    
class IngredientOfQuestion(QuestionTemplate):
    """
    Ex: "what type of food uses Apple as ingredient?"
        "what kind of food uses Apple as ingredient?"
        "what food uses Apple as ingredient?"
        "list food uses Apple as ingredient?"
    """

    regex = (Lemmas("what type") | Lemmas("what kind")) + Pos("IN") + Lemma("food") + Lemma("use") + Group(Pos("NNP"), 'species') + Pos("IN") + Lemma("ingredient") + Question(Pos(".")) | \
        (Question((Lemma("list")) | (Lemma("what")))+ Lemma("food") + Lemma("use") + Group(Pos("NNP"), 'species') + Pos("IN") + Lemma("ingredient") + Question(Pos(".")))
     
    def interpret(self, match):
        name = match.species.tokens
        species = IsSpecies()+ HasKeyword(name)
        Ingredient = IngredientOf(species)
        label = LabelOf(Ingredient)
        return label, "enum"