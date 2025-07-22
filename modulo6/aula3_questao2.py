

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = [url[4:-4] for url in urls]  # remove os 4 primeiros e 4 últimos caracteres

print("dominios:", dominios)
