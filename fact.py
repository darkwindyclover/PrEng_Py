class Factorial:
   def __init__(self):
      pass
   def calculate(self, x):
      if x < 0: 
         raise ValueError("x cannot be negative")
      elif x == 0:
         return 1
      else:
         res = 1
         for i in range(1,x + 1):
            res = res*i
         return res
