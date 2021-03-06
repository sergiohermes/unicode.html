import collections
import json
import unicodedata

l = list()
for codeptx in range(0x20000):
    try:
        c = chr(codeptx)
        n = unicodedata.name(c)
        cat = unicodedata.category(c)
        #if True: print('[{0:2}] {1:<60}{2:>4}'.format(cat, n, c))
        obj = collections.OrderedDict()
        obj['cpt'] = codeptx
        obj['n'] = n
        obj['cat'] = cat
        obj['c'] = c
        l.append(obj)
    except ValueError:
        pass
print(json.dumps(l, indent=1))
