print(" ")
print("reyes yañez oscar alonso_3w_1208_este es un programa en el que se practican las funciones")
print(" ")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nresultados de examenes de recursamiento")
tri_recursion(8)