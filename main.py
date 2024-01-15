import asyncio

from highrise import *
from highrise import BaseBot, Position, __main__
from highrise.models import *
from highrise.models import (
    Position,
    SessionMetadata,
)
import random
from webserver import keep_alive

name_ad = ["_e_rr_o_r_"]
class BotDefinition:
    def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token
      self.following_username = None


class MyBot(BaseBot):
    greetings = [ "الأوامر: نزلني  طلعني  وزني  طولي . طيرني \U0001F497\U0001F525" , 
   "Commands: dance or emote or up or down or weight or Length or fly \U0001F497\U0001F525",
    # ... (other greetings here)
]


    dances = [ "emote-tired", "emoji-thumbsup", "emoji-angry", "dance-macarena",
    "emote-hello","dance-weird", "emote-superpose", "idle-lookup", "idle-hero", "emote-wings",
    "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes", "emote-theatrical",
    "emote-teleporting", "emote-slap", "emote-ropepull", "emote-think", "emote-hot",
    "dance-shoppingcart", "emote-greedy", "emote-frustrated", "emote-float", "emote-baseball",
    "emote-yes", "idle_singing", "idle-floorsleeping", "idle-enthusiastic", "emote-confused",
    "emoji-celebrate", "emote-no", "emote-swordfight", "emote-BUMMED", "emote-shy", "dance-tiktok2", "emote-model",
    "emote-charging", "emote-snake", "dance-russian", "emote-sad", "emote-lust", "emoji-cursing",
    "emoji-flex", "emoji-gagging", "dance-tiktok8", "dance-blackpink", "dance-pennywise",
    "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis",
    "emote-maniac", "emote-energyball", "emote-frog", "emote-cute", "dance-tiktok9", "dance-tiktok10",
    "emote-pose7", "emote-pose8","idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5",
    "emote-cutey", "emote-Relaxing", "emote-model", "emote-cursty", "emote-Rest", "emote-zero gavity" , "emote-LEVITATE" , "emote-FAINT" , "idle-Attentive" , "emote-NAUGHTY" , "dance-PROPOSING", "dance-FALL" ,"idle-Rest" , "emote-Confusion","dance-SAY SO DANCE"
    # ... (أنواع الرقصات هنا)
    ]

    message_count = {}
    def __init__(self, bot, room_id, api_token):
      self.bot = bot
      self.room_id = room_id
      self.api_token = api_token
      self.following_username = None
      super().__init__()
      self.user_positions = {}
      self.is_dancing = False
    
    



    async def on_start(self, session_metadata: SessionMetadata) -> None:
      print("hi im alive?")
      try:
        await self.highrise.walk_to( Position(x=3.2, y=0, z=1.7, facing='FrontRight'))
      except Exception as e:
        print(f"An exception occurred: {e}")



    





    

      # If no matching function is found
      

    
    

    

    

    async def on_whisper(self, user: User, message: str) -> None:
         print(f"{user.username} whispered: {message}")

    async def on_user_join(self, user: User) -> None:
       greeting = random.choice(self.greetings)
       await self.highrise.chat(f"{greeting}، {user.username}!")

    # تشغيل رقصة عند دخول المستخدم
       try:
         emote_id = random.choice(self.dances)
         await self.highrise.send_emote(emote_id, user.id)
       except Exception as e:
        print(f"Error: {e}")

    async def on_chat(self, user: User, message: str) -> None:
        
    # ... (باقي الأوامر هنا)
      if "رقصني" or "dance" or "emote"  in message:
        try:
           emote_id = random.choice(self.dances)
           await self.highrise.send_emote(emote_id, user.id)
        except Exception as e:
          print(f"Error: {e}")


         
      elif "صعدني"or"up"or"طلعني" in message:
        try:
            await self.highrise.teleport(f"{user.id}", Position(1, 7,1))
        except Exception as e:
            print(f"Error: {e}")

      elif "نزلني"or"down" in message:
        try:
            await self.highrise.teleport(f"{user.id}", Position(1, 0,1))
        except Exception as e:
            print(f"Error: {e}")

      elif "طولي"or"Length" in message:
        try:
            height_cm = random.randint(110, 199)
            await self.highrise.chat(f"{user.username} طولك {height_cm} سنتيمتر!")
        except Exception as e:
            print(f"Error: {e}")
      elif "وزني" or "weight" in message:
        try:
            weight_kg = random.randint(35, 150)
            await self.highrise.chat(f"{user.username} وزنك {weight_kg} كيلوجرام!")
        except Exception as e:
            print(f"Error: {e}") 

    async def run(self):
       while True:  
        try:
         definitions = [BotDefinition(self, self.room_id, self.api_token)]
         await __main__.main(definitions)
        except Exception as e:
         print(f"An exception occourred: {e}")

keep_alive()
if __name__ == "__main__":
    room_id = "6568b3b3976fac32224a4d24"
    token = "d1a59ce464c58cad73899b6072a4ba5b1ebfa7949c4eacb70f849809c9f08b66" 
    bot = Highrise() 
    bot_instance = MyBot(bot, room_id, token)
    asyncio.run(bot_instance.run())
