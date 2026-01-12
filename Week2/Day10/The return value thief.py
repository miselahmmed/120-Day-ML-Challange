def timing_decorator(func):
    
        def wrapper():           
            func()
                      
        return wrapper

@timing_decorator
def heavy_computation():
      return 10
      
print(heavy_computation())
