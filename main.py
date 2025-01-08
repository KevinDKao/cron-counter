from datetime import datetime
import os
import subprocess
from datetime import datetime

# Set the working directory to where your Git repository is
REPO_PATH = '/home/kkao/cron-counter'

def set_git_email():
    try:
        subprocess.run(['git', 'config', 'user.email', 'kevindkao@gmail.com'], 
                      check=True,
                      cwd=REPO_PATH)
        print("Git email configured successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error setting Git email: {e}")

def append_datetime():
    print('Appending')
    with open(os.path.join(REPO_PATH, 'src/counter.txt'), 'a') as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{current_time}\n')

def create_git_branch_and_commit():
    try:
        # Set Git email first
        set_git_email()
        
        # Fetch latest changes
        subprocess.run(['git', 'fetch', 'origin'], 
                      check=True,
                      cwd=REPO_PATH)
        
        # Checkout main branch
        subprocess.run(['git', 'checkout', 'main'], 
                      check=True,
                      cwd=REPO_PATH)
        
        # Pull latest changes with rebase
        subprocess.run(['git', 'pull', '--rebase', 'origin', 'main'], 
                      check=True,
                      cwd=REPO_PATH)

        append_datetime()
        
        subprocess.run(['git', 'add', '.'], 
                      check=True,
                      cwd=REPO_PATH)
        subprocess.run(['git', 'commit', '-m', "Added new date"], 
                      check=True,
                      cwd=REPO_PATH)
        subprocess.run(['git', 'push', 'origin', 'main'], 
                      check=True,
                      cwd=REPO_PATH)
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e.cmd}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
create_git_branch_and_commit()