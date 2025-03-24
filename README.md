# 🧠 Virtual Memory Emulator

This project emulates a **Virtual Memory System**, focusing on the mapping between **Virtual Addresses (VA)** and **Physical Addresses (PA)**. It simulates how a CPU processes a series of instructions using paging and page tables, with inputs representing virtual addresses in binary and a uniprocessing (single-program) model.

---

## 📌 Features

- **Virtual-to-Physical Address Translation**
- **Page Table Management per Program**
- **Page Fault Tracking**
- **Main Memory Frame Simulation**
- **Support for Multiple Programs (one at a time) via `NEW` command**

---

## 📁 Input Format

The emulator reads from a structured input file:

```plaintext
<page size in words>         # Decimal
<number of page frames>      # Decimal
NEW
<virtual memory size>        # Decimal
<virtual address>            # Binary
<virtual address>            # Binary
...
NEW
<virtual memory size>
<virtual address>
...
```

### Example:

```plaintext
8
4
NEW
8
101101
101110
...
NEW
16
0001100
0001101
0001110
...
```

### Notes:
- **Page size**, **number of frames**, and **virtual memory size** are in **decimal**.
- **Virtual addresses** are in **binary**.
- `NEW` marks the beginning of a new program. A new page table is initialized.
- Each NEW block is executed independently, simulating uniprocessing.

---

## 📄 Output Format

After executing each `NEW` block (program), the program prints:
1. **Page fault rate** (formatted as `XXX.XXX%`)
2. **Contents of all page tables so far**, in the order of execution.

### Sample Output:

```plaintext
050.000%
01 10 02 03
033.333%
00 01 02 03 04 05
```

---

## 🏗️ Program Structure

### 🔹 MainMemory
- Holds all active and past **PageTables**
- Keeps track of loaded pages and frames

### 🔹 CPU
- Handles:
  - Instruction execution
  - Address translation (VA → PA)
  - Page table creation on `NEW`
  - Page loading and memory management

### 🔹 PageTable
- Stores mapping from virtual pages to physical frames
- Supports operations to:
  - Add new page entries
  - Handle page faults
  - Track memory usage for its program

---

## 🚀 How to Run

1. Ensure Python 3 is installed.
2. Place your input file (e.g., `input.txt`) in the project folder.
3. Run the emulator:

```bash
python vm_emulator.py input.txt
```

4. Output will be displayed on the console or saved to an output file depending on implementation.

---

## 🧠 Concepts Practiced

- Virtual Memory & Paging
- Page Tables & Address Translation
- Page Fault Handling
- Memory Management Simulation
- Data Structures & OOP in Python

---

## ✍️ Author

Endi Troqe
