PLATFORM_TOOLS_DIR = "platform-tools"


class Script:
    ADB_RESET = "appiumatic/scripts/adb_reset.sh"
    CHECK_BOOT_ANIM = "appiumatic/scripts/check_boot_anim.sh"
    BOOT_STANDARD_EMU = "appiumatic/scripts/boot_standard_emulator.sh"
    BOOT_GENYMOTION_EMU = "appiumatic/scripts/boot_genymotion_emulator.sh"
    KILL_STANDARD_EMU = "appiumatic/scripts/kill_standard_emulator.sh"
    KILL_GENYMOTION_EMU = "appiumatic/scripts/kill_genymotion_emulator.sh"
    START_APPIUM = "appiumatic/scripts/start_appium.sh"


class GUIActionType:
    CLICK = "click"
    LONG_CLICK = "long-click"
    CHECK = "check"
    UNCHECK = "uncheck"
    SWIPE_UP = "swipe-up"
    SWIPE_DOWN = "swipe-down"
    SWIPE_RIGHT = "swipe-right"
    SWIPE_LEFT = "swipe-left"
    TEXT_ENTRY = "text-entry"
    HOME_NAV = "home"
    BACK_NAV = "back"
    ENTER_KEY = "enter"
    LAUNCH = "launch"


class SystemActionType:
    LAUNCH = "launch"
    RUN_IN_BACKGROUND = "run-in-background"


class TargetType:
    APP = "App"
    NAV = "Nav"
    SPINNER = "Spinner"
    EDIT_TEXT = "EditText"
    TEXT_VIEW = "TextView"
    BUTTON = "Button"
    RADIO_BUTTON = "RadioButton"
    CHECK_BOX = "CheckBox"
    IMAGE_BUTTON = "ImageButton"


class SelectorType:
    ID = "id"
    XPATH = "xpath"
    SYSTEM = "system"


class KeyCode:
    HOME = 3
    BACK = 4
    RETURN = 66


class TargetState:
    ENABLED = "enabled"
    DISABLED = "disabled"
