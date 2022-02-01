# coding=utf-8
"""
==============================================================================
Name:       test_swapi_request.py

Purpose:    unit test for The Star Wars API request support

Author:     Huck
Created:    2/1/2022

==============================================================================
"""
import unittest
from mock import patch, call
from support.swapi_request import SwapiRequest


class TestSwapiRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mock_swapi_request = SwapiRequest()

    @patch('support.swapi_request.requests')
    def test_resuest_succseefully(self, mock_request):
        req = 'url'
        mock_request.get().status_code = 200
        mock_request.get().text = '{"name": "Death Star"}'
        self.assertEqual(self.mock_swapi_request.get_response_json(
            req), {"name": "Death Star"})
        mock_request.get.assert_called_with(req)

    @patch('support.swapi_request.requests')
    def test_resuest_failed_and_raise_error(self, mock_request):
        req = 'films'
        mock_request.get().status_code = 444
        mock_request.get().text = '{"name": "Death Star"}'
        with self.assertRaises(RuntimeError):
            self.mock_swapi_request.get_response_json(req)

    def test_get_all_data_for_invalid_catagory_and_raise_error(self):
        with self.assertRaises(RuntimeError):
            self.mock_swapi_request.parse_data_withen_pages('xxxxxx')

    def test_get_all_data_in_one_page(self):
        with patch('support.swapi_request.SwapiRequest.get_response_json') as mock_get_response:
            expected_result = [{
                "title": "A Old Hope",
                "episode_id": 5,
            }]
            mock_get_response.return_value = {
                "count": 6,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "title": "A Old Hope",
                        "episode_id": 5,
                    }]
            }

            self.assertEqual(
                self.mock_swapi_request.parse_data_withen_pages('films'), expected_result)
            mock_get_response.assert_called_with(
                self.mock_swapi_request.baseurl+'films')

    def test_get_all_data_withen_multuple_page(self):
        with patch('support.swapi_request.SwapiRequest.get_response_json') as mock_get_response:
            expected_result = [{
                "title": "A Old Hope",
                "episode_id": 5,
            },                    {
                "title": "A New Hope",
                "episode_id": 9,
            }]
            mock_get_response.side_effect = [{
                "count": 6,
                "next": 'page=2',
                "previous": None,
                "results": [
                    {
                        "title": "A Old Hope",
                        "episode_id": 5,
                    }]
            }, {
                "count": 7,
                "next": None,
                "previous": 'page=1',
                "results": [
                    {
                        "title": "A New Hope",
                        "episode_id": 9,
                    }]
            }]

            self.assertEqual(
                self.mock_swapi_request.parse_data_withen_pages('films'), expected_result)
            mock_get_response.assert_has_calls(
                [call(self.mock_swapi_request.baseurl+'films'), call('page=2')])
