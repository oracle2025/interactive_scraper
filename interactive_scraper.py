import re
import mechanicalsoup
import requests
from urllib.parse import urljoin

def convertString_to_Method(s):
    return re.sub('[^0-9a-zA-Z]+', '_', s).strip('_')

class link:
    def __repr__(self):
        return self.href
    def __init__(self, browser, href, base, scraper):
        self.browser = browser
        self.href = href
        self.base = base
        self.scraper = scraper
    def follow(self):
        self.browser.open(urljoin(self.base, self.href))
        self.scraper.index_the_page()
    __call__ = follow
    def download(self):
        pass

class scraper_form:
    def __repr__(self):
        return "Test()"
    def __str__(self):
        return "member of Test"
    def __init__(self, browser, form, scraper):
        self.browser = browser
        self.scraper = scraper
        for i in form.find_all("input"):
            l = False
            if i.has_attr('id'):
                l = form.find(attrs={"for": i['id']})
                if l:
                    name = convertString_to_Method(l.text)
            if not l and i.has_attr('placeholder'):
                l = i['placeholder']
                name = convertString_to_Method(l)
            if not l and i.has_attr('name'):
                l = i['name']
                name = convertString_to_Method(l)
            if l:
                # myid = i['id']
                myname = i['name']
                fun2 = lambda value, myname=myname: self.select().__setitem__(myname, value)
                fun = lambda myname=myname: form.find("input", attrs={"name":myname})
                setattr(self, name, fun)
                setattr(self, name+"_set", fun2)
    def set_input_value(self, input_field, value):
        self.browser[input_field['name']] = value
    def select(self):
        self.browser.select_form()
        return self.browser
    def submit(self):
        self.scraper.submit()

class scraper:
    def __init__(self, url):
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.open(url)
        self.index_the_page()
    def index_the_page(self):
        self.forms = []
        self.links = []
        soup = self.soup()
        self.tags = list(set([tag.name for tag in soup.find_all()]))
        for f in self.forms:
            delattr(self, f)
        for l in self.links:
            delattr(self, l)
        forms = self.soup().find_all("form")
        for f in forms:
            self.process_form(f)
        self.process_links(self.soup())
    def soup(self):
        return self.browser.get_current_page()
    def process_links(self, soup):
        for a in soup.find_all('a'):
            href = a.get("href")
            text = convertString_to_Method(a.text)
            if (href and text):
                setattr(self, "link_"+ text, link(self.browser, href,
                    self.browser.get_url(), self))
                self.links.append("link_" + text)
    def process_form(self, form):
        if form.has_attr('action'):
            form_name = convertString_to_Method(form['action'])
        elif form.has_attr('id'):
            form_name = convertString_to_Method(form['id'])
        form_obj = scraper_form(self.browser, form, self)
        setattr(self, form_name, form_obj)
        self.forms.append(form_name)
    def submit(self):
        self.browser.submit_selected()
        self.index_the_page()

