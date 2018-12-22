import asyncpg

async def create_tables(db):
    tables = [
        '''
        CREATE TABLE IF NOT EXISTS members(
            id serial PRIMARY KEY,
            discord_id text,
            name text,
            dob date
        ) ''',
        '''
        CREATE TABLE IF NOT EXISTS messages(
            id serial PRIMARY KEY,
            discord_id text,
            content text,
            dob date
        ) '''
    ]

    for table in tables:
        await db.execute(table)