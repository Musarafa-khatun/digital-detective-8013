# Mission 3 — Understand the Operating System

## 1. Task / objective
The objective of this mission is to explore how the macOS operating system functions, examine running processes and process IDs (PIDs), inspect available and used secondary storage, analyze absolute vs. relative filesystem paths, understand file permissions, and explain the core responsibilities of an operating system.

## 2. Work completed
- Queried system information and kernel details using `uname` and `sw_vers`.
- Inspected disk space and volume allocations using `df -h`.
- Analyzed running background and foreground processes using `ps aux`.
- Examined file permission flags (`-rw-r--r--`) on a practice file.
- Compared absolute vs. relative file paths with examples from this repository.
- Documented the six major responsibilities of an operating system with clear definitions and practical examples.
- Redacted all sensitive personal information (computer usernames, specific machine identifiers).

## 3. Commands / tools used
- `uname -srm`: Displayed operating system kernel name, release version, and processor architecture (`Darwin 25.6.0 arm64`).
- `sw_vers`: Displayed macOS product version (`macOS 26.6.2`).
- `whoami`: Checked the active user account identity.
- `df -h /`: Inspected the root disk filesystem, showing total, used, and available storage in gigabytes.
- `ps aux`: Listed active processes, their Process IDs (PID), CPU/memory usage, and executing binaries.
- `ls -l`: Displayed file permission bits, ownership, and size.

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| **Operating system / system details** | The exact OS name, kernel build, and hardware CPU architecture. | `macOS 26.6.2 (Darwin Kernel arm64 - Apple Silicon)` |
| **Current account identity** | The username of the user profile running the current shell session. | `[redacted]` (Standard local user account) |
| **Available and used storage** | Total disk capacity, space currently consumed, and free space left for new files. | Root volume total `926 GiB`, Used `15 GiB`, Available `809 GiB` (approx. 2% utilized) |
| **System activity snapshot** | Active programs, background daemons, process IDs, and CPU/memory consumption. | Multiple processes active including WindowServer (`PID 166`), IDE helpers, and background system services |

---

### Task 3.2 — Understand processes

- **What is a process?**:
  A process is an active instance of a program being executed by the operating system. When a program file stored on disk is opened, the operating system allocates memory, loads the code, and creates a process with its own execution context.
- **What does the PID column represent?**:
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to identify and track each running process independently.
- **Two examples of processes running on my computer**:
  1. `WindowServer` (PID `166`): A core macOS background service responsible for drawing windows, compositing visual elements, and rendering the graphical display.
  2. `airportd` (PID `235`): A macOS system daemon responsible for managing Wi-Fi interfaces and wireless connections.

---

### Task 3.3 — Understand paths and permissions

- **Absolute path vs. Relative path**:
  - **Absolute path**: The complete, unambiguous location of a file or directory starting from the root directory `/`. It works identically regardless of where the current working directory is.
    - Example: `/Users/[redacted]/Desktop/S$AI assignment/digital-detective-8013/terminal-practice/sample.txt`
  - **Relative path**: The path to a file or directory relative to the folder you are currently located in.
    - Example: `terminal-practice/sample.txt` (when inside `digital-detective-8013`), or `../README.md` (when inside `terminal-practice`).

- **File Permissions Analysis**:
  Examining `terminal-practice/sample.txt`:
  ```text
  -rw-r--r--  1 [redacted]  staff  74 Nov 24 14:51 sample.txt
  ```
  - The first character `-` indicates it is a regular file.
  - The next three characters `rw-` represent **owner permissions**: the owner can **read** (`r`) and **write** (`w`), but cannot execute (`-`).
  - The middle three characters `r--` represent **group permissions**: members of the `staff` group can only **read** the file.
  - The final three characters `r--` represent **others permissions**: all other system users can only **read** the file.

| Permission | Meaning | Example |
|---|---|---|
| **r — Read** | Allows the file's contents to be opened and viewed. | Viewing `sample.txt` with `cat`. |
| **w — Write** | Allows the file's contents to be edited, overwritten, or modified. | Appending text with `>>` or editing in a text editor. |
| **x — Execute** | Allows the file to be executed as a program or script; on a folder, allows traversing into it. | Running a shell script `./script.sh` or entering a folder with `cd`. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| **Process management** | Creating, scheduling, pausing, and terminating processes, ensuring the CPU shares execution time efficiently among all tasks. | Allocating CPU time slices between an active web browser and background music playback. |
| **Memory management** | Tracking each byte in RAM, allocating blocks to programs when launched, and freeing memory when programs close. | Loading VS Code into RAM and ensuring it cannot corrupt the memory belonging to another app. |
| **Device management** | Communicating with hardware peripherals using device drivers and buffering input/output requests. | Handling USB flash drives, receiving trackpad taps, and sending print jobs to a printer. |
| **File management** | Organizing files into a structured directory hierarchy on storage drives and tracking file metadata and locations. | Creating folders, renaming documents, and looking up files in the APFS file system. |
| **User interface / shell** | Providing a graphical (GUI) or command-line (CLI) mechanism for humans to interact with the computer. | macOS Finder desktop and the Zsh Terminal shell. |
| **Security and permissions** | Enforcing user access controls, authentication, file read/write permissions, and sandboxing applications. | Requiring password or Touch ID before installing system software, and preventing standard users from modifying system files. |

## 5. Difficulties faced
- Remembering what each triplet in `-rw-r--r--` corresponds to.

## 6. How I resolved them
- Broken down the 9 permission characters into three distinct triplets: owner (first 3), group (middle 3), and others/world (last 3).

## 7. Evidence / files
- Documented in [mission-03-operating-system/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-03-operating-system/README.md).

## 8. Commit details
- **Commit message**: `Document operating system and file management`
- **Branch**: `main`
- **Remote status**: Pushed and verified on GitHub.
