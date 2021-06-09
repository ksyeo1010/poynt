# POYNT

A discord bot that adds interactive commands and economy to a server.

As the admin of a server, you can create, stop, end customized polls that users can bet. 

Create an achievement store with roles that users can buy with earned points.

## Requirements

1. `Docker`
2. `python 3.9.4` or `anaconda`

## Setting up the project locally

### Setting up env file:

1. Create a file called `.env` in the root directory.
2. Add the following key value pairs:
    - `DISCORD_TOKEN={discord_token}`. The discord token created in the discord dev portal.
    - `DISCORD_GUILD={discord_guild}`. The discord guild name.
    - `DB_USERNAME={db_username}`. The username to create when the db instance gets created.
    - `DB_PASSWORD={db_password}`. The password to create when the db instance gets created.
    - `DB_HOST={db_host}`. The db host, ideally 127.0.0.1 or localhost since it will be running in the same instance as the bot.
    - `DB_PORT={db_port}`. The db port, ideally 27017 since it is MongoDB's default port.

### Setting up python

If `anaconda` is installed:

1. Run `conda env create -f environment.yml` in the root directory. This will install the required libraries and set up the environment.
2. Run `source activate poynt` to activate the virtual environment.

If `python 3.9.4` is installed:

NOTE: `python` command can be `python3` or `python3.9` depending on machine.

1. Run `python -m pip install virtualenv` to install virtualenv library.
2. Run `python -m venv {env_name}` where `{env_name}` is the name of the environment.
3. Run `source activate {env_name}/bin/activate` to activate the virtual environment.
4. Run `pip -r install requirements.txt` to install the required libraries.

### Setting up MongoDB

1. Run `docker-compose build` to download an image of MongoDB and setup the settings.
2. Run `mkdir db` or create a directory called `db` so the docker container can hook it as a volume. This will be the directory where the db stores the files.

## Running the project locally

After following through the setup part, run the following:

1. Run `docker-compose up -d` to start the container containing the MongoDB instance.
2. Run `python bot.py` to start the discord bot.
3. Once the following is running, the following message should appear to the console:
    - `{discord_guild} has connected to Discord!`
4. Now add the discord bot application to a server, using the authorization url.
5. Type `$help` to learn about the commands and play with the bot.

## Link to bot
[Add bot to your server](https://discord.com/api/oauth2/authorize?client_id=849116691392495677&permissions=8&scope=bot)

## Contributors

- [Kwangsoo yeo](https://github.com/ksyeo1010)
- [Paul Yeon](https://github.com/paulyeon)