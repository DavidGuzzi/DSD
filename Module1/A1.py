pip install pyarrow

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.2f}'.format

df = pd.read_parquet('data-ecomm-10-19-smallsampled.parquet')
#Visualization of the dataset.
df.head()
