import asyncio

async def hello(): # native coroutine
    print("hello")

loop = asyncio.get_event_loop() # get event loop
loop.run_until_complete(hello()) # wait until hello() done
loop.close()

# 먼저 async def로 hello를 만듭니다. 그다음에 asyncio.get_event_loop 함수로 이벤트 루프를 얻고 
# loop.run_until_complete(hello())와 같이 run_until_complete에 코루틴 객체를 넣습니다(네이티브 코루틴을 호출하면 코루틴 객체가 생성됩니다).

