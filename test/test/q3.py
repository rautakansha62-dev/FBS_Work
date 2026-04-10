#A  farmer has a field which is half in circle share  and rest rectangle. he need to do fenching for
# entire field using barbed wire 5 times. Circular section has radius 20m and rectangle length is 50m 
#and breadth is 40m. if cost of barbed wire is 35RS/m then calculate the total cost of fencing the field.
import math
radius = 20
length = 50
breadth = 40
cost_per_meter = 35
if radious > 0 and length > 0 and breadth > 0 and cost_per_meter > 0:
    circular_section_perimeter = math.pi * radius
    rect_section_perimeter = 2 * (length + breadth)
    total_perimeter = circular_section_perimeter + rectangular_section_perimeter
    total_fencing_length = total_perimeter * 5
    total_cost = total_fencing_length * cost_per_meter
    print(f'Total cost of fencing the field: {total_cost} RS')