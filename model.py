from transformers import YolosImageProcessor, YolosForObjectDetection
from PIL import Image, ImageDraw
import torch


class ObjectDetector:
    def __init__(self):
        self.model = YolosForObjectDetection.from_pretrained(
            'hustvl/yolos-tiny')
        self.image_processor = YolosImageProcessor.from_pretrained(
            "hustvl/yolos-tiny")

    def detect_objects(self, image_path):
        # Load the image
        image = Image.open(image_path)

        # Process the image
        inputs = self.image_processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)

        # Post-process the results
        target_sizes = torch.tensor([image.size[::-1]])
        results = self.image_processor.post_process_object_detection(
            outputs, threshold=0.9, target_sizes=target_sizes)[0]

        # Draw bounding boxes and labels on the image
        draw = ImageDraw.Draw(image)
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            draw.rectangle(box, outline="blue", width=1)
            draw.text(box[0], box[1]), f"{self.model.config.id2label[label.item()]}: {
                      round(score.item(), 3)}", fill="red")

        return image
