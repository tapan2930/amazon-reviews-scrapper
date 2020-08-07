import typer
import getReviews as gr

app = typer.Typer()

@app.command()
def start(url: str):
    typer.echo("")	
    message = typer.style("Welcome, You are one hell of a LUCKY GOOSE, 😏😏😏😏", fg=typer.colors.MAGENTA, bold=True)

    typer.echo(message)
    typer.echo("")
    typer.echo("Initializing....")

    url = gr.process_url(url)

    total = 0
    with typer.progressbar(gr.scrape(url), length=gr.total_page, label="Scraping ") as progress:
        for value in progress:
            total = total+1
    typer.echo(f"Scraping Done...")
    typer.echo("Saving Data ito cvs....")
    saved_path = gr.save_data()
    csv_path = typer.style(saved_path, fg=typer.colors.GREEN)
    typer.echo(csv_path)
    typer.echo("Completed...")


if __name__ == "__main__":
    app()

    
