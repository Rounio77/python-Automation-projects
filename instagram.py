import random
from instagrapi import Client
with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()
    

client = Client()
client.login(username, password)

hashtag = "movies"
comments = ["interesting post", "awesome", "i love this", "cool", "nice"]
medias = client.hashtag_medias_recent(hashtag, 70)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"liked post NO. {i+1} of hashtag {hashtag}")
    if i%1 == 0:
        client.user_follow(media.user.pk)
        print(f"follow user {media.user.username}")
        client.media_comment(media.id, "ausome post")
        comment = random.choice(comments)     
        print(f"commented {comment} under post no {i+1}")      
        
