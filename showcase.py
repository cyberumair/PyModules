from colorify import *
from main_msg import msg

def show_tool(tool_name: str, description1: str, description2: str, description3: str, how_to: str):
    """
    Displays a standardized tool showcase banner with:
    - Tool name (highlighted)
    - Short description (multi-color + emojis)
    - How-to-use line
    - Common closing message (from main_msg)
    """

    # Decorative lines
    len_lines = len(tool_name) * 2
    lines = f"{Fore.BLUE}{'='*len_lines}{Style.RESET_ALL}"

    print(f"\n{lines}")
    print(f"\t{Fore.CYAN}{Style.BRIGHT}{tool_name.upper()}{Style.RESET_ALL}")
    print(lines, '\n')

    print(description1, f'{Fore.CYAN}{description2}{Style.RESET_ALL}', description3)

    print(f"\n{Fore.CYAN}💡 How to use:{Style.RESET_ALL} {how_to}\n")

    print(f"{Fore.BLUE}{msg}{Style.RESET_ALL}\n")


if __name__ == '__main__':
    show_tool(
        "SHOWCASE MODULE",
        "🎯 Centralized banner",
        "✅ Multi-color descriptions",
        "⚡ Reusable across all modules",
        "Just call 'show_tool()' inside any module 🎉"
    )