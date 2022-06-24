%%writefile mapper.py

import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    words = re.split("[,;\s]\s*", text, flags=re.UNICODE)
    for word in words:
        flag = False
        for w in list(word):
            if (w <= 'z' and w >= 'a') or (w <= 'Z' and w >= 'A'):
                flag = True
            else:
                flag = False
                break
        if flag is True:
            print(sys.stderr, "reporter:counter:Wiki stats,Total words,%d" % 1)
            print("%s\t%d" % (word.lower(), 1))