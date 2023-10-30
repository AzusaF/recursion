# 問題 1
# 縦(int)、横(int)、高さ(int)を受けとって、立体の体積(int)を計算する boxVolume という関数を作成してください
# 縦 2、横 3、高さ 5 を関数に入力して、コンソールに出力してみましょう (30)
def boxVolume(len, depth, height):
    return len * depth * height

print(boxVolume(2,3,5))

# 問題 2
# 半径(int)、高さ(int)を受け取って、円柱の体積(int)を計算する cylinderVolume という関数を定義してください
# 円周率は 3 で計算してください
# 半径 2、高さ 5 を関数に入力して、コンソールに出力してみましょう(60)
def cylinderVolume(redius, height):
    return redius^2 * 3 * height

print(cylinderVolume(2,5))

# 問題 3
# 上底(int)、下底(int)、高さ(int)を受け取って、台形の面積(double)を返す trapezoidArea という関数を定義してください
# 上底 3、下底 5、高さ 6 を関数に入力して、コンソールに出力してみましょう (24.0)

def trapezoidArea(top, bottom, height):
    return (top + bottom) * height / 2
