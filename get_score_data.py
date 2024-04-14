# import json
# import pandas as pd 
# import os 
# import glob

# f = open(f"/media/yzl/demo/smos.json")
# wav_dict = json.load(f)
# f.close()

# # for key, value in wav_dict.items():
# #     print(key, value)
# #     break

# csvs = glob.glob('/media/yzl/demo/smos/*.csv')


# new_dict = {}

# for csv in csvs:
#     df = pd.read_csv(csv)
#     print(df.head())
#     for index, row in df.iterrows():
#         id = int(row['spk_id'])
#         scroe_1  = row['1']
#         scroe_2  = row['2']
#         wav_01 = f"/media/yzl/demo/libritts/{id}/01.wav"
#         wav_02 = f"/media/yzl/demo/libritts/{id}/02.wav"
#         real_01 = wav_dict[wav_01]
#         real_02 = wav_dict[wav_02]
#         if real_01 in new_dict:
#             new_dict[real_01].append(scroe_1)
#         else:
#             new_dict[real_01] = [scroe_1]
#         if real_02 in new_dict:
#             new_dict[real_02].append(scroe_2)
#         else:
#             new_dict[real_02] = [scroe_2]


# # json.dump(new_dict, open(f"/media/yzl/demo/smos_score.json", "w"))

# import json
# import numpy as np

# class NumpyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.int64):
#             return int(obj)
#         return super(NumpyEncoder, self).default(obj)

# # Assume `new_dict` is a dictionary containing numpy int64 values

# with open("/media/yzl/demo/smos_score.json", "w") as f:
#     json.dump(new_dict, f, cls=NumpyEncoder)

import json
f = open(f"/media/yzl/demo/smos_score.json")

smos_dict = json.load(f)


yourtts = []
my = []


for key,value in smos_dict.items():
    print(key)
    avg = sum(value)/len(value)
    if key.split('/')[6] == 'yourtts.wav':
        yourtts.append(avg)
    else:
        my.append(avg)
print(len(yourtts))
print(len(my))


import numpy as np 
print("smos_yourtts={}".format(sum(yourtts)/len(yourtts)))
print("smos_my={}".format(sum(my)/len(my)))


yourtts_std = np.std(yourtts)
my_std = np.std(my)

print(f'Standard deviation of yourtts: {yourtts_std}')
print(f'Standard deviation of my: {my_std}')