from distutils.util import copydir_run_2to3
import subprocess




def scan() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it nmap_scan bash" '

        #Metasploite
        cmd4=""" gnome-terminal -- bash  -c " docker run --rm -h '--Metasploitable--' --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  bash -c '/bin/services.sh && bash' "  """

        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)  
        subprocess.Popen(cmd4 ,shell=True)  



def DHCPspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=host --ip 192.168.2.22 --privileged -it yersinia bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def DNSspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 --privileged -it ettercap bash" '
        #cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=host -it ettercap bash" '
        #cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=host -it vimagick/dsniff bash" '


        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def ARPspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it arp_kali bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it strm/metasploit:latest bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def MACflooder() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it strm/metasploit:latest bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def IPspoofing() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        #Test
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Test--" --name Test --network=NET --ip 192.168.2.33 -it debien_test bash" '
   

        #Attacker
        cmd3=""" gnome-terminal -- bash -c 'docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it iphping:latest bash' """
        
        #Sniffing 
        cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)



def Sniffing() : 

        #Victime
        #cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        
        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it session_ubuntu_2 bash" '
        
        #server---metasploitable2
        #cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Metasploitable--" --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  sh -c "/bin/services.sh && bash" '
        cmd2=""" gnome-terminal -- bash  -c " docker run --rm -h '--Metasploitable--' --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  bash -c '/bin/services.sh && bash' "  """


        #Attacker
        #cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it --privileged ettercap bash" '
        
        #Attacker
        #cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker2--" --name Attacker2 --network=NET --ip 192.168.2.33 -it nmap_sniffing -sn 192.168.2.0/24 " '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)



def MITMs() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it --privileged mitm_ubuntu bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it --privileged  mitm_kali bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '
        
        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)


def ICMPredirection() : 

        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it --privileged mitm_ubuntu bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it --privileged  mitm_kali bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)

################################################# Apps Layer ############################################## 


def ReverseShell() : 

        #Run container
        subprocess.run("gnome-terminal -- bash -c  'docker run --rm -h '--Attacker--' --name Attacker --network=NET --ip 192.168.2.22 -d -it sauravbrahma/metasploit_image:latest '  ", shell=True)



        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it debien_test bash" '
        
        #Attacker
        cmd2=' gnome-terminal -- bash -c "docker exec -it Attacker bash" '
        cmd3=' gnome-terminal -- bash -c "docker exec -it Attacker bash" '

        #Sniffing 
        cmd4=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)




def SessionHijacking() : 


        #Run container
        subprocess.run("gnome-terminal -- bash -c  'docker run --rm -h '--Attacker--' --name Attacker --network=NET --ip 192.168.2.22 -d -it session_ubuntu_1 ' ", shell=True)
  
        #Victime
        cmd1=' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it session_ubuntu_2 bash" '
        
        #server---metasploitable2
        #cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Metasploitable--" --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  sh -c "/bin/services.sh && bash" '
        cmd2=""" gnome-terminal -- bash  -c " docker run --rm -h '--Metasploitable--' --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  bash -c '/bin/services.sh && bash' "  """


        
        #Attacker
        cmd3 = ' gnome-terminal -- bash -c " docker exec -it Attacker bash " '
        cmd4 = ' gnome-terminal -- bash -c " docker exec -it Attacker bash " '

        #Sniffing 
        cmd5=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)
        subprocess.Popen(cmd5 ,shell=True)



def SessionReset() : 

        #server
        cmd1 = ' gnome-terminal -- bash -c " docker run --rm -h "--Server--" --name Server -it --network=NET --ip 192.168.2.33 --privileged session_ubuntu:latest bash " '
        #client
        cmd2 = ' gnome-terminal -- bash -c " docker run --rm -h "--Victime--" --name Victime --network=NET --ip 192.168.2.11 -it --privileged  session_ubuntu:latest bash " '
        
        #Attacker
        cmd3 = ' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it --privileged session_hping:latest bash " '


        #Sniffing 
        cmd4 = ' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)
        subprocess.Popen(cmd4 ,shell=True)


def DOS() : 

        #Victime 
        cmd1=""" gnome-terminal -- bash  -c " docker run --rm -h '--Metasploitable--' --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  bash -c '/bin/services.sh && bash' "  """

        #Attacker
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Attacker--" --name Attacker --network=NET --ip 192.168.2.22 -it dos_smurf bash" '
        
        #Sniffing 
        cmd3=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)
        subprocess.Popen(cmd3 ,shell=True)



def DOS_Memory() : 

        #Victime 
        cmd1=""" gnome-terminal -- bash  -c " docker run --rm -h '--Metasploitable--' --name metasploitable --network=NET --ip 192.168.2.33 -it tleemcjr/metasploitable2  bash -c '/bin/services.sh && bash' "  """

        #Sniffing 
        cmd2=' gnome-terminal -- bash -c " docker run --rm -h "--Sniffing--" --name Sniffing --net=host tcpdump -i br_test -w - | wireshark -k -i - " '

        #Run in new terminal
        subprocess.Popen(cmd1 ,shell=True)
        subprocess.Popen(cmd2 ,shell=True)

