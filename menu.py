import os

choice=1
cont_name=""
img_name=""
while(choice!=0):
    print("Enter:\n\t1 for AWS Operations\n\t2 for Hadoop Operations\n\t3 for Networking Operations\n\t4 for Docker Operations\n\t5 for other Linux Operations\n\t 0 to EXIT")
    choice=int(input())
    if choice==1:                #AWS
        printf("Delete this and write your code")
    elif choice==2:            #Hadoop
        printf("Delete this and write your code")
    elif choice==3:            #Networking
        printf("Delete this and write your code")
    elif choice==4:            #Docker
        while True:             #As exit condition has been provided within the loop itself
            print("Enter:\n\t1 to run a container\n\t2 to start a container\n\t3 to stop a container\n\t4 to remove a container\n\t5 to view logs for a container\n\t6 to list all containers\n\t7 to list all images\n\t0 to EXIT to main menu");
            choice=int(input())
            if choice==1:
                print("Enter container name")
                cont_name=input()
                print("Enter image name")
                img_name=input()
                os.system("docker run -it --name {0} {1}".format(cont_name,img_name))
                print("Created container {}(Please note the container ID displayed for future reference)".format(cont_name))
            elif choice==2:
                print("Enter container name/id")
                cont_name=input()
                print("Starting container...")  #Giving this kind of output as there is chance of an error message from the system due to container not existing,etc
                os.system("docker start {}".format(cont_name))
            elif choice==3:
                print("Enter container name/id")
                cont_name=input()
                print("Stopping container")
                os.system("docker stop {}".format(cont_name))
            elif choice==4:
                print("Ënter container name/id")
                cont_name=input()
                print("Removing container...")
                os.system("docker stop {}".format(cont_name))
                os.system("docker rm -f {}".format(cont_name))
            elif choice==5:
                print("Enter container name")
                cont_name=input()
                print("Logs for {} are:".format(cont_name))
                os.system("docker logs {}".format(cont_name))
            elif choice==6:
                print("Available containers are:")
                os.system("docker ps")
            elif choice==7:
                print("Available images are:")
                os.system("docket images")
            elif choice==0:
                choice=4             #Reset the "choice" to the value it had while entering the block
                break
    elif choice==5:            #Linux
        printf("Delete this and write your code")
    elif choice!=0:
        print("Invalid Choice, please try again\n")
