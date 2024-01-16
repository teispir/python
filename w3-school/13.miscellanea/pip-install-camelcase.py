# pip install camelcase (to download and install camelcase package)

import camelcase

c = camelcase.CamelCase()

print(c) #camelcase Object

print(dir(c))

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

# This method capitalizes the first letter of each word.