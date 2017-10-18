################################################################################
# Module: settings.py
# Description: Global settings for script
################################################################################

import logging as lg

pause_duration = 0.01 #seconds to pause between tweets

# location to save log files
logs_folder = './logs'

# write log to file and/or to console
log_file = True
log_console = True
log_level = lg.INFO
log_name = 'pgp_bot'
log_filename = 'pgp_bot'
