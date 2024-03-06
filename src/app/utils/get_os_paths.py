import os
import sys

def get_app_path(input):
    if sys.platform.startswith('win'):
        # Windows platform
        app_path = os.path.join(os.getenv('LOCALAPPDATA'), 'BotBattleOfSea', input)
    elif sys.platform.startswith('darwin'):
        # macOS platform
        #app_path = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'RealEstator', input)
        config_folder = os.path.join('/Library', 'Application Support', 'BotBattleOfSea')
        app_path = os.path.join(config_folder, input)
    else:
        # Linux and other platforms
        app_path = os.path.join(os.getenv('XDG_CONFIG_HOME', os.path.expanduser('~/.config')), 'BotBattleOfSea', input)

    return app_path