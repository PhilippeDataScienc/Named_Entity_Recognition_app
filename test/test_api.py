import unittest
import json
from flask import request

from app import app

class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "I am happy to develop in python."})
            assert response._status_code == 200

    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Eddy Mitchell is a poor singer"})
            data = json.loads(response.get_data())
            assert data['entities'][0]['ent'] == 'Eddy Mitchell'
            assert data['entities'][0]['label'] == 'Person'