#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import numpy as np
import kinematics_algorithm as ka



def action_pub(gait_data, data_length):
    j = 0
    while (j<1):
        for i in range(data_length):
            LF_HAA_pos_pub.publish(gait_data.data[i, 0])
            LF_HFE_pos_pub.publish(gait_data.data[i, 1])
            LF_KFE_pos_pub.publish(gait_data.data[i, 2])
            LH_HAA_pos_pub.publish(gait_data.data[i, 3])
            LH_HFE_pos_pub.publish(gait_data.data[i, 4])
            LH_KFE_pos_pub.publish(gait_data.data[i, 5])
            RF_HAA_pos_pub.publish(gait_data.data[i, 3])
            RF_HFE_pos_pub.publish(gait_data.data[i, 4])
            RF_KFE_pos_pub.publish(gait_data.data[i, 5])
            RH_HAA_pos_pub.publish(gait_data.data[i, 0])         
            RH_HFE_pos_pub.publish(gait_data.data[i, 1])
            RH_KFE_pos_pub.publish(gait_data.data[i, 2])
            pause.sleep()
        j = j + 1
    return


def command_analysis(action_command):
    if action_command == 'k':
        rate, gait_np_data = ka.keep_gait()
    elif action_command == 'w':
        rate, gait_np_data = ka.forward_gait()
    elif action_command == 's':
        rate, gait_np_data = ka.backward_gait()
    # elif action_command == 'a':
    #     rate, gait_np_data = ka.turnleft_gait()
    # elif action_command == 'd':
    #     rate, gait_np_data = ka.turnright_gait()
    # elif action_command == 'j':
    #     rate, gait_np_data = ka.jump_gait()
    # elif action_command == 'c':
    #     rate, gait_np_data = ka.clam_gait()
    # elif action_command == 'q':
    #     rate, gait_np_data = ka.slantleft_gait()
    # elif action_command == 'e':
    #     rate, gait_np_data = ka.slantright_gait()
    return rate, gait_np_data


if __name__ == '__main__':
    try:
        # Initialize the node and define the Publisher.
        rospy.init_node('pos_pub_node', anonymous=True)
        LF_HAA_pos_pub = rospy.Publisher('/quadruped/LF_HAA_position_controller/command', Float64, queue_size=10)
        LH_HAA_pos_pub = rospy.Publisher('/quadruped/LH_HAA_position_controller/command', Float64, queue_size=10)
        RF_HAA_pos_pub = rospy.Publisher('/quadruped/RF_HAA_position_controller/command', Float64, queue_size=10)
        RH_HAA_pos_pub = rospy.Publisher('/quadruped/RH_HAA_position_controller/command', Float64, queue_size=10)
        LF_HFE_pos_pub = rospy.Publisher('/quadruped/LF_HFE_position_controller/command', Float64, queue_size=10)
        LH_HFE_pos_pub = rospy.Publisher('/quadruped/LH_HFE_position_controller/command', Float64, queue_size=10)
        RF_HFE_pos_pub = rospy.Publisher('/quadruped/RF_HFE_position_controller/command', Float64, queue_size=10)
        RH_HFE_pos_pub = rospy.Publisher('/quadruped/RH_HFE_position_controller/command', Float64, queue_size=10)
        LF_KFE_pos_pub = rospy.Publisher('/quadruped/LF_KFE_position_controller/command', Float64, queue_size=10)
        LH_KFE_pos_pub = rospy.Publisher('/quadruped/LH_KFE_position_controller/command', Float64, queue_size=10)
        RF_KFE_pos_pub = rospy.Publisher('/quadruped/RF_KFE_position_controller/command', Float64, queue_size=10)
        RH_KFE_pos_pub = rospy.Publisher('/quadruped/RH_KFE_position_controller/command', Float64, queue_size=10)
        while not rospy.is_shutdown():
            # Read action command.
            action_command = rospy.get_param('/quadruped/action_state_param', 'k') 

            # Analyze the action command and do gait planning. Note that the gait data returned here is a numpy array.
            rate, gait_np_data = command_analysis(action_command)

            # Calculate the pause time for each step of publish to make the total publish frequency equal to the "rate" in gait planning.
            # Note that a total publish contains 40 steps of publish. (Number of nodes in the gait planning)
            data_length = gait_np_data.shape[0]
            pause = rospy.Rate(data_length * rate)
            
            # Assign the gait data to gait_data and publish.
            gait_data = Float32MultiArray() # Define the gait data as std_msgs.msg data because it is to be published to the topic.
            gait_data.data = gait_np_data
            action_pub(gait_data, data_length)

    except rospy.ROSInterruptException:
        pass

    

