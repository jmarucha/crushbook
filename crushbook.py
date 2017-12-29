import facebook
from data_downloader import DataDownloader

access_token = open("token.xd", "r").read().strip()


data_downloader = DataDownloader(access_token)

data_downloader.select_group()
# data_downloader.group_id = "1746463952328227"

data_downloader.process_feed()

print(data_downloader.react_dict)
