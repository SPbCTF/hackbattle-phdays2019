На видео: [1:04:14](https://vk.com/video-114366489_456239197?t=1h04m14s)

Отмотать состояние LCG

Можно решить SAT солвером, либо написать функцию, откатывающую состояние (см. видео)

```python
#!/usr/bin/env python
# coding: utf-8

# In[2]:


from z3 import *


# In[3]:


# m = BitVec("m", 32)
m = 1073741827
# c = BitVec("c", 32)
c = 195523042
n = 0x7fffffff # 2^31 - 1

s = Solver()


# In[4]:


seed = BitVec("seed", 32)

def next():
    global seed
    seed = (seed * m + c) & n
    return seed


# In[5]:


state1 = BitVec('state1', 32)
state2 = BitVec('state2', 32)
state3 = BitVec('state3', 32)
state4 = BitVec('state4', 32)
state5 = BitVec('state5', 32)

s.add(state1 == next())
s.add(state2 == next())
s.add(state3 == next())
s.add(state4 == next())
s.add(state5 == next())
s.add(state5 == BitVecVal(0xba771e3, 32))


# In[6]:


s.check()


# In[7]:


print(s.model())
"""
[seed = 667878891,
 state5 = 195523043,
 state4 = 1789569707,
 state3 = 173434947,
 state2 = 350551243,
 state1 = 1125417891]
"""
```
