# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_first_contact_username(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

def test_modify_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(address="New address"))

def test_modify_first_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(mobile="New mobile"))

def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(email="New email"))
