# -*- coding: utf-8 -*-

import nest_asyncio
import discord
from discord.ext import commands
import random

# 필요에 따라 asyncio 이벤트 루프를 중첩 실행 가능하게 설정
nest_asyncio.apply()

# FFXIV 직업 목록
jobs = [
    '전사', '나이트', '암흑기사', '건브레이커',
    '백마도사', '학자', '점성술사', '현자',
    '몽크', '용기사', '닌자', '사무라이', '리퍼',
    '흑마도사', '소환사', '적마도사',
    '음유시인', '기공사', '무도가','픽토맨서','바이퍼'
]

TOKEN = 'YOUR DISCORD TOKEN'  # 여기에 본인의 디스코드 봇 토큰 입력

# 디스코드 봇 생성
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def 직업뽑기(ctx):
    # 직업 목록에서 랜덤하게 선택
    random_job = random.choice(jobs)
    await ctx.send(f'선택된 직업: **{random_job}**')

# 봇 실행
bot.run(TOKEN)
