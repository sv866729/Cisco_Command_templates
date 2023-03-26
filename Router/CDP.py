cdp_timer = input("Please enter the CDP packet transmission interval in seconds: ")
cdp_holdtime = input("Please enter the CDP hold time in seconds: ")
cdp_off = input("Do you want to turn off CDP? (yes or no): ")


#Cisco Discovery Protocol (CDP)
    #Cisco proprietary Layer 2 protocol
    #Collect/discover device information about locally attached neighbor devices
        #Hardware
        #Protocol information
#show cdp config
print(f"""show cdp""")
#shows connceted hosts
print(f"""show cdp neighbors""")
#configuration optionsr
#Sets how often packets are transmitted 
#Time device will hold packets received from
#Turn off CDP
print(f"""
print("cdp run")
print(f"cdp timer {cdp_timer}")
print(f"cdp holdtime {cdp_holdtime}")
if cdp_off == "yes":
    print("no cdp"
""")
