import os
import subprocess


def update_submodules() -> bool:
    """
        To Use this function, please create a Script in the main directory of your project.
        Then, call this function and all submodules will be updated
        :return:  true or false
    """
    updated = False

    current_dir = os.path.dirname(os.path.abspath(__file__))
    submodule_dir = 'submodules'
    submodule_path = os.path.join(current_dir, submodule_dir)

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
    update_submodules()
