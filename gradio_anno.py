import gradio as gr
from gradio_image_annotation import image_annotator

import requests
import json
import base64

global_annotation = {
    "image": "./dog.jpg",
    "boxes": []
}

def send_visual_prompt(annotations):
    data = {
        "image": base64.b64encode(annotations["image"].tobytes()).decode('utf-8'),
        "orig_shape": annotations["image"].shape, # need to change to own shape
        "orig_dtype": str(annotations["image"].dtype),
        "boxes": annotations["boxes"]
    }
    json_data = json.dumps(data)
    response = requests.post(
        url = "http://127.0.0.1:8989/post_data",
        headers = {"Content-Type": "application/json"},
        data = json_data
    )
    return response.json()

def get_boxes_json(annotations):
    return annotations["boxes"]

with gr.Blocks() as demo:
    annotator = image_annotator(
                    global_annotation,
                    label_list=["P", "N"],
                    label_colors=[(0, 255, 0), (255, 0, 0)],
                )
    button_send = gr.Button("Visual Prompt Detection")
    json_answer_boxes = gr.JSON()
    button_send.click(send_visual_prompt, annotator, json_answer_boxes)
    button_get = gr.Button("Get bounding boxes")
    json_boxes = gr.JSON()
    button_get.click(get_boxes_json, annotator, json_boxes)

demo.launch()