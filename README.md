# structured-refusal-boundary

## Français

Refuser les sorties structurées incomplètes ou refusées.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m structured_refusal_boundary examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Frontière déterministe sur traces normalisées : refus, terminal unique, JSON entier et choix admissibles. Un JSON valide ne suffit pas à rendre un tour incomplet utilisable.

### Limites

Schéma plat à enums seulement, pas adaptateur fournisseur ni validation JSON Schema générale. Ne juge ni vérité ni pertinence.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reject incomplete or refused structured outputs.

Synthetic data; no network access or secret required.

```sh
python -m structured_refusal_boundary examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Deterministic boundary over normalized traces: refusal, unique terminal, complete JSON and admissible choices. Valid JSON alone does not make an incomplete turn usable.

### Limits

Flat enum schema only, no provider adapter or general JSON Schema validation. Does not judge truth or relevance.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Rechazar salidas estructuradas incompletas o rechazadas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m structured_refusal_boundary examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Límite determinista sobre trazas normalizadas: rechazo, terminal único, JSON completo y opciones admisibles. JSON válido no vuelve utilizable un turno incompleto.

### Límites

Solo esquema plano de enums, sin adaptador de proveedor ni validación JSON Schema general. No juzga veracidad ni pertinencia.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://json-schema.org/understanding-json-schema/reference/enum
