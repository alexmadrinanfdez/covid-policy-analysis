import pandas as pd
import numpy as np

from .data.cases import cum_cases
from .data.nations import cc_dict
from .data.policies import CH_X, idch

chx_str = [s.split('_')[0] for s in idch]

def _get_init_date(iso):
  name = cc_dict[iso]
  t_idx = cum_cases.loc[cum_cases[name] > 25, name].index
  return t_idx.min()

def _print_model(name, value, score):
  print('Coefficients\n------------')
  for n, v in zip(name, value):
    if v != 0:
      print('{:s} : {:3f}'.format(n, v))
  print('\nR^2\n---')
  print(round(score, 3))

def std_err(y):
  'CLT-based 95% confidence intervals for input population(s).'

  # assumes rows are the populations
  n = y.shape[0]
  s = y.std(axis=0)
  return 1.96 * s / np.sqrt(n)