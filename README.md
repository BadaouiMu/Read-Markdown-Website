# Read-Markdown-Website
## Installation using Docker Images
To install Sharing-Website using Docker images, execute the following command:


```bash
docker run -p 5000:5000 -it  badaouimu/read-markdown-website 
```

## Manual Installation of Aslanpp tools:  
### Install python (exemple sur Ubuntu): 
```

apt update -y
apt install python3 pip -y
pip3 install flask 
```
### Using of Website
```
git clone https://github.com/BadaouiMu/Read-Markdown-Website.git

cd Read-Markdown-Website/
python3 app.py
```
Visit the website at http://YourIP:5000 or use localhost:5000
## Usage : 
Once on the website, you can preview all Mardown file in the folder "code_md".