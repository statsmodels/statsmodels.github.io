import statsmodels.api as sm
import pandas as pd
from load_macrodata import dta

cycle, trend = sm.tsa.filters.hpfilter(dta.realgdp, 1600)
dta["cycle"] = cycle
dta["trend"] = trend

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
dta.ix["2000-03-01":, ["realgdp", "trend"]].plot(ax=ax, fontsize=16)
