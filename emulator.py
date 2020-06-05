import subprocess
import logging
import os
import shutil
import time
import constants

from exceptions import AdbNotFound

logger = logging.getLogger(__name__)


def check_adb(sdk_path):
    adb_exec_path = os.path.join(sdk_path, constants.PLATFORM_TOOLS_DIR, "adb")
    return shutil.which(adb_exec_path) is not None


def reset_adb(sdk_path):
    adb_available = check_adb(sdk_path)
    if not adb_available:
        logger.debug("Could not find ADB!")
        raise AdbNotFound("Could not find ADB. Please check your Android SDK path.")

    adb_exec_path = os.path.join(sdk_path, constants.PLATFORM_TOOLS_DIR, "adb")
    adb_reset_cmd = "{} {}".format(constants.ADB_RESET_SCRIPT, adb_exec_path)
    subprocess.check_call(adb_reset_cmd, shell=True)


def check_device_available(sdk_path):
    """
    checks if there is a connected device
    support multiple devices in future
    """
    adb_available = check_adb(sdk_path)
    if not adb_available:
        logger.debug("Could not find ADB!")
        raise AdbNotFound("Could not find ADB. Please check your Android SDK path.")

    adb_exec_path = os.path.join(sdk_path, constants.PLATFORM_TOOLS_DIR, "adb")
    process = subprocess.Popen("{} devices".format(adb_exec_path, "devices"), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, errors = process.communicate()
    logger.debug("Adb get_devices output: {}".format(output))
    output_lines = output.split("\n")
    return output_lines > 1


def check_boot_complete(sdk_path):
    adb_exec_path = os.path.join(sdk_path, constants.PLATFORM_TOOLS_DIR, "adb")
    process = subprocess.Popen("{} {}".format(constants.CHECK_BOOT_ANIM_SCRIPT, adb_exec_path), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    logger.debug("Check boot animation output: {}.".format(output))
    return output.decode('utf-8').strip() == "stopped"


def verify_emulator_started(sdk_path, boot_delay, tries):
    try_count = 0
    boot_complete = check_boot_complete(sdk_path)
    while not boot_complete and try_count < tries:
        time.sleep(boot_delay)
        try_count += 1
        boot_complete = check_boot_complete(sdk_path)

    if not boot_complete and try_count == tries:
        return False

    return True


def start_avd(sdk_path, device_name, boot_delay, tries=10):
    logger.info("Booting device: {}.".format(device_name))
    subprocess.Popen("{} {} {}".format(constants.BOOT_STANDARD_EMU_SCRIPT, sdk_path, device_name),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    logger.info("Booting standard emulator: {}".format(device_name))

    emulator_started = verify_emulator_started(sdk_path, boot_delay, tries)
    if emulator_started:
        logger.info("Successfully started emulator: {}.".format(device_name))
        return True
    else:
        logger.info("Could not boot standard emulator: {}.".format(device_name))
        return False


def kill_avd(sdk_path):
    logger.info("Terminating emulator.")
    adb_exec_path = os.path.join(sdk_path, constants.PLATFORM_TOOLS_DIR, "adb")
    subprocess.call("{} {}".format(constants.KILL_STANDARD_EMU_SCRIPT, adb_exec_path), shell=True)


def start_genymotion(sdk_path, genymotion_path, device_name, boot_delay, tries=5):
    logger.info("Booting device: {}".format(device_name))
    player_exec_path = os.path.join(genymotion_path, "player")
    subprocess.Popen("{} {} {}".format(constants.BOOT_GENYMOTION_EMU_SCRIPT, player_exec_path, device_name),
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    logger.info("Booting genyotion emulator: {}".format(device_name))

    emulator_started = verify_emulator_started(sdk_path, boot_delay, tries)
    if emulator_started:
        logger.info("Successfully started emulator: {}".format(device_name))
        return True
    else:
        logger.info("Could not boot genymotion emulator: {}".format(device_name))
        return False


def kill_genymotion():
    subprocess.call(constants.KILL_GENYMOTION_EMU_SCRIPT, shell=True)
    logger.info("Successfully terminated emulator.")


if __name__ == '__main__':
    import json
    import logging.config
    if os.path.isfile("appiumatic.log"):
        os.remove("appiumatic.log")

    with open("logging.json") as logging_configuration_file:
        config = json.load(logging_configuration_file)

    logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)
    logger.info("Appiumatic logger configuration complete!")
    # print(check_boot_complete("/home/davidadamojr/Android/Sdk"))

    constants.BOOT_STANDARD_EMU_SCRIPT = "scripts/boot_standard_emulator.sh"
    constants.CHECK_BOOT_ANIM_SCRIPT = "scripts/check_boot_anim.sh"
    constants.KILL_STANDARD_EMU_SCRIPT = "scripts/kill_standard_emulator.sh"
    constants.BOOT_GENYMOTION_EMU_SCRIPT = "scripts/boot_genymotion_emulator.sh"
    constants.KILL_GENYMOTION_EMU_SCRIPT = "scripts/kill_genymotion_emulator.sh"
    constants.ADB_RESET_SCRIPT = "scripts/adb_reset.sh"
    reset_adb("/home/davidadamojr/Android/Sdk")
    # start_avd("/home/davidadamojr/Android/Sdk", "api19_0")
    # kill_avd("/home/davidadamojr/Android/Sdk")
    start_genymotion("/home/davidadamojr/Android/Sdk", "/home/davidadamojr/genymotion",
                     "3942e954-84c4-4766-8e4b-6901dfeebde8", tries=10)
    kill_genymotion()


