# -*- coding: utf-8 -*-

import nest_asyncio
import discord
from discord.ext import commands
import random
import requests

# 필요에 따라 asyncio 이벤트 루프를 중첩 실행 가능하게 설정
nest_asyncio.apply()

# 한국 서버 이름을 영어로 맵핑
server_name_map = {
    '모그리': 'moogle',
    '초코보': 'chocobo',
    '카벙클': 'carbuncle',
    '톤베리': 'tonberry',
    '펜리르': 'fenrir'
}


# FFXIV 직업 목록 (한국 서버에 맞게 한국어로 변경)
jobs = {
    'Warrior': '전사', 'Paladin': '나이트', 'Dark Knight': '암흑기사', 'Gunbreaker': '건브레이커',
    'White Mage': '백마도사', 'Scholar': '학자', 'Astrologian': '점성술사', 'Sage': '현자',
    'Monk': '몽크', 'Dragoon': '용기사', 'Ninja': '닌자', 'Samurai': '사무라이', 'Reaper': '리퍼',
    'Black Mage': '흑마도사', 'Summoner': '소환사', 'Red Mage': '적마도사',
    'Bard': '음유시인', 'Machinist': '기공사', 'Dancer': '무도가'
}

# Discord 봇 토큰과 FFLogs API 키
TOKEN = 'YOUR_DISCORD_TOKEN'  # 여기에 Discord 봇 토큰을 입력하세요
FFLOGS_API_KEY = 'YOUR_FFLOGS_API_KEY'  # 여기에 FFLogs API 키를 입력하세요


# 디스코드 봇 생성
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def 직업뽑기(ctx):
    # 직업 목록에서 랜덤하게 선택
    random_job = random.choice(list(jobs.values()))
    await ctx.send(f'선택된 직업: **{random_job}**')

@bot.command()
async def fflog(ctx, player_name: str, server_name: str):
    # 한국어로 입력된 서버 이름을 영어로 변환
    english_server_name = server_name_map.get(server_name, server_name)
    
    player_info = get_player_info(player_name, english_server_name)
    if player_info:
        await ctx.send(player_info)
    else:
        await ctx.send('플레이어 정보를 찾을 수 없습니다.')


def get_player_info(player_name, server_name):
    # 한국 서버 이름을 영어로 변환
    english_server_name = server_name_map.get(server_name, server_name)

    url = f'https://www.fflogs.com/character/kr/{english_server_name}/{player_name}'
    headers = {
        'Authorization': f'Bearer {FFLOGS_API_KEY}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 처리

        data = response.json()
        if not data:
            return '플레이어의 기록이 없습니다.'

        player_info = f'플레이어 이름: {player_name}\n'
        for record in data:
            spec = record['spec']
            korean_job = jobs.get(spec, spec)  # 직업 이름을 한국어로 가져오거나 기존 이름 그대로 사용
            transformed_rank = transform_rank(record['rank'])
            player_info += (
                f"직업: {korean_job}, "
                f"레이드 이름: {record['encounterName']}, "
                f"랭크: {transformed_rank}\n"
            )
        return player_info

    except requests.exceptions.RequestException as e:
        print(f'Error fetching player info: {e}')
        return None
    
def transform_rank(rank):
    if 0 <= rank < 25:
        return '회딱'
    elif 25 <= rank < 50:
        return '초딱'
    elif 50 <= rank < 75:
        return '파딱'
    elif 75 <= rank < 95:
        return '보딱'
    elif 95 <= rank < 99:
        return '주딱'
    elif 99 <= rank < 100:
        return '핑딱'
    else:
        return '노딱'


# 봇 실행
bot.run(TOKEN)
