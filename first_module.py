#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + ' ' + last
    return full_name.title()