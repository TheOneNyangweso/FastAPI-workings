from fastapi import FastAPI, Body, Header
import asyncio

app = FastAPI()


@app.post('/hello/{name}')
async def get_credentials(name, age: str = Header(embed=True)):
    await asyncio.sleep(10)
    return {'message': f'Hello {name}, you are {age} years old'}

# def doh2():
#     yield "Homer: D'oh!"
#     yield "Marge: A deer!"
#     yield "Lisa: A female deer!"


# async def q():
#     print("Why can't programmers tell jokes?")
#     await asyncio.sleep(3)


# async def a():
#     print('Timing!')


# async def main():
#     await asyncio.gather(q(), a())

# asyncio.run(main())
