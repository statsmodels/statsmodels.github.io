import statsmodels.api as sm

dta = sm.datasets.co2.load_pandas().data
# deal with missing values. see issue
dta = dta.co2.interpolate()

res = sm.tsa.seasonal_decompose(dta.co2)
res.plot()