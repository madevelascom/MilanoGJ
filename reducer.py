__author__ = 'madevelasco'

import sys

current_ZoneCountryCode = None
current_count = 0
ZoneCountryCode = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    region, countryCode, count, time_interval = line.split('\t', 3)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_ZoneCountryCode == ZoneCountryCode:
        current_count += count
    else:
        if current_ZoneCountryCode:
            # write result to STDOUT
            print '%s\t%s' % (current_ZoneCountryCode, current_count, time_interval)
        current_count = count
        current_countryCode = ZoneCountryCode

# do not forget to output the last word if needed!
if current_ZoneCountryCode == ZoneCountryCode:
    print '%s\t%s' % (current_ZoneCountryCode, current_count)