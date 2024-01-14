from flask import Flask, render_template
import os
import markdown2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'code_md'

@app.route('/')
def index():
    md_files = get_md_files()
    return render_template('index.html', md_files=md_files, dark_mode=True)

@app.route('/preview/<filename>')
def preview(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path) or not allowed_file(filename):
        return "Invalid file"

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        html_content = markdown2.markdown(content, extras=['tables', 'fenced-code-blocks'])
        return render_template('preview.html', content=html_content, filename=filename, dark_mode=True)

def get_md_files():
    md_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.endswith('.md')]
    return md_files

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'md'

if __name__ == '__main__':
    #app.run(debug=True) ## to run localy
    app.run(debug=True, host='0.0.0.0', port=5000)

