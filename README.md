# Dappi
[![PyPI version](https://badge.fury.io/py/dappi.svg)](https://badge.fury.io/py/dappi)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)


Scrape messages from discord server dumps and parse them into a csv file. More features to come later though

# Usage
0. Get an html dump from the server you are trying to parse messages from using... 
    - ### [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter)

1. Install dappi
    - ```pip3 install dappi```
## Use As CLI
2. Run the CLI with command line args
    - ```dappi -i {path_to_discord_html_export} -o {path_to_csv_output_directory/file_name.csv} -s {boolean | "Sets a flag to show messages in the terminal while they are being parsed"}```
    - Note: __file_name.csv__, doesn't need to exist, but the __"path_to_csv_output_directory"__ does!

## Use As Library
2. Use dappi as a library
```py
from dappi import parser
                                
dappi_parser = parser.Parser(
        'frostbite.html',    # Html input
        'data/messages.csv', # Output Directory
        True                 # Show messages while writing
    )
dappi_parser.parse_all_messages_into_single_file()
exit
```
# TODO
- Automated tests
- Generate statistics and graphs of user activity from parsed messages?
    - Frequency of user messages?
    - Sentiment analysis of user messages?
    - Other interesting metrics?
- Expose more functionality, I.E Write better docs