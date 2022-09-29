import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.new_pet import NewPet  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server import util


Pet1 = Pet(name="Tom", id=1)
Pet2 = Pet(name="Jerry", id=2)
Pet3 = Pet(name="Tommy", id=3)
Pet4 = Pet(name="Jeremy", id=4)
Pet5 = Pet(name="Roger", id=5)
Pet6 = Pet(name="Poodle", id=6)
Pet7 = Pet(name="Simon", id=7)
Pet8 = Pet(name="Puffy", id=8)
Pet9 = Pet(name="Bubbles", id=9)
Pet10 = Pet(name="Daisy", id=10)
Pets = [Pet1, Pet2, Pet3, Pet4, Pet5, Pet6, Pet7, Pet8, Pet9, Pet10]

def add_pet(new_pet):  # noqa: E501
    """add_pet

    Creates a new pet in the store. Duplicates are allowed # noqa: E501

    :param new_pet: Pet to add to the store
    :type new_pet: dict | bytes

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_pet = NewPet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_pet(id):  # noqa: E501
    """delete_pet

    deletes a single pet based on the ID supplied # noqa: E501

    :param id: ID of pet to delete
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_pet_by_id(id):  # noqa: E501
    """find_pet_by_id

    Returns a pet based on its ID # noqa: E501

    :param id: ID of pet to fetch
    :type id: int

    :rtype: Union[Pet, Tuple[Pet, int], Tuple[Pet, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_pets(tags=None, limit=None):  # noqa: E501
    """find_pets

    Returns all pets from the system that the user has access to # noqa: E501

    :param tags: tags to filter by
    :type tags: List[str]
    :param limit: maximum number of results to return
    :type limit: int

    :rtype: Union[List[Pet], Tuple[List[Pet], int], Tuple[List[Pet], int, Dict[str, str]]
    """
    return Pets
