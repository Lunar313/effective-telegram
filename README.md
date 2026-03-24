# effective-telegram – Kleine Projekte

Eine Sammlung kleiner Python-Hilfsprojekte (**Kleine Projekte**).

## Enthaltene Projekte

| Modul | Beschreibung |
|-------|--------------|
| `Calculator` | Einfacher Taschenrechner (Grundrechenarten) |
| `TodoList` | In-Memory-Aufgabenliste |

## Installation

```bash
pip install -r requirements.txt
```

## Verwendung

### Calculator

```python
from kleine_projekte import Calculator

calc = Calculator()
print(calc.add(3, 4))        # 7
print(calc.multiply(6, 7))   # 42
print(calc.divide(10, 2))    # 5.0
```

### TodoList

```python
from kleine_projekte import TodoList

todo = TodoList()
todo.add("Einkaufen gehen")
todo.add("Tests schreiben")
todo.complete(0)

print(todo)
# [✓] Einkaufen gehen
# [○] Tests schreiben

print(f"Offene Aufgaben: {len(todo.pending())}")
```

## Tests ausführen

```bash
pytest
```