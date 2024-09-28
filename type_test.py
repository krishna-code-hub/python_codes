
import typer

app = typer.Typer(help="This is an advanced calculator that supports arithmetic operations and unit conversions.")

@app.command(help="Performs addition between two numbers.")
def add(a: float = typer.Option(5, help="The first number"),
         b: float = typer.Option(10, help="The second number"),
         verbose: bool = typer.Option(False, "--verbose", "-v", help="Output verbose result")):
    result = a + b
    if verbose:
        typer.echo(f"Adding {a} and {b} gives {result}")
    else:
        typer.echo(result)

@app.command(help="Converts temperature between Celsius and Fahrenheit.")
def convert_temp(value: float = typer.Option(..., help="Temperature value to convert"),
                 scale: str = typer.Option("celsius", "--scale", "-s", help="Target scale: 'celsius' or 'fahrenheit'")):
    if scale.lower() == 'celsius':
        converted = (value - 32) * 5.0/9.0
        typer.echo(f"{value}°F is {converted:.2f}°C")
    elif scale.lower() == 'fahrenheit':
        converted = (value * 9.0/5.0) + 32
        typer.echo(f"{value}°C is {converted:.2f}°F")
    else:
        typer.echo("Invalid scale. Please choose 'celsius' or 'fahrenheit'.")

if __name__ == "__main__":
    app()
