from turtle import *
import colorsys
import streamlit as st
import multiprocessing
#import tkinter


def draw_flower():
    speed(0)
    bgcolor('black')
    h = 0
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
        circle(40, 24)
    done()


def main():
    titles = st.title("Happy Birthday Deina")
    st.write("Wish you all the best!")

    clicked = st.button("Click here for your gift!")

    if clicked:
        st.write("Generating Magic Flower")
        t = multiprocessing.Process(target=draw_flower(), args=(titles, 500, 500, 200,))
        t.start()


if __name__ == "__main__":
    main()
