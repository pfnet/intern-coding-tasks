## Task 3

あなたは5人の友人とポーカーで遊んでいます。使用しているのはジョーカーを除く一般的な52枚のトランプのデッキで、以下の手順でゲームを進行します。

You are playing a draw poker with five members using a standard 52-card deck, excluding jokers. The game proceeds as follows:

- 52枚の山札から6人のプレイヤーに各5枚ずつランダムに手札として配ります。配られた手札は全員に公開します。
- あなたは手札から最大 K 枚のカードを**交換**することができます。（あなた以外のプレイヤーは手札を交換できません。）交換は、以下の手続きで行われます。
  1. まず、 手札から K 枚以下のカードを自由に選び、捨てます。捨てた手札は山札に戻りません。
  2. 捨てた枚数と同じ枚数を山札からランダムに引きます。
- 各手札の強さを比較して勝敗を判定します。勝敗の判定は [勝敗の判定] のセクションの通りに行います。

- Each player is dealt 5 cards from the deck, resulting in a random hand. The dealt hand is shown to all players.
- You may **exchange** up to K cards from your hand. (No other player may exchange their cards.) The exchange occurs as follows:
  1. First, pick any number of cards from your hand, up to K, and discard them. The discarded cards do not return to the deck.
  2. Then, draw the same number of cards that were discarded from the deck randomly.
The winner is decided by comparing the strength of the hands. The details of the process is explained in the "Determination of Winning" section.

あなたが他の5人よりも強い手札を得る確率を最大化するためのカードの交換方法全てと、その確率を求めてください。

Find all the best strategies to maximize the probability that you end up with a stronger hand than the other 5 players.

### デッキの構成 / Deck Composition
トランプのデッキは、4種類のスートと13種類のランクからなる合計52枚から構成されます。

- スートは、スペード、ハート、ダイヤモンド、クラブの4種類です。スートによるカードの強弱の差はありません。
- ランクは、2から10, J, Q, K, A の13種類あります。J, Q, K はそれぞれ11, 12, 13として扱われます。A は1および14のいずれのランクとしてもみなすことができます。値が大きいほど強いランクとして扱われます。

The deck consists of 52 cards - 4 suits and 13 different ranks.

- The 4 suits are spades, hearts, diamonds, and clubs. There is no ranking based on suits.
- The 13 ranks range from 2 to 10, J, Q, K, and A. J, Q, and K are considered as 11, 12, and 13, respectively. Rank A can be considered as either 1 or 14. The higher the value, the stronger the rank.

### 勝敗の判定 / Determination of Winning

最も強い手役を作ったプレイヤーがゲームに勝ちます。手役は強い順に全部で以下の9種類あり、複数の手役の条件を満たす場合は最も強い手役が採用されます。

- ストレートフラッシュ: 同じスートの連続した5枚のカード
- フォーカード: 同じランクの4枚のカードが含まれる
- フルハウス: 同じランクの3枚のカードと、別のランクの2枚のカード
- フラッシュ: 同じスートの5枚のカード
- ストレート: 連続する5枚のカード
- スリーカード: 同じランクの3枚のカードが含まれる
- ツーペア: 同じランクの2枚のカードと、別の同じランクの2枚のカードが含まれる
- ワンペア: 同じランクの2枚のカードが含まれる
- ハイカード: その他

The player with the strongest hand is the winner. There are 9 types of hands based on strength. If more than one hand meets the requirements, the strongest hand will be preferred. The hand types in the order of strength are as follows:

- Straight flush: Five consecutively ranked cards of the same suit
- Four of a kind: Four cards of the same rank
- Full House: Three cards of the same rank along with two cards of another rank
- Flush: Five cards of the same suit
- Straight: Five consecutively ranked cards
- Three of a kind: Three cards of the same rank
- Two Pairs: Two cards of the same rank along with another two cards of a different same rank
- One Pair: Two cards of the same rank
- High Card: Any other hand

複数のプレイヤーが同じ種類の手役を作った場合、カードのランクを比較して勝敗を決定します。基本的に役の構成要素のランクを比較して勝敗を判定し、それでも勝敗が決まらない場合は残ったカードをランクの高い順に辞書順に比較します。

- ストレートフラッシュ: 最高ランクを比較します
- フォーカード: 4枚のカードのランクを比較し、次に残りの1枚のランクを比較します
- フルハウス: 3枚のカードのランクを比較し、次に2枚のカードを比較します
- フラッシュ: すべてのランクを高い順に辞書順比較します
- ストレート: 最高ランクを比較します
- スリーカード: 3枚のカードのランクを比較し、次に残りの2枚を比較します
- ツーペア: 上位ランクの2枚、下位ランクの2枚、残りの1枚の順に比較します
- ワンペア: 2枚を比較し、次に残りの3枚を比較します。
- ハイカード: すべてのランクを高い順に辞書順比較します

If two or more players have the same kind of hand, the winner is determined by comparing the ranks of the cards as follows. The ranks of the cards consisting of the hand type are compared first. If no winner emerges, the remaining cards are compared in lexicographic order of rank.

- Straight flush: Compare the highest-ranked card.
- Four of a kind: Compare the four cards, then the remaining one.
- Full house: Compare the three cards, then the pair.
- Flush: Compare all cards in lexicographic order.
- Straight: Compare the highest-ranked card.
- Three of a kind: Compare the three cards, then the remaining two in lexicographic order.
- Two pairs: Compare the higher-ranked pair, then the lower-ranked, then the last one.
- One pair: Compare the pair, then the remaining three in lexicographic order.
- High card: Compare all cards in lexicographic order.

なお、Aは1または14のいずれのランクとしても考えることができるため、以下のストレートの判定について注意してください。

- [A, K, Q, J, 10] はエースを14としてみなした場合にストレートの手役となり、最高ランクは14です。
- [5, 4, 3, 2, A] はエースを1としてみなした場合にストレートの手役となり、最高ランクは5です。

これまでの判定を適用しても勝敗が決まらなかった場合は引き分け (つまり勝利できなかった) と判定します。

Rank A can be considered 1 or 14, so the following situations should be noted:

- [A, K, Q, J, 10] is a straight when A is considered 14 and the highest rank is 14.
- [5, 4, 3, 2, A] is a straight when A is considered 1 and the highest rank is 5.

If the above rules do not result in a winner, the game is considered a draw (i.e., the user didn't win).

## 実装の詳細 / Implementation

### 入力ルール / Input Rules

このプログラムに、以下のフォーマットの標準入力が与えられます。

The standard input format is as below:

C<sub>1,1</sub> ... C<sub>1,5</sub><br>
:<br>
C<sub>6,1</sub> ... C<sub>6,5</sub><br>
K

先頭の6行に、各プレイヤーに配られた手札がそれぞれ1行ずつ与えられ、1行目はあなたの交換前の手札を表しています。
各行は5枚のカードが半角空白区切りで与えられ、各カードは2字の半角英数字で表現されます。
カードの1字目はスートを表し、`'S'`, `'H'`, `'D'`, `'C'` のいずれかです。
カードの2字目はランクを表し、`'A'`, `'K'`, `'Q'`, `'J'`, `'T'`, `'9'`, `'8'`, `'7'`, `'6'`, `'5'`, `'4'`, `'3'`, `'2'` のいずれかです。`'T'` は 10 を表します。
末尾にはあなたが交換できるカードの枚数の最大値を表す 0 以上 5 以下の整数がひとつ与えられます。

The first six lines each contain a line with cards dealt to each player. The first line signifies your hand before the exchange. 
Each line contains five cards, each separated by spaces. The cards are represented by two alphanumeric characters.
The first character of a card represents a suit and is one of `'S'`, `'H'`, `'D'`, or `'C'`.
The second character of a card represents the rank and is one of `'A'`, `'K'`, `'Q'`, `'J'`, `'T'`, `'9'`, `'8'`, `'7'`, `'6'`, `'5'`, `'4'`, `'3'` or `'2'`. `'T'` denotes 10.
The last line contains an integer between 0 and 5, representing the maximum number of cards you can exchange.

### 出力ルール / Output Rules
1行目に勝率の最大値を出力してください。勝率は、他の全てのメンバーに勝利する確率で定義されます。**引き分けは勝利に含まれません。** 
2行目以降には勝率が最大となる交換を表す文字列を全て1行ずつ辞書順に出力してください。
それぞれの交換は、元の手札を表す文字列のうち、交換する手札を `'**'` に置き換えて得られる文字列で表します。

On the first line, output the maximum winning rate, defined as the probability of that the hands you get are stronger than any other members *excluding tie-break* after the exchange phase.
On the second and subsequent lines, output the string representing the exchange (if any) with the maximum winning rate, one line at a time, in lexicographic order.
Each exchange is represented by the string obtained by replacing each card to be exchanged with `'**'` in the string representing the original hand.

### 得点 / Score
K=0 のテストケースは全体の約40%を占めており、勝敗判定のロジックのテストに利用してください。
また、各テストケースの正誤判定時には、10<sup>-7</sup> までの計算誤差が許容されます。

Test cases where K=0 constitute around 40% of all test cases. These cases are particularly useful for testing the logic used in deciding wins or losses.
It should also be noted that a computational error of up to 10<sup>-7</sup> is permissible.

## 入出力例 / Input & Output samples
### 例 1 / Sample 1
標準入力 / Sample Input (`00_sample001.in`)
```plain
D4 DK SK DT S4
D6 C3 D8 D2 S6
SQ HJ D7 D5 C5
C6 S9 H3 D9 CK
H7 CQ DJ H4 S7
D3 H5 CA H9 C8
0
```

標準出力 / Sample Output
```plain
1.000000000000
D4 DK SK DT S4
```

### 例 2 / Sample 2
標準入力 / Sample Input (`00_sample002.in`)
```plain
CA C4 C2 HQ S9
S2 S8 DT H3 D8
CK HK H8 S5 D6
D5 C6 D7 DQ H6
HT D4 C3 H7 HJ
C7 C9 DA S7 CQ
0
```

標準出力 / Sample Output
```plain
0.000000000000
CA C4 C2 HQ S9
```

### 例 3 / Sample 3
標準入力 / Sample Input (`00_sample003.in`)
```plain
D8 H3 D9 S5 S3
C3 SQ C8 D7 D6
S4 C7 CJ C4 C5
DK DT C9 SK C6
H6 D4 DQ H7 H8
H4 HK HA C2 HQ
5
```

標準出力 / Sample Output
```plain
0.316017316017
** H3 ** S5 S3
** H3 D9 ** S3
```
