## Тестовое задание на Python-разработчик (Junior)

## Задания: 

1. Напишите код программы на Python, которая будет в реальном времени (с максимально возможной скоростью) считывать текущую цену фьючерса XRP/USDT на бирже Binance. 
В случае, если цена упала на 1% от максимальной цены за последний час, программа должна вывести сообщение в консоль. 
При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.

2. Опишите, как бы вы доработали данную программу, чтобы она обрабатывала все пары, а не только XRP/USDT (код писать не нужно, просто текстом)

## Мое решение

1. Первый таск вы можете увидеть основной код в source repository: `./app/main.py`.
А также в папке api хранятся: `Api Key`, `Secret Key`, а также `request url`.
Здесь я не использовал `keys`, но подумал, пусть стоит)
`Request url`, которому отправил `GET` запрос, был предоставлен биржей Binance.
Давайте перейдем в `main.py`, что мы видим? Приложение является асинхронным, почему же я решил написать его так? Подумал, что если нам нужно каждый раз получать текущую цену и в то же время считывать максимальную цену и цену, когда максимальная цена на 1% больше текущей цены, то как раз так и приложение под капотом должно работать асинхронно.

2. Теперь нам определенно понадобится асинхронное приложение) Без него, думаю, никак не можем реализовать эту задачку. Нам нужно написать алгоритм, в котором цены всех пар под капотом будут считываться независимо. И каждый раз, когда максимальная цена любой пары увеличивается на 1% от текущей цены (текущая цена ниже на 1% от максимальной цены), нам нужно будет выводить сообщение на консоль. Мы запускаем здесь итератор, чтобы просмотреть все фьючерсы и, в частности, прайс-лист. Также нужен Join по ID фьючерс. Все это должно занять как минимум O(n * log(m)) времени. Или, может быть, я ответил поспешно) Может быть, есть другой способ.

На этом у меня всё. Спасибо за интересное задание и за полученный опыт!)
