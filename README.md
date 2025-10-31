# 💰 Monitor de Preço do Bitcoin — API CoinMarketCap

Este projeto em **Python** monitora o preço do **Bitcoin (BTC)** em **reais (BRL)** em tempo real, usando a **API do site [CoinMarketCap](https://coinmarketcap.com/)**.  
O script compara o preço atual com o último registrado e envia **alertas automáticos** quando há variações significativas.

---

## 🚀 Funcionalidades
- Consulta o preço do Bitcoin diretamente da **API CoinMarketCap**.  
- Exibe o preço formatado em reais (ex: `R$ 345.678,90`).  
- Calcula automaticamente a **variação percentual** desde o último preço.  
- Envia **notificações no computador** (via `plyer`) quando:
  - 💹 O preço **sobe** acima do limite definido.
  - 📉 O preço **cai** abaixo do limite definido.
- Atualiza a cada poucos segundos.

---

## ⚙️ Tecnologias usadas
- **Python 3**  
- **requests** — para acessar a API.  
- **plyer** — para criar notificações no desktop.  
- **CoinMarketCap API** — fonte oficial dos preços em tempo real.

---

## 📦 Como usar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/monitor-bitcoin.git
cd monitor-bitcoin
