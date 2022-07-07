import asyncio


async def get_prime_amount(numb):
    sum = 0
    for n in numb:
        counter = 0
        for num in range(1, n):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                sum += 1
                counter += 1
        print(counter)
        await asyncio.sleep(0)
    print(f"obschee {sum}")


k = [10, 40, 20000, 20000]
# get_prime_amount(k)
task = [get_prime_amount(k)]
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*task))
event_loop.close()

# asyncio.run(get_prime_amount(k))
# asyncio.run(get_prime_amount(z))
