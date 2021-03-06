# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.core import serializers

from utils.getters import *

#TODO sections je spatny nazev pro vsechny lepsi je asi neco jako clenove menu
#TODO to co je ted sections posilat jako nejakou strukturu ve ktere jsou zvlast jmena na zobrazeni a zvlast urls

def index(request):
    sections = get_sections('index')
    invitations = get_invitations()
    posts = get_all_posts()
    calendars = get_calendars('index')
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'pozvanky.html', {'sections': sections,
                                             'posts': posts,
                                             'current_section': '',
                                             'invitations': invitations,
                                             'calendars': calendars,
                                             'sponsors': sponsors,
                                             'contacts': contacts})

def section(request, section):
    sections = get_sections(section)
    posts = get_posts(section)
    cur_section = get_current_section(section)
    calendars = get_calendars(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    banner = get_banner(section)
    return render(request, 'front_page.html', {'sections': sections,
                                               'posts': posts,
                                               'current_section': cur_section,
                                               'calendars': calendars,
                                               'sponsors': sponsors,
                                               'contacts': contacts,
                                               'banner': banner})

def calendar(request, section):
    sections = get_sections(section)
    calendars = get_calendars(section)
    cur_section = get_current_section(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'calendar_alt.html', {'sections': sections,
                                                 'current_section': cur_section,
                                                 'sponsors': sponsors, 
                                                 'contacts': contacts,
                                                 'calendars': calendars})

def static(request, section, static):
    sections = get_sections(section)
    static = get_static(static)
    cur_section = get_current_section(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'article.html', {'sections': sections,
                                            'article': static,
                                            'current_section': cur_section,
                                            'sponsors': sponsors,
                                            'contacts': contacts})

def news_from_front(request):
    sections = get_sections('index')
    posts = get_all_posts()
    cur_section = get_current_section('index')
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'news.html', {'sections': sections,
                                         'posts': posts,
                                         'current_section': cur_section,
                                         'sponsors': sponsors,
                                         'contacts': contacts})

def news(request, section):
    sections = get_sections(section)
    posts = get_posts(section)
    cur_section = get_current_section(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'news.html', {'sections': sections,
                                         'posts': posts,
                                         'current_section': cur_section,
                                         'sponsors': sponsors,
                                         'contacts': contacts})

def article_by_id(request, section, article_id):
    sections = get_sections(section)
    article = get_article_by_id(article_id)
    cur_section = get_current_section(section) 
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'article.html', {'sections': sections,
                                            'article': article,
                                            'current_section': cur_section, 
                                            'sponsors': sponsors,
                                            'contacts': contacts})

def article_by_url(request, section, article_url):
    sections = get_sections(section)
    article = get_article_by_url(article_url)
    cur_section = get_current_section(section) 
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'article.html', {'sections': sections,
                                            'article': article,
                                            'current_section': cur_section, 
                                            'sponsors': sponsors,
                                            'contacts': contacts})

def article_range(request, section, start, end):
    sections = get_sections(section)
    posts = get_posts(section)[int(start):int(end)]
    cur_section = get_current_section(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'news.html', {'sections': sections,
                                         'posts': posts,
                                         'current_section': cur_section,
                                         'sponsors': sponsors,
                                         'contacts': contacts})

# kdyz se pripoji na url ve tvaru /<identifier>, tak se tim muze myslet bud sekce
# a nebo url, proto se musim rozhodnout, co z toho pouzit
# melo by to fungovat tak ze url se nikdy nebude shodovat s nazvem sekce, to
# osetrimje osetreno v generovani a ukladani url
def article_by_id_or_section(request, identifier):
    section = list(Section.objects.filter(url=identifier))
    if section != []:
        sections = get_sections(identifier)
        posts = get_posts(identifier)
        cur_section = get_current_section(identifier)
        calendars = get_calendars(identifier)
        sponsors = get_sponsors()
        contacts = get_contacts()
        banner = get_banner(identifier)
        return render(request, 'front_page.html', {'sections': sections,
                                                   'posts': posts,
                                                   'current_section': cur_section,
                                                   'calendars': calendars,
                                                   'sponsors': sponsors,
                                                   'contacts': contacts,
                                                   'banner': banner})
    else:
        return article_from_front_by_url(request, identifier)

def article_range_from_front(request, start, end):
    return article_range(request, 'index', start, end)
    
def article_from_front(request, article_id):
    return article_by_id(request, 'index', article_id)

def article_from_front_by_url(request, article_url):
    return article_by_url(request, 'index', article_url)

def react(request):
    return render(request, 'index.html')
