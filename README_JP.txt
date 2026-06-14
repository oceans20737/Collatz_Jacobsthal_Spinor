# **Jacobsthal正規化スピノル表現によるCollatz写像の再構成**
**(Reconstruction of the Collatz Mapping via Jacobsthal-Normalized Spinor Representation)**

Hiroshi Harada - June 14, 2026  

## **概要**
本プロジェクトは、Collatz予想（$3n+1$問題）における奇数核の遷移を、従来の「$3n+1$ 演算と $2^c$ 除算」という手続き的操作から脱却し、**Jacobsthal正規化された2成分離散スピノル（J-spinor）の線形遷移**として完全に再定義するものです。

任意の奇数核 $N_{\mathrm{current}}$ は以下のJ-spinor $J_c(a,b)$ として一意に表現され、次相への遷移は単純な波源の和 $N_{\mathrm{next}} = a+b$ によって決定論的に導かれます。

## **収録内容 (Contents)**
- `REPORT_EN.md` / `REPORT_JP.md` : 本論の数学的証明と解説レポート
- `collatz_jacobsthal_spinor.py` : 任意の初期値 $n$ に対するJ-spinor軌道生成および可視化スクリプト
- `collatz_jacobsthal_spinor_n7.csv` 等 : 生成された軌道の完全なJ数列データセット
- `collatz_jacobsthal_spinor_n7.png` 等 : 2進対数らせん空間（2-adic logarithmic spiral space）におけるJacobsthal路線の可視化プロット

## **実行方法 (Usage)**
Python 3.x環境で以下のスクリプトを実行すると、指定した初期値に対するCSVデータと高解像度PNG画像がカレントディレクトリに生成されます。

```bash
# 依存ライブラリのインストール
pip install numpy matplotlib pandas

# スクリプトの実行
python collatz_jacobsthal_spinor.py

```

※ スクリプト末尾の `generate_artifacts(n)` の引数を変更することで、任意の初期値の軌道を解析可能です。

## **ライセンス (License)**

* **Research Documents & Artifacts**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* **Python Source Code**: [MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2026 Hiroshi Harada
