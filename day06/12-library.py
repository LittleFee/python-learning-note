from collections import OrderedDict

favorite_language=OrderedDict()
favorite_language['kiwi1']='python1'
favorite_language['kiwi2']='python2'
favorite_language['kiwi3']='python3'
favorite_language['kiwi4']='python4'
favorite_language['kiwi5']='python5'
favorite_language['kiwi6']='python6'
favorite_language['kiwi7']='python7'
favorite_language['kiwi8']='python8'
favorite_language['kiwi9']='python9'

for name,lang in favorite_language.items():
    print(name+':'+lang)

