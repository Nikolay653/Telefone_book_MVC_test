import pytest
from contextlib import nullcontext as does_not_raize

from model import Contact, ContactsList
from pathlib import Path


class TestContactsList:

    def test_load_from_file(self, data_test_load_from_file):
        path, res, expectation = data_test_load_from_file
        with expectation:
            print(path)
            path = Path(path)
            t_model = ContactsList()
            t_model.load_from_file(path)
            assert len(t_model.contacts) == res

    def test_save_to_file(self, data_save_to_file):
        path, expectation = data_save_to_file
        with expectation:
            contacts = ContactsList()
            add_contact = Contact(
                1,
                "Максим",
                "Иванов",
                "Матвеевич",
                "+7(499)245-83-56",
                "Костоправы",
                "impiety embitter exposit",
            )
            contacts.add_contact(add_contact)
            contacts.save_to_file(path)
            assert Path(path).exists()

    def test_add_contact(self, data_test_add_contact):
        id_, name, last_name, surname, phone, company, comment, res = (
            data_test_add_contact
        )
        contacts = ContactsList()
        add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
        contacts.add_contact(add_contact)
        assert len(contacts.contacts) == res

    def test_find_contact_by_name(self, data_find_contact_by_name):
        id_, name, last_name, surname, phone, company, comment, res, expectation = (
            data_find_contact_by_name
        )
        with expectation:
            contacts = ContactsList()
            add_contact = Contact(
                id_, name, last_name, surname, phone, company, comment
            )
            contacts.add_contact(add_contact)
            result = contacts.find_contact_by_name("Максим")
            assert len(result) == res

    def test_update_contact(self, data_test_update_delete):
        id_, name, last_name, surname, phone, company, comment = data_test_update_delete
        contacts = ContactsList()
        add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
        new_contact = Contact(1, "t", "t", "t", "t", "t", "t")
        contacts.add_contact(add_contact)
        contacts.update_contact(0, new_contact)
        assert contacts.contacts[0].name == "t"

    def test_delete_contact(self, data_test_update_delete):
        id_, name, last_name, surname, phone, company, comment = data_test_update_delete
        contacts = ContactsList()
        add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
        contacts.add_contact(add_contact)
        contacts.delete_contact(1)
        assert contacts.contacts == []
