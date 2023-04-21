import tkinter as tk
import tkinter.colorchooser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt
import matplotlib
import re
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


bar_count = 0
generate_count = 0

def canvasClear():
    window.ax.cla()      
    try:
        global ax2
        ax2.cla()
        ax2.axis('off')
    except:
        pass
    window.canvas.draw()


def choosecolor1():
    color = tk.colorchooser.askcolor(title="请选择线条颜色")[1]
    color_hex1.set(color)
def choosecolor2():
    color = tk.colorchooser.askcolor(title="请选择线条颜色")[1]
    color_hex2.set(color)
def choosecolor3():
    color = tk.colorchooser.askcolor(title="请选择线条颜色")[1]
    color_hex3.set(color)

#导入中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams.update({'font.size':18})
#定义图像生成函数
def generate_graph(selected_type,data_input_x_entry,data_input_y_entry,line_name_entry,line_color,ax):
    global generate_count
    
    if selected_type == "折线图":
        x_values = data_input_x_entry.get()
        y_values = data_input_y_entry.get()
        line_name = line_name_entry.get()
        x_values = [str(x) for x in re.split(",|，", x_values)]
        y_values = [float(y) for y in re.split(",|，", y_values)]
        for a,b in zip(x_values,y_values):
            ax.text(a,b+0.05, b, ha='center',fontsize=14)
        ax.plot(x_values , y_values ,marker='o', label=line_name , color=line_color)
    if selected_type == "柱状图":
        x_values = data_input_x_entry.get()
        y_values = data_input_y_entry.get()
        x_values = [str(x) for x in re.split(",|，", x_values)]
        y_values = [float(y) for y in re.split(",|，", y_values)]
        line_name = line_name_entry.get()
        for a,b in zip(x_values,y_values):
            ax.text(a,b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=14)
        
        ax.bar(x_values , y_values , label=line_name , color=line_color)
    if selected_type == "散点图":
        x_values = data_input_x_entry.get()
        y_values = data_input_y_entry.get()
        line_name = line_name_entry.get()
        
        x_values = [str(x) for x in re.split(",|，", x_values)]
        y_values = [float(y) for y in re.split(",|，", y_values)]
        for a,b in zip(x_values,y_values):
            ax.text(a,b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=14)
        ax.plot(x_values , y_values ,marker='o', label=line_name , color=line_color)
        
        ax.scatter(x_values, y_values , label=line_name , color=line_color)
    if selected_type == "饼图":
        x_values = data_input_x_entry.get()
        y_values = data_input_y_entry.get()
        x_values = [str(x) for x in re.split(",|，", x_values)]
        y_values = [float(y) for y in re.split(",|，", y_values)]
        ax.pie(y_values,
            labels=x_values,
            autopct="%.2f%%"
        )
    if selected_type == "并列柱状图":
        global bar_count
        print(bar_count)
        x_values = data_input_x_entry.get()
        y_values = data_input_y_entry.get()
        x_values = [str(x) for x in re.split(",|，", x_values)]
        y_values = [float(y) for y in re.split(",|，", y_values)]
        line_name = line_name_entry.get()
        width = 0.3

        if bar_count == 0:
            for a,b in enumerate(y_values):
                ax.text(a,b+0.05, '%.0f' % b, ha='center', fontsize=14)
            ax.bar(np.arange(len(y_values)),y_values,width=width,tick_label=x_values,label=line_name,color=line_color)
            bar_count += 1
        else:
            for a,b in enumerate(y_values):
                ax.text(a+0.3,b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=14)
            ax.bar(np.arange(len(y_values))+width,y_values,width=width,tick_label=x_values,label=line_name,color=line_color)
            bar_count = 0
        
# TODO:
        
def finalGoGo():
    global generate_count , ax2
    # 创建一个画像和子图
    canvasClear()
    if data_name_x_entry1.get():
        selected_type1 = data_type1.get()
        window.ax.set_xlabel(data_name_x_entry1.get())
        window.ax.set_ylabel(data_name_y_entry1.get())
        generate_graph(selected_type1 , data_input_x_entry1 , data_input_y_entry1,line_name_entry1,color_hex1.get(),window.ax)
    if (data_name_x_entry1.get() and data_name_x_entry2.get()) or (data_name_x_entry1.get() and data_name_x_entry3.get()) or (data_name_x_entry3.get() and data_name_x_entry2.get()):
        if generate_count == 0 and data_name_y_entry1.get():
            window.ax.set_ylabel(data_name_y_entry1.get())
            generate_count += 1
        if generate_count == 0 and data_name_y_entry2.get():
            window.ax.set_ylabel(data_name_y_entry2.get())
            generate_count += 1
        if generate_count == 0 and data_name_y_entry3.get():
            window.ax.set_ylabel(data_name_y_entry3.get())
            generate_count += 1
        if generate_count == 1:
            if data_name_x_entry2.get():
                if y_axis_whether_shared2.get() == 1:
                    selected_type2 = data_type2.get()
                    window.ax.set_xlabel(data_name_x_entry2.get())
                    window.ax.set_ylabel(data_name_y_entry2.get())
                    generate_graph(selected_type2 , data_input_x_entry2 , data_input_y_entry2,line_name_entry2,color_hex2.get(),window.ax)
                else:
                    ax2 = window.ax.twinx()
                    selected_type2 = data_type2.get()
                    ax2.set_xlabel(data_name_x_entry2.get())
                    ax2.set_ylabel(data_name_y_entry2.get())
                    generate_graph(selected_type2 , data_input_x_entry2 , data_input_y_entry2,line_name_entry2,color_hex2.get(),ax2)
            if data_name_x_entry3.get():
                if y_axis_whether_shared3.get() == 1:  
                    selected_type3 = data_type3.get()
                    window.ax.set_xlabel(data_name_x_entry3.get())
                    window.ax.set_ylabel(data_name_y_entry3.get())
                    generate_graph(selected_type3 , data_input_x_entry3 , data_input_y_entry3,line_name_entry3,color_hex3.get(),window.ax)    
                else:
                    ax2 = window.ax.twinx()
                    selected_type3 = data_type3.get()
                    ax2.set_xlabel(data_name_x_entry3.get())
                    ax2.set_ylabel(data_name_y_entry3.get())
                    generate_graph(selected_type3 , data_input_x_entry3 , data_input_y_entry3,line_name_entry3,color_hex3.get(),ax2)    
        # 返回共享x轴的第二个轴

    # 如果检测到两个以上的线条，则新增一个坐标轴
    window.ax.legend()
    try:
        ax2.legend()
    except:
        pass
    window.ax.set_title(chart_name_entry.get())
    window.canvas.draw()

        
#生成一个对象 
# window = tk.Tk()
window = ttk.Window()
# 定义颜色全局变量
color_hex1 = tk.StringVar()
color_hex2 = tk.StringVar()
color_hex3 = tk.StringVar()
#themename="darkly"
#窗口的标题，用title
window.title("Graph Generator")
window.iconbitmap("a186y-7gapd-001.ico")
# 窗口的大小，用geometry
window.geometry("2100x900")
#设置主窗口背景颜色
# window['background'] = "white"
# label 控件 ，注意参数
# frame1
y_axis_whether_shared1 = tk.IntVar()

frame1 = tk.Frame(window)
frame1.grid(row=0 , column=0 , sticky="w")
data_name_x_label1 = tk.Label(frame1 , text="X坐标名:").pack(side="left")
data_name_x_entry1 = tk.Entry(frame1)
data_name_x_entry1.pack(side="left")
data_input_x_label1 = tk.Label(frame1 , text="X坐标值:").pack(side="left")
data_input_x_entry1 = tk.Entry(frame1)
data_input_x_entry1.pack(side="left")
data_name_y_label1 = tk.Label(frame1 , text="Y坐标名:").pack(side="left")
data_name_y_entry1 = tk.Entry(frame1)
data_name_y_entry1.pack(side="left")
data_input_y_label1 = tk.Label(frame1 , text="Y坐标值:").pack(side="left")
data_input_y_entry1 = tk.Entry(frame1)
data_input_y_entry1.pack(side="left")
line_name_label1 = tk.Label(frame1 , text="线条名称:").pack(side="left")
line_name_entry1 = tk.Entry(frame1)
line_name_entry1.pack(side="left")
y_axis_shared1 = ttk.Checkbutton(frame1 , text="共用y轴",variable=y_axis_whether_shared1,onvalue=1,offvalue=0).pack(side="left",padx=(5,5))
data_type_label1 = tk.Label(frame1 ,  text="图表类型:").pack(side="left")
data_type1 = ttk.Combobox(frame1)
data_type1['value'] = ('折线图','柱状图','并列柱状图','散点图','饼图')
data_type1.current(0)
data_type1.pack(side="left")
line_color1 = ttk.Button(frame1 , text="点我选择颜色(折/柱/散)" , command =choosecolor1, style=DARK).pack(side="left" , padx=5)

y_axis_whether_shared2 = tk.IntVar()
 
frame2 = tk.Frame(window)
frame2.grid(row=1 , column=0 , sticky="w")
data_name_x_label2 = tk.Label(frame2 , text="X坐标名:").pack(side="left")
data_name_x_entry2 = tk.Entry(frame2)
data_name_x_entry2.pack(side="left")
data_input_x_label2 = tk.Label(frame2 , text="X坐标值:").pack(side="left")
data_input_x_entry2 = tk.Entry(frame2)
data_input_x_entry2.pack(side="left")
data_name_y_label2 = tk.Label(frame2 , text="Y坐标名:").pack(side="left")
data_name_y_entry2 = tk.Entry(frame2)
data_name_y_entry2.pack(side="left")
data_input_y_label2 = tk.Label(frame2 , text="Y坐标值:").pack(side="left")
data_input_y_entry2 = tk.Entry(frame2)
data_input_y_entry2.pack(side="left")
line_name_label2 = tk.Label(frame2 , text="线条名称:").pack(side="left")
line_name_entry2 = tk.Entry(frame2)
line_name_entry2.pack(side="left")
y_axis_shared2 = ttk.Checkbutton(frame2 , text="共用y轴",variable=y_axis_whether_shared2,onvalue=1,offvalue=0).pack(side="left",padx=(5,5))
data_type_label2 = tk.Label(frame2 ,  text="图表类型:").pack(side="left")
data_type2 = ttk.Combobox(frame2)
data_type2['value'] = ('折线图','柱状图','并列柱状图','散点图','饼图')
data_type2.current(1)
data_type2.pack(side="left")
line_color2 = ttk.Button(frame2 , text="点我选择颜色(折/柱/散)" , command=choosecolor2 , style=DARK).pack(side="left" , padx=5)

y_axis_whether_shared3 = tk.IntVar()

frame3 = tk.Frame(window)
frame3.grid(row=2 , column=0 , sticky="w")
data_name_x_label3 = tk.Label(frame3 , text="X坐标名:").pack(side="left")
data_name_x_entry3 = tk.Entry(frame3)
data_name_x_entry3.pack(side="left")
data_input_x_label3 = tk.Label(frame3 , text="X坐标值:").pack(side="left")
data_input_x_entry3 = tk.Entry(frame3)
data_input_x_entry3.pack(side="left")
data_name_y_label3 = tk.Label(frame3 , text="Y坐标名:").pack(side="left")
data_name_y_entry3 = tk.Entry(frame3)
data_name_y_entry3.pack(side="left")
data_input_y_label3 = tk.Label(frame3 , text="Y坐标值:").pack(side="left")
data_input_y_entry3 = tk.Entry(frame3)
data_input_y_entry3.pack(side="left")
line_name_label3 = tk.Label(frame3 , text="线条名称:").pack(side="left")
line_name_entry3 = tk.Entry(frame3)
line_name_entry3.pack(side="left")
y_axis_shared3 = ttk.Checkbutton(frame3 , text="共用y轴",variable=y_axis_whether_shared3,onvalue=1,offvalue=0).pack(side="left",padx=(5,5))
data_type_label3 = tk.Label(frame3 ,  text="图表类型:").pack(side="left")
data_type3 = ttk.Combobox(frame3)
data_type3['value'] = ('折线图','柱状图','并列柱状图','散点图','饼图')
data_type3.current(2)
data_type3.pack(side="left")
line_color3 = ttk.Button(frame3 , text="点我选择颜色(折/柱/散)" , command=choosecolor3 , style=DARK).pack(side="left" , padx=5)

chart_name_label = ttk.Label(window , text="图表名称").grid()
chart_name_entry = tk.Entry(window)
chart_name_entry.grid()
window.fromPlot = ttk.Frame(window)
# 创建画布
window.fig = plt.Figure(figsize = (10,9) ,  dpi= 70)
# 创建子图
window.ax = window.fig.add_subplot(111)         
window.canvas = FigureCanvasTkAgg(window.fig , master = window.fromPlot)
window.canvas.get_tk_widget().grid(row = 3, column = 0)
window.fromPlot.grid(row = 5 , column = 0)

claer_button = ttk.Button(window , text="清空画布" , command= canvasClear , bootstyle=LIGHT).grid()
generate_button = ttk.Button(window , text="生成图表",command=finalGoGo,bootstyle=DARK).grid()
window.mainloop()