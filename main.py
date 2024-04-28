from turtle import *
import colorsys
import streamlit as st
#import multiprocessing
#import tkinter
import imageio
from PIL import Image
import numpy as np


def draw_flower():
    speed(0)
    bgcolor('black')
    h = 0
    frames = []
    for i in range(16):
        for j in range(18):
            c = colorsys.hsv_to_rgb(h, 1, 1)
            color(c)
            h += 0.005
            rt(90)
            circle(150 - j * 6, 90)
            lt(90)
            circle(150 - j * 6, 90)
            rt(180)
            frames.append(get_frame_as_np_array())
        circle(40, 24)
    #done()
    print(len(frames))
    with imageio.get_writer("flower_animation.mp4", mode="I") as writer:
        for index, frame in enumerate(frames):
            print("Index:", index)
            # Do something with the frame
            writer.append_data(frame)


# Function to convert Turtle canvas to numpy array
def get_frame_as_np_array():
    canvas = getscreen().getcanvas()
    canvas.postscript(file="temp.eps", colormode="color")
    img = Image.open("temp.eps")
    img_np = np.array(img)
    return img_np


def main():
    #draw_flower()
    titles = st.title("Happy Birthday Deina")
    st.write("Wish you all the best!")

    clicked = st.button("Click here for your gift!")

    if clicked:
        st.write("Generating Magic Flower")
        #t = multiprocessing.Process(target=draw_flower(), args=(titles, 500, 500, 200,))
        #t.start()
        st.video("flower_animation.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False)


if __name__ == "__main__":
    main()
