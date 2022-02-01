# coding=utf-8
"""
==============================================================================
Name:       api_test.py

Purpose:    1) 有多少不同種族的人出現在第六部？
            2) 請依據電影集數去排序電影名字？
            3) 請幫我挑出電影裡所有的車輛，馬力超過１０００的。

Author:     Huck
Created:    2/1/2022

==============================================================================
"""

from support.swapi_request import SwapiRequest
from integration.dut_base import SUTBase
import logging


class APITest(SUTBase):

    @classmethod
    def setUpClass(cls):
        cls.swapi = SwapiRequest()
        super().setUpClass()

    def test_species_amount_in_film(self):
        """
        Test how many different species appears in film episode 6
        """
        for film in self.swapi.get_all_films():
            if film['episode_id'] == 6:
                logging.info(
                    str(len(film['species'])) + ' different species appears in film episode 3')
                self.assertEqual(len(film['species']), 9)

    def test_get_all_films_name(self):
        """
        Test listing all the film names and sort the name by episode_id
        """
        expected_result = ['The Phantom Menace', 'Attack of the Clones',
                           'Revenge of the Sith', 'A New Hope', 'The Empire Strikes Back', 'Return of the Jedi']

        films = self.swapi.get_all_films()
        film_names = [None]*len(films)

        for f in films:
            film_names[f['episode_id']-1] = f['title']

        logging.info(film_names)
        self.assertEqual(expected_result, film_names)

    def test_get_vehicles_max_atmosphering_speed_over_1000(self):
        """
        test finding out all vehicles which max_atmosphering_speed is over 1000
        """
        expected_result = {'Vulture Droid', 'Droid tri-fighter', 'T-16 skyhopper', 'Geonosian starfighter',
                           'TIE/LN starfighter', 'Storm IV Twin-Pod cloud car', 'TIE/IN interceptor'}
        vehicles = self.swapi.get_all_vehicles()

        vehicles_speed_over_1000 = set()

        for v in vehicles:
            if v['max_atmosphering_speed'] == 'unknown':
                continue
            if int(v['max_atmosphering_speed']) > 1000:
                vehicles_speed_over_1000.add(v['name'])

        logging.info(vehicles_speed_over_1000)
        self.assertEqual(expected_result, vehicles_speed_over_1000)
