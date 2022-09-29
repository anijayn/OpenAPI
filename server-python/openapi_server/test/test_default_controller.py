# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_pet import NewPet  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_pet(self):
        """Test case for add_pet

        
        """
        new_pet = {
  "name" : "name",
  "tag" : "tag"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/pets',
            method='POST',
            headers=headers,
            data=json.dumps(new_pet),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pet(self):
        """Test case for delete_pet

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/pets/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_pet_by_id(self):
        """Test case for find_pet_by_id

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/pets/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_pets(self):
        """Test case for find_pets

        
        """
        query_string = [('tags', ['tags_example']),
                        ('limit', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/pets',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
