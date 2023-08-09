from requests_db import Manager

if __name__ == "__main__":
    manager = Manager()
    news_list1 = [
        (1, 1, '2023-08-04', 'News 1 content'),
        (1, 2, '2023-08-04', 'News 2 content'),
        (1, 3, '2023-08-04', 'News 3 content'),
        (1, 4, '2023-08-04', 'News 4 content'),
    ]

    # manager.subscribe_user_to_channel(2, 4)
    # manager.unsubscribe_user_from_channel(1, 4)

    # manager.add_new_news(1, 1, '2023-08-08', 'Privet narod')
    # manager.add_new_many_news(news_list1)
    # manager.add_new_user('Anton')
    # manager.add_new_channel('Channel2', 'link2')

    manager.check_table('users')
    manager.check_table('channels')
    manager.check_table('subscriptions')
    manager.check_table('news')

    manager.close()
