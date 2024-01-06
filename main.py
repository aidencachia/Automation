from PIL import Image, ImageDraw, ImageFont
import os
import csv
from instaloader.instaloader import Instaloader
import shutil

profileMask = Image.open('PhotoEditingHelp/Mask.png')
profileMask = profileMask.convert('L')
ig = Instaloader()

with open(r"../credentials.txt", 'r') as file:
    username = file.readline().replace('\n', '')
    password = file.readline().replace('\n', '')

ig.login(username, password)

def is_an_image(fpath): 
    return os.path.splitext(fpath)[-1] in ('.png',)


with open(r"../workingsheet.csv", 'r', newline='') as csv_file:
    table = list(csv.reader(csv_file, delimiter=',', quotechar='|'))
    beginning_row = 0
    ending_row = 0

    month = input("Enter the month number: ")

    for i, row in enumerate(table):
        if row[1] == month:
            ending_row = i
            if beginning_row == 0:
                beginning_row = i
    

    for i in range(beginning_row, ending_row):
        name  = table[i][0]

        print(f'{i}: {name}')

        if(table[i][2] != ''):
            ig.download_profile(table[i][2], profile_pic_only=True)

            frame = Image.open('PhotoEditingHelp/Frame.png')
            
            folder_path = f"{table[i][2]}"
            only_image_name = next(file for file in os.listdir(folder_path) if os.path.splitext(file)[1].lower()==".jpg")
            profile = Image.open(f"{folder_path}/{only_image_name}")

            profile = profile.resize(profileMask.size)
            frame.paste(profile,(74,610), profileMask)

            message = f'{name.upper()}!'
            draw = ImageDraw.Draw(frame)
            font = ImageFont.truetype("BebasNeue-Regular.ttf", size = 200)
            _, _, w, _ = draw.textbbox((0, 0), message, font=font)
            draw.text(((frame.size[0]-w)//2, 1300), message, font=font, fill = (33, 66, 77))

            frame = frame.convert("RGB")
            frame.save(f'final/{i} {name}.jpg')
            shutil.rmtree(folder_path)
        else:
            print(f'No instagram for {name}. DO POSTER MANUALLY')