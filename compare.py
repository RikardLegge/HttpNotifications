from pushbullet import Pushbullet
import urllib2
import re
import os
import sys


def read_file(path):
    contents = None

    if os.path.isfile(path):
        f = open(path, "r")
        contents = f.read()
        f.close()

    return contents

def write_file(path, contents):
    f = open(path, "w")
    f.write(contents)
    f.close()

class UrlChecker:

    def __init__(self, url, parser_re, title_id, link_id, force, callback):
        self.url = url
        self.url_path = re.sub('[:/.?&]', '', url) + ".cache"
        self.title_id = title_id
        self.link_id = link_id
        self.parser_re = parser_re
        self.callback = callback
        self.force = force

    def fetch(self):
        return urllib2.urlopen(url).read().decode('utf-8')

    def parse(self, contents):
       return re.search(self.parser_re, contents)


    def prev(self):
        return read_file(self.url_path)

    def curr(self):
        return self.parse(self.fetch())


    def check(self):
        old = self.prev()
        new = self.curr()

        if new:
            title = new.group(self.title_id)
            link = new.group(self.link_id)

            if old != link or self.force:
                write_file(self.url_path,link)
                self.callback(title, link)

def on_change(title, link):
    title = title.encode('ascii', 'ignore')
    link = link.encode('ascii', 'ignore')

    print('NEW:' + title + ' (' + link + ')')

    api_key = read_file('api_key').strip()
    if api_key:
        pb = Pushbullet(api_key)
        pb.push_link(title, link)
    else:
        print('No api_key file available. Push not sent')

if __name__ == '__main__':
    if len (sys.argv) < 5:
        print ('Usage: myscript [Url] [Regex] [Title_Index] [Link_Index]')
    else:
        url = sys.argv[1]
        re_parser = sys.argv[2]
        title_id = int(sys.argv[3])
        link_id = int(sys.argv[4])
        force = False

        if len (sys.argv) > 5:
            force = sys.argv[5] == 'force'

        UrlChecker(url, re_parser, title_id, link_id, force, on_change).check()
