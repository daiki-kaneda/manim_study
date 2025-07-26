from manim import *

# Manimで3次元のアニメーションを行うにはSceneの代わりにSceneのサブクラスのThreeDSceneを使い、基本的には2次元の場合と同じである
# ただし、３次元の場合は、カメラを調整することが重要で、次のようなThreeDTheneのメソッドが使える
# set_camera_orientation...初期のカメラ視点を設定する
# move_camera...カメラをアニメーションとともに移動させるメソッド
# begin(stop)_ambient_camera_rotation...シーンが再生されている間、カメラを自動的に回転させる(または停止させる)ためのメソッド
# add(fixed)_fixed_orientation_mobjects()...カメラが動いても表示を変えないMobjectを追加、削除するメソッド

# phi:水平面からの上下の傾き
# theta:z軸を中心とした水平面上の回転
# gammma:カメラ自体の傾き
# rate:回転速度

# ThreeDMObjectの例:
# Cube:立方体
# Sphere:球体
# Cylinder:円柱
# Cone:円錐
# ParametricSurface:複雑な三次元曲面
# ThreeDAxes:３時の座標軸

class StackedCubes(ThreeDScene): # ThreeDSceneを継承する
    def construct(self):
        # カメラの初期設定（見やすい角度に調整）
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) # カメラを自動でゆっくり回転させる

        # 軸の表示（オプション）
        # axes = ThreeDAxes()
        # self.add(axes)

        # 立方体を積み重ねる
        cubes = VGroup()
        for i in range(3): # 3つの立方体を積み重ねる
            cube = Cube(side_length=1, fill_color=ORANGE)
            # 各立方体を前の立方体の上に配置
            # i=0: Z=0.5 (立方体の中心が0.5、底面が0)
            # i=1: Z=1.5 (最初の立方体の上に置く)
            # i=2: Z=2.5 (2番目の立方体の上に置く)
            cube.move_to(ORIGIN + OUT * 0.5) # Z軸方向に少しずらして立体感を出す
            cube.shift(UP * (i + 0.5)) # i番目の立方体を適切な高さに配置
            cubes.add(cube)

        # 立方体を一つずつ表示させるアニメーション
        for cube in cubes:
            self.play(Create(cube))
            self.wait(0.2)

        self.wait(1)

        # 積み重ねた立方体全体を回転させる
        self.play(Rotate(cubes, angle=PI/2, axis=Z_AXIS)) # Z軸を中心に90度回転
        self.wait(1)

        self.stop_ambient_camera_rotation() # カメラ回転を停止
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2) # 真上から見る視点に移動
        self.wait(1)


class StackedCubes2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,zoom=0.5, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        cubes = VGroup()
        for i in range(10):
            cube = Cube(side_length=1,fill_color=ORANGE)
            cube.shift(OUT*i)
            cubes.add(cube)
            
        for cube in cubes:
            self.play(Create(cube))
            self.wait(duration=0.1)
        
