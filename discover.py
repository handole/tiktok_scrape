from TikTokApi import TikTokApi

api = TikTokApi()

count = 1

tiktoks = api.byUsername('americanredcross', count=count)

for tiktok in tiktoks:
    print(tiktok)