# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
TOKEN = 'Your Discord Developer Token' # 이곳에 자신의 디스코드 봇 토큰을 넣으세요


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def 직업뽑기(ctx):
    # 1부터 1000까지의 숫자 중에서 랜덤하게 선택
    random_number = random.randint(1, 1000)

    # 선택된 숫자에 따라 직업을 결정
    if random_number <= 50:
        job = "나이트"
    elif random_number <= 100:
        job = "전사"
    elif random_number <= 150:
        job = "암흑기사"
    elif random_number <= 200:
        job = "건브레이커"
    elif random_number <= 250:
        job = "백마도사"
    elif random_number <= 300:
        job = "학자"
    elif random_number <= 350:
        job = "점성술사"
    elif random_number <= 400:
        job = "현자"
    elif random_number <= 450:
        job = "흑마도사"
    elif random_number <= 500:
        job = "소환사"
    elif random_number <= 550:
        job = "적마도사"
    elif random_number <= 600:
        job = "몽크"
    elif random_number <= 650:
        job = "용기사"
    elif random_number <= 700:
        job = "닌자"
    elif random_number <= 750:
        job = "사무라이"
    elif random_number <= 800:
        job = "리퍼"
    elif random_number <= 850:
        job = "음유시인"
    elif random_number <= 900:
        job = "기공사"
    elif random_number <= 1000:
        job = "무도가"

    await ctx.send(f'선택된 직업: {job}')

bot.run(TOKEN)
