# Backup Script

This project provides a Python script to perform backups from the network directory `ORIGIN PATH (REPLACE THIS)` to `DESTINY PATH (REPLACE THIS)`. The script lists all the folders in the source directory, prompts the user to select one by entering its corresponding number, and then copies the selected folder to the backup directory. The backup folder is named using the original folder name followed by a timestamp in the format `[yyyyMMdd_HHmm]`.

---

## English Version

### Overview

The script is designed to facilitate backups by allowing the user to choose a folder from a specified source directory. Once a folder is selected, the script copies the folder to a backup directory, appending a timestamp to its name to ensure uniqueness.

### Features

- Lists folders from the source directory.
- Prompts the user to select a folder by its number.
- Copies the selected folder to the backup directory.
- Appends a timestamp (formatted as `yyyyMMdd_HHmm`) to the folder name in the backup directory.

### Prerequisites

- Python 3.x must be installed.
- The machine must have access to the network paths: `ORIGIN PATH (REPLACE THIS)` and `DESTINY PATH (REPLACE THIS)`.
- Appropriate permissions to read from the source directory and write to the backup directory.

### Usage

1. Clone or download the script.
2. Ensure that the network paths are accessible from your machine.
3. Change origin and destiny path
4. Run the script using the command:

   ```bash
   python backup_script.py
