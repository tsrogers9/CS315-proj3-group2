## Author: Caroline Jung
## Input: each file in `output_male/` and `output_female/`
## Output: `compiled_data/female.csv` and `compiled_data/male.csv`

import pandas as pd
import os
import json
import re


def clean_description(description):
    """
    Helper function, takes video description and splits into words, removes punctuation, emojis and stop words.
    """
    if pd.isna(description):  
        return []
    description = re.sub(r'\d+', '', description) # remove numbers from the text
    words = description.split() # split the description into words
    cleaned_words = [re.sub(r'[^\w\s]', '', word).lower() for word in words] # remove punctuation and emojis, make everything lowercase
    cleaned_words = [word for word in cleaned_words if word] # remove empty strings
    return cleaned_words

def combine_data(gender):
    if gender=="M":
        filepath = "output_male/"
        name = "male"
    elif gender=="F":
        filepath = "output_female/"
        name = "female"
    else:
        print("Not a valid input.")
    files = os.listdir(filepath)

    all_description, all_ids, all_comments = [], [], []
    for file in files:
        with open(filepath + file, 'r') as f:
            account = json.load(f)
        f.close()

        for video in account:
            vid_desc = ""
            try: 
                for parts in video["description"]:
                    vid_desc += parts.lower()
                all_description.append(vid_desc)
                all_ids.append(video["id"])
                all_comments.append(video["comments"])
            except:
                pass

    cleaned = [clean_description(desc) for desc in all_description]
    data = pd.DataFrame()
    data["video_id"] = all_ids
    data["description_string"] = all_description
    data["description_list"] = cleaned
    data["comments"] = all_comments

    data.to_csv(f"compiled_data/{name}.csv", index=False)
    return data

combine_data("M")
combine_data("F")
