# -*- coding: utf-8 -*-
import scrapy
from data_scraper.items import PostItem
from HTMLParser import HTMLParser
import re

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

class DouSpider(scrapy.Spider):
    name = "dou"
    allowed_domains = ["dou.ua"]
    start_urls = (
        'http://www.dou.ua/forum/',
    )

    def parse(self, response):
        # get initial topic links
        articles = response.selector.css('div.b-forum-articles article')

        for article in articles:
            link = article.css("h2 a::attr(href)").extract()
            yield scrapy.http.Request(
                url = link[0],
                callback=self.parse_topic,
            )

    def parse_topic(self, response):
        author = response.selector.css('div.b-post-info div.author img::attr(title)')
        topic = response.selector.css('article.b_typo').extract()
        comments = response.selector.css('div.l-comment')
        for comment in comments:
            name = comment.css('div.details a.avatar img::attr(title)').extract()
            content = comment.css('div.text').extract()
            comment_id = comment.css('div.details a.comment-link::attr(href)').extract()
            
            item = PostItem()
            item['username'] = name[0],
            # strip quote text
            if isinstance(content, list) and len(content)>0:
                item['content'] = strip_tags(re.sub('<blockquote>.*?</blockquote>', '',content[0])),
            else:
                item['content'] = strip_tags(re.sub('<blockquote>.*?</blockquote>', '',content)),
            item['comment_id'] = comment_id[0]
            yield item