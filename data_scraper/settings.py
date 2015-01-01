# -*- coding: utf-8 -*-

# Scrapy settings for whoisauthor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'data_scraper'

SPIDER_MODULES = ['data_scraper.spiders']
NEWSPIDER_MODULE = 'data_scraper.spiders'
DOWNLOAD_DELAY = 0.5

ITEM_PIPELINES = {
    'data_scraper.pipelines.ForumPipeline': 300,
}

SQLALCHEMY_DATABASE_URI = "mysql://wia:wia@localhost:3306/wia?charset=utf8"

LOG_LEVEL = 'ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'whoisauthor (+http://www.yourdomain.com)'
