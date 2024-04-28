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
        st.write("Here's your request!")
        #t = multiprocessing.Process(target=draw_flower(), args=(titles, 500, 500, 200,))
        #t.start()
        st.video("flower_animation.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False)

        multi = '''HB Deina
                ni sesuai rikuwes km ktanya mau dibikinin yg ngoding2 tp yg ngoding bukan ak tp jo WKWKKWKW (\+ km minta kdo dr jo, yak btul ni kodingan adlh kdonya, kta jo susah tau bikinnya)\n
        '''
        st.markdown(multi)

        multi_2 = '''gk tau mau wish apa lg selain wish you were here WKWKWKWK.
                sehat sehat tulang punggung keluarga.
                lop,
                n & j
        '''
        st.markdown(multi_2)



if __name__ == "__main__":
    main()
