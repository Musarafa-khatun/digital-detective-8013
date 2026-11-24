# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
The objective of this mission is to practice essential command-line interface (CLI) operations in macOS Terminal within an isolated practice folder, master file creation, modification, copying, renaming, inspect file listings with different flags, practice command piping, and understand how package managers function.

## 2. Work completed
- Explored core Terminal operations (`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Created a safe isolated working folder `terminal-practice` inside the repository.
- Practiced safe file modifications: creating a file, writing content with redirect (`>`), appending text with append (`>>`), making a duplicate with `cp`, and renaming files with `mv`.
- Analyzed command flags (`-l`, `-a`, `-h`) and compared human-readable vs. default byte output.
- Demonstrated command piping by combining `ls -la` with `head -n 5`.
- Verified Homebrew installation (`Homebrew 7.0.9`) on Apple Silicon macOS (`/opt/homebrew/bin/brew`).

## 3. Commands / tools used
- `pwd`: Prints the full absolute path of the current working directory.
- `ls`: Lists files and directories in the current folder.
- `ls -l`: Displays detailed file listings including permissions, owners, file size, and modification timestamp.
- `ls -lah`: Combines long listing (`-l`), hidden files (`-a`), and human-readable units like KB/MB (`-h`).
- `cd`: Changes the current working directory.
- `mkdir`: Creates a new folder/directory.
- `touch`: Creates an empty file or updates timestamps.
- `echo "text" > file`: Overwrites file content with new text.
- `echo "text" >> file`: Appends new text to the end of a file without overwriting.
- `cat`: Concatenates and displays file contents on the screen.
- `cp`: Copies files or directories.
- `mv`: Moves or renames files or directories.
- `|` (Pipe): Streams the standard output of one command into the standard input of another.
- `brew --version`: Checked the installed Homebrew package manager version.

## 4. My understanding

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
|---|---|---|
| **Current-directory display (`pwd`)** | Displays the full absolute path of the directory you are currently in. | Output showed the full path `/Users/[redacted]/Desktop/S$AI assignment/digital-detective-8013/terminal-practice`. |
| **Directory listing (`ls`)** | Lists names of non-hidden files and directories in the current folder. | Showed file names cleanly without extra metadata. |
| **Detailed listing (`ls -l`)** | Displays permissions, link count, owner, group, byte size, and last modified date. | Columns appeared showing `-rw-r--r--`, user, staff, size in bytes, and timestamp. |
| **Change directory (`cd ..`)** | Moves current location up one level to the parent directory. | Prompt path changed to the parent `digital-detective-8013` directory. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new subdirectory with the specified name. | New folder was created and visible in subsequent `ls`. |
| **Create empty file (`touch sample.txt`)** | Creates a new 0-byte file if it does not exist, or updates its timestamp. | An empty file `sample.txt` was created. |
| **Copy file (`cp sample.txt sample_backup.txt`)** | Duplicates an existing file into a new independent file. | Both `sample.txt` and `sample_backup.txt` existed side-by-side with identical contents. |
| **Move / rename file (`mv sample_backup.txt notes.txt`)** | Renames a file or moves it to another directory path. | `sample_backup.txt` disappeared and was renamed to `notes.txt`. |
| **Display file contents (`cat sample.txt`)** | Reads text from a file and prints it directly in the terminal window. | Printed the stored text lines directly to standard output. |

---

### Task 2.2 — Practise file changes safely

- **Difference between replacing (`>`) and appending (`>>`)**:
  Using `>` overwrites the destination file completely from scratch; whatever was inside is lost. Using `>>` preserves existing contents and appends new lines at the end of the file.
- **Difference between copying (`cp`) and moving (`mv`)**:
  `cp` creates an identical second copy, leaving the original file intact in its location. `mv` relocates or renames the file so only one instance remains.
- **Information provided by `pwd`**:
  It shows the absolute path starting from the root directory `/`, giving an exact, unambiguous location in the filesystem.
- **Why a directory listing is useful**:
  It lets you verify that files were created, check file sizes, inspect permissions, and confirm the names of files before running commands on them.

---

### Task 2.3 — Understand flags and pipes

- **Flags (`-l`, `-a`, `-h`)**:
  - `ls`: Shows only visible file names horizontally.
  - `ls -l`: Shows a vertical list with file modes/permissions, owner, group, exact size in bytes, date, and name.
  - `ls -a`: Reveals hidden entries (names beginning with a dot `.`), including `.` (current folder) and `..` (parent folder).
  - `ls -lah`: Displays sizes with human-readable units (`74B`, `480B`, etc.) instead of raw bytes, making large files easier to understand at a glance.
- **Pipes (`|`)**:
  - In `ls -la | head -n 5`, the pipe symbol `|` takes the text stream generated by `ls -la` (which could be hundreds of lines) and routes it directly as input to `head -n 5`.
  - The left side produces the full listing; the right side consumes it and filters it to display only the top 5 lines.

---

### Task 2.4 — Understand package managers
Homebrew is installed on my macOS system (`Homebrew 7.0.9` at `/opt/homebrew/bin/brew`).
Package managers are command-line tools that automate the installation, updating, dependency management, and uninstallation of software packages. Instead of searching the web for an installer, downloading DMG files, and manually dragging files, a single command like `brew install <tool>` downloads the correct binaries, installs missing dependencies, and puts them into your system path safely.

## 5. Difficulties faced
- In terminal scripting, directory paths containing special symbols like `$` require careful quoting (e.g. `'S$AI assignment'`) to prevent the shell from interpreting them as variables.

## 6. How I resolved them
- Used single quotes around directory paths in terminal commands, ensuring that spaces and dollar signs are treated as literal text.

## 7. Evidence / files
- Created directory: `terminal-practice/`
- Practice files: `terminal-practice/sample.txt` and `terminal-practice/notes.txt`
- Mission documentation: [mission-02-terminal/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-02-terminal/README.md)

## 8. Commit details
- **Commit message**: `Complete Terminal and file management mission`
- **Branch**: `main`
- **Remote status**: Pushed and verified on GitHub.
