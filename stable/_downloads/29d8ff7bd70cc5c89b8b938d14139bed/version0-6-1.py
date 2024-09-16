import statsmodels.api as sm

dta = sm.datasets.co2.load_pandas().data
# deal with missing values. see issue
co2 = dta.co2.interpolate()
res = sm.tsa.seasonal_decompose(co2)
res.plot()