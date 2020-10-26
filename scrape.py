from threading import Thread
from multiprocessing import Process, Queue
import asyncio
from TikTokApi import TikTokApi
import pandas as pd
import datetime
import psycopg2
import json

api = TikTokApi()

n_videos = 10
hashtag = input("Masukan hashtag / keyword yang akan di scraping : ")

def simple_dict(tiktok_dict):
    to_return = {}
    # to_return['user_name'] = tiktok_dict['authorId']
    to_return['user_id'] = tiktok_dict['itemInfos']['authorId']
    to_return['user_name'] = tiktok_dict['authorInfos']['uniqueId']
    to_return['video_id'] = tiktok_dict['itemInfos']['id']
    to_return['video_desc'] = tiktok_dict['itemInfos']['text']
    to_return['create_time'] = datetime.datetime.fromtimestamp(int(tiktok_dict['itemInfos']['createTime']))
    to_return['video_length'] = tiktok_dict['itemInfos']['video']['videoMeta']
    to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=id'.format(to_return['user_name'], to_return['video_id'])
    to_return['n_likes'] = tiktok_dict['itemInfos']['diggCount']
    to_return['n_shares'] = tiktok_dict['itemInfos']['shareCount']
    to_return['n_comments'] = tiktok_dict['itemInfos']['commentCount']
    to_return['n_plays'] = tiktok_dict['itemInfos']['playCount']
    return to_return

tiktoks = api.byHashtag(hashtag, count=n_videos)
tiktoks = (simple_dict(v) for v in tiktoks)

# json_arr = []
# for tik in tiktoks:
#     user = tk['user_name']
#     profil = api.byUsername(user, count=1)
#     json_arr.append(profil)
#     profil_df = pd.DataFrame(json_arr)
#     profil_df.to_csv('profils/22okt_1445{}.csv'.format(hashtag), index=False)

def posts_hashtag():
    # hashtag = input("Masukan hashtag / keyword yang akan di scraping : ")
    # n_videos = input("masukan jumlah scrapingnya: ")
    
    
    # print(tiktoks)
    tag_df = pd.DataFrame(tiktoks)
    # now = datetime.datetime.now()
    tag_df.to_csv('posts/23okt_1315_{}.csv'.format(hashtag), index=False)
    # with open('posts/21okt_1553_{}.json'.format(hashtag), 'w') as f:
    #     json.dump(tiktoks, f, indent=2)
    return tag_df

def get_profil():
    # await posts_hashtag()
    json_arr = []
    for tik in tiktoks:
        user = tik['user_name']
        profil = api.byUsername(user, count=1)
        json_arr.append(profil)
        profil_df = pd.DataFrame(json_arr)
        profil_df.to_csv('profils/23okt_1315_{}.csv'.format(hashtag), index=False)
        with open('profils/23okt_1315_from_{}.json'.format(hashtag), 'w') as f:
            json.dump(json_arr, f, indent=2)
    return json_arr

# posts_hashtag()
# get_profil()
# tag_df = pd.DataFrame(tiktoks)
# tag_df.to_csv('posts/22okt_1620{}.csv'.format(hashtag), index=False)

def main():
    posts_hashtag()
    get_profil()

if __name__ == "__main__":
    main()
    # hashtag = input("Masukan hashtag / keyword yang akan di scraping : ")
    # n_videos = input("masukan jumlah scrapingnya: ")
    # posts_hashtag()
    # get_profil()
    
    # asyncio.run(get_profil())
    # await posts_hashtag()
    
    # Thread(target=posts_hashtag).start()
    # Thread(target=get_profil).start()
    # posts_hashtag()
    # get_profil()
    # posts_hashtag()


# for tik in tiktoks:
#     # print(tik['user_name'])
#     user = tik['user_name']
#     profil = api.byUsername(user, count=1)
#     # profil = (get_user(v) for v in profil)
#     # print(profil)
#     json_arr.append(profil)
#     with open('profils/21okt_1012_profil_from_{}.json'.format(hashtag), 'w') as f:
#         json.dump(json_arr, f, indent=2)


# def get_user(tiktok_dict):
#     to_return = {}
#     to_return['user_id'] = tiktok_dict['author']['id']
#     to_return['user_name'] = tiktok_dict['author']['uniqueId']
#     to_return['signature'] = tiktok_dict['author']['signature']
#     to_return['following'] = tiktok_dict['authorStats']['followingCount']
#     to_return['follower'] = tiktok_dict['authorStats']['followerCount']
#     to_return['heart'] = tiktok_dict['authorStats']['heartCount']
#     to_return['video'] = tiktok_dict['authorStats']['videoCount']
#     to_return['digg'] = tiktok_dict['authorStats']['diggCount']
#     return to_return 