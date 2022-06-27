import re

url = "https://www.banco.com.br/cambio"
padrao_url = re.compile("(http(s)?://)?(www.)?banco.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL é inválida!")

print("A URL é válida!")
