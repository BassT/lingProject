# Author: Sebastian Richter <sebric@t-online.de>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.
from dbpedia.dsl import HasKeyword

""" Company related regular expressions """

from refo import Group
from dsl import IsCompany, OwnedBy, LabelOf, NameOf
from quepy.parsing import Lemma, Pos, QuestionTemplate, Token, Particle

class OwnedByQuestion(QuestionTemplate):
	"""
	Regex for questions about which companies a company owns.
	Ex: Which companies are owned by Google?
	"""

	regex = Pos("WDT") + Lemma("company") + Lemma("be") + Lemma("own") + Pos("IN") + Group(Pos("NNP"), 'company')

	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		ownedCompanies = OwnedBy(company)
		label = NameOf(ownedCompanies)
		return label, "enum"