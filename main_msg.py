msg = "Thanks for using this PyModule, it was created by 'Umair Shakoor 😈' (@cyberUmair). Check other useful modules at 'https://github.com/cyberumair/PyModules' \n\tHappy Coding 🙂"

if __name__ == "__main__":
    try:
        from showcase import show_tool

        show_tool(
            "MAIN_MSG",
            "📢 Provides a universal message",
            "✅ Auto-shared across modules",
            "🔄 Update once, reflect everywhere",
            "Just call 'from main_msg import msg' and use 'print(msg)' 🎉",
        )

    except:
        pass
