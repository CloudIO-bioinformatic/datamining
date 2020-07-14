#Write by: Claudio Quevedo G.
#Date: 13-07-2020
#Reason: Data Mining
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
datasets = pd.read_csv('datasets',sep=';')
records = []
for i in range(0, 50):
    records.append([datasets.values[i,j] for j in range(1, 6)])
records_rounded = []
for r in records:
    records_rounded.append(["population_"+str(round(round_up(round(r[0]),-len(str(round(r[0])))+1))),"infected_"+str(round(round_up(round(r[1]),-len(str(round(r[1])))+1))),"death_"+str(round(round_up(round(r[2]),-len(str(round(r[2])))+1))),"recovered_"+str(round(round_up(round(r[3]),-len(str(round(r[3])))+1))),"migration_"+str(round(r[4],3))])
########################################################################################################
association_rules = apriori(records_rounded, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print("Item1\tItem2\tSupport\tConfidence\tLift")
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print(items[0]+"\t"+items[1]+"\t"+str(item[1])+"\t"+str(item[2][0][2])+"\t"+str(item[2][0][3]))
########################################################################################################
