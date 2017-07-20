from SendKeys import SendKeys
import time

def menu():
    print("\n\nChoose from list:\n")
    print("\t1 Start attack")
    print("\t2 Exit\n")

def brute():
    print "importing wordlist"
    with open("wordlist.txt","r") as f:
        warray=[line.rstrip('\n') for line in f]
    print("\nwordlist imported")
    print "\nyou now have 10 seconds to make sure the active window is\nthe target for the bruteforce attack"
    time.sleep(10)
    attack_number=0
    print "attack starting..."
    while int(attack_number) != int(len(warray)):
        SendKeys(warray[attack_number])
        SendKeys("{ENTER}")
        time.sleep(0.2)
        SendKeys("{ENTER}")
        attack_number+=1
    if attack_number == int(len(warray)):
        print "attack complete"
        time.sleep(5)

def main():
    menu()
    menuchoice=int(raw_input("Enter selection: "))
    if menuchoice == 1:
        print "\tStart attack selected"
        brute()
    elif menuchoice == 1:
        print "\tExiting program, have a nice day!"
        exit()
        
main()
