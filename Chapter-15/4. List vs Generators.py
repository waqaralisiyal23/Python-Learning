# List vs Generator
# Memory Usage, Time
# When to use list, when to use generator

import time

t1 = time.time()
# l = [ i**2 for i in range(10000000) ]
g = ( i**2 for i in range(10000000) )
print(time.time() - t1)

# Pehle ek ko comment kro or check kro task manager mn memory or console mn time phr dsre ko comment kro or check kro memory
# or time

# Use list when you want to use sequence again and again and use generator when you want to use sequence only once