from flask import Flask
app = Flask(__name__)

def gfg():
   return 'Myname'
app.add_url_rule('/', 'g2g', gfg)

if __name__ == '__main__':
    app.run()