import numpy as np
import matplotlib.pyplot as plt
d1 ={'nov': 25, 'dec': 5, 'jan': 25, 'feb': 5}
courses = list(d1.keys())
values = list(d1.values())
#fig = plt.figure(figsize = (10, 5)) 
# creating the bar plot
plt.bar(courses, values, color ='maroon',width = 0.4)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
