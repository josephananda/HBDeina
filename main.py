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
        #st.write("Here's your request!")
        #t = multiprocessing.Process(target=draw_flower(), args=(titles, 500, 500, 200,))
        #t.start()
        st.video("flower_animation_letters.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False)

        line_1 = '''HB Deina'''
        line_2 = '''ni sesuai rikuwes km ktanya mau dibikinin yg ngoding2 tp yg ngoding bukan ak tp jo WKWKKWKW (\+ km minta kdo dr jo, yak btul ni kodingan adlh kdonya, kta jo susah tau bikinnya)'''
        line_3 = ''''''
        line_4 = '''gk tau mau wish apa lg selain wish you were here WKWKWKWK.'''
        line_5 = '''sehat sehat tulang punggung keluarga.'''
        line_6 = ''''''
        line_7 = '''lop,'''
        line_8 = '''N & J'''
        st.markdown(line_1)
        st.markdown(line_2)
        st.markdown(line_3)
        st.markdown(line_4)
        st.markdown(line_5)
        st.markdown(line_6)
        st.markdown(line_7)
        st.markdown(line_8)


if __name__ == "__main__":
    main()
