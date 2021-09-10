import os
import sys
src_path = f"{os.path.abspath('')}\\src"
sys.path.append(src_path)
for path, subdirs, _ in os.walk(src_path):
    # ! Uncomment only if __pycache__ folder affects code
    # if "__pycache__" in subdirs:
    #     subdirs.remove("__pycache__")
    if subdirs:
        print(subdirs)
        for subdir in subdirs:
            sys.path.append(f"{path}\\{subdir}")