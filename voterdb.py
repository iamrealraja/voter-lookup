import web
import json
import logging
from webpy_jinja2 import render_template
import os

urls = (
    "/", "index",
    "/([A-Z][A-Z])", "state",
    "/([A-Z][A-Z])/(.*)", "voterid"
)
app = web.application(urls, globals())
application = app.wsgifunc()

def setup_logger():
    FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
    logging.basicConfig(level=logging.INFO, format=FORMAT)    
    return logging.getLogger("voterdb")

logger = setup_logger()

dbfile = os.getenv("VOTERDB_DATABASE", "voterids.db")
logger.info("using the sqlite database %r", dbfile)

db = web.database(dbn="sqlite", db=dbfile)

def init_app(dbfile):
    global db
    db = web.database(dbn="sqlite", db=dbfile)

def get_states():
    return db.select("state").list()

def get_state(code):    
    result = db.where("state", code=code).list()
    return result and result[0] or None

def get_voter(state_code, voterid):
    result = db.where("voterid", state=state_code, voterid=voterid).list()
    return result and result[0] or None

class index:
    def GET(self):
        states = get_states()
        return render_template("index.html", states=states)

class state:
    def GET(self, state_code):
        state = get_state(state_code.upper())
        if not state:
            raise web.notfound()

        i = web.input(voterid=None)
        voter = i.voterid and get_voter(state_code, i.voterid)
        return render_template("state.html", state=state, voter=voter, voterid=i.voterid)

class voterid:
    def GET(self, state_code, voterid):
        voter = get_voter(state_code, voterid)
        if not voter:
            web.ctx.status = "404 Not Found"

        web.header("Content-Type", "application/json")
        return json.dumps(voter)

def main():
    app.run()

if __name__ == '__main__':
    main()
