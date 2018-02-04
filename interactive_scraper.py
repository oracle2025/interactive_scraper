import re
import MechanicalSoup
import requests

def convertString_to_Method(s):
    return re.sub('[^0-9a-zA-Z]+', '_', s).strip('_')

class scraper_form:
    def __init__(self, browser, form):
        self.browser = browser
        for i in form.find_all("input"):
            if i.has_attr('id'):
                l = form.find(attrs={"for": i['id']})
                name = convertString_to_Method(l.text)
                myid = i['id']
                fun = lambda myid=myid: form.find("input", id=myid)
                setattr(self, name, fun)
    def set_input_value(self, input_field, value):
        self.browser[input_field['name']] = value
    def select(self):
        browser.select_form()

class scraper:
    def __init__(self, browser):
        self.browser = browser
        forms = self.soup().find_all("form")
        for f in forms:
            self.process_form(f)
    def soup(self):
        return self.browser.get_current_page()
    def process_form(self, form):
        form_name = convertString_to_Method(form['action'])
        form_obj = scraper_form(self.browser, form)
        setattr(self, form_name, form_obj)
        return
        for i in form.find_all("input"):
            if i.has_attr('id'):
                l = form.find(attrs={"for": i['id']})
                name = convertString_to_Method(l.text)
                myid = i['id']
                fun = lambda: form.find("input", id=myid)
                setattr(self, name, fun)

