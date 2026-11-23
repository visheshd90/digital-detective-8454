
## Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the specific OS name, kernel version, and build details of the machine. | macOS Darwin kernel version with standard Darwin system architecture (`[redacted]`). |
| **Current account identity** | Displays the username of the active logged-in user currently executing terminal commands. | Displays current user handle (`[redacted]`). |
| **Available and used storage** | Shows total disk capacity, used space, available free space, and mounting percentages (`df -h`). | Displays disk size in gigabytes with adequate free space available on the primary volume. |
| **System activity snapshot** | Provides a point-in-time list of active processes, Process IDs (PIDs), and CPU/memory usage (`ps aux`). | Lists active background processes and system daemons currently managed by the kernel. |

## Task 3.2 — Understand processes

### Questions & Answers:
* **What is a process?**
  A process is an instance of a computer program that is currently being executed and managed by the operating system's kernel, allocated with its own memory space, system resources, and execution state.

* **What does the PID column represent?**
  The PID (Process ID) column represents the unique numerical identification number assigned by the operating system to each active process so it can be tracked, managed, or terminated individually.

* **Give two examples of processes that may be running on your computer:**
  1. **Visual Studio Code / Text Editor:** The application process responsible for managing the user interface, editing files, and running extensions.
  2. **WindowServer / System Daemon:** A core macOS background system process responsible for managing the display window server and rendering graphics on the screen.

## Task 3.3 — Understand paths and permissions

### Paths Explanation & Examples:
- **Absolute Path vs. Relative Path:**
  An **absolute path** defines the complete location of a file or directory starting from the filesystem root `/` (e.g., `/Users/[redacted]/digital-detective-[USN]/mission-03-operating-system`). A **relative path** specifies the location relative to your current working directory (e.g., `mission-03-operating-system/notes.md`).
- **Examples from assignment folder:**
  * **Absolute path example:** `/Users/vedishbansal/documents/digital-detective-8005/mission-03-operating-system`
  * **Relative path example:** `mission-03-operating-system/notes.md`

### File Permissions Analysis:
- **Command used:** `ls -l mission-03-operating-system/notes.md`
- **Owner Permission Letters Observed:** `-rw-r--r--` (where the first three characters `rw-` represent the file owner's permissions).
- **Owner Permissions Breakdown:**
  * **Read (`r`):** Yes, the owner has permission to read the file contents.
  * **Write (`w`):** Yes, the owner has permission to modify and write updates to the file.
  * **Execute (`x`):** No (`-`), the owner cannot execute the file as an application script since it is a markdown text document.

## Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Creating, scheduling, suspending, and terminating active processes, allocating CPU time so multiple applications can run concurrently. | Running a web browser and terminal simultaneously while the OS switches CPU attention between them. |
| **Memory management** | Allocating and deallocating blocks of physical RAM to active programs, ensuring they do not overwrite each other's data space. | Assigning RAM to VS Code when opened and reclaiming that memory when closed. |
| **Device management** | Interfacing with hardware peripherals and external devices using specialized device drivers so applications can use hardware seamlessly. | Sending print jobs from a document editor to a physical printer. |
| **File management** | Organizing, creating, reading, writing, and storing files and folders in a hierarchical directory structure on storage drives. | Saving and organizing markdown notes inside your assignment folder. |
| **User interface / shell** | Providing an accessible bridge (graphical desktop or text-based command shell) for users and programs to interact with the OS kernel. | Typing terminal commands like `ls` or `pwd` in the macOS Terminal app. |
| **Security and permissions** | Enforcing user authentication, access control lists, and file permissions to protect system files and private data from unauthorized access. | Restricting file modification permissions so only the owner can write to sensitive notes files. |
