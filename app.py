import streamlit as st
from model import ObjectDetector


def main():
    st.title("Object Detection with YOLOS")
    st.markdown(
        """
        <link rel="stylesheet" href="style.css">
        """,
        unsafe_allow_html=True
    )
    detector = ObjectDetector()
    uploaded_image = st.file_uploader(
        "Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Perform object detection on the uploaded image
        image = detector.detect_objects(uploaded_image)

        # Display the result
        st.image(image, caption="Object Detection Result",
                 use_column_width=True)


if __name__ == "__main__":
    main()
