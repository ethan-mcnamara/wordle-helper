# wordle-helper
A CLI tool to help Wordle players. Users provide the words they've previously guessed along with the colour of each letter and the tool displays the possible solutions.

## Initial Setup
Before using this tool, you will need to install Python and two Python libraries. 

To install Python, visit [python.org](https://www.python.org/downloads/) and follow the steps listed on their site.

Next, open your command window and run the following commands:
  - `pip install regex`
  - `pip install nltk`
  - `pip install corpus`

Next, using the command window, locate the directory in which the `init_script.py` file is located.

From that directory, run the command `python3 init_script.py`. That script will download the necessary data, including the list of dictionary words. A window will likely open, follow all instructions in that window. This script only needs to be run once, no additional data will be downloaded if the script is ran again.

Assuming all downloads were properly completed, the tool should be usable.

## Using the Tool
Using a command window, locate the directory in which the `wordle_helper.py` file is located.

From that directory, run the command `python3 wordle_helper.py`. That will run the script. Follow all instructions shown in the command window to effectively use the tool.