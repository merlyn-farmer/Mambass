import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    @property
    def get_reg_variable(self):
        return self.config.get('Settings', 'reg_variable')

    @property
    def get_photos_dir(self):
        return self.config.get('Settings', 'photos_dir')

    @property
    def get_name_variation(self):
        return self.config.get('Settings', 'name_variation')

    @property
    def get_city(self):
        return self.config.get('Settings', 'geo')

    @property
    def get_group_id(self):
        try:
            return self.config.get('Settings', 'group_id')
        except configparser.NoOptionError:
            pass

    @property
    def get_change_account(self):
        return bool(self.config.get('Settings', 'change_account_settings'))

    @property
    def get_port(self):
        return self.config.get('Settings', 'Port')


config_data = Config()
