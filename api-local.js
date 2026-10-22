// Camada de dados: usa o servidor (server.py) quando ele existe e,
// caso contrário (ex.: GitHub Pages), guarda tudo no navegador.
(function () {
  var BASE = new URL('.', document.currentScript.src).href;
  var realFetch = window.fetch.bind(window);
  var chave = function (n) { return 'atlas_' + n; };
  var json = function (o, s) {
    return new Response(JSON.stringify(o), { status: s || 200, headers: { 'Content-Type': 'application/json' } });
  };
  async function lerLocal(nome) {
    try { var v = localStorage.getItem(chave(nome)); if (v) return JSON.parse(v); } catch (e) {}
    try {
      var r = await realFetch(BASE + 'dados_banco/' + nome + '.json');
      if (r.ok) return await r.json();
    } catch (e) {}
    return { columns: [], data: [] };
  }
  window.fetch = async function (input, init) {
    var url = typeof input === 'string' ? input : ((input && input.url) || '');
    var m = url.match(/\/api\/(adm|honor|sindicos)(?:[?#].*)?$/);
    if (!m) return realFetch(input, init);
    var nome = m[1];
    var metodo = ((init && init.method) || 'GET').toUpperCase();
    try {
      var r = await realFetch(input, init);
      if (r.ok) return r;
    } catch (e) {}
    if (metodo === 'POST') {
      try { localStorage.setItem(chave(nome), init.body); } catch (e) {}
      return json({ status: 'sucesso' });
    }
    return json(await lerLocal(nome));
  };
})();
