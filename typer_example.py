import typer
import os
import time
from pathlib import Path
from typing import Optional

app = typer.Typer()

# Command Group for File Operations
file_app = typer.Typer()
app.add_typer(file_app, name="file")

# Command Group for Report Generation
report_app = typer.Typer()
app.add_typer(report_app, name="report")


# Command: List files in a directory
@file_app.command("list")
def list_files(directory: Path, extension: Optional[str] = None):
    """
    List all files in a directory. Optionally filter by file extension.
    """
    if not directory.is_dir():
        typer.echo(f"Error: {directory} is not a valid directory.", err=True)
        raise typer.Exit(code=1)

    files = [f for f in directory.iterdir() if f.is_file()]
    
    if extension:
        files = [f for f in files if f.suffix == f".{extension}"]
    
    if files:
        typer.echo(f"Files in {directory}:")
        for file in files:
            typer.echo(f" - {file.name}")
    else:
        typer.echo("No files found.")

# Command: Process files (e.g., compress, encrypt)
@file_app.command("process")
def process_files(
    directory: Path,
    operation: str = typer.Argument(..., help="Operation: compress or encrypt"),
    extension: Optional[str] = None
):
    """
    Process files in a directory (e.g., compress, encrypt). Optionally filter by extension.
    """
    valid_operations = ["compress", "encrypt"]
    
    if operation not in valid_operations:
        typer.echo(f"Error: Invalid operation '{operation}'. Choose from {valid_operations}.", err=True)
        raise typer.Exit(code=1)
    
    files = [f for f in directory.iterdir() if f.is_file()]
    
    if extension:
        files = [f for f in files if f.suffix == f".{extension}"]

    if not files:
        typer.echo("No files to process.")
        raise typer.Exit(code=0)
    
    typer.echo(f"Performing '{operation}' on {len(files)} file(s)...")

    # Using a progress bar
    with typer.progressbar(files, label=f"Processing {operation} operation") as progress:
        for file in progress:
            time.sleep(1)  # Simulating processing time
            if operation == "compress":
                typer.echo(f"Compressed {file.name}")
            elif operation == "encrypt":
                typer.echo(f"Encrypted {file.name}")


# Command: Generate a file report (size, count, etc.)
@report_app.command("generate")
def generate_report(directory: Path):
    """
    Generate a report on the files in the directory (e.g., total size, file count).
    """
    if not directory.is_dir():
        typer.echo(f"Error: {directory} is not a valid directory.", err=True)
        raise typer.Exit(code=1)

    files = [f for f in directory.iterdir() if f.is_file()]
    total_size = sum(f.stat().st_size for f in files)
    file_count = len(files)

    typer.echo(f"Report for {directory}:")
    typer.echo(f"Total files: {file_count}")
    typer.echo(f"Total size: {total_size / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    app()
