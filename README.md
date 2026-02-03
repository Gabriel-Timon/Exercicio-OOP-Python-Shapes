<div align="center">

<h1>📐 Shapes em Python (POO) — Área & Comprimento</h1>

<p>
  Um mini-projeto em <b>Python</b> para treinar <b>Programação Orientada a Objetos</b> com herança, classe abstrata e polimorfismo,
  calculando <b>área</b> e <b>comprimento/perímetro</b> de diferentes formas geométricas.
</p>

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img alt="Paradigma" src="https://img.shields.io/badge/POO-OOP-success" />
  <img alt="Status" src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" />
</p>

</div>

<br/>

<a id="sumario"></a>
<h2>🧭 Sumário</h2>

<ul>
  <li><a href="#sobre">Sobre o projeto</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#estrutura">Estrutura de pastas</a></li>
  <li><a href="#requisitos">Requisitos</a></li>
  <li><a href="#como-rodar">Como rodar</a></li>
  <li><a href="#como-funciona">Como funciona</a></li>
  <li><a href="#exemplo">Exemplo de saída</a></li>
  <li><a href="#adicionar-shape">Como adicionar um novo shape</a></li>
  <li><a href="#notas">Notas & possíveis melhorias</a></li>
</ul>

<hr/>

<a id="sobre"></a>
<h2>✨ Sobre o projeto</h2>

<p>
  A ideia aqui é simples e objetiva: criar formas geométricas como classes e padronizar o contrato delas
  através de uma classe abstrata chamada <code>Shape</code>.
</p>

<p>
  Cada shape implementa:
</p>

<ul>
  <li><b>area()</b> → retorna a área</li>
  <li><b>comprimento()</b> → retorna o comprimento/circunferência/perímetro</li>
</ul>

<p>
  Além disso, toda forma criada entra automaticamente numa lista interna (<code>Shape.lista_shapes</code>),
  permitindo listar tudo de uma vez (áreas e comprimentos) no terminal.
</p>

<p align="right"><a href="#sumario">⬆️ voltar ao topo</a></p>

<hr/>

<a id="features"></a>
<h2>🚀 Features</h2>

<ul>
  <li>✅ Classe abstrata (<code>ABC</code>) definindo contrato (<code>area</code> e <code>comprimento</code>)</li>
  <li>✅ Herança e polimorfismo: cada shape calcula de um jeito, mas com a mesma interface</li>
  <li>✅ Lista global de instâncias (<code>Shape.lista_shapes</code>) para consolidar resultados</li>
  <li>✅ CLI simples no terminal para exibir áreas ou comprimentos</li>
  <li>✅ Implementações: <b>Quadrado</b>, <b>Círculo</b>, <b>Retângulo</b>, <b>Triângulo</b></li>
</ul>

<p align="right"><a href="#sumario">⬆️ voltar ao topo</a></p>

<hr/>

<a id="estrutura"></a>
<h2>🗂️ Estrutura de pastas</h2>

<pre>
.
├── app.py
└── models/
    ├── shape.py
    ├── circulo.py
    ├── quadrado.py
    ├── retangulo.py
    └── triangulo.py
</pre>

<p>
  <b>Dica:</b> se você estiver organizando como pacote Python, crie também um <code>models/__init__.py</code> (pode ser vazio).
</p>

<p align="right"><a href="#sumario">⬆️ voltar ao topo</a></p>

<hr/>

<a id="requisitos"></a>
<h2>🧩 Requisitos</h2>

<ul>
  <li><b>Python 3.10+</b> (o projeto usa <code>match/case</code>)</li>
</ul>

<p align="right"><a href="#sumario">⬆️ voltar ao topo</a></p>

<hr/>

<a id="como-rodar"></a>
<h2>▶️ Como rodar</h2>

<ol>
  <li>Clone o repositório:</li>
</ol>

```bash
git clone SEU_LINK_AQUI
cd SEU_REPO_AQUI
