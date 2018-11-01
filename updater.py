#Updates the OS of the raspberry Pi 
import os
import time 

git_hash_file = "git_hash"

#returns current hash
def current_git_hash():
    return os.popen("git rev-parse --verify HEAD").read().replace("\n","")

#retrieves the hash from git_hash file
def get_git_hash_from_file():
    if not os.path.isfile(git_hash_file):
        git_hash = ""
    else:
        with open(git_hash_file, "r") as myfile:
            git_hash = myfile.read()
            git_hash = git_hash.split("\n")[0]

    return git_hash

#updates the git_hash file with current hash
def update_git_hash_file():
    print("Updating git hash file!")
    git_hash = current_git_hash()
    with open(git_hash_file, "w+") as writer:
        writer.write(str(git_hash) + "\n")

#compares the hash in hash file with current hash
def compare_git_hash():
    git_hash = get_git_hash_from_file()
    if git_hash == "" or git_hash !=current_git_hash():
        update_git_hash_file()
        return False
    else:
        return True

def update():
    while True:
        os.system("git pull origin live")
        if not compare_git_hash():
            print("Updated system!")
            print("REBOOTING!")
            os.system("sudo reboot")
        time.sleep(600)
    
if __name__ == '__main__': update()