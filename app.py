from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporária de produtos
produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'].replace(',', '.'))
        produtos.append({'id': len(produtos)+1, 'nome': nome, 'preco': preco})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return "Produto não encontrado", 404
    if request.method == 'POST':
        produto['nome'] = request.form['nome']
        produto['preco'] = float(request.form['preco'].replace(',', '.'))
        return redirect(url_for('index'))
    return render_template('edit.html', produto=produto)


@app.route('/delete/<int:id>')
def delete(id):
    global produtos
    produtos = [p for p in produtos if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
