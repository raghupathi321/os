import os

try:
    os.setuid(1000)  # change to UID 1000 (normal user, may require root)
    print("UID changed successfully")
except PermissionError:
    print("Permission denied: Run as root to change UID")
