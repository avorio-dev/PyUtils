import os
import subprocess
from pathlib import Path


def update_submodules(project_name) -> bool:
    """
        To Use this function, please create a Script in the main directory of your project.
        Then, call this function and all submodules will be updated
        :return:  true or false
    """
    updated = False

    # Current Directory where start search
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = Path.cwd()

    root_dir = ""
    for parent_dir in current_dir.parents:
        if parent_dir.parts[-1] == project_name:
            root_dir = parent_dir
            break

    submodule_dir = 'submodules'
    submodule_path = os.path.join(root_dir, submodule_dir)

    try:
        # Run command git submodule update --remote
        subprocess.run(['git', 'submodule', 'update', '--remote'], check=True, cwd=submodule_path, shell=True)

        updated = True
        print("Submodules Updated")

    except subprocess.CalledProcessError as e:
        print(f"Error during submodules update: {e}")

    except Exception as ex:
        print(f"Undefined error in submodules update: {ex}")

    return updated


if __name__ == "__main__":
    project_name = "PyUtils"
    update_submodules(project_name)
