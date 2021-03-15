def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(n):
      print(trow)
      trow=[f+r for f,r in zip(trow+y, y+trow)]
   
pascal_triangle(6)
