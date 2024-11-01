import streamlit as st 
from PIL import Image
from rembg import remove
import io

st.title("Remove Image Background")
st.link_button(label="Youtube Channel", url="https://www.youtube.com/@Here_We_Code")

# File uploader
inserted_image = st.file_uploader(label="Upload Your Image Here", type="jpg")
col1, col2 = st.columns(2)

if inserted_image:
    with col1:
        st.image(inserted_image, caption="Original Image")

    # Remove background
    input_image = inserted_image.read()
    output_data = remove(input_image)

    # Load output into PIL image
    output_image = Image.open(io.BytesIO(output_data))

    # Display processed image
    with col2:
        st.image(output_image, caption="Background Removed")

    # Convert output image to BytesIO for download
    output_buffer = io.BytesIO()
    output_image.save(output_buffer, format="PNG")
    output_buffer.seek(0)

    # Download button
    st.download_button(
        label="Download",
        data=output_buffer,
        file_name="rembgImage.png",
        mime="image/png"
    )

# Add video links
st.video("https://youtu.be/tf_V9o-vHA8?si=AjIrnENOfwwVJAPW")
st.video("https://youtu.be/VK9kpfRvrvk?si=Jwvu6ReitLe9a2Qa", autoplay=True)
