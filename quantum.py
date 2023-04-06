###############################
# drawing.py
###############################
import matplotlib.pyplot as plt

# drawing used for math

def plot_2D_plane(right=5,up=5,left=-5,down=-5,fsize=(8,8)):
    hpoints, vpoints = [],[]
    for i in range(left,right+1):
        if i!=0: hpoints.append(i)
    for i in range(down,up+1):
        if i!=0: vpoints.append(i)
    
    ax = plt.figure(figsize=fsize).gca()

    # Set identical scales for both axes
    ax.set(xlim=(left-1,right+1), ylim=(down-1, up+1), aspect='equal')
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    # Create minor ticks placed at each integer to enable drawing of minor grid
    ax.set_xticks(hpoints)
    ax.set_yticks(vpoints)
    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (0), marker='<', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    ax.plot((0), (0), marker='v', transform=ax.get_xaxis_transform(), **arrow_fmt)

def draw_sides(x=1,y=2,side_color="b",lwidth=1):
    plt.arrow(x,0,0,y,color=side_color,linestyle="dotted",width=0.001*lwidth)
    plt.arrow(0,y,x,0,color=side_color,linestyle="dotted",width=0.001*lwidth)
    
def draw_vector(x=1,y=2,vname="v",show_name=True,vcolor="b",sides=False,side_color="b",lwidth=1):
    plt.quiver(0,0,x,y,scale=1,scale_units='xy',angles = 'xy',color=vcolor,width=0.008*lwidth)
    dx = x
    if y<0: dy=y-0.3
    else: dy = y+0.3
        
    if show_name:
        vector_name="$"+vname+"=("+str(x)+","+str(y)+")$"
        plt.text(dx,dy,vector_name,color=vcolor)
    
    if sides:
        draw_sides(x,y,side_color)

def place_text(x,y,text,tcolor="blue"):
    plt.text(x,y,text,color=tcolor)

def show_plt():
    plt.show()
    
# drawing used for quantum
def draw_axes():
	points = [ [1.2,0], [0,1.2], [-1.2,0], [0,-1.2] ] # dummy points for zooming out
	arrows = [ [1.1,0], [0,1.1], [-1.1,0], [0,-1.1] ] # coordinates for the axes
	for p in points: 
		plt.plot(p[0],p[1]+0.1) # drawing dummy points
	for a in arrows: 
		plt.arrow(0,0,a[0],a[1],head_width=0.04, head_length=0.08) # drawing the axes


def draw_unit_circle():
    unit_circle= plt.Circle((0,0),1,color='black',fill=False)
    plt.gca().add_patch(unit_circle)
	
def draw_quantum_state(x,y,name):
	# shorten the line length to 0.92
	# line_length + head_length should be 1
	x1 = 0.92 * x
	y1 = 0.92 * y
	plt.arrow(0,0,x1,y1,head_width=0.04,head_length=0.08,color="blue")
	x2 = 1.15 * x
	y2 = 1.15 * y
	plt.text(x2,y2,name)
	
def draw_qubit():
	# draw a figure
	plt.figure(figsize=(6,6), dpi=60)
	# draw the origin
	plt.plot(0,0,'ro') # a point in red color
	# drawing the axes by using one of our predefined function
	draw_axes()
	# drawing the unit circle by using one of our predefined function
	draw_unit_circle()
	# drawing |0>
	plt.plot(1,0,"o")
	plt.text(1.05,0.05,"|0>")
	# drawing |1>
	plt.plot(0,1,"o")
	plt.text(0.05,1.05,"|1>")
	# drawing -|0>
	plt.plot(-1,0,"o")
	plt.text(-1.2,-0.1,"-|0>")
	# drawing -|1>
	plt.plot(0,-1,"o")
	plt.text(-0.2,-1.1,"-|1>")

def draw_qubit_grover():
	# draw a figure
	plt.figure(figsize=(7,7), dpi=60)
	# draw the origin
	plt.plot(0,0,'ro') # a point in red color
	# drawing the axes by using one of our predefined function
	draw_axes()
	# drawing the unit circle by using one of our predefined function
	draw_unit_circle()
	# drawing |0>
	plt.plot(1,0,"o")
	plt.text(1.05,0.05,"|unmarked>")
	# drawing |1>
	plt.plot(0,1,"o")
	plt.text(0.05,1.05,"|marked>")
	# drawing -|0>
	plt.plot(-1,0,"o")
	plt.text(-0.98,-0.09,"-|unmarked>")
	# drawing -|1>
	plt.plot(0,-1,"o")
	plt.text(-0.4,-1.1,"-|marked>")

###############################
# quantum_state.py
###############################
import random, math

# randomly create a 2-dimensional quantum state
def random_qstate_by_value():
    first_entry = random.randrange(-100,101)
    second_entry = random.randrange(-100,101)
    length_square = first_entry**2+second_entry**2
    while length_square == 0:
        first_entry = random.randrange(-100,101)
        second_entry = random.randrange(-100,101)
    length_square = first_entry**2+second_entry**2
    first_entry = first_entry / length_square**0.5
    second_entry = second_entry / length_square**0.5
    return [first_entry,second_entry]
	
# randomly create a 2-dimensional quantum state	
def random_qstate_by_angle(precision=1):
    sample_angle = 360 * (10**precision)
    angle_degree = random.randrange(sample_angle)
    angle_radian = 2 * math.pi * angle_degree / sample_angle
    return [math.cos(angle_radian),math.sin(angle_radian)]	
	
# finding the angle of a 2-dimensional quantum state
def angle_qstate(x,y):
    angle_radian = math.acos(x) # radian of the angle with state |0>
    angle_degree = 360*angle_radian/(2*math.pi) # degree of the angle with state |0>
	# if the second amplitude is negative, 
	#     then angle is (-angle_degree)
	#     or equivalently 360 + (-angle_degree)
    if y<0: angle_degree = 360-angle_degree # degree of the angle
	# else degree of the angle is the same as degree of the angle with state |0>
    return angle_degree	


###############################
# grover.py
###############################
def giant_oracle(circuit99,quantum_reg):
    number=18
    if(number%2 == 0):
        circuit99.x(quantum_reg[0])
    if(number%4 < 2):
        circuit99.x(quantum_reg[1])
    if(number%8 < 4):
        circuit99.x(quantum_reg[2])
    if(number%16 < 8):
        circuit99.x(quantum_reg[3])
    if(number%32 < 16):
        circuit99.x(quantum_reg[4])
    if(number%64 < 32):
        circuit99.x(quantum_reg[5])
    if(number%128 < 64):
        circuit99.x(quantum_reg[6])
    if(number%256 < 128):
        circuit99.x(quantum_reg[7])
    if(number%512 < 256):
        circuit99.x(quantum_reg[8])
    if(number < 512):
        circuit99.x(quantum_reg[9])
    
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    
    if(number%2 == 0):
        circuit99.x(quantum_reg[0])
    if(number%4 < 2):
        circuit99.x(quantum_reg[1])
    if(number%8 < 4):
        circuit99.x(quantum_reg[2])
    if(number%16 < 8):
        circuit99.x(quantum_reg[3])
    if(number%32 < 16):
        circuit99.x(quantum_reg[4])
    if(number%64 < 32):
        circuit99.x(quantum_reg[5])
    if(number%128 < 64):
        circuit99.x(quantum_reg[6])
    if(number%256 < 128):
        circuit99.x(quantum_reg[7])
    if(number%512 < 256):
        circuit99.x(quantum_reg[8])
    if(number < 512):
        circuit99.x(quantum_reg[9])

def giant_oracle2(circuit99,quantum_reg):
    numbers=[12,45]
    for number in numbers:
        if(number%2 == 0):
            circuit99.x(quantum_reg[0])
        if(number%4 < 2):
            circuit99.x(quantum_reg[1])
        if(number%8 < 4):
            circuit99.x(quantum_reg[2])
        if(number%16 < 8):
            circuit99.x(quantum_reg[3])
        if(number%32 < 16):
            circuit99.x(quantum_reg[4])
        if(number%64 < 32):
            circuit99.x(quantum_reg[5])
        if(number%128 < 64):
            circuit99.x(quantum_reg[6])
        if(number%256 < 128):
            circuit99.x(quantum_reg[7])
        if(number%512 < 256):
            circuit99.x(quantum_reg[8])
        if(number < 512):
            circuit99.x(quantum_reg[9])

        circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
        circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
        circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
        circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
        circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])

        circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
        circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])

        circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
        circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
        circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])

        circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
        circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])

        circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
        circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
        circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
        circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
        circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])

        if(number%2 == 0):
            circuit99.x(quantum_reg[0])
        if(number%4 < 2):
            circuit99.x(quantum_reg[1])
        if(number%8 < 4):
            circuit99.x(quantum_reg[2])
        if(number%16 < 8):
            circuit99.x(quantum_reg[3])
        if(number%32 < 16):
            circuit99.x(quantum_reg[4])
        if(number%64 < 32):
            circuit99.x(quantum_reg[5])
        if(number%128 < 64):
            circuit99.x(quantum_reg[6])
        if(number%256 < 128):
            circuit99.x(quantum_reg[7])
        if(number%512 < 256):
            circuit99.x(quantum_reg[8])
        if(number < 512):
            circuit99.x(quantum_reg[9])

def giant_diffusion(circuit99,quantum_reg):
    for i in range(10):
        circuit99.h(quantum_reg[i])
        circuit99.x(quantum_reg[i])

    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])

    for i in range(10):
        circuit99.x(quantum_reg[i])
        circuit99.h(quantum_reg[i])
    
    circuit99.x(quantum_reg[10])


def Uf(circuit,qreg):
	circuit.ccx(qreg[0],qreg[1],qreg[2])
	
def Uf_8(circuit,quantum_reg):
	circuit.x(quantum_reg[2])
	circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[4])
	circuit.ccx(quantum_reg[4],quantum_reg[0],quantum_reg[3])
	circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[4])
	circuit.x(quantum_reg[2])
	
