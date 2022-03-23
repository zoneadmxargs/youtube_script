from apiclient.discovery import build
YOUTUBE_API_KEY = 'Your API KEY'
CHANNEL_ID = 'UCZikuEIssIzv0fdkVEH7Djg'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

data = []
pageToken = ""
while True:
  res = youtube.search().list(
    part = "snippet",
    channelId = CHANNEL_ID,
    maxResults = 50,
    order = "date",
    pageToken=pageToken if pageToken != "" else ""
  ).execute()
  v = res.get('items', [])
  if v:
    data.extend(v)
  pageToken = res.get('nextPageToken')
  if not pageToken:
    break

for item in data:
  print(item['snippet']['title'])
