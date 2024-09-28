import click

# This could be replaced with a database or any other method of persistence
tasks = []

@click.group()
def cli():
    """A simple CLI todo list manager."""
    pass

@cli.command()
@click.option(
    "--debug/--no-debug",
    "-d/ ",
    envvar="DBT_DEBUG",
    help="Display debug logging during dbt execution. Useful for debugging and making bug reports.",
)
@click.argument('task', type=str)
def add(task):
    """Add a new task to the list."""
    tasks.append(task)
    click.echo(f"Added task: {task}")

@cli.command()
@click.argument('task', type=str)
def remove(task):
    """Remove a task from the list."""
    try:
        tasks.remove(task)
        click.echo(f"Removed task: {task}")
    except ValueError:
        click.echo("Task not found.")

@cli.command()
def list():
    """List all the tasks."""
    click.echo("Tasks:")
    for task in tasks:
        click.echo(task)

if __name__ == '__main__':
    cli()
