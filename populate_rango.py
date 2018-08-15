import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Python Beginner Cheat Sheet",
         "url":"https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/"} ]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
         "url":"http://flask.pocoo.org"} ]

    polish_pages = [
        {"title":"Wykop",
         "url":"http://www.wykop.pl"},
        {"title":"Onet",
         "url":"http://www.onet.pl"},
        {"title":"Wirtualna Polska",
         "url":"http://www.wp.pl"},
        {"title":"Interia",
         "url":"http://www.interia.pl"},
        {"title":"Bociany",
         "url":"http://www.bocianyonline.pl/kamery.html"}]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages},
            "Polska": {"pages": polish_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()