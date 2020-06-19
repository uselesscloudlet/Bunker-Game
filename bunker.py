import discord as ds
import random
from token_info import return_TOKEN

TOKEN = return_TOKEN()
#722571695755362522 test id
#630845143557341194 konoha id
CHANNEL_ID = 722571695755362522
IN_GAME = False

class Player(object):
    def __init__(self, s_bio_char, s_human_qual, s_proffesion, s_hobby, s_health, s_phobia, s_baggage, s_add_info, s_card_f, s_card_s):
        """Constructor"""
        self.s_bio_char = s_bio_char
        self.s_human_qual = s_human_qual
        self.s_proffesion = s_proffesion
        self.s_hobby = s_hobby
        self.s_health = s_health
        self.s_phobia = s_phobia
        self.s_baggage = s_baggage
        self.s_add_info = s_add_info
        self.s_card_f = s_card_f
        self.s_card_s = s_card_s

def randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories):
    bio_char_id = random.randint(0, len(bio_characteristics) - 1)
    human_qual_id = random.randint(0, len(human_qualities) - 1)
    profession_id = random.randint(0, len(professions) - 1)
    hobby_id = random.randint(0, len(hobbys) - 1)
    health_id = random.randint(0, len(health) - 1)
    phobia_id = random.randint(0, len(phobias) - 1)
    baggage_id = random.randint(0, len(baggage) - 1)
    add_info_id = random.randint(0, len(add_info) - 1)
    first_card_id = random.randint(0, len(card_categories) - 1)
    second_card_id = random.randint(0, len(card_categories) - 1)
    player = Player(s_bio_char=bio_characteristics[bio_char_id],
                    s_human_qual=human_qualities[human_qual_id],
                    s_proffesion=professions[profession_id],
                    s_hobby=hobbys[hobby_id],
                    s_health=health[health_id],
                    s_phobia=phobias[phobia_id],
                    s_baggage=baggage[baggage_id],
                    s_add_info=add_info[add_info_id],
                    s_card_f=card_categories[first_card_id],
                    s_card_s=card_categories[second_card_id])
    del professions[profession_id]
    return player

# part of initialization
def fill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories):
    file = open('resources/bio_characteristics.txt', 'r', encoding='UTF-8') # биологические характеристики
    for line in file:
        bio_characteristics.append(line)
    file.close()

    file = open('resources/human_qualities.txt', 'r', encoding='UTF-8') # человеческие качества
    for line in file:
        human_qualities.append(line)
    file.close()
    
    file = open('resources/professions.txt', 'r', encoding='UTF-8') # професссии
    for line in file:
        professions.append(line)
    file.close()

    file = open('resources/hobbys.txt', 'r', encoding='UTF-8') # хобби
    for line in file:
        hobbys.append(line)
    file.close()

    file = open('resources/health.txt', 'r', encoding='UTF-8') # здоровье
    for line in file:
        health.append(line)
    file.close()

    file = open('resources/phobias.txt', 'r', encoding='UTF-8') # фобии
    for line in file:
        phobias.append(line)
    file.close()

    file = open('resources/baggage.txt', 'r', encoding='UTF-8') # багаж
    for line in file:
        baggage.append(line)
    file.close()

    file = open('resources/add_info.txt', 'r', encoding='UTF-8') # доп инфа
    for line in file:
        add_info.append(line)
    file.close()

    file = open('resources/card_categories.txt', 'r', encoding='UTF-8') # карты
    for line in file:
        card_categories.append(line)
    file.close()

def refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories):
    bio_characteristics.clear()
    human_qualities.clear()
    professions.clear()
    hobbys.clear()
    health.clear()
    phobias.clear()
    baggage.clear()
    add_info.clear()
    card_categories.clear()
    fill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)

if __name__ == "__main__":
    bio_characteristics = []
    human_qualities = []
    professions = []
    hobbys = []
    health = []
    phobias = []
    baggage = []
    add_info = []
    card_categories = []
    fill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
    client = ds.Client()

    @client.event
    async def on_message(message:ds.Message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        global IN_GAME
        if message.content.startswith('>game'):
            channel = message.channel
            voice_channel = client.get_channel(CHANNEL_ID)
            members = voice_channel.members
            members_id = []

            if (IN_GAME):
                msg = '{0.author.mention}, игра уже **запущена**. Используйте >endgame, чтобы приостановить игру.'.format(message)
                await channel.send(msg)
            else:
                for member in members:
                    members_id.append(member.id)
                
                for member in members_id:
                    user = client.get_user(member)
                    player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                    line = "||------------------------------------------------------------------------------||\n"
                    biochar_str = "**Биологические характеристики (пол, возраст, ориентация):** \n - {0} \n".format(player.s_bio_char)
                    humanqual_str = "**Человеческое качество:** \n - {0} \n".format(player.s_human_qual)
                    prof_str = "**Профессия:** \n - {0} \n".format(player.s_proffesion)
                    hobby_str = "**Хобби:** \n - {0} \n".format(player.s_hobby)
                    health_str = "**Состояние здоровья:** \n - {0} \n".format(player.s_health)
                    phobia_str = "**Фобия:** \n - {0} \n".format(player.s_phobia)
                    baggage_str = "**Багаж:** \n - {0} \n".format(player.s_baggage)
                    addinfo_str = "**Дополнительная информация:** \n - {0} \n\n".format(player.s_add_info)
                    fcard_str = "**Первая карта:** \n - {0} \n".format(player.s_card_f)
                    scard_str = "**Вторая карта:** \n - {0} \n".format(player.s_card_s)
                    msg = line + biochar_str + humanqual_str + prof_str + hobby_str + health_str + phobia_str + baggage_str + addinfo_str + fcard_str + scard_str
                    await user.send(msg)
                msg = '{0.author.mention}, игра запущена, сообщения отправлены.'.format(message)
                IN_GAME = True
                await channel.send(msg)

        if message.content.startswith('>prof'):
            channel = message.channel
            voice_channel = client.get_channel(CHANNEL_ID)
            members = voice_channel.members
            members_id = []

            if (IN_GAME):
                #перераздать карты
                for member in members:
                    members_id.append(member.id)
                
                for member in members_id:
                    user = client.get_user(member)
                    refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                    player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                    line = "||------------------------------------------------------------------------------||\n"
                    prof_str = "**Профессия:** \n - {0} \n".format(player.s_proffesion)
                    msg = line + prof_str + line
                    await user.send(msg)
                chmsg = '{0.author.mention}, сообщения с новыми профессиями отправлены.'.format(message)
                await channel.send(chmsg)
            else:
                #игра не началась
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)
        
        if message.content.startswith('>health'):
            channel = message.channel
            voice_channel = client.get_channel(CHANNEL_ID)
            members = voice_channel.members
            members_id = []

            if (IN_GAME):
                #перераздать карты
                for member in members:
                    members_id.append(member.id)
                
                for member in members_id:
                    user = client.get_user(member)
                    player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                    line = "||------------------------------------------------------------------------------||\n"
                    health_str = "**Состояние здоровья:** \n - {0} \n".format(player.s_health)
                    msg = line + health_str + line
                    await user.send(msg)
                chmsg = '{0.author.mention}, сообщения с новыми состояниями здоровья отправлены.'.format(message)
                await channel.send(chmsg)
            else:
                #игра не началась
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>hobby'):
            channel = message.channel
            voice_channel = client.get_channel(CHANNEL_ID)
            members = voice_channel.members
            members_id = []

            if (IN_GAME):
                #перераздать карты
                for member in members:
                    members_id.append(member.id)
                
                for member in members_id:
                    user = client.get_user(member)
                    player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                    line = "||------------------------------------------------------------------------------||\n"
                    hobby_str = "**Хобби:** \n - {0} \n".format(player.s_hobby)
                    msg = line + hobby_str + line
                    await user.send(msg)
                chmsg = '{0.author.mention}, сообщения с новыми хобби отправлены.'.format(message)
                await channel.send(chmsg)
            else:
                #игра не началась
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)
        
        if message.content.startswith('>biochar'):
            channel = message.channel
            voice_channel = client.get_channel(CHANNEL_ID)
            members = voice_channel.members
            members_id = []

            if (IN_GAME):
                #перераздать карты
                for member in members:
                    members_id.append(member.id)
                
                for member in members_id:
                    user = client.get_user(member)
                    player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                    line = "||------------------------------------------------------------------------------||\n"
                    biochar_str = "**Биологические характеристики (пол, возраст, ориентация):** \n - {0} \n".format(player.s_bio_char)
                    msg = line + biochar_str + line
                    await user.send(msg)
                chmsg = '{0.author.mention}, сообщения с новыми биологическими характеристиками отправлены.'.format(message)
                await channel.send(chmsg)
            else:
                #игра не началась
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>@prof'):
            channel = message.channel
            if (IN_GAME):
                user_id = message.mentions[0].id
                user = client.get_user(user_id)
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                line = "||------------------------------------------------------------------------------||\n"
                prof_str = "**Профессия:** \n - {0} \n".format(player.s_proffesion)
                msg = line + prof_str + line
                await user.send(msg)
                chmsg = '{0.author.mention}, сообщение с новой профессией отправлено.'.format(message)
                await channel.send(chmsg)
            else:
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>@biochar'):
            channel = message.channel
            if (IN_GAME):
                user_id = message.mentions[0].id
                user = client.get_user(user_id)
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                line = "||------------------------------------------------------------------------------||\n"
                biochar_str = "**Биологические характеристики (пол, возраст, ориентация):** \n - {0} \n".format(player.s_bio_char)
                msg = line + biochar_str + line
                await user.send(msg)
                chmsg = '{0.author.mention}, сообщение с новой биологической характеристикой отправлено.'.format(message)
                await channel.send(chmsg)
            else:
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>@health'):
            channel = message.channel
            if (IN_GAME):
                user_id = message.mentions[0].id
                user = client.get_user(user_id)
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                line = "||------------------------------------------------------------------------------||\n"
                health_str = "**Состояние здоровья:** \n - {0} \n".format(player.s_health)
                msg = line + health_str + line
                await user.send(msg)
                chmsg = '{0.author.mention}, сообщение с новым состоянием здоровья отправлено.'.format(message)
                await channel.send(chmsg)
            else:
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>@phobia'):
            channel = message.channel
            if (IN_GAME):
                user_id = message.mentions[0].id
                user = client.get_user(user_id)
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                line = "||------------------------------------------------------------------------------||\n"
                phobia_str = "**Фобия:** \n - {0} \n".format(player.s_phobia)
                msg = line + phobia_str + line
                await user.send(msg)
                chmsg = '{0.author.mention}, сообщение с новой фобией отправлено.'.format(message)
                await channel.send(chmsg)
            else:
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>@addinfo'):
            channel = message.channel
            if (IN_GAME):
                user_id = message.mentions[0].id
                user = client.get_user(user_id)
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                line = "||------------------------------------------------------------------------------||\n"
                addinfo_str = "**Дополнительная информация:** \n - {0} \n\n".format(player.s_add_info)
                msg = line + addinfo_str + line
                await user.send(msg)
                chmsg = '{0.author.mention}, сообщение с новой дополнительной информацией отправлено.'.format(message)
                await channel.send(chmsg)
            else:
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>@addinfo'):
            channel = message.channel
            if (IN_GAME):
                user_id = message.mentions[0].id
                user = client.get_user(user_id)
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                player = randomize_characteristics(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                line = "||------------------------------------------------------------------------------||\n"
                addinfo_str = "**Дополнительная информация:** \n - {0} \n\n".format(player.s_add_info)
                msg = line + addinfo_str + line
                await user.send(msg)
                chmsg = '{0.author.mention}, сообщение с новой дополнительной информацией отправлено.'.format(message)
                await channel.send(chmsg)
            else:
                msg = '{0.author.mention}, игра не запущена.'.format(message)
                await channel.send(msg)

        if message.content.startswith('>help'):
            channel = message.channel
            help_msg = "**>help** - узнать все доступные команды.\n"
            game_msg = "**>game** - запустить игру.\n"
            prof_msg = "**>prof** - перераздать всем профессии.\n"
            health_msg = "**>health** - перераздать всем состояние здоровья.\n"
            hobby_msg = "**>hobby** - перераздать всем хобби.\n"
            biochar_msg = "**>biochar** - перераздать всем биологические характеристики.\n"
            direct_prof_msg = "**>@prof @nickname** - сменить профессию определенному юзеру.\n"
            direct_biochar_msg = "**>@biochar @nickname** - сменить биологическую характеристику определенному юзеру.\n"
            direct_health_msg = "**>@health @nickname** - сменить состояние здоровья определенному юзеру.\n"
            direct_phobia = "**>@phobia @nickname** - сменить фобию определенному юзеру.\n"
            direct_addinfo = "**>@addinfo @nickname** - сменить дополнительную информацию определенному юзеру.\n"
            endgame_msg = "**>endgame** - закончить игру.\n"
            # >@biochar >@health >@phobia >@addinfo
            msg = help_msg + game_msg + prof_msg + health_msg + hobby_msg + biochar_msg + direct_prof_msg + direct_biochar_msg + direct_health_msg + direct_phobia + direct_addinfo + endgame_msg
            await channel.send(msg)

        if message.content.startswith('>endgame'):
            channel = message.channel
            if (IN_GAME):
                refill_arrs(bio_characteristics, human_qualities, professions, hobbys, health, phobias, baggage, add_info, card_categories)
                msg = '{0.author.mention}, игра окончена!'.format(message)
                IN_GAME = False
                await channel.send(msg)
            else:
                msg = '{0.author.mention}, игра не начиналась!'.format(message)
                await channel.send(msg)

        if message.content.startswith('>exit'):
            channel = message.channel
            msg = 'Бот приостановил работу=('
            await channel.send(msg)
            exit(0)
    client.run(TOKEN)