from fastapi import FastAPI
from TikTokApi import TikTokApi
import pandas as pd
import datetime
import psycopg2
import json

app = FastAPI()

api = TikTokApi()

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

@app.get("/")
async def test():
    return {"test": "test api async"}


@app.get("/tiktok/posts")
async def posts():
    hashtag = api.byHashtag(hashtag='omnibuslaw', count=10)
    hashtag = (simple_dict(v) for v in hashtag)
    
    return {"posts": hashtag}


