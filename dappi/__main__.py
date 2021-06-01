import argparse
import optparse
from .parser import *

def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--html;',
        action="store", dest="html",
        help="html to parse")
    parser.add_option('-o', '--output',
        action="store", dest="output",
        help="place to output messages", default="messages.csv")
    parser.add_option('-s', '--show',
        action="store", dest="show",
        help="show messages as they are being written", default=True)

    options, args = parser.parse_args()
    return options, args

def main(): 
    options, args = get_args()
    parser = Parser(options.html, options.output, options.show)
    parser.parse_all_messages_into_single_file()




if __name__ == "__main__":
    main()