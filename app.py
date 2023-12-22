from flask import Flask, render_template, request
from model import predict_step
from model2 import generate_story
import os
from tempfile import NamedTemporaryFile
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Toppage rooting
@app.route("/")
def toppage():
    return render_template("index.html")


# generate page rooting
@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "GET":
        return render_template("generate.html")
    
    elif request.method == "POST":
        
        try:
            tokens = request.form.get("tokens", 150, type=int)
            input_images = request.files.getlist("image_files")
            detection_results = []
            img_data = []
            
            for image in input_images:
                if image:
                    filename = secure_filename(image.filename)
                    img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image.save(img_path)
                    detection_result = predict_step([img_path])
                    detection_results.extend(detection_result)
                    
                    img_path = os.path.join("uploads", filename).replace("\\", "/")

                    img_data.append({
                        "path": img_path,
                        "caption": detection_result[0] if detection_result else "No caption"
                    })
            
            story = generate_story(detection_results, max_tokens=tokens)
            
        except Exception as e:
            print(f"画像の保存中にエラーが発生しました: {str(e)}")
            img_data = []
            story = ""
            
        return render_template("generate.html", story=story, img_data=img_data) 




if __name__ == "__main__":
    app.run(debug=True)