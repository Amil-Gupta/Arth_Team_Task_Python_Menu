import os

choice=1
name=""
img_name=""
while(choice!=0):
    print("""Enter:
\t1 for AWS Operations
\t2 for Hadoop Operations
\t3 for Networking Operations
\t4 for Docker Operations
\t5 for other Linux Operations
\t0 to EXIT""")
    choice=int(input())
    if choice==1:                #AWS
        print("Delete this and write your code")

    elif choice==2:
        while True:
            print("""
Enter:
\t1 To Configure the Master Node
 \t2 To Configure the Data Node
\t3 To Configure the Client
\t4 To See the Cluster Report
\t5 To Run the TCPDUMP
\t6 To Create a Directory in the Cluster
\t7 To Create a Upload a File in the Cluster
\t8 To Read a File in the Distributed File Storage
\t9 To see the file structure
\t0 to EXIT
            """)
        
            my_input = input("Enter your choice: ")
            print(my_input)

            if int(my_input) == 1:
                ip_master = input("Enter Master Node IP: ")
                print(ip_master)
                os.system("scp hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm hdfs-site.xml core-site.xml {}:\nchmod +x hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm".format(ip_master))
                os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip_master))
                os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip_master))
    
                my_name_dir = input("Enter directory name for Master Node: ")
                print(my_name_dir)
                os.system("mkdir /{}".format(my_name_dir))
                os.system("hadoop namenode -format") 
                os.system("hadoop-daemon.sh start namenode")

    #mytree = ET.parse('hdfs-site.xml')
    #myroot = mytree.getroot()
    #myroot[0]

    #src_file1 = "hdfs-site.xml"
    #dest_path1 = "/etc/hadoop/hdfs-site.xml"
    #shutil.copy(src_file1, dest_path1)
    
    #with open("hdfs-site.xml") as f:
        #with open("hdfs.xml", "w") as f1:
            #for line in f:
                    #f1.write(line)
            
    
    
    #src_file2 = "core-site.xml"
    #dest_path2 = "/etc/hadoop/hdfs-site.xml"
    #shutil.copy(src_file2, dest_path2)

            elif int(my_input) == 2:
                ip_slave = input("Enter Slave Node IP: ")
                print(ip_slave)
                os.system("scp hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm  {}:\nchmod +x hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm".format(ip_slave))
                os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip_slave))
                os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip_slave))

                my_data_dir = input("Enter directory name for Data Node: ")
                print(my_name_dir)
                os.system("mkdir /{}".format(my_data_dir)) 
                os.system("hadoop-daemon.sh start datanode") 

            elif int(my_input) == 3:
                ip_client = input("Enter Client IP: ")
                print(ip_client)
                os.system("scp hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm  {}:\nchmod +x hadoop-1.2.1-1.x86_64.rpm jdk-8u171-linux-x64.rpm".format(ip_client))
                os.system("ssh {} rpm -ivh jdk-8u171-linux-x64.rpm".format(ip_client))
                os.system("ssh {} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(ip_client))

            elif int(my_input) == 4:
                os.system("hadoop dfsadmin -report | less")

            elif int(my_input) == 5:
                os.system("ssh {} tcpdump -i enp0s3 tcp port 9001 -n not ssh 22".format(ip_client))
                os.system("ssh {} tcpdump -i enp0s3 tcp port 9001 -n not ssh 22".format(ip_master))
                os.system("ssh {} tcpdump -i enp0s3 tcp port 9001 -n not ssh 22".format(ip_slave))

            elif int(my_input) == 6:
                os.system("ssh {} hadoop fs -mkdir /mydir".format(ip_client))

            elif int(my_input) == 7:
                os.system("ssh {} hadoop fs -put myfile.txt".format(ip_client))

            elif int(my_input) == 8:
                os.system("ssh {} hadoop fs -cat /myfile.txt".format(ip_client))

            elif int(my_input) == 9:
                os.system("ssh {} hadoop fs -ls /".format(ip_client))
            elif int(my_input) == 0:
                break
            else: 
                print("Option not supported")


    elif choice==3:            #Networking
        print("Delete this and write your code")
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
        while True:
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
