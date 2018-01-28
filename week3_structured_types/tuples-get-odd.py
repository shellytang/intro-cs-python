def oddTuples(aTup):
  '''
  aTup: a tuple
  returns: tuple, every other element of aTup. 
  '''
  # return aTup[0:len(aTup):2]
  return aTup[::2]

oddTuples(('I', 'am', 'a', 'test', 'tuple')) # ('I','a', 'tuple')
