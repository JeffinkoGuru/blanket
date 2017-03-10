from blanket import *

blanket = Blanket()
encoded = blanket.cover("payload")

print (encoded)

print (blanket.uncover(encoded))
