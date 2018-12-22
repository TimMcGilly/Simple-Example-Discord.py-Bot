## Settting up bot

There are a few steps required to setup the discord bot:
1. **Make sure python 3.6 or higher is installed**


2. **Install python dependancies**

pip install -U -r requirements.txt

3. **Create PostgreSQL database**

You will need PostgreSQL installed and then type into the `psql` tool (on windows this is installed as `SQL Shell`):
```sql
CREATE ROLE discord WITH LOGIN PASSWORD 'discordpw';
CREATE DATABASE SimpleExampleDiscordBot OWNER discord;
```

