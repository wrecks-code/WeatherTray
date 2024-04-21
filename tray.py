from typing import Any

from pystray import Icon, Menu, MenuItem
from PIL import Image
import weather


ICON: Any = None


def save_mmt_config_clicked(): ...


def icon_tray_clicked(): ...


def exit_clicked():
    ICON.stop()


def open_folder_clicked(): ...


def startup_with_windows_clicked(): ...


def get_icon_image(_option: bool) -> Image.Image:
    if _option:
        return Image.open("paths.ASSETS_ICON_ENABLED_PATH")
    return Image.open("paths.ASSETS_ICON_DISABLED_PATH")


def is_true() -> bool:
    return True


def init_tray():
    menu = (
        MenuItem("Weather", icon_tray_clicked, default=True, visible=False),
        MenuItem(
            weather.get_weather()[weather.DESCRIPTION_KEY],
            startup_with_windows_clicked,
            checked=lambda icon: is_true,
        ),
        Menu.SEPARATOR,
        MenuItem("Exit", exit_clicked),
    )

    # pylint: disable=global-statement
    global ICON
    ICON = Icon(
        "ui_strings.APP_NAME", Image.open("icon.ico"), "ui_strings.APP_NAME", menu
    )
    ICON.run()
