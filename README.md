# ros_stepup_kadai 

# 概要
これはROSの本当の基本ができる人向けのステップアップ課題です。  
Turtlebot2を使用します。Ubuntuは18.04、ROSはMelodicを想定しています。また、言語は、Pythonを想定しています。  
Turtlebot2を動かすところから始まり、PublisherとSubscriberの理解、msgファイルについて、launchファイルについて、及びparamとargの理解を課題として提供します。課題は全部で7つあります。  
  
課題1: Turtlebot2を動かしてみよう！  
課題2: Publisherを使ってみよう！  
課題3: Subscriberを使ってみよう！  
課題4: メッセージの型を自作してみよう！  
課題5: launchファイルを自作してみよう！  
課題6: paramを使ってみよう！  
課題7: argを使ってみよう！  
  
ここでは、課題を提示します。解答例は、付属のファイルの中にあります。

# 課題1: Turtlebot2を動かしてみよう！

### 製作者からのお言葉
以下の課題をやる上で、Turtlebot2を動かすことができる必要があります。まずは、簡単に動かしてみましょう。[ここ](https://github.com/rionehome/ros_practice_2022/blob/main/sample.py)に例があります。ただし、下にあるようにコピペは禁止です。1行1行何をしているか説明できないと意味がないからです。Turtlebot2を動かすために必要なパッケージらは[ここ](https://github.com/rionehome/Turtlebot2-On-Melodic)にあります。さあ、まずは1つ目、頑張ってみましょう！  
  
### 内容
①真っ直ぐ適当な速さである程度進んで、  
②上から見て時計回りに180°その場で回転し、  
③①と同様にし初めの場所まで帰ってくる  
プログラムを以下の条件で作成しなさい。

### 条件
* コピペはせずに、すべて打ち込み  
  
  
# 課題2,3: PublisherとSubscriberを使ってみよう！
### 製作者からのお言葉
いよいよ本格的にROSのプログラムを書いていってもらいます。ROSのプログラムは、メッセージを送信する側と受け取る側があって初めて成り立ちます。ここでは、実際のROSシステムの開発のように、実装したいことを元に開発をしてもらいます。通常は、トピックの情報さえあれば、出版者と購読者は別々に作成することができ、別々に作成することが普通です。しかし、ここでは両方を同時に実装してもらいます。その方がプログラムの流れを追いやすいと考えているからです。2つのプログラムを同時に実装することは難しいですが、この課題をすることで、ROSの通信をより理解できると思います。というわけで、いってみましょう、課題2&3です！
  
### ヒント  
まずは、図にしてみましょう。ROSの図、つまりrqt-graphを書いてみましょう。また、各ノードおよびトピックの情報も別にまとめられるといいですね。  
次に、プログラムの流れをフローチャートで書いてみましょう。テキトーでも流れがわかれば問題ないと思います。どんな処理をしなければいけないのかが見えてくるはずです。  
  
### 内容
次のようなノード、トピックを持ち、以下の指示に従ったプログラムを作りなさい。  

* トピック名:　`oreno/shijini/shitagae`  
メッセージの型　`std_msgs/Int16`  
(メッセージの取り得る値　0,1,2,3,4,5)  
* ノード1 名前:　`kitaini_kotaetemiyo`  
Publisher `oreno/shijini/shitagae`  
* ノード2 名前:　`shouchi`  
Publisher `mobile_base/commands/velocity`  
Subscriber `oreno/shijini/shitagae`  
  
ノード1を持つファイルを課題2、ノード2を持つファイルを課題3とする。  
  
* 課題2から課題3へメッセージを送り、課題3からTurtlebot2へメッセージを送る。  
* 課題2は、上のトピックを使い、0〜5の値を送る。それを受け取った課題3は、値に対応する動作をTurtlebot2へ命令する。値と動作の対応は以下である。  

| 値 | 動き |
|:---:|:---:|
|0|停止|
|1|前進|
|2|後進|
|3|左回転|
|4|右回転|
|5|プログラム終了|
  
* Turtlebotの動く速さは、直線成分が0.2、回転成分が0.5とする。  
  
### 動作  
①Turtlebot2のノード起動  
②課題3を実行  
③課題2を実行  
④課題2が時刻0に動作し始めたとして、時刻に対する値を以下のように送信する。  

| 時刻 | 値 |
|:---:|:---:|
|0〜3|1|
|3〜5|3|
|5〜7|4|
|7〜10|2|
|10〜|5|
  
⑤課題2の終了  
⑥課題3の終了  

### 条件
* classを使用  
* Subscriberのコールバック関数の条件分岐にはswitch文ではなくif-elif文を使用  
  
以上の内容に沿ったプログラムならば、これ以外は指定しない。ただし、出来るだけ簡潔に美しく、コメントアウトなどもしながら、きれいな読みやすいプログラムを作成すること。  
  
  
# 課題4: メッセージの型を自作してみよう！  
<!--
### 製作者からのお言葉
ROSで通信する際にいつもメッセージを使っていますよね。でも、Int16とかTwistなどのメッセージの型って普通プログラムで使うものじゃないですよね。あれって、何なんでしょうか。あれはユーザによって独自に定義された型です。てことは、どこかに定義があり、どうにかして使えるようになっているはずなんです。ROSのシステムを設計する際に、新しい型を作れることは必須です。ここでは、その型の作り型をやさしい課題として提供し、学んでいただきます。それでは、さっそくやってみましょう、課題4です！
  
### ヒント
さすがに、いきなりメッセージを作るのは難しいと思うので、かなりやりすぎなぐらいサポートします。  
メッセージを定義するには、ROSのパッケージ作成時に自動で生成されるCMakeLists.txtとpackage.xmlの内容を変更する必要があります。  
なんですが、今回、このパッケージをご利用のお客様に限り、なんとすでに変更したものを、無料で、無料でご提供いたします！  
パッケージ内にある[CMakeLists.txt](https://github.com/rionehome/ros_stepup_kadai/blob/main/CMakeLists.txt)と[package.xml](https://github.com/rionehome/ros_stepup_kadai/blob/main/package.xml)がそれになります。  
package.xmlの方は、これ以上変更する必要はありません。すでに、自作のメッセージファイルを読み込む設定になっています。  
CMakeLists.txtのadd_message_filesに自作したメッセージの名前を、
```  
add_message_files(  
	FILES  
	(自作したメッセージ名).msg
)  
```
のように追記し、catkin_makeをするだけで自作のメッセージが使えます。  

次に、メッセージファイルの書き方について説明します。  
メッセージファイルとは、自作のメッセージについて定義しているファイルです。そのままですね。  
普通、メッセージファイルは、パッケージ内に「msg」という名前のディレクトリを作り、その中に保存します。ここでもそのようにしてください。  
メッセージファイルの定義に使える基本的な型は、14種類ありますが、ここでは、int64を使った例を紹介します。  
x,y,zの3つの要素を持った型「Vector3」を作成します。  
まず、msgディレクトリ内に、「Vector3.msg」という名前のファイルを作成します。  
次に、このファイルに下の内容を書き込みます。  
```  
int64 x
int64 y
int64 z
```  
これで、CMakeLists.txtを変更し、catkin_makeをすると、型「Vector3」が使用可能となります。簡単ですよね。なんせ、ファイルの名前追記するだけで良いようにしてますから！  
実際に、自作した型を見てみましょう。下のコマンドを打ってみると、上の定義が表示されるはずです。  
```
rosmsg show ros_stepup_kadai/Vector3
```
自作した型は、他の型を定義するのにも使えます。ROSで通信をするのに適した内容の型を作成すると、とても便利になります。それがこの課題で学んで欲しいことです。  

  
### 内容
次の2つのメッセージの型を定義し、以下の指示に従ったプログラムを作りなさい。  

* メッセージの型 1  
名前: `Kangaeruna`  
定義:  
```  
Ugoki ugoki1  
Ugoki ugoki2  
Ugoki ugoki3  
Ugoki ugoki4
```  

* メッセージの型 2  
名前: `Ugoki`  
定義:  
```
int16 movement  
int16 time  
```  
* 基本的なプログラムの動作は、[課題2,3](https://github.com/rionehome/ros_stepup_kadai#課題23-publisherとsubscriberを使ってみよう)と同様とする。必要なら自作したプログラムをコピーして用いてよい。その上で、次の項目を変更しなさい。  

* トピック名:　`oreno/shijini/shitagae`  
メッセージの型　`Kangaeruna`  

* 課題2が送っていた値は、movementへ格納し、課題3がその値でロボットを動かす時間は、timeに格納されているものとする。つまり、トピックの値に対応する動きが、次の表のようになればよい。  
  
| トピックの値 | 動作 |
|:---:|:---:|
|Kangaeruna.ugoki1.movement = 1<br>Kangaeruna.ugoki1.time = 3|前進を3秒間|
|Kangaeruna.ugoki2.movement = 3<br>Kangaeruna.ugoki2.time = 2|左回転を2秒間|
|Kangaeruna.ugoki3.movement = 4<br>Kangaeruna.ugoki3.time = 2|右回転を2秒間|
|Kangaeruna.ugoki4.movement = 2<br>Kangaeruna.ugoki4.time = 3|後進を3秒間|
  
### 条件
* classを使用  
* Subscriberのコールバック関数の条件分岐にはswitch文ではなくif-elif文を使用  
* この課題の本質を理解し、課題2,3と同等あるいは、さらに簡潔で美しいプログラムを書くよう心がけて作成
-->

# 課題5: launchファイルを自作してみよう！
### 製作者からのお言葉
### 内容
# 課題6: paramを使ってみよう！
### 製作者からのお言葉
### 内容
# 課題7: argを使ってみよう！
### 製作者からのお言葉
### 内容
  
  
# 解答
* 課題1の解答 (未公開)  
* 課題2の解答 (未公開)  
* 課題3の解答 (未公開)  
* 課題4の解答 (未制作)  
* 課題5の解答 (未制作)  
* 課題6の解答 (未制作)  
* 課題7の解答 (未制作)  
