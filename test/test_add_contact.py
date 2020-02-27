# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact_page(Contact("Vasya", "Petrov", "Lenina", "89689686868", "test@gmail.com"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact_page(Contact("", "", "", "", ""))
    app.logout()



