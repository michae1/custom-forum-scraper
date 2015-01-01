# -*- coding: utf-8 -*-
#!/usr/bin/env python
import binascii
import re
from models import Post, get_session
import operator

print "started"

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

tw = 0
word_counts = {}

def update_words_counts(txt):
	global tw
	global word_counts
	utxt = txt.encode('utf8')
	#print utxt
	words = re.findall(u"[\w']+", txt, re.UNICODE)
	# remove short (1-2)
	for w in words:
		word = w.lower()
		if len(word)<4:
			continue
		tw += 1	
		# print word_counts
		if word not in word_counts:	
			word_counts[word] = 1
		else:
			word_counts[word] += 1

session = get_session()

posts = session.query(Post).all()

#1 get total counts

for post in posts:
	update_words_counts(post.text)

# for wc in word_counts:
# 	print "%s: %s"%(wc, word_counts[wc])

swc = sorted(word_counts.items(), key=operator.itemgetter(1))
for w in swc:
	print "%s: %s"%(w[0], w[1])
# print "Total: %s"%tw

author_counts = {}
