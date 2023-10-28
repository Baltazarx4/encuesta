from flask import Flask, render_template, request, session,redirect

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Guardar los datos del formulario en la sesión
        session['name'] = request.form.get('name')
        session['location'] = request.form.get('location')
        session['language'] = request.form.get('language')
        session['comment'] = request.form.get('comment')

        # Redirigir al resultado
        return redirect('/result')

    return render_template('index.html')

@app.route('/result')
def result():
    # Obtener datos de la sesión
    name = session.get('name', '')
    location = session.get('location', '')
    language = session.get('language', '')
    comment = session.get('comment', '')

    return render_template('result.html', name=name, location=location, language=language, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
