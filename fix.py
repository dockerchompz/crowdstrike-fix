import glob
import os

for file in glob.glob("C:\\Windows\\System32\\drivers\\CrowdStrike\\C-00000291*.sys"):
    try:
        os.remove(file)
    except Exception as e:
        print(e)
