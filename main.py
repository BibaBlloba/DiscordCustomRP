import time

from pypresence import Presence
from pypresence.types import ActivityType

from config import settings


def main(loop: bool = False):
    client_id = settings.APP_ID
    RPC = Presence(client_id)

    base_params = {
        'details': 'Пинаю хуище',
        'state': '¯\_(ツ)_/¯',
        'start': int(69.0),
        'large_image': 'nyarch',
        'large_text': 'ദ്ദി( • ᴗ - ) ✧',
        'buttons': [
            {
                'label': 'GitHub',
                'url': 'https://youtu.be/06t4AUshIg4?si=7S5Gfw_XQbxMZ3nh',
            }
        ],
    }

    try:
        RPC.connect()
        print('Running...')

        if loop:
            activity_types = [ActivityType.COMPETING, ActivityType.WATCHING]
            while True:
                for activity_type in activity_types:
                    RPC.update(**base_params, activity_type=activity_type)
                    time.sleep(5)
        else:
            RPC.update(**base_params, activity_type=ActivityType.COMPETING)

    except Exception as e:
        print(f'Exception: {e}')
    finally:
        RPC.close()
        print('Connection closed.')


if __name__ == '__main__':
    main(loop=True)
