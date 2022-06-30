# tips
- use functools lru_cache

```python
import time
from functools import lru_cache

@lru_cache(maxsize=1)
def test(_):
    print(time.time())
for i in range(1,10000):
    test(time.time()//10)
    time.sleep(1)
```
-  
```python
with contextlib.suppress(Exception): 
    do_something()

try:
    do_something()
except Exception:
    pass
```