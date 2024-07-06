import sys
import argparse
import textwrap
from Registry import Registry


class RegAnalyze:
    def __init__(self,args):
        self.filename = args.file
        self.registrytype = args.type
        #check for registry filename
        try:
            self.reg = Registry.Registry(args.file)
        except FileNotFoundError:
            print(f'[X] Registry file {args.file} not found, check filename and directory')
            sys.exit(1)
        if args.users:
            self.get_users()
        
    def get_users(self):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Python windows registry analysis tool for forensics',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
            python reganalyze.py -t RegistryType -f filename [options]
            Usage Example:
                python reganalyze.py -t SYSTEM -f SYSTEM -r #generate full report
                python reganalyze.py -t SYSTEM -f SYSTEM -u #extract available users
        '''))
    parser.add_argument('-t', '--type', help='registry type')
    parser.add_argument('-f', '--file', help='registry filename')
    parser.add_argument('-r', '--report', action='store_true', help='generate full report')
    parser.add_argument('-u', '--users', action='store_true',help='extract available users')
    args = parser.parse_args()
    
    #check if no arguments to print help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    ra = RegAnalyze(args)