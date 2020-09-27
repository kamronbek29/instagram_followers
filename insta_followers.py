# coding=utf-8
import getpass
import asyncio
import os

from instagram_private_api import Client


async def login(username, password):  # authorize to account
    try:
        api = Client(username, password)
        print('[I] Login to "' + username + '" OK!')
        return api

    except Exception as err:
        print('[E] Login to ' + username + ' FAILED!\n ERROR: {}'.format(err))
        return


async def get_list_user_followers(session, user_id, next_max_id):
    kwargs = {}
    if next_max_id:
        kwargs['max_id'] = next_max_id
    followers_info = session.user_followers(user_id, rank_token=session.generate_uuid(), **kwargs)

    followers = followers_info['users']
    next_max_id = followers_info['next_max_id']

    list_username = []
    for profile in range(len(followers)):
        follower_username = followers[profile]['username']
        list_username.append('@{}'.format(follower_username))

    return list_username, next_max_id


async def save_list_username_to_file(user_to_get, list_username):
    file_name = '{}.txt'.format(user_to_get)
    joined_list_username = '\n'.join(list_username)

    if not os.path.exists(file_name):
        file_option = 'w'
    else:
        file_option = 'a'

    with open(file_name, file_option) as file_to_write:
        file_to_write.write(joined_list_username)


async def main(username, password, user_to_get):
    session = await login(username, password)

    user_res = session.username_info(user_to_get)
    user_id = user_res['user']['pk']

    next_max_id = None
    count = 0
    while True:
        list_username, next_max_id = await get_list_user_followers(session, user_id, next_max_id)
        await save_list_username_to_file(user_to_get, list_username)

        count += len(list_username)
        print('{0} usernames are saved'.format(count))


async def start():
    username = input('Please, put your username here: ')
    password = input('Please put your password here: ')
    user_to_get = input('Please, write username of who you want to get followers: ')

    await main(username, password, user_to_get)


if __name__ == '__main__':
    asyncio.run(start())
