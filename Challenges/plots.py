import matplotlib.pyplot as plt
import matplotlib.image as img


x=[1,2,3,4,5]
y=[100,200,300,400,500]
# Create a  bar graph with lists x and y where color of the bars is light blue. Set Legend.

plt.bar(x,y, color="lightblue", label='The Label for the Legend',)
# Set the title
plt.title("The Title")
# Lable the X axis
plt.xlabel("x axis")
# Label y axis
plt.ylabel("y axis")
# Creates a legend with a shadow and title
plt.legend(facecolor="lightgrey", shadow=True, loc=0, title ="Legend Title")
# Creats figtext
plt.figtext(.5,.7,"stuff", size=20)
plt.show()

