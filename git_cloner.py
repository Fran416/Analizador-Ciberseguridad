import os
import shutil
import subprocess

TEMP_DIR = "temp_repos"

def clone_repo(url: str) -> bool:
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    
    os.makedirs(TEMP_DIR, exist_ok=True)
    command = ["git", "clone", "--depth", "1", url, TEMP_DIR]
    
    try:
        subprocess.run(command, check=True, capture_output=True)
        return True
    except:
        return False

def cleanup():
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)    
        

