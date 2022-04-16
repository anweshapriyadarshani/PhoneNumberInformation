#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install phonenumbers')


# In[8]:


import phonenumbers
from phonenumbers import geocoder
phone_number=phonenumbers.parse("+917735708867")
print(geocoder.description_for_number(phone_number,'en'))

