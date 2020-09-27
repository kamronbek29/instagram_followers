# Instagram followers downloader
  Python script that saves all instagram user followers' username to a file

## Login and password is required
   In order to make successful request to user followers list, you need to authorize

## Requirements

   * aiohttp
   * instagram_private_api

## Install

   Clone repository

   ``git clone https://github.com/kamronbek29/instagram_followers.git``

   Install aiohttp using pip:

   ``pip install aiohttp``

   Install instagram_private_api using pip:

   ``pip install git+https://git@github.com/ping/instagram_private_api.git@1.6.0``

## Usage

   Run the script

   ``python3.7 insta_followers.py``

   Put your username, password and username with followers
   
   ```python

   Please, put your username here: YOUR_USERNAME
   Please put your password here: YOUR_PASSWORD
   Please, write username of who you want to get followers: USERNAME_WITH_FOLLOWERS

   ```

   Then script starts working and will be saved as username.txt