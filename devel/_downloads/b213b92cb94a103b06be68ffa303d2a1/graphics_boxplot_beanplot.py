"""

Created on Fri May 04 00:22:40 2012

Author: Ralf Gommers

"""

import matplotlib.pyplot as plt
import numpy as np

import statsmodels.api as sm

data = sm.datasets.anes96.load_pandas()
party_ID = np.arange(7)
labels = ["Strong Democrat", "Weak Democrat", "Independent-Democrat",
          "Independent-Indpendent", "Independent-Republican",
          "Weak Republican", "Strong Republican"]

plt.rcParams['figure.subplot.bottom'] = 0.23  # keep labels visible
age = [data.exog['age'][data.endog == id] for id in party_ID]
fig = plt.figure()
ax = fig.add_subplot(111)
sm.graphics.beanplot(age, ax=ax, labels=labels,
                     plot_opts={'cutoff_val':5, 'cutoff_type':'abs',
                                'label_fontsize':'small',
                                'label_rotation':30})
ax.set_xlabel("Party identification of respondent.")
ax.set_ylabel("Age")

#plt.show()
