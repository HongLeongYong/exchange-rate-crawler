# move history file to archive directory
import os
import shutil
import global_variable as gv

# if file_archive_dir not exist, create it
if not os.path.isdir(gv.file_archive_dir):
    os.mkdir(gv.file_archive_dir)

# move file to archive directory
def move_history_file(file_name):
    shutil.move(file_name, gv.file_archive_dir)
    print('move file to archive directory')

# move_history_file('taiwan_cooperative_bank_exchange_rate.csv')