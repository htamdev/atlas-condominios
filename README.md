# Atlas Condomínios · Painel de gestão

Painel web para consultar condomínios, administradoras, síndicos, siglas e honorários,
com relatórios operacionais e quadro por colaborador. Projeto de demonstração: todos
os dados e nomes são fictícios.

## Funcionalidades
- Menu com busca global e contador de condomínios ativos
- Administradoras, Síndicos e Siglas/Honorários: busca, filtros por coluna, ordenação,
  detalhes em janela e colunas configuráveis
- Relatórios: indicadores, tabelas de status, comparativo mensal e quadro Kanban por colaborador,
  com atualização automática a cada 30 segundos
- Importação de planilhas CSV (a cada abertura de tela) e cache dos dados

## Como rodar
- **Com servidor local:** `python server.py` e abrir http://localhost:8000
- **Hospedagem estática (GitHub Pages):** funciona sem servidor; os dados editados ficam no navegador

## Dados
As planilhas de exemplo estão em `planilhas/`. Para usar o Google Sheets, publique a aba como CSV
e cole o link na constante `LINK_GOOGLE_SHEETS` de cada `script_*.js`.
Painel administrativo: `ENABLE_ADMIN` em `config.js` (senha de demonstração `demo@2026`).
