

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



countries_data = [
    ("Canada", 9_984_670, 38_246_108, "North America"),
    ("China", 9_596_961, 1_411_778_724, "Asia"),
    ("United States", 9_833_517, 331_893_745, "North America"),
    ("Brazil", 8_515_767, 214_326_223, "South America"),
    ("Australia", 7_692_024, 25_687_041, "Australia/Oceania"),
    ("India", 3_287_263, 1_393_409_038, "Asia"),
    ("Argentina", 2_780_400, 45_808_747, "South America"),
    ("Kazakhstan", 2_724_900, 19_002_586, "Asia"),
    ("Algeria", 2_381_741, 44_616_626, "Africa"),
    ("Democratic Republic of the Congo", 2_344_858, 92_378_000, "Africa"),
    ("Greenland", 2_166_086, 56_421, "North America"),
    ("Saudi Arabia", 2_149_690, 35_340_680, "Asia"),
    ("Mexico", 1_964_375, 126_014_024, "North America"),
    ("Indonesia", 1_904_569, 276_361_788, "Asia"),
    ("Sudan", 1_861_484, 44_909_351, "Africa"),
    ("Libya", 1_759_540, 6_958_538, "Africa"),
    ("Iran", 1_648_195, 85_028_760, "Asia"),
    ("Mongolia", 1_564_110, 3_329_282, "Asia"),
    ("Peru", 1_285_216, 33_359_416, "South America"),
    ("Chad", 1_284_000, 16_914_985, "Africa"),
    ("Niger", 1_267_000, 25_130_810, "Africa"),
    ("Angola", 1_246_700, 33_933_611, "Africa"),
    ("Mali", 1_240_192, 20_856_000, "Africa"),
    ("South Africa", 1_221_037, 60_041_996, "Africa"),
    ("Colombia", 1_141_748, 51_049_498, "South America"),
    ("Ethiopia", 1_104_300, 117_876_226, "Africa"),
    ("Bolivia", 1_098_581, 11_832_936, "South America"),
    ("Mauritania", 1_030_700, 4_775_110, "Africa"),
    ("Egypt", 1_002_450, 104_258_327, "Africa"),
    ("Tanzania", 945_087, 61_498_438, "Africa"),
    ("Nigeria", 923_768, 211_400_708, "Africa"),
    ("Venezuela", 916_445, 28_704_947, "South America"),
    ("Pakistan", 881_912, 225_199_937, "Asia"),
    ("Namibia", 825_615, 2_587_344, "Africa"),
    ("Mozambique", 801_590, 32_163_045, "Africa"),
    ("Turkey", 783_562, 85_042_736, "Asia"),
    ("Chile", 756_102, 19_212_362, "South America"),
    ("Zambia", 752_618, 18_920_657, "Africa"),
    ("Myanmar", 676_578, 54_806_014, "Asia"),
    ("Afghanistan", 652_864, 40_099_462, "Asia"),
    ("France", 643_801, 67_499_343, "Europe"),
    ("Somalia", 637_657, 16_359_500, "Africa"),
    ("Central African Republic", 622_984, 4_920_467, "Africa"),
    ("South Sudan", 619_745, 11_381_377, "Africa"),
    ("Ukraine", 603_500, 43_733_759, "Europe"),
    ("Madagascar", 587_041, 28_427_333, "Africa"),
    ("Botswana", 581_730, 2_397_240, "Africa"),
    ("Kenya", 580_367, 54_985_702, "Africa"),
    ("Yemen", 527_968, 30_490_639, "Asia"),
    ("Thailand", 513_120, 69_950_844, "Asia"),
    ("Germany", 357_022, 83_240_525, "Europe"), 
    ("Japan", 377_975, 125_800_000, "Asia")
]

df = pd.DataFrame(countries_data, columns=["Country", "Area", "Population", "Continent"])



df['Density'] = df['Population'] / df['Area']

top_density = df.sort_values('Density', ascending=False).head(15)


plt.figure(figsize=(12, 8))
sns.barplot(
    data=top_density, 
    x="Density", 
    y="Country", 
    palette="magma" 
)


plt.title("Top 15 zemí podle hustoty zalidnění", fontsize=16)
plt.xlabel("Hustota (obyvatel na km²)", fontsize=12)
plt.ylabel("Země", fontsize=12)

for index, value in enumerate(top_density['Density']):
    plt.text(value, index, f'{int(value)}', va='center')

plt.tight_layout()
plt.show()



