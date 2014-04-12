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
    OpeningDateOf, FloorCountOf, ExternalLinkOf, NameOf


class Hotel(Particle):
    
    regex = Plus(Pos("CD") | Pos("JJ") |Pos("NNS") | Pos("DT") | Pos("NNP") | Pos("NNP") | Pos("NNP"))

    def interpret(self, match):
        name = match.words.tokens
        return IsHotel() + HasKeyword(name)
    

class ListHotelsQuestion(QuestionTemplate):
    """
    Regex for questions about listing all Hotels in dbpedia
    Ex: "list all hotels?"
        "list all hotels in dbpedia?"
        "all hotels in dbpedia"
    """
    
    regex = (Question(Lemma("list")) + Lemma("all") + Lemma("hotel") + Question(Pos("."))) | \
        (Question(Lemma("list")) + Lemma("all") + Lemma("hotel") + Pos("IN") + Lemma("dbpedia") + Question(Pos("."))) 
    
    def interpret(self, match):
        hotels = IsHotel()
        return NameOf(hotels), "enum"
    

class NumberOfRoomsQuestion(QuestionTemplate):
    """
    Regex for questions about the number of rooms in a hotel
    Ex: "How many rooms in Jumeirah Beach Hotel?"
    """
    
    regex = (Lemmas("how many") + Lemma("rooms") + Pos("IN") + Hotel() + Question(Lemma("hotel")) + Question(Pos(".")))
    
    def interpret(self, match):
        Rooms = NumOfRooms(match.hotel)
        return Rooms, "literal"
    

class NumberOfRestaurantsQuestion(QuestionTemplate):
    """
    Regex for questions about the number of restaurants in hotel
    Ex: "How many restaurants in The Peninsula Hong Kong hotel?"
    """
    
    regex = (Lemmas("how many") + Lemma("restaurant") + Pos("IN") + Hotel() + Question(Lemma("hotel")) + Question(Pos(".")))
    
    def interpret(self, match):
        Restaurants = NumOfRestaurants(match.hotel)
        return Restaurants, "literal"


class OwnerOfQuestion(QuestionTemplate):
    """
    Regex for questions about the owner of a hotel
    Ex: "who is the owner of Capital Hilton?"
    """
    
    regex = (Lemmas("who be") + Lemma("the") + Lemma("owner") + Pos("IN") + Hotel() + Question(Lemma("hotel")) + Question(Pos("."))) 
    
    def interpret(self, match):
        Owner = OwnerOf(match.hotel)
        return NameOf(Owner), "enum"

    

class OpeningDateQuestion(QuestionTemplate):
    """
    Regex for questions about the opening date of a hotel
    Ex: "When was the opening of Novotel Century Hong Kong hotel?"
        "Which date the Hyatt Regency Atlanta was opened?"
        "When did Hilton Chicago hotel opened?"
    """
    
    regex = (Lemmas("when be") + Lemma("the") + Lemma("open") + Pos("IN") + Hotel() + Question(Lemma("hotel")) + Question(Pos("."))) | \
        (Lemma("which") + Lemma("date") + Lemma("the") + Hotel() + Question(Lemma("hotel")) + Lemma("be") + Lemma("open") + Question(Pos("."))) | \
        (Lemmas("when do") + Hotel() + Question(Lemma("hotel")) + Lemma("open") + Question(Pos("."))) 
    
    def interpret(self, match):
        Date = OpeningDateOf(match.hotel)
        return Date, "literal"
    
    
class FloorCountQuestion(QuestionTemplate):
    """
    Regex for questions about the number of floors in a hotel
    Ex: "How many floors in The Peninsula New York hotel?"
    """
    
    regex = (Lemmas("how many") +  Lemma("floor") + Pos("IN") + Hotel() + Question(Lemma("hotel")) + Question(Pos(".")))
    
    def interpret(self, match):
        FloorCount = FloorCountOf(match.hotel)
        return FloorCount, "literal"

