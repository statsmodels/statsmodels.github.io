import numpy as np
from statsmodels.graphics.factorplots import interaction_plot
np.random.seed(12345)
weight = np.random.randint(1,4,size=60)
duration = np.random.randint(1,3,size=60)
days = np.log(np.random.randint(1,30, size=60))
fig = interaction_plot(weight, duration, days,
            colors=['red','blue'], markers=['D','^'], ms=10)
import matplotlib.pyplot as plt
#plt.show()