# -*- coding: utf-8 -*-
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from models import Post, get_session
from sqlalchemy.exc import IntegrityError

class ForumPipeline(object):
    def __init__(self):
        self.session = get_session()

    def process_item(self, item, spider):
        if spider.name in ['dou',]:
            try:
                p = Post(username = item['username'],
                        text = item['content'],
                        comment_id = item['comment_id']
                        )
                self.session.add(p)
                self.session.commit()
                print "record %s saved"%item['comment_id']
            except IntegrityError, e:
                self.session.rollback()
                print "record already saved"
            except Exception,e:
                self.session.rollback()
                print "Unknown esception: %s"%e
            return item