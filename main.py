import streamlit as st 
from PIL import Image
from rembg import remove


st.title("Remove Image Background ")
st.link_button(label="Youtube Channel",url="https://www.youtube.com/@Here_We_Code")

inserted_image = st.file_uploader(label="Upload Your Image Here",type="jpg")
col1,col2 = st.columns(2)
with col1:
    if inserted_image:
        st.image(inserted_image)
    input = Image.open(inserted_image)
    output_image = "rembgImage.jpeg"
    output = remove(input)
    output.save(output_image)
    st.video("https://youtu.be/tf_V9o-vHA8?si=AjIrnENOfwwVJAPW")
with col2 :
    st.download_button(
        label="Download ",
        data=output_image,
        file_name=output_image,
   

    )
    st.video("https://youtu.be/VK9kpfRvrvk?si=Jwvu6ReitLe9a2Qa",autoplay=True)






