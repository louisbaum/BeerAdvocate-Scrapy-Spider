# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 RuxitSynthetic/1.0 v1811908203 t3425716988635793755 smf=0"

class hopitem(Item):
    name = Field()
    aka = Field()
    characteristics = Field()
    purpose = Field()
    alpha_acid = Field()
    beta_acid = Field()
    co_humulone = Field()
    country = Field()
    myrcene = Field()
    humulene = Field()
    caryophyllene = Field()
    farnesene = Field()
    substitutes = Field()
    flavor = Field()
    citrus = Field()
    sweet_fruits = Field()
    green_fruits = Field()
    berries_curant = Field()
    cream_caramel= Field()
    woody_aromatic= Field()
    menthol= Field()
    herbal= Field()
    spicy= Field()
    grassy= Field()
    vegetal= Field()
    floral= Field()
    
class revitem(Item):
    name = Field()
    style = Field()
    stylegroup = Field()
    abv  = Field()
    score = Field()
    avg_rating = Field()
    num_reviews = Field()
    num_ratings = Field()
    brewery = Field()
    location = Field()
    availability = Field()
    wants = Field()
    gots = Field()
    user_id = Field()
    ba_score = Field()
    look = Field()
    smell = Field()
    taste = Field()
    mouth_feel = Field()
    overall = Field()
    date= Field()
    text= Field()
   