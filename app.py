from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    names = request.form['names'].split(',')
    generated_texts = generate_texts(names)
    return render_template('result.html', generated_texts=generated_texts)


def generate_texts(names):
    generated_texts = []
    for name in names:
        # Modify this logic to create sentences with the name
        sentence1 = f"<b>{name} Landa Frøkedal</b>"
        sentence2 = f"{name} Landa Frøkedal<br>Borggata 12 E<br>0650 Oslo"
        sentence3 = f"Vidar, Anne Lise og {name}"
        sentence4 = f"<span style='font-family: \"Qwitcher Grypen\", sans-serif; font-size: 40px;'>{name} Landa Frøkedal</span>"
        sentence5 = f"<span style='font-family: \"Inconsolata\", monospace;'>{name}, 2 år, bor på Tøyen med mor Anne Lise og far Vidar</span>"
        sentence6 = f"<span style='font-family: \"Abril Fatface\", cursive; font-size: 30px;'>{name} Landa Frøkedal</span>"
        sentence7 = f"<span style='font-family: \"Creepster\", cursive; font-size: 34px;'>🎃 {name} feirer Halloween!</span>"
        sentence8 = f"<span style='font-family: \"Bungee Shade\", cursive; color: green;'>Anne Lise, Vidar, {name}</span>"
        sentence9 = f"<span style='font-family: \"New Rocker\", cursive; font-size: 30px;'>Gratulerer med dagen, {name}! 🎂</span>"
        space_between = "<div style='background-color: grey; height: 5px; margin: 10px 0;'></div>"
        
        generated_texts.extend([sentence1, sentence2, sentence3, sentence4, sentence5, sentence6, sentence7, sentence8, sentence9, space_between])
    return generated_texts

if __name__ == '__main__':
    app.run(debug=True)
