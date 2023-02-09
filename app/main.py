import asyncio
import requests

from api.path import URL  # https://fapi.binance.com/fapi/v1/ticker/price?symbol=XRPUSDT


max_price = 0


async def updatedMaxPrice(current_price):
    global max_price

    if current_price > max_price:
        max_price = current_price
        await asyncio.sleep(1)
        print(f'Max Price updated to {current_price}')


async def droppedMaxPrice(current_price):
    global max_price

    if (max_price - current_price) / max_price >= 0.0001:
        await asyncio.sleep(1)
        print(
            f'\nThe price of XRP/USDT has dropped by 1% of the maximum price in the last hour.\n'
            f'Current price: {current_price}\n'
            f'Max price: {max_price}\n'
            )


async def main():
    while True:
        response = requests.get(URL)
        current_price = float(response.json()['price'])

        await asyncio.sleep(1)
        print(f'Current price: {current_price}')

        await asyncio.create_task(updatedMaxPrice(current_price))
        await asyncio.create_task(droppedMaxPrice(current_price))


asyncio.run(main())