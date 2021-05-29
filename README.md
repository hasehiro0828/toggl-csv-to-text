# toggl-csv-to-text

[toggl track](https://toggl.com/track/) の csv をいい感じにフォーマットするスクリプト

# 環境構築

python の環境構築は[MacBook Pro (13-inch, M1, 2020)を買ったらやったこと(2021/02/11)](https://qiita.com/hasehiro0828/items/d8f1dd2a72c7999c9b76#python)を参照

```bash
pyenv install 3.9.5
pyenv local 3.9.5
poetry install
rm -f .python-version
poetry run python main.py csv/[filename]
```
