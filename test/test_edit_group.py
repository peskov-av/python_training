# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="test_edit!", header="test_edit!", footer="test_edit!"))
    app.session.logout()