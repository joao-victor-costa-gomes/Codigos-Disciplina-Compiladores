
## Questão 3: Construção da Tabela de Análise Sintática LL(1)

## **Tabela LL(1)**

Com base nos conjuntos **FIRST** e **FOLLOW**, a tabela LL(1) é construída como segue:

| **Não-terminal** | **v**                     | **p**                     | **n**                     | **s**                     | **[** | **]** | **:**                     | **$** |
|-------------------|---------------------------|---------------------------|---------------------------|---------------------------|-------|-------|---------------------------|-------|
| **expr**          | `expr → var '[' index ']'` |                           |                           |                           |       |       |                           |       |
| **var**           | `var → v`                |                           |                           |                           |       |       |                           |       |
| **index**         | `index → nested`         | `index → nump`            | `index → numn`            | `index → str`             |       |       | `index → slice`          |       |
| **nump**          |                           | `nump → p`                |                           |                           |       |       |                           |       |
| **numn**          |                           |                           | `numn → n`                |                           |       |       |                           |       |
| **str**           |                           |                           |                           | `str → s`                 |       |       |                           |       |
| **nested**        | `nested → var '[' index ']'` |                           |                           |                           |       |       |                           |       |
| **slice**         |                           | `slice → nump ':' nump`   | `slice → numn ':' numn`   | `slice → str ':' str`     |       |       | `slice → ':'`            |       |

---

## **Análise das Cadeias**

### **Cadeia 1: `v [ v [ p : p ] ]`**

1. **Passo 1:** Começamos com `<expr>`:
   - A entrada começa com `v`, então seguimos a produção:
     ```
     expr → var '[' index ']'
     ```

2. **Passo 2:** Processamos `<var>`:
   - O próximo símbolo é `v`, então usamos a produção:
     ```
     var → v
     ```

3. **Passo 3:** Processamos `[` e chamamos `<index>`:
   - A entrada agora é `[`, seguido por um índice. O próximo símbolo é `v`, então seguimos a produção:
     ```
     index → nested
     ```

4. **Passo 4:** Processamos `<nested>`:
   - O próximo símbolo é `v`, então seguimos:
     ```
     nested → var '[' index ']'
     ```

5. **Passo 5:** Processamos `<var>` novamente:
   - Usamos:
     ```
     var → v
     ```

6. **Passo 6:** Processamos outro `[` e chamamos `<index>`:
   - O próximo símbolo é `p`, seguido por `:`, então seguimos:
     ```
     index → slice
     ```

7. **Passo 7:** Processamos `<slice>`:
   - O próximo símbolo é `p`, então usamos:
     ```
     slice → nump ':' nump
     ```

8. **Passo 8:** Processamos os dois números (`p`) e o `:`:
   - Para o primeiro `p`, usamos:
     ```
     nump → p
     ```
   - Para o segundo `p`, usamos novamente:
     ```
     nump → p
     ```

9. **Passo 9:** Processamos o fechamento de colchetes (`]`) e terminamos a análise.

**Resultado:** A cadeia `v [ v [ p : p ] ]` é **aceita**.

---

### **Cadeia 2: `v [ p : s ]`**

1. **Passo 1:** Começamos com `<expr>`:
   - A entrada começa com `v`, então seguimos a produção:
     ```
     expr → var '[' index ']'
     ```

2. **Passo 2:** Processamos `<var>`:
   - O próximo símbolo é `v`, então usamos a produção:
     ```
     var → v
     ```

3. **Passo 3:** Processamos `[` e chamamos `<index>`:
   - A entrada agora é `[`, seguido por um índice. O próximo símbolo é `p`, então verificamos as produções:
     ```
     index → nump | numn | str | nested | slice
     ```

4. **Tentativas de Produções:**
   - Para `index → nump`, `nump` consome apenas o `p`, mas não cobre o `:`.
   - Para `index → slice`, verificamos as produções de `slice`:
     ```
     slice → str ':' str | str ':' | ':' str | ':' 
             | nump ':' nump | nump ':' | ':' nump 
             | numn ':' numn | numn ':' | ':' numn
     ```
     Nenhuma produção permite `nump ':' str`.

5. **Conclusão:** Nenhuma produção cobre o caso `p : s`.

**Resultado:** A cadeia `v [ p : s ]` **não é aceita** pela gramática.

---

## **Conclusão**

1. A tabela LL(1) foi construída com base nos conjuntos **FIRST** e **FOLLOW**.
2. **Cadeia 1: `v [ v [ p : p ] ]`**:
   - A cadeia foi analisada corretamente e é **aceita** pela gramática.
3. **Cadeia 2: `v [ p : s ]`**:
   - A cadeia **não é aceita** pela gramática, pois não existe uma produção que permita `p : s`.

