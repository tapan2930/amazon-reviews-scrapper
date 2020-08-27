import typer
import getReviews as gr

app = typer.Typer()

@app.command()
def start():
    echo_color("⭐⭐⭐⭐⭐ Amazon Reviews Scrapper ⭐⭐⭐⭐⭐",color=typer.colors.MAGENTA, bold=True)
    typer.echo("")
    typer.echo("Initializing....")
    running = True

    while(running):

        process()
        echo_color("Continue....(Y(yes) - N(No)):", color=typer.colors.BRIGHT_GREEN, bold=True)
        retry = input()
        if(retry.lower() != "y" and retry.lower() != "yes"):
            save_to_cvs()
            running = False
        
    


def process():
    print()
    print("URL:", end=" ")
    url = input()
    url = gr.process_url(url)

    total = 0
    with typer.progressbar(gr.scrape(url), length=gr.total_page, label="Scraping ") as progress:
        for value in progress:
            total = total+1
    echo_color("Scraping Done...", color=typer.colors.BLUE)


def save_to_cvs():    
    echo_color("Saving Data to cvs....", color=typer.colors.BLUE)
    saved_path = gr.save_data()
    echo_color(saved_path, color=typer.colors.GREEN)
    echo_color("Completed...👍", color=typer.colors.BLUE)

def echo_color(text:str, bold:bool = False, color=typer.colors.WHITE):
    echo = typer.style(text, fg=color, bold=bold, blink=True)
    typer.echo(echo)

if __name__ == "__main__":
    app()

    