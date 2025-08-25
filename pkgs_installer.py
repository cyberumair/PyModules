import importlib.util, os, sys
from colorify import *

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
            from colorify import Fore, Style
            print(f"\n{Fore.RED}❗ Something Went Wrong{Style.RESET_ALL}")
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
        print(f"\n{Fore.GREEN}✅ Done, All dependencies are already installed!{Style.RESET_ALL}\n")
        exit()
    else:
        print(f"\n{Fore.YELLOW}📦 Installing the following Dependencies:{Style.RESET_ALL}\n")
        for index, pkg in enumerate(pkgs):
            print(f"{Fore.CYAN}{index+1}. {pkg}{Style.RESET_ALL}")
        print("")

        for pkg in pkgs:
            result = install(pkg)
            if result:
                pkg_installed.append(result)

        not_installed_pkgs = len(pkgs) - len(pkg_installed)

        print('')
        if not_installed_pkgs == 0:
            print(f"{Fore.GREEN}✅ Done, All dependencies installed Successfully!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}❗ Something Went Wrong, {not_installed_pkgs} dependencie(s) are (is) Not installed.{Style.RESET_ALL}")
            print(f"\t{Fore.YELLOW}Exiting, Try running the program again...{Style.RESET_ALL}\n")
            exit()


if __name__ == "__main__":
    try:
        from showcase import show_tool

        show_tool(
            "pkgs installer module",
            "📦 Smart installer", "✅ Handles mismatches", "⚡ Auto-installs dependencies",
            "Just call \"install_pkgs(['pkg1', 'pkg2', ...])\" in your main project 🎉"
        )

    except Exception as e:
        print(e)
