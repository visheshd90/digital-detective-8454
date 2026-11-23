
## Task 4.1 — Create and run a Python program
* **File created:** `hello.py`
* **Program code:** `print("Hello from Python")`
* **Execution command:** `python3 hello.py`
* **Observation / Verification:** The terminal successfully executed the script via Python 3 and outputted `Hello from Python`.

## Task 4.2 — Compare compiler and interpreter

### Comparison Table:
| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire source code into machine code all at once *before* execution. | Translates and executes the source code line-by-line (or statement-by-statement) at *runtime*. |
| **Typical output** | Generates a standalone executable file or object code. | Produces direct execution results/output on the screen without creating a separate binary. |
| **One example** | GCC (GNU Compiler Collection) for C/C++. | Python interpreter (CPython). |
| **One advantage** | Offers faster execution speed once compiled since translation is already complete. | Easier debugging and platform independence, allowing immediate execution and error checking. |

### Summary Explanation:
A compiler translates the entire source code into machine code prior to execution, generating a standalone executable file that runs very efficiently. In contrast, an interpreter translates and executes code line-by-line at runtime, which provides immediate feedback and simplifies error tracking during development. While compilers prioritize fast execution performance, interpreters offer greater flexibility and cross-platform ease of use.
