## 1) **Gramática que reconhece as cadeias**

A gramática que define o formato das cadeias, utilizando variáveis, números e strings transformados em letras, é definida como:

```bnf
<expr>    ::= <var> '[' <index> ']'
<var>     ::= v
<index>   ::= <nump> | <numn> | <str> | <nested> | <slice>
<nump>    ::= p
<numn>    ::= n
<str>     ::= s
<nested>  ::= <var> '[' <index> ']'
<slice>   ::= <str> ':' <str> | <str> ':' | ':' <str> | ':' | <nump> ':' <nump> | <nump> ':' | ':' <nump> | <numn> ':' <numn> | <numn> ':' | ':' <numn>
```

### Explicação:
- **`<expr>`**: Representa uma expressão principal, composta de uma variável (`<var>`) e um índice (`<index>`) entre colchetes.
- **`<var>`**: Nome da variável, representado por `v`.
- **`<index>`**: Pode ser um dos seguintes:
  - **Número positivo/negativo** (`<nump>` ou `<numn>`), representado por `p` (positivo) ou `n` (negativo).
  - **String** (`<str>`), representada por `s`.
  - **Intervalo (slice)** (`<slice>`), que pode ser formado por dois números, duas strings, ou limites opcionais (omitindo um dos valores).
  - **Índice aninhado** (`<nested>`), que é um acesso a uma variável com um índice, formando uma expressão mais complexa.
- **`<nump>`**: Representa números positivos/zero, indicado por `p`.
- **`<numn>`**: Representa números negativos, indicado por `n`.
- **`<str>`**: Representa strings, indicadas por `s`.
- **`<slice>`**: Um intervalo de números ou strings separados por `:`. Pode ter as seguintes variações:
  - `str:str` (intervalo entre duas strings),
  - `str:` (um intervalo com limite inferior como string),
  - `:str` (um intervalo com limite superior como string),
  - `:` (intervalo sem limites),
  - `nump:nump` (intervalo entre dois números positivos),
  - `nump:` (um intervalo com limite inferior como número),
  - `:nump` (um intervalo com limite superior como número),
  - `numn:numn` (intervalo entre dois números negativos),
  - `numn:` (um intervalo com limite inferior como número negativo),
  - `:numn` (um intervalo com limite superior como número negativo).
- **`<nested>`**: Permite acessar índices que são, eles mesmos, acessos a outras variáveis, representando uma expressão aninhada de variáveis e índices entre colchetes.

---
