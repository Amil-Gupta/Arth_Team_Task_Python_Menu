import os
from termcolor import colored

choice=1
name=""
img_name=""
ip_master=""
ip_client=""
ip_slave=""
my_input=""
keyname = ""
sgid = ""
os.system("clear")
while(choice!=0):
    print(colored("""Enter:
\t1 for AWS Operations
\t2 for Hadoop Operations
\t3 for Networking Operations
\t4 for Docker Operations
\t5 for other Linux Operations
\t0 to EXIT to console""",'blue'))
    choice=int(input())
    os.system("clear")
    if choice==1:                #AWS
        print(colored("""
Enter:
\t1 To check the version of aws installed
\t2 To refer to the aws documentation for help
\t3 To login to a user
\t4 To show all the available instances
\t5 To describe all the tags of ec2 instances
\t6 To describe the all the subnets
\t7 To describe the all the vpc
\t8 To describe all the volumes
\t9 To describe key-pairs
\t10 To describe security groups
\t11 To describe all the available regions
\t12 To create a key-pair
\t13 To create a security group
\t14 To create an instance
\t15 To create EBS storage
\t16 To attach EBS storage to an instance
\t17 To create cloudfront distriution
\t18 To create S3 bucket and add files
\t19 To stop an instance
\t20 To terminate an instance
\t21 To detach volume and delete it
\t22 To delete key pair
\t0 To EXIT to the main menu """,'yellow'))
        my_input = input()

        os.system("clear")

        if int(my_input) == 1:
            print("CHECK THE VERSION OF AWS INSTALLED")
            os.system("aws --version")

        elif int(my_input) == 2:
            os.system("aws help")

        elif int(my_input) == 3:
            os.system("aws configure")

        elif int(my_input) == 4:
            os.system("aws ec2 describe-instances")

        elif int(my_input) == 5:
            os.system("aws ec2 describe-tags")

        elif int(my_input) == 6:
            os.system("aws ec2 describe-subnets")

        elif int(my_input) == 7:
            os.system("aws ec2 describe-vpcs")

#        elif int(my_input) == 7:
 #           os.system("aws ec2 describe-hosts")

        elif int(my_input) == 8:
            os.system("aws ec2 describe-volumes")

        elif int(my_input) == 9:
            os.system("aws ec2 describe-key-pairs")

        elif int(my_input) == 10:
            os.system("aws ec2 describe-security-groups")

        elif int(my_input) == 11:
            os.system("aws ec2 describe-regions")
        
        elif int(my_input) == 12:
            keyname =input("The name of the key:")
            os.system("aws ec2 create-key-pair --key-name {0} --query \"KeyMaterial\" > {0}.pem".format(keyname))
            print("Wait for a moment!")
            os.system("aws ec2 describe-key-pairs --key-name {}".format(keyname))
        elif int(my_input) == 13:
            print("Creating security Group")
            groupname = input("Enter the groupname")
            os.system("clear")
            desc = input("Description")
            vpcid = input("Enter the vpc id")
            os.system("aws ec2 create-security-group --group-name {} --description \"{}\" --vpc-id {}".format(groupname,desc,vpcid))
            #allow the routes
            sgid = input("Enter security group id") 
            os.system("aws ec2  describe-security-groups --group-id".format(sgid))
        elif int(my_input) == 14:
            os.system("aws  ec2 describe-images --query \"Images[*].{Architecture:Architecture,ImageId:ImageId,PlatformDetails:PlatformDetails,VirtualizationType:VirtualizationType}\" --output json")
            imageid = input("Enter the image id")
            count = input("No of instances required")
            os.system("aws ec2 describe-instance-types  --query \"InstanceTypes[*].{InstanceType:InstanceType}\" --output json")
            instType = input("The instance type like t2.nano,t2.micro,t2.small,etc")
            os.system("aws ec2 describe-key-pairs --query \"KeyPairs[*].{KeyName:KeyName}\" --output json")
            keyname = input("Enter key name which already exists")
            os.system("aws ec2 describe-security-groups --query \"SecurityGroups[*].{GroupId:GroupId}\" --output json")
            sgid = input("Enter valid Security group id")
            key = input("For tag, enter the key")
            value = input("For tag, enter the value")
            os.system("aws ec2 run-instances --image-id  {} --count {} --instance-type {} --key-name {} --security-group-ids {} --tag-specifications  ResourceType=instance,Tags=[{Key={},Value={}}]".format(imageid,count,instType,keyname,sgid,key,value))
        elif int(my_input) == 15:
            print("The Amazon EBS volume type. This can be gp2 for General Purpose SSD, io1 or io2 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic volumes.")
            volType = input("Enter the volume type")
            size = input("Enter the size")
            os.system("aws ec2 describe-availability-zones  --query \"AvailabilityZones[*].{RegionName:RegionName}\" --output json")
            AZ = input("Enter the Availability Zone")
            key = input("For tag, enter the key")
            value = input("For tag, enter the value")
            os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {} --tag-specifications  ResourceType=volume,Tags=[{Key={},Value={}}]".format(volType,size,AZ,key,value))
        elif int(my_input) == 16:
            os.system("aws ec2 describe-volumes  --query \"Volumes[*].Attachments[*].{InstanceId:InstanceId,VolumeId:VolumeId}\" --output json")
            volId = input("Enter the Volume ID from the above list")
            instId = input("Enter the Instance ID from the above list")
            os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volId,instId))
        elif int(my_input) == 18:
            bucketName = input("Enter the name of the S3 bucket.Note it should be unique")
            acl = input("Possible values:private, public-read, public-read-write, authenticated-read. Enter som")
            os.system("aws ec2 describe-regions --query \"Regions[*].{RegionName:RegionName}\" --output json")
            region = input("Enter a valid region name")
            os.system("aws s3api create-bucket --bucket {}  --acl {}  --region {}".format(bucketName,acl,region))
            key = input("Enter the path you  want to save in the S3 bucket")
            body = input("Enter the path of the object you want to put in the location")
            os.system("aws s3api put-object --acl {} --bucket {} --key {} --body {}".format(acl,bucketName,key,body))
        elif int(my_input) == 17:
            os.system("aws s3 ls")
            bucketNamePresent = input("Enter the name of the S3 bucket")
            rootObject = input("Enter the path of the object")
            os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucketNamePresent,rootObject))

        elif int(my_input) == 19:
            os.system("aws ec2 describe-volumes  --query \"Volumes[*].Attachments[*].{InstanceId:InstanceId}\" --output json")
            instId = input("Enter the Instance ID from the above list")
            os.system("aws ec2 stop-instances --instance-ids {}".format(instId))

        elif int(my_input) == 20:
            os.system("aws ec2 describe-volumes  --query \"Volumes[*].Attachments[*].{InstanceId:InstanceId}\" --output json")
            instId = input("Enter the Instance ID from the above list")
            os.system("aws ec2 terminate-instances --instance-ids {}".format(instId))

        elif int(my_input) == 21:
            os.system("aws ec2 describe-volumes  --query \"Volumes[*].Attachments[*].{VolumeId:VolumeId}\" --output json")
            volId = input("Enter the Volume ID from the above list")
            os.system("aws ec2 detach-volume  --volume-id {}".format(volId))
            os.system("aws ec2 delete-volume  --volume-id {}".format(volId))

        #elif int(my_input) == 22:
         #   os.system("")
        elif int(my_input) == 22:
            os.system("aws ec2 describe-key-pairs --query \"KeyPairs[*].{KeyName:KeyName}\" --output json")
            keyname = input("Enter key name which already exists")
            os.system("aws ec2 delete-key-pair --key-name {}".format())

    elif choice==2:
        while True:
            print(colored("""
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
\t0 to EXIT to main menu """,'yellow'))
        
            my_input = input()
            
            os.system("clear")

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
                choice=2
                break
            else: 
                print("Option not supported")


    elif choice==3:            #Networking
        print("Delete this and write your code")
    elif choice==4:            #Docker
        while True:             #As exit condition has been provided within the loop itself
            print(colored("""
Enter:
\t1 to run a container
\t2 to start a container
\t3 to stop a container
\t4 to remove a container
\t5 to view logs for a container
\t6 to list all containers
\t7 to list all images
\t0 to EXIT to main menu""",'yellow'));
            choice=int(input())
            os.system("clear")
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
            else:
                print("Option Not Supported")
    elif choice==5:            #Linux
        while True:
            print(colored("""
Enter:
\t1 to start a service
\t2 to stop a service
\t3 to enable(permanently start) a service
\t4 to disable(permanently stop) a service
\t5 to install a software using yum (yum repository for the software must be configured)
\t6 to uninstall a software using yum
\t7 to view date and time
\t8 to view calendar
\t9 to view the details of a directory
\t10 to view present working directory
\t11 to open a file using gedit(GUI)
\t12 to open a using vim(CLI)
\t-1 to run your own CLI command
\t0 to EXIT""",'yellow'))
            choice=int(input())
            os.system("clear")
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
            elif choice==-1:
                print("Enter your CLI command below")
                name=input()
                os.system(name)
            elif choice==0:
                choice=5
                break
            else:
                print("Option Not Supported")
    elif choice!=0:
        print("Invalid Choice, please try again\n")
