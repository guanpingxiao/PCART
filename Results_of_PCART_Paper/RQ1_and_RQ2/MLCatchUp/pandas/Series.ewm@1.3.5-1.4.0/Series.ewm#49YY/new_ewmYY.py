import pandas as pd
import numpy as np
df = pd.Series({'B': 0})
df.ewm(0.5,  None,  None,  None,  0, adjust=True, ignore_na=False, axis=0, times=None).mean()