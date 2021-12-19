import os  
import cv2
import numpy as np

# 画像ファイルのあるフォルダの相対パス
dir_path = os.path.dirname(os.path.abspath(__file__)) + "/Pokemon" + "/"
# フォルダ内のファイルのリスト生成
files = os.listdir(dir_path)
# pngファイルのリスト生成
files_png = [s for s in files if '.png' in s]
# print(files_png)


##########フリーザー##########
freezer = cv2.imread(os.path.dirname(os.path.abspath(__file__)) + "/Pokemon" + "/articuno.png")

height, width, channel = freezer.shape
bgr = np.zeros(3, np.uint8)
zero = np.zeros(3, np.uint8)
count = 0
# print()

for i in range(height):
        for j in range(width):
                bgr += freezer[i, j]

sum_bgr = bgr[0] + bgr[1] + bgr[2]
sum_freezer = bgr / sum_bgr
# print(sum_freezer[0] + sum_freezer[1] + sum_freezer[2])



list_all = []
for i in files_png:  # ファイル数だけ繰り返す
    img = cv2.imread(dir_path + i)  # 画像の読み出し
    #BGR各チャンネルの輝度をすべての輝度の合計で規格化しリスト化 
    bgr_sum = np.sum(img, axis = (0, 1))                     #元々はaxis = (0, 1)
#     print(bgr_sum)
    b_ratio, g_ratio, r_ratio = bgr_sum / np.sum(bgr_sum)
    bgr_list = [b_ratio,g_ratio, r_ratio]
    list_all.append(bgr_list)

# リストをndarrayに変換
list_all_n = np.array(list_all)
# リストをfloat32に変換
list_all_n = np.float32(list_all_n)
# 計算終了条件の設定。指定された精度(1.0)か指定された回数(10)計算したら終了
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# クラスター数
K = 3
# K-Meansクラスタリングの実施
ret,label,center = cv2.kmeans(list_all_n, K, sum_freezer, criteria, 10, cv2.KMEANS_PP_CENTERS) #元はcv2.KMEANS_RANDOM_CENTERS
# print(len(label))


# ラベル別ディレクトリ作成
for i in range(K):
    new_dir_path = dir_path+str(i) 
    os.mkdir(new_dir_path)

# クラスタリング結果に応じたディレクトリに画像ファイルを移動
for file_name,dir_name in zip(files_png, label):
    original_file_name = dir_path + file_name
    new_file_name = dir_path + str(int(dir_name)) + '/' + file_name
    os.rename(original_file_name, new_file_name)

# クラスタリングされたフォルダの相対パス
result_0 = os.path.dirname(os.path.abspath(__file__)) + "/Pokemon" + "/0"
result_1 = os.path.dirname(os.path.abspath(__file__)) + "/Pokemon" + "/1"
result_2 = os.path.dirname(os.path.abspath(__file__)) + "/Pokemon" + "/2"

# フォルダ内のファイルのリスト生成
result_list_0 = os.listdir(result_0)
result_list_1 = os.listdir(result_1)
result_list_2 = os.listdir(result_2)


# 結果出力
print(sum_freezer)

print("ID: 0")
for i in range(len(result_list_0)):
        print(result_list_0[i])

print("ID: 1")
for i in range(len(result_list_1)):
        print(result_list_1[i])

print("ID: 2")
for i in range(len(result_list_2)):
        print(result_list_2[i])