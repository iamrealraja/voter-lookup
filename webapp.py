from __future__ import print_function
import web
import json
import os

urls = (
    "/", "index",
    "/search", "search"
)
app = web.application(urls, globals())
application = app.wsgifunc()

dbfile = os.getenv("VOTER_LOOKUP_DATABASE", "voter.db")
print("using the sqlite database:", dbfile)

db = web.database(dbn="sqlite", db=dbfile)

def get_voters(voterid, state=None):
    voterid1 = voterid.strip()
    wheres = dict(voterid=voterid1)
    if state:
        wheres['state'] = state.upper()
    return db.where("voterid", **wheres).list()

class index:
    def GET(self):
        html = open("static/index.html")
        web.header("Content-type", "text/html")
        return html

class search:
    def GET(self):
        i = web.input(voterid=None, state=None)
        voter = get_voters(i.voterid, state=i.state)
        web.header("Content-Type", "application/json")
        return json.dumps(voter, indent=True)

def main():
    app.run()

if __name__ == '__main__':
    main()
