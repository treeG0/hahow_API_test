# coding=utf-8
"""
==============================================================================
Name:       swapi_request.py

Purpose:    The Star Wars API request support

Author:     Huck
Created:    2/1/2022

==============================================================================
"""

import json
import requests
import configparser

class SwapiRequest:

    def __init__(self):
        pass

    def get_response_json(self, req):
        """
        parse data from a respond
        :req: string API request
        :return: json
        """
        res = requests.get(req)
        if res.status_code != 200:
            raise RuntimeError(res)
        return json.loads(res.text)

    def parse_data_withen_pages(self, category):
        """
        parse data for a category
        :category: string category( planets, starships, vehicles, people, films and species); otherwise, raise RuntimeError
        :return: json
        """
        #planets, starships, vehicles, people, films and species
        if category not in ('planets', 'starships', 'vehicles', 'people', 'films', 'species'):
            raise RuntimeError(category + 'is not a valid category.')
        res = self.get_response_json(self.baseurl+category)
        data = res['results']
        while res['next']:
            res = self.get_response_json(res['next'])
            data += res['results']

        return data

    def get_all_films(self):
        """
        get all films
        :return: json films
        """
        return self.parse_data_withen_pages('films')

    def get_all_vehicles(self):
        """
        get all vehicles
        :return: json films
        """
        return self.parse_data_withen_pages('vehicles')
