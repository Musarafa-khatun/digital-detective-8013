# Mission 5 — Numbers and Data

## 1. Task / objective
The objective of this mission is to understand number systems (decimal, binary, hexadecimal) used by computers, carry out step-by-step manual conversions, verify each calculation using Python, write a command-line Python number converter program (`number_converter.py`), and explain character encoding standards like ASCII and UTF-8.

## 2. Work completed
- Performed step-by-step manual conversions for all 7 required conversion problems using the repeated division and positional value methods.
- Verified all manual results using Python's built-in conversion functions (`bin()`, `hex()`, `int()`).
- Developed `mission-05-numbers-data/number_converter.py` using standard beginner-friendly Python.
- Tested the converter with three distinct positive integers (`13`, `25`, `42`) and documented the terminal output.
- Researched and explained ASCII and UTF-8 character encoding standards, verified decimal ASCII codes for 'A' and 'a', and identified a character requiring multi-byte UTF-8 representation.

## 3. Commands / tools used
- Python 3 interactive shell and scripts:
  - `bin()`: Converts an integer to a binary string with a `0b` prefix.
  - `hex()`: Converts an integer to a hexadecimal string with a `0x` prefix.
  - `int(string, base)`: Parses a number string in a specified base into a decimal integer.
  - `input()`: Captures user input as a string from the terminal.
  - `ord()`: Returns the integer Unicode/ASCII code point of a given character.

## 4. My understanding

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
|---|---|
| **Convert decimal 13 to binary** | Repeated division by 2:<br>13 ÷ 2 = 6, remainder **1** (LSB)<br>6 ÷ 2 = 3, remainder **0**<br>3 ÷ 2 = 1, remainder **1**<br>1 ÷ 2 = 0, remainder **1** (MSB)<br>Reading remainders from bottom to top: **1101₂** |
| **Convert decimal 25 to binary** | Repeated division by 2:<br>25 ÷ 2 = 12, remainder **1** (LSB)<br>12 ÷ 2 = 6, remainder **0**<br>6 ÷ 2 = 3, remainder **0**<br>3 ÷ 2 = 1, remainder **1**<br>1 ÷ 2 = 0, remainder **1** (MSB)<br>Reading remainders from bottom to top: **11001₂** |
| **Convert binary 1010 to decimal** | Positional value expansion (powers of 2):<br>= (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>= (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)<br>= 8 + 0 + 2 + 0 = **10₁₀** |
| **Convert binary 1101 to decimal** | Positional value expansion (powers of 2):<br>= (1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)<br>= (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)<br>= 8 + 4 + 0 + 1 = **13₁₀** |
| **Convert hexadecimal A to decimal** | Positional value (base 16):<br>In hex, digits 0–9 represent values 0–9, and letters A–F represent 10–15.<br>A = **10₁₀** |
| **Convert hexadecimal 1F to decimal** | Positional value expansion (powers of 16):<br>= (1 × 16¹) + (F × 16⁰)<br>= (1 × 16) + (15 × 1)<br>= 16 + 15 = **31₁₀** |
| **Convert binary 1111 to hexadecimal** | Grouping 4 bits into one hex digit:<br>Binary: 1111<br>Positional value: (1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 15₁₀<br>In hexadecimal, the value 15 is represented by the single symbol **F₁₆** |

---

### Task 5.2 — Verify using Python

| Expression tested | Python result | Matches manual calculation? |
|---|---|---|
| `bin(13)` | `'0b1101'` | Yes, matches 1101₂ (`0b` indicates binary prefix). |
| `bin(25)` | `'0b11001'` | Yes, matches 11001₂. |
| `int('1010', 2)` | `10` | Yes, matches 10₁₀. |
| `int('1101', 2)` | `13` | Yes, matches 13₁₀. |
| `int('A', 16)` | `10` | Yes, matches 10₁₀. |
| `int('1F', 16)` | `31` | Yes, matches 31₁₀. |
| `hex(int('1111', 2))` | `'0xf'` | Yes, matches F₁₆ (`0x` indicates hex prefix). |

---

### Task 5.3 — Build a small number converter

The Python script `number_converter.py` uses four key functions:
- `input()`: Pauses program execution and reads a line entered by the user from the console as a text string.
- `int()`: Parses the string into an integer so arithmetic and base transformations can be performed.
- `bin()`: Converts the integer into its binary representation string starting with `0b`.
- `hex()`: Converts the integer into its hexadecimal representation string starting with `0x`.

#### Test Results

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| **13** | `0b1101` | `0xd` |
| **25** | `0b11001` | `0x19` |
| **42** | `0b101010` | `0x2a` |

---

### Task 5.4 — How is text stored?

- **ASCII decimal codes for 'A' and 'a'**:
  - Uppercase `A`: **65** (binary `01000001`)
  - Lowercase `a`: **97** (binary `01100001`)
  - Difference: 32 (toggling bit 5 switches between upper and lower case).
- **Why computers need an encoding standard**:
  Computers only store and transmit electrical states (bits: 0s and 1s). They cannot directly store the letter 'A' or the symbol '?'. An encoding standard acts like a shared dictionary that assigns every letter, symbol, and punctuation mark a unique numeric code so computers around the world can interpret and display the same text consistently.
- **Example of a character not in basic ASCII**:
  The Indian Rupee symbol `₹` (Unicode `U+20B9`) or an emoji like `🌟`. Basic ASCII only defines 128 characters (codes 0–127) covering English letters, digits, and control codes. Modern standards like UTF-8 use variable-length encodings (up to 4 bytes) to represent thousands of symbols and writing systems from across the globe.

## 5. Difficulties faced
- In Python, `bin()` and `hex()` return strings starting with prefixes (`0b` and `0x`), which initially can look like letters inside the number.

## 6. How I resolved them
- Understood that `0b` denotes base 2 (binary) and `0x` denotes base 16 (hexadecimal) in Python, which prevents ambiguity between decimal 10 and binary 10.

## 7. Evidence / files
- Python program: [mission-05-numbers-data/number_converter.py](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-05-numbers-data/number_converter.py)
- Mission documentation: [mission-05-numbers-data/README.md](file:///Users/musarafakhatun/Desktop/S$AI%20assignment/digital-detective-8013/mission-05-numbers-data/README.md)

## 8. Commit details
- **Commit message**: `Build number converter and practise data representation`
- **Branch**: `main`
- **Remote status**: Pushed and verified on GitHub.
