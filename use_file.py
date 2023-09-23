import requests

# url = "https://parsinger.ru/video_downloads/"
# response = requests.get(url=url, stream=True)
# with open("file.mp4", "wb") as video:
#     video.write(response.content)


url = "https://parsinger.ru/video_downloads/"
response = requests.get(url=url, stream=True)
with open("file.3gp", "wb") as video:
    for z in response.iter_lines(chunk_size=110000):
        video.write(z)
