## 3) Análise Sintática LL(1) das Cadeias

## Tabela LL(1)

| **Não-terminal** | **v**                | **p**                | **n**                | **s**                | **[**                | **]**                | **:**                | **$**        |
|-------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|--------------|
| `<expr>`          | `<var> [ <index> ]`  |                      |                      |                      |                      |                      |                      | `<EOF>`      |
| `<var>`           | `v`                  |                      |                      |                      |                      |                      |                      |              |
| `<index>`         |                      | `<num>`              | `<num>`              | `<str>`              | `<nested>`           |                      |                      |              |
| `<num>`           |                      | `p`                  | `n`                  |                      |                      |                      |                      |              |
| `<str>`           |                      |                      |                      | `s`                  |                      |                      |                      |              |
| `<slice>`         |                      | `<num> : <num>`      | `<num> : <num>`      | `<str> : <str>`      |                      |                      |                      |              |
| `<nested>`        | `v [ <index> ]`      |                      |                      |                      |                      |                      |                      |              |

---

## Análise da Cadeia `v [ v [ p : p ] ]`

### **Passo 1: Início**
A cadeia começa com `v`, que corresponde ao símbolo inicial `<expr>`. Na tabela, para `<expr>` com `v`, temos a produção:

```
<expr> ::= <var> [ <index> ]
```

Agora temos: `v [ <index> ]`

### **Passo 2: Analisando `<var>`**
O próximo símbolo é `v`, que corresponde à produção para `<var>`:

```
<var> ::= v
```

Agora temos: `[ <index> ]`

### **Passo 3: Analisando o `[` após `<var>`**
O próximo símbolo é `[`. De acordo com a tabela, para `<index>` com `[` devemos usar a produção `<nested>`, pois `[` é seguido por outra lista de expressões entre colchetes. A produção é:

```
<nested> ::= <var> [ <index> ]
```

Agora temos: `v [ <index> ]`

### **Passo 4: Analisando o próximo `<var>`**
O próximo símbolo é `v`. Usamos novamente a produção de `<var>`:

```
<var> ::= v
```

Agora temos: `[ <index> ]`

### **Passo 5: Analisando o `[` após o segundo `<var>`**
O próximo símbolo é `[`. Como estamos em `<index>`, utilizamos novamente a produção `<nested>`:

```
<nested> ::= <var> [ <index> ]
```

Agora temos: `v [ p : p ]`

### **Passo 6: Analisando o `p : p`**
Após o símbolo `[`, temos `p : p`, que corresponde à produção de `<slice>`:

```
<slice> ::= <num> : <num>
```

Analisamos o primeiro `p` com a produção de `<num>`:

```
<num> ::= p
```

Agora temos: `: p`

Em seguida, analisamos o segundo `p`:

```
<num> ::= p
```

Agora temos: `]`

### **Passo 7: Finalizando**
O próximo símbolo é `]`, que finaliza a cadeia. A análise está completa, e a cadeia foi derivada corretamente!

---

## Análise da Cadeia `v [ p : s ]`

### **Passo 1: Início**
A cadeia começa com `v`, que corresponde ao símbolo inicial `<expr>`. Na tabela, para `<expr>` com `v`, temos a produção:

```
<expr> ::= <var> [ <index> ]
```

Agora temos: `v [ <index> ]`

### **Passo 2: Analisando `<var>`**
O próximo símbolo é `v`, que corresponde à produção para `<var>`:

```
<var> ::= v
```

Agora temos: `[ <index> ]`

### **Passo 3: Analisando o `[` após `<var>`**
O próximo símbolo é `[`. De acordo com a tabela, para `<index>` com `[` devemos usar a produção `<slice>`, porque estamos lidando com índices e colchetes. A produção é:

```
<slice> ::= <num> : <num>
```

### **Passo 4: Analisando o `p : s`**
Após o símbolo `[`, temos `p : s`, que corresponde a um **slice** de números e strings.

Primeiro, analisamos o `p` com a produção de `<num>`:

```
<num> ::= p
```

Agora temos: `: s`

Em seguida, analisamos o `s` com a produção de `<str>`:

```
<str> ::= s
```

Agora temos: `]`

### **Passo 5: Finalizando**
O próximo símbolo é `]`, que finaliza a cadeia. A análise está completa, e a cadeia foi derivada corretamente!

---

- **Cadeia `v [ v [ p : p ] ]`**: A cadeia foi analisada corretamente utilizando a tabela LL(1), e as produções foram aplicadas conforme esperado.
- **Cadeia `v [ p : s ]`**: A cadeia também foi analisada corretamente utilizando a tabela LL(1), e as produções de números e strings foram aplicadas conforme a tabela.
