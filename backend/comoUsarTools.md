# Cómo usar los Tools correctamente

## Tool: `edit`

### Parámetros correctos (sin underscores):

```python
edit(
    filePath="ruta/al/archivo.md",
    oldString="texto a buscar",
    newString="nuevo texto"
)
```

### Errores comunes:
- ❌ `file_path` (con underscore) → debe ser `filePath`
- ❌ `old_string` → debe ser `oldString`
- ❌ `new_string` → debe ser `newString`

---

## Tool: `read`

```python
read(
    filePath="ruta/al/archivo.md",
    offset=1,      # línea inicial (opcional)
    limit=2000      # máximo de líneas (opcional)
)
```

---

## Tool: `write`

```python
write(
    content="contenido del archivo",
    filePath="ruta/nuevo_archivo.md"
)
```

---

## Tool: `glob`

```python
glob(pattern="**/*.md")  # busca todos los .md recursivamente
```

---

## Tool: `grep`

```python
grep(
    pattern="texto a buscar",
    path="ruta/al/directorio",  # opcional
    include="*.md"              # filtro de archivos, opcional
)
```

---

## Resumen de convención de nombres:

| Tool | Parámetro correcto | Erróneo |
|------|-------------------|---------|
| `edit` | `filePath`, `oldString`, `newString` | `file_path`, `old_string`, `new_string` |
| `read` | `filePath`, `offset`, `limit` | `_` versions |
| `write` | `content`, `filePath` | `_` versions |
| `glob` | `pattern`, `path` | `_` versions |
| `grep` | `pattern`, `path`, `include` | `_` versions |

---

**Nota:** Todos los parámetros usan camelCase (primera palabra minúscula, siguientes mayúsculas), **no** snake_case.
