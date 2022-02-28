import pandas as pd

url_pol = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv'
oxcgrt = pd.read_csv(url_pol, dtype={'RegionName': str, 'RegionCode': str})
oxcgrt['Date'] = pd.to_datetime(oxcgrt['Date'], format='%Y%m%d')

oxcgrt.drop(oxcgrt.columns[37:], axis=1, inplace=True) # indexes and extra

# policy implementation is available at state level in some countries
oxcgrt_sub = oxcgrt[oxcgrt['Jurisdiction'] == 'STATE_TOTAL'].copy()
# region information
oxcgrt.drop(oxcgrt.columns[[2, 3]], axis=1, inplace=True)
oxcgrt = oxcgrt[oxcgrt['Jurisdiction'] == 'NAT_TOTAL']

