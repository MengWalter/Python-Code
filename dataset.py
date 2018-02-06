# imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#get_ipython().run_line_magic('matplotlib','inline')
#%matplotlib inline
data=pd.read_csv('brain_size.csv',sep=';',na_values=".")
data.head() #show the data
