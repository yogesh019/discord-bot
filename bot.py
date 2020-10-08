import discord
from vault.credentials import Credentials
from models.search import Search
from googleSearch import google_search

client = discord.Client()

cred= Credentials()
search=Search()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    #handling hi input
    if message.content.startswith('hi'):
        msg = 'Hey {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!google'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        search.post_search_data(author_id, query)

        results = google_search(query)
        if results:
            links = ' \n'.join(results)
            msg = 'Hello {}, you searched for {}. The top five results are: \n {}'.format(
                message.author.mention, query, links)
        else:
            msg = 'Hello {}, you searched for {}. \n Sorry, no matching links found.'.format(
                message.author.mention, query)
        await message.channel.send(msg)

    if message.content.startswith('!recent'):
        query = message.content.split(None, 1)[1]
        author_id = message.author.id
        results = search.fetch_search_data(author_id, query)
        if(len(results) > 0):
            keywords = 'Your matching search results are: \n' + \
                ' \n'.join([x[1] for x in results])
        else:
            keywords = 'No matching results found'
        await message.channel.send(keywords)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

client.run(cred.get_discord_token())

