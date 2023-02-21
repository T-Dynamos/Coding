import time
import os


def run() -> os.system:
    os.system("mpc pause")
    os.system("kitty pipes.sh -p 10")
    return os.system("flite -t '{}'".format(message))


while True:
    with open("/home/tdynamos/.state", "r") as file:
        if file.read().split("\n")[0] == "sts":
            file.close()
            time.sleep(2)
            with open("/home/tdynamos/.state") as file_2:
                if file_2.read().split("\n")[0] == "sts2":
                    file_2.close()
                    time.sleep(2)
                    with open("/home/tdynamos/.state") as file_3:
                        if file_3.read().split("\n")[0] == "sts3":
                            run()
                            file_3.close()
