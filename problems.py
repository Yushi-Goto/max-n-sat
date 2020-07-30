import random

class MaxNSat(object):
  def __init__(self, N, xc_num, ltrl_ind):
    self.N = N
    self.x_num = xc_num[0]
    self.c_num = xc_num[1]
    self.x_init = self.cleate_x()
    self.ltrl_ind = ltrl_ind

  def cleate_x(self):
    """Cleate Random variable x"""
    return [random.choice([True, False]) for i in range(self.x_num)]

  def sum_satisfied_clause(self, x):
    """Calculate number of True clauses"""
    cla_list = []
    for i in range(self.c_num):

      ltrl_list = []
      for l in self.ltrl_ind[i]:
        if l < 0:
          ltrl_tmp = not x[abs(l) - 1]
        else:
          ltral_tmp = x[l - 1]
        ltrl_list.append(ltrl_tmp)

      operation = self.operate_or(ltrl_list) 
      cla_list.append(operation)

    return sum(c==True for c in cla_list)

  def solve_max_sat(self):
    """Solve Max N Sat (Find optimal solution)"""
    x = self.x_init
    while True:
      sati_cla_num = self.sum_satisfied_clause(x)
      if sati_cla_num == self.c_num:
        break
      x = self.cleate_x()
    return x

  def operate_or(self, ltrl_list):
    """Calculate OR"""
    return any(ltrl_list)
