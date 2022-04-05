from tkinter import *
from tkinter import ttk
import datetime

# Generate output filename from date and time
def generate_filename():
    now = str(datetime.datetime.now())
    now = now.replace(":","-")
    now = now.replace(".","")
    now += ".txt"
    return now

# Main window class
class Window(Frame):

    def __init__(self):
        super().__init__()

        self.last_x = 10
        self.last_y = 0

        self.start_x = 110
        self.start_y = 50

        self.shape_list = []
        self.arc_list = []
        self.shape_index = 0

        self.shape_column = 0
        self.shape_row = 0

        self.shape_data = {}
        self.joined_shapes = {}
        self.current_shape = None
        self.current_data = []

        self.shape_type = {}

        self.triangle_count = 0
        self.square_count = 0
        self.combined_count = 0

        self.initUI()

    def single_shape_clicked(self, event):
        x, y = event.x, event.y
        #shape = self.canvas.find_closest(x, y)
        index = (event.widget.find_withtag("current")[0])
        #c.delete(shape)
        self.current_shape = index
        self.current_data = self.shape_data[index]

        shape = self.shape_type[self.current_shape]
        if shape[:8] == "Centrale" and "+" not in shape:
            self.info_1_entry.configure(state = "normal")
            self.info_2_entry.configure(state = "normal")
            self.info_3_entry.configure(state = "normal")
            self.info_4_entry.configure(state = "normal")
            self.info_5_entry.configure(state = "normal")
            self.info_6_button.configure(text = " << OFF >> ", state = "normal")
            self.info_7_entry.configure(state = "normal")
            self.info_8_entry.configure(state = "disabled")
            self.info_9_entry.configure(state = "disabled")
            self.info_10_entry.configure(state = "disabled")
        elif shape[:6] == "Réservoir":
            self.info_1_entry.configure(state = "normal")
            self.info_2_entry.configure(state = "disabled")
            self.info_3_entry.configure(state = "disabled")
            self.info_4_entry.configure(state = "disabled")
            self.info_5_entry.configure(state = "disabled")
            self.info_6_button.configure(text = " << OFF >> ", state = "disabled")
            self.info_7_entry.configure(state = "disabled")
            self.info_8_entry.configure(state = "normal")
            self.info_9_entry.configure(state = "normal")
            self.info_10_entry.configure(state = "normal")
        elif "+" in shape:
            self.info_1_entry.configure(state = "normal")
            self.info_2_entry.configure(state = "normal")
            self.info_3_entry.configure(state = "normal")
            self.info_4_entry.configure(state = "normal")
            self.info_5_entry.configure(state = "normal")
            self.info_6_button.configure(text = " << OFF >> ", state = "normal")
            self.info_7_entry.configure(state = "normal")
            self.info_8_entry.configure(state = "normal")
            self.info_9_entry.configure(state = "normal")
            self.info_10_entry.configure(state = "normal")    

        self.clear_information()
        self.fetch_information()

    def joined_shape_clicked(self, event):
        x, y = event.x, event.y
        #shape = self.canvas.find_closest(x, y)
        index = (event.widget.find_withtag("current")[0])
        #c.delete(shape)
        reference = self.joined_shapes[index]
        self.current_shape = reference
        self.current_data = self.shape_data[reference]

        shape = self.shape_type[self.current_shape]
        if shape[:8] == "Centrale" and "+" not in shape:
            self.info_1_entry.configure(state = "normal")
            self.info_2_entry.configure(state = "normal")
            self.info_3_entry.configure(state = "normal")
            self.info_4_entry.configure(state = "normal")
            self.info_5_entry.configure(state = "normal")
            self.info_6_button.configure(text = " << OFF >> ", state = "normal")
            self.info_7_entry.configure(state = "normal")
            self.info_8_entry.configure(state = "disabled")
            self.info_9_entry.configure(state = "disabled")
            self.info_10_entry.configure(state = "disabled")
        elif shape[:6] == "Square":
            self.info_1_entry.configure(state = "normal")
            self.info_2_entry.configure(state = "disabled")
            self.info_3_entry.configure(state = "disabled")
            self.info_4_entry.configure(state = "disabled")
            self.info_5_entry.configure(state = "disabled")
            self.info_6_button.configure(text = " << OFF >> ", state = "disabled")
            self.info_7_entry.configure(state = "disabled")
            self.info_8_entry.configure(state = "normal")
            self.info_9_entry.configure(state = "normal")
            self.info_10_entry.configure(state = "normal")
        elif "+" in shape:
            self.info_1_entry.configure(state = "normal")
            self.info_2_entry.configure(state = "normal")
            self.info_3_entry.configure(state = "normal")
            self.info_4_entry.configure(state = "normal")
            self.info_5_entry.configure(state = "normal")
            self.info_6_button.configure(text = " << OFF >> ", state = "normal")
            self.info_7_entry.configure(state = "normal")
            self.info_8_entry.configure(state = "normal")
            self.info_9_entry.configure(state = "normal")
            self.info_10_entry.configure(state = "normal")

        self.clear_information()
        self.fetch_information()

    def clear_last(self):
        if not self.shape_list:
            return

        count = len(self.shape_list)-1

        for shape in self.shape_list[count]:
            self.canvas.delete(shape)

            try:
                if "Centrale + Reservoir" in self.shape_type[shape]:
                    self.combined_count -= 1
                    self.shape_data.pop(shape)
                elif "Square" in self.shape_type[shape]:
                    self.square_count -= 1
                    self.shape_data.pop(shape)
                elif "Centrale" in self.shape_type[shape]:
                    self.triangle_count -= 1
                    self.shape_data.pop(shape)
                
            except:
                pass

        self.shape_list.pop()

        if self.shape_column > 0:
            self.shape_column -= 1
        else:
            self.shape_column = 4
            self.shape_row -= 1
            self.start_y -= 100

            count = len(self.arc_list)

            for line in self.arc_list[count-1]:
                self.canvas.delete(line)

            self.arc_list.pop()

        if self.shape_row % 2 != 0:
            self.last_x = self.start_x
            self.start_x += (100)
        else:
            self.last_x = self.start_x - 100 - 40
            self.start_x -= (100)


    def clear_all(self):
        self.canvas.delete('all')

        self.last_x = 10
        self.last_y = 0

        self.start_x = 110
        self.start_y = 50

        self.shape_list = []
        self.arc_list = []
        self.shape_index = 0

        self.shape_column = 0
        self.shape_row = 0

        self.shape_data = {}
        self.joined_shapes = {}
        self.current_shape = None
        self.current_data = []

        self.shape_type = {}

        self.triangle_count = 0
        self.square_count = 0
        self.combined_count = 0

    # Draw square
    def draw_square(self):
        start_x = self.start_x
        start_y = self.start_y

        last_x  = self.last_x
        last_y  = self.last_y

        side = 60
        spacing_x = 100

        if self.shape_row % 2 == 0:

            line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2)
            square = self.canvas.create_rectangle(start_x, start_y, start_x + side, start_y + side,
                outline="black", fill="#05f", width = 2,tags="single_shape")

            self.last_x = start_x + side
            self.start_x += spacing_x

        else:

            line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2)
            square = self.canvas.create_rectangle(start_x - spacing_x, start_y, start_x - spacing_x + side, start_y + side,
                outline="black", fill="#05f", width = 2,tags="single_shape")


            self.last_x = start_x - spacing_x - side
            self.start_x -= spacing_x

        self.shape_list.append([line, square])

        self.square_count += 1
        self.shape_type[square] = "Tank %s"%self.square_count
        self.shape_data[square] = ["Tank %s"%self.square_count]

        self.canvas.tag_bind("single_shape","<Button-1>",self.single_shape_clicked)

        if self.shape_column < 4:
            self.shape_column += 1

            count = len(self.arc_list)

            if count:
                for line in self.arc_list[count-1]:
                    self.canvas.itemconfigure(line, state = "normal")
        else:
            self.shape_column = 0
            self.shape_row += 1

            if self.shape_row % 2 != 0:
                self.draw_right_arc()
                self.start_y += 100
            else:
                self.draw_left_arc()
                self.start_y += 100

    # Draw triangle
    def draw_triangle(self):
        start_x = self.start_x
        start_y = self.start_y

        last_x  = self.last_x
        last_y  = self.last_y

        side = 60
        spacing_x = 100

        if self.shape_row % 2 == 0:

            line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2)
            triangle = self.canvas.create_polygon((start_x, start_y + side, start_x, start_y, start_x + side, start_y + side/2), 
            outline="black", fill="#05f", width = 2,tags="single_shape")

            self.last_x = start_x + side
            self.start_x += spacing_x

        else:
            line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2)
            triangle = self.canvas.create_polygon((start_x - spacing_x + side , start_y + side, start_x - spacing_x + side, start_y, start_x - spacing_x, start_y + side/2), 
            outline="black", fill="#05f", width = 2,tags="single_shape")

            self.last_x = start_x - spacing_x - side
            self.start_x -= spacing_x

        self.shape_list.append([line, triangle])

        self.triangle_count += 1
        self.shape_type[triangle] = "Power plant %s"%self.triangle_count
        self.shape_data[triangle] = ["Power plant %s"%self.triangle_count]

        self.canvas.tag_bind("single_shape","<Button-1>",self.single_shape_clicked)

        if self.shape_column < 4:
            self.shape_column += 1

            count = len(self.arc_list)

            if count:
                for line in self.arc_list[count-1]:
                    self.canvas.itemconfigure(line, state = "normal")
        else:
            self.shape_column = 0
            self.shape_row += 1

            if self.shape_row % 2 != 0:
                self.draw_right_arc()
                self.start_y += 100
            else:
                self.draw_left_arc()
                self.start_y += 100

    # Draw triangle + square
    def draw_triangle_square(self):
        start_x = self.start_x
        start_y = self.start_y

        last_x  = self.last_x
        last_y  = self.last_y

        side = 60
        spacing_x = 100

        if self.shape_row % 2 == 0:

            line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2)
            square = self.canvas.create_rectangle(start_x, start_y, start_x + side/2, start_y + side,
                outline="black", fill="#05f", width = 2,tags="single_shape")

            last_x = start_x + side/2
            start_x += side/2
            
            triangle = self.canvas.create_polygon((start_x, start_y + side, start_x, start_y, start_x + side/2, start_y + side/2), 
            outline="black", fill="#05f", width = 2,tags="joined_shape")

            self.last_x = start_x + side/2
            self.start_x += spacing_x

        else:
            line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2)
            square = self.canvas.create_rectangle(start_x - spacing_x + side, start_y, start_x - spacing_x + side/2, start_y + side,
                outline="black", fill="#05f", width = 2,tags="single_shape")

            last_x = start_x - side/2
            start_x -= side/2
            
            triangle = self.canvas.create_polygon((start_x - spacing_x + side, start_y + side, start_x - spacing_x + side, start_y, start_x- spacing_x + side/2, start_y + side/2), 
            outline="black", fill="#05f", width = 2,tags="joined_shape")

            self.last_x = start_x - spacing_x - side
            self.start_x -= spacing_x

        self.shape_list.append([line, square, triangle])
        self.joined_shapes[triangle] = square

        self.combined_count += 1
        self.shape_type[square] = "Power plant + Tank %s"%self.combined_count
        self.shape_data[square] = ["Power plant + Tank %s"%self.combined_count]

        self.canvas.tag_bind("single_shape","<Button-1>",self.single_shape_clicked)
        self.canvas.tag_bind("joined_shape","<Button-1>",self.joined_shape_clicked)

        if self.shape_column < 4:
            self.shape_column += 1

            count = len(self.arc_list)

            if count:
                for line in self.arc_list[count-1]:
                    self.canvas.itemconfigure(line, state = "normal")
        else:
            self.shape_column = 0
            self.shape_row += 1

            if self.shape_row % 2 != 0:
                self.draw_right_arc()
                self.start_y += 100
            else:
                self.draw_left_arc()
                self.start_y += 100

    # Draw right arc to go a level below from the right
    def draw_right_arc(self):
        start_x = self.start_x
        start_y = self.start_y

        last_x  = self.last_x
        last_y  = self.last_y

        side = 60
        spacing_x = 100

        h_line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2, state = "hidden")

        v_line = self.canvas.create_line(start_x, start_y + side/2, start_x, start_y + side/2 + 100, width = 2, state = "hidden")

        self.arc_list.append([h_line, v_line])

    # Draw left arc to go a level below from the left
    def draw_left_arc(self):
        start_x = self.start_x
        start_y = self.start_y

        last_x  = self.last_x
        last_y  = self.last_y

        side = 60
        spacing_x = 100

        h_line = self.canvas.create_line(last_x, start_y + side/2, start_x, start_y + side/2, width = 2, state = "hidden")

        v_line = self.canvas.create_line(last_x, start_y + side/2, last_x, start_y + side/2 + 100, width = 2, state = "hidden")

        self.arc_list.append([h_line, v_line])

    # Read input fields and save information to shape
    def save_information(self):
        info_1 = self.info_1_entry.get()
        info_2 = self.info_2_entry.get()
        info_3 = self.info_3_entry.get()
        info_4 = self.info_4_entry.get()
        info_5 = self.info_5_entry.get()
        info_6 = self.info_6_button["text"]
        info_7 = self.info_7_entry.get()
        info_8 = self.info_8_entry.get()
        info_9 = self.info_9_entry.get()
        info_10 = self.info_10_entry.get()

        info = [info_1, info_2, info_3, info_4,info_5, info_6, info_7, info_8,info_9, info_10]
        self.shape_data[self.current_shape] = info
        self.current_data = self.shape_data[self.current_shape]

    # Copy information to input fields
    def fetch_information(self):
        data = self.current_data
        try:
            data[0] = self.shape_type[self.current_shape]
            self.info_1_entry.insert(0, data[0])
        except:
            data.append(self.shape_type[self.current_shape])
            self.info_1_entry.insert(0, data[0])
        if len(data) == 10:
            self.info_2_entry.insert(0,data[1])
            self.info_3_entry.insert(0, data[2])
            self.info_4_entry.insert(0,data[3])
            self.info_5_entry.insert(0,data[4])
            self.info_7_entry.insert(0, data[6])
            self.info_8_entry.insert(0,data[7])
            self.info_9_entry.insert(0, data[8])
            self.info_10_entry.insert(0,data[9])

            self.info_6_button.configure(text = data[5])

    # Clear text boxes
    def clear_information(self):
        self.info_1_entry.delete(0, END)
        self.info_2_entry.delete(0, END)
        self.info_3_entry.delete(0, END)
        self.info_4_entry.delete(0, END)
        self.info_5_entry.delete(0, END)
        self.info_7_entry.delete(0, END)
        self.info_8_entry.delete(0, END)
        self.info_9_entry.delete(0, END)
        self.info_10_entry.delete(0, END)

        self.info_6_button.configure(text = " << OFF >> ")

    # Save data to a text file
    def export_data(self):
        data = list(self.shape_data.values())
        filename = generate_filename()
        with open(filename, "w") as file:
            for line in data:
                for value in line:
                    file.write(value)
                    file.write("\n")

                file.write("\n")

    def show_help(self):
        help_window = Toplevel(root)
        help_window.geometry("640x400")
        help_window.title("Help")
        help_window.iconbitmap("images/help.ico")

        help_text1 = Label(help_window, text = "Hello, this is the help screen!\n\n")
        help_text2 = Label(help_window, text = "You may add as many structures as you wish by clicking on the three add buttons.\n")
        help_text3 = Label(help_window, text = "You may change the settings of the structures at any time by clinking on their drawings.\n")
        help_text4 = Label(help_window, text = "Once you have entered all your settings, you may click on Save Information in order to export the data.\n")
        help_text5 = Label(help_window, text = "You may click on the menu File then Export to export your settings in a .txt file.\n\n")
        help_text6 = Label(help_window, text = "Enjoy!")
        help_text1.pack()
        help_text2.pack()
        help_text3.pack()
        help_text4.pack()
        help_text5.pack()
        help_text6.pack()

    def toggle_turbine_state(self):
        text = self.info_6_button["text"]

        if text == " << OFF >> ":
            self.info_6_button.configure(text = " << ON >> ")

        elif text == " << ON >> ":
            self.info_6_button.configure(text = " << OFF >> ")


    # Create and style UI widgets
    def initUI(self):

        self.master.title("Draw")
        self.pack(fill=BOTH, expand=1)

        # This will create style object
        style = ttk.Style()
        
        # This will be adding style, and
        # naming that style variable as
        # W.Tbutton (TButton is used for ttk.Button).
        style.configure('W.TButton', font =
                    ('calibri', 10, 'bold', 'underline'),
                        foreground = 'red')

        style.configure("TMenubutton", background="#cccccc")

        # Create menubar
        menu = Menu(self.master, bg="gray")
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu, tearoff = 0)
        file.add_command(label="Export", command=self.export_data)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the help object)
        help = Menu(menu, tearoff = 0)
        help.add_command(label="Show Help screen", command=self.show_help)

        #added "file" to our menu
        menu.add_cascade(label="Help", menu=help)

        ## Frame Creation ##

        self.buttons_frame = LabelFrame(self, text="Control Buttons")
        self.buttons_frame.grid(row = 0, column = 0, sticky="ewns", padx = 10, pady = 20)

        self.information_frame = LabelFrame(self, text="Form Selected")
        self.information_frame.grid(row = 1, column = 0,sticky="ewns", padx = 10, pady = 20)

        self.canvas_frame = Frame(self, bg = "white")
        self.canvas_frame.grid(row = 0, column = 1, rowspan=2, sticky="ewns", padx = 20, pady = 20)

        ## Buttons creation ##

        self.add_triangle_button = ttk.Button(self.buttons_frame, text = "Add a Power plant", command=self.draw_triangle)
        self.add_triangle_button.grid(columnspan=2, pady = 5, sticky="ew", padx = 30)

        self.add_square_button = ttk.Button(self.buttons_frame, text = "Add a Tank", command=self.draw_square)
        self.add_square_button.grid(columnspan=2, sticky="ew", padx = 30)

        self.add_triangle_square_button = ttk.Button(self.buttons_frame, text = "Add a Power plant + Tank", command=self.draw_triangle_square)
        self.add_triangle_square_button.grid(columnspan=2, pady = 5, sticky="ew", padx = 30)

        self.clear_last_button = ttk.Button(self.buttons_frame, text = "Clear last", command = self.clear_last)
        self.clear_last_button.grid(row = 3, column = 0, sticky="ew", padx = 30)

        self.clear_all_button = ttk.Button(self.buttons_frame, text = "Clear all", command=self.clear_all)
        self.clear_all_button.grid(row = 3, column = 1, sticky="ew", padx = 30)

        ## Information Entry ##

        self.info_1_label = Label(self.information_frame, text = "Name", anchor = W)
        self.info_1_label.grid(sticky="ew", pady = 5, padx = 30, row = 0, column = 0)

        self.info_1_entry = ttk.Entry(self.information_frame)
        self.info_1_entry.grid(sticky="ew", pady = 5, padx = 30, row = 0, column = 1)

        self.info_2_label = Label(self.information_frame, text = "Inflow", anchor = W)
        self.info_2_label.grid(sticky="ew", pady = 5, padx = 30, row = 1, column = 0)        

        self.info_2_entry = ttk.Entry(self.information_frame)
        self.info_2_entry.grid(sticky="ew", padx = 30, row = 1, column = 1)

        self.info_3_label = Label(self.information_frame, text = "Power Produce", anchor = W)
        self.info_3_label.grid(sticky="ew", pady = 5, padx = 30, row = 2, column = 0)

        self.info_3_entry = ttk.Entry(self.information_frame)
        self.info_3_entry.grid(sticky="ew", pady = 5, padx = 30, row = 2, column = 1)

        self.info_4_label = Label(self.information_frame, text = "Outflow", anchor = W)
        self.info_4_label.grid(sticky="ew", pady = 5, padx = 30, row = 3, column = 0)

        self.info_4_entry = ttk.Entry(self.information_frame)
        self.info_4_entry.grid(sticky="ew", padx = 30, row = 3, column = 1)

        self.info_5_label = Label(self.information_frame, text = "Number of turbine", anchor = W)
        self.info_5_label.grid(sticky="ew", pady = 5, padx = 30, row = 4, column = 0)

        self.info_5_entry = ttk.Entry(self.information_frame)
        self.info_5_entry.grid(sticky="ew", padx = 30, row = 4, column = 1)

        self.info_6_label = Label(self.information_frame, text = "State of turbines", anchor = W)
        self.info_6_label.grid(sticky="ew", pady = 5, padx = 30, row = 5, column = 0)

        self.info_6_button = ttk.Button(self.information_frame, text = " << OFF >> ", command = self.toggle_turbine_state)
        self.info_6_button.grid(sticky="ew", padx = 30, row = 5, column = 1)

        self.info_7_label = Label(self.information_frame, text = "Flow rate per turbine", anchor = W)
        self.info_7_label.grid(sticky="ew", pady = 5, padx = 30, row = 6, column = 0)

        self.info_7_entry = ttk.Entry(self.information_frame)
        self.info_7_entry.grid(sticky="ew", padx = 30, row = 6, column = 1)

        self.info_8_label = Label(self.information_frame, text = "Upstream Elevation", anchor = W)
        self.info_8_label.grid(sticky="ew", pady = 5, padx = 30, row = 7, column = 0)

        self.info_8_entry = ttk.Entry(self.information_frame)
        self.info_8_entry.grid(sticky="ew", padx = 30, row = 7, column = 1)

        self.info_9_label = Label(self.information_frame, text = "Downstream Elevation", anchor = W)
        self.info_9_label.grid(sticky="ew", pady = 5, padx = 30, row = 8, column = 0)

        self.info_9_entry = ttk.Entry(self.information_frame)
        self.info_9_entry.grid(sticky="ew", padx = 30, row = 8, column = 1)

        self.info_10_label = Label(self.information_frame, text = "Volume", anchor = W)
        self.info_10_label.grid(sticky="ew", pady = 5, padx = 30, row = 9, column = 0)

        self.info_10_entry = ttk.Entry(self.information_frame)
        self.info_10_entry.grid(sticky="ew", padx = 30, row = 9, column = 1)

        self.save_info_button = ttk.Button(self.information_frame, text = "Save Information", command = self.save_information)
        self.save_info_button.grid(sticky="ew", padx = 30, pady= 10, columnspan = 2)

        ## Create canvas  ##

        self.canvas = Canvas(self.canvas_frame, bg = "white")   
        self.canvas.pack(fill=BOTH, expand=True)

        # Set grid column weights to define how they stretch
        #self.grid_columnconfigure(0,weight=)
        self.grid_columnconfigure(1,weight=4)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.information_frame.grid_columnconfigure(0, weight=1)
        self.information_frame.grid_columnconfigure(1, weight=4)
        
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)


# Create root window and start event loop
def main():
    global root

    root = Tk()
    ex = Window()
    root.title("UQAC - Hydroelectric Generation System")
    root.iconbitmap("images/logo.ico")
    root.geometry("1100x650+150+30")
    root.mainloop()


if __name__ == '__main__':
    main()