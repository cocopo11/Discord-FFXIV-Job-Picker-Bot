# pip install discord.py aiomysql nest_asyncio

import nest_asyncio
import discord
from discord.ext import commands
import aiomysql
import random
import csv

# 필요에 따라 asyncio 이벤트 루프를 중첩 실행 가능하게 설정
nest_asyncio.apply()

# FFXIV 직업 목록
jobs = [
    '전사', '나이트', '암흑기사', '건브레이커',
    '백마도사', '학자', '점성술사', '현자',
    '몽크', '용기사', '닌자', '사무라이', '리퍼',
    '흑마도사', '소환사', '적마도사',
    '음유시인', '기공사', '무도가'
]

TOKEN = 'YOUR DISCORD TOKEN'  # 여기에 본인의 디스코드 봇 토큰 입력

# Database connection details
DB_HOST = 'localhost'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'

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

@bot.command()
async def 검색(ctx, *, item_name: str):
    # Search for the item in the MariaDB database
    async with aiomysql.connect(
        host=DB_HOST,
        port=3306,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    ) as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            sql = "SELECT material, quantity FROM recipes WHERE item_name = %s"
            await cursor.execute(sql, (item_name,))
            rows = await cursor.fetchall()
            
            if rows:
                response = f"**{item_name}**의 필요한 재료:\n"
                for row in rows:
                    response += f"- {row['material']}: {row['quantity']}개\n"
                await ctx.send(response)
            else:
                await ctx.send(f'{item_name}에 대한 정보를 찾을 수 없습니다.')

# 봇 실행
bot.run(TOKEN)
