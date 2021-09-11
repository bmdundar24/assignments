result = list(filter(lambda x : all(x % y != 0 for y in range(2,x)),range(2,101)))
print(result)



"""
import matplotlib.pyplot as p
s = [40,30,10,10,10]
i = ["Python","Java","C++", "C", "Javascript"]  # pasta dilimi gösterme
p.pie(s,labels=i)
p.show()
"""