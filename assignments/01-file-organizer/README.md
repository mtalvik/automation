# 📁 File Organizer Assignment

## 📋 Ülesande kirjeldus

Sinu ülesanne on luua Python skript, mis automatiseerib failide organiseerimist. Skript peab sorteerima failid kaustadesse nende tüübi järgi.

## 🎯 Nõuded

### Põhifunktsioonid (70 punkti)
- [ ] Sorteeri failid laiendi järgi eraldi kaustadesse
- [ ] Käsitle duplikaate (lisa number faili nimele)
- [ ] Loo automaatselt puuduvad kaustad
- [ ] Logi kõik tegevused faili

### Failitüübid
```python
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
}
```

### Lisa funktsioonid (30 punkti)
- [ ] Käsurea argumendid (source ja destination kaustad)
- [ ] Dry-run režiim (näita mis juhtuks, aga ära tee midagi)
- [ ] Rekursiivne kaustas otsimine
- [ ] Konfiguratsioonifail kategooriate jaoks

## 📝 Starter Code

```python
#!/usr/bin/env python3
"""
File Organizer Script
Organizes files into folders based on their type.
"""

import os
import shutil
import logging
from pathlib import Path
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_organizer.log'),
        logging.StreamHandler()
    ]
)

FILE_CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
}

def organize_files(source_dir: str, destination_dir: str = None, dry_run: bool = False) -> Dict[str, int]:
    """
    Organize files from source directory into categorized folders.
    
    Args:
        source_dir: Path to directory containing files to organize
        destination_dir: Path where organized folders will be created (default: source_dir)
        dry_run: If True, only simulate the organization without moving files
    
    Returns:
        Dictionary with statistics of organized files by category
    """
    # TODO: Implement file organization logic
    pass

def get_file_category(file_path: Path) -> str:
    """
    Determine the category of a file based on its extension.
    
    Args:
        file_path: Path to the file
    
    Returns:
        Category name or 'Other' if no category matches
    """
    # TODO: Implement category detection
    pass

def handle_duplicate(destination: Path) -> Path:
    """
    Generate a unique filename if the destination already exists.
    
    Args:
        destination: Proposed destination path
    
    Returns:
        Unique destination path
    """
    # TODO: Implement duplicate handling
    pass

def main():
    """Main function to run the file organizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize files into folders by type')
    parser.add_argument('source', help='Source directory containing files to organize')
    parser.add_argument('--destination', help='Destination directory (default: source directory)')
    parser.add_argument('--dry-run', action='store_true', help='Simulate organization without moving files')
    
    args = parser.parse_args()
    
    # TODO: Call organize_files with arguments
    # TODO: Print statistics

if __name__ == '__main__':
    main()
```

## 🧪 Testimine

Testid käivituvad automaatselt, kui pushid koodi. Lokaalselt testimiseks:

```bash
pytest test_organizer.py -v
```

## 📊 Hindamine

| Kriteerium | Punkte | Kirjeldus |
|------------|--------|-----------|
| Põhifunktsioonid | 50 | Failide sorteerimine töötab |
| Error handling | 10 | Käsitleb vigu graatsiliselt |
| Logging | 10 | Logib kõik tegevused |
| Duplikaadid | 10 | Käsitleb duplikaate õigesti |
| CLI | 10 | Käsurea parameetrid töötavad |
| Koodi kvaliteet | 10 | PEP8, type hints, docstrings |

## 💡 Vihjed

1. Kasuta `pathlib` mooduli `Path` objekti failide käsitlemiseks
2. `shutil.move()` on parem kui `os.rename()` cross-platform toe jaoks
3. Testi oma koodi erinevate failitüüpidega
4. Ära unusta käsitleda edge case'e (tühjad failid, erikaraktered nimedes)

## 📚 Ressursid

- [Python pathlib dokumentatsioon](https://docs.python.org/3/library/pathlib.html)
- [Python shutil dokumentatsioon](https://docs.python.org/3/library/shutil.html)
- [Python logging dokumentatsioon](https://docs.python.org/3/library/logging.html)

## ✅ Submission

Push oma lahendus `main` branchi. GitHub Actions käivitab testid automaatselt.

Edu! 🚀
