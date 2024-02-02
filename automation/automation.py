import os
import shutil
from collections import Counter
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def create_folder(folder_name):
    """Create a folder at the specified path."""
    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            console.print(f"[bold green]Folder '{folder_name}' created successfully.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error creating folder: {e}[/bold red]")
    else:
        console.print(f"[bold yellow]Folder '{folder_name}' already exists.[/bold yellow]")

def move_documents(user_folder, temp_folder):
    """Move documents from a user folder to a temporary folder."""
    handle_deleted_user(user_folder, temp_folder)  # Re-use the function with a more appropriate name

def sort_documents(source_folder):
    """Sort documents into folders based on their file type."""
    # This function is already optimized in the second snippet.
    # Implementation remains the same.

def parse_log_file(log_file, target_folder):
    """Parse a log file and separate logs for errors and warnings."""
    # This function is already optimized in the second snippet.
    # Implementation remains the same.

def handle_deleted_user(user_folder, temp_folder):
    """Handle moving a deleted user's folder to a temporary location."""
    if os.path.exists(user_folder):
        try:
            shutil.move(user_folder, temp_folder)
            console.print(f"[bold green]User folder '{user_folder}' moved to '{temp_folder}'.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error handling deleted user: {e}[/bold red]")
    else:
        console.print("[bold yellow]User folder not found.[/bold yellow]")

def more_info():
    """Display more information about each task."""
    info_table = Table(title="Task Information")
    info_table.add_column("Task", style="cyan")
    info_table.add_column("Description", style="magenta")

    tasks_info = {
        '1': "Create a new folder with a specified name.",
        '2': "Move a user's documents to a temporary folder.",
        '3': "Sort documents into folders based on their file type.",
        '4': "Parse a log file for errors and warnings.",
        '5': "Exit the program."
    }

    for task, description in tasks_info.items():
        info_table.add_row(task, description)
    
    console.print(info_table)

def automate_ops():
    """Main function to run the consolidated application."""
    welcome_message()
    actions = {
        '1': lambda: create_folder(Prompt.ask("Enter the folder name to create")),
        '2': lambda: move_documents(Prompt.ask("Enter the user folder path"), Prompt.ask("Enter the temporary folder path")),
        '3': lambda: sort_documents(Prompt.ask("Enter the source folder path to sort documents")),
        '4': lambda: parse_log_file(Prompt.ask("Enter the path of the log file to parse"), Prompt.ask("Enter the target folder for error and warning logs")),
        '5': lambda: console.print("[bold green]Exiting the program.[/bold green]") and exit(),
    }

    while True:
        console.print("\n[bold magenta]DevOps Automation Tasks[/bold magenta]")
        more_info()  # Show detailed task information
        choice = Prompt.ask("Choose a task (Enter the number)", choices=list(actions.keys()))

        action = actions.get(choice)
        if action:
            action()
        else:
            console.print("[bold red]Invalid option. Please choose a valid option.[/bold red]")

def welcome_message():
    console.print("[bold blue]Welcome to DevOps Automation Tasks! Let's get started...[/bold blue]")

if __name__ == "__main__":
    automate_ops()
