<img width="1786" height="907" alt="image" src="https://github.com/user-attachments/assets/1e7cd7da-ce22-4d50-b27b-2bbdd0a01d03" /># Autonomous Mobile Robot (AMR) Project

This project documents the development of an Autonomous Mobile Robot (AMR) powered by a Raspberry Pi 5. The robot utilizes ROS 2 (Humble) running within a Docker container to manage sensor processing, control, and autonomous navigation.

## Key Features
*   **ROS 2 Humble Environment**: Containerized setup for portability and consistency.
*   **Autonomous Navigation**: Leverages the Nav2 stack for mapping and navigation.
*   **Sensor Integration**: 2D Lidar (RPLidar A1M8-R5) and BNO085 IMU for SLAM and localization.
*   **Differential Drive**: Driven by two 12V DC motors with encoders.

## Hardware Components
*   **Processor**: Raspberry Pi 5
*   **Sensor**: RPLidar A1M8-R5 (2D Lidar)
*   **IMU**: BNO085
*   **Actuation**: 2x 12V DC motors with encoders
*   **Motor Driver**: MDD10A (Dual-channel)
*   **Power**: 13.5V Battery with dual HCW-P715 Buck Converters
*   **Connectivity**: USB Hub for peripheral communication

## Software & Setup
The system runs on **Ubuntu 24.04** with **ROS 2 Humble**.
The project utilizes a custom Docker workflow for ROS 2.

1.  **Build the Container**:
    Navigate to the `rpi_ws` workspace and run:
    ```bash
    ./ros2custombuild.sh
    ```

2.  **Run the Container**:
    Use the provided script to launch the container with necessary hardware access (privileged mode, host networking, and device mapping):
    ```bash
    ./ros2customrun.sh
    ```

## Robot Specifications
*   **Wheel Separation**: 31.0 cm
*   **Wheel Diameter**: 7.0 cm
