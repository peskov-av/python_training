# -*- coding: utf-8 -*-
from model.contact import Contact



def test_modify_first_contact_username(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    app.session.logout()

def test_modify_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    app.session.logout()

def test_modify_first_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="New address"))
    app.session.logout()

def test_modify_first_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile="New mobile"))
    app.session.logout()

def test_modify_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email="New email"))
    app.session.logout()