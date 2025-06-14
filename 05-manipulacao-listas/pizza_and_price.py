# lista de coberturas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# lista de precos
prices = [2, 6, 1, 3, 2, 7, 2]

# conta quantas pizzas custam 2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# conta quantos tipos de pizza existem
num_pizzas = len(toppings)
print(f'We sell {num_pizzas} different kinds of pizza!')

# junta preco e cobertura
pizza_and_prices = [list(item) for item in zip(prices, toppings)]
print(pizza_and_prices)

# ordena do mais barato pro mais caro
pizza_and_prices.sort()
print(pizza_and_prices)

# armazena a pizza mais barata
cheapest_pizza = pizza_and_prices[0]

# armazena a pizza mais cara
priciest_pizza = pizza_and_prices[-1]

# remove a pizza mais cara
pizza_and_prices.pop()

# adiciona nova pizza com peppers
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# seleciona as 3 mais baratas
three_cheapest = pizza_and_prices[:3]
print(f'tres pizzas mais barata: {three_cheapest}')