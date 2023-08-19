#i have done project by my own.
#Shouzab Khan
#skhan6
#networking socket programming
#networking socket programming



import socket
import random
import time

class Student:
        
    def __init__(self):
        self.localhost = '127.0.0.1'

    def createUDPServer(self, iUDPPortRobot, iUDPPortStudent, robotIP):

        ########################## STEP 4 CONTINUES ######################################### 
        try:
            
            # Create a UDP socket to send and receive data
            print("\nCreating UDP socket...")
            
        #STEP 4: creating a UDP socket s3 to send variable a num (5 < num < 10) on port eeeee which is iUDPPortStudent
            addr = (self.localhost, iUDPPortStudent)
            s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s3.bind(addr)
            print("Done")

        #STEP 4: Generating num (5 < num < 10)

            print("\nPreparing to send num...")
            num = random.randint(6,9)

            messageToTransmit=bytes(str(num), encoding='utf-8')

        #STEP 4: Sending variable num (5 < num < 10) to port fffff which is iUDPPortRobot

            s3.sendto(messageToTransmit,(robotIP,iUDPPortRobot))
            print("Number sent = %d" % (int(num)))



        #STEP 4: Receiving char string xxx with length num * 10 on port eeeee which is iUDPPortStudent
            print("\nReceiving UDP packet:")
            while True: # remove potentially duplicate msg
                data, addr = s3.recvfrom(int(num) * 10)
                data = data.decode()
                if int(data) != int(num):
                    break
            print("Received: ", data)
            
        ########################## STEP 4 ENDS #########################################

        ########################## STEP 5 ######################################### 
         
            print("\nPreparing to send UDP packets:")
            
            messageToTransmit = data

            print("Message to transmit: " + messageToTransmit)
            
        #STEP 5: Sending back the char string xxx with length num * 10 to port fffff which is iUDPPortRobot every 1 second
           
            print("\nSending UDP packets:")
        
            for i in range(0,5):
                s3.sendto(messageToTransmit.encode(),(robotIP,iUDPPortRobot))
                time.sleep(1)
                print("UDP packet %d sent" %(i+1))

        ########################## STEP 5 ENDS #########################################

        ########################## STEP 6  ######################################### 
            print("\ncompleted successfully!!!")
            s3.close()
        ########################## STEP 6 ENDS  ######################################### 
        except:
            print("UDP error")


    def createTcpServer(self, port):
        
        ########################## STEP 3 CONTINUES ######################################### 
        try:
            # Create a TCP socket to listen connection
            print("Creating TCP socket...")
            s_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s_2.bind((self.localhost, port))
            s_2.listen(5)
            print("Done")

            #STEP 3: creating a TCP socket s_2 at robot_5_char_string from Robot to accept a new connection
            print("\nTCP socket created, ready for listening and accepting connection...")

            #print "Waiting for connection on port %(listenPort)s" % locals()
            print("Waiting for connection on port", self.localhost, port)

            # accept connections from Robot, a new socket is constructed
            robot_fd, address = s_2.accept()
            robotIP = address[0]
            print("\nClient from %s at port %d connected" %(robotIP, address[1]))
            
            # Close the listen socket
            s_2.close()
            ########################## STEP 3 ENDS ######################################### 

            ########################## STEP 4 ######################################### 
            
            #STEP 4: Receiving the 12 char string from Robot string
            data = robot_fd.recv(100)
            print("Received 12 char string from Robot: " + str(data))

            iUDPPortRobot, iUDPPortStudent = data.decode().split(',', 1)

             #STEP 4: creating a UDP socket s3 to send variable a num (5 < num < 10) with the 12 char  from Robot which are iUDPPortRobot, iUDPPortStudent 

            self.createUDPServer(int(iUDPPortRobot), int(iUDPPortStudent), robotIP)

            robot_fd.close()
        ##################################################################   
        except:
            print("TCP error")
        
    
    def main(self):

        #STEP 1: is the executing of the file
        #Therefore comment proceed from STEP 2

        try:
        ############## STEP 2 #########################################
            ip = "127.0.0.1"

        #STEP 2:  ROBOT port
            port = 3310

            
            print("Client started")

            print("")

            # create a socket object
            client_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        ############## STEP 2 #########################################
        
        #STEP 2: connecting to the ROBOT at port 3310
            client_fd.connect((ip, port))

            #STEP2:  Getting the BlazerID
            iBlazerID = "Skhan6"

            #STEP2:  sending the BlazerID via the connection established
            sent_bytes = client_fd.send(iBlazerID.encode('utf-8'))
        
        ############## END OF STEP 2 #########################################


        ########################## STEP 3 #########################################    
            
            #STEP3: receiving the 5 char string from Robot
            robot_5_char_string = client_fd.recv(100)

            if robot_5_char_string:
                
                print("Received 5 char string from Robot\n")

            #STEP3: creating a TCP socket s_2 at robot_5_char_string from ROBOT to accept a new connection
                self.createTcpServer(int(robot_5_char_string))
                client_fd.close()
        ##################################################################   
            else:
                    print("Unable received 5 char string from Robot")
            
        except IndexError:
            print("USAGE: python3 client.py <port number of Robot>\n")

        except BrokenPipeError:
            print("Lost connection with Robot\n")

        except ConnectionRefusedError:
            print("Robot port is not active [check the Robot for the active port]\n")

        except KeyboardInterrupt:
            client_fd.close()
            print("\n")

if __name__ == '__main__':
    student_int = Student()
    student_int.main()




