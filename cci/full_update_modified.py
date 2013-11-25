import os, imp
from datetime import datetime, timedelta

def parse_args():
    from argparse import ArgumentParser
    ap = ArgumentParser(prog='full_update', description="Updates all tasks")
    ap.add_argument(dest='settings_path', help='Settings Path')
    return ap.parse_args()

if __name__ == '__main__':   
    args = parse_args()
    settings_path = args.settings_path
    mod_time = datetime.today() - timedelta(hours=24)
    
    print('INFO:last modified time limit='+str(mod_time))
    print('INFO:running full update, Start Time:'+str(datetime.now()))

    # Load the settings file
    print('INFO:loading settings from:'+settings_path)
    settings = imp.load_source('settings', settings_path)
    settings_filename=os.path.splitext(os.path.basename(settings_path))[0]

    # Run the Modules:
    settings.myLauncher.update_modules(settings_filename, mod_time)

    # Run the full update
    settings.myLauncher.update(settings_filename, mod_time)

    print('INFO:finished full update, End Time: '+str(datetime.now()))
