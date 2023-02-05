import re

url_input = input()
url_checked = re.match('^https?://[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*', url_input)
print(url_checked)
if url_checked:
    print('True')
else:
    print('False')
