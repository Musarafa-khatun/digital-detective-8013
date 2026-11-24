# Mission 4 — How Programs Run

## 1. Task / objective
The objective of this mission is to write and execute a simple Python program (`hello.py`), confirm its output in the macOS Terminal, and understand how programming languages translate source code by comparing compilers and interpreters.

## 2. Work completed
- Created `mission-04-programs/hello.py` containing a single `print("Hello from Python")` statement.
- Executed the program using `python3 mission-04-programs/hello.py` and confirmed the expected output printed to the terminal.
- Analyzed the key differences between compilation and interpretation, including translation timing, output format, examples, and trade-offs.
- Highlighted modern hybrid approaches, such as how Python compiles code into intermediate bytecode (`.pyc`) before running it on the Python Virtual Machine (PVM).

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py`: Used Python 3 runtime to interpret and execute the script.
- Terminal output verification: Confirmed `Hello from Python`.

## 4. My understanding

### Task 4.1 — Python execution observation
Executing `python3 mission-04-programs/hello.py` directly produced:
```text
Hello from Python
```
Python takes the human-readable source text in `hello.py`, parses it into bytecode, and immediately executes the instructions via its virtual machine without requiring a separate compilation and linking step by the user.

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation / execution happens** | Translates the entire source code into machine code or binary executable all at once before the program can run. | Translates and executes the program instruction-by-instruction or statement-by-statement at runtime. |
| **Typical output** | A standalone executable file (such as an `.exe` file on Windows or a Mach-O binary on macOS). | Immediate execution of instructions; usually no permanent standalone executable file is saved. |
| **One example** | C, C++, or Rust. | Python, JavaScript, or Ruby. |
| **One advantage** | Runs significantly faster because the code is already translated into native machine instructions ahead of time. | Much easier to test and debug because code can be run immediately without a lengthy build step. |

---

### Explanation in my own words
A compiler takes a high-level source code file and converts the entire program into low-level machine code that the CPU can execute directly. Once compiled, the program runs independently and very quickly, but any change requires recompiling the entire code. In contrast, an interpreter reads high-level source code line-by-line and executes each command on the fly. This makes testing, experimenting, and finding errors much faster during development, though line-by-line interpretation has more runtime overhead. In practice, many modern languages combine both: for instance, Python first compiles source code into intermediate bytecode and then interprets that bytecode on the Python Virtual Machine (PVM).

## 5. Difficulties faced
- Understanding whether Python is strictly an interpreter or if compilation is involved.

## 6. How I resolved them
- Learned that Python uses a hybrid approach: CPython silently compiles `.py` files into intermediate `.pyc` bytecode, which is then executed line-by-line by the Python interpreter.

## 7. Evidence / files
- Python program: [mission-04-programs/hello.py](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-04-programs/hello.py)
- Mission documentation: [mission-04-programs/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-04-programs/README.md)

## 8. Commit details
- **Commit message**: `Compare compilers and interpreters`
- **Branch**: `main`
- **Remote status**: Pushed and verified on GitHub.
