# lista de cortes
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# precos dos cortes
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# quantas vezes cada corte foi feito na ultima semana
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# calcula preco medio
total_price = 0
for preco in prices:
    total_price += preco
average_price = total_price / len(prices)
print(f'Preco medio do corte: {average_price}')

# aplica desconto de 5 em todos os cortes
new_prices = [corte - 5 for corte in prices]
print(new_prices)

# calcula receita total da semana
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f'Receita total: {total_revenue}')

# receita media por dia
average_daily_revenue = total_revenue / 7
print(f'Receita media diaria: {average_daily_revenue}')

# cortes com preco novo abaixo de 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(f'Cortes com preco abaixo de 30: {cuts_under_30}')