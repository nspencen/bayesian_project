# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:38:20 2021

@author: naomi
"""

import pandas as pd
import numpy as np
from datetime import date, timedelta
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

    
def get_posterior_p(prior, likelihood):
    #calculate total probability
    if type(prior) == list:
        prior = np.array(prior)
    if type(likelihood) == list:    
        likelihood = np.array(likelihood)
    total_prob = np.sum(prior * likelihood)
    #calculate posterior probabilities    
    posterior = prior * likelihood/total_prob
    return posterior

'''
101 cookie jars 
bowl0 0% vanilla 100% chocolate
bowl1 1% vanilla 99% chocolate
...
bowl101 100% vanilla 0% chocolate

first cookie vanilla
posterior = get_posterior_p([1/101]*101, np.arange(0,1.01,0.01))

second cookie vanilla
posterior2 = get_posterior_p(posterior, np.arange(0,1.01,0.01))

third cookie chocolate
posterior3 = get_posterior_p(posterior2, np.arange(1.01,0,-0.01))

maximum a posteori probability
posterior3.argmax()
#67



likelihood_heads = np.linspace(0, 1, 101)
likelihood_tails = 1 - likelihood_heads
likelihood = {
    'H':likelihood_heads,
    'T':likelihood_tails
    }
dataset = 'H' * 140 + 'T' * 110
posterior = 0.5
posterior_list = []
for d in dataset:
    posterior = get_posterior_p(posterior, likelihood[d])
    posterior_list.append(posterior)



'''




