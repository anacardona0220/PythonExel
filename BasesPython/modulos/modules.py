import sys
import re
import time
text = 'Mi numero de telefono es 311 y el dog del pais 54'
result = re.findall('[0-9]+', text)
print(result)

print('')

timesTamp = time.time()
print(timesTamp)