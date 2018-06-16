### Introduction ###
Simple python socket programming to retrieve the ssh login attempts(Succesfully connected, Disconnected and Invalid attempts) and show them
to the server side.
Requirements:
2 clients and 1 server.

### How it works: ###
Here, I am using client-server architecture by Python socket programming.
what you need to do id, Create 3 ubuntu servers(2 clients and 1 server), Copy the Server.py file to the server and copy the client folder
to the Clients in /home/ubuntu dir.
Now you need to change the server Ip in client/Client.py (ip = str("IP")) on both clients, and now you need to setup cron jobs for 
Client.py.
command: crontab -e
"***** python /home/ubuntu/client/Client.py &"
save and close

Now, You need to go to the server side and run the server file by using this command "python Server.py" it will ask you for client IP
enter the client IP of which you wanna get details of ssh.
Now, You will see the screen where you need to select option, option includes:
1. Successful (To check successfull ssh logins)
2. Disconnect (To check Disconnected ssh users)
3. Invalid    (To chcek Invalid logins)


### Automation ###
I am using Asible for the Automation at the server side
1. Install the Ansible (apt-get install ansible -y)
2. create ansible user (useradd ansible) (passwd ansible)
3. Generate the ssh key (ssh-keygen)
4. Copy the ssh key to clients (ssh-copy-id ansible@<IP>) enter the password and copy will be done
5. Now, entry for ansible user in sudoers file (vim /etc/sudoers)
6. Add this line "ansible ALL:ALL  NOPASSWD:ALL"  
7. Add your clients to ansible (vim /etc/ansible/hosts)
Add following lines to the hosts file
[client1]
<IP>

[client2]
<IP>

6. Install git and "git clone https://github.com/starsunny/TekionTask/ansible/"
7. Go into the cloned directory (cd ansible)
8. change the server IP in client/Clients.py (ip = str("IP"))
8. Run the command (ansible-playbook setup.yml)

### What it will do ##
It will copy the client directory to the both cients in /home/ubuntu directory
and setup the cron job


