### Introduction ###
Simple python socket programming to retrieve the ssh login attempts(Succesfully connected, Disconnected and Invalid attempts) and show them
to the server side.
Requirements:
2 clients and 1 server.

### How it works: ###
Here, I am using client-server architecture by Python socket programming.
what you need to do is, Create 3 ubuntu servers(2 clients and 1 server), Copy the Server.py file to the server and copy the client folder
to the Clients in /home/ubuntu dir.
or git clone "git clone https://github.com/starsunny/TekionTask
do git clone on the Both clients and server
here you will find 1 client folder which will be used for clients and
one Server.py which will be used for server.
Now at the client side you need to change the server Ip in client/Client.py (ip = str("IP")) on both clients, and now you need to setup cron jobs for 
Client.py.
command: crontab -e
"***** python /home/ubuntu/client/Client.py &"
save and close

Now, You need to go to the server side and run the server file by using this command "python Server.py" it will ask you for client IP
enter the client IP of which you wanna get details of ssh.
Now, You will see the screen where you need to select option, option includes:
1. Successful (To check successfull ssh logins)
2. Disconnect (To check Disconnected ssh connections)
3. Invalid    (To chcek Invalid login counts)

note: In case there is any issue of index out of range then just make few changes in
the files Succes.py Disconnected.py Invald.py
changes to be made
change the variables, like if
count=s[5] change it to count=s[6]
Usr=s[7] chang it to Usr=s[8]
IPa=s[6] change it to Ipa=[7]
same changes in all 3 files
-variables names are different in all files

Why we need to made this changes:
because,  sometimes /var/log/auth.log saves data in list with extra spaces.
and as we are greping our data from this file, we need to take care about the extra spaces.

### Automation ###
I am using Asible for the Automation at the server side
1. Install the Ansible (apt-get install ansible -y)
2. create ansible user (useradd ansible) (passwd ansible)
3. Generate the ssh key (ssh-keygen)
4. Copy the ssh key to clients (ssh-copy-id ansible@<IP>) enter the password and copy will be done
5. Now, entry for ansible user in sudoers file (vim /etc/sudoers)
6. Add this line "ansible ALL=(ALL)  NOPASSWD:ALL"  
7. Add your clients to ansible (vim /etc/ansible/hosts)
Add following lines to the hosts file


[client1]
<IP>

[client2]
<IP>

8. Install git and "git clone https://github.com/starsunny/TekionTask/ansible/"
9. Go into the cloned directory (cd ansible)
10. change the server IP in client/Clients.py (ip = str("IP"))
11. Run the command (ansible-playbook setup.yml)
12. In case not working then go to the /etc/ssh/sshd.config and 
search the line "password authentication no" change it to "password authentication yes"
then repeat from step3.
### What it will do ##
It will copy the client directory to the both clients in /home/ubuntu directory
and setup the cron job

### Note ###
I have donw it for check the ubuntu user only, If you wanna check all the user
then you need to change one line in client/Succes.py,
you need to make some changes in the last line of this  file.
change variable in the line client.send("dialog --msgbox <result variable>,
  add this result in this line and remove all other variable.
  basically you need to replace the all other variable and put variable name result there.
  thwn you will get details pf all the other users.

