import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69c19b80765e0a0204792cc8",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c19b80765e0a0204792cc8",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":"69cc396be11aa3855791fe60","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":1,"limit.max_effort":50,"limit.effort_step":0.5,"limit.max_velocity":180,"limit.velocity_step":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19b99765e0a0204792cdf","source_node_id":"69c199d9765e0a0204792a52","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20cb893e4107be6a97bdf","target_node_id":"69c199d9765e0a0204792a52","source_pin_id":"state","target_pin_id":"joint_states"}]')),
            }
        ),
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69c19b6c765e0a0204792cba",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c19b6c765e0a0204792cba",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":"69cc3963e11aa3855791fdc8","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":1,"limit.max_effort":50,"limit.effort_step":0.5,"limit.max_velocity":180,"limit.velocity_step":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19b9e765e0a0204792ce5","source_node_id":"69c199d9765e0a0204792a52","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20d0793e4107be6a97bec","target_node_id":"69c199d9765e0a0204792a52","source_pin_id":"state","target_pin_id":"joint_states"}]')),
            }
        ),
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69c19b6f765e0a0204792cbf",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c19b6f765e0a0204792cbf",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":"69cc3967e11aa3855791fe14","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":1,"limit.max_effort":50,"limit.effort_step":0.5,"limit.max_velocity":180,"limit.velocity_step":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19b9a765e0a0204792ce2","source_node_id":"69c199d9765e0a0204792a52","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20d0093e4107be6a97be8","target_node_id":"69c199d9765e0a0204792a52","source_pin_id":"state","target_pin_id":"joint_states"}]')),
            }
        ),
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69c19b6a765e0a0204792cb5",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c19b6a765e0a0204792cb5",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":"69cc395de11aa3855791fd60","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":1,"limit.max_effort":50,"limit.effort_step":0.5,"limit.max_velocity":180,"limit.velocity_step":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19ba0765e0a0204792ce8","source_node_id":"69c199d9765e0a0204792a52","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20d0e93e4107be6a97bef","target_node_id":"69c199d9765e0a0204792a52","source_pin_id":"state","target_pin_id":"joint_states"}]')),
            }
        ),
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69c19b85765e0a0204792cce",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c19b85765e0a0204792cce",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":"69cc3970e11aa3855791feac","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":1,"limit.max_effort":50,"limit.effort_step":0.5,"limit.max_velocity":180,"limit.velocity_step":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19b97765e0a0204792cdc","source_node_id":"69c199d9765e0a0204792a52","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20cdf93e4107be6a97be5","target_node_id":"69c199d9765e0a0204792a52","source_pin_id":"state","target_pin_id":"joint_states"}]')),
            }
        ),
        Node(
            package="odrive_s1",
            executable="odrive_s1_node",
            name="odrive_s1_n69c19b8e765e0a0204792cd5",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c19b8e765e0a0204792cd5",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"joint_id":"69cc3973e11aa3855791fef8","transport":"can","units":"radians","gear_ratio":1,"smoothing_alpha":0,"can.node_id":0,"can.interface":"socketcan","can.channel":"can0","can.bitrate":1000000,"can.poll_hz":50,"can.request_iq":false,"can.heartbeat_timeout_s":2,"can.enable_closed_loop_on_start":true,"can.torque_constant":0,"limit.lower_position":-180,"limit.upper_position":180,"limit.position_step":1,"limit.max_effort":50,"limit.effort_step":0.5,"limit.max_velocity":180,"limit.velocity_step":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69b5b247145f6cae225f9da5:state","name":"state","direction":"output","msg_type":"sensor_msgs/JointState"},{"pin_id":"69b5b247145f6cae225f9da5:trajectory","name":"trajectory","direction":"input","msg_type":"trajectory_msgs/JointTrajectoryPoint"},{"pin_id":"69b5b247145f6cae225f9da5:mode","name":"mode","direction":"input","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19b95765e0a0204792cd9","source_node_id":"69c199d9765e0a0204792a52","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20cd393e4107be6a97be2","target_node_id":"69c199d9765e0a0204792a52","source_pin_id":"state","target_pin_id":"joint_states"}]')),
            }
        ),
        Node(
            package="inverse_kinematics",
            executable="inverse_kinematics_node",
            name="inverse_kinematics_n69c199d9765e0a0204792a52",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69c199d9765e0a0204792a52",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"root_component_id":"69cc395de11aa3855791fd61","end_effector_component_id":"69cc3978e11aa3855791ff43","components":[],"joints":[],"max_iterations":100,"tolerance":0.001,"damping":0.01}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69be1505ff9537f4b6bbf473:target_pose","name":"target_pose","direction":"input","msg_type":"geometry_msgs/Pose"},{"pin_id":"69be1505ff9537f4b6bbf473:joint_states","name":"joint_states","direction":"input","msg_type":"sensor_msgs/JointState[]"},{"pin_id":"69be1505ff9537f4b6bbf473:joint_commands","name":"joint_commands","direction":"output","msg_type":"trajectory_msgs/JointTrajectoryPoint[]"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c20cb893e4107be6a97bdf","source_node_id":"69c19b80765e0a0204792cc8","source_pin_id":"state","target_pin_id":"joint_states"},{"connection_id":"69c20cd393e4107be6a97be2","source_node_id":"69c19b8e765e0a0204792cd5","source_pin_id":"state","target_pin_id":"joint_states"},{"connection_id":"69c20cdf93e4107be6a97be5","source_node_id":"69c19b85765e0a0204792cce","source_pin_id":"state","target_pin_id":"joint_states"},{"connection_id":"69c20d0093e4107be6a97be8","source_node_id":"69c19b6f765e0a0204792cbf","source_pin_id":"state","target_pin_id":"joint_states"},{"connection_id":"69c20d0793e4107be6a97bec","source_node_id":"69c19b6c765e0a0204792cba","source_pin_id":"state","target_pin_id":"joint_states"},{"connection_id":"69c20d0e93e4107be6a97bef","source_node_id":"69c19b6a765e0a0204792cb5","source_pin_id":"state","target_pin_id":"joint_states"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69c19b95765e0a0204792cd9","target_node_id":"69c19b8e765e0a0204792cd5","source_pin_id":"joint_commands","target_pin_id":"trajectory"},{"connection_id":"69c19b97765e0a0204792cdc","target_node_id":"69c19b85765e0a0204792cce","source_pin_id":"joint_commands","target_pin_id":"trajectory"},{"connection_id":"69c19b99765e0a0204792cdf","target_node_id":"69c19b80765e0a0204792cc8","source_pin_id":"joint_commands","target_pin_id":"trajectory"},{"connection_id":"69c19b9a765e0a0204792ce2","target_node_id":"69c19b6f765e0a0204792cbf","source_pin_id":"joint_commands","target_pin_id":"trajectory"},{"connection_id":"69c19b9e765e0a0204792ce5","target_node_id":"69c19b6c765e0a0204792cba","source_pin_id":"joint_commands","target_pin_id":"trajectory"},{"connection_id":"69c19ba0765e0a0204792ce8","target_node_id":"69c19b6a765e0a0204792cb5","source_pin_id":"joint_commands","target_pin_id":"trajectory"}]')),
            }
        ),
        Node(
            package="camera",
            executable="camera_node",
            name="camera_n69ceaaab99bf1d9ff1aa02d2",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69ceaaab99bf1d9ff1aa02d2",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"camera_id":"camera_0","device_index":0,"width":640,"height":480,"fps":30}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":30,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e728cd15153dec61d816:capture","name":"capture","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3e728cd15153dec61d816:frame","name":"frame","direction":"output","msg_type":"polyflow_msgs/CameraFrame"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
    ])