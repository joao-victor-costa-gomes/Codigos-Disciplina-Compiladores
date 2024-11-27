## 2) **Conjuntos NULLABLE, FIRST e FOLLOW**

### **Conjunto NULLABLE**

O conjunto **NULLABLE** contém não-terminais que podem derivar a cadeia vazia (`ε`). No caso desta gramática:

```plaintext
NULLABLE = {}
```

Nenhum símbolo pode derivar `ε`, pois sempre é necessário pelo menos um token para cada produção.

---

### **Conjunto FIRST**

O conjunto **FIRST** define os símbolos que podem aparecer no início de uma derivação para cada não-terminal.

| Não-terminal | FIRST                   |
|--------------|-------------------------|
| `<expr>`     | { `v` }                |
| `<var>`      | { `v` }                |
| `<index>`    | { `p`, `n`, `s`, `v` } |
| `<num>`      | { `p`, `n` }           |
| `<str>`      | { `s` }                |
| `<slice>`    | { `p`, `n`, `s` }      |
| `<nested>`   | { `v` }                |

---

### **Conjunto FOLLOW**

O conjunto **FOLLOW** contém os símbolos que podem seguir um não-terminal em uma derivação.

| Não-terminal | FOLLOW          |
|--------------|-----------------|
| `<expr>`     | { `EOF`, `]` } |
| `<var>`      | { `[`, `EOF` } |
| `<index>`    | { `]` }         |
| `<num>`      | { `:`, `]` }    |
| `<str>`      | { `:`, `]` }    |
| `<slice>`    | { `]` }         |
| `<nested>`   | { `]` }         |

---