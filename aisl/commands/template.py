import os
import re
from typing import List
import logging
logger = logging.getLogger("aisl")

from aisl.helpers import *

def summarize(opts):
    text = opts.get("<text>", None)
    if text is None:
        logger.error("Please specify text to summarize.")
        return
    
    logger.debug(f"Summarizing...")
