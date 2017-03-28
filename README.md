# WikiCrawler

* WikiCrawler.py: Pretty inefficient Web Crawler for http://wowwiki.wikia.com/
 * save_file() makes a copy of the global set, and saves that to the file 'items.txt'
 * recurse_page(link) takes a string and will recurse through the basepage/wiki/link
* FixData.py: Crappy hack that just removes items from 'items.txt' that have a '#' or ':'
 * Also makes it lowercase, and writes to 'fixed_items.txt'
* SplitData.py: Takes all the items, removes the newline character, then splits them by '_'
 * Keeps the phrases with the underscores, but also adds the seperated ones too
 * Writes to 'split_items.txt'
 
The node.js Web Server is currently using 'split_items.txt'

Let me know if you have any ideas / improvements. Feel free to fork or merge.

Note: Use Python3 and run 'pip install -r requirements.txt' from the main directory

TODO: Comment code, add stuff, fix bad stuff
