#! /usr/bin/python

# Author: Fatema Alabdulkareem <fatima@cse.yorku.ca> | <faa@yorku.ca>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.

__author__="Fatima"
__date__ ="$4-Apr-2014 7:56:21 PM$"

"""
University related regex.
"""
from refo import Question, Plus
from quepy.dsl import HasKeyword
from quepy.parsing import Lemma, Lemmas, Pos, QuestionTemplate, Particle
from dbpedia.dsl import IsUniversity, GradStudentOf, UnderGradStudentOf, StaffOf, \
    ColorOf, MottoOf, EstablishOf, NicknameOf, UniversityOwnerOf, LabelOf, NameOf


class University(Particle):
    
    regex = Plus(Pos("CD") | Pos("JJ") |Pos("NNS") | Pos("DT") | Pos("NNP") | Pos("NNP") | Pos("NNP") | Pos("IN"))

    def interpret(self, match):
        name = match.words.tokens
        return IsUniversity() + HasKeyword(name)
    
    
class ListUniversitiesQuestion(QuestionTemplate):
    """
    Ex: "list all universities?"
        "list all universities in dbpedia?"
    """
    
    regex = (Question(Lemma("list")) + Lemma("all") + Lemma("university") + Question(Pos("."))) | \
        (Question(Lemma("list")) + Lemma("all") + Lemma("university") + Pos("IN") + Lemma("dbpedia") + Question(Pos("."))) 
    
    def interpret(self, match):
        University = IsUniversity()
        return LabelOf(University), "enum"


class GradStudentQuestion(QuestionTemplate):
    """
    Ex: "How many postgraduate students in York University?"
        "How many post grad students in University of Toronto?"
        "How many post graduate students in University of Toronto?"
        "Number of postgraduate students in York University?"
        "Number of post grad students in Harvard University?"
        "Number of post graduate students in Harvard University?"    
    """
    
    regex = ((Lemmas("how many")| Lemmas("number of")) + Lemma("postgraduate") + Lemma("student") + Pos("IN") + University() + Question(Pos("."))) | \
        ((Lemmas("how many") | Lemmas("number of")) + Lemma("post") + (Lemma("grad") | Lemma("graduate")) + Lemma("student") + Pos("IN") + University() + Question(Pos(".")))
   
    def interpret(self, match):
        GradStudent = GradStudentOf(match.university)
        return GradStudent, "literal"
    
    
class UndergradStudentQuestion(QuestionTemplate):
    """
    Ex: "How many undergraduate students in York University?"
        "How many under grad students in University of Toronto?"
        "How many under graduate students in University of Toronto?"
        "Number of undergraduate students in York University?"
        "Number of under grad students in McGill University?"
        "Number of under graduate students in McGill University?"
    """
    
    regex = ((Lemmas("how many") | Lemmas("number of")) + Lemma("undergraduate") + Lemma("student") + Pos("IN") + University() + Question(Pos("."))) | \
        ((Lemmas("how many")| Lemmas("number of")) + Lemma("under") + (Lemma("grad") | Lemma("graduate")) + Lemma("student") + Pos("IN") + University() + Question(Pos(".")))
   
    def interpret(self, match):
        UndergradStudent = UnderGradStudentOf(match.university)
        return UndergradStudent, "literal"
    
    
class NumberOfStaffQuestion(QuestionTemplate):
    """
    Ex: "How many staff in York University?"
        "How many staff working in McGill University?"
        "Number of staff in University of Toronto?"
        "Number of staff working in University of Toronto?"
    """
    
    regex = ((Lemmas("how many") | Lemmas("number of")) + Lemma("staff") + Pos("IN") + University() + Question(Pos("."))) | \
        ((Lemmas("how many") | Lemmas("number of")) + Lemma("staff") + Lemma("work") + Pos("IN") + University() + Question(Pos(".")))
   
    def interpret(self, match):
        staff = StaffOf(match.university)
        return staff, "literal"
    
    
class ColorOfQuestion(QuestionTemplate):
    """
    Ex: "What is York University colors?"
        "What is York University color?"
        "What is the colors of University of Toronto?"
        "What is the color of University of Toronto?"
    """

    regex = (Lemmas("what be") + University() + (Lemma("colors")|Lemma("color")) + Question(Pos("."))) | \
        (Lemmas("what be") + Lemma("the") + (Lemma("colors")|Lemma("color")) + Pos("IN") + University() + Question(Pos(".")))

    def interpret(self, match):
        color = ColorOf(match.university)
        return color, "enum"
    
    
class MottoOfQuestion(QuestionTemplate):
    """
    Ex: "What is the motto of York University?"
        "What is University of Toronto motto?"
    """

    regex = (Lemmas("what be") + University() + Lemma("motto") + Question(Pos("."))) | \
        (Lemmas("what be") + Lemma("the") + Lemma("motto") + Pos("IN") + University() + Question(Pos(".")))

    def interpret(self, match):
        motto = MottoOf(match.university)
        return motto, "enum"


class EstablishOfQuestion(QuestionTemplate):
    """
    Ex: "when was the establishment of McGill University?"
        "on which date York University was established?"
        "which date Harvard University was established?"
        "When did University of Toronto established?"
    """
    
    regex = (Lemmas("when be") + Lemma("the") + Lemma("establishment") + Pos("IN") + University() + Question(Pos("."))) | \
        ((Lemma("which") | Lemmas("on which")) + Lemma("date") +  University() + Lemma("be") + Lemma("establish") + Question(Pos("."))) | \
        (Lemmas("when do") + University() + Lemma("establish") + Question(Pos(".")))
    
    def interpret(self, match):
        Date = EstablishOf(match.university)
        return Date, "literal"


class NicknameOfQuestion(QuestionTemplate):
    """
    Ex: "What is the nickname of York University?"
        "What is University of Toronto nickname?"
    """

    regex = (Lemmas("what be") + University() + Lemma("nickname") + Question(Pos("."))) | \
        (Lemmas("what be") + Lemma("the") + Lemma("nickname") + Pos("IN") + University() + Question(Pos(".")))

    def interpret(self, match):
        nick = NicknameOf(match.university)
        return nick, "enum"
    
    
class UniversityOwnerOfQuestion(QuestionTemplate):
    """
    Ex: "What does York University own?"
        "What does University of Toronto own?"
        "List some properties owned by Harvard University?"
        "Some properties owned by McGill University?"
    """

    regex = (Lemmas("what do") + University() + Lemma("own") + Question(Pos("."))) | \
        (Question(Lemma("list")) + Lemma("some") + Lemma("property") + Lemma("own") + Pos("IN") + University() + Question(Pos(".")))

    def interpret(self, match):
        own = UniversityOwnerOf(match.university)
        return NameOf(own), "enum"