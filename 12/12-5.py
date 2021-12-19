import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt

tf.compat.v1.disable_eager_execution()


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#データのサイズ
train_size = x_train.shape[0]
test_size = x_test.shape[0]

#①[28×28]のデータを[1×784]へ---------------
x_train2 = []
x_test2 = []

#学習用画像データ
for i in range(train_size):
    x_train2.append(x_train[i].reshape(-1,))

#テスト用画像データ
for i in range(test_size):
    x_test2.append(x_test[i].reshape(-1,))

#「0〜255」の値を「0〜1」に変換
x_train = np.array(x_train2)/255
x_test = np.array(x_test2)/255


#画像データを入れる用のプレースホルダー
x = tf.compat.v1.placeholder(tf.float32, [None, 784])

#圧縮後の次元数(中間層のノード数)
dim = 100

#各パラメータの初期化
w_enc = tf.Variable(tf.random.truncated_normal(shape=[784, dim], stddev=0.01))
b_enc = tf.Variable(tf.random.truncated_normal(shape=[dim], stddev=0.01))
w_dec = tf.transpose(w_enc)
b_dec = tf.Variable(tf.random.truncated_normal(shape=[784], stddev=0.01))


#エンコード後の結果
encoded = tf.sigmoid(tf.matmul(x, w_enc)+b_enc)

#デコード後の結果
decoded = tf.sigmoid(tf.matmul(encoded, w_dec) + b_dec)


#誤差関数：2乗和誤差
loss = tf.nn.l2_loss(decoded - x)

#学習アルゴリズム
optimizer = tf.optimizers.SGD(0.005)

#学習
train = optimizer.minimize(loss, var_list=[w_enc, b_enc, b_dec])


#パラメータ保存用オブジェクト
saver = tf.train.Saver()
savePlace = 'middle400/middle400'

#損失関数の値の推移を格納するためのリスト
lossList = []


with tf.Session() as sess:

    sess.run(tf.initialize_all_variables())  # 変数の初期化

    #バッチサイズ
    batch_size = 100

    for i in range(6000):

        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]

        sess.run(train, feed_dict={x: x_batch})
        lossValue = sess.run(loss, feed_dict={x: x_batch})/batch_size

        if i % 100 == 0:
            print("バッチ数:", i, "loss:", lossValue)

    #パラメータの保存
    saver.save(sess, 'model/autoencoder/'+savePlace)


encodedList = []  # エンコード後の画像データを入れる。
decodedList = []  # デコードした画像のデータリスト
imgNum = 5  # 表示数

with tf.Session() as sess:
    # 訓練済みモデルのmetaファイルを読み込み
    saver = tf.train.import_meta_graph(
        'model/autoencoder/' + savePlace + '.meta')
    saver.restore(sess, 'model/autoencoder/' + savePlace)

    for i in x_train[:imgNum]:
        encodedImgData = sess.run(encoded, feed_dict={x: i.reshape(1, -1)})
        encodedList.append(encodedImgData)

        decodeImgData = sess.run(decoded, feed_dict={x: i.reshape(1, -1)})
        decodedList.append(decodeImgData)


#リストをnp.array型へ変換
encodedList = np.array(encodedList)
decodedList = np.array(decodedList)

encodedList2 = []
decodedList2 = []

#データの形式を「1×〜」から、「x×x」に変換。
for i in range(imgNum):

    encodedImg = encodedList[i].reshape(5, 5)         #元は(length, length)
    encodedList2.append(encodedImg)

    decodedImg = decodedList[i].reshape(28, 28)
    decodedList2.append(decodedImg)


#表示枚数
col = 5  # 1行に表示する数
row = int(imgNum/col)  # 行数

#学習用画像(元画像)
plt.figure(figsize=(21, 21))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

for i in range(imgNum):
    plt.subplot(row+1, col, i+1)
    img = x_train[i].reshape(28, 28)
    plt.imshow(img, cmap='Greys')

plt.show()


#エンコード後データ
plt.figure(figsize=(21, 21))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

for i in range(imgNum):
    plt.subplot(row+1, col, i+1)
    img = encodedList2[i]
    plt.imshow(img, cmap='Greys')

plt.show()


#デコード後の画像
plt.figure(figsize=(21, 21))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

for i in range(imgNum):
    plt.subplot(row+1, col, i+1)
    img = decodedList2[i]
    plt.imshow(img, cmap='Greys')

plt.show()
