#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BHANU
#
# Created:     18-01-2019
# Copyright:   (c) BHANU 2019
# Licence:
#-------------------------------------------------------------------------------

# Creating necessary Functions for Rail Frence cipher

def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = range(numrails - 1) + range(numrails - 1, 0, -1)
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x
    if 0: # debug
        for rail in fence:
            print ''.join('.' if c is None else str(c) for c in rail)
    return [c for rail in fence for c in rail if c is not None]

def encode(text, n):
    return ''.join(fence(text, n))

def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)

# Create Encryption object

class text():
    def __init__(self,a):
        self.a=a
        self.b=""
    def Caesar(self):                       #Encryption of Caesar Cipher variant
        z=int(raw_input("Enter numeric password"))
        l=len(self.a)
        x=0
        c=""
        if z>94:
            z=z%94
        for i in range(0,l):
            k=ord(self.a[i])
            j=0
            t=k+z
            while j==0:
                if t>125:
                    t=t-94
                else:
                    j=j+1

            v=chr(t)
            c=c+str(v)
        self.b=c
        return self.b
    def RailFence(self):                       # Encryption of Rail Fence Cipher
        z=input("Enter numeric Key")
        print encode(self.a,z)

# Create Decryption Object

class dtext():
    def __init__(self,a):
        self.a=a
        self.b=""
    def Caesar(self):                      # Decryption of Caesar Cipher variant
        z=input("Enter numeric password")
        l=len(self.a)
        x=0
        c=""
        if z>94:
            z=z%94
        for i in range(0,l):
            k=ord(self.a[i])
            j=0
            t=k-z
            while j==0:
                if t<32:
                    t=t+94
                else:
                    j=j+1
            v=chr(t)
            c=c+str(v)
        self.b=c
        return self.b
    def RailFence(self):                       # Decryption of Rail Fence Cipher
        z=input("Enter numeric Key")
        print decode(self.a,z)

# Execution of Program
m=0
while m==0:
    print "Hello user \n"
    print "Enter corresponding no. to initate execution \n"
    i1=input("(1-Encryption,2-Decryption,3-Add Content to your Vault,4-View Your Vault Contents,5-Exit) \n")
    if i1==1:                                               # Encryption Process
        print "What do you wish to encrypt ? \n"
        i2=input("(1-text,2-text file) \n")
        if i2==1:
            z=raw_input("Enter text for encryption. \n")
            x=text(z)
            i3=input("Choose encryption module(1-3) \n")
            if i3==1:
                print x.Caesar(),"\n"
            elif i3==2:
                print x.RailFence(),"\n"
            elif i3==3:
                y=text(x.Caesar())
                print y.RailFence(),"\n"
            else:
                print "Wrong Input. \n"
        elif i2==2:
            y=raw_input("Enter file address. \n")
            l=open(y,"w+")
            z=l.read()
            x=text(z)
            i3=input("Choose encryption module(1-3) \n")

            if i3==1:
                k=x.Caesar()
                l.write(k)
            elif i3==2:
                    k=x.RailFence(),"\n"
                    l.write(k)
            elif i3==3:
                    t=text(x.Caesar())
                    k=t.RailFence(),"\n"
                    l.write(k)
            else:
                    print "Wrong input. \n"
    elif i1==2:                                             # Decryption Process
        print "What do you wish to decrypt ? \n"
        i2=input("(1-text,2-text file) \n")
        z=raw_input("Enter text for decryption. \n")
        x=dtext(z)
        if i2==1:
            i3=input("Choose decryption module(1-3) \n")
            if i3==1:
                print x.Caesar(),"\n"

            elif i3==2:
                print x.RailFence(),"\n"
            elif i3==3:
                y=dtext(x.Caesar())
                print y.RailFence(),"\n"
            else:
                print "Wrong Input."
        elif i2==2:
            y=raw_input("Enter file address.")
            l=open(y,"r")
            z=l.read()
            x=dtext(z)
            if i2==1:
                i3=input("Choose decryption module(1-3)")
                if i3==1:
                    k=x.Caesar(),"\n"
                    l.write(k)
                elif i3==2:
                    k=x.RailFence(),"\n"
                    l.write(k)


                elif i3==3:
                    t=text(x.Caesar())
                    k=t.RailFence(),"\n"
                    l.write(k)
                else:
                    print "Wrong input."
    elif i1==3:                                             # Saving new message
        n=open("C:\\Users\BHANU\Desktop\Vault.txt","a")     #Update the path to vault according to installation
        z=raw_input("Enter data to be added.")
        n.seek(2)
        n.writelines(z)
        n.close()
        print "\n"
    elif i1==4:                                          # Showing saved message
        n=open("C:\\Users\BHANU\Desktop\Vault.txt","r")  # Update Path
        print n.read(),"\n"
        n.close()
    elif i1==5:                                                           # Exit
        m+=1
exit()
