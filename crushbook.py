import csv

from data_downloader import DataDownloader
from statistical_prediction import StatisticalPrediction
from facebook import GraphAPIError

def pullData():
    access_token = open("token.xd", "r").read().strip()
    data_downloader = DataDownloader(access_token)

    data_downloader.select_group()
    
    print("Hit Ctrl-C to stop downloading.")
    try:
        data_downloader.process_feed()
    except KeyboardInterrupt:
        print(" Stopped downloading.")
    except GraphAPIError:
        print(" Graph Api Error")

    react_data = data_downloader.react_dict
    user_data = data_downloader.users_dict

    return (react_data, user_data)

def main():
    output = open('data.csv', 'w')
    outputwriter = csv.writer(output)
    reacts, users = pullData()
    print(reacts)
    stats = StatisticalPrediction(reacts)

    for receiver in reacts:
        for giver in reacts:
            if stats.actual(receiver, giver) > 5:
                print(users.get(receiver)["name"],
                  users.get(giver)["name"],
                  stats.compare(receiver, giver))
                outputwriter.writerow([users.get(receiver)["name"],
                  users.get(giver)["name"],
                  stats.compare(receiver, giver)])

if __name__ == "__main__":
    main()