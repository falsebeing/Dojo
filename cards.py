import json
import requests
import time
from PIL import ImageTk, Image
from io import BytesIO
import shutil


IMAGE_CACHE = "/data/images"

ALL_CARDS = [
	'id',
	'oracle_id',
	'set_name',
	'rulings_uri',
	'layout',
	'all_parts',
	'cmc',
	'color_identity'
	'hand_modifier', # vanguard-exclusive
	'keywords', # holds important gameplay info
	'legalities',
	'life_modifier', # vanguard-exclusive
	'booster', # bool, found in boosters
	'games', # paper, arena, or mtgo
	'name',
	'prices'
]

ART_ATTRIBUTES = [
	'artist',
	'border_color',
	'illustration_id',
]

NORMAL_FACE_ATTRIBUTES = [
	'colors',
	'color_indicator',
	'loyalty',
	'image_uris',
	'flavor_text',
	'power',
	'toughness',
	'type_line',
	'oracle_text',
	'mana_cost',
]

MULTI_FACE_ATTRIBUTES = [
	'colors',
	'color_indicator', 
	'flavor_text',
	'image_uris',
	'loyalty',
	'mana_cost',
	'name',
	'oracle_text',
	'power',
	'printed_name',
	'printed_text',
	'printed_type_line',
	'toughness',
	'type_line',
]

BASIC_LAND = ['Island', 'Plains', 'Mountain', 'Forest', 'Swamp']


# Layout types with deferred implentation status
IGNORED_LAYOUTS = ['scheme', 'adventure', 'vanguard']


"""
Special inspection needs: 
oracle_text for any \n, as in for Fuse
image_uri

identify:
name vs printed name
printed everything - printed seems to be an extra line of cosmetic info, ie Huntmaster Liger
"""


# Separate tokens

class CardCatalog:
	def __init__(self):
		self.cards_json = json.load(open("data/cards.json", "r"))

		self.catalog = []
		self.fill_catalog()

		self.names_list = self.list_card_names()
		self.names_list_unique = self.list_unique_card_names()


	def list_unique_card_names(self):
		return list(set(self.names_list))

	def list_card_names(self):
		return [card['name'] for card in self.catalog if card['name'] not in BASIC_LAND]

	def _find_doubles(self):
		for card_i in range(len(self.catalog)):
			if self.catalog[card_i]['name'] not in ['Plains', 'Island', 'Mountain', 'Swamp', 'Forest']:
				for c in self.catalog[card_i+1:]:
					if c['id'] == self.catalog[card_i]['id']:
						print(f"{c['name']} has Double ====8=8=8=8=8=8=8=8=88=8=8=")

	def search_by_name_contains(self, name, case_sensitive=False):
		results = []
		for card in self.catalog:
			if case_sensitive == False:
				if name.lower() in card['name'].lower():
					results.append(card)
			else:
				if name in card['name']:
					results.append(card)
		return results

	def search_by_name_exact(self, name):
		results = []
		for card in self.catalog:
			if card['name'] == name:
				results.append(card)
		return results

	def lookup_by_name_and_set(self, name, set_name):
		for card in self.catalog:
			if name == card['name'] and set_name == card['set_name']:
				return card

	# fill_catalog and related functions
	def fill_catalog(self):

		for card_source in self.cards_json:
			self.catalog.append(self.create_card(card_source))

	def create_card(self, card_source):
		# core items for all cards
		card_dict = self.derive_core(card_source)

		# derive remaining items according to layout
		if card_dict['layout'] == 'normal':
			self.derive_normal(card_dict, card_source)
		elif card_dict['layout'] == 'flip':
			self.derive_flip(card_dict, card_source)
		elif card_dict['layout'] == 'split':
			self.derive_split(card_dict, card_source)
		elif card_dict['layout'] in ['transform', 'double_faced_token']:
			self.derive_double(card_dict, card_source)

		return card_dict

	def derive_core(self, card_source):
		return {k:v for (k,v) in card_source.items() if k in ALL_CARDS + ART_ATTRIBUTES}

	def derive_normal(self, card, card_source):
		card.update({k:v for (k,v) in card_source.items() if k in NORMAL_FACE_ATTRIBUTES})

	def derive_double(self, card, card_source):
		card['front_face'] = {k:v for (k,v) in card_source['card_faces'][0].items() if k in MULTI_FACE_ATTRIBUTES}
		card['back_face'] = {k:v for (k,v) in card_source['card_faces'][1].items() if k in MULTI_FACE_ATTRIBUTES}

	def derive_split(self, card, card_source):
		card['faces'] = card_source['card_faces']

	# assignment accuracy not tested
	def derive_flip(self, card, card_source):
		card['up'] = card_source['card_faces'][0]
		card['down'] = card_source['card_faces'][1]
	# -----end

	# polish card:
	# pull images
		


	# API 
	def fetch_by_id(self, id):
		request = requests.get(f"https://api.scryfall.com/cards/{id}")
		print(request.json())

	def retrieve_card_image(self, card):
		return requests.get(f"{card['image_uris']['normal']}")


class Card:
	def __init__(self, card_dict, owner=None):
		self.__dict__.update(card_dict)

		# holds additional types added in-game
		self.additional_types = []
		self.original_owner = owner
		self.owner = owner

		self.image = self.load_image()

	# store card images
	def load_image(self):
		pass

	# checks if Card currently qualifies as a particular type
	def check_type(self, card_type):
		return card_type in self.get_all_types()

	def get_all_types(self):
		return self.type_line.replace('-', '').split() + self.additional_types
	# -----end

	def fetch_value(self):
		pass
		# return (fetch price from api)


class Standard(Card):
	def __init__(self, card_dict):
		super().__init__(card_dict)


class Flip(Card):
	def __init__(self, card_dict):
		super().__init__(card_dict)

	def flip(self):
		pass


class Split(Card):
	def __init__(self, card_dict):
		super().__init__(card_dict)


class Double(Card):
	def __init__(self, card_dict):
		super().__init__(card_dict)


class Deck:
	def __init__(self, owner, cards):
		self.owner = owner
		self.cards = cards

		self.wld = (0,0,0)

	def add_value(self):
		return sum([card.fetch_value() for card in self.cards])


if __name__ == "__main__":
	cardcatalog = CardCatalog()
	a = Card(cardcatalog.catalog[200])
	print(a.name, a.power, a.toughness, a.cmc, a.artist, a.prices['usd'])
	for i in range(1000):
		print('Island' in cardcatalog.names_list)


	types =0
	ntypes=0
	for card in cardcatalog.catalog:

		if 'type_line' in card.keys():
			types += 1
		else:
			ntypes += 1
			print(card)
			print('\n\n')

	print(types, ntypes)

	for name in cardcatalog.names_list_unique:
		print(name)