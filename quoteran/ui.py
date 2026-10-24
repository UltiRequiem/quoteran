"""
Colored terminal output.
"""
import colorama

cyan, red = (
    colorama.Fore.CYAN,
    colorama.Fore.RED,
)


def setup_colorama() -> None:
    """
    Make ANSI colors work on old Windows consoles. Does nothing elsewhere.
    """
    colorama.just_fix_windows_console()


def cprint(
    text: str,
    color: str = red,
    brightness: str = colorama.Style.NORMAL,
    **kwargs,
) -> None:
    """
    Print the text with colors.
    """
    print(f" {brightness}{color}{text}{colorama.Style.RESET_ALL}", **kwargs)
