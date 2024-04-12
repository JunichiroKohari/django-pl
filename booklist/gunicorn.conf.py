import multiprocessing

# ワーカー数を「(コア数 x 2) + 1」に設定
workers = multiprocessing.cpu_count() * 2 + 1
# accesslogに`-`を指定すると、出力先が標準出力になる
accesslog = "-"
wsgi_app = "booklist.wsgi"
