import os,sys,time
from spoofer import conf

os.system("pyfiglet -f slant GLoriusHeLL666 | lolcat")
def main():
    args = conf.parser.parse_args()
    args.func(args)

sys.exit(main())
