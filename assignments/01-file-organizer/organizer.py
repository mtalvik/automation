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
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.md'],
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
    # 1. Validate source directory exists
    # 2. Set destination_dir to source_dir if not provided
    # 3. Get all files in source directory
    # 4. For each file:
    #    - Determine its category
    #    - Create category folder if needed
    #    - Move/copy file to category folder
    #    - Handle duplicates
    # 5. Return statistics
    
    stats = {category: 0 for category in FILE_CATEGORIES}
    stats['Other'] = 0
    
    # Your implementation here
    
    return stats

def get_file_category(file_path: Path) -> str:
    """
    Determine the category of a file based on its extension.
    
    Args:
        file_path: Path to the file
    
    Returns:
        Category name or 'Other' if no category matches
    """
    # TODO: Implement category detection
    # 1. Get file extension
    # 2. Check which category it belongs to
    # 3. Return category name or 'Other'
    
    return 'Other'

def handle_duplicate(destination: Path) -> Path:
    """
    Generate a unique filename if the destination already exists.
    
    Args:
        destination: Proposed destination path
    
    Returns:
        Unique destination path
    """
    # TODO: Implement duplicate handling
    # 1. Check if destination exists
    # 2. If yes, add number suffix until unique name found
    # 3. Return unique path
    
    return destination

def main():
    """Main function to run the file organizer."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize files into folders by type')
    parser.add_argument('source', help='Source directory containing files to organize')
    parser.add_argument('--destination', help='Destination directory (default: source directory)')
    parser.add_argument('--dry-run', action='store_true', help='Simulate organization without moving files')
    
    args = parser.parse_args()
    
    # TODO: Implementation
    # 1. Validate arguments
    # 2. Call organize_files with arguments
    # 3. Print statistics
    # 4. Handle errors gracefully
    
    print(f"Organizing files in {args.source}...")
    
    try:
        stats = organize_files(args.source, args.destination, args.dry_run)
        
        # Print results
        print("\n📊 Organization Complete!")
        print("-" * 30)
        for category, count in stats.items():
            if count > 0:
                print(f"{category}: {count} files")
        
        if args.dry_run:
            print("\n⚠️  DRY RUN - No files were actually moved")
    
    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
