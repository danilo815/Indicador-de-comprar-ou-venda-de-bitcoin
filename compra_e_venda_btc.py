import requests
import time
from plyer import notification

api_key = "SUA_CHAVE_AQUI"
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
parametros = {"symbol": "BTC", "convert": "BRL"}
headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": api_key}

resposta = requests.get(url, headers=headers, params=parametros)

if resposta.status_code == 200:
    print("Sucesso")
    dados = resposta.json()
    preco = dados["data"]["BTC"]["quote"]["BRL"]["price"]
    print("Preço atual:", preco)
else:
    print("Erro no código ou na API:", resposta.status_code)


ALERTA_PERCENT = 0.01
ultimo_preco = None  # Aqui vamos guardar o último preço






while True:
    try:
        # Pegar preço da API
        resposta = requests.get(url, headers=headers, params=parametros, timeout=10)
        resposta.raise_for_status()  
        dados = resposta.json()
        preco_atual = dados["data"]["BTC"]["quote"]["BRL"]["price"]

        # Formatar preço para R$ 1.234.567,89
        preco_formatado = f"R${preco_atual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Comparar com o último preço e calcular variação
        if ultimo_preco is not None:
            variacao = ((preco_atual - ultimo_preco) / ultimo_preco) * 100

            if preco_atual > ultimo_preco:
                print(f"Preço subiu! Variação: +{variacao:.2f}%")
            elif preco_atual < ultimo_preco:
                print(f"Preço caiu! Variação: {variacao:.2f}%")
            else:
                print("Preço igual. Variação: 0%")

            # Disparar alertas
            if variacao >= ALERTA_PERCENT:
                print(f"💹 Alerta: preço subiu {variacao:.2f}%! Considere vender.")
                notification.notify(
                    title="💹 Alerta Bitcoin",
                    message=f"Preço atual: {preco_formatado}\nVariação: +{variacao:.2f}%",
                    timeout=10
                )
            elif variacao <= -ALERTA_PERCENT:
                print(f"📉 Alerta: preço caiu {variacao:.2f}%! Considere comprar.")
                notification.notify(
                    title="📉 Alerta Bitcoin",
                    message=f"Preço atual: {preco_formatado}\nVariação: {variacao:.2f}%",
                    timeout=10
                )

        # Atualizar o último preço
        ultimo_preco = preco_atual

        # Mostrar preço atual
        print(f"💰 Preço atual do Bitcoin: {preco_formatado}")

    except requests.exceptions.RequestException as e:
        print("Erro ao consultar API:", e)

    # Espera 60 segundos antes da próxima verificação
    time.sleep(2)


