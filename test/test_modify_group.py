# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.modify_first_group(Group(header="New header"))


def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test"))
    app.group.modify_first_group(Group(footer="New footer"))