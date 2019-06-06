# from __future__ import unicode_literals
import scrapy

import json

import os

import scrapy

from scrapy.spiders import Spider

from scrapy.http import FormRequest

from scrapy.http import Request

from chainxy.items import ChainItem

from scrapy import signals

from scrapy.xlib.pydispatch import dispatcher

from lxml import etree

from lxml import html

import time

import pdb

import csv


class ParseAPI(scrapy.Spider):

	name = 'parseapi'

	domain = 'https://example.com'

	history = []

	name_list = []

	output = []


	def __init__(self):

		try:

			file_path = 'name_list.csv'

			with open(file_path, 'rb') as csvfile:

				spamreader = csv.reader(csvfile)

				for row in spamreader:

					code = row[0].split(';')[0]

					self.name_list.append(code)
				
		except Exception as e:

			print(e)


	def start_requests(self):

		# for name in self.name_list:

		# 	url = "http://www.url.com/name="+name

		# 	yield scrapy.Request(url, callback=self.parse) 

		yield scrapy.Request('https://example.com', callback=self.parse)


	def parse(self, response):

		# data = json.loads(response.body)

		data = []

		with open('raw_data.json') as jsonfile:

			data = json.load(jsonfile)	

		# item = ChainItem()

		item = {}

		item['FrequencyAllCultures'] = data['FrequencyAllCultures']

		item['FemalePercentAllCultures'] = data['FemalePercentAllCultures']

		item['MalePercentAllCultures'] = data['MalePercentAllCultures']

		gender_data = data['GenderDataItem']

		for gender in gender_data:

			# pdb.set_trace()

			field_name = ''

			for key, value in gender.items():

				if key == 'culture':

					field_name = value

				else:

					item[field_name + '_' + key] = value
		
		yield item