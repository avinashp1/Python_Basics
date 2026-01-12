### Purpose
Help an AI coding agent be productive in this repository by describing the architecture, key files, and project-specific conventions.

### Big picture
- This is a small, single-package Python project with three logical layers:
  - Models: `models/` holds plain Python data/domain classes (`models/person.py`, `models/student.py`). Student subclasses Person and implements `introduce()`.
  - Services: `services/` contains business logic (in-memory state). `services/student_service.py` manages `Student` objects in a simple list.
  - Utilities: `utils/` contains helpers with static methods. `utils/file_manager.py` provides `save_to_file` / `load_from_file` that read/write JSON files.

### Key files to inspect (quick links)
- [main.py](main.py#L1-L13): simple runner that uses `StudentService` and `FileManager`.
- [models/student.py](models/student.py#L1-L12): shows model inheritance pattern.
- [services/student_service.py](services/student_service.py#L1-L20): shows the pattern for service classes (in-memory list, add/list methods).
- [utils/file_manager.py](utils/file_manager.py#L1-L20): file I/O utilities; used by `main.py` to persist student introductions.

### Project-specific conventions
- Small, explicit modules; prefer small classes over frameworks. Follow existing naming: `XService` for service classes, `FileManager` for I/O utilities.
- Services keep state in memory (lists). Avoid adding external DB layers unless asked—persisting is done via `FileManager.save_to_file` in callers.
- Utilities use `@staticmethod` and operate on raw Python types (lists/strings/JSON). Mimic this style when adding helpers.

### Typical data flow / example
- `main.py` constructs `StudentService`, calls `add_student(name, age, id)`, then `list_students()` to get a list of strings; finally `FileManager.save_to_file("students.json", students)` persists JSON.
- When modifying the flow, preserve the separation: service returns domain objects or simple serializable lists; `FileManager` handles only serialization.

### Developer workflows (how to run / debug)
- Run the app from repository root:

  ```powershell
  python main.py
  ```

- There is no test runner configured. If adding tests, prefer `pytest` and place tests under `tests/`.

### Guidelines for AI edits
- Keep changes minimal and idiomatic to existing code: small functions, clear names, no new frameworks.
- When changing persistence, update callers in `main.py` instead of changing `StudentService` unless explicitly migrating to a DB.
- If adding new utility functions, place them under `utils/` as `@staticmethod` helpers and use simple types (dict/list).
- When editing models, preserve `introduce()` semantics: return a human-readable string used by `list_students()`.

### Patterns & examples to follow
- Add a new service method:

  - Follow `StudentService` style: mutates `self.students` and returns the created object.

- Persisting output: call `FileManager.save_to_file(filename, data)` with serializable `data` (e.g., list of strings).

### Integration points / risks
- File I/O is synchronous and uses filesystem paths relative to the current working directory — prefer explicit paths in changes.
- No concurrency controls: if you add async code or threads, ensure service state is protected.

If any part of this is unclear or you want me to include examples for contributing changes (e.g., a new persistence adapter or tests), tell me which area to expand.