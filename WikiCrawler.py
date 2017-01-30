import requests as r
from bs4 import BeautifulSoup
import threading as t
import sys

base_url = "http://wowwiki.wikia.com/wiki/"
start_page = "Portal:Main"
item_set = set()
verbose = True


def recurse_page(link):
    global item_set
    global verbose

    page = r.get(base_url + link)
    soup = BeautifulSoup(page.text, "lxml")
    links = soup.find_all("a")

    fixed_links = []
    for l in links:
        try:
            href = l['href']
            if "http" not in href and '=' not in href and '?' not in href and '%' not in href and "/wiki/" in href:
                fixed_links.append(href[6:])
        except:
            pass
    if verbose:
        print(t.current_thread().name," :  Page",link, "has", len(fixed_links), "links (", t.active_count(), "threads )")

    for l in fixed_links:
        try:
            if l not in item_set:
                item_set.add(l)
                thread = t.Thread(target=recurse_page, name="Thread-" + str(t.active_count() + 1), args=(l,))
                thread.start()
        except:
            pass


def save_file():
    global item_set
    global verbose

    save_set = item_set.copy()

    file = open("items.txt", "w")
    for i in save_set:
        file.write(i + "\n")
    file.close()

    t.Timer(10.0, save_file).start()

    if verbose:
        print("\n\nWrote", len(save_set), "items to file\n\n")
    else:
        print("Wrote", len(save_set), "items to file (", t.active_count(), "active threads )")


if "-v" in sys.argv:
    verbose = True

print("Starting...\n")

# Commented out reading old items from file

#print("Reading from file...\n")
#file = open("items.txt", 'r')
#lines = file.readlines()
#for l in lines:
    #item_set.add(l[:-1])
#file.close()

print("Program Started! (", len(item_set), "items loaded )")


t.Timer(10.0, save_file).start()
recurse_page(start_page)