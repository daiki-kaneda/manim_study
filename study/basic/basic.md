
### Manimの基本

Manim...pythonを使って、数学のアニメーションを生成するライブラリ

Mobject...Manimにおいて、アニメーションを構成する要素を表すもの。例:Circle,Rectangleなど
(Mobjectは基本的に外郭を表すので、継承して使われる)

Animation...Animationを表すクラス.例:FadeIn,Rotateなど.カスタムアニメーションはAnimationを継承して、interporate_mobjectを実装することで作ることが可能。

Scene...アニメーションの動画を表すクラス。Sceneを継承した
constructメソッド内でmobjectの追加、削除、アニメーションが行われる
Sceneの基本的なメソッド
- add...Mobjectを画面に追加する
- remove...Mobjectを画面から削除する
- play...Mobjectとアニメーションを指定して、アニメーションを起こす
- wait...一定期間、アニメーションをストップする
Sceneの基本的なプロパティ
- mobjects...現在の画面内のmobject全体のリスト
