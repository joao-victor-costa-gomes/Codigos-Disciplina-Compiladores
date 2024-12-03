## 2) **Conjuntos NULLABLE, FIRST e FOLLOW**

### **Conjunto NULLABLE**

O conjunto **NULLABLE** contém os não-terminais que podem derivar a cadeia vazia (`ε`). Nesta gramática:

```plaintext
NULLABLE = {}
```

Nenhum não-terminal pode derivar diretamente a cadeia vazia, pois todas as produções requerem pelo menos um símbolo terminal.

---

### **Conjunto FIRST**

O conjunto **FIRST** define os símbolos terminais que podem aparecer no início de uma derivação para cada não-terminal.

| Não-terminal | FIRST                                      |
|--------------|-------------------------------------------|
| `<expr>`     | { `v` }                                   |
| `<var>`      | { `v` }                                   |
| `<index>`    | { `p`, `n`, `s`, `v`, `:` }               |
| `<nump>`     | { `p` }                                   |
| `<numn>`     | { `n` }                                   |
| `<str>`      | { `s` }                                   |
| `<nested>`   | { `v` }                                   |
| `<slice>`    | { `:`, `p`, `n`, `s` }                    |

---

### **Conjunto FOLLOW**

O conjunto **FOLLOW** contém os símbolos terminais que podem aparecer imediatamente após cada não-terminal em alguma derivação.

| Não-terminal | FOLLOW               |
|--------------|----------------------|
| `<expr>`     | { `$` }             |
| `<var>`      | { `[` }             |
| `<index>`    | { `]` }             |
| `<nump>`     | { `:`, `]` }        |
| `<numn>`     | { `:`, `]` }        |
| `<str>`      | { `:`, `]` }        |
| `<nested>`   | { `]` }             |
| `<slice>`    | { `]` }             |

---