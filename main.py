import time

from pypresence import Presence

from config import settings


def main():
    client_id = settings.APP_ID
    RPC = Presence(client_id)

    try:
        RPC.connect()
        RPC.update(
            details='Пинаю хуище',
            state='¯\_(ツ)_/¯',
            start=int(69.0),
            large_image='nyarch',
            large_text='ദ്ദി( • ᴗ - ) ✧',
            buttons=[
                {
                    'label': 'GitHub',
                    'url': 'https://youtu.be/06t4AUshIg4?si=7S5Gfw_XQbxMZ3nh',
                }
            ],
        )
        print('Running...')
        while True:
            time.sleep(15)

    except Exception as e:
        print(f'Exception: {e}')
    finally:
        RPC.close()
        print('Connection closed.')


if __name__ == '__main__':
    main()
