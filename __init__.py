import markdown
#import framework
from flask import flask

#create instance
app = Flask(__name__)

@app.route("/")
def index():
    #popen the README file
    with open(os.path.dirname(app.root_path) + 'README.md', 'r') as markdown_file:
       #read content of file
        content = markdown_file.read()
        #convert to html
        return markdown.markdown(content)