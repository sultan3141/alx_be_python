def safe_divide(numerator, denominator):
  try:
    print(numerator/denominator)
  except ZeroDivisionError:
    print("it have division by zero error")
    
         
