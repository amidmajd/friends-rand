import os
import sys
import re
import random


friends_base_dir = os.path.abspath("/media/amid/AmiD/Video/Friends")
print(friends_base_dir)
ignore_phrases = ["other", 'srt']
player_command = "vlc"

friends_list = []
for root, dirs, files in os.walk(friends_base_dir):
    for name in files:
        abs_file_path = os.path.join(root, name)
        if re.findall(pattern="|".join(ignore_phrases), string=abs_file_path) == []:
            # print(abs_file_path)
            friends_list.append(abs_file_path)

random.shuffle(friends_list)
# print(friends_list)
os.system("{} '{}'".format(player_command, friends_list[0]))
