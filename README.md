
This script turns an e-Paper display into a digital nametag, and displays
a new randomly-generated name (and university affiliation) every 10 seconds.

It uses three input files:
 - `firstnames.csv`
 - `lastnames.csv`
 - `colleges.csv`

I used (this data from FiveThirtyEight)[https://github.com/fivethirtyeight/data/tree/master/most-common-name]
as a basis for the files here.

Each should contain a list to sample from, with one value on each line. For example,
`firstnames.csv` should be a text file with one possible first name on each line.

The script as written relies on my fork of [PaperTTY](https://github.com/GregDMeyer/PaperTTY),
which you need to install before running.

The font, `BrownBagLunch.ttf`, was created by Kevin Richey and is licensed as Freeware. See
[here](https://www.fontspace.com/kevin-richey/brown-bag-lunch).