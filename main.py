import asyncio
from pytgcalls import idle
from config import call_py
from MusicAndVideo.play import arq
async def main():
    await call_py.start()
    print(
        """
    ------------------
   | ميوزك تليثون الان شغال ! |
    ------------------
"""
    )
    await idle()
    await arq.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
