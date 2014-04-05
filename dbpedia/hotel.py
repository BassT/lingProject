#! /usr/bin/python

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$3-Apr-2014 1:35:39 PM$"

"""
Hotel related regex.
"""
from refo import Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dbpedia.dsl import IsHotel, LocationOf, LabelOf, NumOfRooms, NumOfRestaurants, OwnerOf, \
    OpeningDateOf, FloorCountOf, ExternalLinkOf


class Hotel(Particle):
    
    regex = Plus(Pos("CD") | Pos("JJ") |Pos("NNS") | Pos("DT") | Pos("NNP") | Pos("NNP") | Pos("NNP"))

    def interpret(self, match):
        name = match.words.tokens
        return IsHotel() + HasKeyword(name)
    

class ListHotelsQuestion(QuestionTemplate):
    """
    Ex: "list all hotels?"
        "list all hotels in dbpedia?"
    """
    
    regex = (Question(Lemma("list")) + Lemma("all") + Lemma("hotel") + Question(Pos("."))) | \
        (Question(Lemma("list")) + Lemma("all") + Lemma("hotel") + Pos("IN") + Lemma("dbpedia") + Question(Pos("."))) 
    
    def interpret(self, match):
        hotels = IsHotel()
        return LabelOf(hotels), "enum"
    
"""    

********** Add LocationOfQuestion to Basic.py **********

class LocationOfQuestion(QuestionTemplate):
    
    Ex: "Where is Jumeirah Beach Hotel?"
        "Where is the location of Jumeirah Beach Hotel?"
        "What is the location of Jumeirah Beach Hotel?"
        "Show me the location of Jumeirah Beach Hotel?"
        "Give me the location of Jumeirah Beach Hotel?"
    
    regex = (Lemma("where") + Lemma("be") + Hotel() + Question(Pos("."))) | \
         (Question(Lemmas("where be") | Lemmas("what be")) + Lemma("the") + Lemma("location") + Pos("IN") + Hotel() + Question(Pos("."))) | \
         (Question(Lemma("show")|Lemma("give")) + Lemma("me") + Lemma("the") + Lemma("location") + Pos("IN") + Hotel() + Question(Pos("."))) 
            
    def interpret(self, match):
        HotelLocation = LocationOf(match.hotel)
        return LabelOf(HotelLocation), "enum"
 """   

class NumberOfRoomsQuestion(QuestionTemplate):
    """
    Ex: "How many rooms in Jumeirah Beach Hotel?"
    """
    
    regex = (Lemmas("how many") + Lemma("rooms") + Pos("IN") + Hotel() + Question(Pos("."))) | \
        (Lemmas("how many") + Lemma("rooms") + Pos("IN") + Hotel() + Lemma("hotel") + Question(Pos(".")))
    
    def interpret(self, match):
        Rooms = NumOfRooms(match.hotel)
        return Rooms, "literal"
    

class NumberOfRestaurantsQuestion(QuestionTemplate):
    """
    Ex: "How many restaurants in Jumeirah Beach Hotel?"
    """
    
    regex = (Lemmas("how many") + Lemma("restaurant") + Pos("IN") + Hotel() + Question(Pos("."))) | \
        (Lemmas("how many") + Lemma("restaurant") + Pos("IN") + Hotel() + Lemma("hotel") +  Question(Pos(".")))
    
    def interpret(self, match):
        Restaurants = NumOfRestaurants(match.hotel)
        return Restaurants, "literal"


class OwnerOfQuestion(QuestionTemplate):
    """
    Ex: "who is the owner of Jumeirah Beach Hotel?"
    """
    
    regex = (Lemmas("who be") + Lemma("the") + Lemma("owner") + Pos("IN") + Hotel() + Question(Pos("."))) | \
        (Lemmas("who be") + Lemma("the") + Lemma("owner") + Pos("IN") + Hotel() + Lemma("hotel") +  Question(Pos(".")))
    
    def interpret(self, match):
        Owner = OwnerOf(match.hotel)
        return LabelOf(Owner), "enum"

    

class OpeningDateQuestion(QuestionTemplate):
    """
    Ex: "when was the opening of Jumeirah Beach Hotel?"
        "which date the Jumeirah Beach Hotel was opened?"
        "When did Jumeirah Beach Hotel opened?"
    """
    
    regex = (Lemmas("when be") + Lemma("the") + Lemma("open") + Pos("IN") + Hotel() + Question(Pos("."))) | \
        (Lemmas("when be") + Lemma("the") + Lemma("open") + Pos("IN") + Hotel() + Lemma("hotel") +  Question(Pos("."))) | \
        (Lemma("which") + Lemma("date") + Lemma("the") + Hotel() + Lemma("be") + Lemma("open") + Question(Pos("."))) | \
        (Lemma("which") + Lemma("date") + Lemma("the") + Hotel() + Lemma("hotel") + Lemma("be") + Lemma("open") + Question(Pos("."))) | \
        (Lemmas("when do") + Hotel() + Lemma("open") + Question(Pos("."))) | \
        (Lemmas("when do") + Hotel() + Lemma("hotel") + Lemma("open") + Question(Pos(".")))
    
    def interpret(self, match):
        Date = OpeningDateOf(match.hotel)
        return Date, "literal"
    
    
class FloorCountQuestion(QuestionTemplate):
    """
    Ex: "how many floors in Jumeirah Beach Hotel?"
    """
    
    regex = (Lemmas("how many") +  Lemma("floor") + Pos("IN") + Hotel() + Question(Pos("."))) | \
        (Lemmas("how many") +  Lemma("floor") + Pos("IN") + Hotel() + Lemma("hotel") +  Question(Pos(".")))
    
    def interpret(self, match):
        FloorCount = FloorCountOf(match.hotel)
        return FloorCount, "literal"
    
"""

********** Add LinkQuestion to NewBasic.py **********

class LinkQuestion(QuestionTemplate):
    
    Ex: "what is the link of Jumeirah Beach Hotel?"
        "what is the website of Jumeirah Beach Hotel?"
    
        
    regex = (Lemmas("what be") +  Lemma("the") + (Lemma("link") | Lemma("website")) + Pos("IN") + Hotel() + Question(Pos("."))) | \
        (Lemmas("what be") +  Lemma("the") + (Lemma("link") | Lemma("website")) + Pos("IN") + Hotel() + Lemma("hotel") + Question(Pos(".")))
    
    def interpret(self, match):
        Link = ExternalLinkOf(match.hotel)
        return Link, "enum"
"""  

