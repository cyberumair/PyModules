import importlib.util

if importlib.util.find_spec('colorama'):
    from colorama import Style, Fore, init
    init(autoreset=True)
else:
    class Dummy:
        def __getattr__(self, name): return ''
    Style = Fore = Dummy()

if __name__ == '__main__':
    try:
        from showcase import show_tool
        show_tool(
            "COLORIFY MODULE",
            "✨ Adds beautiful colors",
            "✅ Auto toggle",
            "🎨 For all CLI Tools",
            "Just add 'from colorify import *' at the top of your project 🚀"
        )
    except:
        exit()
