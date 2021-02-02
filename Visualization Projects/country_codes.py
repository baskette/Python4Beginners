#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the country wasn't found, return None.
    return None
