import asyncio

import requests

from api.path import URL  # https://fapi.binance.com/fapi/v1/ticker/price?symbol=XRPUSDT


max_price = 0


async def droppedMaxPrice(current_price):
    await asyncio.sleep(1)
    print(
            f'\nThe price of XRP/USDT has dropped by 1% of the maximum price in the last hour.\n'
            f'Current price: {current_price}\n'
            f'Max price: {max_price}\n'
    )


async def maxPriceValue(current_price):
    global max_price

    if current_price > max_price:
        max_price = current_price
        # await asyncio.sleep(1)
        # print(f'Max Price updated to {current_price}')

    if (max_price - current_price) / max_price >= 0.01:
        await droppedMaxPrice(current_price)


async def main():
    try:
        while True:
            response = requests.get(URL)
            current_price = float(response.json()['price'])

            # await asyncio.sleep(1)
            # print(f'Current price: {current_price}')

            max_price_value = asyncio.create_task(maxPriceValue(current_price))

            await max_price_value

    except Exception as e:
        return e


asyncio.run(main())