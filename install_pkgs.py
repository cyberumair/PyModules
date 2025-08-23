import importlib.util, os, sys
from main_msg import msg

# Only true mismatches are stored here
PKG_MAP = {
    "pillow": "PIL",
    "opencv-python": "cv2",
    "beautifulsoup4": "bs4",
    "scikit-learn": "sklearn",
    "qrcode[pil]": "qrcode"
}


def check_import(pkg: str) -> bool:
    """
    Try importing a package:
      1. First try pip_name.lower()
      2. Then try PKG_MAP if mismatch exists
    """
    try:
        __import__(pkg.lower())
        return True
    except ImportError:
        if pkg in PKG_MAP:
            try:
                __import__(PKG_MAP[pkg])
                return True
            except ImportError:
                return False
        return False

def check_install(pkg: str) -> bool:
    """Check if a package is installed or not"""
    return not check_import(pkg)


def install(pkg: str):
    """Try installing a package with pip"""
    if check_install(pkg):
        try:
            exit_code = os.system(f'{sys.executable} -m pip install {pkg}')
            if exit_code == 0 and not check_install(pkg):
                return pkg
            else:
                return
        except Exception as e:
            print("\nSomething Went Wrong")
            print(f"\n{e}")
            exit()
    else:
        return pkg


def install_pkgs(pkgs: list):
    """Install a list of packages"""
    pkg_installed = []
    pkg_done = []

    for p in pkgs:
        if not check_install(p):
            pkg_done.append(1)

    if len(pkg_done) == len(pkgs):
        print("\n✅ Done, All dependencies are already installed!\n")
        exit()
    else:
        print("\nInstalling the following Dependencies:\n")
        for index, pkg in enumerate(pkgs):
            print(f"{index+1}. {pkg}")
        print("")

        for pkg in pkgs:
            result = install(pkg)
            if result:
                pkg_installed.append(result)

        not_installed_pkgs = len(pkgs) - len(pkg_installed)

        print('')
        if not_installed_pkgs == 0:
            print("✅ Done, All dependencies installed Successfully!\n")
        else:
            print(f"❗ Something Went Wrong, {not_installed_pkgs} dependencie(s) are (is) Not installed.")
            print("\tExiting, Try running the program again...\n")
            exit()


if __name__ == "__main__":
    install_pkgs(["colorama", "pyjokes", "qrcode[pil]"])  # Example list
    print(f"\n{msg}\n")
