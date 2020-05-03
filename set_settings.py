from configparser import ConfigParser

path_to_settings = "settings.ini"

def get_config(path = path_to_settings):
    """
    Возвращает объект с файлом конфига
    """
    config = ConfigParser()
    config.read(path)

    return config

def get_setting(section, setting, path = path_to_settings):
    """
    Возвращает значение из конфига
    """
    config = get_config()

    value = config.get(section, setting)

    return value

def update_setting(section, setting, value, path = path_to_settings):
    """
    Обновляет значение из конфига
    """
    config = get_config()

    if not config.has_section(section):
        config.add_section(section)
    config.set(section, setting, value)

    with open(path, "w") as config_file:
        config.write(config_file)

def get_key(section, setting, delimiter = " ", path = path_to_settings):
    """
    Возвращает кнопку
    """
    first_step = get_setting(section, setting)
    second_step = first_step[:first_step.find(delimiter)]
    third_step = int(second_step)
    return third_step