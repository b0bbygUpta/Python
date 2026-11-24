import streamlit as st
from PIL import Image 
import os

uploaded_file=st.file_uploader("Upload an image", type=["png","jpg","jpng"])
if uploaded_file is not None:
    # output_image="./image.png"
    # st.image(uploaded_file, "Uploaded image")
    image=Image.open(uploaded_file)
    image.save(f"saved_images/{uploaded_file.name}")





os.makedirs("saved_images", exist_ok=True)

# st.image(output_image)


# print("18:45")


















































# import ollama 
# import os

# import streamlit as st



# # import streamlit as st
# from PIL import Image 
# # import os

# uploaded_file=st.file_uploader("Upload an image", type=["png","jpg","jpng"])
# if uploaded_file is not None:
#     # output_image="./image.png"
#     # st.image(uploaded_file, "Uploaded image")
#     image=Image.open(uploaded_file)
#     image.save(f"saved_images/{uploaded_file.name}")





# os.makedirs("saved_images", exist_ok=True)

# # st.image(output_image)


# # print("18:45")

# # print("hellop")

# model="pika:latest"

# # input_image="./saved_images/Screenshot 2026-06-07 153835.png"


# input_image=uploaded_file

# # st.write("sllkj")


# # try:
# #     response=ollama.generate(model=model)
# #     generated_text= response.get("response", "")


# # except Exception as e: 
# #     print("An error occurred:", str(e))


# def res(input_image):
        
#     try:
#         response=ollama.generate(model=model)
#         generated_text= response.get("response", "")


#     except Exception as e: 
#         generated_text= "An error occurred:", str(e)

#     return generated_text


# st.write(res(input_image))
        




import streamlit as st
from PIL import Image
import ollama
import os

# model = "pika"

model="llava:7b"

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

prompt="""
    Give me the detail available to the orgainism such as name of organism, habitat, eating habits, is it venomous or not (or it carries any kind of virus, bacteria or etc), if venomous what could be the cure and other detail the under stand that particular organism, & the history of the that organism if possible. Also show if there is any fun or knowledga
    """
if uploaded_file is not None:

    os.makedirs("saved_images", exist_ok=True)

    image = Image.open(uploaded_file)

    save_path = os.path.join(
        "saved_images",
        uploaded_file.name
    )

    image.save(save_path)

    st.image(image, caption="Uploaded Image")

    try:
        response = ollama.generate(
            model=model,
            prompt=prompt,
            # "Describe this image",
            images=[save_path]
        )

        st.write("yet to reach")
        st.write(response["response"])
        st.write("passed from there")

    except Exception as e:
        st.error(str(e))