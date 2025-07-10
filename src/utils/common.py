import os
import aiofiles
import base64

def temp_path_generator(file_name:str, parent_directory:str="src", sub_directory:str="temp"):
    temp_path = os.path.join(os.getcwd(),parent_directory,sub_directory,file_name)
    return temp_path

async def file_generator(file_path, file_content):
    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await file_content.read()
            await out_file.write(content)
        return
    except Exception as err:
        print("exception occured during generating file",str(err))

async def base64_converter(file_path):

    with open(file_path, "rb") as audio_file:
        file_base64 = base64.b64encode(audio_file.read()).decode("utf-8")
    return file_base64

