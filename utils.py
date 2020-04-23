from typing import List,Tuple
import numpy as np
from PIL import Image
from numpy import array
from numpy import ndarray
import pytesseract
from Letter import Letter
import asyncio

TOLERANCE=3

def get_rows(image_bin:ndarray,image_rgb:ndarray)->Tuple[List[np.ndarray],List[np.ndarray]]:
    rows_bin=[]
    rows_rgb=[]
    start=0
    end=0
    looking_for_row_end=False
    for i in range(0,int(image_bin.shape[0])):
        if looking_for_row_end and image_bin[i].all():
            end=i
            rows_bin.append(image_rgb[start-TOLERANCE:(end+1+TOLERANCE)])
            rows_rgb.append(image_bin[start-TOLERANCE:(end+1+TOLERANCE)])
            looking_for_row_end=False
        elif not(looking_for_row_end) and not(image_bin[i].all()) and (i+1!=int(image_bin.shape[0]) and not(image_bin[i+1].all())):
            start=i
            looking_for_row_end=True
    return (rows_bin,rows_rgb)


def split_rows_to_letters(rows_bin: List[np.ndarray], rows_rgb: List[np.ndarray], cordinates) ->List[List[np.ndarray]]:
    letters_grid=[]
    for index,row in enumerate(rows_bin):
       row_letters_list=split_row_for_letters_img(cordinates,rows_rgb[index])
       letters_grid.append(row_letters_list)
    return letters_grid


def split_row_for_letters_img(cordinates:List[Tuple[int,int]], rows_rgb:np.ndarray):

    letters = []
    start = 0
    end = 0
    looking_for_letter_end = False
    for letter_cordinates in cordinates:
        letters.append(rows_rgb[:,letter_cordinates[0]:letter_cordinates[1]])
    return letters


def get_columns_cordintaes(image_bin:np.ndarray)->List[Tuple[int,int]]:
    columns_cordinates = []
    start = 0
    end = 0
    looking_for_letter_end = False
    for i in range(0, int(image_bin.shape[1])):
        if looking_for_letter_end and image_bin[:, i].all():
            end = i
            columns_cordinates.append((start - TOLERANCE,end + 1 + TOLERANCE))

            looking_for_letter_end = False
        elif not (looking_for_letter_end) and not (image_bin[:, i].all()):
            start = i
            looking_for_letter_end = True
    return columns_cordinates


def split_image_to_images_of_letters(image_bin:ndarray,image_rgb:ndarray)->list:
    """
    split one image of grid of letters to collection of images of letters
:return list of numpy arrays which includes images of latters
    """
    rows_rgb,rows_bin,=get_rows(image_bin,image_rgb)
    columns_cordinates=get_columns_cordintaes(image_bin)
    letters_img_np=split_rows_to_letters(rows_bin,rows_rgb,columns_cordinates)
    return letters_img_np

def to_binary(x:np.ndarray,mean):


    if(x.mean()>=mean):
        return True
    else:
        return False


def convert_to_binar(image_np):
    fun=np.vectorize(to_binary)
    result=np.apply_along_axis(to_binary, 2, image_np, min(image_np.mean(),170))
    r=image_np[:,:,0]
    g=image_np[:,:,1]
    b=image_np[:,:,2]
    return result

def load_image_as_np_array(image_name:str, is_rgb)->ndarray:
    """

    :param image_name: string
    :return: returns image as numpy array
    """
    image = Image.open(image_name)
    image_np = array(image)
    if not(is_rgb):
        image_np=convert_to_binar(image_np)
        # image=image.convert('1')
    # image_np=array(image)

    return image_np




def convert_images_to_letters(img_letters:List[List[np.ndarray]],signal)->List[List[Letter]]:


    table=[]
    rows_number=len(img_letters)
    for r_index,row in enumerate(img_letters):
        table.append([])

        for letter_img in row:
            letter_character: str = " "
            if letter_img.min()<=170:
                letter_character:str=pytesseract.image_to_string(letter_img, config="--psm 10")[0]
                if letter_character=="=":
                    letter_character="e"
            letter_character=letter_character.lower()

            table[r_index].append(Letter(letter_img,letter_character))
        signal.emit(100*((r_index+1)/rows_number))

    return table



def mark_letter(letter:Letter):
    image=letter.img_letter
    np.apply_along_axis(mark,2,image)
def mark(x:np.ndarray):
    x[0]-=100
    x[2] -= 100


def split_image_to_images_of_words(image_np_bin:np.ndarray, image_np_rgb:np.ndarray):
   result=pytesseract.image_to_string(image_np_rgb,config="--psm 4")
   result=result.split("\n")
   result=list(filter(lambda x:len(x)!=0, result))
   return result