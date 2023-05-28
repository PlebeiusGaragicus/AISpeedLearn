# NOTE: This usage string is very important.  Since we are using docopt, it is used to parse the command line arguments.
USAGE = '''
Usage:
  aisl version
  aisl demo
'''

  # aisl extract [ --all | <file> ]
  # aisl summarize [ --all | <file> ]



# # NOTE: This usage string is very important.  Since we are using docopt, it is used to parse the command line arguments.
# USAGE = '''
# aisl

# Usage:
#   aisl home [--verbose] [--json] [--onlyreplies] [--noreplies] [--kinds=<kinds>...] [--since=<since>] [--until=<until>] [--limit=<limit>]
#   aisl inbox [--verbose] [--json] [--onlyreplies] [--noreplies] [--since=<since>] [--until=<until>] [--limit=<limit>]
#   aisl setprivate <key>
#   aisl sign <event-json>
#   aisl verify <event-json>
#   aisl public
#   aisl publish [--reference=<id>...] [--profile=<id>...] [--file=<file>] [<content>]
#   aisl message [--reference=<id>...] <pubkey> <content>
#   aisl metadata --name=<name> [--about=<about>] [--picture=<picture>] [--nip05=<nip05>] [--banner=<banner>] [--displayname=<displayname>] [--lud16=<lud16>] [--username=<username>] [--website=<website>]
#   aisl profile [--verbose] [--json] <pubkey>
#   aisl follow <pubkey> [--name=<name>]
#   aisl unfollow <pubkey>
#   aisl following
#   aisl event view [--verbose] [--json] <id>
#   aisl event delete <id>
#   aisl share-contacts
#   aisl key-gen
#   aisl relay
#   aisl relay add <url>
#   aisl relay remove [--all]
#   aisl relay remove <url>
#   aisl relay recommend <url>
#   aisl relay getonline

# Specify <content> as '-' to make the publish or message command read it
# from stdin.
# '''






# NOTE: This is an example of the args dictionary that is returned by docopt.
# args: {'--about': None,
#  '--all': False,
#  '--banner': None,
#  '--displayname': None,
#  '--file': None,
#  '--json': False,
#  '--kinds': [],
#  '--limit': None,
#  '--lud16': None,
#  '--name': None,
#  '--nip05': None,
#  '--noreplies': False,
#  '--onlyreplies': False,
#  '--picture': None,
#  '--profile': [],
#  '--reference': [],
#  '--since': None,
#  '--until': None,
#  '--username': None,
#  '--verbose': False,
#  '--website': None,
#  '<content>': None,
#  '<event-json>': None,
#  '<id>': None,
#  '<key>': None,
#  '<pubkey>': None,
#  '<url>': None,
#  'add': False,
#  'delete': False,
#  'event': False,
#  'follow': False,
#  'following': False,
#  'getonline': False,
#  'home': True,
#  'inbox': False,
#  'key-gen': False,
#  'message': False,
#  'metadata': False,
#  'profile': False,
#  'public': False,
#  'publish': False,
#  'recommend': False,
#  'relay': False,
#  'remove': False,
#  'setprivate': False,
#  'share-contacts': False,
#  'sign': False,
#  'unfollow': False,
#  'verify': False,
#  'view': False}