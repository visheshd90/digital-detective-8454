# Mission 5 - Number Systems Notes

## Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary.** | • Divide by 2 successively:<br>13 ÷ 2 = 6 remainder **1**<br>6 ÷ 2 = 3 remainder **0**<br>3 ÷ 2 = 1 remainder **1**<br>1 ÷ 2 = 0 remainder **1**<br>• Reading remainders bottom-up:<br>**Answer: `1101₂`** |
| **Convert decimal 25 to binary.** | • Divide by 2 successively:<br>25 ÷ 2 = 12 remainder **1**<br>12 ÷ 2 = 6 remainder **0**<br>6 ÷ 2 = 3 remainder **0**<br>3 ÷ 2 = 1 remainder **1**<br>1 ÷ 2 = 0 remainder **1**<br>• Reading remainders bottom-up:<br>**Answer: `11001₂`** |
| **Convert binary 1010 to decimal.** | • Multiply each bit by powers of 2 from right to left:<br>(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>= (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)<br>= 8 + 0 + 2 + 0<br>**Answer: `10₁₀`** |
| **Convert binary 1101 to decimal.** | • Multiply each bit by powers of 2 from right to left:<br>(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)<br>= (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)<br>= 8 + 4 + 0 + 1<br>**Answer: `13₁₀`** |
| **Convert hexadecimal A to decimal.** | • Since hexadecimal A represents decimal 10:<br>A₁₆ = 10 × 16⁰<br>= 10 × 1<br>**Answer: `10₁₀`** |
| **Convert hexadecimal 1F to decimal.** | • Multiply each digit by powers of 16 (where F = 15):<br>(1 × 16¹) + (F × 16⁰)<br>= (1 × 16) + (15 × 1)<br>= 16 + 15<br>**Answer: `31₁₀`** |
| **Convert binary 1111 to hexadecimal.** | • Group 4 binary bits into hexadecimal:<br>1111₂ = 8 + 4 + 2 + 1 = 15<br>• Decimal 15 corresponds to hexadecimal **F**<br>**Answer: `F₁₆`** |

## Task 5.2 — Verify using Python

| Conversion Type | Python Expression Tested | Python Output / Result | Matches Manual Calculation? |
| :--- | :--- | :--- | :--- |
| **Decimal 13 to Binary** | `bin(13)` | `'0b1101'` | Yes |
| **Decimal 25 to Binary** | `bin(25)` | `'0b11001'` | Yes |
| **Binary 1010 to Decimal** | `int('1010', 2)` | `10` | Yes |
| **Binary 1101 to Decimal** | `int('1101', 2)` | `13` | Yes |
| **Hexadecimal A to Decimal** | `int('A', 16)` | `10` | Yes |
| **Hexadecimal 1F to Decimal** | `int('1F', 16)` | `31` | Yes |
| **Binary 1111 to Hexadecimal** | `hex(0b1111)` | `'0xf'` | Yes |

## Task 5.3 — Build a small number converter

* **File created:** `number_converter.py`
* **Program code implemented:** Uses `input()`, `int()`, `bin()`, and `hex()` to capture user input, convert types, and display base-2 and base-16 representations.

### Test Results Table:
| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| **10** | `0b1010` | `0xa` |
| **42** | `0b101010` | `0x2a` |
| **255** | `0b11111111` | `0xff` |

### Function Explanations:
* **`bin()` function:** Takes an integer as input and returns its binary representation as a string prefixed with `0b` (base 2).
* **`hex()` function:** Takes an integer as input and returns its hexadecimal representation as a string prefixed with `0x` (base 16).

## Task 5.4 — How is text stored?

### Questions & Answers:
* **ASCII decimal codes for uppercase 'A' and lowercase 'a':**
  * Uppercase **`A`** decimal code: `65` (Hex: `41`)
  * Lowercase **`a`** decimal code: `97` (Hex: `61`)

* **Why a computer needs an encoding standard to store text:**
  Computers operate entirely using binary digits (zeros and ones) and cannot directly understand human letters or symbols. An encoding standard provides a universal mapping system that assigns a unique numeric code to every character so the computer can reliably store, process, and display text.

* **One example of a character that is not part of basic ASCII:**
  * **Example:** The euro sign (`€`), a Chinese character (e.g., `中`), or an emoji (e.g., `😊`), which require extended encodings like UTF-8 because basic ASCII only supports 128 standard English-centric characters.
