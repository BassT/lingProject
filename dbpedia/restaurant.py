#! /usr/bin/python

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$9-Apr-2014 03:32:21 PM$"

"""
Restaurant related regex.
"""
from refo import Question, Plus, Group
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dbpedia.dsl import IsRestaurant, CityOf, FoodTypeOf, AddressOf, DressOf, \
    ChefOf, NameOf

class Restaurant(Particle):
    
    regex = Plus(Pos("NNS") | Pos("NNP") | Pos("NNPS") | Pos("DT") | Pos("CD"))
   
    def interpret(self, match):
        name = match.words.tokens
        return IsRestaurant() + HasKeyword(name)
    
    
class ListRestaurantInCityQuestion(QuestionTemplate):
    """
    Regex for questions about listing all restaurants in a city
    Ex: "list all restaurants in New York City?"
        "Restaurants in London?"  
    """
    
    city = Group(Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS")), "city")
    
    regex = (Question(Lemma("list")) + Question(Lemma("all")) + (Lemma("restaurant") |Lemma("restaurants")) + Pos("IN") + city + Question(Pos("."))) 
    
    def interpret(self, match):
        city = HasKeyword(match.city.tokens)
        restaurants = IsRestaurant() + CityOf(city)
        return NameOf(restaurants), "enum"
    

class TypeOfFoodQuestion(QuestionTemplate):
    """
    Regex for questions about the type of food a restaurant serve
    Ex: "What type of food does Oyster Bar serve?"
        "What kind of food does Beigel Bake restaurant have?"  
    """
     
    regex = (Lemma("what") + (Lemma("type") | Lemma("kind")) + Pos("IN") + Lemma("food") + Lemma("do") + \
            Restaurant() + Question(Lemma("restaurant")) + (Lemma("serve") | Lemma("have")) + Question(Pos(".")))
    
    def interpret(self, match):
        Type = FoodTypeOf(match.restaurant)
        return Type, "enum"
    

class AddressOfQuestion(QuestionTemplate):
    """
    Regex for questions asking about the address of a restaurant
    Ex: "What is the address of Square Boy restaurant?"
        "where is Brasserie Julien located?"  
    """
     
    regex = (Lemmas("what be") + Pos("DT") + Lemma("address") + Pos("IN") + \
            Restaurant() + Question(Lemma("restaurant")) + Question(Pos("."))) | \
            (Lemmas("where be") + Restaurant() + Lemma("locate") + Question(Lemma("restaurant")) + Question(Pos(".")))
    
    def interpret(self, match):
        address = AddressOf(match.restaurant)
        return address, "enum"
    
    
class DressOfQuestion(QuestionTemplate):
    """
    Regex for questions about the dress code in a restaurant
    Ex: "What is the dress code in The Ivy restaurant?"
        "What can I wear at the Oyster Bar?" 
        "What should you wear at 21 Club restaurant?"
    """
     
    regex = (Lemmas("what be") + Pos("DT") + Lemma("dress") + Lemma("code") + Pos("IN") + \
            Restaurant() + Question(Lemma("restaurant")) + Question(Pos("."))) | \
            ((Lemmas("what should") | Lemmas("what can")) + (Lemma("you") | Lemma("i")) + Lemma("wear") + \
            Pos("IN") + Question(Lemma("the")) + Restaurant() + Question(Lemma("restaurant")) + Question(Pos(".")))
    
    def interpret(self, match):
        DressType = DressOf(match.restaurant)
        return DressType, "enum"
   
   
class ChefOfQuestion(QuestionTemplate):
    """
    Regex for questions asking about the head chef of a restaurant
    Ex: "who is the chef of The Ivy?"
        "who is the head chef of 21 Club restaurant?"
    """
    
    regex = (Lemmas("who be") + Lemma("the") + Question(Lemma("head")) + Lemma("chef") + Pos("IN") + \
        Restaurant() + Question(Lemma("restaurant")) + Question(Pos("."))) 
    
    def interpret(self, match):
        ChefName = ChefOf(match.restaurant)
        return ChefName, "enum"