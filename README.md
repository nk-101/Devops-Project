# Task-Manager
# DevOps Project
# Implementation of CI/CD Pipeline on AWS Console Using ec2 Instance using tools jenkins,docker
# Commands for installation of java,jenkins and docker on aws console 
    1  sudo apt update
    2  sudo apt install openjdk-11-jre
    3  sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    4  echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee       
       /etc/apt/sources.list.d/jenkins.list > /dev/null
    5 sudo apt-get update
    6  sudo apt-get install jenkins
    7  sudo systemctl enable jenkins
    8  sudo systemctl start jenkins
    9  sudo systemctl status jenkins
   10  sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   11  ssh-keygen
   12  ls
   13  cat id_rsa
   14  cd .ssh
   15  ls
   16  cat id_rsa
   17  cat id_rsa.pub
   18  cd
   19  cd /var/lib/jenkins/workspace/my devops project
   20  ls
   21  cd
   22  cd /var/lib/jenkins/workspace/taskpython
   23  ls
   24  sudo apt install python3
   25  python3 task.py
   26  sudo rm Dockerfile
   27  sudo apt install docker.io
   29  sudo vim Dockerfile
   30  ls
   31  docker build . -t tasktm
   32  sudo usermod -a -G docker $USER
   33  sudo reboot
   34  clear
   35  cd /var/lib/jenkins/workspace/taskpython
   36  history
   37  docker build . -t tm
   38  docker run -d --name task -p 8000:8000 tm
   39  docker ps
   40  clear
   41  history
   42  docker run -d --name task -p 8000:8000 tm
   43  docker kill 5d40d79d159080
   44  docker rm task
   45  docker run -d --name task -p 8000:8000 tm
   46  docker ps
   47  docker rm -f e221c03da76c7
   48  history
   49  chmod 777 /var/lib/jenkins/workspace/taskpython
   50  sudo chmod 777 /var/lib/jenkins/workspace/taskpython
   51  sudo usermod -a -G docker jenkins
   52  sudo systemctl restart jenkins
   53  docker ps
   54  docker rm -f e221c03da76c7
   55  docker ps -a
   56  docker kill task
   57  docker rm -f e49946b3e721  
   58  history
  # After code runs successfully on Ec2 Instance and docker image is built, a git webhook is created so whevever changes is commited it is triggered. 
