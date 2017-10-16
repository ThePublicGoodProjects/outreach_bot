################################################################################
# Module: settings.py
# Description: Global settings, can be configured by user by passing values to
#              utils.config()
# License: MIT, see full license in LICENSE.txt
# Source Code by: Geoff Boeing
# Source Web: https://github.com/gboeing/osmnx
################################################################################

import logging as lg

# locations to save data, logs, images, and cache
data_folder = './data'
logs_folder = './logs'
imgs_folder = './images'
cache_folder = './cache'

# cache server responses
use_cache = True

# write log to file and/or to console
log_file = True
log_console = True
log_level = lg.INFO
log_name = 'pgp_bot'
log_filename = 'pgp_bot'

# useful tags - left empty
useful_tags_node = []
useful_tags_path = []