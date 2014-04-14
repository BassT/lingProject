# Author: Sebastian Richter <sebric@t-online.de>
# This file is part of a final project for the course Computational Linguistics
# of the winter term 14/13 at York University by Nick Cercone.
from dbpedia.dsl import HasKeyword
from rdflib.plugins.sparql.parserutils import Comp

""" Company related regular expressions """

from refo import Group, Plus
from dsl import IsCompany, OwnedBy, NameOf, EquityOf, RevenueOf, AssetsOf, IndustryOf, DevelopedBy, LabelOf
from quepy.parsing import Lemma, Pos, QuestionTemplate

class OwnedByQuestion(QuestionTemplate):
	"""
	Regex for questions about which companies a company owns.
	Ex: Which companies are owned by Google?
	"""

	regex = Pos("WDT") + Lemma("company") + Lemma("be") + Lemma("own") + Pos("IN") + Group(Pos("NNP"), 'company') + Pos(".")

	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		ownedCompanies = OwnedBy(company)
		label = NameOf(ownedCompanies)
		return label, "enum"
	
class EquityOfQuestion(QuestionTemplate):
	"""
	Regex for questions about how much equity a company holds.
	Ex: How much equity does Google hold?
	"""
	
	regex = Pos("WRB") + Lemma("much") + Lemma("equity") + Lemma("do") + Group(Pos("NNP"), 'company') + Lemma("hold") + Pos(".")
	
	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		equity = EquityOf(company)
		return equity, "enum"
	
class RevenueOfQuestion(QuestionTemplate):
	"""
	Regex for questions about how much revenue a company makes.
	Ex: How much revenue does Google make?
	"""
	
	regex = Pos("WRB") + Lemma("much") + Lemma("revenue") + Lemma("do") + Group(Pos("NNP"), 'company') + Lemma("make") + Pos(".")
	
	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		revenue = RevenueOf(company)
		return revenue, "enum"
	
class AssetsQuestion(QuestionTemplate):
	"""
	Regex for questions about how much assets a company has.
	Ex: How much assets does Google have?
	"""
	
	regex = Pos("WRB") + Plus(Lemma("much") | Lemma("many")) + Plus(Lemma("asset") | Lemma("assets")) + Lemma("do") + Group(Pos("NNP"), 'company') + Lemma("have") + Pos(".")
	
	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		assets = AssetsOf(company)
		return assets, "enum"
	
class IndustriesQuestion(QuestionTemplate):
	"""
	Regex for questions about which industries a company belongs to.
	Ex: Which industries does Google belong to?
	"""
	
	regex = Pos("WDT") + Lemma("industry") + Lemma("do") + Group(Pos("NNP"), 'company') + Lemma("belong") + Lemma("to") + Pos(".")
	
	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		industries = IndustryOf(company)
		return industries, "enum"
	
class DeveloperQuestion(QuestionTemplate):
	"""
	Regex for questions about which products a company developed.
	Ex: Which products were developed by Google?
	"""
	
	regex = Pos("WDT") + Lemma("product") + Lemma("be") + Lemma("develop") + Lemma("by") + Group(Pos("NNP"), 'company') + Pos(".")
	
	def interpret(self, match):
		name = match.company.tokens
		company = IsCompany() + HasKeyword(name)
		products = DevelopedBy(company)
		labels = NameOf(products)
		return labels, "enum"
	