<p align="center">
  <img src="banner.png" alt="Pyrus Banner" width="100%">
</p>

<p align="center">
  <a href="https://security-labor.github.io/pyrus/">
    <img src="https://img.shields.io/badge/docs-security--labor.github.io%2Fpyrus-8b5cf6" alt="Docs Oficiais">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Licença: MIT">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python: 3.8+">
  </a>
  <a href="https://github.com/Security-Labor/Pyrus">
    <img src="https://img.shields.io/badge/status-pre--alpha-red" alt="Status: Pré-Alpha">
  </a>
</p>

# 🏺 Linguagem de Programação Pyrus (v0.1.0.0 Alpha)

**Pyrus** é uma linguagem de programação orientada a sistemas, projetada para engenheiros e especialistas em automação. Ela preenche a lacuna entre a prototipagem rápida do Python e a execução rígida e segura exigida por aplicações industriais e de segurança.

---

## 🚀 A Visão Principal
A Pyrus nasceu dentro do ecossistema **Security-Labor** para fornecer uma ferramenta que seja:
- **Previsível:** Sintaxe rígida com uso obrigatório de ponto e vírgula.
- **Focada em Matemática:** Manipulação de alta precisão para cálculos de engenharia (Vazão, Pressão, Carga de Rede).
- **Concorrente:** Projetada desde o início para operações `spawn` e tarefas assíncronas.
- **Extensível:** Integração contínua com ferramentas baseadas em Python e futura compilação LLVM.

## ✨ Funcionalidades (v0.1.0.0)
- **Sistema de Tipos Híbrido:** Detecção automática de `String`, `Int` e `Float`.
- **Mecanismo Matemático Recursivo:** Suporte para expressões complexas como `var x = (a + b) * (c / d);`.
- **CLI para Desenvolvedores:** Uma interface de linha de comando robusta para executar arquivos `.pyu`.
- **Suporte a Comentários:** Sintaxe `//` integrada para documentação de código.

## 🛠️ Início Rápido

### 1. Instalação
A Pyrus requer o mecanismo de parsing **Lark**. Instale-o via terminal (Termux, CMD ou Linux):

```bash
pip install lark
```
**2. Seu Primeiro Script (main.pyu)**
Crie um arquivo com a extensão .pyu:

```bash
Rust
// Exemplo de Automação Pyrus
var target = "192.168.1.1";
var base_freq = 60;
var multiplier = 1.5;

var final_freq = base_freq * multiplier;

print("Sistema Alvo:");
print(target);
print("Frequência Calibrada:");
print(final_freq);
```
**3. Executando o Código**
Navigate to the src folder and execute:

```Bash
python pyrus.py run ../examples/main.pyu
```
**🗺️ Roadmap para π**
[x] v0.0.0.0: Prova de Conceito de Lexer/Parser.

[x] v0.1.0.0: Mecanismo Matemático e Tipos Numéricos.

[ ] v0.2.0.0: Fluxo Lógico (if/else) e Álgebra Booleana.

[ ] v0.3.0.0: Loops (while, for) e estruturas de Lista.

[ ] v0.5.0.0: Sistema de Propriedade de Memória (Ownership) e Empréstimo (Borrowing).

[ ] v1.0.0.0: Integração nativa com Backend LLVM.

**🛡️ Security & Labor**
Pyrus é um projeto de código aberto mantido pela Security-Labor Foundation. Acreditamos em ferramentas que empoderam o usuário através de transparência e desempenho.

**Website**: AAD-Systems.github.io/pyrus

**Organização**: github.com/AAD-Systems

**Desenvolvido em Alagoas, Brasil.🇧🇷**
