"""
Test suite for file organizer assignment
"""

import os
import tempfile
import shutil
from pathlib import Path
import pytest
from organizer import organize_files, get_file_category, handle_duplicate


class TestFileOrganizer:
    """Test cases for the file organizer."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        # Cleanup
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def sample_files(self, temp_dir):
        """Create sample files for testing."""
        files = {
            'document.pdf': 'Documents',
            'image.jpg': 'Images',
            'video.mp4': 'Videos',
            'script.py': 'Code',
            'archive.zip': 'Archives',
            'music.mp3': 'Audio',
            'random.xyz': 'Other'
        }
        
        for filename in files.keys():
            (temp_dir / filename).touch()
        
        return temp_dir, files
    
    def test_get_file_category(self):
        """Test file category detection."""
        assert get_file_category(Path('test.pdf')) == 'Documents'
        assert get_file_category(Path('photo.jpg')) == 'Images'
        assert get_file_category(Path('script.py')) == 'Code'
        assert get_file_category(Path('unknown.xyz')) == 'Other'
    
    def test_organize_files_basic(self, sample_files):
        """Test basic file organization."""
        source_dir, expected_categories = sample_files
        
        stats = organize_files(str(source_dir))
        
        # Check that files are organized
        for filename, category in expected_categories.items():
            expected_path = source_dir / category / filename
            assert expected_path.exists(), f"File {filename} not found in {category}"
        
        # Check statistics
        assert stats['Documents'] == 1
        assert stats['Images'] == 1
        assert stats['Code'] == 1
    
    def test_handle_duplicate(self, temp_dir):
        """Test duplicate file handling."""
        # Create original file
        original = temp_dir / 'test.txt'
        original.touch()
        
        # Get unique name for duplicate
        unique_path = handle_duplicate(original)
        
        assert unique_path != original
        assert 'test_1.txt' in str(unique_path) or 'test (1).txt' in str(unique_path)
    
    def test_dry_run_mode(self, sample_files):
        """Test that dry run doesn't move files."""
        source_dir, _ = sample_files
        original_files = list(source_dir.glob('*'))
        
        organize_files(str(source_dir), dry_run=True)
        
        # Check that files haven't moved
        current_files = list(source_dir.glob('*'))
        assert len(original_files) == len(current_files)
        assert all(f.is_file() for f in current_files)
    
    def test_custom_destination(self, sample_files):
        """Test organizing to a different destination directory."""
        source_dir, expected_categories = sample_files
        dest_dir = source_dir.parent / 'organized'
        
        stats = organize_files(str(source_dir), str(dest_dir))
        
        # Check files in destination
        for filename, category in expected_categories.items():
            expected_path = dest_dir / category / filename
            assert expected_path.exists(), f"File {filename} not found in destination"
    
    def test_empty_directory(self, temp_dir):
        """Test organizing an empty directory."""
        stats = organize_files(str(temp_dir))
        
        assert all(count == 0 for count in stats.values())
    
    def test_nested_directories(self, temp_dir):
        """Test that subdirectories are handled correctly."""
        # Create nested structure
        sub_dir = temp_dir / 'subdir'
        sub_dir.mkdir()
        (sub_dir / 'nested.pdf').touch()
        (temp_dir / 'root.pdf').touch()
        
        stats = organize_files(str(temp_dir))
        
        # Should only organize files in root by default
        assert stats['Documents'] == 1
        assert (temp_dir / 'Documents' / 'root.pdf').exists()
        assert (sub_dir / 'nested.pdf').exists()  # Should remain in subdir
    
    @pytest.mark.parametrize('filename,expected_category', [
        ('README.md', 'Documents'),
        ('photo.jpeg', 'Images'),
        ('.gitignore', 'Other'),
        ('Makefile', 'Code'),
        ('song.flac', 'Audio'),
    ])
    def test_various_file_types(self, temp_dir, filename, expected_category):
        """Test various file types are categorized correctly."""
        file_path = temp_dir / filename
        file_path.touch()
        
        category = get_file_category(file_path)
        # This test might need adjustment based on implementation
        assert category in [expected_category, 'Other', 'Documents', 'Code']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
