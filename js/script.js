// 1. Função para LER os dados do MySQL (Consulta)
function carregarCategorias() {
    fetch('http://127.0.0.1:5000/categorias')
        .then(resposta => resposta.json())
        .then(dados => {
            const lista = document.getElementById('listaCategorias');
            lista.innerHTML = ''; // Limpa a lista no ecrã antes de atualizar
            
            // Transforma o JSON recebido numa lista visual de HTML
            dados.forEach(categoria => {
                const item = document.createElement('li');
                item.textContent = `ID ${categoria.id} — ${categoria.nome}`;
                lista.appendChild(item);
            });
        })
        .catch(erro => console.error('Erro ao carregar categorias:', erro));
}

// 2. Função para GRAVAR um novo dado (Cadastro)
function salvarCategoria() {
    const nomeInput = document.getElementById('nomeCategoria');
    
    // Faz um pedido POST enviando o texto convertido para JSON
    fetch('http://127.0.0.1:5000/categorias', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome: nomeInput.value })
    })
    .then(resposta => resposta.json())
    .then(dados => {
        nomeInput.value = ''; // Limpa a caixa de texto
        carregarCategorias(); // Atualiza a lista automaticamente no ecrã
    })
    .catch(erro => console.error('Erro ao guardar categoria:', erro));
}

// Executa a função de leitura assim que a página é aberta
window.onload = carregarCategorias;