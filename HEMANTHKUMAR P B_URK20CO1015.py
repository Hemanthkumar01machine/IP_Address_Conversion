"""Program to Convert Valid Dotted deciaml to Binary, Octal and Hexadeciaml 
And store the same in a file named conversion.txt with Handling Exceptions
Come on Let's try it Out
Enter 10 IPv4 Addresses"""

print(__doc__)
#Initializing as 1st IP later it will be updated till 10  
items=1

#Creating a file named conversion.txt where the results will be stored
with open("conversion.txt","w") as f:
    while items<=10:
        ip_li=[]        #Initializing an empty list that stores the IP address in different formats
        ipv4=input()        #Getting an IPv4 address as an Input from the user

        #Handling Exceptions
        try:       
            ipv4_splited=list(map(int,ipv4.split(".")))         #Convertig octets to a list of integers

            #Checking Is the IP is a valid else raise a customized Exception
            if len(ipv4_splited)==4 and all(octet<=255 for octet in ipv4_splited) and ipv4_splited[0]>=1:
                #Appending Dotted decimal representation of IPv4 to the list
                ip_li.append(ipv4)      

                ip_b=list(map(bin,ipv4_splited))        #Convertig octets to a list of binary numbers
                for i in range(len(ip_b)):
                    ip_b_i_replaced=ip_b[i].replace("0b","")        #Removing 0b from each element
                    #Adding 0's at MSB to make it as 8 bits
                    ip_b_i_reversed=ip_b_i_replaced[::-1]
                    while len(ip_b_i_reversed)<8:
                        ip_b_i_reversed+="0"
                    ip_b_i=ip_b_i_reversed[::-1]
                    ip_b[i]=ip_b_i
                #Appending Binary representation of IPv4 to the list
                ip_li.append(" ".join(ip_b))

                ip_o=list(map(oct,ipv4_splited))        #Convertig octets to a list of octal numbers
                for i in range(len(ip_o)):
                    ip_o_i_replaced=ip_o[i].replace("0o","")        #Removing 0c from each element
                    #Adding 0's at MSB to make it as 4 digits of Octal number
                    ip_o_i_reversed=ip_o_i_replaced[::-1]
                    while len(ip_o_i_reversed)<4:
                        ip_o_i_reversed+="0"
                    ip_o_i=ip_o_i_reversed[::-1]
                    ip_o[i]=ip_o_i
                #Appending Octal representation of IPv4 to the list
                ip_li.append(" ".join(ip_o))

                ip_h=list(map(hex,ipv4_splited))        #Convertig octets to a list of hexadeciaml numbers
                for i in range(len(ip_h)):
                    ip_h_i_replaced=ip_h[i].replace("0x","")        #Removing 0x from each element
                    #Adding 0's at MSB to make it as 2 digits of Hexadecimal number
                    ip_h_i_reversed=ip_h_i_replaced[::-1]
                    while len(ip_h_i_reversed)<2:
                            ip_h_i_reversed+="0"
                    ip_h_i=ip_h_i_reversed[::-1]
                    ip_h[i]=ip_h_i
                #Appending Hexadeciaml representation of IPv4 to the list
                ip_li.append(" ".join(ip_h).upper())

                #Writing the list of contents into the file
                f.write(str(ip_li))
                f.write("\n")
                print(ip_li)
                items+=1        #Incrementing items by 1
            else:
                raise Exception("INVALID IPv4 address Please type a valid address")     #Raising a customized Exception called as Invalid if the IP is not a valid one
        except Exception as e:
            print(e)        #Displaying the Exception that is caused while the program is running
