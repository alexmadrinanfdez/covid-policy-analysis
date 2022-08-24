import pandas as pd

url_pol = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker-legacy/main/legacy_data_202207/OxCGRT_latest.csv'
oxcgrt = pd.read_csv(url_pol, dtype={'RegionName': str, 'RegionCode': str})
oxcgrt['Date'] = pd.to_datetime(oxcgrt['Date'], format='%Y%m%d')

oxcgrt.drop(oxcgrt.columns[37:], axis=1, inplace=True) # indexes and extra

# policy implementation is available at state level in some countries
oxcgrt_sub = oxcgrt[oxcgrt['Jurisdiction'] == 'STATE_TOTAL'].copy()
# region information
oxcgrt.drop(oxcgrt.columns[[2, 3]], axis=1, inplace=True)
oxcgrt = oxcgrt[oxcgrt['Jurisdiction'] == 'NAT_TOTAL']

# Pivot the data to obtain 
# a different dataset for each policy type indexed by time (date).
idch = list(oxcgrt.columns[4:19:2])
idch.append(oxcgrt.columns[24])
idch.append(oxcgrt.columns[30])

C1 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[0])
C2 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[1])
C3 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[2])
C4 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[3])
C5 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[4])
C6 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[5])
C7 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[6])
C8 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[7])
H1 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[8])
H6 = oxcgrt.pivot(index='Date', columns='CountryCode', values=idch[9])

CH_X = [C1, C2, C3, C4, C5, C6, C7, C8, H1, H6]