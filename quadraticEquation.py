import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from cmath import sqrt
print ("\n=>this program is designed to receive a ,b ,c values from the user and calculate the roots of a quadratic equation \n\t")

a = float(input("enter the value of a: "))      # receive the values 
b = float(input("\nenter the value of b: "))    # 〃
c = float(input("\nenter the value of c: "))    # 〃
if a == 0 : # make sure that we even have a quadratic equation.
  print ("the coefficient of x^2 cannot be set to zero.")
delta = pow(b,2) - (4*a*c)  # formula of delta.
print ("\n\t=> delta is : (" ,delta, ")" )
if  delta > 0 : 
  print (" \n\t\t=> the equation has two real roots :\n")
  x_1 = ((-b) + sqrt(delta)) / 2*a
  x_2 = ((-b) - sqrt(delta)) / 2*a
  print ("x1 is: ",x_1,"and x2 is: ",x_2)
elif delta == 0 :
  print (" \n=> there is one real root for the entered values of a ,b ,c. this implies that the curve conjoints with the X axis in one point")
  doubleRoot = -b / 2*a
  print (doubleRoot)
else :
  print(" \n\t=> when the value of delta is negative the equation has no real roots")
img = mpimg.imread('2844f484-224b-4f72-a9ee-b419663501fa.')  # an image of different types of quadratic equations.
shouldShowImage = str(input("\t\nwould you like to see what each of the three types of qudratic equation look like? (yes/no): "))
if shouldShowImage == "yes":
  plt.imshow(img)
  plt.axis('off')
  plt.show()
elif shouldShowImage == "no":
  print("\n=> okay then, hope this program has been a bit of help to you")