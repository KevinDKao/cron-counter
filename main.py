from datetime import datetime
import os
import subprocess
import random
import time

REPO_PATH = '/home/kkao/cron-counter'
# Store your token in an environment variable
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # You'll need to set this environment variable

def set_git_credentials():
    try:
        # Set email
        subprocess.run(['git', 'config', 'user.email', 'kevindkao@gmail.com'], 
                      check=True,
                      cwd=REPO_PATH)
        
        # Set the token as credential
        repo_url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url'], 
                                         cwd=REPO_PATH).decode().strip()
        if repo_url.startswith('https://'):
            # Convert HTTPS URL to include token
            new_url = f'https://{GITHUB_TOKEN}@github.com/KevinDKao/cron-counter.git'
            subprocess.run(['git', 'remote', 'set-url', 'origin', new_url], 
                         check=True,
                         cwd=REPO_PATH)
            
        print("Git credentials configured successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error setting Git credentials: {e}")

def append_datetime():
    print('Appending')
    with open(os.path.join(REPO_PATH, 'src/counter.txt'), 'a') as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{current_time}\n')

def create_git_branch_and_commit():
    try:
        # Set Git credentials first
        set_git_credentials()
        
        # Stash any existing changes
        subprocess.run(['git', 'stash'], 
                      check=True,
                      cwd=REPO_PATH)
        
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
        
        # Pop stashed changes if any
        try:
            subprocess.run(['git', 'stash', 'pop'], 
                         check=True,
                         cwd=REPO_PATH)
        except subprocess.CalledProcessError:
            # If there was nothing to pop, that's fine
            pass
        
        append_datetime()
        
        # Add and commit changes
        subprocess.run(['git', 'add', '.'], 
                      check=True,
                      cwd=REPO_PATH)
        
        try:
            subprocess.run(['git', 'commit', '-m', "Added new date"], 
                         check=True,
                         cwd=REPO_PATH)
            
            # Push changes
            subprocess.run(['git', 'push', 'origin', 'main'], 
                         check=True,
                         cwd=REPO_PATH)
        except subprocess.CalledProcessError as e:
            print(f"Nothing to commit or error in committing: {e}")
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e.cmd}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
random_number = random.randint(5, 15)
print(f'Running the GitHub Script for {random_number+1} times')
for i in range(random_number):
    create_git_branch_and_commit()
    time.sleep(5)