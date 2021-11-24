# import webbrowser
# import random
# import string
# # webbrowser.open('http://google.com')  # Go to example.com
# # d = {}
# # d.get('5':['2'])
# # print(d)


import pandas as pd

# df = pd.DataFrame(index=['New link'],columns=['Original link','Counter'])
# pd.DataFrame.to_json(df)
# df.to_json('data')
print(pd.read_json('data.json'))
df = pd.read_json('data.json')

df['aa'] = [{"Original link":'google','Counter': 0}]
print(df)