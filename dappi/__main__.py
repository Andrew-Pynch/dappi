import argparse
import optparse
from parser import Parser

def get_args():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--html;',
        action="store", dest="html",
        help="html to parse")
    parser.add_option('-o', '--output',
        action="store", dest="output",
        help="place to output messages", default="messages.csv")

    options, args = parser.parse_args()
    return options, args

def main(): 
    options, args = get_args()
    parser = Parser(options.html, options.output)
    parser.parse_all_messages_into_single_file()




if __name__ == "__main__":
    main()