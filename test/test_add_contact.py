# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Vasya", lastname="Petrov", address="Lenina", mobile="89689686868", email="test@gmail.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="", email=""))




