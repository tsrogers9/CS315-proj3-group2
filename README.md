# 315 Project 3

By Caroline Jung, Sandy Liu, Josie Ramirez, Tayae Rogers

## prep
1. activate your virtual environment before running anything
2. cd into the directory 1-data_collection
2. All the urls for each profile is under the raw_data folder 

## how to run the comment scraper
1. go into VideoScraper.py
2. go to main, change the account name to what you are scraping
3. run the scraper and manually log in (sorry I wasn't able to bypass it with Eni's code)
4. leave it there until it's done scraping

Note that the webdriver would constantly bring you back to the chrome browser interface, so you 
probably want to not use your computer while running the code

Female Account assignment:
* Sandy: aoc, ilhanmn, repwilson, sheilaforhouston,
* Caroline: kirstengillibrand, nikemawilliams, rashidatlaib, teampattymurray
* Tayae: repchrissyhoulahan, repkatieporter, repstansbury
* Josie: reppressley, repshontelbrown, repsummerlee
* Note: congresswomanjayapal is empty

Male Account Assignment:
* Sandy: 
corybooker
johnfetterman
jon
bernie
kevinmullinforcongress
congressmancardenas
added from Tayae's: 
stevenahorsford
billpascrell
* Caroline: 
adamschiffca
repmarktakano
robertgarcia
repmaxwellfrost
troyc4congress
repdeanphillips
added from Tayae's: 
repbowman
wileynickel
* Tayae: (laptop broke)

* Josie: 
jeffjacksonnc
greglandsmanoh
colinallredtx
repcasar
repres.gerryconnolly
repmarkpocan

## notable files in 1-data_collection folder
* New TikTok Scraping.ipynb -- Collects video IDs for videos on a given user's page (this was run on each politician's page)
* VideoScraper.py -- Collects metadata for each video in JSON with video links (this was run on every file in `raw_male/` and `raw_female/`)
* compile_data.py -- Compiles data across from all files with video metadata into files gender (this was run on every file in `output_male/` and `output_female/`)

## notable files in 2-analysis folder
files in types-of-video-content:
* gpt_categorization.ipynb -- Feeds video descriptions to GPT to categorize them (this was run on `M_all_vid_descriptions_2024_04_28.csv` and `F_all_vid_descriptions_2024_04_28.csv`)
* gpt_categorization_analysis.ipynb -- Visualizes GPT categorization (this was run on `female_categories.csv` and `male_categories_may2.csv`)
* gpt_manual_visualization.ipynb -- Visualizes the results of our manual check of GPT categorization

files in stance-detection-comments:
* stance_detection.ipynb -- Feeds comments to Perspective API to get mean attribute scores for comments on each video (this was run on every file in `output_male/` and `output_female/`)
* stance_detection_analysis.ipynb -- Visualizes and models attribute scores by demographic characteristics (this was run on `female_data_scores.json` and `male_data_scores.json`)