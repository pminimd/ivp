import gradio as gr

# Dummy initial boxes (x, y, width, height) and label
initial_boxes = [
    {"x": 20, "y": 20, "width": 100, "height": 100, "label": "Object1"},
    {"x": 150, "y": 150, "width": 80, "height": 80, "label": "Object2"}
]

# Image path
image_path = "example_image.png"

# Function to dynamically update the boxes
def update_boxes(new_boxes, boxes):
    # Here you can modify the boxes based on user input or other logic
    updated_boxes = boxes
    # Add new box or modify an existing one
    updated_boxes.append(new_boxes)  # Simulate adding a new box

    return updated_boxes  # Return updated boxes

# Gradio interface
with gr.Blocks() as demo:
    # Image annotator with initial boxes
    image_annotator = gr.ImageAnnotator(value=image_path, boxes=initial_boxes, label="Annotate Image")
    
    # Textbox to simulate new box input
    new_box_input = gr.Textbox(label="New box (x, y, width, height, label)")

    # State to hold and update the boxes
    current_boxes = gr.State(initial_boxes)

    # Button to trigger box update
    update_button = gr.Button("Update Boxes")

    # Function to be called when update_button is clicked
    update_button.click(update_boxes, inputs=[new_box_input, current_boxes], outputs=image_annotator)

# Launch the interface
demo.launch()
