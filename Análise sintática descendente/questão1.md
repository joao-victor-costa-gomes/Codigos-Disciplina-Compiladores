## 1) **Gramática que reconhece as cadeias**

A gramática que define o formato das cadeias, utilizando variáveis, números e strings transformados em letras, é definida como:

```bnf
<expr>    ::= <var> [ <index> ]
<var>     ::= v
<index>   ::= <num> | <str> | <slice> | <nested>
<num>     ::= p | n
<str>     ::= s
<slice>   ::= <num> : <num> | <str> : <str> | <num> : <str> | <str> : <num>
<nested>  ::= <var> [ <index> ]
```

### Explicação:
- **`<expr>`**: Representa uma expressão principal, composta de uma variável (`<var>`) e um índice (`<index>`), entre colchetes.
- **`<var>`**: Nome da variável, representado por `v`.
- **`<index>`**: Pode ser:
  - Um número (`<num>`).
  - Uma string (`<str>`).
  - Um slice (`<slice>`).
  - Um índice aninhado (`<nested>`), ou seja, outro acesso a uma variável.
- **`<num>`**: Representa números positivos/zero (`p`) ou negativos (`n`).
- **`<str>`**: Representa strings (`s`).
- **`<slice>`**: Um intervalo (slice) de números ou strings separados por `:`.
- **`<nested>`**: Permite acessar índices que são eles mesmos acessos a outras variáveis.

---


