# SPDX-License-Identifier: MIT
from textual.app import App
from textual.widgets import *
from textual.containers import Grid
class CalculatorApp(App):
    CSS = """
    Grid {
        layout: grid;
        grid-size: 4;
        grid-gutter: 1 2;
        width: 30;
        height: auto;
        margin: 1 2; 
    }
    Button {
        width: 100%;
        height: 3;
    }
    """

    def compose(self):
        yield Label("Calculator")
        yield Input("", id="formula")
        with Grid():
            yield Button("9", id="_9")
            yield Button("8", id="_8")
            yield Button("7", id="_7")
            yield Button("+", id="plus")
            yield Button("6", id="_6")
            yield Button("5", id="_5")
            yield Button("4", id="_4")
            yield Button("-", id="minus")
            yield Button("3", id="_3")
            yield Button("2", id="_2")
            yield Button("1", id="_1")
            yield Button("*", id="times")
            yield Button("0", id="_0")
            yield Button(".", id="dot")
            yield Button("/", id="divide")
            yield Button("=", id="equals")
            yield Button("C", id="clear")
            yield Button("<-", id="backspace")
        yield Footer()
    def on_button_pressed(self, event):
        if event.button.id == "clear":
            self.query_one("#formula").value = ""
        elif event.button.id == "equals":
            formula = self.query_one("#formula").value
            try:
                result = eval(formula)
                self.query_one("#formula").value = f"{result}"
            except Exception as e:
                self.notify(f"Error: {e}", severity="error")
                self.query_one("#formula").value = ""
        elif event.button.id == "backspace":
            self.query_one("#formula").value = self.query_one("#formula").value[:-1]
        elif event.button.id == "dot":
            self.query_one("#formula").value += "."
        elif event.button.id == "plus":
            self.query_one("#formula").value += "+"
        elif event.button.id == "minus":
            self.query_one("#formula").value += "-"
        elif event.button.id == "times":
            self.query_one("#formula").value += "*"
        elif event.button.id == "divide":
            self.query_one("#formula").value += "/"
        else:
            self.query_one("#formula").value += event.button.id.replace("_", "")
if __name__ == "__main__":
    CalculatorApp().run()
