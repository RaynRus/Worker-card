from flask import Flask, request, url_for, render_template

app = Flask("main")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        print(request.form)
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        about = request.form.get('about')
        stack = ', '.join(request.form.getlist('technology_stack'))
        dev_level = request.form.get('development_level')
        photo = request.files.get('photo')

        with open(f".{url_for('static', filename='photo_image.png')}", mode='wb') as file:
            file.write(photo.read())

        return render_template(
          "card.html", 
          first_name=first_name,
          last_name=last_name,
          about=about,
          stack=stack,
          dev_level=dev_level
        )



app.run(host='0.0.0.0', port=8080)
