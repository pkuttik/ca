import re
from collections import Counter
from collections import OrderedDict
c =re.compile(r'(\+|-)?\d+')
m = c.search('-2029.0')
# print(m)
# f = re.findall('(\+|-)?(\d+)','+2029.20', re.DEBUG)
f = re.findall('\w+','This This has has to be completed by 10.30 AM for 20 $', re.DEBUG)
m = re.search('(\w+)','This This has has to be completed by 10.30 AM for 20 $', re.DEBUG)
# print(dict(Counter(f)))
print(m.groups())
m = re.search('b(c?)', 'cba')
print(m.group(0))
# print(f)
# print(f, m.span(), m.group())
# print(re.split('[a-z]+', 'words words'))
# print(re.split('\W+', 'Words, words, words.'))
print(dict(Counter('Hello my counter'.replace(' ', ''))))