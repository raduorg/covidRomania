from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics import tsaplots

#from statsmodels.tsa.arima.model import ARIMAX

df = pd.read_csv('data_complete.csv')
df.dropna(inplace = True)
#?df['Covid deaths'] = np.log(df['Covid deaths'])
#print(df)
X = df['Stringency index']
y = df['Covid deaths']
# #autocorrelation stringency index
# fig = tsaplots.plot_acf(X)
# plt.pyplot.savefig('autocorrelation_plot_Stringency_index.png')
# #autocorrelation covid deaths
# fig = tsaplots.plot_acf(y)
# plt.pyplot.savefig('autocorrelation_plot_Covid_deaths.png')

model = ARIMA(endog=y, exog=X, order=(5,1,2))
model_fit = model.fit()

# Print the model summary
print(model_fit.summary())