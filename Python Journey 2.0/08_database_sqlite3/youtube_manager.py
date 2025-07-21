import sqlite3

con = sqlite3.connect('youtube_videos.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS VIDEOS (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_videos():
    cur.execute("SELECT * FROM videos")
    videos_list = cur.fetchall()
    if not videos_list:
        print("Empty list, Please add videos")
    for row in videos_list:
        print(row)

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\n Youtube Manager | choose and option")
        print("1. List all youtube videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit Loop \n")
        choice = input("Enter your choice: ")

        # print(videos)

        if choice == '1':
            print('-' * 80)
            list_videos()
            print('_' * 80)
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '5' or 'stop' or 'break':
            break
        else:
            print("Invalid choice")

    con.close()


if __name__ == "__main__":
    main()