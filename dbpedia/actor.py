#! /usr/bin/python

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$7-Apr-2014 01:56:27 PM$"

"""
Actor related regex.
"""
from refo import Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dbpedia.dsl import IsPerson, NumOfChildren, SpouseOf, NameOf, ActiveYears, \
    ProducedBy, ProducerOf, WriterBy, WriterOf, GuestBy, ShowGuestBy, LabelOf, IsMovie

class Actor(Particle):
    
    regex = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))
   

    def interpret(self, match):
        name = match.words.tokens
        print name
        return IsPerson() + HasKeyword(name)
   
   
class Movie(Particle):
    regex =  Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS") | Pos("DT"))

    def interpret(self, match):
        MovieName = match.words.tokens
        print MovieName
        return IsMovie() + HasKeyword(MovieName)
    
class ChildrenOfQuestion(QuestionTemplate):
    """
    Ex: "How many kids did Mel Gibson have?"
        "How many children does Tom Hanks have?"
    """
    
    regex = ((Lemmas("how many")) + (Lemma("child") | Lemma("kid")) + Lemma("do") + Actor() + Lemma("have") + Question(Pos("."))) 
   
    def interpret(self, match):
        NumOfKids = NumOfChildren(match.actor)
        return NumOfKids, "enum"
    

class SpouseOfQuestion(QuestionTemplate):
    """
    Ex: "who is Tom Hanks married to?"
        "who is Sandra Bullock married to?"
    """
    
    regex = ((Lemmas("who be")) + Actor() + Lemma("marry") + Pos("TO") + Question(Pos("."))) 
   
    def interpret(self, match):
        spouse = SpouseOf(match.actor)
        return NameOf(spouse), "enum"
    
    
class ActiveYearsOfQuestion(QuestionTemplate):
    """
    Ex: "when did Tom Cruise start acting?"
        "when did Jennifer Aniston first start acting?"
        "how long has Tom Hanks been acting?"
        "how long has Mel Gibson been an actor?"
    """
    
    regex = ((Lemmas("when do")) + Actor() + Question(Lemma("first")) + Lemma("start") + Lemma("act") + Question(Pos("."))) | \
        ((Lemma("how")) + Lemma("long") + Lemma("have") + Actor() + Lemma("be") + (Lemma("act") | Pos("DT") + Lemma("actor")) + Question(Pos(".")))
   
    def interpret(self, match):
        Years = ActiveYears(match.actor)
        return Years, "literal"
    
    
class MoviesByProducerQuestion(QuestionTemplate):
    """
    Ex: "List films produced by Brad Pitt"
        "Movies produced by Tom Cruise"
        "which movies did Mel Gibson produced?"
    """

    regex = (Question(Lemma("list")) + (Lemma("movie") | Lemma("film") | Lemma("movies") | Lemma("films")) +
             Question(Lemma("produce")) + Lemma("by") + Actor()) | \
            (Lemma("which") + (Lemma("movie") | Lemma("film")) + Lemma("do") +
             Actor() + Lemma("produce") + Question(Pos(".")))

    def interpret(self, match):
        movie = ProducedBy(match.actor)
        return NameOf(movie), "enum"
    

class ProducerOfQuestion(QuestionTemplate):
    """
    Ex: "Who is the producer of Cast Away?"
        "Who produce Vanilla Sky?"
    """

    regex = ((Lemmas("who be") + Pos("DT") + Lemma("producer") +
             Pos("IN") + Movie()) |
             (Lemma("who") + Lemma("produce") + Movie())) + \
            Question(Pos("."))

    def interpret(self, match):
        producer = ProducerOf(match.movie)
        return NameOf(producer), "enum"
    
    
class WriterByQuestion(QuestionTemplate):
    """
    Ex: "list movies written by Tom Hanks"
        "which movies did Sandra Bullock wrote?"
        "what films did Mel Gibson wrote?"
        "Films written by Tom Hanks"
    """

    regex = (Question(Lemma("list")) + (Lemma("movie") | Lemma("film") | Lemma("movies") | \
            Lemma("films")) + Lemma("write") + Pos("IN") +  Actor()) | \
            ((Lemma("which") | Lemma("what")) + (Lemmas("movie do") | Lemmas("film do")) +
             Actor() + Lemma("write") + Question(Pos(".")))

    def interpret(self, match):
        movie_name = WriterBy(match.actor)
        return NameOf(movie_name), "enum"
    

class WriterOfQuestion(QuestionTemplate):
    """
    Ex: "Who is the writer of Get the Gringo?"
        "Who wrote Making Sandwiches?"
    """

    regex = ((Lemmas("who be") + Pos("DT") + Lemma("writer") +
             Pos("IN") + Movie()) |
             (Lemma("who") + Lemma("write") + Movie())) + \
            Question(Pos("."))

    def interpret(self, match):
        wrtier = WriterOf(match.movie)
        return NameOf(wrtier), "enum"
    

class GuestByQuestion(QuestionTemplate):
    """
    Ex: "list movies that Brad Pitt appear as guest star"
        "Films that Jennifer Aniston appears in as guest?"
    """

    regex = (Question(Lemma("list")) + (Lemma("movie") | Lemma("film") | \
            Lemma("movies") | Lemma("films")) + Lemma("that") +  Actor() + Lemma("appear") + \
            Pos("IN") + Question(Pos("IN")) + Lemma("guest") + Question(Lemma("star")) + Question(Pos("."))) 
           
    def interpret(self, match):
        show_name = GuestBy(match.actor)
        return NameOf(show_name), "enum"
    
    
class ShowGuestByQuestion(QuestionTemplate):
    """
    Ex: "list shows that Tom Hanks appears in?"
        "Shows that invites Tom Cruise?"
        "Talk shows that Sandra Bullock appears in"
    """

    regex = (Question(Lemma("list")) + Question(Lemma("talk")) + (Lemma("show") | Lemma("shows")) + Pos("IN") +  Actor() + Lemma("appear") + \
            Pos("IN") + Question(Pos("."))) | \
        (Question(Lemma("list")) + Question(Lemma("talk")) + (Lemma("show") | Lemma("shows")) + Pos("IN") + Lemma("invite") + Actor() +  \
         Question(Pos("."))) 
           
    def interpret(self, match):
        show_name = ShowGuestBy(match.actor)
        return LabelOf(show_name), "enum"
    

