# Preferred Networks インターンシップ2020 チップテーマ25・26の選考課題

チップテーマ課題では、以下の3つの選択肢からいずれかを選び、回答して下さい。

1. 本 PDF 記載の課題1,2,3
2. (`README-ja.pdf` の記載の汎用コーディング課題のQ1,Q2,Q3) + (本 PDF 記載の課題3)
3. (本 PDF 記載の課題1) + (`README-ja.pdf` に記載の汎用コーディング課題にあるQ1,Q2,Q3のうちいずれか1つ) + (本 PDF 記載の課題3)

`README-ja.pdf` の記載の汎用コーディング課題を解く際には、プログラミング言語には Python3, C, C++, Rust, Perl のいずれかの言語を使用して下さい。

諸注意、提出方法、問い合わせ方法については `README-ja.pdf` を参照して下さい。

## まず

もし手元にRTLシミュレーション環境がない場合はVerilatorとGTK Waveのようなオープンソースソフトウェアをインストールする、もしくはEDA playground のようなWebサイトを利用してください。なお、これらのソフトウェアやWebサイトはPFNとは関係が無いため質問にお答えすることはできません。  
https://www.veripool.org/wiki/verilator  
http://gtkwave.sourceforge.net/  
https://www.edaplayground.com/  

## 課題1: 単純なFIFO
### 課題1.1
FIFOとは2つのコンポーネント間の通信と同期を実現させるのに必要なものです。パラメータ化したFIFOを好きなHDLで作ってください。FIFO自体は非常に基礎的ですので、どうやって実装するか、どういう信号を出力させるのか、よく考えて実装してください。
### 課題1.2　
テストベンチを作って、FIFOをテストしてください。

### 提出物
* FIFOのRTLコードとテストベンチコード
* 正しい動作を示しているテストベンチの波形スクリーンショット

## 課題2　2つのFIFOから作ったキュー
### 課題2.1　2つのFIFOからキューを作る
FIFOはよく2つのコンポーネントを接続するために利用されています。データ消失させてはなりません。2つのFIFO（深さ4）を使って、キューになる様に繋いでください。この課題のキューははSTOP信号が立つまで毎サイクル入力を受け取ってFIFOに保存する、という独自のプロトコルで動作します。

キューの具体的なプロトコルは以下の通りです。  
**FIFO1は一杯じゃない：** 入力を受け取る  
**FIFO1は一杯、FIFO2は空：** 入力を中止して（STOP=1）、FIFO1のデータをポップして、FIFO2にプッシュする。FIFO1は空になってからまた入力を再開する（STOP=0）  
**FIFO1は一杯、FIFO2は一杯：** 入力を中止して（STOP=1）、まずFIFO2のデータポップして、出力する。FIFO2は空になってからFIFO1のデータをポップして、またFIFO2にプッシュする。FIFO1は空になってからまた入力を再開する（STOP=0）。  

上記のようにSTOP信号でテストベンチにデータの送信をを停止するように指示してください。STOP=1の期間の入力データは取り込まずに無視してください。ただし、待たされている期間を最小化する様に、STOP信号が立っているサイクル数が最小になることを確認してください。

### 課題2.2　テストベンチを作って、キューをテストする
以上のプロトコルをテストできるテストベンチを作ってください。STOP信号が立っていなければ、毎サイクルをデータワードを入力させてください。

テストベンチの波形は以下の様に見えるはずです。
![課題2の波形](images/chip_hw2.png)

実装の出力例
>  0 Pushing  4 stop: 0 out:  0  
>  1 Pushing  1 stop: 0 out:  0  
>  2 Pushing  9 stop: 0 out:  0  
>  3 Pushing  3 stop: 0 out:  0  
>  4 Waiting... stop: 1 out:  0  
>  5 Waiting... stop: 1 out:  0  
>  6 Waiting... stop: 1 out:  0  
>  7 Waiting... stop: 1 out:  0  
>  8 Pushing 13 stop: 0 out:  0  
>  9 Pushing 13 stop: 0 out:  0  
> 10 Pushing  5 stop: 0 out:  0  
> 11 Pushing  2 stop: 0 out:  0  
> 12 Waiting... stop: 1 out:  4  
> 13 Waiting... stop: 1 out:  1  
> 14 Waiting... stop: 1 out:  9  
> 15 Waiting... stop: 1 out:  3  
> 16 Waiting... stop: 1 out:  0  
> 17 Waiting... stop: 1 out:  0  
> 18 Waiting... stop: 1 out:  0  
> 19 Waiting... stop: 1 out:  0  
> 20 Pushing  1 stop: 0 out:  0  
> 21 Pushing 13 stop: 0 out:  0  
> 22 Pushing  6 stop: 0 out:  0  
> 23 Pushing 13 stop: 0 out:  0  
> 24 Waiting... stop: 1 out: 13  
> 25 Waiting... stop: 1 out: 13  
> 26 Waiting... stop: 1 out:  5  
> 27 Waiting... stop: 1 out:  2  
> 28 Waiting... stop: 1 out:  0  
> 29 Waiting... stop: 1 out:  0  
> 30 Waiting... stop: 1 out:  0  
> 31 Waiting... stop: 1 out:  0  

### 提出物
次のものを提出してください。
* キューのRTLコードとテストベンチのコード
* 正しい動作を示しているテストベンチの波形スクリーンショット
* 任意　追加資料（状態遷移図、あなたの実装方法や考え方等を説明しているドキュメント、など）

## 課題3　疑似論文査読　（テーマ25　次世代の高効率学習・推論アーキテクチャ）
関心のあるアーキテクチャ分野の論文一本を自由に選んでください。学会の候補を以下に例示します。これらの学会でなくても構いません。  
ISCA, HPCA, ASPLOS, MICRO, DATE, DAC, ASP-DAC, ICCAD, VLSI

迷った場合、以下から選んでください。  
[1] Schuiki, Fabian, Michael Schaffner, and Luca Benini. "Ntx: An energy-efficient streaming accelerator for floating-point generalized
reduction workloads in 22 nm fd-soi." 2019 Design, Automation & Test in Europe Conference & Exhibition (DATE). IEEE, 2019. https://arxiv.org/pdf/1812.00182  
[2] B. Zimmer et al., "A 0.32–128 TOPS, Scalable Multi-Chip-Module-Based Deep Neural Network Inference Accelerator With Ground-Referenced Signaling in 16 nm," in IEEE Journal of Solid-State Circuits, vol. 55, no. 4, pp. 920-932, April 2020.  

選んだ論文に対し、擬似的な査読を行ってください。論文の要点をA4 1枚で、以下の項目を含めつつまとめてください。
* 論文のアプローチの3つの利点
* 論文のアプローチの3つの欠点
* PPA (Power 消費電力, Performance 性能, Area 面積) にどう影響しているか
* 手法に改善できるところがあるか
* 研究の次のステップとして何が考えられるか

### 提出物
* 擬似的な査読

## 課題3　記事論文査読　（テーマ26　機械学習とEDA）
関心のあるEDA分野の論文一本を自由に選んでください。学会の候補を以下に例示します。これらの学会でなくても構いません。  
ISCA, HPCA, ASPLOS, MICRO, DATE, DAC, ASP-DAC, ICCAD, VLSI

迷った場合、以下から選んでください。  
[1] Han, Seung-Soo, et al. "A deep learning methodology to proliferate golden signoff timing." 2014 Design, Automation & Test in Europe Conference & Exhibition (DATE). IEEE, 2014. https://vlsicad.ucsd.edu/Publications/Conferences/311/c311.pdf  
[2] Ma, Yuzhe, et al. "Understanding Graphs in EDA: From Shallow to Deep Learning." Proceedings of the 2020 International Symposium on Physical Design. 2020. http://www.cse.cuhk.edu.hk/~byu/papers/C94-ISPD2020-GCN.pdf  

選んだ論文に対し、擬似的な査読を行ってください。論文の要点をA4 1枚で、以下の項目を含めつつまとめてください。
* 論文のアプローチの3つの利点
* 論文のアプローチの3つの欠点
* PPA (Power 消費電力, Performance 性能, Area 面積)、もしくはアルゴリズムの処理時間・計算複雑度にどう影響しているか
* 手法に改善できるところがあるか
* 研究の次のステップとして何が考えられるか

### 提出物
* 擬似的な査読

