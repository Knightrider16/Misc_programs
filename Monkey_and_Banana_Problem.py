def monkey_banana(monkey_input,box_input):
    monkey_pos=monkey_input
    box_pos=box_input
    banana_taken=False

    if not banana_taken:
        if monkey_pos!="top of box":
            if box_pos!="near banana":
                if monkey_pos!="near box":
                    monkey_pos="near box"
                    print(f"The monkey goes {monkey_pos}")
                box_pos="near banana"
                print(f"The monkey pushes box to {box_pos}")
            monkey_pos="top of box"
            print(f"The monkey is at {monkey_pos}")
        banana_taken=True
    print(f"The monkey took the banana")

monkey_pos_inputs={1:"ground",2:"near box"}
box_pos_inputs={1:"away from banana",2:"near banana"}
monkey_input=monkey_pos_inputs[int(input(f"Enter the corresponding digit from {monkey_pos_inputs} for the monkey's position"))]
box_input=box_pos_inputs[int(input(f"Enter the corresponding digit from {box_pos_inputs} for the box's position"))]
monkey_banana(monkey_input,box_input)
