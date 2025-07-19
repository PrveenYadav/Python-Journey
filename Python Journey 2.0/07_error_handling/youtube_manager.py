# YouTube Manager 
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) # After reading data it will convert into json and return it
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file) #dump means write

def list_all_videos(videos):
    print('-' * 80)
    #enumerate gives the index, start from 1
    videos_list = enumerate(videos, start=1) 
    for index, video in videos_list:
        print(f"{index}. Name: {video['name']} | Duration: {video['time']} ")
    print('-' * 80)

def add_video(videos):
    name = input("Enter videos name: ")
    time = input("Enter videos time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("Invalid video index")


# main function code will start running from here
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose and option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit a youtube video \n")
        choice = input("Enter your choice: ")

        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5' | '0' | 'stop':
                break
            case _:
                print("Invalid Choice")

if __name__== "__main__":
    main()