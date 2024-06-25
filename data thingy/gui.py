import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class MatplotlibGUI:
    def __init__(self, root, graphs):
        self.root = root
        self.root.title('Matplotlib GUI')

        self.plot_index = 0

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack()

        self.graphs = graphs


        self.btn_prev = ttk.Button(self.root, text=self.get_prev_button_text(), command=self.prev_graph)
        self.btn_prev.pack(side=tk.LEFT, padx=10)

        self.btn_next = ttk.Button(self.root, text=self.get_next_button_text(), command=self.next_graph)
        self.btn_next.pack(side=tk.LEFT, padx=10)

        self.graph_selector = ttk.Combobox(self.root, values=[graph['title'] for graph in self.graphs], state='readonly')
        self.graph_selector.current(0)  # Set initial selection to the first graph
        self.graph_selector.pack(side=tk.LEFT, padx=10)
        self.graph_selector.bind('<<ComboboxSelected>>', self.on_graph_select)

        self.update_plot()

    def get_next_button_text(self):
        next_index = (self.plot_index + 1) % len(self.graphs)
        return f'Next Graph: {self.graphs[next_index]["title"]}'
    
    def get_prev_button_text(self):
        prev_index = (self.plot_index - 1) % len(self.graphs)
        return f'Next Graph: {self.graphs[prev_index]["title"]}'

    def next_graph(self):
        self.plot_index += 1
        if self.plot_index >= len(self.graphs):
            self.plot_index = 0
        self.update_plot()

    def prev_graph(self):
        self.plot_index -= 1
        if self.plot_index < 0:
            self.plot_index = len(self.graphs) - 1
        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        graph = self.graphs[self.plot_index]
        self.ax.plot(graph['data'][0], graph['data'][1])
        self.ax.set_title(graph['title'])
        self.canvas.draw()

        self.btn_next.config(text=self.get_next_button_text())

    def on_graph_select(self, event):
        selected_index = self.graph_selector.current()
        self.plot_index = selected_index
        self.update_plot()
