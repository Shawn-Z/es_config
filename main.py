import config_settings


if __name__ == '__main__':
    config_json = config_settings.get_file_configs()

    config_settings.get_config(config_json)
