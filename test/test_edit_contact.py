# -*- coding: utf-8 -*-
from model.contact import Contact



def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="Vasya", lastname="Petrovich", address="Len.12", mobile="89689666767", email="edit@gmail.com"))
