# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:08:24 2023

@author: DWalz
"""


import pandas as pd


df = pd.read_csv(r'C:\Users\DWalz\OneDrive - Universität St.Gallen\2_Staggered Board\Data\ccm total\export.csv')
FF_5 = pd.DataFrame([])

# Function to map SIC codes to FF_5 categories
def map_sic_to_ff5(sic_code):
    if 100 <= sic_code <= 999:
        return 1
    elif (2000 <= sic_code <= 2399) or (2700 <= sic_code <= 2749) or (3100 <= sic_code <= 3199) or (3940 <= sic_code <= 3989) or \
         (2500 <= sic_code <= 2519) or (2590 <= sic_code <= 2599) or (3630 <= sic_code <= 3659) or (3710 <= sic_code <= 3711) or \
         (3714 <= sic_code <= 3714) or (3716 <= sic_code <= 3716) or (3750 <= sic_code <= 3751) or (3792 <= sic_code <= 3792) or \
         (3990 <= sic_code <= 3999) or (5000 <= sic_code <= 5999) or (7200 <= sic_code <= 7299) or (7600 <= sic_code <= 7699) or \
         (2770 <= sic_code <= 2799) or (3900 <= sic_code <= 3939):
        return 1
    elif (2520 <= sic_code <= 2589) or (2600 <= sic_code <= 2699) or (2750 <= sic_code <= 2769) or (2800 <= sic_code <= 2829) or \
         (2840 <= sic_code <= 2899) or (3000 <= sic_code <= 3099) or (3200 <= sic_code <= 3569) or (3580 <= sic_code <= 3621) or \
         (3623 <= sic_code <= 3629) or (3700 <= sic_code <= 3709) or (3712 <= sic_code <= 3713) or (3715 <= sic_code <= 3715) or \
         (3717 <= sic_code <= 3749) or (3752 <= sic_code <= 3791) or (3793 <= sic_code <= 3799) or (3860 <= sic_code <= 3899) or \
         (1200 <= sic_code <= 1399) or (2900 <= sic_code <= 2999) or (4900 <= sic_code <= 4949):
        return 2
    elif (3570 <= sic_code <= 3579) or (3622 <= sic_code <= 3622) or (3660 <= sic_code <= 3692) or (3694 <= sic_code <= 3699) or \
         (3810 <= sic_code <= 3839) or (7370 <= sic_code <= 7372) or (7373 <= sic_code <= 7373) or (7374 <= sic_code <= 7374) or \
         (7375 <= sic_code <= 7375) or (7376 <= sic_code <= 7376) or (7377 <= sic_code <= 7377) or (7378 <= sic_code <= 7378) or \
         (7379 <= sic_code <= 7379) or (7391 <= sic_code <= 7391) or (8730 <= sic_code <= 8734) or (4800 <= sic_code <= 4899):
        return 3
    elif (2830 <= sic_code <= 2839) or (3693 <= sic_code <= 3693) or (3840 <= sic_code <= 3859) or (8000 <= sic_code <= 8099):
        return 4
    else:
        return 5

# Apply the function to create the FF_5 column
FF_5['FF_5'] = df['sic'].apply(map_sic_to_ff5)

FF_5["sic"] = df["sic"]


FF_5 = FF_5.drop_duplicates()
FF_5.to_excel(r'C:\Users\DWalz\OneDrive - Universität St.Gallen\2_Staggered Board\Data\FF5\FF5.xlsx')
