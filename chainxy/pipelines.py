# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

import time

import datetime

from scrapy import signals

# from scrapy.contrib.exporter import CsvItemExporter

import pdb

class ChainxyPipeline(object):

    def __init__(self):

        self.file = {}

        self.headers = []

        # self.headers = ['FrequencyAllCultures', 'FemalePercentAllCultures','MalePercentAllCultures', 
        #         'AMBIGUOUS_frequency', 'AMBIGUOUS_femalePercent', 'AMBIGUOUS_malePercent', 'ANGLO_femalePercent',
        #         'ANGLO_frequency', 'ANGLO_malePercent']

        self.count = 0

        self.file_number = 0

        self.data_list = []
        

    @classmethod
    def from_crawler(cls, crawler):

        pipeline = cls()

        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)

        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)

        return pipeline


    def spider_opened(self, spider):

        pass


    def spider_closed(self, spider):

        with open('%s.csv' %spider.name, mode='w') as employee_file:

            self.exporter = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for key, value in self.data_list[0].items():

                if key != 'FrequencyAllCultures' and key != 'FemalePercentAllCultures' and  key != 'MalePercentAllCultures':

                    self.headers.append(key)

            self.headers.sort()

            self.headers.append('FrequencyAllCultures')

            self.headers.append('FemalePercentAllCultures')

            self.headers.append('MalePercentAllCultures')

            self.exporter.writerow(self.headers)

            for data in self.data_list:

                temp = []

                for key in self.headers:

                    temp.append(str(data[key]))
            
                self.exporter.writerow(temp)


    def process_item(self, item, spider):

        self.data_list.append(item)

        return item