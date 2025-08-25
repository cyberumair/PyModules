from colorify import *

def run(func):
    try:
        func()
        return f"{Fore.GREEN}✔ Success{Style.RESET_ALL}"
        
    except (FileNotFoundError, ModuleNotFoundError):
        return f"\n{Fore.RED}❗ Requirements are not satisfied.{Style.RESET_ALL} Run 'python requirements.py' to install requirements"
        
    except Exception as e:
        return f"\n{Fore.RED}❗ Error:{Style.RESET_ALL} {e}"


if __name__ == '__main__':
    try:
        from showcase import show_tool
        show_tool(
            "run safe MODULE",
            "🛡 Wraps functions safely",
            "✅ Handles errors",
            "⚡ Keeps your tools clean",
            "Just call 'safe_run.run(your_function)' in your main project 🎉"
        )
    except:
        exit()
