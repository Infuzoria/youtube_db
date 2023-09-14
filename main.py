import os
import utils
from config import config


def main():
    api_key = os.getenv('YOUTUBE_API_KEY')
    channel_ids = [
        'UCDaIW2zPRWhzQ9Hj7a0QP1w',  # Руслан Усачев
        'UC2Ru64PHqW4FxoP0xhQRvJg',  # Топлес
    ]
    params = config()

    data = utils.get_youtube_data(api_key, channel_ids)
    utils.create_database('youtube', params)
    utils.save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
