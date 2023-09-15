# coding: utf-8
import feedparser
import requests
import os

f = open("YT_to_WP.txt", "r", encoding="utf-8")
old_up = f.readline().replace("\n", "")
f.close()
old_up = 0

entries = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UC33HnC11kHWjIS2IxFhqa4Q')['entries']
i = 0

feed_size = len(entries)

# ブログのURL
blog_url = "https://blossomsarchive.com/"

# WordPressのユーザー名
wordpress_user = os.environ.get("WORDPRESS_USER")
api_user = wordpress_user

# アプリケーションパスワード
wordpress_api_password = os.environ.get("WORDPRESS_API_PASSWORD")
api_password = wordpress_api_password

for i in range(feed_size):
    now_up = entries[i]["updated"]
    if now_up == old_up:
        new_up = entries[0]["updated"]
        g = open("nvnb-ipa.txt", "w", encoding="utf-8")
        g.write(new_up)
        g.close()
        break
    else:
        title = entries[i]['title']
        page_url = entries[i]['link']
        # 送信する記事データ
        post_data = {
            'title': "動画:"+title,
            'content': page_url,
            'categories': '17',
            # 'status': 'publish',  # draft=下書き、publish=公開　省略時はdraftになる
        }
        # Post APIのURL
        post_api_url = f'{blog_url}/wp-json/wp/v2/posts'

        # 記事投稿リクエスト
        response = requests.post(post_api_url, json=post_data, auth=(api_user, api_password))

    print(title+"\n"+page_url)
    i = i+1
    
new_up = entries[0]["updated"]
print(new_up)
g = open("YT_to_WP.txt", "w", encoding="utf-8")
g.write(new_up)
g.close()
