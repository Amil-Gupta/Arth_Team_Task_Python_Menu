import os

choice=1
while(choice!=0):
  print("Enter:\n\t1 for AWS Operations\n\t2 for Hadoop Operations\n\t3 for Networking Operations\n\t4 for Docker Operations\n\t5 for other Linux Operations\n\t 0 to EXIT\n")
  choice=input()
  if choice==1:              //AWS
  elif choice==2:            //Hadoop
  elif choice==3:            //Networking
  elif choice==4:            //Docker
  elif choice==5:            //Linux
  elif choice!=0:
    print("Invalid Choice, please try again\n")
