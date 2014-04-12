# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Basic questions for DBpedia.
"""

from refo import Group, Plus, Question
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle, \
                          Lemmas
from quepy.dsl import HasKeyword, IsRelatedTo, HasType
from dsl import LabelOf, IsPlace, \
    UTCof


# Openings
LISTOPEN = Lemma("list") | Lemma("name")


class Thing(Particle):
    regex = Question(Pos("JJ")) + (Pos("NN") | Pos("NNP") | Pos("NNS")) |\
            Pos("VBN")

    def interpret(self, match):
        return HasKeyword(match.words.tokens)


class ListEntity(QuestionTemplate):
    """
    Regex for questions like "List Microsoft software"
    """

    entity = Group(Pos("NNP"), "entity")
    target = Group(Pos("NN") | Pos("NNS"), "target")
    regex = LISTOPEN + entity + target

    def interpret(self, match):
        entity = HasKeyword(match.entity.tokens)
        target_type = HasKeyword(match.target.lemmas)
        target = HasType(target_type) + IsRelatedTo(entity)
        label = LabelOf(target)

        return label, "enum"


class WhatTimeIs(QuestionTemplate):
    """
    Regex for questions about the time
    Ex: "What time is it in Cordoba"
    """

    nouns = Plus(Pos("NN") | Pos("NNS") | Pos("NNP") | Pos("NNPS"))
    place = Group(nouns, "place")
    openings = (Lemma("what") +
        ((Token("is") + Token("the") + Question(Lemma("current")) +
        Question(Lemma("local")) + Lemma("time")) |
        (Lemma("time") + Token("is") + Token("it")))) | \
               Lemma("time")
    regex = openings + Pos("IN") + place + Question(Pos("."))

    def interpret(self, match):
        place = HasKeyword(match.place.lemmas.title()) + IsPlace()
        utc_offset = UTCof(place)

        return utc_offset, "time"