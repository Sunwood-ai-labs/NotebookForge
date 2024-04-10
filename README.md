

<p align="center">
<img src="docs/NotebookForge_icon.png" width="100%">
<br>
<h1 align="center">NotebookForge</h1>
<h2 align="center">

</p>

setup

conda create -n notebook-forge python=3.11 
conda activate notebook-forge


マークダウンファイルをノートブックに変換するツールです。


コードブロックがあるマークダウンファイルを用意
example.md

変換
python create_jupyter_notebook.py 

出力ファイル
example.ipynb