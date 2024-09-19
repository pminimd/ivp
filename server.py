from flask import Flask, request, jsonify
import base64
import numpy as np
from PIL import Image
import time

app = Flask(__name__)

# Route to handle POST requests
@app.route('/post_data', methods=['POST'])
def post_data():
    # Retrieve JSON data from the POST request
    data = request.get_json()
    # print(data)

    base64str_imgarray = data["image"]
    image_shape = data["orig_shape"]
    image_dtype = data["orig_dtype"]
    boxes = data["boxes"]
    print(boxes)

    decoded_bytes = base64.b64decode(base64str_imgarray)
    decoded_array = np.frombuffer(decoded_bytes, dtype=image_dtype).reshape(image_shape)
    image = Image.fromarray(decoded_array)
    # image.save(f'received_img_{time.strftime("%Y%m%d_%H%M%S")}.png')
    image.save(f'received_img_{time.time()}.png')

    # Perform any processing with the data here (optional)
    response_data = {
        "message": "Data received successfully",
        "detect_boxes": {
                "label": "P",
                "color": {
                    "0": 0,
                    "1": 255,
                    "2": 0
                },
                "xmin": 27,
                "ymin": 70,
                "xmax": 161,
                "ymax": 148
            }
        }

    # Return a JSON response
    return jsonify(response_data)

if __name__ == '__main__':
    # Run the Flask app on port 8989
    app.run(port=8989)
