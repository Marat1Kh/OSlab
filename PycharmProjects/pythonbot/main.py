from telethon.sync import TelegramClient
from datetime import datetime, timedelta
import random
import asyncio
start_time = datetime.strptime("17:48", "%H:%M")
end_time = datetime.strptime("00:40", "%H:%M")
accounts = [
    {
        'description': 'Stark',
        'api_id': '20717788',
        'api_hash': '1fc881a36d861eb40785cffcd27d4ce7',
        'phone_number': '+447901017635',
        'message_interval': 240,
    },
    {
        'description': 'Smith',
        'api_id': '23222961',
        'api_hash': '99cec6919544283ba7dcf9af376131dc',
        'phone_number': '+447442225176',
        'message_interval': 260,
    },

    {
        'description': 'Jackie',
        'api_id': '26583423',
        'api_hash': '2a9e453fef13d592098fe89eda940309',
        'phone_number': '+447300567870',
        'message_interval': 410,
    },
    {
        'description': 'Jax',
        'api_id': '25075193',
        'api_hash': 'c964eccd824242ea9f6ebffd42d247eb',
        'phone_number': '+447951767586',
        'message_interval': 210,
    },
    {
        'description': 'Luka',
        'api_id': '24216686',
        'api_hash': '2d4a8825b9a19eca6c5c8d54ac22c3d9',
        'phone_number': '+447944269387',
        'message_interval': 210,
    },
    {
        'description': 'Rim',
        'api_id': '26686443',
        'api_hash': '2d4a8825b9a19eca6c5c8d54ac22c3d9',
        'phone_number': '+447551553729',
        'message_interval': 410,
    }

]

receiver_username = '@makokinhoo'  # or receiver phone number

# List of random messages without indexes
random_messages = [
      "hello everyone",
    "have a good day",
    "have a good evening with rush!",
    "28000 coins and counting :) :)",
    "coool man keep grinding",
    "game is actually greaat",
    "guys if u guys ever get any bugs or errors write here, so admins tell to devs and they fix it ASAP",
    "yeee right",
    "anyone got new cars?",
    "cars are super expensive hahah",
    "I am with fast car now:P",
    "taxi enjoyer :P",
    "no cars yet.... default one",
    "ggwp's",
    "then how about weapons?",
    "flamethrower like we expected buffed weapon kinda META xd",
    "yeeeah flmaethrower just different than others but damage seems less no?",
    " I felt that too but range is really good enough",
    "agree guys",
    "dont buy mini gun it sucks ....",
    "laser gun is the best option",
    "minigun has too less damage but more ammo xd",
    "just buy laser gun guys ....",
    "hahahaha its expensive maaan wtf",
    "tryhard hustle haha",
    "https://dmission.me/missions/undeads-airdrop?via=0ukuvs81 airdrop link guys",
    "coool",
    "how to change username, why its random name though?",
    "u can change it on user settings, /app/settings",
    "loving the variety in weapons, adds real strategic depth",
    "really love it",
    "gives the game and edge fore real",
    "cars handle like a dream, perfect for swift getaways",
    "agree, its like driving through choas and precision",
    "makes escaping hordes a thrilling maan ((",
    "any tips about guns??",
    "shotgun for close range and smgs for mid range",
    "imo armored truck is solid option at the end xd",
    "will there be any bosses of zombies",
    "imo, there will be!",
    "hmmmm, interesting....",
    "investing points for better waepons and having good car is my opinion haha",
    "flmaethrower sounds epic",
    "hahaha solid idea!",
    "btw we have nades for more damage and more zombies to kill",
    "u mean explosives",
    "y he meant grenades like explosives hahaa",
    "laser gun!",
    "undeads.com/rush's game design nails the zombie apocalypse vibe."
    "absolutely, the atmosphere is spot-on feels apocalyptic",
    "post apocalyptic chaos :X",
    "The flamethrower is a game-changer against those hordes",
    "its like wielding controlled chaos xd",
    "vehicles are more than transportation, they're weapons on wheels",
    "for me the visuals are good and cars are your best weapon thna weapons xd",
    "vehicle combat with weapons pretty cool btw",
    "graphics are top-notch, immersing you in post-apocalyptic chaos.",
    "the visuals are pretty cool, kinda top-notch",
    "map layout keeps you on your toes, unpredictable encounters.",
    "oooh maan, never know what is around the corner fr",
    "agree bro hahahaah",
    "sniper rifles add a satisfying element of long-range precision.",
    "sharpshooter is so satisfying, strategical xd",
    "yeees!!",
    "customization options for weapons and cars are a nice touch.",
    "wait really?",
    "haha dude is jkoing around xdxd",
    "yeeeah he is jkoing lol, almost believed it xd",
    "Undeads.com/rush strikes a perfect balance of challenge and fun.",
    "challenging enough lol, hard to get coins :((((",
    "yeaah so hard ffs",
    "sadge(((("
    "the in-game economy system encourages strategic resource management.",
    "Zombie AI is smart, keeps you guessing every encounter hahahaha",
    "melee weapons feel visceral, up-close combat is intense.",
    "nothing beats that thrill of smashing that f zombies hahahh",
    "so rude maaan hahhaha",
"Love the rare, unique weapons – feels like finding treasure.",
    "lets find hidden coins :P",
    "anyone found one?",
    "naaaah not yet xd",
    "nopppeee",
    "cant find one",
    "Undeads.com/rush's sound design heightens the overall immersive experience.",
    "cars aren't just for escape; they're your mobile fortress.",
    "the crossbow is my go-to silent zombie slayer.",
    "game events keep you engaged, always something new happening.",
    "The crafting system is intuitive, enhances survival strategies.",
    "so game strikes a balance between oh shit and fun hahaha",
    "Character progression system keeps you invested in the apocalypse.",
    "diverse zombie types keep combat fresh and challenging(((("
    "game delivers on the promise of adrenaline-pumping action, love it!"
    "Love the hidden easter eggs scattered throughout the game world.",
    "Dynamic weather effects amp up the tension during gameplay.",
    "game  proves that survival can be stylish and thrilling.",
    "Sniper rifles add a satisfying element of long-range precision."
]
# Initialize a dictionary to keep track of sent messages for each account
sent_messages = {account['description']: [] for account in accounts}

async def send_message_from_account(account_info, message, sent_messages):
    async with TelegramClient(account_info['phone_number'], account_info['api_id'], account_info['api_hash']) as client:
        await client.send_message(receiver_username, message)
        print(f"Message sent from {account_info['description']} to {receiver_username}: {message}")
        # Update the sent messages for this account
        sent_messages[account_info['description']].append(message)

async def wait_until_start_time():
    current_time = datetime.now().time()

    while current_time < start_time.time():
        print(f"Waiting until {start_time.time()} to start...")
        await asyncio.sleep(60)  # Wait for 1 minute before checking again
        current_time = datetime.now().time()

async def main():
        await wait_until_start_time()

        account_count = len(accounts)
        message_count = len(random_messages)
        sent_message_count = 0

        while sent_message_count < message_count:
            random.shuffle(accounts)
            accounts_order = list(range(account_count))

            for account_index in accounts_order:
                if sent_message_count >= message_count:
                    break

                account_info = accounts[account_index]
                message_index = sent_message_count % message_count
                message_text = random_messages[message_index]

                if message_text not in sent_messages[account_info['description']]:
                    await send_message_from_account(account_info, message_text, sent_messages)
                    sent_message_count += 1
                    await asyncio.sleep(account_info['message_interval'])

if __name__ == "__main__":
    asyncio.run(main())