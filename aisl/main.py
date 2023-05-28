import os
import logging

import dotenv
import docopt

from aisl.logger import setup_logging

from aisl.usage import USAGE
from aisl.version import VERSION

from aisl.commands.demo import demo


def main():
    dotenv.load_dotenv()

    if os.getenv("DEBUG", False):
        print("-"*100)

    setup_logging()
    logger = logging.getLogger("aisl")

    args = docopt.docopt(USAGE, version=f"aisl {VERSION}")

    passed_args = {k: v for k, v in args.items() if v not in (False, [], None)}
    logger.debug(f"passed args: {passed_args}")

    #####################################
    ### COMMANDS ########################
    #####################################
    if args.get("version", False):
        print(f"aisl {VERSION}")
    elif args.get("demo", False):
        demo(args)
