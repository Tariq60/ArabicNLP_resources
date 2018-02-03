import pandas as pd

names = pd.read_csv('behindthename.csv')
n = names['Name'].values

new_names = []
for i in n:
    new_names.append(i.decode('unicode_escape'))

names['Name'] = new_names

f = open('behindthename_fixed_unicode.csv','wb')
for text in new_names:
    f.write(text.encode('utf-8'))
    f.write('\n')
f.close()
