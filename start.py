import subprocess
import time
import urllib2
import sys

# cmd = "ssh -i ./data/serveo.net/id_rsa -R ci.signalwerk.ch:80:localhost:80 serveo.net"
cmd = "ssh -p 2222 -R ci:80:localhost:80 ssh-dns.signalwerk.ch"


def check_url( url, timeout=15 ):
    try:
        return urllib2.urlopen(url,timeout=timeout).getcode() == 200
    except urllib2.URLError as e:
        return False


def main():
    print("--- ssh-dns start\n")
    proc = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)

    while True:
        time.sleep(30)
        print("    check\n")
        online = check_url("https://ci.signalwerk.ch/")


        if (online == False):
            print("    offline!\n")
            break

        print("    online!\n")

    proc.terminate()
    print("--- ssh-dns end\n")


while True:
    print("--- start\n")
    main()
    time.sleep(30)
