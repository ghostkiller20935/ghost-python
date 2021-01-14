def addition(func):
      def wrapper_function(a,b):
            print("sabiranje result is {}".format(a+b))
            return func(a,b)
      return wrapper_function
 
def subtraction(func):
      def wrapper_function(a,b):
             print("oduzimanje result is {}".format(a-b))
             return func(a,b)
      return wrapper_function
 
@addition
@subtraction
def operations(a,b):
      print("brojevi su : {} i {}".format(a,b))
 
operations(9, 15)