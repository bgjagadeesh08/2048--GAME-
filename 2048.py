from tkinter import Frame,Label,CENTER

import logicfile

import constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind("<key>",self.key_down)
        self.commands={c.KEY_UP: Logicfile.move_up ,c.KEY_DOWN : Logicfile.move_down, c.KEY_LEFT :Logicfile.move_left ,c.MOVE_RIGHT : logicfile.move_right}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()
    def init_grid(self):
        background=Frame(self, bg=c.BACKGROUND_COLOR_GAME ,width =c.SIZE ,height=c.SIZE)
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                Cell =Frame(background ,bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                            width=c.SIZE/c.GRID_LEN,
                            height=c.SIZE/c.GRID_LEN)
                Cell.grid(row=i ,column=j ,padx=c.GRID_PADDING ,
                          pady=c.GRID_PADDING)
                t=Label(master=cell ,text="",
                        bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                        justify=CENTER ,font=c.FONT ,width =5 ,height =2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)
    def init_matrix(self):
        self.matrix=Logicfile.start_game()
        Logicfile.add_2(self.matrix)
        Logicfile.add_2(self.matrix)
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for i in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j] .configure(text="" ,bg =c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text =str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],
                                                    fg=c.CELL_COLOR_DICT[new_number])

                
        self.update_idletasks()
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands :
            self.matrix ,changed = self.commands[repr (event.char)](self.matrix)
            if changed:
                Logicfile.add2(self.matrix)
                self.update_grid_cells()
                changed=False
                if Logicfile.get_current(self.matrix) =="WON":
                    self.grid_cells[1][1].configure(text="YOU" ,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="WIN!" ,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if Logicfile.get_current(self.matrix)=="LOSE":
                    self.grid_cells[1][1].configure(text="YOU" ,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!" ,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    
                    
                
        
