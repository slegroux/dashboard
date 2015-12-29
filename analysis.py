#!/usr/bin/env python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from IPython import embed
df = pd.read_csv("deezer.csv", thousands=',')
grouped = df.groupby(['Cohort', 'Planet'])
summed = grouped.aggregate(np.sum).reset_index()
summed.Cohort = pd.to_datetime(summed.Cohort, format="%B-%y")
embed()