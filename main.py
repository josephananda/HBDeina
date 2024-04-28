#from turtle import *
#import colorsys
import streamlit as st
#import multiprocessing
#import tkinter
#import imageio
#from PIL import Image
#import numpy as np

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
