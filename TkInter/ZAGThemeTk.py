####################################################################################################################
# IMPORTS
import bisect
import json
import os

import tkinter as tk
import tkinter.font as tk_font

from tkinter import ttk


####################################################################################################################
# CORE
class ZAGThemeTk:
    # ---> CONSTANTS
    DEFAULT = "default"
    DEFAULT_DIR = "tkThemes/"
    STYLE_PREFIX = "ZAG."

    # ---> ATTRIBUTES
    _theme = []
    _current_theme = None
    _sty_name_frame = STYLE_PREFIX + "TFrame"
    _sty_name_button = STYLE_PREFIX + "TButton"
    _sty_name_menubutton = STYLE_PREFIX + "TMenubutton"
    _sty_name_label = STYLE_PREFIX + "TLabel"
    _sty_name_scrollbar = STYLE_PREFIX + "Vertical.TScrollbar"

    # ---> CONSTRUCTOR
    def __init__(self, themes=None):

        file_list = themes
        if themes is None:
            file_list = self._get_default_themes()

        file_list.sort()

        for file in file_list:
            with open(file, "r") as json_file:
                try:
                    theme_data = json.load(json_file)
                except (ValueError, FileNotFoundError):
                    continue

                new_theme = {
                    "theme_name": theme_data["theme_name"],
                    "theme_specs": theme_data["theme_specs"]
                }

                if self._current_theme is None:
                    self._current_theme = new_theme

                if theme_data["theme_name"] == self.DEFAULT:
                    self._current_theme = new_theme

                self._theme.append(new_theme)

                json_file.close()

        self._style = ttk.Style()
        self._style.theme_use("default")
        self._style.configure(self._sty_name_frame)
        self._style.configure(self._sty_name_button, focuscolor="none")
        self._style.configure(self._sty_name_menubutton)
        self._style.configure(self._sty_name_label)
        self._style.configure(self._sty_name_scrollbar)

    # ---> FUNCTIONS
    def _get_default_themes(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        temi_dir = os.path.join(current_dir, self.DEFAULT_DIR)

        file_names = []
        for filename in os.listdir(temi_dir):
            file_path = os.path.join(temi_dir, filename)
            if os.path.isfile(file_path):
                file_names.append(file_path)

        return file_names

    def get_current_theme(self):
        return self._current_theme

    def _set_current_theme(self, theme_name):
        keys = [theme["theme_name"] for theme in self._theme]
        index = bisect.bisect_left(keys, theme_name)
        self._current_theme = self._theme[index]

    def get_loaded_themes(self):
        theme_names = []
        for theme in self._theme:
            theme_names.append(theme["theme_name"])

        return theme_names

    def get_theme_specs(self, theme_name):
        keys = [theme["theme_name"] for theme in self._theme]
        index = bisect.bisect_left(keys, theme_name)
        return self._theme[index]["theme_specs"]

    def _on_btn_enter(self, widget, theme_specs, event):
        if widget.cget("state") != tk.DISABLED:
            """
            widget.configure(background=theme_specs["background"]["on_enter"],
                             foreground=theme_specs["foreground"]["on_enter"])
            """
            style_name = self._sty_name_button
            self._style.configure(style_name,
                                  background=theme_specs["background"]["on_enter"],
                                  foreground=theme_specs["foreground"]["on_enter"])
            widget.configure(style=style_name)

    def _on_btn_leave(self, widget, theme_specs, event):
        if widget.cget("state") != tk.DISABLED:
            """
            widget.configure(background=theme_specs["background"]["default"],
                             foreground=theme_specs["foreground"]["default"])
            """
            style_name = self._sty_name_button
            self._style.configure(style_name,
                                  background=theme_specs["background"]["default"],
                                  foreground=theme_specs["foreground"]["default"])
            widget.configure(style=style_name)

    def _on_btn_disabled(self, widget, theme_specs, event):
        if widget.cget("state") == tk.DISABLED:
            style_name = self._sty_name_button
            widget.configure(style=style_name)

    def apply_theme_component(self, tk_widget, theme):

        if theme != self.get_current_theme()["theme_name"]:
            self._set_current_theme(theme)

        theme_specs = self.get_current_theme()["theme_specs"]

        # ### TK ###
        if isinstance(tk_widget, tk.Tk) or isinstance(tk_widget, tk.Toplevel):
            theme_specs = theme_specs["root"]
            tk_widget.configure(background=theme_specs["background"])

        # ### FRAME ###
        elif isinstance(tk_widget, ttk.Frame):
            theme_specs = theme_specs["frame"]
            style_name = self._sty_name_frame

            self._style.configure(style_name, background=theme_specs["background"])
            tk_widget.configure(style=style_name)

        # ### BUTTON ###
        elif isinstance(tk_widget, ttk.Button):
            theme_specs = theme_specs["button"]
            style_name = self._sty_name_button

            font_specs = theme_specs["font"]
            font = tk_font.Font(
                family=font_specs["family"],
                name=font_specs["name"],
                size=font_specs["size"],
                weight=font_specs["weight"],
                slant=font_specs["slant"]
            )

            self._style.configure(style_name,
                                  background=theme_specs["background"]["default"],
                                  foreground=theme_specs["foreground"]["default"],
                                  borderwidth=theme_specs["borderwidth"],
                                  padding=theme_specs["padding"],
                                  relief=theme_specs["relief"],
                                  justify=theme_specs["justify"],
                                  font=font)
            tk_widget.configure(style=style_name)

            # TODO da capire come applicare a un singolo bottone e non a tutti
            """
            tk_widget.bind("<Enter>", lambda event: self._on_btn_enter(tk_widget, theme_specs, event))
            tk_widget.bind("<Leave>", lambda event: self._on_btn_leave(tk_widget, theme_specs, event))
            tk_widget.bind("<Button-3>", lambda event: self._on_btn_disabled(tk_widget, theme_specs, event))
            """

        # ### MENU BUTTON ###
        elif isinstance(tk_widget, ttk.Menubutton):
            theme_specs = theme_specs["menubutton"]
            style_name = self._sty_name_menubutton

            font_specs = theme_specs["font"]
            font = tk_font.Font(
                family=font_specs["family"],
                name=font_specs["name"],
                size=font_specs["size"],
                weight=font_specs["weight"],
                slant=font_specs["slant"]
            )

            self._style.configure(style_name,
                                  background=theme_specs["background"],
                                  foreground=theme_specs["foreground"],
                                  borderwidth=theme_specs["borderwidth"],
                                  padding=theme_specs["padding"],
                                  relief=theme_specs["relief"],
                                  justify=theme_specs["justify"],
                                  font=font)
            tk_widget.configure(style=style_name)

        # ### MENU ###
        elif isinstance(tk_widget, tk.Menu):
            theme_specs = theme_specs["menu"]

            font_specs = theme_specs["font"]
            font = tk_font.Font(
                family=font_specs["family"],
                name=font_specs["name"],
                size=font_specs["size"],
                weight=font_specs["weight"],
                slant=font_specs["slant"]
            )

            tk_widget.configure(background=theme_specs["background"],
                                foreground=theme_specs["foreground"],
                                activebackground=theme_specs["activebackground"],
                                activeforeground=theme_specs["activeforeground"],
                                font=font)

        # ### LABEL ###
        elif isinstance(tk_widget, ttk.Label):
            theme_specs = theme_specs["label"]
            style_name = self._sty_name_label

            font_specs = theme_specs["font"]
            font = tk_font.Font(
                family=font_specs["family"],
                name=font_specs["name"],
                size=font_specs["size"],
                weight=font_specs["weight"],
                slant=font_specs["slant"]
            )

            self._style.configure(style_name,
                                  background=theme_specs["background"],
                                  foreground=theme_specs["foreground"],
                                  font=font)

            tk_widget.configure(style=style_name)

        # ### ENTRY ###
        elif isinstance(tk_widget, tk.Entry):
            theme_specs = theme_specs["entry"]

            font_specs = theme_specs["font"]
            font = tk_font.Font(
                family=font_specs["family"],
                name=font_specs["name"],
                size=font_specs["size"],
                weight=font_specs["weight"],
                slant=font_specs["slant"]
            )
            tk_widget.configure(background=theme_specs["background"],
                                foreground=theme_specs["foreground"],
                                borderwidth=theme_specs["borderwidth"],
                                relief=theme_specs["relief"],
                                font=font)

        # ### TEXT ###
        elif isinstance(tk_widget, tk.Text):
            theme_specs = theme_specs["text"]

            font_specs = theme_specs["font"]
            font = tk_font.Font(
                family=font_specs["family"],
                name=font_specs["name"],
                size=font_specs["size"],
                weight=font_specs["weight"],
                slant=font_specs["slant"]
            )
            tk_widget.configure(background=theme_specs["background"],
                                foreground=theme_specs["foreground"],
                                borderwidth=theme_specs["borderwidth"],
                                relief=theme_specs["relief"],
                                font=font)

        # ### SCROLLBAR ###
        elif isinstance(tk_widget, ttk.Scrollbar):
            theme_specs = theme_specs["scrollbar"]
            style_name = self._sty_name_scrollbar

            self._style.configure(style_name,
                                  background=theme_specs["background"],
                                  activebackground=theme_specs["activebackground"],
                                  troughcolor=theme_specs["troughcolor"],
                                  arrowsize=0)
            tk_widget.configure(style=style_name)

        else:
            pass

    def apply_theme_recurs(self, widget, theme):

        if widget.winfo_parent() == "" or isinstance(widget, tk.Toplevel):
            self.apply_theme_component(widget, theme)

        children = widget.winfo_children()
        for child in children:
            self.apply_theme_component(child, theme)
            self.apply_theme_recurs(child, theme)


if __name__ == "__main__":

    def update_scrollbar_visibility(scrollbar_widget, text_widget, event=None):
        if text_widget.yview()[0] == 0:
            scrollbar_widget.grid_forget()
        else:
            scrollbar_widget.grid(row=0, column=1, sticky="ns")
            text_widget.config(yscrollcommand=scrollbar_widget.set)


    root = tk.Tk()


    def switch_theme():
        current_theme = zag_theme.get_current_theme()["theme_name"]
        if current_theme == "default":
            zag_theme.apply_theme_recurs(root, "dark")
        elif current_theme == "dark":
            zag_theme.apply_theme_recurs(root, "default")


    frame = ttk.Frame(root)
    frame.pack(padx=20, pady=20)

    label = ttk.Label(frame, text="Label Text")
    label.pack()

    entry = tk.Entry(frame)
    entry.pack(pady=10)

    button = ttk.Button(frame, text="Switch Theme", command=switch_theme)
    button.pack()

    frame_text = ttk.Frame(frame)
    frame_text.pack()

    text = tk.Text(frame_text, height=3)
    text.grid(row=0, column=0)
    text.bind("<KeyRelease>", lambda event: update_scrollbar_visibility(scrollbar, text, event))

    scrollbar = ttk.Scrollbar(frame_text, orient="vertical", command=text.yview, takefocus=0)
    text.config(yscrollcommand=scrollbar.set)
    update_scrollbar_visibility(scrollbar, text)

    zag_theme = ZAGThemeTk()
    zag_theme.apply_theme_recurs(root, "dark")

    root.mainloop()
