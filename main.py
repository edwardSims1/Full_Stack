
from flask import Flask 
from flask import render_template 
  
# creates a Flask application 
app = Flask(__name__) 
  
  
 
  



# Images 
@app.route("/image") 
def serve_image(): 
    message = "Image Route"
    return render_template('images.html', message=message)


  
@app.route("/") 
def hello(): 
    message = "Hello, World"
    return render_template('index.html', message=message) 
  
  
@app.route("/video") 
def serve_video(): 
    message = "Video Route"
    return render_template('video.html', message=message) 
  
  
@app.route("/audio") 
def serve_audio(): 
    message = "Audio Route"
    return render_template('audio.html', message=message) 
  
  
# run the application 
if __name__ == "__main__": 
    app.run(debug=True)