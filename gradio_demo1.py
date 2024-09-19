import gradio as gr

def greet(name):
    return "hello " + name + "!"

demo = gr.Interface(
    fn = greet,
    inputs = "textbox",
    outputs = "textbox"
)

demo.launch()