from datetime import datetime
import os
import subprocess
from datetime import datetime

def append_datetime():
    print('Appending')
    with open('src/counter.txt', 'a') as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{current_time}\n')

def create_git_branch_and_commit():
    today = datetime.now().strftime('%Y-%m-%d')
    branch_name = today
    
    try:
        # Fetch latest changes
        subprocess.run(['git', 'fetch', 'origin'], check=True)
        
        # Try to create and checkout branch
        result = subprocess.run(['git', 'checkout', '-b', branch_name], capture_output=True, text=True)
        if result.returncode != 0:
            # If branch already exists, just checkout
            subprocess.run(['git', 'checkout', branch_name], check=True)
            
            # Pull latest changes with --rebase to avoid merge commits
            subprocess.run(['git', 'pull', '--rebase', 'origin', branch_name], check=True)

        append_datetime()
        
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', "Added new date"], check=True)
        
        # Add --force if you want to override remote changes
        # Or remove --force to ensure you don't accidentally override important changes
        subprocess.run(['git', 'push', '--force', 'origin', branch_name], check=True)
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e.cmd}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
create_git_branch_and_commit()