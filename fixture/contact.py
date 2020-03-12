

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # init contact edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # init contact update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # init contact modify
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # init contact update
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # init contact deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()