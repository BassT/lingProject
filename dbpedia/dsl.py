# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

"""
Domain specific language for DBpedia quepy.
"""

from quepy.dsl import FixedType, HasKeyword, FixedRelation, FixedDataRelation

# Setup the Keywords for this application
HasKeyword.relation = "rdfs:label"
HasKeyword.language = "en"


class IsPerson(FixedType):
    fixedtype = "foaf:Person"


class IsPlace(FixedType):
    fixedtype = "dbpedia:Place"


class IsCountry(FixedType):
    fixedtype = "dbpedia-owl:Country"


class IsBand(FixedType):
    fixedtype = "dbpedia-owl:Band"


class IsAlbum(FixedType):
    fixedtype = "dbpedia-owl:Album"


class IsTvShow(FixedType):
    fixedtype = "dbpedia-owl:TelevisionShow"


class IsMovie(FixedType):
    fixedtype = "dbpedia-owl:Film"


class HasShowName(FixedDataRelation):
    relation = "dbpprop:showName"
    language = "en"


class HasName(FixedDataRelation):
    relation = "dbpprop:name"
    language = "en"


class DefinitionOf(FixedRelation):
    relation = "rdfs:comment"
    reverse = True


class LabelOf(FixedRelation):
    relation = "rdfs:label"
    reverse = True


class UTCof(FixedRelation):
    relation = "dbpprop:utcOffset"
    reverse = True


class PresidentOf(FixedRelation):
    relation = "dbpprop:leaderTitle"
    reverse = True


class IncumbentOf(FixedRelation):
    relation = "dbpprop:incumbent"
    reverse = True


class CapitalOf(FixedRelation):
    relation = "dbpedia-owl:capital"
    reverse = True


class LanguageOf(FixedRelation):
    relation = "dbpprop:officialLanguages"
    reverse = True


class PopulationOf(FixedRelation):
    relation = "dbpprop:populationCensus"
    reverse = True


class IsMemberOf(FixedRelation):
    relation = "dbpedia-owl:bandMember"
    reverse = True


class ActiveYears(FixedRelation):
    relation = "dbpprop:yearsActive"
    reverse = True


class MusicGenereOf(FixedRelation):
    relation = "dbpedia-owl:genre"
    reverse = True


class ProducedBy(FixedRelation):
    relation = "dbpedia-owl:producer"


class BirthDateOf(FixedRelation):
    relation = "dbpprop:birthDate"
    reverse = True


class BirthPlaceOf(FixedRelation):
    relation = "dbpedia-owl:birthPlace"
    reverse = True


class ReleaseDateOf(FixedRelation):
    relation = "dbpedia-owl:releaseDate"
    reverse = True


class StarsIn(FixedRelation):
    relation = "dbpprop:starring"
    reverse = True


class NumberOfEpisodesIn(FixedRelation):
    relation = "dbpedia-owl:numberOfEpisodes"
    reverse = True


class ShowNameOf(FixedRelation):
    relation = "dbpprop:showName"
    reverse = True


class HasActor(FixedRelation):
    relation = "dbpprop:starring"


class CreatorOf(FixedRelation):
    relation = "dbpprop:creator"
    reverse = True


class NameOf(FixedRelation):
    relation = "foaf:name"
    reverse = True


class DirectedBy(FixedRelation):
    relation = "dbpedia-owl:director"


class DirectorOf(FixedRelation):
    relation = "dbpedia-owl:director"
    reverse = True


class DurationOf(FixedRelation):
    # DBpedia throws an error if the relation it's
    # dbpedia-owl:Work/runtime so we expand the prefix
    # by giving the whole URL.
    relation = "<http://dbpedia.org/ontology/Work/runtime>"
    reverse = True


class HasAuthor(FixedRelation):
    relation = "dbpedia-owl:author"


class AuthorOf(FixedRelation):
    relation = "dbpedia-owl:author"
    reverse = True


class IsBook(FixedType):
    fixedtype = "dbpedia-owl:Book"


class LocationOf(FixedRelation):
    relation = "dbpedia-owl:location"
    language = "en"
    reverse = True

# ============================================ #
#    Domain specific language for company      #
# ============================================ #

class IsCompany(FixedType):
    fixedtype = "dbpedia-owl:Company"
    
class OwnedBy(FixedRelation):
    relation = "dbpedia-owl:owningCompany"
    
class EquityOf(FixedRelation):
    relation = "dbpedia-owl:equity"
    reverse = True
    
class RevenueOf(FixedRelation):
    relation = "dbpedia-owl:revenue"
    reverse = True

class AssetsOf(FixedRelation):
    relation = "dbpedia-owl:assets"
    reverse = True
    
class IndustryOf(FixedRelation):
    relation = "dbpedia-owl:industry"
    reverse = True
    
class DevelopedBy(FixedRelation):
    relation = "dbpedia-owl:developer"

# ============================================ #
#    Domain specific language for Species      #
# ============================================ #

class IsSpecies(FixedType):
    fixedtype = "dbpedia-owl:Species"

class FiberOf(FixedRelation):
    relation = "dbpprop:fiber" 
    reverse = True
    
class CarbsOf(FixedRelation):
    relation = "dbpprop:carbs" 
    reverse = True

class FatOf(FixedRelation):
    relation = "dbpprop:fat" 
    reverse = True
    
class ProteinOf(FixedRelation):
    relation = "dbpprop:protein"
    reverse = True
    
class SugarOf(FixedRelation):
    relation = "dbpprop:sugars"
    reverse = True

class IngredientOf(FixedRelation):
    relation = "dbpedia-owl:ingredient"
   
# ============================================ #
#    Domain specific language for Hotel        #
# ============================================ #

class IsHotel(FixedType):
    fixedtype = "dbpedia-owl:Hotel"
    
class NumOfRooms(FixedRelation):
    relation = "dbpedia-owl:numberOfRooms"  
    reverse = True
    
class NumOfRestaurants(FixedRelation):
    relation = "dbpedia-owl:numberOfRestaurants"  
    reverse = True
    
class OwnerOf(FixedRelation):
    relation = "dbpedia-owl:owner" 
    reverse = True
    
class OpeningDateOf(FixedRelation):
    relation = "dbpprop:openingDate"  
    reverse = True
    
class FloorCountOf(FixedRelation):
    relation = "dbpedia-owl:floorCount"  
    reverse = True
    
class ExternalLinkOf(FixedRelation):
    relation = "dbpedia-owl:wikiPageExternalLink"  
    reverse = True
    
# ============================================ #
#    Domain specific language for University   #
# ============================================ #

class IsUniversity(FixedType):
    fixedtype = "dbpedia-owl:University"
    
class GradStudentOf(FixedRelation):
    relation = "dbpedia-owl:numberOfPostgraduateStudents"
    reverse = True
    
class UnderGradStudentOf(FixedRelation):
    relation = "dbpedia-owl:numberOfUndergraduateStudents"
    reverse = True
    
class StaffOf(FixedRelation):
    relation = "dbpedia-owl:staff"
    reverse = True
    
class ColorOf(FixedRelation):
    relation = "dbpedia-owl:officialSchoolColour"
    reverse = True
    
class MottoOf(FixedRelation):
    relation = "dbpprop:mottoeng"
    reverse = True
    
class EstablishOf(FixedRelation):
    relation = "dbpprop:established"
    reverse = True
    
class NicknameOf(FixedRelation):
    relation = "foaf:nick"
    reverse = True
    
class UniversityOwnerOf(FixedRelation):
    relation = "dbpedia-owl:owner"
    
# ============================================ #
#    Domain specific language for Language     #
# ============================================ #

class IsLanguage(FixedType):
    fixedtype = "dbpedia-owl:Language"
    
class SpeakersOf(FixedRelation):
    relation = "dbpprop:speakers"
    reverse = True
    
class SpokenIn(FixedRelation):
    relation = "dbpedia-owl:spokenIn"
    reverse = True
    
class LanguageFamilyOf(FixedRelation):
    relation = "dbpedia-owl:languageFamily"
    reverse = True
    
class OfficialLanguageOf(FixedRelation):
    relation = "dbpprop:officialLanguages"
    
class CommonNameOf(FixedRelation):
    relation = "dbpprop:commonName"
    reverse = True
    
# ============================================ #
#    Domain specific language for Actor        #
# ============================================ #

class NumOfChildren(FixedRelation):
    relation = "dbpprop:children"
    reverse = True
    
class SpouseOf(FixedRelation):
    relation = "dbpprop:spouse"
    reverse = True
    
class ProducerOf(FixedRelation):
    relation = "dbpedia-owl:producer"
    reverse = True
    
class WriterBy(FixedRelation):
    relation = "dbpedia-owl:writer"
    
class WriterOf(FixedRelation):
    relation = "dbpedia-owl:writer"
    reverse = True
    
class GuestBy(FixedRelation):
    relation = "dbpedia-owl:guest"
    
class ShowGuestBy(FixedRelation):
    relation = "dbpprop:guests"

# ============================================ #
#    Domain specific language for Restaurant   #
# ============================================ #

class IsRestaurant(FixedType):
    fixedtype = "dbpedia-owl:Restaurant"
    
class CityOf(FixedRelation):
    relation = "dbpprop:city"
   
class FoodTypeOf(FixedRelation):
    relation = "dbpedia-owl:cuisine"
    reverse = True
    
class AddressOf(FixedRelation):
    relation = "dbpedia-owl:address"
    reverse = True
    
class DressOf(FixedRelation):
    relation = "dbpprop:dressCode"
    reverse = True
    
class ChefOf(FixedRelation):
    relation = "dbpprop:headChef"
    reverse = True    
