# 研究室 開発環境チュートリアル

このリポジトリは、研究室のGPUサーバー上で開発を始めるための**練習用プロジェクト**です。

大学3年生が初めて研究室の開発環境を使うことを想定しています。Pythonの内容を学ぶことよりも、次の一連の流れを一度経験することが目的です。

- VS Codeから研究室サーバーへ接続する
- GitHubからプロジェクトをcloneする
- Dev Containerで開く
- `uv sync` でPython環境を準備する
- Pythonプログラムを実行する
- RuffとtyによるVS Code上の支援を確認する
- `uv add` / `uv remove` でライブラリを追加・削除する
- Jupyter Notebookを開く
- Gitで変更内容を確認してcommitする

> このリポジトリは研究室標準の構成例です。外部の研究コードを使う場合は、まずそのリポジトリのREADMEやセットアップ手順を優先してください。

## 1. リポジトリをcloneする

VS Codeから研究室サーバーへRemote SSHで接続したあと、ターミナルで作業したいディレクトリへ移動し、次を実行します。

```bash
git clone https://github.com/tatsylab/dev-tutorial.git
cd dev-tutorial
```

その後、VS Codeで `dev-tutorial` フォルダを開いてください。

## 2. Dev Containerで開く

VS Codeのコマンドパレットから

```text
Dev Containers: Reopen in Container
```

を選びます。

初回はコンテナの準備に少し時間がかかることがあります。コンテナが開いたら、VS Codeのターミナルで次を確認してください。

```bash
python --version
uv --version
nvidia-smi
```

Pythonとuvのバージョンが表示され、`nvidia-smi` でGPUの情報が見えれば基本的な環境は動いています。

## 3. Python環境を準備する

次を実行します。

```bash
uv sync
```

この操作で、プロジェクト専用のPython環境 `.venv/` が作成されます。

`.venv/` は自動生成されるためGitでは管理しません。プロジェクトに必要な情報は `pyproject.toml` と `uv.lock` に保存します。

## 4. Pythonプログラムを実行する

次を実行してください。

```bash
uv run python hello.py
```

次のようなメッセージが2行表示されれば成功です。

```text
Hello from the Tatsy Lab development environment!
Hello from the Tatsy Lab development environment!
```

`uv run` を使うと、そのプロジェクトの `.venv/` を使ってコマンドを実行できます。

## 5. テストを実行する

このチュートリアルでは、外部ライブラリを追加しなくても実行できる小さなテストを用意しています。

```bash
uv run python -m unittest discover -s tests -v
```

`OK` と表示されれば成功です。

## 6. Ruffとtyを確認する

`hello.py` をVS Codeで開いてみてください。

研究室のDev Containerでは、Pythonコードの整形とLintにRuff、型チェックにtyを使います。これらはVS Code拡張として設定されているため、通常はコマンドを覚える必要はありません。

### Ruff

`hello.py` の空白や改行を少し崩してから保存してみてください。保存時にRuffによる整形が適用されます。

### ty

例えば一時的に、`hello.py` の

```python
print(repeat_message(message, 2))
```

を

```python
print(repeat_message(message, "2"))
```

に変更すると、`count` に文字列を渡しているためVS Code上で型の問題が表示されます。

確認したら、元の `2` に戻して保存してください。

## 7. ライブラリの追加と削除を試す

研究室内のPythonプロジェクトでは、通常 `pip install` を直接使わず、`uv add` を使います。

例としてNumPyを追加します。

```bash
uv add numpy
```

追加できたら、次を実行します。

```bash
uv run python -c "import numpy as np; print(np.arange(5))"
```

`[0 1 2 3 4]` と表示されれば成功です。

Gitの差分も確認してみてください。

```bash
git diff -- pyproject.toml uv.lock
```

`pyproject.toml` と `uv.lock` が更新されていることが分かります。

今回は練習なので、NumPyを削除して元に戻します。

```bash
uv remove numpy
```

## 8. Jupyter Notebookを試す

Notebookを実行するためのパッケージを開発用依存関係として追加します。

```bash
uv add --dev ipykernel
```

次に、VS Codeで

```text
notebooks/example.ipynb
```

を開き、Kernelとしてこのプロジェクトの `.venv` を選んでセルを実行してください。

動作を確認したら、今回追加したパッケージは削除して構いません。

```bash
uv remove --dev ipykernel
```

## 9. Gitで変更を確認する

最後に `hello.py` の表示メッセージを好きな文章に変更してみてください。

変更後、まず状態と差分を確認します。

```bash
git status
git diff
```

内容を確認したらcommitしてみます。

```bash
git add hello.py
git commit -m "Practice editing the tutorial program"
```

これは自分のclone内でGitの操作を練習するためのcommitなので、GitHubへpushする必要はありません。

## ここまでできればOK

次の内容を一度経験できていれば、このチュートリアルの目的は達成です。

- [ ] Remote SSHで研究室サーバーへ接続した
- [ ] GitHubからリポジトリをcloneした
- [ ] Dev Containerでプロジェクトを開いた
- [ ] `uv sync` を実行した
- [ ] Pythonプログラムとテストを実行した
- [ ] Ruffとtyの動作を確認した
- [ ] `uv add` / `uv remove` を試した
- [ ] Jupyter Notebookを実行した
- [ ] `git status` / `git diff` / `git commit` を試した

実際の研究では、リポジトリごとにプログラムの構成や必要なライブラリは異なります。ただし、研究室で管理するPythonプロジェクトでは、**Dev Container + uv + VS Code** を基本の開発環境として使います。
