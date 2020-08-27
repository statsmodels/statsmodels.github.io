import statsmodels.api as sm

dta = sm.datasets.co2.load_pandas().data
dta.co2.interpolate(inplace=True)
dta = dta.resample('M')

res = sm.tsa.x13_arima_select_order(dta.co2)
print(res.order, res.sorder)

results = sm.tsa.x13_arima_analysis(dta.co2)

fig = results.plot()
fig.set_size_inches(12, 5)
fig.tight_layout()