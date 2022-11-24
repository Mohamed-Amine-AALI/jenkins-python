from typing import List, Union


class InvalidParam(Exception):
    pass


# Fonctions
def invert(list_to_invert: List[int]) -> List[int]:
    inverted_list = [-i for i in list_to_invert]
    return inverted_list


def ascending_order(list_to_ascend_order: List[int]) -> List[int]:
    if type(list_to_ascend_order) is not list:
        raise InvalidParam()
    ordered_list = sorted(list_to_ascend_order)
    return ordered_list


def descending_order(list_to_descend_order: List[int]) -> List[int]:
    ordered_list = sorted(list_to_descend_order, reverse=True)
    return ordered_list


def get_sum(int_list: List[int]) -> int:
    return sum(int_list)


def double(int_list: List[int]) -> List[int]:
    doubled_list = [i * 2 for i in int_list]
    return doubled_list


# Tests unitaires :
def test_invert():
    list_to_invert = [1, 4, 9, -4, 0, 199]
    inverted_list = invert(list_to_invert)
    assert inverted_list == [-1, -4, -9, 4, 0, -199]


def test_ascending_order():
    list_to_order = [1, 99, 102, 45, 6]
    ordered_list = ascending_order(list_to_order)
    assert ordered_list == [1, 6, 45, 99, 102]

    try:
        ascending_order(list_to_ascend_order=1)
    except Exception as e:
        e == InvalidParam


def test_descending_order():
    list_to_order = [1, 99, 102, 45, 6]
    ordered_list = descending_order(list_to_order)
    assert ordered_list == [102, 99, 45, 6, 1]


def test_sum():
    assert get_sum([10, 20, 30, 100]) == 160


def test_double():
    list_to_double: List[int] = [100, 1000, 826, 2, 0]
    doubled_list = double(list_to_double)
    assert doubled_list == [200, 2000, 1652, 4, 0]


# ------------------------------------------------------------
# Tests avec des classes
# ------------------------------------------------------------


class Contact(object):
    def __init__(self, identity: str, phone_number: str) -> None:
        self.identity = identity
        self.phone_number = phone_number


class User(object):
    def __init__(
        self, first_name: str, last_name: str, contacts: List[Contact] = []
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.contacts = contacts

    def add_contacts(self, contacts: Union[List[Contact], Contact]) -> None:
        if isinstance(contacts, Contact):
            self.contacts.append(contacts)
        else:
            self.contacts += contacts

    def change_first_name(self, new_first_name: str) -> None:
        self.first_name = new_first_name

    def change_last_name(self, new_last_name: str) -> None:
        self.last_name = new_last_name

    def reset_contacts(self) -> None:
        self.contacts = []


def test_add_contacts():
    user: User = User(first_name="Mohamed-Amine", last_name="AALI", contacts=[])
    new_contact: Contact = Contact(identity="soeur", phone_number="0601363106")
    user.add_contacts(contacts=new_contact)
    assert len(user.contacts) == 1

    new_contacts: List[Contact] = [
        Contact(identity="maman", phone_number="0781450866"),
        Contact(identity="frère", phone_number="0781329266"),
    ]
    user.add_contacts(contacts=new_contacts)
    assert len(user.contacts) == 3


def test_reset_contacts():
    user: User = User(first_name="Mohamed-Amine", last_name="AALI", contacts=[])
    new_contact: Contact = Contact(identity="soeur", phone_number="0601363106")
    user.add_contacts(contacts=new_contact)
    assert len(user.contacts) == 1

    user.reset_contacts()
    assert len(user.contacts) == 0


def test_change_first_name():
    user: User = User(first_name="Mohamed-Amine", last_name="AALI", contacts=[])
    user.change_first_name(new_first_name="Faudel")
    assert user.first_name == "Faudel"


def test_change_last_name():
    user: User = User(first_name="Mohamed-Amine", last_name="AALI", contacts=[])
    user.change_last_name(new_last_name="Faudel")
    assert user.last_name == "Faudel"
