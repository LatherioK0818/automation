import pytest
from automation.automation import create_folder, move_documents, sort_documents, parse_log_file, handle_deleted_user
from pathlib import Path
import shutil
import os

# Assuming your automation.py script's functions are correctly defined as per your description.

def setup_file_structure(tmp_path):
    """
    Creates a temporary file structure for testing document sorting and handling deleted users.
    """
    # Create source, user, and temp folders
    source_folder = tmp_path / "source"
    user_folder = tmp_path / "user_folder"
    temp_folder = tmp_path / "temp_folder"
    log_file = source_folder / "example.log"
    email_file = source_folder / "email.txt"

    source_folder.mkdir()
    user_folder.mkdir()
    temp_folder.mkdir()
    log_file.write_text("This is a log entry.")
    email_file.write_text("This is an email content.")

    return {
        "source_folder": source_folder,
        "user_folder": user_folder,
        "temp_folder": temp_folder,
        "log_file": log_file,
        "email_file": email_file
    }

def test_create_folder(tmp_path):
    """
    Test the create_folder function to ensure it creates a folder.
    """
    folder_name = tmp_path / "new_folder"
    create_folder(str(folder_name))
    assert folder_name.exists(), "Folder was not created by create_folder function."

def test_handle_deleted_user(setup_file_structure, mocker):
    """
    Test the handle_deleted_user function to ensure it moves the user folder to a temporary folder.
    """
    user_folder = setup_file_structure["user_folder"]
    temp_folder = setup_file_structure["temp_folder"]
    mocker.patch('shutil.move')
    handle_deleted_user(str(user_folder), str(temp_folder))
    shutil.move.assert_called_once_with(str(user_folder), str(temp_folder))

def test_sort_documents(setup_file_structure):
    """
    Test the sort_documents function to ensure it sorts documents into appropriate folders.
    """
    source_folder = setup_file_structure["source_folder"]
    sort_documents(str(source_folder))
    logs_folder = source_folder / "logs"
    mail_folder = source_folder / "mail"
    
    assert logs_folder.exists() and mail_folder.exists(), "Document folders were not created."
    assert (logs_folder / "example.log").exists(), "Log file was not moved to logs folder."
    assert (mail_folder / "email.txt").exists(), "Email file was not moved to mail folder."

def test_parse_log_file(tmp_path):
    """
    Test the parse_log_file function to ensure it creates separate logs for errors and warnings.
    """
    log_file = tmp_path / "example.log"
    log_file.write_text("ERROR: This is an error\nWARNING: This is a warning")
    target_folder = tmp_path / "target"
    target_folder.mkdir()

    parse_log_file(str(log_file), str(target_folder))
    
    error_log = target_folder / "errors.log"
    warning_log = target_folder / "warnings.log"
    assert error_log.exists() and warning_log.exists(), "Log files were not created."
    with error_log.open() as f:
        assert "ERROR: This is an error" in f.read(), "Error log does not contain expected content."
    with warning_log.open() as f:
        assert "WARNING: This is a warning" in f.read(), "Warning log does not contain expected content."
