def dataloader(path):
    f = open(path, encoding="utf8")
    count = 0
    ltrl_ind = [] # Literal index of each clause
    while True: # Read a line from txt
      line = f.readline()
      if line:
        line = line.split() # Splitting and listing strings
        line = list(map(int, line)) # Convert list str element to int
        if count == 0:
          xc_num = line # Number of variables x and clauses
        else:
          ltrl_ind.append(line) # ADD literal index of each clause
        count += 1
      else:
        break
    f.close()

    N = len(ltrl_ind[0]) # Number of literals in each clause (MAX-3SAT)

    # (N : Number of literal), (xc_num : Number of variables x and clauses), (Literal index of each clause)
    return N, xc_num, ltrl_ind
