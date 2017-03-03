bottleで作る「画像地理情報マップ」
===
## 目的
技術評論社の「Pythonエンジニア養成読本」第5章「入門Webアプリケーション開発」を参考に、
軽量Webフレームワークのbottleを使ったアプリーケーション開発の演習を行います[1]。
テキストで作成する「書籍管理アプリ」を参考にして、画像の撮影位置をGoogle Map APIで表示する
「画像地理情報マップ」を作成します。

## 機能
- 一覧：登録した画像のタイトル、サムネール、緯度、経度の一覧を表示します。
- 登録：画像のタイトル、ファイル名を登録します。緯度と経度は画像ファイルのメタデータから読み込みます。
- 地図：登録した画像の撮影位置をGoogle Map APIを使用して、一括表示します。

## テキスト
[1] 鈴木たかのり, 清原弘貴, 関根裕紀ほか, 『Pythonエンジニア養成読本』, 技術評論社 (2015)  
[http://gihyo.jp/book/2015/978-4-7741-7320-7](http://gihyo.jp/book/2015/978-4-7741-7320-7)

[2] 『Webを支える技術』, 技術評論社（2010）
[http://gihyo.jp/magazine/wdpress/plus/978-4-7741-4204-3](http://gihyo.jp/magazine/wdpress/plus/978-4-7741-4204-3)

## ウェブサイト
[3] 『実践コンピュータビジョン サンプルプログラム』<br>
第5章担当の関根さんによる「書籍管理アプリ」のサンプルコードが掲載されている。<br>
[https://github.com/checkpoint/pymook_web_application](https://github.com/checkpoint/pymook_web_application)  

[4] Google Maps API, ウェブ向け Maps JavaScript API<br>
JavaScriptを用いたGoogle Maps APIの操作について説明されている。<br>
[https://developers.google.com/maps/documentation/javascript/](https://developers.google.com/maps/documentation/javascript/)
