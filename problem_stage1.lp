\* NFL_DFS_Optimization *\
Maximize
OBJ: 16.47 C.J._Stroud_QB_37040965 + 8.18 Calvin_Austin_III_FLEX_37041042
 + 8.18 Calvin_Austin_III_WR_37041042 + 7.35 Chiefs_DST_37041164
 + 8.93 Dalton_Schultz_FLEX_37041120 + 8.93 Dalton_Schultz_TE_37041120
 + 10.63 DeAndre_Hopkins_FLEX_37041032 + 10.63 DeAndre_Hopkins_WR_37041032
 + 17 Derrick_Henry_FLEX_37040976 + 17 Derrick_Henry_RB_37040976
 + 4.03 Hollywood_Brown_FLEX_37041084 + 4.03 Hollywood_Brown_WR_37041084
 + 6.95 Isaiah_Likely_FLEX_37041122 + 6.95 Isaiah_Likely_TE_37041122
 + 10.84 Isiah_Pacheco_FLEX_37040980 + 10.84 Isiah_Pacheco_RB_37040980
 + 10.05 Jaylen_Warren_FLEX_37040984 + 10.05 Jaylen_Warren_RB_37040984
 + 18.73 Joe_Mixon_FLEX_37040978 + 18.73 Joe_Mixon_RB_37040978
 + 7.57 Justice_Hill_FLEX_37040988 + 7.57 Justice_Hill_RB_37040988
 + 8.31 Kareem_Hunt_FLEX_37040986 + 8.31 Kareem_Hunt_RB_37040986
 + 21.67 Lamar_Jackson_QB_37040963 + 8.78 Mark_Andrews_FLEX_37041116
 + 8.78 Mark_Andrews_TE_37041116 + 4.93 Mike_Williams_FLEX_37041044
 + 4.93 Mike_Williams_WR_37041044 + 12.6 Najee_Harris_FLEX_37040982
 + 12.6 Najee_Harris_RB_37040982 + 18.2 Nico_Collins_FLEX_37041026
 + 18.2 Nico_Collins_WR_37041026 + 6.83 Noah_Gray_FLEX_37041124
 + 6.83 Noah_Gray_TE_37041124 + 9.86 Pat_Freiermuth_FLEX_37041118
 + 9.86 Pat_Freiermuth_TE_37041118 + 18.34 Patrick_Mahomes_QB_37040964
 + 7.7 Rashod_Bateman_FLEX_37041038 + 7.7 Rashod_Bateman_WR_37041038
 + 7.68 Ravens_DST_37041162 + 4.07 Robert_Woods_FLEX_37041100
 + 4.07 Robert_Woods_WR_37041100 + 14.67 Russell_Wilson_QB_37040966
 + 5.06 Steelers_DST_37041165 + 10.42 Tank_Dell_FLEX_37041034
 + 10.42 Tank_Dell_WR_37041034 + 6.15 Texans_DST_37041163
 + 13.87 Travis_Kelce_FLEX_37041114 + 13.87 Travis_Kelce_TE_37041114
 + 4.9 Van_Jefferson_FLEX_37041052 + 4.9 Van_Jefferson_WR_37041052
 + 10.27 Xavier_Worthy_FLEX_37041036 + 10.27 Xavier_Worthy_WR_37041036
 + 14.48 Zay_Flowers_FLEX_37041030 + 14.48 Zay_Flowers_WR_37041030
Subject To
Global_Team_BAL: Derrick_Henry_FLEX_37040976 + Derrick_Henry_RB_37040976
 + Isaiah_Likely_FLEX_37041122 + Isaiah_Likely_TE_37041122
 + Justice_Hill_FLEX_37040988 + Justice_Hill_RB_37040988
 + Lamar_Jackson_QB_37040963 + Mark_Andrews_FLEX_37041116
 + Mark_Andrews_TE_37041116 + Rashod_Bateman_FLEX_37041038
 + Rashod_Bateman_WR_37041038 + Ravens_DST_37041162
 + Zay_Flowers_FLEX_37041030 + Zay_Flowers_WR_37041030 <= 4
Global_Team_HOU: C.J._Stroud_QB_37040965 + Dalton_Schultz_FLEX_37041120
 + Dalton_Schultz_TE_37041120 + Joe_Mixon_FLEX_37040978
 + Joe_Mixon_RB_37040978 + Nico_Collins_FLEX_37041026
 + Nico_Collins_WR_37041026 + Robert_Woods_FLEX_37041100
 + Robert_Woods_WR_37041100 + Tank_Dell_FLEX_37041034 + Tank_Dell_WR_37041034
 + Texans_DST_37041163 <= 4
Global_Team_KC: Chiefs_DST_37041164 + DeAndre_Hopkins_FLEX_37041032
 + DeAndre_Hopkins_WR_37041032 + Hollywood_Brown_FLEX_37041084
 + Hollywood_Brown_WR_37041084 + Isiah_Pacheco_FLEX_37040980
 + Isiah_Pacheco_RB_37040980 + Kareem_Hunt_FLEX_37040986
 + Kareem_Hunt_RB_37040986 + Noah_Gray_FLEX_37041124 + Noah_Gray_TE_37041124
 + Patrick_Mahomes_QB_37040964 + Travis_Kelce_FLEX_37041114
 + Travis_Kelce_TE_37041114 + Xavier_Worthy_FLEX_37041036
 + Xavier_Worthy_WR_37041036 <= 4
Global_Team_PIT: Calvin_Austin_III_FLEX_37041042
 + Calvin_Austin_III_WR_37041042 + Jaylen_Warren_FLEX_37040984
 + Jaylen_Warren_RB_37040984 + Mike_Williams_FLEX_37041044
 + Mike_Williams_WR_37041044 + Najee_Harris_FLEX_37040982
 + Najee_Harris_RB_37040982 + Pat_Freiermuth_FLEX_37041118
 + Pat_Freiermuth_TE_37041118 + Russell_Wilson_QB_37040966
 + Steelers_DST_37041165 + Van_Jefferson_FLEX_37041052
 + Van_Jefferson_WR_37041052 <= 4
Max_Salary: 6000 C.J._Stroud_QB_37040965
 + 3800 Calvin_Austin_III_FLEX_37041042 + 3800 Calvin_Austin_III_WR_37041042
 + 2700 Chiefs_DST_37041164 + 3400 Dalton_Schultz_FLEX_37041120
 + 3400 Dalton_Schultz_TE_37041120 + 5300 DeAndre_Hopkins_FLEX_37041032
 + 5300 DeAndre_Hopkins_WR_37041032 + 8000 Derrick_Henry_FLEX_37040976
 + 8000 Derrick_Henry_RB_37040976 + 3000 Hollywood_Brown_FLEX_37041084
 + 3000 Hollywood_Brown_WR_37041084 + 3300 Isaiah_Likely_FLEX_37041122
 + 3300 Isaiah_Likely_TE_37041122 + 6000 Isiah_Pacheco_FLEX_37040980
 + 6000 Isiah_Pacheco_RB_37040980 + 5200 Jaylen_Warren_FLEX_37040984
 + 5200 Jaylen_Warren_RB_37040984 + 7800 Joe_Mixon_FLEX_37040978
 + 7800 Joe_Mixon_RB_37040978 + 4800 Justice_Hill_FLEX_37040988
 + 4800 Justice_Hill_RB_37040988 + 5000 Kareem_Hunt_FLEX_37040986
 + 5000 Kareem_Hunt_RB_37040986 + 8200 Lamar_Jackson_QB_37040963
 + 4300 Mark_Andrews_FLEX_37041116 + 4300 Mark_Andrews_TE_37041116
 + 3700 Mike_Williams_FLEX_37041044 + 3700 Mike_Williams_WR_37041044
 + 5700 Najee_Harris_FLEX_37040982 + 5700 Najee_Harris_RB_37040982
 + 8100 Nico_Collins_FLEX_37041026 + 8100 Nico_Collins_WR_37041026
 + 3200 Noah_Gray_FLEX_37041124 + 3200 Noah_Gray_TE_37041124
 + 3900 Pat_Freiermuth_FLEX_37041118 + 3900 Pat_Freiermuth_TE_37041118
 + 6400 Patrick_Mahomes_QB_37040964 + 4900 Rashod_Bateman_FLEX_37041038
 + 4900 Rashod_Bateman_WR_37041038 + 3300 Ravens_DST_37041162
 + 3000 Robert_Woods_FLEX_37041100 + 3000 Robert_Woods_WR_37041100
 + 5700 Russell_Wilson_QB_37040966 + 2500 Steelers_DST_37041165
 + 5100 Tank_Dell_FLEX_37041034 + 5100 Tank_Dell_WR_37041034
 + 3100 Texans_DST_37041163 + 5600 Travis_Kelce_FLEX_37041114
 + 5600 Travis_Kelce_TE_37041114 + 3300 Van_Jefferson_FLEX_37041052
 + 3300 Van_Jefferson_WR_37041052 + 5000 Xavier_Worthy_FLEX_37041036
 + 5000 Xavier_Worthy_WR_37041036 + 5900 Zay_Flowers_FLEX_37041030
 + 5900 Zay_Flowers_WR_37041030 <= 50000
Min_Salary: 6000 C.J._Stroud_QB_37040965
 + 3800 Calvin_Austin_III_FLEX_37041042 + 3800 Calvin_Austin_III_WR_37041042
 + 2700 Chiefs_DST_37041164 + 3400 Dalton_Schultz_FLEX_37041120
 + 3400 Dalton_Schultz_TE_37041120 + 5300 DeAndre_Hopkins_FLEX_37041032
 + 5300 DeAndre_Hopkins_WR_37041032 + 8000 Derrick_Henry_FLEX_37040976
 + 8000 Derrick_Henry_RB_37040976 + 3000 Hollywood_Brown_FLEX_37041084
 + 3000 Hollywood_Brown_WR_37041084 + 3300 Isaiah_Likely_FLEX_37041122
 + 3300 Isaiah_Likely_TE_37041122 + 6000 Isiah_Pacheco_FLEX_37040980
 + 6000 Isiah_Pacheco_RB_37040980 + 5200 Jaylen_Warren_FLEX_37040984
 + 5200 Jaylen_Warren_RB_37040984 + 7800 Joe_Mixon_FLEX_37040978
 + 7800 Joe_Mixon_RB_37040978 + 4800 Justice_Hill_FLEX_37040988
 + 4800 Justice_Hill_RB_37040988 + 5000 Kareem_Hunt_FLEX_37040986
 + 5000 Kareem_Hunt_RB_37040986 + 8200 Lamar_Jackson_QB_37040963
 + 4300 Mark_Andrews_FLEX_37041116 + 4300 Mark_Andrews_TE_37041116
 + 3700 Mike_Williams_FLEX_37041044 + 3700 Mike_Williams_WR_37041044
 + 5700 Najee_Harris_FLEX_37040982 + 5700 Najee_Harris_RB_37040982
 + 8100 Nico_Collins_FLEX_37041026 + 8100 Nico_Collins_WR_37041026
 + 3200 Noah_Gray_FLEX_37041124 + 3200 Noah_Gray_TE_37041124
 + 3900 Pat_Freiermuth_FLEX_37041118 + 3900 Pat_Freiermuth_TE_37041118
 + 6400 Patrick_Mahomes_QB_37040964 + 4900 Rashod_Bateman_FLEX_37041038
 + 4900 Rashod_Bateman_WR_37041038 + 3300 Ravens_DST_37041162
 + 3000 Robert_Woods_FLEX_37041100 + 3000 Robert_Woods_WR_37041100
 + 5700 Russell_Wilson_QB_37040966 + 2500 Steelers_DST_37041165
 + 5100 Tank_Dell_FLEX_37041034 + 5100 Tank_Dell_WR_37041034
 + 3100 Texans_DST_37041163 + 5600 Travis_Kelce_FLEX_37041114
 + 5600 Travis_Kelce_TE_37041114 + 3300 Van_Jefferson_FLEX_37041052
 + 3300 Van_Jefferson_WR_37041052 + 5000 Xavier_Worthy_FLEX_37041036
 + 5000 Xavier_Worthy_WR_37041036 + 5900 Zay_Flowers_FLEX_37041030
 + 5900 Zay_Flowers_WR_37041030 >= 49500
Offense_vs_Defense_BAL_vs_PIT: Calvin_Austin_III_FLEX_37041042
 + Calvin_Austin_III_WR_37041042 + Jaylen_Warren_FLEX_37040984
 + Jaylen_Warren_RB_37040984 + Mike_Williams_FLEX_37041044
 + Mike_Williams_WR_37041044 + Najee_Harris_FLEX_37040982
 + Najee_Harris_RB_37040982 + Pat_Freiermuth_FLEX_37041118
 + Pat_Freiermuth_TE_37041118 + Russell_Wilson_QB_37040966
 + Van_Jefferson_FLEX_37041052 + Van_Jefferson_WR_37041052
 + 13 defense_BAL_selected <= 15
Offense_vs_Defense_HOU_vs_KC: DeAndre_Hopkins_FLEX_37041032
 + DeAndre_Hopkins_WR_37041032 + Hollywood_Brown_FLEX_37041084
 + Hollywood_Brown_WR_37041084 + Isiah_Pacheco_FLEX_37040980
 + Isiah_Pacheco_RB_37040980 + Kareem_Hunt_FLEX_37040986
 + Kareem_Hunt_RB_37040986 + Noah_Gray_FLEX_37041124 + Noah_Gray_TE_37041124
 + Patrick_Mahomes_QB_37040964 + Travis_Kelce_FLEX_37041114
 + Travis_Kelce_TE_37041114 + Xavier_Worthy_FLEX_37041036
 + Xavier_Worthy_WR_37041036 + 15 defense_HOU_selected <= 17
Offense_vs_Defense_KC_vs_HOU: C.J._Stroud_QB_37040965
 + Dalton_Schultz_FLEX_37041120 + Dalton_Schultz_TE_37041120
 + Joe_Mixon_FLEX_37040978 + Joe_Mixon_RB_37040978
 + Nico_Collins_FLEX_37041026 + Nico_Collins_WR_37041026
 + Robert_Woods_FLEX_37041100 + Robert_Woods_WR_37041100
 + Tank_Dell_FLEX_37041034 + Tank_Dell_WR_37041034 + 11 defense_KC_selected
 <= 13
Offense_vs_Defense_PIT_vs_BAL: Derrick_Henry_FLEX_37040976
 + Derrick_Henry_RB_37040976 + Isaiah_Likely_FLEX_37041122
 + Isaiah_Likely_TE_37041122 + Justice_Hill_FLEX_37040988
 + Justice_Hill_RB_37040988 + Lamar_Jackson_QB_37040963
 + Mark_Andrews_FLEX_37041116 + Mark_Andrews_TE_37041116
 + Rashod_Bateman_FLEX_37041038 + Rashod_Bateman_WR_37041038
 + Zay_Flowers_FLEX_37041030 + Zay_Flowers_WR_37041030
 + 13 defense_PIT_selected <= 15
Position_DST: Chiefs_DST_37041164 + Ravens_DST_37041162
 + Steelers_DST_37041165 + Texans_DST_37041163 = 1
Position_FLEX: Calvin_Austin_III_FLEX_37041042 + Dalton_Schultz_FLEX_37041120
 + DeAndre_Hopkins_FLEX_37041032 + Derrick_Henry_FLEX_37040976
 + Hollywood_Brown_FLEX_37041084 + Isaiah_Likely_FLEX_37041122
 + Isiah_Pacheco_FLEX_37040980 + Jaylen_Warren_FLEX_37040984
 + Joe_Mixon_FLEX_37040978 + Justice_Hill_FLEX_37040988
 + Kareem_Hunt_FLEX_37040986 + Mark_Andrews_FLEX_37041116
 + Mike_Williams_FLEX_37041044 + Najee_Harris_FLEX_37040982
 + Nico_Collins_FLEX_37041026 + Noah_Gray_FLEX_37041124
 + Pat_Freiermuth_FLEX_37041118 + Rashod_Bateman_FLEX_37041038
 + Robert_Woods_FLEX_37041100 + Tank_Dell_FLEX_37041034
 + Travis_Kelce_FLEX_37041114 + Van_Jefferson_FLEX_37041052
 + Xavier_Worthy_FLEX_37041036 + Zay_Flowers_FLEX_37041030 = 1
Position_QB: C.J._Stroud_QB_37040965 + Lamar_Jackson_QB_37040963
 + Patrick_Mahomes_QB_37040964 + Russell_Wilson_QB_37040966 = 1
Position_RB: Derrick_Henry_RB_37040976 + Isiah_Pacheco_RB_37040980
 + Jaylen_Warren_RB_37040984 + Joe_Mixon_RB_37040978
 + Justice_Hill_RB_37040988 + Kareem_Hunt_RB_37040986
 + Najee_Harris_RB_37040982 = 2
Position_TE: Dalton_Schultz_TE_37041120 + Isaiah_Likely_TE_37041122
 + Mark_Andrews_TE_37041116 + Noah_Gray_TE_37041124
 + Pat_Freiermuth_TE_37041118 + Travis_Kelce_TE_37041114 = 1
Position_WR: Calvin_Austin_III_WR_37041042 + DeAndre_Hopkins_WR_37041032
 + Hollywood_Brown_WR_37041084 + Mike_Williams_WR_37041044
 + Nico_Collins_WR_37041026 + Rashod_Bateman_WR_37041038
 + Robert_Woods_WR_37041100 + Tank_Dell_WR_37041034
 + Van_Jefferson_WR_37041052 + Xavier_Worthy_WR_37041036
 + Zay_Flowers_WR_37041030 = 3
QB_Runback_C.J._Stroud_Min_runback_1: DeAndre_Hopkins_WR_37041032
 + Hollywood_Brown_WR_37041084 + Isiah_Pacheco_RB_37040980
 + Kareem_Hunt_RB_37040986 + Xavier_Worthy_WR_37041036
 - qb_C.J._Stroud_selected >= 0
QB_Runback_Lamar_Jackson_Min_runback_1: Calvin_Austin_III_WR_37041042
 + Jaylen_Warren_RB_37040984 + Mike_Williams_WR_37041044
 + Najee_Harris_RB_37040982 + Van_Jefferson_WR_37041052
 - qb_Lamar_Jackson_selected >= 0
QB_Runback_Patrick_Mahomes_Min_runback_1: Joe_Mixon_RB_37040978
 + Nico_Collins_WR_37041026 + Robert_Woods_WR_37041100 + Tank_Dell_WR_37041034
 - qb_Patrick_Mahomes_selected >= 0
QB_Runback_Russell_Wilson_Min_runback_1: Derrick_Henry_RB_37040976
 + Justice_Hill_RB_37040988 + Rashod_Bateman_WR_37041038
 + Zay_Flowers_WR_37041030 - qb_Russell_Wilson_selected >= 0
QB_Stack_C.J._Stroud_Min_stack_1: Dalton_Schultz_TE_37041120
 + Nico_Collins_WR_37041026 + Robert_Woods_WR_37041100 + Tank_Dell_WR_37041034
 - qb_C.J._Stroud_selected >= 0
QB_Stack_Lamar_Jackson_Min_stack_1: Isaiah_Likely_TE_37041122
 + Mark_Andrews_TE_37041116 + Rashod_Bateman_WR_37041038
 + Zay_Flowers_WR_37041030 - qb_Lamar_Jackson_selected >= 0
QB_Stack_Patrick_Mahomes_Min_stack_1: DeAndre_Hopkins_WR_37041032
 + Hollywood_Brown_WR_37041084 + Noah_Gray_TE_37041124
 + Travis_Kelce_TE_37041114 + Xavier_Worthy_WR_37041036
 - qb_Patrick_Mahomes_selected >= 0
QB_Stack_Russell_Wilson_Min_stack_1: Calvin_Austin_III_WR_37041042
 + Mike_Williams_WR_37041044 + Pat_Freiermuth_TE_37041118
 + Van_Jefferson_WR_37041052 - qb_Russell_Wilson_selected >= 0
Select_Defense_BAL: - Ravens_DST_37041162 + defense_BAL_selected = 0
Select_Defense_HOU: - Texans_DST_37041163 + defense_HOU_selected = 0
Select_Defense_KC: - Chiefs_DST_37041164 + defense_KC_selected = 0
Select_Defense_PIT: - Steelers_DST_37041165 + defense_PIT_selected = 0
Select_QB_C.J._Stroud: - C.J._Stroud_QB_37040965 + qb_C.J._Stroud_selected = 0
Select_QB_Lamar_Jackson: - Lamar_Jackson_QB_37040963
 + qb_Lamar_Jackson_selected = 0
Select_QB_Patrick_Mahomes: - Patrick_Mahomes_QB_37040964
 + qb_Patrick_Mahomes_selected = 0
Select_QB_Russell_Wilson: - Russell_Wilson_QB_37040966
 + qb_Russell_Wilson_selected = 0
Single_Use_C.J._Stroud: C.J._Stroud_QB_37040965 <= 1
Single_Use_Calvin_Austin_III: Calvin_Austin_III_FLEX_37041042
 + Calvin_Austin_III_WR_37041042 <= 1
Single_Use_Chiefs: Chiefs_DST_37041164 <= 1
Single_Use_Dalton_Schultz: Dalton_Schultz_FLEX_37041120
 + Dalton_Schultz_TE_37041120 <= 1
Single_Use_DeAndre_Hopkins: DeAndre_Hopkins_FLEX_37041032
 + DeAndre_Hopkins_WR_37041032 <= 1
Single_Use_Derrick_Henry: Derrick_Henry_FLEX_37040976
 + Derrick_Henry_RB_37040976 <= 1
Single_Use_Hollywood_Brown: Hollywood_Brown_FLEX_37041084
 + Hollywood_Brown_WR_37041084 <= 1
Single_Use_Isaiah_Likely: Isaiah_Likely_FLEX_37041122
 + Isaiah_Likely_TE_37041122 <= 1
Single_Use_Isiah_Pacheco: Isiah_Pacheco_FLEX_37040980
 + Isiah_Pacheco_RB_37040980 <= 1
Single_Use_Jaylen_Warren: Jaylen_Warren_FLEX_37040984
 + Jaylen_Warren_RB_37040984 <= 1
Single_Use_Joe_Mixon: Joe_Mixon_FLEX_37040978 + Joe_Mixon_RB_37040978 <= 1
Single_Use_Justice_Hill: Justice_Hill_FLEX_37040988 + Justice_Hill_RB_37040988
 <= 1
Single_Use_Kareem_Hunt: Kareem_Hunt_FLEX_37040986 + Kareem_Hunt_RB_37040986
 <= 1
Single_Use_Lamar_Jackson: Lamar_Jackson_QB_37040963 <= 1
Single_Use_Mark_Andrews: Mark_Andrews_FLEX_37041116 + Mark_Andrews_TE_37041116
 <= 1
Single_Use_Mike_Williams: Mike_Williams_FLEX_37041044
 + Mike_Williams_WR_37041044 <= 1
Single_Use_Najee_Harris: Najee_Harris_FLEX_37040982 + Najee_Harris_RB_37040982
 <= 1
Single_Use_Nico_Collins: Nico_Collins_FLEX_37041026 + Nico_Collins_WR_37041026
 <= 1
Single_Use_Noah_Gray: Noah_Gray_FLEX_37041124 + Noah_Gray_TE_37041124 <= 1
Single_Use_Pat_Freiermuth: Pat_Freiermuth_FLEX_37041118
 + Pat_Freiermuth_TE_37041118 <= 1
Single_Use_Patrick_Mahomes: Patrick_Mahomes_QB_37040964 <= 1
Single_Use_Rashod_Bateman: Rashod_Bateman_FLEX_37041038
 + Rashod_Bateman_WR_37041038 <= 1
Single_Use_Ravens: Ravens_DST_37041162 <= 1
Single_Use_Robert_Woods: Robert_Woods_FLEX_37041100 + Robert_Woods_WR_37041100
 <= 1
Single_Use_Russell_Wilson: Russell_Wilson_QB_37040966 <= 1
Single_Use_Steelers: Steelers_DST_37041165 <= 1
Single_Use_Tank_Dell: Tank_Dell_FLEX_37041034 + Tank_Dell_WR_37041034 <= 1
Single_Use_Texans: Texans_DST_37041163 <= 1
Single_Use_Travis_Kelce: Travis_Kelce_FLEX_37041114 + Travis_Kelce_TE_37041114
 <= 1
Single_Use_Van_Jefferson: Van_Jefferson_FLEX_37041052
 + Van_Jefferson_WR_37041052 <= 1
Single_Use_Xavier_Worthy: Xavier_Worthy_FLEX_37041036
 + Xavier_Worthy_WR_37041036 <= 1
Single_Use_Zay_Flowers: Zay_Flowers_FLEX_37041030 + Zay_Flowers_WR_37041030
 <= 1
Team_Limit_BAL_With_QB_C.J._Stroud: Derrick_Henry_FLEX_37040976
 + Derrick_Henry_RB_37040976 + Isaiah_Likely_FLEX_37041122
 + Isaiah_Likely_TE_37041122 + Justice_Hill_FLEX_37040988
 + Justice_Hill_RB_37040988 + Lamar_Jackson_QB_37040963
 + Mark_Andrews_FLEX_37041116 + Mark_Andrews_TE_37041116
 + Rashod_Bateman_FLEX_37041038 + Rashod_Bateman_WR_37041038
 + Ravens_DST_37041162 + Zay_Flowers_FLEX_37041030 + Zay_Flowers_WR_37041030
 - 11 qb_C.J._Stroud_selected <= 3
Team_Limit_BAL_With_QB_Patrick_Mahomes: Derrick_Henry_FLEX_37040976
 + Derrick_Henry_RB_37040976 + Isaiah_Likely_FLEX_37041122
 + Isaiah_Likely_TE_37041122 + Justice_Hill_FLEX_37040988
 + Justice_Hill_RB_37040988 + Lamar_Jackson_QB_37040963
 + Mark_Andrews_FLEX_37041116 + Mark_Andrews_TE_37041116
 + Rashod_Bateman_FLEX_37041038 + Rashod_Bateman_WR_37041038
 + Ravens_DST_37041162 + Zay_Flowers_FLEX_37041030 + Zay_Flowers_WR_37041030
 - 11 qb_Patrick_Mahomes_selected <= 3
Team_Limit_HOU_With_QB_Lamar_Jackson: C.J._Stroud_QB_37040965
 + Dalton_Schultz_FLEX_37041120 + Dalton_Schultz_TE_37041120
 + Joe_Mixon_FLEX_37040978 + Joe_Mixon_RB_37040978
 + Nico_Collins_FLEX_37041026 + Nico_Collins_WR_37041026
 + Robert_Woods_FLEX_37041100 + Robert_Woods_WR_37041100
 + Tank_Dell_FLEX_37041034 + Tank_Dell_WR_37041034 + Texans_DST_37041163
 - 9 qb_Lamar_Jackson_selected <= 3
Team_Limit_HOU_With_QB_Russell_Wilson: C.J._Stroud_QB_37040965
 + Dalton_Schultz_FLEX_37041120 + Dalton_Schultz_TE_37041120
 + Joe_Mixon_FLEX_37040978 + Joe_Mixon_RB_37040978
 + Nico_Collins_FLEX_37041026 + Nico_Collins_WR_37041026
 + Robert_Woods_FLEX_37041100 + Robert_Woods_WR_37041100
 + Tank_Dell_FLEX_37041034 + Tank_Dell_WR_37041034 + Texans_DST_37041163
 - 9 qb_Russell_Wilson_selected <= 3
Team_Limit_KC_With_QB_Lamar_Jackson: Chiefs_DST_37041164
 + DeAndre_Hopkins_FLEX_37041032 + DeAndre_Hopkins_WR_37041032
 + Hollywood_Brown_FLEX_37041084 + Hollywood_Brown_WR_37041084
 + Isiah_Pacheco_FLEX_37040980 + Isiah_Pacheco_RB_37040980
 + Kareem_Hunt_FLEX_37040986 + Kareem_Hunt_RB_37040986
 + Noah_Gray_FLEX_37041124 + Noah_Gray_TE_37041124
 + Patrick_Mahomes_QB_37040964 + Travis_Kelce_FLEX_37041114
 + Travis_Kelce_TE_37041114 + Xavier_Worthy_FLEX_37041036
 + Xavier_Worthy_WR_37041036 - 13 qb_Lamar_Jackson_selected <= 3
Team_Limit_KC_With_QB_Russell_Wilson: Chiefs_DST_37041164
 + DeAndre_Hopkins_FLEX_37041032 + DeAndre_Hopkins_WR_37041032
 + Hollywood_Brown_FLEX_37041084 + Hollywood_Brown_WR_37041084
 + Isiah_Pacheco_FLEX_37040980 + Isiah_Pacheco_RB_37040980
 + Kareem_Hunt_FLEX_37040986 + Kareem_Hunt_RB_37040986
 + Noah_Gray_FLEX_37041124 + Noah_Gray_TE_37041124
 + Patrick_Mahomes_QB_37040964 + Travis_Kelce_FLEX_37041114
 + Travis_Kelce_TE_37041114 + Xavier_Worthy_FLEX_37041036
 + Xavier_Worthy_WR_37041036 - 13 qb_Russell_Wilson_selected <= 3
Team_Limit_PIT_With_QB_C.J._Stroud: Calvin_Austin_III_FLEX_37041042
 + Calvin_Austin_III_WR_37041042 + Jaylen_Warren_FLEX_37040984
 + Jaylen_Warren_RB_37040984 + Mike_Williams_FLEX_37041044
 + Mike_Williams_WR_37041044 + Najee_Harris_FLEX_37040982
 + Najee_Harris_RB_37040982 + Pat_Freiermuth_FLEX_37041118
 + Pat_Freiermuth_TE_37041118 + Russell_Wilson_QB_37040966
 + Steelers_DST_37041165 + Van_Jefferson_FLEX_37041052
 + Van_Jefferson_WR_37041052 - 11 qb_C.J._Stroud_selected <= 3
Team_Limit_PIT_With_QB_Patrick_Mahomes: Calvin_Austin_III_FLEX_37041042
 + Calvin_Austin_III_WR_37041042 + Jaylen_Warren_FLEX_37040984
 + Jaylen_Warren_RB_37040984 + Mike_Williams_FLEX_37041044
 + Mike_Williams_WR_37041044 + Najee_Harris_FLEX_37040982
 + Najee_Harris_RB_37040982 + Pat_Freiermuth_FLEX_37041118
 + Pat_Freiermuth_TE_37041118 + Russell_Wilson_QB_37040966
 + Steelers_DST_37041165 + Van_Jefferson_FLEX_37041052
 + Van_Jefferson_WR_37041052 - 11 qb_Patrick_Mahomes_selected <= 3
Binaries
C.J._Stroud_QB_37040965
Calvin_Austin_III_FLEX_37041042
Calvin_Austin_III_WR_37041042
Chiefs_DST_37041164
Dalton_Schultz_FLEX_37041120
Dalton_Schultz_TE_37041120
DeAndre_Hopkins_FLEX_37041032
DeAndre_Hopkins_WR_37041032
Derrick_Henry_FLEX_37040976
Derrick_Henry_RB_37040976
Hollywood_Brown_FLEX_37041084
Hollywood_Brown_WR_37041084
Isaiah_Likely_FLEX_37041122
Isaiah_Likely_TE_37041122
Isiah_Pacheco_FLEX_37040980
Isiah_Pacheco_RB_37040980
Jaylen_Warren_FLEX_37040984
Jaylen_Warren_RB_37040984
Joe_Mixon_FLEX_37040978
Joe_Mixon_RB_37040978
Justice_Hill_FLEX_37040988
Justice_Hill_RB_37040988
Kareem_Hunt_FLEX_37040986
Kareem_Hunt_RB_37040986
Lamar_Jackson_QB_37040963
Mark_Andrews_FLEX_37041116
Mark_Andrews_TE_37041116
Mike_Williams_FLEX_37041044
Mike_Williams_WR_37041044
Najee_Harris_FLEX_37040982
Najee_Harris_RB_37040982
Nico_Collins_FLEX_37041026
Nico_Collins_WR_37041026
Noah_Gray_FLEX_37041124
Noah_Gray_TE_37041124
Pat_Freiermuth_FLEX_37041118
Pat_Freiermuth_TE_37041118
Patrick_Mahomes_QB_37040964
Rashod_Bateman_FLEX_37041038
Rashod_Bateman_WR_37041038
Ravens_DST_37041162
Robert_Woods_FLEX_37041100
Robert_Woods_WR_37041100
Russell_Wilson_QB_37040966
Steelers_DST_37041165
Tank_Dell_FLEX_37041034
Tank_Dell_WR_37041034
Texans_DST_37041163
Travis_Kelce_FLEX_37041114
Travis_Kelce_TE_37041114
Van_Jefferson_FLEX_37041052
Van_Jefferson_WR_37041052
Xavier_Worthy_FLEX_37041036
Xavier_Worthy_WR_37041036
Zay_Flowers_FLEX_37041030
Zay_Flowers_WR_37041030
defense_BAL_selected
defense_HOU_selected
defense_KC_selected
defense_PIT_selected
qb_C.J._Stroud_selected
qb_Lamar_Jackson_selected
qb_Patrick_Mahomes_selected
qb_Russell_Wilson_selected
End
