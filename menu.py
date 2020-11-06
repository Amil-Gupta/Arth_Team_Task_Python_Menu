import os

choice=1
name=""
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
                name=input()
                print("Enter image name")
                img_name=input()
                os.system("docker run -it --name {0} {1}".format(name,img_name))
                print("Created container {}(Please note the container ID displayed for future reference)".format(name))
            elif choice==2:
                print("Enter container name/id")
                name=input()
                print("Starting container...")  #Giving this kind of output as there is chance of an error message from the system due to container not existing,etc
                os.system("docker start {}".format(name))
            elif choice==3:
                print("Enter container name/id")
                name=input()
                print("Stopping container")
                os.system("docker stop {}".format(name))
            elif choice==4:
                print("Ënter container name/id")
                name=input()
                print("Removing container...")
                os.system("docker stop {}".format(name))
                os.system("docker rm -f {}".format(name))
            elif choice==5:
                print("Enter container name")
                name=input()
                print("Logs for {} are:".format(name))
                os.system("docker logs {}".format(name))
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
        print("Enter:\n\t1 to start a service\n\t2 to stop a service\n\t3 to enable(permanently start) a service\n\t4 to disable(permanently stop) a service\n\t5 to install a software using yum (yum repository for the software must be configured)\n\t6 to uninstall a software using yum\n\t7 to view date and time\n\t8 to view calendar\n\t9 to view the details of a directory\n\t10 to view present working directory\n\t11 to open a file using gedit(GUI)\n\t12 to open a using vim(CLI)\n\t0 to EXIT")
        choice=int(input())
        if choice==1:
            print("Enter service name")
            name=input()
            os.system("systemctl start {}".format(name))
        elif choice==2:
            print("Enter service name")
            name=input()
            os.system("systemctl stop {}".format(name))
        elif choice==3:
            print("Enter service name")
            name=input()
            os.system("systemctl enable {}".format(name))
        elif choice==4:
            print("Enter service name")
            name=input()
            os.system("systemctl disable {}".format(name))
        elif choice==5:
            print("Enter software name")
            name=input()
            os.system("yum install {}".format(name))
        elif choice==6:
            print("Enter software name")
            name=input()
            os.system("yum uninstall {}".format(name))
        elif choice==7:
            os.system("date")
        elif choice==8:
            os.system("cal")
        elif choice==9:
            print("Enter directory name/address")
            name=input()
            os.system("ls {}".format(name))
        elif choice==10:
            print("Present working directory is:")
            os.system("pwd")
        elif choice==11:
            print("Enter file name/address")
            name=input()
            os.system("gedit {}".format(name))
        elif choice==12:
            print("Enter file name/address")
            name=input()
            os,system("vim {}".format(name))
        elif choice==0:
            choice=5
            break
    elif choice!=0:
        print("Invalid Choice, please try again\n")
