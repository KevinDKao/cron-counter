from datetime import datetime
import os
import subprocess
from datetime import datetime

def append_datetime():
    with open('src/counter.txt', 'a') as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f'{current_time}\n')

# Example usage
append_datetime()


def create_git_branch_and_commit():
    today = datetime.now().strftime('%Y-%m-%d')
    branch_name = "main"
    
    try:
        # Git commands with proper argument handling
        # subprocess.run(['git', 'checkout', '-b', branch_name], check=True)
        # print(f"Executed: git checkout -b {branch_name}")

        # subprocess.run(['git', 'checkout', 'main'], check=True)
        # print(f"Executed: git checkout main")
        
        subprocess.run(['git', 'add', '.'], check=True)
        print("Executed: git add .")
        
        # Keep commit message as a single argument
        subprocess.run(['git', 'commit', '-m', "Added new date"], check=True)
        print('Executed: git commit -m "Added new date"')
        
        subprocess.run(['git', 'push', 'origin', branch_name], check=True)
        print(f"Executed: git push origin {branch_name}")
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e.cmd}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
create_git_branch_and_commit()