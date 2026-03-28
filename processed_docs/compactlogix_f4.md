## 1769 CompactLogix Controllers User Manual

Catalog Numbers 1769-L31, 1769-L32C, 1769-L32E, 1769-L35CR, 1769-L35E

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Important User Information

Solid-state equipment has operational characteristics differing from those of electromechanical equipment. Safety Guidelines for the Application, Installation and Maintenance of Solid State Controls (publication SGI-1.1 available from your local Rockwell Automation sales office or online at http://www.rockwellautomation.com/literature/) describes some important differences between solid-state equipment and hard-wired electromechanical devices. Because of this difference, and also because of the wide variety of uses for solid-state equipment, all persons responsible for applying this equipment must satisfy themselves that each intended application of this equipment is acceptable.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

<!-- image -->

<!-- image -->

## IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

Identifies information that is critical for successful application and understanding of the product.

Allen-Bradley, Rockwell Automation, Rockwell Software, CompactLogix, ControlFLASH, Logix5000, RSLinx, RSLogix, PanelView, PhaseManager, ControlLogix, PanelView, Ultra, PowerFlex, FlexLogix, PLC-5, DriveLogix, SLC, MicroLogix, and TechConnect are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

## New and Updated Information

This manual contains new and updated information. Changes throughout this revision are marked by change bars, as shown to the right of this paragraph.

This table contains the changes made to this revision.

| Topic                                    |   Page |
|------------------------------------------|--------|
| Updated the Verify Compatibility section |     18 |

## Notes:

| Preface                           | Additional Resources . . . .  . . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . . . 9   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
|                                   | Chapter 1                                                                                                          |                                               |
| 1769 CompactLogix Controllers     | About the 1769 CompactLogix Controller . . . . . . . . . . . . . . . . . . . . . . . . . 11                        |                                               |
| Overview                          | Design a CompactLogix System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13              |                                               |
|                                   | Chapter 2                                                                                                          |                                               |
| Install the 1769-L3x Controllers  | Verify Compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18  |                                               |
|                                   | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . . 19    |
|                                   | Parts List . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . . . . 19    |
|                                   | Set the Node Address (ControlNet only) . . . . . . . . . . . . . . . . . . . . . . . . . . 19                      |                                               |
|                                   | Connect the 1769-BA Battery. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20            |                                               |
|                                   | Install a CompactFlash Card (optional) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                  |                                               |
|                                   | Assemble the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22   |                                               |
|                                   | Mount the System. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 |                                               |
|                                   | Minimum Spacing. . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . 23              |
|                                   | Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24  |                                               |
|                                   | Ground the Wiring. . . . . . . . .  . . . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . 24            |
|                                   | Mount the Panel . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . 25            |
|                                   | Mount the Controller on the DIN Rail . . . . . . . . . . . . . . . . . . . . . . . . 25                            |                                               |
|                                   | Make RS-232 Connections to the Controller. . . . . . . . . . . . . . . . . . . . . . . 26                          |                                               |
|                                   | RS-232 Cable . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . 26            |
|                                   | Optical Isolator (1769-L31 only)  . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . 27                |
|                                   | Default Serial Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                |                                               |
|                                   | Using the Channel 0 Default Communication Push Button . . . . . 28                                                 |                                               |
|                                   | Make Ethernet Connections to the Controller . . . . . . . . . . . . . . . . . . . . . 28                           |                                               |
|                                   | Assign an IP Address. . . . . . . .  . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 29            |
|                                   | Make ControlNet Connections to the Controller . . . . . . . . . . . . . . . . . . 32                               |                                               |
|                                   | Connect the Controller to the Network via a ControlNet Tap . . . 33                                                |                                               |
|                                   | Load the Controller Firmware . . .  . . . . . . . . . . . . . . . . . .                                            |                                               |
|                                   | Install the Appropriate EDS Files. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36            |                                               |
|                                   |                                                                                                                    | . . . . . . . . . . . . . . . 36              |
|                                   | Use the ControlFLASH Utility to Load Firmware . . . . . . . . . . . . . . 37                                       |                                               |
|                                   | Use AutoFlash to Load Firmware . . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . . 37                |
|                                   | Use a CompactFlash Card to Load Firmware . . . . . . . . . . . . . . . . . . . 38                                  |                                               |
|                                   | Select the Controller’s Operating Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . 39                   |                                               |
|                                   | Chapter 3                                                                                                          |                                               |
| Connect to the Controller via the | Connect to the Controller via the Serial Port . . . . . . . . . . . . . . . . . . . . . . . 41                     |                                               |
| Serial Port                       | Configure the Serial Driver  . . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . . 43        |
|                                   | Select the Controller Path . . . . .  . . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . 45            |

Controller Options. . . . . . . . . .

. . . . . . . . . . . . . . . . . .

Chapter 4

| Communicate over Networks         | EtherNet/IP Network Communication . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                       |                                            |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
|                                   | Connections over an EtherNet/IP Network . . . . . . . . . . . . . . . . . . . . 49                                 |                                            |
|                                   | ControlNet Network Communication. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                       |                                            |
|                                   | Connections over ControlNet Network . . . . . . . . . . . . . . . . . . . . . . . . 52                             |                                            |
|                                   | DeviceNet Communication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53           |                                            |
|                                   | Serial Communication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55    |                                            |
|                                   | Configure an Isolator . . . . . . .  . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 57         |
|                                   | Communicate with DF1 Devices . .  . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . 59               |
|                                   | DF1 Radio Modem Support . . . . .  . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . 61             |
|                                   | Modbus Support . . . . . .  . . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . . 67     |
|                                   | Broadcast Messages over a Serial Port . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                     |                                            |
|                                   | DH-485 Network Communication. .  . . . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . . 72             |
|                                   | Chapter 5                                                                                                          |                                            |
| Manage Controller Communication   | Produce and Consume Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75           |                                            |
|                                   | Send and Receive Messages .  . . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . . 76     |
|                                   | Determine Whether to Cache Message Connections . . . . . . . . . . . . 77                                          |                                            |
|                                   | Connections . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . . . . 77 |
|                                   | Calculate Total Connections .  . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . 78       |
|                                   | Connections Example . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . . 79         |
|                                   | Chapter 6                                                                                                          |                                            |
| Place, Configure, and Monitor I/O | Select I/O Modules. .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . 81               |
|                                   | Validate I/O Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 |                                            |
|                                   | Estimate Requested Packet Interval   . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . 82               |
|                                   | Calculate System Power Consumption . . . . . . . . . . . . . . . . . . . . . . . . . 83                            |                                            |
|                                   | Validate Placement of I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83                       |                                            |
|                                   | Place Local I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86      |                                            |
|                                   | Configure I/O . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . 87     |
|                                   | I/O Connections . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . 88         |
|                                   | Configure Distributed I/O on an EtherNet/IP Network . . . . . . . . . . . . 88                                     |                                            |
|                                   | Configure Distributed I/O on a ControlNet Network . . . . . . . . . . . . . . 89                                   |                                            |
|                                   | Configure Distributed I/O on a DeviceNet Network. . . . . . . . . . . . . . . . 90                                 |                                            |
|                                   | Address I/O Data . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . . 91 |
|                                   | Determine When Data Is Updated .  . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . 92             |
|                                   | Monitor I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93     |                                            |
|                                   | Display Fault Data . . . . .  . . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . . . 93     |
|                                   | End-cap Detection and Module Faults. . . . . . . . . . . . . . . . . . . . . . . . . . 94                          |                                            |
|                                   | Reconfigure an I/O Module . . . . .  . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 94         |
|                                   | Reconfigure a Module via RSLogix 5000 Programming Software . 94                                                    |                                            |
|                                   | Reconfigure a Module via a MSG Instruction . . . . . . . . . . . . . . . . . . . 95                                |                                            |

Chapter 7

| Develop Applications                                                  | Manage Tasks. . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . 97    |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
|                                                                       | Develop Programs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 |                                           |
|                                                                       | Define Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99  |                                           |
|                                                                       | Define Programs . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 101       |
|                                                                       | Define Routines . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . 101       |
|                                                                       | Sample Controller Projects . . .  . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . 102         |
|                                                                       | Organize Tags . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . 103     |
|                                                                       | Select a Programming Language . . .  . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . 104           |
|                                                                       | Add-on Instructions . . . . . . . .  . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . 105         |
|                                                                       | Monitor Connections . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . 107       |
|                                                                       | Determine if Device Communication Has Timed Out . . . . . . . . . 107                                              |                                           |
|                                                                       | Determine if I/O Module Communication Has Timed Out . . . . 108                                                    |                                           |
|                                                                       | Interrupt the Execution of Logic and Execute the Fault Handler 109                                                 |                                           |
|                                                                       | Select a System Overhead Time Slice Percentage . . . . . . . . . . . . . . . . . . . 109                           |                                           |
|                                                                       | Chapter 8                                                                                                          |                                           |
| Configure PhaseManager Application PhaseManager Overview. . . . . . . | . . . . . . . . . . . . . . . . . .                                                                                | . . . . . . . . . . . . . . . . 113       |
|                                                                       | State Model Overview . .  . . . . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . . . . . 114 |
|                                                                       | How Equipment Changes States. .  . . . . . . . . . . . . . . .                                                     | . . . . . . . . . . . . . 116             |
|                                                                       | Manually Change States . . . . .  . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . 117         |
|                                                                       | Compare PhaseManager to Other State Models . . . . . . . . . . . . . . . . . . . 117                               |                                           |
|                                                                       | Minimum System Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118                  |                                           |
|                                                                       | Equipment Phase Instructions . . .  . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . 118         |
|                                                                       | Chapter 9                                                                                                          |                                           |
| Use a CompactFlash Card                                               | Locate the Controller Serial Number in RSLinx Software . . . . . . . 119                                           |                                           |
|                                                                       | Locate the Controller Serial Number. . . . . . . . . . . . . . . . . . . . . . . . . . 121                         |                                           |
|                                                                       | Use a CompactFlash Card to Load/Store a User Application . . . . . . . 122                                         |                                           |
|                                                                       | Manually Change Which Project Loads . . . . . . . . . . . . . . . . . . . . . . . 122                              |                                           |
|                                                                       | Manually Change the Load Parameters. . . . . . . . . . . . . . . . . . . . . . . . 124                             |                                           |
|                                                                       | Use a CompactFlash Card for Data Storage . . . . . . . . . . . . . . . . . . . . . . . 125                         |                                           |
|                                                                       | Read and Write User Data to the CompactFlash Card . . . . . . . . . . . . . 125                                    |                                           |
|                                                                       | Chapter 10                                                                                                         |                                           |
| Maintain the Battery                                                  | Battery Handling . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . 127     |
|                                                                       | Check If the Battery Is Low . . . .  . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 128       |
|                                                                       | Estimate 1769-BA Battery Life . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128            |                                           |
|                                                                       | Store Lithium Batteries . .  . . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . . . 129 |
|                                                                       | Battery Removal . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . . 129 |
|                                                                       | Additional Resources . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 130     |

Appendix A

| Status Indicators            | 1769-L3xx Controllers Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . 131                |                                           |
|------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------|
|                              | CompactFlash Indicator . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 133 |                                           |
|                              | RS-232 Serial Port Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133           |                                           |
|                              | ControlNet Indicators . . . . . . . .  . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . 133     |
|                              | Module Status (MS) Indicator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134               |                                           |
|                              | Network Channel Indicators . . .  . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . 135           |
|                              | EtherNet/IP Indicators . . .  . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . . 135 |
|                              | Module Status (MS) Indicator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135               |                                           |
|                              | Network Status (NS) Indicator  . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . 136         |
|                              | Link Status (LNK) Indicator . . . . . . . . . .  . . . . . . . . . . . .                                       | . . . . . . . . . . . 136                 |
|                              | Appendix B                                                                                                     |                                           |
| Dynamic Memory Allocation in | Messages. . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . . . 138 |
| CompactLogix Controllers     | RSLinx Tag Optimization.  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . . . 138 |
|                              | Trends . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . 139 |
|                              | DDE/OPC Topics . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . 139     |
|                              | Specify Connections per PLC Controller . . . . . . . . . . . . . . . . . . . . . . 139                         |                                           |
|                              | Number of Connections Needed to Optimize Throughput . . . . . 141                                              |                                           |
|                              | View the Number of Open Connections. . . . . . . . . . . . . . . . . . . . . . . 141                           |                                           |
| Index                        |                                                                                                                |                                           |

## Additional Resources

Use this manual to become familiar with the CompactLogix™ controller and its features.

This manual describes the necessary tasks to install, configure, program, and operate a CompactLogix system. In some cases, this manual includes references to additional documentation that provides the more comprehensive details.

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                              | Description                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1769 CompactLogix Controllers Specifications Technical Data, publication 1769-TD005                   | Contains technical specifications and certifications for all CompactLogix controllers.                                                                                                                     |
| 1769-L3x CompactLogix System Quick Start, publication IASIMP-QS001                                    | Provides examples of using a 1769-L3x CompactLogix controller to connect to multiple devices over various networks.                                                                                        |
| Logix5000 Controller Design Considerations Reference Manual, publication 1756-RM094                   | Provides guidelines you can follow to optimize your system. This manual also provides system information you need to make system design choices.                                                           |
| Logix5000 Controllers Common Procedures Manual, publication 1756-PM001                                | Guides the development of projects for Logix5000™ controllers. It provides links to individual guides.                                                                                                     |
| Logix5000 Controllers General Instruction Set Reference Manual, publication 1756-RM003                | Provides a programmer with details about each available instruction for a Logix5000 controller. You should already be familiar with how the Logix5000 controller stores and processes data.                |
| Logix5000 Controllers Process Control/Drives Instruction Set Reference Manual, publication 1756-RM006 | Provides a programmer with details about each function block instruction available for a Logix5000 controller. You should already be familiar with how the Logix5000 controller stores and processes data. |
| EtherNet/IP Modules in Logix5000 Control Systems User Manual, publication ENET-UM001                  | Describes how to install and configure EtherNet/IP modules in Logix5000 control systems.                                                                                                                   |
| ControlNet Communication Modules in Logix5000 Control Systems User Manual, publication CNET-UM001     | Describes how to install and configure ControlNet modules in a Logix5000 control system.                                                                                                                   |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                           | Provides general guidelines for installing a Rockwell Automation® industrial system.                                                                                                                       |
| Product Certifications website, http://www.ab.com                                                     | Provides declarations of conformity, certificates, and other certification details.                                                                                                                        |

You can view or download publications at http:/www.rockwellautomation.com/literature/. To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

## Notes:

## About the 1769 CompactLogix Controller

<!-- image -->

## 1769 CompactLogix Controllers Overview

This chapter introduces the 1769 CompactLogix controllers. These controllers offer state-of-the-art control, communication, and I/O elements in a distributed control package.

The 1769 CompactLogix controller offers state-of-the-art control, communication, and I/O elements in a distributed control package.

Figure 1 - CompactLogix Controller and 1769 I/O Modules

<!-- image -->

For a more flexible system, use:

- multiple controllers in a single chassis.
- multiple controllers joined across networks.
- I/O in multiple platforms that is distributed in many locations and connected over multiple I/O links.

Figure 2 - CompactLogix System Overview

<!-- image -->

The CompactLogix controller, part of the Logix family of controllers, provides a small, powerful, cost-effective system consisting of the following:

- RSLogix™ 5000 programming software
- Built-in communication ports for EtherNet/IP (1769-L32E and 1769L35E only) and ControlNet (1769-L32C and 1769-L35CR only) networks
- A 1769-SDN communication interface module providing I/O control and remote device configuration over DeviceNet
- A built-in serial port on every CompactLogix controller
- Compact I/O modules providing a compact, DIN-rail or panel-mounted I/O system

Table 1 - CompactLogix Controller Combinations

|                   |        | Controller Available Memory Communication Options                                            | Number of Tasks Supported   | Number of Local I/O Modules Supported   |
|-------------------|--------|----------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------|
| 1769-L35CR 1.5 MB |        | 1 port ControlNet - supports redundant media 1 port RS-232 serial (system or user protocols) |                             | 8 30                                    |
| 1769-L35E         |        | 1 port EtherNet/IP 1 port RS-232 serial (system or user protocols)                           |                             | 8 30                                    |
| 1769-L32C 750 KB  |        | 1 port ControlNet 1 port RS-232 serial (system or user protocols)                            |                             | 6 16                                    |
| 1769-L32E         |        | 1 port EtherNet/IP 1 port RS-232 serial (system or user protocols)                           |                             | 6 16                                    |
| 1769-L31          | 512 KB | 1 port RS-232 serial (system or user protocols) 1 port RS-232 serial (system protocol only)  | 4                           | 6 16                                    |

## Design a CompactLogix System

When designing a CompactLogix system, determine the network configuration and the placement of components in each location. To design your CompactLogix system, you must select the following:

- I/O devices
- A communication network
- Controllers
- Power supplies
- Software

## Notes:

## Install the 1769-L3x Controllers

| Topic                                         |   Page |
|-----------------------------------------------|--------|
| Verify Compatibility                          |     18 |
| Before You Begin                              |     19 |
| Set the Node Address (ControlNet only)        |     19 |
| Connect the 1769-BA Battery                   |     20 |
| Install a CompactFlash Card (optional)        |     21 |
| Assemble the System                           |     22 |
| Mount the System                              |     23 |
| Make RS-232 Connections to the Controller     |     26 |
| Make Ethernet Connections to the Controller   |     28 |
| Make ControlNet Connections to the Controller |     32 |
| Install the Appropriate EDS Files             |     36 |
| Load the Controller Firmware                  |     36 |
| Select the Controller’s Operating Mode        |     39 |

Use this chapter to install the CompactLogix™ controller, which must be the leftmost module in the first bank of the system.

<!-- image -->

<!-- image -->

<!-- image -->

WARNING: This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC publication 60664-1), at altitudes up to 2000 meters (6562 ft) without derating.

This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR Publication 11. Without appropriate precautions, there may be potential difficulties ensuring electromagnetic compatibility in other environments due to conducted as well as radiated disturbance.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA, V2, V1, V0 (or equivalent) if non-metallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, Allen-Bradley® publication 1770-4.1, for additional installation requirements
- NEMA 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by different types of enclosure

WARNING: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

<!-- image -->

Table 3 - European Hazardous Location Approval

<!-- image -->

Table 2 - North American Hazardous Location Approval

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time | Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time                      | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | WARNING: Explosion Hazard - •  Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. •  Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. •  Substitution of components may impair suitability for Class I, Division 2. •  If this product contains batteries, they must only be changed in an area known to be nonhazardous. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | AVERTISSEMENT: Risque d’Explosion – •  Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement. •  Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit. •  La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2. •  S'assurer que l'environnement est classé non dangereux avant de changer les piles.                                    |

## European Zone 2 Certification (The following applies when the product bears the Ex or EEx Marking)

This equipment is intended for use in potentially explosive atmospheres as defined by European Union Directive 94/9/EC and has been found to comply with the Essential Health and Safety Requirements relating to the design and construction of Category 3 equipment intended for use in potentially explosive atmospheres, given in Annex II to this Directive.

Compliance with the Essential Health and Safety Requirements has been assured by compliance with EN 60079-15 and EN 60079-0.

## Verify Compatibility

<!-- image -->

<!-- image -->

## IMPORTANT

## WARNING:

- This equipment must be installed in an enclosure providing at least IP54 protection when applied in Zone 2 environments.
- This equipment shall be used within its specified ratings defined by Allen-Bradley.
- Provisions shall be made to prevent the rated voltage from being exceeded by transient disturbances of more than 40% when applied in Zone 2 environments.
- Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.

ATTENTION: This equipment is not resistant to sunlight or other sources of UV radiation.

The series B controllers are compatible only with the controller firmware and the RSLogix 5000 software versions as indicated in the table below.

Attempting to use controllers with incompatible software and firmware revisions can result in the following:

- An inability to connect to the series B controller in RSLogix 5000 software
- Unsuccessful firmware upgrades in ControlFLASH ™ ™ or AutoFlash utilities

This table shows the compatible pairs of RSLogix 5000 software versions and controller firmware revisions.

| Controller                                            | RSLogix 5000 Software Version or Later Controller Firmware Revision or Later   |        |
|-------------------------------------------------------|--------------------------------------------------------------------------------|--------|
| 1769-L31, 1769-L32C, 1769-L32E, 1769-L35CR, 1769-L35E | 16.00.00                                                                       | 16.023 |
| 1769-L31, 1769-L32C, 1769-L32E, 1769-L35CR, 1769-L35E | 17.01.02                                                                       | 17.012 |
| 1769-L31, 1769-L32C, 1769-L32E, 1769-L35CR, 1769-L35E | 19.01.00                                                                       | 19.015 |
| 1769-L31, 1769-L32C, 1769-L32E, 1769-L35CR, 1769-L35E | 20.01.00                                                                       | 20.013 |

## Before You Begin

Consider the following when planning your CompactLogix system:

- The CompactLogix controller is always the leftmost module in the system.
- The controller must be within four modules of the system power supply. Some I/O modules may be up to eight modules away from the power supply. See the documentation for your 1769 I/O modules for details.
- The 1769-L32E controller supports as many as 16 I/O modules and the 1769-L35E controller supports as many as 30 I/O modules. Both controllers can use a maximum of 3 I/O banks with 2 expansion cables.
- Each I/O bank requires its own power supply.
- Only one controller can be used in a CompactLogix system.
- A 1769-ECR right end cap or 1769-ECL left end cap is required to terminate the end of the communication bus.

## Parts List

These components are shipped with the controller.

<!-- image -->

<!-- image -->

| Component   | Description            |
|-------------|------------------------|
|             | 1769-BA battery        |
|             | 1747-KY controller key |

You may also use these components with the controller.

| If you want to                           | Then use this component                                                                                                                                                                                                            |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connect a device to the RS-232 port      | 1756-CP3 or 1747-CP3 serial cable                                                                                                                                                                                                  |
| Add nonvolatile memory                   | 1784-CF128 Industrial CompactFlash card                                                                                                                                                                                            |
| Connect a device to the EtherNet/IP port | Standard Ethernet cable with RJ-45 connector                                                                                                                                                                                       |
| Connect a device to the ControlNet port  | •  ControlNet taps for connections from controller channels A or B to the ControlNet network •  1786-CP cable for connections from a programming terminal to the ControlNet network via the controller’s network access port (NAP) |

## Set the Node Address (ControlNet only)

Every ControlNet network requires at least one module that can store parameters and configure the network with those parameters upon startup. The CompactLogix controller is called a keeper because it keeps the network configuration.

The CompactLogix controller can keep the network parameters at any legal node address (01…99). Multiple devices on any one network can act as the network keepers. Each device capable of being the network keeper acts to back up the current keeper. This back-up function is automatic and requires no action on your part.

Node address switches are set to the 99 position at shipment, as shown in the figure.

<!-- image -->

<!-- image -->

Use these steps to set the node address.

1. Slide the side cover forward.

<!-- image -->

43860

2. Use a small screwdriver to set the node address via the controller switches.
3. Write the node address on the front panel overlay after setting the node address switches.

<!-- image -->

Connect the 1769-BA Battery The controller is shipped with the 1769-BA battery that is packed separately. To
hbfllhid connect the battery, follow this procedure.

<!-- image -->

ATTENTION: The 1769-BA battery is the only battery you can use with the 1769-L32E and 1769-L35E controllers. The 1747-BA battery is not compatible with the 1769-L32E and 1769-L35E controllers and may cause problems.

43868

## Install a CompactFlash Card (optional)

<!-- image -->

WARNING: When you connect or disconnect the battery, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

For safety information on the handling of lithium batteries, including handling and disposal of leaking batteries, see Guidelines for Handling Lithium Batteries Technical Data, publication AG-5.4NOV04 .

1. Remove the battery door by sliding it forward.

<!-- image -->

Do not remove the plastic insulation covering the battery. The insulation is necessary to protect the battery contacts.

## IMPORTANT

1. Insert the battery connector into the connector port.

The connector is keyed to be installed with the correct polarity.

2. Insert the battery into the battery port in the battery door.
3. Slide the battery door back until it clicks into position.

<!-- image -->

At the end of its life, the used battery should be collected separately from any unsorted municipal

- TIP waste and recycled.

<!-- image -->

<!-- image -->

ATTENTION: Do not remove the CompactFlash card while the controller is reading from or writing to the card, as indicated by a flashing green CF status indicator. This could corrupt the data on the card or in the controller, as well as corrupt the latest firmware in the controller.

## Assemble the System

The optional industrial CompactFlash card provides nonvolatile memory for a CompactLogix controller. The card is not required for controller operation.

<!-- image -->

WARNING: When you insert or remove the CompactFlash card while power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

To install a CompactFlash card, push the locking tab to the right and insert the industrial CompactFlash card into the socket on the front of the controller.

The label of the CompactFlash card faces toward the left. Match the orientation arrow on the card with the arrow on the front of the controller.

To remove the CompactFlash card, push the locking tab away from the CompactFlash card and pull the CompactFlash card from the socket.

<!-- image -->

The controller can be attached to an adjacent I/O module or power supply before or after mounting.

<!-- image -->

WARNING: The CompactLogix controller is not designed for removal and insertion under power.

If you insert or remove the module while backplane power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

Refer to the illustration when installing a controller.

<!-- image -->

1. Disconnect line power.
2. Check that the lever of the adjacent module (A) is in the unlocked (fully right) position.

## Mount the System

3. Use the upper and lower tongue-and-groove slots (B) to secure the modules together.
4. Move the module back along the tongue-and-groove slots until the bus connectors line up with each other.
5. Use your fingers or a small screwdriver to push the module's bus lever back slightly to clear the positioning tab (C).
6. Move the module's bus lever fully to the left (D) until it clicks, being sure it is locked firmly in place.

<!-- image -->

ATTENTION: When attaching the controller, power supply, and I/O modules, make sure the bus connectors are securely locked together to be sure of proper electrical connection.

This equipment is not resistant to sunlight or other sources of UV radiation.

7. Attach an end-cap terminator (E) to the last module in the system by using the tongue-and-groove slots as before.
8. Lock the end-cap bus terminator (F).

<!-- image -->

ATTENTION: During panel or DIN-rail mounting of all devices, be sure that all debris (such as metal chips or wire strands) is kept from falling into the controller. Debris that falls into the controller could cause damage while the controller is energized.

## Minimum Spacing

Maintain spacing from enclosure walls, wireways, and adjacent equipment. Allow 50 mm (2 in.) of space on all sides, as shown. This provides ventilation and electrical isolation.

<!-- image -->

## Dimensions

<!-- image -->

All dimensions are in mm (in.).

## IMPORTANT

Compact I/O expansion cables have the same dimensions as the end caps. Expansion cables can be used on either the right or left end. A 1769-ECR right-end cap or 1769-ECL left-end cap terminates the end of the communication bus.

## Ground the Wiring

<!-- image -->

ATTENTION: This product is grounded through the DIN rail to chassis ground. Use zinc-plated yellow-chromate steel DIN rail to assure proper grounding. The use of other DIN rail materials (such as aluminum or plastic) that can corrode, oxidize, or are poor conductors, can result in improper or intermittent grounding. Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.) and use end-anchors appropriately.

This product is intended to be mounted to a well-grounded mounting surface such as a metal panel. Additional grounding connections from the controller's mounting tabs or DIN rail (if used) are not required unless the mounting surface cannot be grounded.

Refer to Allen-Bradley Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional information.

## Mount the Panel

Mount the controller to a panel by using two screws per module. Use M4 or #8 panhead screws. Mounting screws are required on every module. This procedure lets you use the assembled modules as a template for drilling holes in the panel.

## IMPORTANT

Due to module-mounting hole tolerance, it is important to follow these procedures.

1. On a clean work surface, assemble no more than three modules.
2. Using the assembled modules as a template, carefully mark the center of all module-mounting holes on the panel.
3. Return the assembled modules to the clean work surface, including any previously mounted modules.
4. Drill and tap the mounting holes for the recommended M4 or #8 screw.
5. Place the modules back on the panel and check for proper hole alignment.

TIP

The grounding plate, that is, where you install the mounting screws, enables the module to be grounded when it is panel-mounted.

6. Attach the modules to the panel by using the mounting screws.

TIP

If you are mounting more modules, mount only the last one of this group and put the others aside. This reduces remounting time when you are drilling and tapping the next group of modules.

7. Repeat steps 1…6 for any remaining modules.

## Mount the Controller on the DIN Rail

The controller can be mounted on the following DIN rails:

- EN 50 022 - 35 x 7.5 mm (1.38 x 0.30 in.)
- EN 50 022 - 35 x 15 mm (1.38 x 0.59 in.)

<!-- image -->

ATTENTION: This product is grounded through the DIN rail to chassis ground. Use zinc-plated yellow-chromate steel DIN rail to assure proper grounding. The use of other DIN rail materials (for example, aluminum or plastic) that can corrode, oxidize, or are poor conductors, can result in improper or intermittent grounding. Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.) and use end-anchors appropriately.

1. Before mounting the controller on a DIN rail, close the DIN rail latches.
2. Press the DIN-rail mounting area of the controller against the DIN rail. The latches will momentarily open and lock into place.

## Make RS-232 Connections to the Controller

Connect the 9-pin female end of the serial cable to the serial port of the controller.

<!-- image -->

WARNING: If you connect or disconnect the serial cable with power applied to this module or the serial device on the other end of the cable, an electrical arc can occur. This could cause an explosion in hazardous location installations.

<!-- image -->

Be sure that power is removed or the area is nonhazardous before proceeding.

## RS-232 Cable

<!-- image -->

TIP This cable must be shielded and tied to the connector housing.

## Optical Isolator (1769-L31 only)

Channel 0 is fully isolated and does not need a separate isolation device. Channel 1 is nonisolated. If you connect channel 1 to a device outside of the system's enclosure, consider installing an isolator (such as the 1761-NET-AIC interface converter) between the controller and device.

<!-- image -->

## Select the appropriate cable.

| Isolator Use   | Cable                                                                                                                                                                                                                                                                                                                                   | Cable                                                                                                                                                                                                                                                                                                                                   | Cable                                                                                                                                                                                                                                                                                                                                   | Cable                                                                                                                                                                                                                                                                                                                                   | Cable                                                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No             | The 1756-CP3 cable attaches the controller directly to the controller. If you make your own cable, it must be shielded and the shields must be tied to the metal shell surrounding the pins on the ends of the cable. You can also use a 1747-CP3 cable. This cable has a taller right-angle connector housing than the 1756-CP3 cable. | The 1756-CP3 cable attaches the controller directly to the controller. If you make your own cable, it must be shielded and the shields must be tied to the metal shell surrounding the pins on the ends of the cable. You can also use a 1747-CP3 cable. This cable has a taller right-angle connector housing than the 1756-CP3 cable. | The 1756-CP3 cable attaches the controller directly to the controller. If you make your own cable, it must be shielded and the shields must be tied to the metal shell surrounding the pins on the ends of the cable. You can also use a 1747-CP3 cable. This cable has a taller right-angle connector housing than the 1756-CP3 cable. | The 1756-CP3 cable attaches the controller directly to the controller. If you make your own cable, it must be shielded and the shields must be tied to the metal shell surrounding the pins on the ends of the cable. You can also use a 1747-CP3 cable. This cable has a taller right-angle connector housing than the 1756-CP3 cable. | The 1756-CP3 cable attaches the controller directly to the controller. If you make your own cable, it must be shielded and the shields must be tied to the metal shell surrounding the pins on the ends of the cable. You can also use a 1747-CP3 cable. This cable has a taller right-angle connector housing than the 1756-CP3 cable. |
| Yes            | The 1761-CBL-AP00 cable (right-angle connector to controller) or the 1761-CBL-PM02 cable (straight connector to the controller) attaches the controller to port 2 on the 1761-NET-AIC isolator. The mini-DIN connector is not commercially available, so you cannot make this cable.                                                    | The 1761-CBL-AP00 cable (right-angle connector to controller) or the 1761-CBL-PM02 cable (straight connector to the controller) attaches the controller to port 2 on the 1761-NET-AIC isolator. The mini-DIN connector is not commercially available, so you cannot make this cable.                                                    | The 1761-CBL-AP00 cable (right-angle connector to controller) or the 1761-CBL-PM02 cable (straight connector to the controller) attaches the controller to port 2 on the 1761-NET-AIC isolator. The mini-DIN connector is not commercially available, so you cannot make this cable.                                                    | The 1761-CBL-AP00 cable (right-angle connector to controller) or the 1761-CBL-PM02 cable (straight connector to the controller) attaches the controller to port 2 on the 1761-NET-AIC isolator. The mini-DIN connector is not commercially available, so you cannot make this cable.                                                    | The 1761-CBL-AP00 cable (right-angle connector to controller) or the 1761-CBL-PM02 cable (straight connector to the controller) attaches the controller to port 2 on the 1761-NET-AIC isolator. The mini-DIN connector is not commercially available, so you cannot make this cable.                                                    |
|                |                                                                                                                                                                                                                                                                                                                                         | Pin DB-9 End Mini-DIN End                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                |                                                                                                                                                                                                                                                                                                                                         | 1 DCD DCD                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                | 2 RxD                                                                                                                                                                                                                                                                                                                                   | RxD                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                | 3 TxD                                                                                                                                                                                                                                                                                                                                   | TxD                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                |                                                                                                                                                                                                                                                                                                                                         | 4 DTR DTR                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                | 5 Ground                                                                                                                                                                                                                                                                                                                                | Ground                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                |                                                                                                                                                                                                                                                                                                                                         | 6 DSR DSR                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                |                                                                                                                                                                                                                                                                                                                                         | 7 RTS RTS                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                |                                                                                                                                                                                                                                                                                                                                         | 8 CTS CTS                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                |                                                                                                                                                                                                                                                                                                                                         | 9 N/A N/A                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                         |

## Default Serial Configuration

Channel 0 and Channel 1 (both serial ports) have the following default communication configuration.

| Parameter          | Default         |
|--------------------|-----------------|
| Protocol           | DF1 Full-duplex |
| Communication Rate | 19.2 Kbps       |
| Parity             | None            |
| Station Address    | 0               |

<!-- image -->

<!-- image -->

## Make Ethernet Connections to the Controller

| Parameter                                 | Default        |
|-------------------------------------------|----------------|
| Control Lines                             | No Handshaking |
| Error Detection                           | BCC            |
| Embedded Responses                        | Auto Detect    |
| Duplicate Packet (Message) Detect Enabled |                |
| ACK Timeout                               | 50 (x 20 ms)   |
| NAK Receive Limit                         | 3 Retries      |
| ENQ Transmit Limit                        | 3 Retries      |
| Data Bits                                 | 8              |
| Stop Bits                                 | 1              |

TIP

Only Channel 0 has a default communication push button.

## Using the Channel 0 Default Communication Push Button

The Channel 0 default communication push button is located on the front of the controller in the lower right corner as shown in the illustration. Use the Channel 0 default communication push button to change from the user-defined communication configuration to the default Communication mode. The Channel 0 default communication (DCH0) status indicator turns on (green, steady) to indicate that the default communication configuration is active.

## IMPORTANT

<!-- image -->

<!-- image -->

The default communication push button is recessed.

Before pressing the default communication push button, be sure to note the present communication configuration for Channel 0. Pushing the default communication push button resets all configured parameters back to their default settings.

To return the channel to its user-configured parameters, you must enter them manually while online with the controller or download them as part of an RSLogix 5000 software project file. To do this online with RSLogix 5000 software, access the Controller Properties dialog box and enter parameters on the Serial Port, System Protocol, and User Protocol tabs.

The 1769-L32E and 1769-L35E controller are shipped with the BOOTP utility enabled. You must assign an IP address to the Ethernet port for the controller to communicate over an EtherNet/IP network.

<!-- image -->

WARNING: If you connect or disconnect the communication cable with power applied to this module or any device on the network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding

Connect the RJ-45 connector of the Ethernet cable to the Ethernet port (top port) on the controller.

<!-- image -->

ATTENTION: Do not plug a DH-485 network cable or a NAP cable into the Ethernet port. Undesirable behavior or damage to the port may result.

<!-- image -->

## Assign an IP Address

You can set the IP address by using any of these utilities:

- Rockwell BOOTP Utility (available with RSLinx and RSLogix 5000 software)
- RSLinx software
- RSLogix 5000 software

Use BOOTP to Set the IP Address

The BOOTP utility is a standalone program in one of the following directories:

- RSLinx Tools directory in the Rockwell Software® program folder on the Start menu

The utility is automatically installed when you install RSLinx software.

- Utils directory on the RSLogix 5000 software installation CD

Follow this procedure to use the BOOTP utility.

1. Start the BOOTP software.
2. Select Tools&gt;Network Settings.
3. Enter the Ethernet mask and gateway.

## 4. Click OK.

<!-- image -->

In the BOOTP Request History dialog box, you see the hardware addresses of devices issuing BOOTP requests.

5. Double-click the hardware address of the device you want to configure.
2. TIP The hardware address is on the sticker on the left-side circuit board of the controller next to the battery.

<!-- image -->

The hardware address will be in this format: 00-0b-db-14-55-35.

The New Entry dialog box displays the device's Ethernet Address (MAC).

6. Enter the IP address.
7. Click OK.
8. To permanently assign this configuration to the device, highlight the device and click Disable BOOTP/DHCP.

<!-- image -->

When you cycle power, the device uses the configuration you assigned and does not issue a BOOTP request.

## Use RSLinx Software to Set the IP Address

1. You can use RSLinx software, version 2.41 or later, to set the IP address.
2. Make sure the controller that uses the IP address is installed and running.
3. Connect to the controller via the serial connection (see page 26).
4. Start RSLinx software.

The RSWho dialog box opens.

5. Navigate to the Ethernet network via the serial network.
6. Right-click the Ethernet port (not the controller) and select Module Configuration.
7. Select the Port Configuration tab.
8. Click the appropriate radio button to choose the Network Configuration type.
9. Enter the IP address, network (subnet) mask, and gateway address (if needed).

<!-- image -->

<!-- image -->

## Make ControlNet Connections to the Controller

## Use RSLogix 5000 Software to Set the IP Address

You can use RSLogix software to set the IP address.

1. Make sure the controller that uses the IP address is installed and running.
2. Connect to the controller via the serial connection (see page 26).
3. Start RSLogix 5000 software.
4. In the Controller Organizer, select properties for the Ethernet port.
5. Choose the Port Configuration tab.
6. Specify the IP address.
7. Click Apply.
8. Click OK.

<!-- image -->

This sets the IP address in the hardware. This IP address should be the same IP address you assigned under the General tab.

The CompactLogix 1769-L32C and 1769-L35CR controllers connect to the ControlNet network. The CompactLogix 1769-L32C controller supports channel A connections only. The CompactLogix 1769-L35CR controller supports channels A and B (redundant media) connections.

For permanent connections to the network, you connect the module to the ControlNet network by using a ControlNet tap (for example, 1786-TPR, 1786-TPS, 1786-TPYR, 1786-TPYS).

The figure shows an example ControlNet network using redundant media.

<!-- image -->

| Item Description                               |
|------------------------------------------------|
| 1 ControlNet node                              |
| 2 Redundant media available on 1769-L35CR only |
| 3 ControlNet link                              |

When connecting the CompactLogix controller to a ControlNet network, also refer to the following documentation:

- ControlNet Coax Tap Installation Instructions, publication 1786-IN007
- ControlNet Coax Media Planning and Installation Guide, publication CNET-IN002
- ControlNet Fiber Media Planning and Installation Guide, publication CNET-IN001

## IMPORTANT

For network connections we recommend taps with a straight connector (catalog number 1786-TPS or 1786-TPYS) because of the location of the BNC connectors on the bottom of the module.

## Connect the Controller to the Network via a ControlNet Tap

Typically, ControlNet taps are used to make permanent connections from the CompactLogix controller to the network. Perform the following steps to connect the module to the network by using a ControlNet tap.

<!-- image -->

ATTENTION: Do not allow any metal portions of the tap to contact any conductive material.

If you disconnect the tap from the module, place the dust cap back on the straight or right angle connector to prevent the connector from accidentally contacting a metallic grounded surface.

1. Remove and save the dust caps from the ControlNet taps.
2. Connect the tap's straight or right-angle connector to the module's BNC connector as shown in the figure.

<!-- image -->

| Item Description   |
|--------------------|
| 1 Segment 1        |
| 2 Segment 2        |
| 3 Dust caps        |

<!-- image -->

| Item Description                                                                          |
|-------------------------------------------------------------------------------------------|
| 1 Segment 1                                                                               |
| 2 Segment 2                                                                               |
| 3 Tap connected to a CompactLogix controller not using redundant media                    |
| 4 Tap connected to a CompactLogix controller using redundant media (1769-L35CR unit only) |
| 5 Tap                                                                                     |

## IMPORTANT

To prevent inadvertent reversal of the tap connections (resulting in incorrect status displays requiring troubleshooting), check the tap drop cable for the label indicating the attached segment before making your connection.

<!-- image -->

WARNING: If you connect or disconnect the communication cable with power applied to this module or any device on the network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding

## Connect a Programming Terminal to the Network via a 1786-CP Cable

You can use the CompactLogix controller's network access port (NAP) to connect a programming terminal to the ControlNet network. The figure shows the 1786-CP cable connections.

<!-- image -->

<!-- image -->

<!-- image -->

WARNING: The NAP port is intended for temporary local-programming purposes only and not intended for permanent connection. If you connect or disconnect the NAP cable with power applied to this module or any device on the network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

ATTENTION: Use the 1786-CP cable when you connect a programming terminal to the network through the NAP.

Using another cable could result in possible network failures or product damage.

Connect one end of the 1786-CP cable to the CompactLogix controller and the other end to the NAP of the programming terminal.

<!-- image -->

<!-- image -->

ATTENTION: Do not plug a DH-485 network cable or an RJ45 connector for the EtherNet/IP network to the NAP. Undesirable behavior and/or damage to the port may result.

## Install the Appropriate EDS Files

If you have RSLinx software, version 2.42 or later, the most current EDS files were installed with the software. If you are using an earlier version of RSLinx software, you might need to install EDS files.

You need EDS files for these devices:

- 1769-L32E and 1769-L35E controllers
- 1769 CompactBus
- 1769 local adapter

All of these EDS files, except for the 1769 CompactBus file, are updated for each firmware revision. There is also a version 1 of the controller EDS file that you need for new controllers. Each controller is shipped with revision 1 firmware. To update the firmware, you must have the revision 1 EDS file (0001000E00410100.eds) installed for the controller.

The EDS files are available on the RSLogix 5000 Enterprise Series software CD. The files are also available at http://www.ab.com/networks/eds .

Load the Controller Firmware You must download the current firmware before you can use the controller.

To load firmware, you can use any of the following:

- ControlFLASH utility that is shipped with RSLogix 5000 programming software
- AutoFlash that launches through RSLogix 5000 software when you download a project and the controller does not have the matching firmware revision
- CompactFlash card (catalog number 1784-CF128) with valid memory already loaded

If you use the ControlFLASH or AutoFlash utilities, you need a network connection to the controller.

The firmware is available with RSLogix 5000 software or you can download it from the support website. Go to http://www.rockwellautomation.com/support/.

Follow these steps to download firmware from the support website.

1. On the Rockwell Automation Support Page, click Software Updates, Firmware and Other Downloads under the Other Tools heading.
2. Click Firmware Updates.
3. Select the appropriate firmware update.
4. Select the firmware revision.
5. Click a revision file to unzip the data.

## Use the ControlFLASH Utility to Load Firmware

You can use the ControlFLASH utility to load firmware through a serial connection.

1. Make sure the appropriate network connection is made before starting.
2. Start the ControlFLASH utility.
3. When the Welcome dialog box appears, click Next.
4. Choose the catalog number of the controller and click Next.
5. Expand the network until you see the controller.
6. If the required network is not shown, first configure a driver for the network in RSLinx software.
7. Choose the controller and click OK.
8. Choose the revision level to which you want to update the controller and click Next.
9. To start the update of the controller, click Finish and then click Yes.
10. After the controller is updated, the status dialog box displays Update complete.
11. Click OK.
12. To close the ControlFLASH utility, click Cancel and then click Yes.

## Use AutoFlash to Load Firmware

You can use AutoFlash to load firmware through a network connection.

| IMPORTANT   | When upgrading your controller firmware, it is extremely important to allow the upgrade to complete without interruption.                                |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|             | If you interrupt the firmware upgrade either in the software or by disturbing the physical media, you may render the controller inoperable.              |
|             | For more information about upgrading your CompactLogix controller firmware, see information posted at http://www.rockwellautomation.com/knowledgebase/ . |

1. Make sure the appropriate network connection is made and your network driver is configured in RSLinx software.
2. Use RSLogix 5000 programming software to create a controller project.
3. Click RSWho to specify the controller path.

4. Select your controller and click Download.

You may also choose to click Update Firmware to complete this process. If you do so, skip to step 8 .

A dialog box displays indicating that the project revision and controller firmware revision are different.

5. Click Update Firmware.
6. Use the checkbox and pull-down menu to select your controller and firmware revision.
7. Click Update.
8. Click Yes.

The firmware upgrade begins.

## IMPORTANT

## DO NOT INTERRUPT THE FIRMWARE UPGRADE ONCE IT HAS BEGUN.

Interrupting the firmware upgrade may result in an inoperable controller.

When the firmware upgrade is complete, the Download dialog box appears and you may continue by downloading your project to the controller.

## Use a CompactFlash Card to Load Firmware

If you have an existing controller that is already configured and has firmware loaded, you can store the current controller user program and firmware on the CompactFlash card and use that card to update other controllers.

1. Use RSLogix 5000 software to store the controller user program and firmware of a currently configured controller to the CompactFlash card.
2. Access the Nonvolatile Memory tab of the Controller Properties dialog box.

Be sure to select Load Image On Powerup when you save to the card.

3. Remove the card and insert it into a controller that will use the same firmware and controller user program.

When you apply power to the second controller, the image stored on the CompactFlash card is loaded into the controller.

## Select the Controller's Operating Mode

Use the keyswitch on the front panel of the controller to determine the controller's operating mode.

| Keyswitch Position Description   |                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Run                              | •  Upload projects. •  Run the program and enable outputs. •  You cannot create or delete tasks, programs, or routines. You cannot create or delete tags or edit online while the keyswitch is in the Run position. •  You cannot change the mode by using the programming software while the keyswitch is in the Run position. | •  Upload projects. •  Run the program and enable outputs. •  You cannot create or delete tasks, programs, or routines. You cannot create or delete tags or edit online while the keyswitch is in the Run position. •  You cannot change the mode by using the programming software while the keyswitch is in the Run position. |
| Prog                             | •  Disable outputs.  •  Upload/download projects.  •  Create, modify, and delete tasks, programs, or routines.  •  The controller does not execute (scan) tasks while the keyswitch is in the Prog position. •  You cannot change the mode through the programming software while the keyswitch is in the Prog position.        | •  Disable outputs.  •  Upload/download projects.  •  Create, modify, and delete tasks, programs, or routines.  •  The controller does not execute (scan) tasks while the keyswitch is in the Prog position. •  You cannot change the mode through the programming software while the keyswitch is in the Prog position.        |
| Rem                              | •  Upload/download projects.  •  Change between Remote Program, Remote Test, and Remote Run modes through the programming software.                                                                                                                                                                                             | •  Upload/download projects.  •  Change between Remote Program, Remote Test, and Remote Run modes through the programming software.                                                                                                                                                                                             |
|                                  | Remote Run                                                                                                                                                                                                                                                                                                                      | •  The controller executes (scans) tasks. •  Enable outputs. •  Edit online.                                                                                                                                                                                                                                                    |
|                                  | Remote Program                                                                                                                                                                                                                                                                                                                  | •  Disable outputs. •  Create, modify, and delete tasks, programs, or routines. •  Download projects.  •  Edit online.  •  The controller does not execute (scan) tasks.                                                                                                                                                        |
|                                  | Remote Test                                                                                                                                                                                                                                                                                                                     | •  Execute tasks with outputs disabled.  •  Edit online.                                                                                                                                                                                                                                                                        |

## Notes:

## Connect to the Controller via the Serial Port

<!-- image -->

## Connect to the Controller via the Serial Port

This chapter describes how to connect to the controller via the serial port so that you can configure the controller and upload or download a project to the controller.

| Topic                                         |   Page |
|-----------------------------------------------|--------|
| Connect to the Controller via the Serial Port |     41 |
| Configure the Serial Driver                   |     43 |
| Select the Controller Path                    |     45 |

For the CompactLogix controller to operate on a serial network, you need:

- a workstation with a serial port.
- RSLinx software to configure the serial communication driver.
- RSLogix5000 programming software to configure the serial port of the controller.

Channel 0 on the CompactLogix controllers is fully isolated and does not need a separate isolation device. Channel 1 on the 1769-L31 is not an isolated serial port.

Figure 3 - Serial Connection to Controller

<!-- image -->

If you connect channel 1 of the 1769-L31 controller to a modem or an ASCII device, consider installing an isolator between the controller and modem or ASCII device. An isolator is also recommended when connecting the controller directly to a programming workstation. One possible isolator is the 1761-NETAIC interface converter.

For more information on installing an isolator, see Configure an Isolator on page 57 .

To connect a serial cable, perform this procedure.

1. Obtain a 1747-CP3 or 1756-CP3 serial cable.
2. TIP If you make your own serial cable, complete this procedure.
- Limit the length to 15.2 m (50 ft).
- Wire the connectors.
2. Connect the cable to your controller and workstation.

<!-- image -->

<!-- image -->

<!-- image -->

## Configure the Serial Driver

Use RSLinx software to configure the RS-232 DF1 Device driver for serial communication. To configure the driver, perform this procedure.

1. From the communication pull-down menu, choose Configure Drivers.

<!-- image -->

The Configure Drivers dialog box appears.

<!-- image -->

2. From the Available Driver Types pull-down menu, choose the RS-232 DF1 Device driver.
3. Click Add New to add the driver.

The Add New RSLinx Driver dialog box appears.

<!-- image -->

4. Specify the driver name and click OK.

- The Configure RS-232 DF1 Devices dialog box appears.
5. Specify the serial port settings.
- a. From the Comm Port pull-down menu, choose the serial port on the workstation to which the cable is connected.
- b. From the Device pull-down menu, choose Logix 5550-Serial Port.
- c. Click Auto-Configure.
6. Verify that the Auto-Configuration was successful.
7. Click Close.

<!-- image -->

| If Then                                                                     |
|-----------------------------------------------------------------------------|
| Yes Click OK.                                                               |
| No Go to step5 and verify that you selected the correct communication port. |

## Select the Controller Path

To select the controller path, perform this procedure.

1. In RSLogix 5000 programming software, open a project for the controller.
2. From the Communications pull-down menu, choose Who Active.

<!-- image -->

<!-- image -->

The Who Active dialog box appears.

<!-- image -->

3. Expand the communication driver to the level of the controller.
4. Select the controller.

## Controller Options

Once you have selected a controller, you have several options.

| To                                                                                 | Choose    |
|------------------------------------------------------------------------------------|-----------|
| Monitor the project in the controller                                              | Go Online |
| Transfer a copy of the project from the controller to RSLogix 5000 software Upload |           |
| Transfer the open project to the controller                                        | Download  |

## Communicate over Networks

This chapter explains how CompactLogix controllers support additional networks to enable various functions.

<!-- image -->

| Topic                             |   Page |
|-----------------------------------|--------|
| EtherNet/IP Network Communication |     48 |
| ControlNet Network Communication  |     50 |
| DeviceNet Communication           |     53 |
| Serial Communication              |     55 |
| DH-485 Network Communication      |     72 |

Table 4 - CompactLogix Controller Network Support

<!-- image -->

## EtherNet/IP Network Communication

The EtherNet/IP network offers a full suite of control, configuration and data collection services by layering the Common Industrial Protocol (CIP) over the standard Internet protocols, such as TCP/IP and UDP. This combination of well-accepted standards provides the capability required to both support information data exchange and control applications.

The EtherNet/IP network also uses commercial, off-the-shelf Ethernet components and physical media, providing you with a cost-effective plant-floor solution.

For EtherNet/IP communication, you can use these CompactLogix controllers with a built-in EtherNet/IP communication port:

- 1769-L32E CompactLogix controller
- 1769-L35E CompactLogix controller

You can use several software products with a 1769 CompactLogix controller on an EtherNet/IP network.

Table 5 - EtherNet/IP Network Software Combinations

| Software                                                  | Functions                                                                 | Requirement   |
|-----------------------------------------------------------|---------------------------------------------------------------------------|---------------|
| RSLogix 5000 programming software                         | •  Configure the CompactLogix project •  Define EtherNet/IP communication | Yes           |
| BOOTP/DHCP utility with RSLogix 5000 programming software | Assign IP addresses to devices on an EtherNet/IP network                  | No            |
| RSNetWorx software for an EtherNet/IP network             | Configure EtherNet/IP devices by IP addresses and/or host names           | No            |

The EtherNet/IP communication modules:

- support messaging, produced/consumed tags, HMI, and distributed I/O.
- encapsulate messages within standard TCP/UDP/IP protocol.
- share a common application layer with ControlNet and DeviceNet.
- interface via RJ45, category 5, unshielded, twisted-pair cable.
- support half/full-duplex 10 Mbps or 100 Mbps operation.
- support standard switches.
- require no network scheduling.
- require no routing tables.

## In this example:

- the controllers produce and consume tags amongst themselves.
- the controllers initiate MSG instructions that send and receive data or configure devices.
- the personal computer uploads or downloads projects to the controllers.
- the personal computer configures devices on an EtherNet/IP network.

Figure 4 - CompactLogix EtherNet/IP Overview

<!-- image -->

## Connections over an EtherNet/IP Network

You indirectly determine the number of connections the controller uses by configuring the controller to communicate with other devices in the system. Connections are allocations of resources that provide more reliable communication between devices than unconnected messages.

All EtherNet/IP connections are unscheduled. An unscheduled connection is a message transfer between controllers that is triggered by the requested packet interval (RPI) or the program, such as a MSG instruction. Unscheduled messaging lets you send and receive data when needed.

## ControlNet Network Communication

The 1769-L32E and 1769-L35E controllers support 100 connections. However, the built-in EtherNet/IP port supports only 32 CIP connections over an EtherNet/IP network. With these controllers, the number of end-node connections they effectively support depends on a connection's RPI.

| Requested Packet Interval Max EtherNet/IP Port Communication Connections   |
|----------------------------------------------------------------------------|
| 2 ms 2                                                                     |
| 4 ms 5                                                                     |
| 8 ms 10                                                                    |
| 16 ms 18                                                                   |
| 32 ms+ 25+                                                                 |

You can use all 32 communication connections on the built-in EtherNet/IP port. However, we recommend that you leave some connections available for tasks such as going online and non-I/O purposes.

ControlNet is a real-time control network that provides high-speed transport of both time-critical I/O and interlocking data and messaging data, including uploading and downloading of programming and configuration data on a single physical-media link. The ControlNet network's highly-efficient data transfer capability significantly enhances I/O performance and peer-to-peer communication in any system or application.

The ControlNet network is highly deterministic and repeatable and remains unaffected as devices are connected or disconnected from the network. This robust quality results in dependable, synchronized, and coordinated real-time performance.

The ControlNet network often functions as:

- the default network for the CompactLogix platform.
- a substitute/replacement for the remote I/O (RIO) network because the ControlNet network adeptly handles large numbers of I/O points.
- a backbone to multiple distributed DeviceNet networks.
- a peer interlocking network.

For ControlNet communication, you can use these CompactLogix controllers with a built-in ControlNet communication port:

- 1769-L32C CompactLogix controller
- 1769-L35CR CompactLogix controller

You can use these software products with a 1769 CompactLogix controller on a ControlNet network.

Table 6 - ControlNet Network Software Combinations

| Software                          | Functions                                                                                                       | Requirement   |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|
| RSLogix 5000 programming software | •  Configure the CompactLogix project •  Define EtherNet/IP communication                                       | Yes           |
| RSNetWorx for ControlNet software | •  Configure the ControlNet network •  Define the NUT (network update time)  •  Schedule the ControlNet network | Yes           |

## The ControlNet communication modules:

- support messaging, produced/consumed tags and distributed I/O.
- share a common application layer with DeviceNet and EtherNet/IP networks.
- require no routing tables.
- support the use of coax and fiber repeaters for isolation and increased distance.

## In this example:

- the controllers produce and consume tags amongst themselves.
- the controllers initiate MSG instructions that send and receive data or configure devices.
- the personal computer uploads or downloads projects to the controllers.
- the personal computer configures devices on ControlNet, and configures the network itself.

Table 7 - ControlNet Connection Methods

| Connection Method Description   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scheduled                       | A scheduled connection is unique to ControlNet communication. A scheduled connection lets you send and receive data repeatedly at a set interval, which is the requested packet interval (RPI). For example, a connection to an I/O module is a scheduled connection because you repeatedly receive data from the module at a specified interval. Other scheduled connections include connections to: •  communication devices. •  produced/consumed tags. On a ControlNet network, you must use RSNetWorx for ControlNet to enable all scheduled connections and establish a network update time (NUT). Scheduling a connection reserves network bandwidth to specifically handle the connection. |
| Unscheduled                     | An unscheduled connection is a message transfer between nodes that is triggered by ladder logic or the program (such as a MSG instruction). Unscheduled messaging lets you send and receive data when needed. Unscheduled messages use the remainder of network bandwidth after scheduled connections are allocated.                                                                                                                                                                                                                                                                                                                                                                               |

Figure 5 - CompactLogix ControlNet Overview

<!-- image -->

## Connections over ControlNet Network

You indirectly determine the number of connections the controller uses by configuring the controller to communicate with other devices in the system. Connections are allocations of resources that provide more reliable communication between devices compared to unconnected messages.

## DeviceNet Communication

The 1769-L32C and 1769-L35CR controllers support 100 connections. However, the built-in ControlNet port only supports 32 communication connections. With these controllers, the number of end-node connections they effectively support depends on the connection's NUT and RPI.

| NUT RPI Supported ControlNet Communication Connections (1)   |
|--------------------------------------------------------------|
| 2 ms 2 ms 0…1                                                |
| 3 ms 3 ms 1…2                                                |
| 5 ms 5 ms 3…4                                                |
| 10 ms 10 ms 6…9                                              |
| 14 ms 14 ms 10…12                                            |
| 5 ms 20 ms 12…16                                             |
| 4 ms 64 ms 31                                                |

You can use all 32 communication connections on the built-in ControlNet port. However, we recommend that you leave some connections available for tasks such as going online and unscheduled network traffic.

The DeviceNet network uses the Common Industrial Protocol (CIP) to provide the control, configuration, and data collection capabilities for industrial devices. The DeviceNet network uses the proven Controller Area Network (CAN) technology, which lowers installation costs and decreases installation time and costly downtime.

A DeviceNet network provides access to the intelligence present in your devices by letting you connect devices directly to plant-floor controllers without having to hard wire each device into an I/O module.

Table 8 - CompactLogix DeviceNet Communication Interfaces

| If your application                                                                                                                                                                    | Select                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| •  Communicates with other DeviceNet devices •  Uses the controller as a master or slave on DeviceNet •  Uses a controller ControlNet, Ethernet or serial port for other communication | 1769-SDN DeviceNet scanner module     |
| •  Accesses remote Compact I/O over a DeviceNet network •  Sends remote I/O data for as many as 30 modules back to scanner or controller                                               | 1769-ADN DeviceNet adapter module (1) |

<!-- image -->

You can use these software products with a 1769 CompactLogix controller on a DeviceNet network.

Table 9 - CompactLogix DeviceNet Software Combinations

| Software                          | Functions                                                                     | Requirement   |
|-----------------------------------|-------------------------------------------------------------------------------|---------------|
| RSLogix 5000 programming software | •  Configure the CompactLogix project  •  Define EtherNet/IP communication    | Yes           |
| RSNetWorx software for DeviceNet  | •  Configure DeviceNet devices  •  Define the scan list for DeviceNet devices | Yes           |

The DeviceNet communication module:

- supports messaging to devices, not controller to controller.
- shares a common application layer with ControlNet and EtherNet/IP.
- offers diagnostics for improved data collection and fault detection.
- requires less wiring than traditional, hardwired systems.

You can use a linking device as a:

- gateway to connect information.
- control-level network to device-level network for programming, configuration, control or data collection.
- router/bridge to connect the EtherNet/IP or ControlNet network to the DeviceNet network.

Figure 7 - CompactLogix Linking Device Overview

<!-- image -->

## Serial Communication

CompactLogix controllers have a built-in RS-232 port.

- 1769-L32C, -L32E, -L35CR, and -L35E CompactLogix controllers have one built-in RS-232 port. By default, that port is channel 0 on these controllers.
- The 1769-L31 CompactLogix controller has two RS-232 ports. One port only allows DF1 protocol only. The second port accepts DF1 and ASCII protocol.

## IMPORTANT

Limit the length of serial (RS-232) cables to 15.2 m (50 ft).

You can configure the serial port of the controller for several modes.

Table 10 - CompactLogix Serial Port Configuration

| Mode                  | Functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DF1 Point-to-Point    | Communicate between the controller and one other DF1-protocol-compatible device. This is the default system mode. Default parameters are: •  Baud Rate: 19,200 •  Data Bits: 8 •  Parity: None •  Stop Bits: 1 •  Control Line: No Handshake •  RTS send Delay: 0 •  RTS Off Delay: 0 This mode is typically used to program the controller through its serial port.                                                                                                                                                                                                                                                                                                                                          |
| DF1 Master            | Control polling and message transmission between the master and slave nodes. •  The master/slave network includes one controller configured as the master node and as many as 254 slave nodes. Link slave nodes using modems or line drivers. •  A master/slave network can have node numbers from 0…254. Each node must have a unique node address. Also, at least 2 nodes must exist to define your link as a network (1 master and 1 slave station are the two nodes).                                                                                                                                                                                                                                     |
| DF1 Slave             | Use a controller as a slave station in a master/slave serial communication network. •  When there are multiple slave stations on the network, link slave stations using modems or line drivers to the master. When you have a single slave station on the network, you do not need a modem to connect the slave station to the master. You can configure the control parameters for no handshaking. You can connect 2…255 nodes to a single link. In DF1 slave mode, a controller uses DF1 half-duplex protocol. •  One node is designated as the master and it controls who has access to the link. All the other nodes are slave stations and must wait for permission from the master before transmitting. |
| DF1 Radio Modem       | •  Compatible with SLC™ 500 and MicroLogix™ 1500 controllers. •  This mode supports master and slave, and store and forward modes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| User (channel 0 only) | Communicate with ASCII devices. This requires your program to use ASCII instructions to transmit data to and from ASCII device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DH-485                | •  Communicate with other DH-485 devices.  •  This multi-master, token-passing network allows programming and peer-to-peer messaging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Configure an Isolator

Channel 0 on the CompactLogix controllers is fully isolated and does not need a separate isolation device. Channel 1 on the 1769-L31 controller is not an isolated serial port. To configure an isolator, perform this procedure.

1. Determine whether you need an isolator.

If you connect channel 1 of the 1769-L31 controller to a modem or an ASCII device, consider installing an isolator between the controller and modem or ASCII device. An isolator is also recommended when connecting the controller directly to a programming workstation.

One possible isolator is the 1761-NET-AIC interface converter.

<!-- image -->

## 2. Select the appropriate cable.

## Are you using an isolator? Then use this cable

No

Yes

The 1756-CP3 cable attaches the controller directly to the controller.

<!-- image -->

If you make your own cable, it must be shielded, and the shields must be tied to the metal shell (that surrounds the pins) on both ends of the cable.

You can also use a 1747-CP3 cable from the SLC product family. This cable has a taller right-angle connector housing than that of the 1756-CP3 cable.

The 1761-CBL-AP00 cable (right-angle connector to controller) or the 1761-CBL-PM02 cable (straight connector to the controller) attaches the controller to port 2 on the 1761-NET-AIC isolator. The mini-DIN connector is not commercially available, so you cannot make this cable.

<!-- image -->

<!-- image -->

DB-9 Right-angle or Straight Cable End 8-pin, Mini-DIN Cable End

| Pin DB-9 End Mini-DIN End   |
|-----------------------------|
| 1 DCD DCD                   |
| 2 RxD RxD                   |
| 3 TxD TxD                   |
| 4 DTR DTR                   |
| 5 Ground Ground             |
| 6 DSR DSR                   |
| 7 RTS RTS                   |
| 8 CTS CTS                   |
| 9 NA NA                     |

3. Connect the appropriate cable to the serial port.

## Communicate with DF1 Devices

You can configure the controller as a master or slave on a serial communication network. Use serial communication when:

- the system contains three or more stations.
- communication occur regularly and require leased-line, radio, or power-line modem.

<!-- image -->

ATTENTION: Only the 1769-L31 controller has more than one RS-232 port. All other 1769 controllers are limited to one RS-232 port.

.

<!-- image -->

To configure the controller for DF1 communication, perform this procedure.

1. In RSLogix 5000 programming software, right-click your controller and select Properties.

<!-- image -->

The Controller Properties dialog box appears.

<!-- image -->

2. Click the Serial Port tab.
3. From the Mode pull-down menu, choose System.
4. Specify communication settings.
5. Click the System Protocol tab.
6. From the Protocol pull-down menu, choose a DF1 protocol.
7. Specify DF1 settings.

<!-- image -->

## DF1 Radio Modem Support

Your ControlLogix controller includes a driver that lets it to communicate over the DF1 Radio Modem protocol. This driver implements a protocol, optimized for use with radio modem networks, that is a hybrid between DF1 full-duplex protocol and DF1 half-duplex protocol, and therefore is not compatible with either of these protocols.

## IMPORTANT

The DF1 radio modem driver should be used only among devices that support and are configured for the DF1 radio modem protocol.

Additionally, there are some radio modem network configurations that will not work with the DF1 radio modem driver. In these configurations, continue to use DF1 half-duplex protocol.

<!-- image -->

Like DF1 full-duplex protocol, DF1 radio modem lets any node to connect to any other node at any time (if the radio modem network supports full-duplex data port buffering and radio transmission collision avoidance). Like DF1 half-duplex protocol, a node ignores any packets received that have a destination address other than its own, with the exception of broadcast packets and pass-through packets.

Unlike either DF1 full-duplex or DF1 half-duplex protocols, DF1 radio modem protocol does not include ACKs, NAKs, ENQs, or poll packets. Data integrity is assured by the CRC checksum.

## Using the DF1 Radio Modem Driver

The DF1 radio modem driver can be configured as the system mode driver by using RSLogix 5000 programming software, version 17 or later.

To configure the controller for DF1 Radio Modem communication, perform this procedure.

1. In the Controller Organizer of RSLogix 5000 programming software, right-click your controller and select Properties.

<!-- image -->

The Controller Properties dialog box appears.

<!-- image -->

2. Click the System Protocol tab.
3. From the Protocol pull-down menu, choose DF1 Radio Modem.

<!-- image -->

## 4. Specify DF1 Radio Modem system protocol settings.

| Setting         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Station Address | Specifies the node address of the controller on the serial network. Select a number 1… 254 decimal, inclusive. To optimize network performance, assign node addresses in sequential order. Initiators, such as personal computers, should be assigned the lowest address numbers to minimize the time required to initialize the network.                                                                                                                                                                                                                                                                                                                                                                |
| Error Detection | Click one of the radio buttons to specify the error detection scheme used for all messages. •  BCC - the processor sends and accepts messages that end with a BCC byte. •  CRC - the processor sends and accepts messages with a 2-byte CRC.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                 | Enable Store and Forward Check the Enable Store and Forward checkbox if you want to enable the store and forward functionality. When enabled, the destination address of any received message is compared to the Store and Forward tag table. If there is a match, the message is then forwarded (re-broadcasted) from the port. From the Store and Forward Tag pull-down menu, choose an integer (INT[16]) tag. Each bit represents a station address. If this controller reads a message destined for a station that has its bit set in this table, it forwards the message. Also note, the Enable Store and Forward function is usable only if the controller is connected to the master radio modem. |

## 5. Click OK.

## Advantage of Using DF1 Radio Modem Protocol

The primary advantage of using DF1 radio modem protocol for radio modem networks is in transmission efficiency. Each read/write transaction (command and reply) requires only one transmission by the initiator (to send the command) and one transmission by the responder (to return the reply). This minimizes the number of times the radios need to key-up to transmit, which maximizes radio life and minimizes radio power consumption. In contrast, DF1 half-duplex protocol requires five transmissions for the DF1 master to complete a read/write transaction with a DF1 slave - three by the master and two by the slave.

The DF1 radio modem driver can be used in a pseudo master/slave mode with any radio modems, as long as the designated master node is the only node initiating MSG instructions, and as long as only one MSG instruction is triggered at a time.

For modern serial radio modems that support full-duplex data port buffering and radio transmission collision avoidance, the DF1 radio modem driver can be used to set up a masterless peer-to-peer radio network. In a peer-to-peer radio network, any node can initiate communication to any other node at any time, as long as all of the nodes are within radio range so that they receive each other's transmissions.

## DF1 Radio Modem System Limitations

The following questions need to be answered to determine if you can implement the new DF1 radio modem driver in your radio modem network.

- If all of the devices on the network are ControlLogix controllers, you must configure them with the DF1 radio modem driver by using RSLogix 5000 programming software, version 17 or later. If not, then make sure that all of the nodes can support the DF1 radio modem protocol.
- If each node receives the radio transmissions of every other node, being both within radio transmission/reception range and on a common receiving frequency (either via a Simplex radio mode or via a single, common, full-duplex repeater) the radio modems must handle full-duplex data port buffering and radio transmission collision avoidance.

If this is the case, you can take full advantage of the peer-to-peer message initiation capability in every node (for example, the ladder logic in any node can trigger a MSG instruction to any other node at any time).

If not all modems can handle full-duplex data port buffering and radio transmission collision avoidance, you may still be able to use the DF1 radio modem driver, but only if you limit MSG instruction initiation to a single master node whose transmission can be received by every other node.

- If not all nodes receive the radio transmission of every other node, you may still be able to use the DF1 radio modem driver, but only if you limit MSG instruction initiation to the node connected to the master radio modem whose transmissions can be received by every other radio modem in the network.
- You can take advantage of the ControlLogix controller channel-to-channel pass-through to remotely program the other nodes using RSLinx and RSLogix 5000 programming software running on a personal computer connected to a local ControlLogix controller via DH-485, DH+, or Ethernet.

## Communicate with ASCII Devices

You can use the serial port to interface with ASCII devices when the controller is configured for user mode. For example, you can use the serial port to:

- read ASCII characters from a weigh scale module or bar code reader.
- send and receive messages from an ASCII triggered device, such as a MessageView terminal.

Figure 8 - ASCII Device Serial Communication

<!-- image -->

To configure the controller for ASCII communication, perform this procedure.

1. In RSLogix 5000 programming software, right-click your controller and select Properties.

<!-- image -->

The Controller Properties dialog box appears.

<!-- image -->

2. Click the Serial Port tab.
3. From the Mode pull-down menu, choose User.
4. Specify communication settings.

5. Click the User Protocol tab.
6. From the Protocol pull-down menu, choose ASCII.
7. Specify ASCII settings.

<!-- image -->

The controller supports several instructions to manipulate ASCII characters. The instructions are available in ladder diagram (LD) and structured text (ST).

## Read and Write ASCII Characters

| Instruction Code   | Description                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------|
| ABL                | Determine when the buffer contains termination characters                                             |
| ACB                | Count the characters in the buffer                                                                    |
| ACL                | Clear the buffer                                                                                      |
| ACL                | Clear out ASCII Serial Port instructions that are currently executing or are in the queue             |
| AHL                | Obtain the status of the serial port control lines                                                    |
| AHL                | Turn on or off the DTR signal                                                                         |
| AHL                | Turn on or off the RTS signal                                                                         |
| ARD                | Read a fixed number of characters                                                                     |
| ARL                | Read a varying number of characters, up to and including the first set of termination characters      |
| AWA                | Send characters and automatically append one or two additional characters to mark the end of the data |
| AWT                | Send characters                                                                                       |

## Create and Modify Strings of ASCII Characters

| Instruction Code   | Description                                     |
|--------------------|-------------------------------------------------|
| CONCAT             | Add characters to the end of a string           |
| DELETE             | Delete characters from a string                 |
| FIND               | Determine the starting character of a substring |
| INSERT             | Insert characters into a string                 |
| MID                | Extract characters from a string                |

## Convert Data to or from ASCII Characters

| Instruction Code Description   |                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------|
| STOD                           | Convert the ASCII representation of an integer value to a SINT, INT, DINT, or REAL value |
| STOR                           | Convert the ASCII representation of a floating-point value to a REAL value               |
| DTOS                           | Convert a SINT, INT, DINT, or REAL value to a string of ASCII characters                 |
| RTOS                           | Convert a REAL value to a string of ASCII characters                                     |
| UPPER                          | Convert the letters in a string of ASCII characters to upper case                        |
| LOWER                          | Convert the letters in a string of ASCII characters to lower case                        |

## Modbus Support

To use Logix5000 controllers on Modbus, connect the controllers through the serial port and execute specific ladder logic routines.

A sample controller project is available with RSLogix 5000 Enterprise programming software.

## Broadcast Messages over a Serial Port

You can broadcast messages over a serial port connection from a master controller to all of its slave controllers by using several communication protocols. Those protocols are the following:

- DF1 Master
- DF1 Radio Modem
- DF1 Slave

Broadcasting over a serial port is achieved using the 'message' tag. Because messages are sent to receiving controllers, only the 'write' type messages can be used for broadcasting.

The broadcast feature can be set up by using ladder logic programming software or Structured Text programming software.

The broadcast feature can also be set by modifying the path value of a message tag in the tag editor.

For this example, Ladder Logic programming software will be used.

## Step 1: Set Broadcast-Controller Properties

First, set the System Protocol by following these steps.

1. In the Controller Organizer, right-click on the controller and choose Properties.
2. In the Controller Properties dialog box, from the System Protocol tab, choose the settings for the controller, then choose OK.

<!-- image -->

| Field                        | DF-1 Master Protocol                                                                                                                                         | DF-1 Slave Protocol                                                                                   | DF-1 Radio Modem Protocol                                                                                                                                                                                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Station Address              |                                                                                                                                                              | Controller station address number Controller station address number Controller station address number |                                                                                                                                                                                                                                                                                        |
| Transmit Retries             | 3                                                                                                                                                            | 3                                                                                                     | N/A                                                                                                                                                                                                                                                                                    |
| ACK Timeout                  | 50                                                                                                                                                           | N/A                                                                                                   | N/A                                                                                                                                                                                                                                                                                    |
| Slave Poll Timeout           | N/A                                                                                                                                                          | 3000                                                                                                  | N/A                                                                                                                                                                                                                                                                                    |
| Reply Message Wait           | 5                                                                                                                                                            | N/A                                                                                                   | N/A                                                                                                                                                                                                                                                                                    |
| Polling Mode                 | Message: polls the slave by using the Message instruction Slave: initiates messages for slave-to-slave broadcast. Standard: schedules polling for the slave. | N/A                                                                                                   | N/A                                                                                                                                                                                                                                                                                    |
| EOT Suppression              | N/A                                                                                                                                                          | Disable                                                                                               | N/A                                                                                                                                                                                                                                                                                    |
| Error Detection              | BCC                                                                                                                                                          | BCC                                                                                                   | BCC                                                                                                                                                                                                                                                                                    |
| Duplicate Detection          | Enabled                                                                                                                                                      | Enabled                                                                                               | N/A                                                                                                                                                                                                                                                                                    |
| Enable Store and Forward N/A |                                                                                                                                                              | N/A                                                                                                   | Choose enable if you want to use the store and forward tag. The last bit of the INT[16] Enable Store and Forward array must be ’enabled.’ For example, say you create an INT[16] tag named EnableSandF. Then EnableSandF[15].15 must be set to 1 for broadcast to work on radio modem. |

## Step 2: Set Broadcast - Create Controller Scope Message Tag

Next, create a Message tag by following these steps.

1. In the Controller Organizer, right-click on the Controller Tags folder and choose New Tag.

The new tag must be a 'message' tag.

2. Name the tag and select the Data Type 'Message', then choose OK.

The Message tag in the Controller Scope's Controller Tags folder will look similar to the following.

Step 3: Ladder Logic Programming Software

<!-- image -->

| Name 色       | Value ←     | Style   | Data Type   |
|---------------|-------------|---------|-------------|
| -newtag       | {...}       |         | MESSAGE     |
| -newtag.Flags | 16#0200     | Hex     | INT         |
| newtag.Ew     | 0           | Decimal | BOOL        |
| newtag.ER     | 0           | Decimal | BOOL        |
| newtag.DN     | 0           | Decimal | BOOL        |
| newtag.ST     | 0           | Decimal | BOOL        |
| newtag.EN     | 0           | Decimal | BOOL        |
| newtag.TO     | 0           | Decimal | BOOL        |
| newtag.EN...  | 1           | Decimal | BOOL        |
| -newtag.ERR   | 16#0000     | Hex     | INT         |
| l-noutsnFV    | 16#0000000n | Hau     | DINIT       |

Then, to set broadcasting over a serial port, follow these steps.

1. In the Controller Organizer, from the Tasks folder, choose Main Routine to display the ladder logic programming software interface.
2. Open a MSG instruction from the Input/Output tab.
3. Double-click in the Message Control field to enable the pull-down menu and select the tag you created.
4. Launch the View Configuration dialog box.

5. In the Message Configuration dialog box, from the Configuration tab, select the message type from the Message Type field.

<!-- image -->

Valid 'Write' Message Types include the following:

- CIP Generic
- CIP Data Table Write
- PLC2 Unprotected Write
- PLC3 Typed Write
- PLC3 Word Range Write
- PLC5 Typed Write
- PLC5 Word Range Write
- SLC Typed Write
6. Fill in any other fields needed.

7. From the Communication tab, select the Broadcast Radio button and the Channel from the pull-down, then choose OK.

<!-- image -->

<!-- image -->

ATTENTION: When using structured text programming software, broadcast over serial is set by typing MSG(aMsg) and right-clicking on aMSG to display the Message Configuration dialog box.

## DH-485 Network Communication

For DH-485 communication, use the controller's serial port.

However, with a CompactLogix controller, we recommend that you use NetLinx networks, such as EtherNet/IP, ControlNet, or DeviceNet, because excessive traffic on a DH-485 network may make it impractical to connect to a controller with RSLogix 5000 programming software.

## IMPORTANT

If your application uses connections to DH-485 networks, select built-in serial ports.

The DH-485 protocol uses RS-485 half-duplex as its physical interface. RS-485 is a definition of electrical characteristics, not a protocol. You can configure the CompactLogix controller's RS-232 port to act as a DH-485 interface. By using a 1761-NET-AIC converter and the appropriate RS-232 cable (1756-CP3 or 1747-CP3), a CompactLogix controller can send and receive data on a DH-485 network.

Figure 9 - CompactLogix DH-485 Communication Overview

<!-- image -->

On the DH-485 network, the CompactLogix controller can send and receive messages to and from other controllers.

## IMPORTANT

A DH-485 network consists of multiple cable segments. Limit the total length of all the segments to 1219 m (4000 ft).

For the controller to operate on a DH-485 network, you need a 1761-NET-AIC interface converter for each controller you want to put on the DH-485 network.

You can have two controllers for each 1761-NET-AIC converter, but you need a different cable for each controller.

To establish DH-485 communication, perform this procedure.

1. Connect the serial port of the controller to either port 1 or port 2 of the 1761-NET-AIC converter.
2. Use the RS-485 port to connect the converter to the DH-485 network. The cable you use to connect the controller depends on the port you use on the 1761-NET-AIC converter.
3. In RSLogix 5000 programming software, right-click on your controller and choose Properties.

| Connection                          | Required Cable                 |
|-------------------------------------|--------------------------------|
| Port 1 DB-9 RS-232, DTE connection  | 1747-CP3 or 1761-CBL-AC00      |
| Port 2 mini-DIN 8 RS-232 connection | 1761-CBL-AP00 or 1761-CBL-PM02 |

<!-- image -->

The Controller Properties dialog appears.

<!-- image -->

4. Click the Serial Port tab.
5. From the Mode pull-down menu, choose System.
6. Specify communication settings.

## IMPORTANT

The baud rate specifies the communication rate for the DH-485 port. All devices on the same DH-485 network must be configured for the same baud rate. Select 9600 or 19200 KB.

Table 11 - System Protocol Specifications

| Characteristic Description   |                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              | Station Address Specifies the node address of the controller on the DH-485 network. Select a number 1…31 decimal, inclusive. To optimize network performance, assign node addresses in sequential order. Initiators, such as personal computers, should be assigned the lowest address numbers to minimize the time required to initialize the network. |
|                              | Token Hold Factor Number of transmissions plus retries that a node holding a token can send onto the data link each time it receives the token. Enter a value between 1…4. The default is 1.                                                                                                                                                            |
| Maximum Station Address      | Specifies the maximum node address of all the devices on the DH-485 network. Select a number 1…31 decimal, inclusive. To optimize network performance, make sure: •  the maximum node address is the highest node number being used on the network.  •  that all the devices on the same DH-485 network have the same maximum node address.             |

7. Click the System Protocol tab.
8. From the Protocol pull-down menu, choose DH485.
9. Specify DH-485 settings.
10. From the Protocol pull-down menu, choose DF1 Radio.

<!-- image -->

## Produce and Consume Data

## Manage Controller Communication

This chapter explains how to manage controller communication.

| Topic                       |   Page |
|-----------------------------|--------|
| Produce and Consume Data    |     75 |
| Send and Receive Messages   |     76 |
| Connections                 |     77 |
| Calculate Total Connections |     78 |
| Connections Example         |     79 |

The controller supports the ability to produce (broadcast) and consume (receive) system-shared tags over ControlNet or EtherNet/IP networks. Produced and consumed tags each require connections. Over ControlNet, produced and consumed tags are scheduled connections.

Table 12 - Controller Communication Overview

<!-- image -->

| Tag Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produced   | A produced tag allows other controllers to consume the tag, which means that a controller can receive the tag data from another controller. The producing controller uses one connection for the produced tag and another for each consumer. The controller’s communication device uses one connection for each consumer. As you increase the number of controllers that can consume a produced tag, you also reduce the number of connections the controller and communication device have available for other operations, like communication and I/O. |
| Consumed   | Each consumed tag requires one connection for the controller that is consuming the tag. The controller’s communication device uses one connection for each consumer.                                                                                                                                                                                                                                                                                                                                                                                    |

For two controllers to share produced or consumed tags, both controllers must be attached to the same control network, such as a ControlNet or Ethernet/IP network. You cannot bridge produced and consumed tags over two networks.

<!-- image -->

## Send and Receive Messages

The number of available connections limits the total number of tags that can be produced or consumed. If the controller uses all of its connections for I/O and communication devices, no connections are left for produced and consumed tags.

Messages transfer data to other devices, such as controllers or operator interfaces. Messages use unscheduled connections to send or receive data. Connected messages can leave the connection open (cache) or close the connection when the message is done transmitting.

Table 13 - Message Transmission

| Message Type                            | Communication Method       |               | Connected Message Can the message be cached?   |
|-----------------------------------------|----------------------------|---------------|------------------------------------------------|
| CIP data table read or write NA         |                            | Yes           | Yes                                            |
| PLC-2, PLC-3, PLC-5, or SLC (all types) | CIP  CIP with Source ID No | No            | No No                                          |
| PLC-2, PLC-3, PLC-5, or SLC (all types) | DH+                        | Yes           | Yes                                            |
| CIP generic                             | NA                         | Optional  (1) | Yes(2)                                         |
| Block-transfer read or write NA         |                            | NA            | Yes                                            |

Connected messages are unscheduled connections on both ControlNet and EtherNet/IP networks.

Each message uses one connection, regardless of how many devices are in the message path. You can program the target of a MSG instruction to optimize message transfer time.

Table 14 - Caching Messages

| Message Execution   | Function                                                                                                                                                         |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Repeatedly          | Cache the connection. This keeps the connection open and optimizes execution time. Opening a connection each time the message executes increases execution time. |
| Infrequently        | Do not cache the connection. This closes the connection upon completion of the message, freeing up that connection for other uses.                               |

## Connections

A Logix5000 system uses a connection to establish a communication link between two devices. Connections can be:

- a controller to local I/O modules or local communication modules.
- a controller to remote I/O or remote communication modules.
- a controller to remote I/O (rack-optimized) modules.
- produced and consumed tags.
- messages.
- controller access by RSLogix 5000 programming software.
- controller access by RSLinx software for HMI or other applications.

The limit of connections may ultimately reside in the communication module you use for the connection. If a message path routes through a communication module, the connection related to the message also counts towards the connection limit of that communication module.

Table 15 - Connections Overview

| Device                                                                                  | Supported Connections   |
|-----------------------------------------------------------------------------------------|-------------------------|
| CompactLogix controller (1769-L31)                                                      |                         |
| 100 Built-in ControlNet communication port (1769-L32C and 1769- L35CR controllers only) |                         |
| Built-in EtherNet/IP communication port (1769-L32E and 1769-L35E controllers only)      |                         |

## Determine Whether to Cache Message Connections

When you configure a MSG instruction, you can cache or not cache the connection.

## Calculate Total Connections

Table 16 - Local Connections Calculation

| Local Connection Type                                                              | Device Quantity Connections per Device   | Total Connections   |
|------------------------------------------------------------------------------------|------------------------------------------|---------------------|
| Local I/O module (always a direct connection)                                      | 1                                        |                     |
| Built-in ControlNet communication port (1769-L32C and 1769-L35CR controllers only) | 0                                        |                     |
| Built-in EtherNet/IP communication port (1769-L32E and 1769-L35E controllers only) | 0                                        |                     |
| 1769-SDN DeviceNet scanner module                                                  | 2                                        |                     |
| Total                                                                              | Total                                    | Total               |

The number of remote connections a communication module supports determines how many connections the controller can access through that module.

Table 17 - Remote Connections Calculation

| Remote Connection Type                                                                                                               | Device Quantity Connections per Device   | Total Connections   |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|---------------------|
| Remote ControlNet communication module •  I/O configured as direct connection (none) •  I/O configured as rack-optimized connection  | 0 or 1                                   |                     |
| Remote I/O module over ControlNet (direct connection)                                                                                | 1                                        |                     |
| Remote EtherNet/IP communication module •  I/O configured as direct connection (none) •  I/O configured as rack-optimized connection | 0 or 1                                   |                     |
| Remote I/O module over a EtherNet/IP network (direct connection)                                                                     | 1                                        |                     |
| Remote device over a DeviceNet network (accounted for in rack-optimized connection for local 1769- SDN module)                       | 0                                        |                     |
| Other remote communication adapter (POINT and FLEX adapters, for example)                                                            | 1                                        |                     |
| Produced tag Each consumer                                                                                                           | 1 1                                      |                     |
| Consumed tag                                                                                                                         | 1                                        |                     |
| Message (depending on type)                                                                                                          | 1                                        |                     |
| Block-transfer message                                                                                                               | 1                                        |                     |
|                                                                                                                                      |                                          | Total               |

You can calculate the total number of local and remote connections the controller uses.

## Connections Example

In this example system the 1769-L35E CompactLogix controller:

- controls local digital I/O modules in the same chassis.
- controls remote I/O devices on a DeviceNet network.
- sends and receives messages to/from a ControlLogix controller on an EtherNet/IP network.
- produces one tag that the 1794 FlexLogix controller consumes.
- is programmed via RSLogix 5000 programming software.

Figure 10 - Example - CompactLogix System Connections

<!-- image -->

Table 18 - Example - CompactLogix Connection Types

| Connection Type                                                        |       | Device Quantity Connections per Device   |   Total Connections |
|------------------------------------------------------------------------|-------|------------------------------------------|---------------------|
| Controller to local I/O modules (rack-optimized)                       | 2     | 1                                        |                   2 |
| Controller to 1769-SDN scanner module                                  | 1     | 2                                        |                   2 |
| Controller to built-in EtherNet/IP communication port (rack-optimized) | 1     | 0                                        |                   0 |
| Controller to RSLogix 5000 programming software                        | 1     | 1                                        |                   1 |
| Message to ControlLogix controller                                     | 2     | 1                                        |                   2 |
| Produced tag consumed by FlexLogix controller                          | 2     | 1                                        |                   2 |
| Total                                                                  | Total | Total                                    |                   9 |

## Notes:

## Select I/O Modules

## Place, Configure, and Monitor I/O

This chapter explains how to place, configure, and monitor CompactLogix I/O modules.

| Topic                                               |   Page |
|-----------------------------------------------------|--------|
| Select I/O Modules                                  |     81 |
| Place Local I/O Modules                             |     86 |
| Configure I/O                                       |     87 |
| Configure Distributed I/O on an EtherNet/IP Network |     88 |
| Configure Distributed I/O on a ControlNet Network   |     89 |
| Configure Distributed I/O on a DeviceNet Network    |     90 |
| Address I/O Data                                    |     91 |
| Determine When Data Is Updated                      |     92 |
| Reconfigure an I/O Module                           |     94 |

When choosing 1769 I/O modules, select:

- specialty I/O modules when appropriate.

Some modules have field-side diagnostics, electronic fusing, or individually-isolated inputs and outputs.

- a 1492 wiring system for each I/O module as an alternative to the terminal block that comes with the module.
- 1492 PanelConnect modules and cables if you are connecting input modules to sensors.

<!-- image -->

## Validate I/O Layout

After you have selected your I/O modules, you need to validate the system you want to design. Before you begin to place your I/O modules, consider that the minimum backplane RPI increases as you add modules. Also, the I/O modules must be distributed so that the current consumed from the left or right side of the power supply never exceeds 2.0 A at 5V DC or 1.0 A at 24V DC.

## Estimate Requested Packet Interval

The requested packet interval (RPI) defines the frequency at which the controller sends and receives all I/O data on the backplane. Each module on the backplane can have its own individual RPI setting.

The effective scan frequency for any individual module is still impacted by the other modules in the system and those modules' RPI settings. The following table provides relative scanning durations for various types of modules. This information should be taken into account when setting an individual module's RPI in order to achieve the desired effective scan frequency for any module in the system.

| Type of Module               | Request Packet Interval                                                                                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Digital and analog (any mix) | •  1…4 modules can be scanned in 1 ms. •  5…30 modules can be scanned in 2 ms. •  Some input modules have a fixed 8 ms filter, so selecting a greater RPI has no effect. |
| Specialty                    | •  Full-sized 1769-SDN modules add 2 ms per module. •  1769-HSC modules add 1 ms per module. •  Full-sized 1769-ASCII modules add 1 ms per module.                       |

You can always select an RPI that is slower than these. The RPI shows how quickly modules can be scanned, not how quickly an application can use the data. The RPI is asynchronous to the program scan. Other factors, such as program execution duration, affect I/O throughput.

## Calculate System Power Consumption

To validate your proposed system, calculate the total 5V DC current and 24V DC to be consumed.

Table 19 - I/O Module Power Consumption Calculation Table

| Catalog Number Number of     | Modules                      | Module Current Requirements Calculated Current = (Number of Modules) x (Module Current Requirements)   | Module Current Requirements Calculated Current = (Number of Modules) x (Module Current Requirements)   |
|------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                              |                              |                                                                                                        | at 5V DC (in mA) at 24V DC (in mA) at 5V DC (in mA) at 24V DC (in mA)                                  |
|                              | 1769-L31 330 40              |                                                                                                        |                                                                                                        |
|                              | 1769-L32C 650 40             |                                                                                                        |                                                                                                        |
|                              | 1769-L32E 660 90             |                                                                                                        |                                                                                                        |
|                              | 1769-L35CR 680 40            |                                                                                                        |                                                                                                        |
| 1769-L35E                    |                              |                                                                                                        | 660  90                                                                                                |
| Total Current Required (1) : | Total Current Required (1) : | Total Current Required (1) :                                                                           | Total Current Required (1) :                                                                           |

Table 20 - Power Supply Current Capacity

| Specification                                   | Power Supply and Capacity        | Power Supply and Capacity        | Power Supply and Capacity      | Power Supply and Capacity      |
|-------------------------------------------------|----------------------------------|----------------------------------|--------------------------------|--------------------------------|
|                                                 | 1769-PA2                         |                                  |                                | 1769-PB2 1769-PA4 1769-PB4     |
| Output Bus Current Capacity 0…55 °C (32…131 °F) | 2 A at 5V DC and 0.8 A at 24V DC | 2 A at 5V DC and 0.8 A at 24V DC | 4 A at 5V DC and 2 A at 24V DC | 4 A at 5V DC and 2 A at 24V DC |
| 24V DC User Power Capacity 0…55 °C (32…131 °F)  | 250 mA (maximum)                 | NA                               |                                |                                |

## Validate Placement of I/O Modules

The controller you use determines how many local I/O modules you can configure.

Table 21 - Controller I/O Support

| Controller                        |   Supported Local I/O Modules I/O Banks |    |
|-----------------------------------|-----------------------------------------|----|
| 1769-L35CR                        |                                      30 |  3 |
| 1769-L35E                         |                                      30 |  3 |
| 1769-L32C, 1769-L32E and 1769-L31 |                                      16 |  3 |

To validate the proposed placement of I/O modules in your CompactLogix system, perform this procedure.

1. Verify that your 1769-L3x controller resides on the leftmost side of the bank.

## Single-Bank System

<!-- image -->

Controller

2. Verify that you have placed no more than three I/O modules between your controller and power supply (bank 0).

Placing more than three I/O modules in bank 0 would exceed the distance rating of four and invalidate your system.

3. Validate the number of I/O modules your power supply can support.

In a single-bank system, make sure you have not placed more than eight I/ O modules between the power supply and end cap (bank 1).

## IMPORTANT

In a single-bank system, the power supply can support up to eight I/O modules as long as the modules' power consumption does not exceed the power supply's capacity.

So, in a single-bank system, you may not have more than eleven total I/O modules, three to the left of your power supply and eight to the right.

If your system requires additional I/O modules, you must add an additional bank.

In a multi-bank system, make sure that your additional bank(s) do not have more than eight I/O modules on either side of the additional power supply.

## IMPORTANT

In a multi-bank system, you may place up to eight I/O modules on either side of the additional power supply so long as the power consumed by these modules does not exceed the power supply's capacity.

In this example, the I/O modules 12…30 could be arranged in any way as long as the power supplies' capacity was not exceeded. In other words, the first additional bank could contain fewer than 16 I/O modules This is just 1 possible arrangement.

## Example of Multi-Bank System

4. Verify that all banks have end caps.

<!-- image -->

## IMPORTANT

If you place and configure more I/O modules and I/O banks than your controller can support, your system may run well for a period of time. Nothing alerts you to the fact that you have exceeded your controller's capacity.

However, by exceeding your controller's I/O capacity, you put your system at risk of intermittent faults, the most common being Major Fault Type 03 (I/O Fault) Code 23.

## Place Local I/O Modules

Horizontal

Orientation

Use the 1769-CRR1/-CRR3 or 1769-CRL1/-CRL3 expansion cable to connect banks of I/O modules.

Each I/O module also has a power supply distance rating, the number of modules from the power supply. The distance rating is printed on each module's label. Each module must be located within its distance rating.

Figure 11 - Controller I/O Placement

<!-- image -->

<!-- image -->

ATTENTION: The CompactLogix system does not support Removal and Insertion Under Power (RIUP). While the CompactLogix system is under power:

- any break in the connection between the power supply and the controller (for example, removing the power supply, controller, or an I/O module) may subject the logic circuitry to transient conditions above the normal design thresholds and may result in damage to system components or unexpected behavior.
- removing an end cap or an I/O module faults the controller and may also result in damage to system components.

The CompactLogix controller also supports distributed (remote) I/O via these networks:

- EtherNet/IP
- ControlNet
- DeviceNet

## Configure I/O

Table 22 - I/O Configuration Options

| Configuration Option   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        | Requested packet interval (RPI) The RPI specifies the interval at which data updates over a connection. For example, an input module sends data to a controller at the RPI that you assign to the module. •  Typically, you configure an RPI in milliseconds (ms). The range is 0.1…750 ms. •  If a ControlNet network connects the devices, the RPI reserves a slot in the stream of data flowing across the ControlNet network. The timing of this slot may not coincide with the exact value of the RPI, but the control system guarantees that the data transfers at least as often as the RPI. |
| Change of state (COS)  | Digital I/O modules use COS to determine when to send data to the controller. If a COS does not occur within the RPI timeframe, the module multicasts data at the RPI. Because the RPI and COS functions are asynchronous to the logic scan, it is possible for an input to change state during program scan execution. If this is a concern, buffer input data so your logic has a stable copy of data during its scan. Use the Synchronous Copy (CPS) instruction to copy the input data from your input tags to another structure and use the data from that structure.                          |
| Communication format   | Many I/O modules support different formats. The communication format that you choose also determines: •  data structure of tags. •  connections. •  network usage.  •  ownership.  •  returning of diagnostic information.                                                                                                                                                                                                                                                                                                                                                                          |
| Electronic keying      | When you configure a module, you specify the slot number for the module. However, it is possible to purposely or accidentally place a different module in that slot. Electronic keying lets you protect your system against the accidental placement of the wrong module in a slot. The chosen keying option determines how closely any module in a slot must match the configuration for that slot before the controller opens a connection to the module. There are different keying options depending on your application needs.                                                                 |

To communicate with an I/O module in your system, add the module to the I/O Configuration folder of the controller.

Figure 12 - I/O Module Configuration

<!-- image -->

When you add a module, you also define a specific configuration for the module. While the configuration options vary from module to module, there are some common options that you typically configure

Table 23 - Logix5000 I/O Connections

| Connection     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct         | A direct connection is a real-time, data-transfer link between the controller and an I/O module. The controller maintains and monitors the connection between the controller and the I/O module. Any break in the connection, such as a module fault or the removal of a module while under power, causes the controller to set fault status bits in the data area associated with the module. Typically, analog I/O modules, diagnostic I/O modules, and specialty modules require direct connections. |
| Rack-optimized | For digital I/O modules, you can select rack-optimized communication. A rack-optimized connection consolidates connection usage between the controller and all the digital I/O modules on a rack (or DIN rail). Rather than having individual, direct connections for each I/ O module, there is one connection for the entire rack (or DIN rail).                                                                                                                                                      |

## Configure Distributed I/O on an EtherNet/IP Network

## For a typical distributed I/O network…

<!-- image -->

To communicate with distributed I/O modules over an EtherNet/IP network:

- choose a 1769-L32E or 1769-L35E CompactLogix controller with a builtin EtherNet/IP communication port.
- add an EtherNet/IP adapter, and I/O modules to the I/O Configuration folder of the controller.

Within the I/O Configuration folder, organize the modules into a hierarchy of tree/branch and parent/child.

Figure 13 - EtherNet/IP Distributed I/O Configuration

## I/O Connections

A Logix5000 system uses connections to transmit I/O data.

## Configure Distributed I/O on a ControlNet Network

## For a typical distributed I/O network…

<!-- image -->

To communicate with distributed I/O modules over a ControlNet network:

- choose a 1769-L32C or 1769-L35CR CompactLogix controller with a built-in ControlNet communication port.
- add a ControlNet adapter, and I/O modules to the I/O Configuration folder of the controller.

Within the I/O Configuration folder, organize the modules into a hierarchy of tree/branch and parent/child.

Figure 14 - ControlNet Distributed I/O Configuration

## Configure Distributed I/O on a DeviceNet Network

For a typical distributed I/O network…

To communicate with the I/O modules over a DeviceNet network, add the DeviceNet bridge to the I/O Configuration folder of the controller. RSNetWorx for DeviceNet software is used to define the scanlist within the DeviceNet scanner to communicate data between the devices and the controller through the scanner.

Figure 15 - DeviceNet Distributed I/O Configuration

<!-- image -->

## Address I/O Data

I/O information is presented as a set of tags.

- Each tag uses a structure of data, depending on the specific features of the I/O module.
- The name of the tags is based on the location of the I/O module in the system.

## Figure 16 - I/O Address Format

Location :Slot :Type .Member

.SubMember

.Bit

= Optional

| Where     | Is                                                                                                                                                                                                                                                                   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location  | Network location.                                                                                                                                                                                                                                                    |
| Location  | Local = same chassis or DIN rail as the controller.                                                                                                                                                                                                                  |
| Location  | Adapter_Name = identifies remote communication adapter or bridge module.                                                                                                                                                                                             |
| Slot      | Slot number of I/O module in its chassis or DIN rail.                                                                                                                                                                                                                |
| Type      | Type of data.                                                                                                                                                                                                                                                        |
| Type      | I = input.                                                                                                                                                                                                                                                           |
| Type      | O = output.                                                                                                                                                                                                                                                          |
| Type      | C = configuration.                                                                                                                                                                                                                                                   |
| Type      | S = status.                                                                                                                                                                                                                                                          |
| Member    | Specific data from the I/O module, depending on what type of data the module can store. •  For a digital module, a data member usually stores the input or output bit values. •  For an analog module, a channel member (CH#) usually stores the data for a channel. |
| SubMember | Specific data related to a member.                                                                                                                                                                                                                                   |
| Bit       | Specific point on a digital I/O module, depending on the size of the I/O module (0…31 for a 32-point module).                                                                                                                                                        |

## Determine When Data Is Updated

CompactLogix controllers update data asynchronously with the execution of logic. This flowchart illustrates when producers send data. Controllers, input modules and bridge modules are producers.

<!-- image -->

TIP If you need to ensure that the I/O values being used during logic execution are from one moment in time, such as at the beginning of a ladder program, use the Synchronous Copy instruction (CPS) to buffer I/O data.

## Monitor I/O Modules

With the CompactLogix controller, you can monitor I/O modules at different levels by:

- ·
- using the programming software to display fault data.

Refer to Display Fault Data on page 93 .

- programming logic to monitor fault data so you can take appropriate action

## Display Fault Data

Fault data for certain types of module faults can be viewed through the programming software.

To display fault data, perform this procedure.

1. In RSLogix 5000 programming software, select Controller Tags in the Controller Organizer and right-click to select Monitor Tags.

<!-- image -->

The display style for the fault data defaults to decimal.

<!-- image -->

2. Change the display style to Hex to read the fault code.

If the module faults, but the connection to the controller remains open, the controller tags database displays the fault value 16#0E01\_0001. The fault word uses this format.

<!-- image -->

## Reconfigure an I/O Module

| Bit       | Description                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fault_Bit | This bit indicates that at least one bit in the fault word is set (1). If all the bits in the fault word are cleared (0), this bit is cleared (0).              |
|           | Connection_Closed This bit indicates whether the connection to the module is open (0) or closed (1). If the connection is closed (1), the Fault_Bit is set (1). |

## End-cap Detection and Module Faults

If a module not adjacent to an end cap experiences a fault and the connection to the controller is not broken, only the module enters the fault state. If a module adjacent to an end cap experiences a fault, both the module and the controller transition to the fault state.

If an I/O module supports reconfiguration, you can reconfigure the module via:

- the Module Properties dialog box in RSLogix 5000 programming software.
- a MSG instruction in program logic.

## Reconfigure a Module via RSLogix 5000 Programming Software

To reconfigure an I/O module via RSLogix 5000 programming software, perform this procedure.

1. Highlight the module in the I/O Configuration tree and right-click to choose Properties.

<!-- image -->

The Controller Properties dialog box appears.

<!-- image -->

2. Reconfigure the module.

## Reconfigure a Module via a MSG Instruction

To reconfigure an I/O module, use a Module Reconfigure MSG instruction. During the reconfiguration:

- input modules continue to send input data to the controller.
- output modules continue to control their output devices.

A Module Reconfigure message requires the property Message Type and a selection of Module Reconfigure.

To reconfigure an I/O module, perform this procedure.

1. Set the required member of the configuration tag of the module to the new value.
2. Send a Module Reconfigure message to the module.

<!-- image -->

## Notes:

## Manage Tasks

## Develop Applications

This chapter explains how to develop applications.

| Topic                                          |   Page |
|------------------------------------------------|--------|
| Manage Tasks                                   |     97 |
| Develop Programs                               |     98 |
| Organize Tags                                  |    103 |
| Select a Programming Language                  |    104 |
| Monitor Controller Status                      |    106 |
| Monitor Connections                            |    107 |
| Select a System Overhead Time Slice Percentage |    109 |

With a Logix5000 controller, you can use multiple tasks to schedule and prioritize the execution of your programs based on specific criteria. This divides your controller's processing time among the different operations in your application. Remember that:

- the controller executes only one task at one time.
- one exception task can interrupt another and take control.
- in any given task, only one program executes at one time.

<!-- image -->

## Develop Programs

Control Application

The controller's operating system is a preemptive multitasking system that is IEC 1131-3 compliant. This environment provides:

- tasks to configure controller execution.
- programs to group data and logic.
- routines to encapsulate executable code written in a single programming language.

Figure 19 - Program Development

<!-- image -->

## Define Tasks

Tasks provide scheduling and priority information for programs. You can configure tasks as continuous, periodic, or event tasks. Only one task can be continuous.

Table 24 - Task Support

| Controller   |   Tasks Supported |
|--------------|-------------------|
| 1769-L35x    |                 8 |
| 1769-L32x    |                 6 |
| 1769-L31     |                 4 |

A task can have as many as 32 separate programs, each with its own executable routines and program-scoped tags. Once a task is triggered (activated), all the programs assigned to the task execute in the order in which they are grouped. Programs can only appear once in the Controller Organizer and cannot be shared by multiple tasks.

## Specify Task Priorities

Each task in the controller has a priority level. The operating system uses the priority level to determine which task to execute when multiple tasks are triggered. You can configure periodic tasks to execute from the lowest priority of 15 up to the highest priority of 1. A higher-priority task will interrupt any lowerpriority task. The continuous task has the lowest priority and is always interrupted by a periodic task.

The CompactLogix controller uses a dedicated periodic task at priority 6 to process I/O data. This periodic task executes at the RPI you configure for the CompactBus, which can be as fast as once each millisecond. Its total execution time is as long as it takes to scan the configured I/O modules.

How you configure your tasks affects how the controller receives I/O data. Tasks at priorities 1…5 take precedence over the dedicated I/O task. Tasks in this priority range can impact I/O processing time. For example, if you use the following configuration:

- I/O RPI = 1 ms
- a task of priority = 1…5 that requires 500 s to execute and is scheduled to run every millisecond

this configuration leaves the dedicated I/O task 500 s to complete its job of scanning the configured I/O.

Table 25 - Multiple Tasks Example

|    | Task Priority Level   | Task Type                            |       | Example Execution Time Worst-Case Completion Time   |
|----|-----------------------|--------------------------------------|-------|-----------------------------------------------------|
|  1 | 5                     | 20 ms periodic task                  | 2 ms  | 2 ms                                                |
|  2 | 7                     | Dedicated I/O task 5 ms selected RPI | 1 ms  | 3 ms                                                |
|  3 | 10                    | 10 ms periodic task                  | 4 ms  | 8 ms                                                |
|  4 | None (lowest)         | Continuous task                      | 25 ms | 60 ms                                               |

<!-- image -->

However, if you schedule two high priority tasks 1…5 to run every millisecond, and they both require 500 s or more to execute, no CPU time would be left for the dedicated I/O task. Furthermore, if you have so much configured I/O that the execution time of the dedicated I/O task approaches 2 ms (or the combination of the high priority tasks and the dedicated I/O task approaches 2 ms) no CPU time is left for low priority tasks 7…15.

TIP

For example, if your program needs to react to inputs and control outputs at a set rate, configure a periodic task with a priority higher than 6 (1…5). This keeps the dedicated I/O task from affecting the periodic rate of your program. However, if your program contains a lot of math and data manipulation, place this logic in a task with priority lower than 6 (7…15), such as the continuous task, so that the dedicated I/O task is not adversely affected by your program.

Remember that:

- the highest priority task interrupts all lower priority tasks.
- the dedicated I/O task can be interrupted by tasks with priority levels 1…5.

The dedicated I/O task interrupts tasks with priority levels 7…15. This task runs at the selected RPI rate scheduled for the CompactLogix system (2 ms in this example).

- the continuous task runs at the lowest priority and is interrupted by all other tasks.
- a lower priority task can be interrupted multiple times by a higher priority task.
- when the continuous task completes a full scan it restarts immediately, unless a higher priority task is running.

## Define Programs

Each program contains:

- program tags.
- a main executable routine.
- other routines.
- an optional fault routine.

Each task can schedule as many as 32 programs.

The scheduled programs within a task execute to completion from first to last. Programs unattached to any task show up as unscheduled programs. You must specify (schedule) a program within a task before the controller can scan the program.

## Define Routines

A routine is a set of logic instructions in a single programming language, such as ladder logic. Routines provide the executable code for the project in a controller. A routine is similar to a program file or subroutine in a PLC or SLC controller.

Each program has a main routine. This is the first routine to execute when the controller triggers the associated task and calls the associated program. Use logic, such as the Jump to Subroutine ( JSR) instruction, to call other routines.

You can also specify an optional program fault routine. The controller executes this routine if it encounters an instruction-execution fault within any of the routines in the associated program.

## Sample Controller Projects

RSLogix 5000 Enterprise programming software includes sample projects that you can copy and then modify to fit your application.

To view a set of sample controller projects, perform this procedure.

1. From the Help pull-down menu, choose Vendor Sample Projects.
2. Scroll down to select a set of sample projects.

<!-- image -->

<!-- image -->

## Organize Tags

With a Logix5000 controller, you use a tag (alphanumeric name) to address data (variables). In Logix5000 controllers, there is no fixed, numeric format. The tag name itself identifies the data. This lets you:

- organize your data to mirror your machinery.
- document (through tag names) your application as you develop it.

Figure 20 - Tag Organization

<!-- image -->

When you create a tag, assign these properties to the tag:

- Tag type
- Data type
- Scope

## Select a Programming Language

Table 26 - Programming Language Selection

| Required Language               | Program                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Ladder diagram (LD)             | Continuous or parallel execution of multiple operations (not sequenced)                                                |
| Ladder diagram (LD)             | Boolean or bit-based operations                                                                                        |
| Ladder diagram (LD)             | Complex logical operations                                                                                             |
| Ladder diagram (LD)             | Message and communication processing                                                                                   |
| Ladder diagram (LD)             | Machine interlocking                                                                                                   |
| Ladder diagram (LD)             | Operations that service or maintenance personnel may have to interpret in order to troubleshoot the machine or process |
| Function block diagram (FBD)    | Continuous process and drive control                                                                                   |
| Function block diagram (FBD)    | Loop control                                                                                                           |
| Function block diagram (FBD)    | Calculations in circuit flow                                                                                           |
| Sequential function chart (SFC) | High-level management of multiple operations                                                                           |
| Sequential function chart (SFC) | Repetitive sequence of operations                                                                                      |
| Sequential function chart (SFC) | Batch process                                                                                                          |
| Sequential function chart (SFC) | Motion control using structured text                                                                                   |
| Sequential function chart (SFC) | State machine operations                                                                                               |
| Structured text (ST)            | Complex mathematical operations                                                                                        |
| Structured text (ST)            | Specialized array or table loop processing                                                                             |
| Structured text (ST)            | ASCII string handling or protocol processing                                                                           |

The CompactLogix controller supports these programming languages, both online and offline.

## Add-on Instructions

With version 18 of RSLogix 5000 programming software, you can design and configure sets of commonly used instructions to increase project consistency. Similar to the built-in instructions contained in Logix5000 controllers, these instructions you create are called Add-on Instructions. Add-on Instructions reuse common control algorithms. With them, you can:

- ease maintenance by animating logic for a single instance.
- protect intellectual property with locking instructions.
- reduce documentation development time.

You can use Add-on Instructions across multiple projects. You can define your instructions, obtain them from somebody else, or copy them from another project.

Once defined in a project, Add-on Instructions behave similarly to the built-in instructions in Logix5000 controllers. They appear on the instruction tool bar for easy access, as do internal RSLogix 5000 software instructions.

| Feature                              | Description                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Save Time                            | With Add-on Instructions, you can combine your most commonly used logic into sets of reusable instructions. You save time when you create instructions for your projects and then share them with others. Add-on Instructions increase project consistency since commonly used algorithms all work in the same manner, regardless of who implements the project. |
| Use Standard Editors                 | You create Add-on Instructions by using one of three RSLogix 5000 software programming editors.  •  Standard Ladder  •  Function Block Diagram  •  Structured Text Once you have created instructions, you can use them in any RSLogix 5000 editor.                                                                                                              |
| Export Add-on Instructions           | You can export Add-on Instructions to other projects as well as copy and paste them from one project to another. Give each instruction a unique name so that you don’t accidentally overwrite another instruction of the same name.                                                                                                                              |
| Add-on InstructionsUse Context Views | Context views let you visualize an instruction’s logic for a specific instant, simplifying online troubleshooting of your Add-on Instructions. Each instruction contains a revision, a change history, and an auto-generated help page.                                                                                                                          |
| Create Custom Help                   | When you create an instruction, you enter information for the description fields in software dialog boxes, information that becomes what is known as Custom Help. Custom Help makes it easier for users to get the help they need when implementing the instructions.                                                                                            |
| Apply Source Protection              | As the creator of Add-on Instructions, you can limit users of your instruction(s) to read-only access, or you can bar access to the internal logic or local parameters used by the instruction(s). This source protection lets you prevent unwanted changes to your instruction(s) and protects your intellectual property.                                      |

## Monitor Controller Status

<!-- image -->

The CompactLogix controller uses Get System Value (GSV) and Set System Value (SSV) instructions to get and set (change) controller data. The controller stores system data in objects. There is no status file, as in the PLC-5 processor.

The GSV instruction retrieves the specified information and places it in the destination. The SSV instruction sets the specified attribute with data from the source.

When you enter a GSV/SSV instruction, the programming software displays the:

- valid object classes.
- object names.
- attribute names.

For the GSV instruction, you can get values for all the available attributes. For the SSV instruction, the software displays only those attributes you are allowed to set.

In some cases, there will be more than one of the same type of object, so you might also have to specify the object name. For example, there can be several tasks in your application. Each task has its own TASK object that you access by the task name.

You can access these object classes:

- AXIS
- CONTROLLER
- CONTROLLERDEVICE
- CST
- DF1
- FAULTLOG
- MESSAGE
- MODULE
- MOTIONGROUP

## Monitor Connections

- PROGRAM
- ROUTINE
- SERIALPORT
- TASK
- WALLCLOCKTIME

If communication with a device in the I/O configuration of the controller does not occur for 100 ms or 4 times the RPI, whichever is less, the communication times out, and the controller produces these warnings:

- The I/O status indicator on the front of the controller flashes green.
- A displays over the I/O configuration folder and the device (s) that has timed out.
- A module fault code is produced, which you can access via:
- – the Module Properties dialog box for the module.
- – a GSV instruction.

## Determine if Device Communication Has Timed Out

If communication times out with at least one device (module) in the I/O configuration of the controller, the I/O status indicator on the front of the controller flashes green.

- The GSV instruction gets the status of the I/O status indicator and stores it in the I\_O\_LED tag.
- If I\_O\_LED equals 2, the controller has lost communication with at least one device.

<!-- image -->

where:

I\_O\_LED is a DINT tag that stores the status of the I/O status indicator on the front of the controller.

## Determine if I/O Module Communication Has Timed Out

If communication times out with a device (module) in the I/O configuration of the controller, the controller produces a fault code for the module.

- The GSV instruction gets the fault code for IO\_Module and stores it in the Module\_Status tag.
- If Module\_Status is any value other than 4, the controller is not communicating with the module.

Figure 21 - I/O Module Communication

<!-- image -->

Select a System Overhead Time Slice Percentage

## Interrupt the Execution of Logic and Execute the Fault Handler

To interrupt the execution of logic and execute the fault handler, perform this procedure.

1. In the Controller Organizer of RSLogix 5000 programming software, right-click the module and choose Properties.

<!-- image -->

The Module Properties dialog box appears.

<!-- image -->

2. Click the Connection and check Major Fault On Controller If Connection Fails While in Run Mode checkbox.
3. Click OK.
4. Develop a routine for the Controller Fault Handler.

With RSLogix 5000 programming software, you can specify a percentage for the system overhead time slice. A Logix5000 controller communicates with other devices (I/O modules, controllers, HMI terminals) at either a specified rate (scheduled) or when there is processing time available to service the communication (unscheduled).

Service communication is any communication that you do not configure through the I/O configuration folder of the project.

- The system overhead time slice specifies the percentage of time (excluding the time for periodic or event tasks) that the controller devotes to service communication.
- The controller performs service communication for up to 1 ms at a time and then resumes the continuous task.

To select a system overhead percentage, perform this procedure.

1. In the Controller Organizer of RSLogix 5000 programming software, right-click on your controller and choose Properties.

<!-- image -->

The Controller Properties dialog box appears.

<!-- image -->

2. Click the Advanced tab.
3. From the System Overhead Time Slice menu, choose a percentage.

System overhead time slice functions include:

- communicating with programming and HMI devices, such as RSLogix 5000 software.
- responding to messages.
- sending messages.

The controller performs system overhead functions for up to 1 millisecond at a time. If the controller completes the overhead functions in less than one millisecond, it resumes the continuous task.

Periodic

System Overhead

Continuous Task

## Legend:

0

Elapsed Time (ms)

The interruption of a periodic task increases the elapsed time (clock time) between the execution of system overhead functions.

<!-- image -->

As the system overhead time slice percentage increases, time allocated to executing the continuous task decreases. If there are no communication for the controller to manage, the controller uses the communication time to execute the continuous task. While increasing the system overhead percentage does increase communication performance, it also increases the amount of time it takes to execute a continuous task, increasing overall scan time.

|                   | V15 and Lower   | V15 and Lower   | V16 and Higher   | V16 and Higher   |
|-------------------|-----------------|-----------------|------------------|------------------|
| Time Slice (SOTS) | Comms           | Continuous Task | Comms            | Continuous Task  |
| 10%               | 1 msec          | 9 msec          | 1 msec           | 9 msec           |
| 20%               | 1 msec          | 4 msec          | 1 msec           | 4 msec           |
| 33%               | 1 msec          | 2 msec          | 1 msec           | 2 msec           |
| 50%               | 1 msec          | 1 msec          | 1 msec           | 1 msec           |
| 66%               | 1 msec          | 0.5 msec        | 2 msec           | 1 msec           |
| 80%               | 1 msec          | 0.2 msec        | 4 msec           | 1 msec           |
| 90%               | 1 msec          | 0.1 msec        | 9 msec           | 1 msec           |

At a time slice of 10%, system overhead interrupts the continuous task every 9 ms of continuous task time.

Task executes.

Task is interrupted (suspended).

1 ms 1 ms

9 ms

5

9 ms

10

15

20

25

If you use the default time slice of 20%, the system overhead interrupts the continuous task every 4 ms.

<!-- image -->

If you increase the time slice to 50%, the system overhead interrupts the continuous task every 1 ms.

<!-- image -->

If the controller contains only a periodic task(s), the system overhead time slice value has no effect. System overhead runs whenever a periodic task is not running.

Elapsed Time (ms)

<!-- image -->

## PhaseManager Overview

<!-- image -->

## Configure PhaseManager Application

This chapter explains how to configure a PhaseManager™ application.

The PhaseManager option of RSLogix 5000 programming software gives you a state model for your equipment.

| Topic                                      |   Page |
|--------------------------------------------|--------|
| PhaseManager Overview                      |    113 |
| State Model Overview                       |    114 |
| Compare PhaseManager to Other State Models |    117 |
| Minimum System Requirements                |    118 |
| Equipment Phase Instructions               |    118 |

For additional information, consult PhaseManager User Manual, publication LOGIX-UM001

PhaseManager lets you add equipment phases to your controller. An equipment phase helps you lay out your code in sections that are easier to write, find, follow, and change.

|                 | Term Description                                                                                                                                                                                                                                                                                                   |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Equipment phase | •  As with a program, an equipment phase is run in a task and is given a set of routines and tags. •  Unlike a program, an equipment phase runs by a state model and lets you do one activity.                                                                                                                     |
|                 | State model A state model divides the operating cycle of your equipment into a series of states. Each state is an instant in the operation of the equipment. It's the actions or conditions of the equipment at a given time. The state model of an equipment phase is similar to the S88 and PackML state models. |
| State machine   | •  An equipment phase includes an embedded state machine that:  •  calls the main routine (state routine) for an acting state.  •  manages the transitions between states with minimal coding.  •  makes sure that the equipment goes from state to state along an allowable path.                                 |
|                 | PHASE tag When you add an equipment phase, RSLogix 5000 programming software makes a tag, using the PHASE data type.                                                                                                                                                                                               |

Figure 22 - PhaseManager Overview

<!-- image -->

## State Model Overview

A state model divides the operating cycle of your equipment into a series of states. Each state is an instant in the operation of the equipment, an action or condition at a given time.

In a state model, you define what your equipment does under different conditions, such as run, hold, and stop. You don't need to use all the states for your equipment. Use only needed states.

Table 27 - Types of States

| State   | Description                                                                                                                           |
|---------|---------------------------------------------------------------------------------------------------------------------------------------|
| Acting  | Does something or several things for a certain time or until certain conditions are met. An acting state runs one time or repeatedly. |
|         | Waiting Shows that certain conditions are met and the equipment is waiting for the signal to go to the next state.                    |

Figure 23 - PhaseManager States

<!-- image -->

With a state model, you define the behavior of your equipment and put it into a brief functional specification. In this way you show what happens and when it happens.

| State Question To Be Asked                                                           |
|--------------------------------------------------------------------------------------|
| Stopped What happens when you turn on power?                                         |
| Resetting How does the equipment get ready to run?                                   |
| Idle How do you tell that the equipment is ready to run?                             |
| Running What does the equipment do to make product?                                  |
| Holding How does the equipment temporarily stop making product without making scrap? |
| Held How do you tell if the equipment is safely holding?                             |
| Restarting How does the equipment resume production after holding?                   |
| Complete How do you tell when the equipment has finished what it had to do?          |
| Stopping What happens during a normal shutdown?                                      |
| Aborting How does the equipment shut down if a fault or failure happens?             |
| Aborted How do you tell if the equipment is safely shut down?                        |

## How Equipment Changes States

The arrows in the state model show how your equipment can transition from one state to another.

- Each arrow is called a transition.
- A state model lets the equipment make only certain transitions. This transition restriction standardizes equipment behavior so that another piece of equipment using the same model will behave the same way.

Table 28 - PhaseManager Transitions Overview

<!-- image -->

Table 29 - PhaseManager Transition Types

| Transition Type   | Description                                                                                                                                                                                                                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | Command A command tells the equipment to start doing something or do something different. For example the operator pushes the start button to start production and the stop button to halt production. PhaseManager uses these commands: •  Reset •  Start •  Stop •  Hold •  Restart •  Abort                  |
|                   | Done Equipment goes to a waiting state when it has completed a task. You don’t have to command equipment to stop. Instead, set up your code to signal when a task is complete.                                                                                                                                  |
|                   | Fault A fault tells you that something unusual has occurred. Set up your code to find and take action for faults. Suppose you want your equipment to shut down as fast as possible in case of a certain fault. In that case, set up your code to look for that fault and give the abort command if it finds it. |

## Current State of Equipment Phase

## Manually Change States

With RSLogix 5000 programming software, you can monitor and command an equipment phase. To manually change states, perform this procedure.

<!-- image -->

## Compare PhaseManager to Other State Models

Table 30 - State Model Comparisons

| S88                | PackML             | PhaseManager                   |
|--------------------|--------------------|--------------------------------|
| Idle               | Starting Ready   | Resetting Idle               |
| Running Complete | Producing          | Running Complete             |
| Pausing Paused   | Standby            | Subroutines and/or breakpoints |
| Holding Held     | Holding Held     | Holding Held                 |
| Restarting         | None               | Restarting                     |
| Stopping Stopped | Stopping Stopped | Stopping Stopped             |
| Aborting Aborted | Aborting Aborted | Aborting Aborted             |

You can compare PhaseManager's state models to other common state models.

## Minimum System Requirements

## Equipment Phase Instructions

To develop PhaseManager programs, you need:

- a CompactLogix controller with firmware revision 16.0 or later.
- a communication path to the controller.
- RSLogix 5000 programming software, version 15.0 or later.

To enable PhaseManager support, you need the full or professional editions of RSLogix 5000 programming software or the optional PhaseManager add-on (9324-RLDPMENE) to your RSLogix 5000 programming software package.

With CompactLogix controllers, you can issue many ladder diagram (LD) and structured text (ST) instructions to begin various equipment phases.

| Instruction Code   | Instruction                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSC                | Signal a phase that the state routine is complete so go to the next state                                                                                                                                    |
| PCMD               | Change the state or substate of a phase                                                                                                                                                                      |
| PFL                | Signal a failure for a phase                                                                                                                                                                                 |
| PCLF               | Clear the failure code of a phase                                                                                                                                                                            |
| PXRQ               | Initiate communication with RSBizWare Batch software                                                                                                                                                         |
| PRNP               | Clear the NewInputParameters bit of a phase                                                                                                                                                                  |
| PPD                | Set up breakpoints within the logic of a phase                                                                                                                                                               |
| PATT               | Take ownership of a phase to either: •  prevent another program or RSBizWare Batch software from commanding a phase or •  make sure another program or RSBizWare Batch software does not already own a phase |
| PDET               | Relinquish ownership of a phase                                                                                                                                                                              |
| POVR               | Override a command                                                                                                                                                                                           |

## Use a CompactFlash Card

This chapter explains how to use a CompactFlash card for nonvolatile memory or data storage.

| Topic                                                    |   Page |
|----------------------------------------------------------|--------|
| Use a CompactFlash Card to Load/Store a User Application |    122 |
| Use a CompactFlash Card for Data Storage                 |    125 |
| Read and Write User Data to the CompactFlash Card        |    125 |

CompactLogix controllers only support nonvolatile storage through CompactFlash removable media. CompactLogix controllers support the 1784-CF128 Industrial CompactFlash memory cards for nonvolatile memory.

CompactLogix controllers 1769- L31, 1769-L32E, 1769-L32C, 1769-L35E, and 1769-L35CR can save and restore user applications to CompactFlash memory.

Of the 1769 CompactLogix controllers, only the 1769-L32E and 1769-L35E can store user data (for example, a recipe) to the CompactFlash card during runtime. This feature is supported on 1769-L35E controllers with serial numbers starting with SS0OR9GE, or greater, and 1769-L32E controllers with serial numbers starting with SS0QZ000, or greater. To find the controller's serial number, look on the label on the outside of the controller, or access it electronically in RSLinx software or RSLogix 5000 programming software. You must use firmware version V16, or greater.

## Locate the Controller Serial Number in RSLinx Software

To find the controller's serial number in RSLinx software, follow these steps.

1. Open RSLinx software and from the Communication pull-down menu, choose RSWho.

<!-- image -->

2. Right-click on the controller in the RSWho browse window and select Device Properties.

<!-- image -->

The Device Properties dialog box displays, showing the serial number.

<!-- image -->

## Locate the Controller Serial Number

Via the RSLogix 5000 Project

To find the controller's serial number in your RSLogix 5000 project when using ladder logic or structured text, use the Get System Value (GSV) instruction to obtain the value of the Serial Number attribute of the ControllerDevice object.

<!-- image -->

The value can be shown in RSLogix 5000 programming software's data monitor. When the style is set to Hex, the displayed value is the same as shown in RSLinx software.

<!-- image -->

- TIP

If the user wants to access the serial number programmatically, additional logic is needed to obtain the serial number's value.

## Via RSLogix 5000 Programming Software

To find the controller's serial number in RSLogix programming software, follow these steps.

1. In the controller organizer, right-click on the controller and select Properties from the pull-down menu.
2. The Controller Properties dialog box displays.
2. Click the Advanced tab to see the serial number.

## Use a CompactFlash Card to Load/Store a User Application

You can load the user application/project from nonvolatile memory/ CompactFlash to the user memory of the controller:

- on every power-up.
- on corrupt memory.
- anytime through RSLogix 5000 programming software.

<!-- image -->

ATTENTION: Fault conditions can occur if the controller types do not match. For example, if the CompactFlash user program and controller firmware were created for a 1769-L35E controller, and then an attempt was made to load that program and/or firmware into a 1769-L32E controller.

## IMPORTANT

<!-- image -->

## IMPORTANT

The user application and firmware version on the CompactFlash card is loaded into the controller. If the contents of the CompactFlash card are a different revision than the revision that is on the controller, then the controller will be updated to the revision on the CompactFlash card.

ATTENTION: Do not remove the CompactFlash card while the controller is reading from or writing to the card, as indicated by a flashing green CF status indicator. Doing so could corrupt the data on the card or in the controller, as well as corrupt the latest firmware in the controller.

CompactFlash card memory stores the contents of the user memory when you store the project.\

- Changes made after you store the project are not reflected in CompactFlash card memory.
- If you change the project but do not store those changes, you overwrite them when you load the project from the CompactFlash card. If this occurs, you have to upload or download the project to go online.
- If you want to store changes such as online edits, tag values, or a ControlNet network schedule, store the project again after you make the changes.

When you store a project to a 1784-CF128 Industrial CompactFlash memory card, the controller formats the card, if required.

## Manually Change Which Project Loads

A CompactFlash card stores multiple projects. By default, the controller loads the project that you most recently stored, according to the load options of that project.

## IMPORTANT

Be aware that when loading a different project, the firmware revisions must be the same.

To assign a different project to load from the CompactFlash card, edit the Load.xml file on the card.

<!-- image -->

.

1. To change which project loads from the card, open Load.xml. Use a text editor to open the file.
2. Edit the name of the project that you want to load.
- Use the name of an XML file that is in the CurrentApp folder.
- In the CurrentApp folder, a project is comprised of an XML file and a P5K file.

3

.

## Manually Change the Load Parameters

When you store a project to a CompactFlash card, you define:

- when the project is to load (On Power Up, On Corrupt Memory, User Initiated).
- mode to which to set the controller (if the keyswitch is in REM and the load mode is not User Initiated).

## IMPORTANT

Be aware that when loading a different project, the firmware revisions must be the same.

To assign a different project to load from the CompactFlash card, edit the Load.xml file on the card.

<!-- image -->

1. To change the load parameters for a project, open the XML file with the same name as the project. Use a text editor to open the file.

&lt;?xml version="1.0" encoding="uTF-8" ?&gt;

- &lt;Controller&gt;
- -&lt;ExecutiveLoadoption&gt;
- &lt;ExecFile&gt;\Logix\CurrentApp\Executive.bin&lt;/ExecFile&gt; &lt;/ExecutiveLoadOption&gt;
- -&lt;ProgramLoadOption&gt;
- 2 . &lt;ProgramLoadMode&gt;CORRUPT\_RAM&lt;/ProgramLoadMode&gt; &lt;LoadFile&gt;\Logix\CurrentApp\Rev\_12\_Project\_2.p5k&lt;/LoadFile&gt;
- &lt;/ProgramLoadOption&gt;
- -&lt;ControllerModeOption&gt;

&lt;ControllerMode&gt;RuN&lt;/ControllerMode&gt;

- &lt;/ControllerModeOption&gt;

&lt;/Controller&gt;

## Use a CompactFlash Card for Data Storage

## Read and Write User Data to the CompactFlash Card

2. Edit the Load Image option of the project.
3. Edit the Load Mode option of the project (doesn't apply if the Load Image option is User Initiated).

| If you want to set the Load Image option to   | Then enter     |
|-----------------------------------------------|----------------|
| On Power Up                                   | ALWAYS         |
| On Corrupt Memory                             | CORRUPT_RAM    |
| User Initiated                                | USER_INITIATED |

| If you want to set the Load Mode option to   | Then enter   |
|----------------------------------------------|--------------|
| Program (Remote Only)                        | PROGRAM      |
| Run (Remote Only)                            | RUN          |

You can also store data to the CompactFlash memory card.

## For example:

- A PanelView terminal changes tag values in a controller project. If power to the controller is lost (and the controller is not battery backed up), the program running in the controller, along with any values that were changed by the PanelView terminal, will be lost. Use the CompactFlash file system and logic in the project to store tag values as they change. When the project reloads from the CompactFlash card, it can check the CompactFlash card for any saved tag values and reload those into the project.
- Store a collection of recipes on the CompactFlash card. When you need to change a recipe, program the controller to read data for the new recipe from a CompactFlash card.
- Program the controller to write data logs at specific time intervals.

A sample controller project that reads and writes from a CompactFlash card is available with RSLogix 5000 Enterprise programming software.

## Notes:

## Battery Handling

## Maintain the Battery

This chapter explains how to maintain your battery.

| Topic Page                        |
|-----------------------------------|
| Battery Handling 127              |
| Check If the Battery Is Low 128   |
| Estimate 1769-BA Battery Life 128 |
| Store Lithium Batteries 129       |
| Battery Removal 129               |

CompactLogix controllers support the 1769-BA battery.

<!-- image -->

ATTENTION: The 1769-BA battery is the only battery you can use with the CompactLogix controllers. The 1747-BA battery is not compatible with the CompactLogix controllers and may cause problems.

Lithium batteries are primary (not rechargeable) cells that give extended memory support for Rockwell Automation products.

<!-- image -->

ATTENTION: This product contains a sealed lithium battery that may need to be replaced during the life of the product.

At the end of its life, the battery contained in this product should be collected separately from any unsorted municipal waste.

The collection and recycling of batteries helps protect the environment and contributes to the conservation of natural resources as valuable materials are recovered.

<!-- image -->

## Check If the Battery Is Low

## Estimate 1769-BA Battery Life

Table 32 - Battery Life Estimations

| Time On/Off                         | At 25  ° C (77  ° F)                                                      | At 40  ° C (104  ° F)                                                     | At 60  ° C (140  ° F)                                                     |
|-------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Always off                          | 14 months                                                                 | 12 months                                                                 | 9 months                                                                  |
| On 8 hours per day 5 days per week  | 18 months                                                                 | 15 months                                                                 | 12 months                                                                 |
| On 16 hours per day 5 days per week | 26 months                                                                 | 22 months                                                                 | 16 months                                                                 |
| Always On                           | There is almost no drain on the battery when the controller is always on. | There is almost no drain on the battery when the controller is always on. | There is almost no drain on the battery when the controller is always on. |

The battery indicator (BAT) warns when the battery is low. Once the controller is powered down, the battery retains controller memory as long as the BAT indicator remains on. Temperature dictates how long the BAT indicator remains on.

Figure 24 - Battery Status Indicator

<!-- image -->

Table 31 - BAT Indicator Duration

| Temperature    | Duration   |
|----------------|------------|
| 60 °C (140 °F) | 8 days     |
| 25 °C (77 °F)  | 25 days    |

Certain conditions affect typical battery life.

## Store Lithium Batteries

## Battery Removal

<!-- image -->

ATTENTION: Follow these general rules to store your batteries.

- Store batteries in a cool, dry environment. We recommend 25 °C (77 °F) with 40…60% relative humidity.
- Regularly monitor the temperature and humidity of the storage area.
- Use a first-in/first-out system for handling stored batteries.
- Store in the original containers away from flammable materials.
- Keep track of storage time. Reference storage time to the date of manufacture.
- Do not store batteries longer than 10 years.
- Do not store used batteries longer than 3 months before disposal.
- Clearly mark the contents of the storage area.
- Place a Lith-X or Class D Powder fire extinguisher in a readily accessible area in or around the storage area.
- Ventilate and protect the storage area against fire. You must have a system that automatically detects and extinguishes fires and automatically activates an alarm signal.
- Do not smoke in the storage area.
- You may store batteries for up to 30 days between -45…85 °C (-49…185 °F) such as during transportation. Do not store in temperatures above 85° C (185 °F).
- To avoid leakage or other hazards, do not store batteries above 60° C for more than 30 days.
- The rate of capacity loss increases as storage temperature increases.

Table 33 - Storage Temperatures for 1769-BA Lithium Batteries

| Storage Temperature Capacity Loss                              |
|----------------------------------------------------------------|
| 40 °C (104 °F) for 5 years Loses up to 4% of original capacity |
| 60 °C (140 °F) Loses 2.5 % of capacity each year               |

<!-- image -->

WARNING: When you connect or disconnect the battery, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

## Additional Resources

For additional information, consult this publication.

| Resource                                              | Description                                                                          |
|-------------------------------------------------------|--------------------------------------------------------------------------------------|
| Guidelines for Handling Batteries, publication AG 5-4 | Detailed information on battery-handling procedures for the 1769-BA lithium battery. |

## 1769-L3xx Controllers Status Indicators

## Status Indicators

This appendix explains how to interpret the status indicators on your CompactLogix controllers.

| Topic                                   |   Page |
|-----------------------------------------|--------|
| 1769-L3xx Controllers Status Indicators |    131 |
| RS-232 Serial Port Status Indicators    |    133 |
| ControlNet Indicators                   |    133 |
| EtherNet/IP Indicators                  |    135 |

These are the 1769-L3xx CompactLogix controller status indicators.

|       | Indicator Condition   | Interpretation                                                                                                          |
|-------|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
| RUN   | Off                   | The controller is in program or test mode.                                                                              |
| RUN   | Steady green          | The controller is in run mode.                                                                                          |
| FORCE | Off                   | •  No tags contain I/O force values. •  I/O forces are inactive (disabled).                                             |
| FORCE | Steady amber          | •  I/O forces are active (enabled). •  I/O force values may or may not exist.                                           |
| FORCE | Flashing amber        | One or more input or output addresses have been forced to an On or Off condition, but the forces have not been enabled. |
| BAT   | Off                   | The battery supports memory.                                                                                            |
| BAT   | Steady red            | •  The battery is: •  not installed. •  95% discharged and should be replaced.                                          |
| I/O   | Off                   | •  There are no devices in the I/O configuration of the controller. •  The controller does not contain a project.       |
| I/O   | Steady green          | The controller is communicating with all the devices in its I/O configuration.                                          |
| I/O   | Flashing green        | One or more devices in the I/O configuration of the controller are not responding.                                      |
| I/O   | Flashing red          | •  The controller is not communicating with any devices. •  The controller is faulted.                                  |

<!-- image -->

| Indicator Condition Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Indicator Condition Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Indicator Condition Interpretation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OK Off No power is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | OK Off No power is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | OK Off No power is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| •  The controller requires a firmware update. •  A major recoverable fault occurred on the controller. To clear the fault, perform this procedure. a. Turn the controller keyswitch from PROG to RUN to PROG. b. Go online with RSLogix 5000 programming software. •  A nonrecoverable major fault occurred on the controller. In this case, the controller: a. initially displays a steady red status indicator. b. resets itself. c. clears the project from its memory. d. sets the status indicator to flashing red. e. produces a major recoverable fault. f. generates a fault code in the RSLogix 5000 project. The fault code displayed in RSLogix 5000 programming software, and the subsequent fault recovery method, depends on whether you have installed a CompactFlash card in the controller. | •  The controller requires a firmware update. •  A major recoverable fault occurred on the controller. To clear the fault, perform this procedure. a. Turn the controller keyswitch from PROG to RUN to PROG. b. Go online with RSLogix 5000 programming software. •  A nonrecoverable major fault occurred on the controller. In this case, the controller: a. initially displays a steady red status indicator. b. resets itself. c. clears the project from its memory. d. sets the status indicator to flashing red. e. produces a major recoverable fault. f. generates a fault code in the RSLogix 5000 project. The fault code displayed in RSLogix 5000 programming software, and the subsequent fault recovery method, depends on whether you have installed a CompactFlash card in the controller. | •  The controller requires a firmware update. •  A major recoverable fault occurred on the controller. To clear the fault, perform this procedure. a. Turn the controller keyswitch from PROG to RUN to PROG. b. Go online with RSLogix 5000 programming software. •  A nonrecoverable major fault occurred on the controller. In this case, the controller: a. initially displays a steady red status indicator. b. resets itself. c. clears the project from its memory. d. sets the status indicator to flashing red. e. produces a major recoverable fault. f. generates a fault code in the RSLogix 5000 project. The fault code displayed in RSLogix 5000 programming software, and the subsequent fault recovery method, depends on whether you have installed a CompactFlash card in the controller. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Code Condition Fault recovery method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 60 CompactFlash card is not installed. 61 CompactFlash is installed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 1. Clear the fault. 2. Download the project. 3. Change to Remote Run/Run mode. If the problem persists: 1. Before you cycle power to the controller, record the state of the OK and RS232 status indicators. 2. Contact Rockwell Automation support. See the back cover. 1. Clear the fault. 2. Download the project. 3. Change to Remote Run/Run mode. If the problem persists, contact Rockwell Automation support. See                                                                                                                                                                                                                                                                                                                                                                                    |
| Steady red The controller detected a nonrecoverable major fault, so it cleared the project from memory. To recover from a major fault, perform this procedure. 1. Cycle power to the chassis. 2. Download the project. 3. Change to Run mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Steady red The controller detected a nonrecoverable major fault, so it cleared the project from memory. To recover from a major fault, perform this procedure. 1. Cycle power to the chassis. 2. Download the project. 3. Change to Run mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Steady red The controller detected a nonrecoverable major fault, so it cleared the project from memory. To recover from a major fault, perform this procedure. 1. Cycle power to the chassis. 2. Download the project. 3. Change to Run mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Steady green Controller is OK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Steady green Controller is OK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Steady green Controller is OK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Flashing green The controller is storing or loading a project to or from nonvolatile memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Flashing green The controller is storing or loading a project to or from nonvolatile memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Flashing green The controller is storing or loading a project to or from nonvolatile memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## CompactFlash Indicator

## RS-232 Serial Port Status Indicators

## ControlNet Indicators

This is the CompactFlash card status indicator present on all CompactLogix controllers.

<!-- image -->

ATTENTION: Do not remove the CompactFlash card while the controller is reading from or writing to the card, as indicated by a flashing green CF status indicator. This could corrupt the data on the card or in the controller, as well as corrupt the latest firmware in the controller.

.

| Indicator Condition Interpretation                                                 |
|------------------------------------------------------------------------------------|
| CF Off There is no activity.                                                       |
| Flashing green The controller is reading from or writing to the CompactFlash card. |
| Flashing red CompactFlash card does not have a valid file system.                  |

These are the RS-232 serial port status indicators present on all CompactLogix controllers.

|                     | Indicator Condition Interpretation                                              |
|---------------------|---------------------------------------------------------------------------------|
|                     | DCH0 Off Channel 0 configuration differs from the default serial configuration. |
|                     | Steady green Channel 0 has the default serial configuration.                    |
|                     | CH0 Off No RS-232 activity.                                                     |
|                     | Flashing green RS-232 activity.                                                 |
| CH1 (1769-L31 only) | Off No RS-232 activity.                                                         |
| CH1 (1769-L31 only) | Flashing green RS-232 activity.                                                 |

The ControlNet indicators are only on the 1769-L32C and 1769L35CR controllers.

Use these indicators to determine how your CompactLogix 1769-L32C or 1769L35CR controller is operating on the ControlNet network:

- Module Status
- Network Status

These indicators provide information about the controller and network when the controller is connected to ControlNet via the BNC connectors.

Table 34 - ControlNet Network Status Indicator States

| Status Indicator State Interpretation                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Steady The indicator is on continuously in the defined state.                                                                                                         |
| Alternating When viewed together, two indicators alternate between two defined states; the two indicators are always in opposite states, out of phase.                |
| Flashing  When viewed independent of another, an indicator alternates between the two defined states; if both indicators are flashing, they flash together, in phase. |

## IMPORTANT

Keep in mind that the Module Status indicator reflects the module state (for example, self-test, firmware update, normal operation but no connection established). The network status indicators, A and B, reflect network status. Remember that the host is able to engage in local messaging with the card although it is detached from the network. Therefore, the Module Status indicator is flashing green if the host has successfully started the card. Note, however, that until the host removes reset, all communication port status indicators.

When you view the indicators, always view the Module Status indicator first to determine the state of the communication port. This information may help you to interpret the network indicators. As a general practice, view all indicators (Module Status and Network Status) together to gain a full understanding of the daughtercard's status.

## Module Status (MS) Indicator

These are the ControlNet module indicators.

| Indicator Condition                                                                                                         | Recommended Action                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off  The controller has no power.                                                                                           | Apply power.                                                                                                                                                                      |
| The controller is faulted.                                                                                                  | Make sure that the controller is firmly seated in the slot.                                                                                                                       |
| Steady red A major fault has occurred on the controller.                                                                    | 1. Cycle power. 2. If the problem persists, replace the controller.                                                                                                               |
| Flashing red A minor fault has occurred because a firmware update is in progress. Normal operation - No action is required. |                                                                                                                                                                                   |
| A node address switch change has occurred. The controller’s node address switches may have been changed since power-up.     | Change the node address switches back to the original setting. The module will continue to operate properly.                                                                      |
| The controller uses invalid firmware.                                                                                       | Update the controller firmware with the ControlFlash Update utility.                                                                                                              |
| The controller’s node address duplicates that of another device. 1. Remove power.                                           | 2. Change the node address to a unique setting. 3. Reapply power.                                                                                                                 |
| Steady green Connections are established.                                                                                   | Normal operation - No action is required.                                                                                                                                         |
| Flashing green No connections are established.                                                                              | Establish connections, if necessary.                                                                                                                                              |
| Flashing red/green The controller is diagnosing a problem.                                                                  | Wait briefly to see if problem corrects itself. If problem persists, check the host. If the daughtercard cannot communicate with the host, the card may remain in self-test mode. |

## Network Channel Indicators

These are the ControlNet network channel indicators.

Channel B is only labelled on the 1769-L35CR controller. The 1769-L32C controller only has channel A but uses the second indicator in some status indicator patterns as described below.

| Indicator  Condition Recommended Action                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off  A channel is disabled.  Program network for redundant media, if necessary.                                                                                                                                                                      |
| Steady green  Normal operation is occurring.  Normal operation - No action is required.                                                                                                                                                              |
| Flashing green/off Temporary network errors have occurred.  1. Check media for broken cables, loose connectors, and missing terminators. 2. If condition persists, refer to the ControlNet Planning and Installation Manual, publication 1786-6.2.1. |
| The node is not configured to go online.  Make sure the network keeper is present and working and the selected (1) address is less or equal to the UMAX (1) .                                                                                                                                                                                                                                                      |
| Flashing red/off Media fault has occurred. 1. Check media for broken cables, loose connectors, and missing terminators. 2. If condition persists, refer to the ControlNet Planning and Installation Manual, publication 1786-6.2.1.                  |
| No other nodes are present on the network. Add other nodes to the network.                                                                                                                                                                           |
| Flashing red/green The network is configured incorrectly. Reconfigure the ControlNet network so that UMAX is greater than or equal to the card’s node address.                                                                                       |
| Off You should check the MS indicators. Check the MS indicators.                                                                                                                                                                                     |
| Steady red The controller is faulted. 1. Cycle power. 2. If the fault persists, contact your Rockwell Automation representative or distributor.                                                                                                      |
| Alternating red/green The controller is performing a self test. Normal operation - No action is required.                                                                                                                                            |
| Alternating red/off The node is configured incorrectly. Check the card’s network address and other ControlNet configuration parameters.                                                                                                              |

## EtherNet/IP Indicators

The EtherNet/IP indicators are only on 1769-L32E and 1769-L35E controllers.

## Module Status (MS) Indicator

These are the EtherNet/IP module indicators.

| Indicator Condition                                                                                                  | Recommended Action                                                                        |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Off  The controller does not have power.                                                                             | Check the controller power supply.                                                        |
| Flashing green The port is in standby mode; it does not have an IP address and is operating in BOOTP mode.           | Verify that the BOOTP server is running.                                                  |
| Steady green The port is operating correctly.                                                                        | Normal operation - No action is required.                                                 |
| Steady red The controller is holding the port in reset or the controller has faulted. 1. Clear the controller fault. | 2. If the fault will not clear, replace the controller.                                   |
| The port is performing its power-up self test.                                                                       | Normal operation - No action is required.                                                 |
| A nonrecoverable fault has occurred.                                                                                 | 1. Cycle power to the controller. 2. If the fault will not clear, replace the controller. |
| Flashing red The port firmware is being updated.                                                                     | Normal operation - No action is required.                                                 |

## Network Status (NS) Indicator

These are the EtherNet/IP network indicators.

| Indicator Condition                                                                                                       | Recommended Action                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off  The port is not initialized; it does not have an IP address and is operating in BOOTP mode.                          | Verify that the BOOTP server is running.                                                                                                             |
| Flashing green The port has an IP address, but no CIP connections are established.                                        | •  If no connections are configured, no action is required. •  If connections are configured, check connection originator for connection error code. |
| Steady green The port has an IP address and CIP connections (Class 1 or Class 3) are established.                         | Normal operation - No action is required.                                                                                                            |
| Steady red The port has detected that the assigned IP address is already in use. Verify that all IP addresses are unique. |                                                                                                                                                      |
| Flashing red/green The port is performing its power-up self test.                                                         | Normal operation - No action is required.                                                                                                            |

## Link Status (LNK) Indicator

| Indicator Condition                                                                                               | Recommended Action                                                                           |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Off  The port is not connected to a powered Ethernet device. Therefore, the port cannot communicate on Ethernet.  | 1. Verify that all Ethernet cables are connected. 2. Verify that Ethernet switch is powered. |
| Flashing green The port is performing its power-up self-test.                                                     | Normal operation - No action is required.                                                    |
| The port is communicating on Ethernet.                                                                            | Normal operation - No action is required.                                                    |
| Steady green The port is connected to a powered Ethernet device. Therefore, the port can communicate on Ethernet. | Normal operation - No action is required.                                                    |

## Dynamic Memory Allocation in CompactLogix Controllers

This appendix explains the dynamic allocation of memory in CompactLogix controllers.

| Topic                   |   Page |
|-------------------------|--------|
| Messages                |    138 |
| RSLinx Tag Optimization |    138 |
| Trends                  |    139 |
| DDE/OPC Topics          |    139 |

Certain operations cause the controller to dynamically allocate and remove useravailable memory, affecting the space available for program logic. As these functions become active, memory is allocated. Memory is then removed when these functions become inactive.

Operations that dynamically allocate memory are:

- messages.
- connections to processors with RSLogix 5000 programming software.
- RSLinx tag optimization.
- trends.
- DDE/OPC topics.

<!-- image -->

## Messages

## RSLinx Tag Optimization

Messages come in and go out of the controller via the Ethernet, ControlNet, and serial ports, causing memory allocation. The memory allocations for messages destined to I/O are accounted for in these allocations. To prevent message instructions from using too much memory, do not send messages simultaneously.

Table 35 - Message Types

| Message Path   | Connection Established? Memory Allocated                                    |            |
|----------------|-----------------------------------------------------------------------------|------------|
|                | ControlNet Port Incoming Yes - The message is connected.                    | 1200 bytes |
|                | No - The message is unconnected.                                            | 1200 bytes |
|                | Outgoing All outgoing messages whether connected or unconnected             | 1200 bytes |
|                | Ethernet Port Incoming Yes - The message is connected.                      | 1200 bytes |
|                | No - The message is unconnected.                                            | 1200 bytes |
|                | Outgoing All outgoing messages whether connected or unconnected             | 1200 bytes |
|                | Serial Port Incoming All incoming messages whether connected or unconnected | 1200 bytes |
|                | Outgoing All outgoing messages whether connected or unconnected             | 1200 bytes |

With tag optimization, trend objects, trend drivers, and connections allocate memory.

Table 36 - Tag Functions

| Item  Description                                                                                                                 | Memory Allocated   |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Trend Object Object is created in the controller to group the requested tags. One trend object can handle approximately 100 tags. | 80 bytes           |
| Trend Driver Drive is created to communicate with the trend object. 36 bytes                                                      |                    |
| Connection Connection is created between the controller and RSLinx software.                                                      | 1200 bytes         |

| EXAMPLE   | To monitor 100 points: 100 points x 36 bytes = 3600 bytes (Trend Driver) 3600 (Trend Driver) + 80 (Trend Object) + 1200 (Connection) = approximately 4000 bytes We estimate that one tag consumes about 40 bytes of memory.   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Trends

## DDE/OPC Topics

Each trend created in a controller creates a trend object and allocates a buffer for logging.

Table 37 - Controller Trends

| Item         | Memory Allocated   |
|--------------|--------------------|
| Trend Object | 80 bytes           |
| Log Buffer   | 4000 bytes         |

A DDE/OPC topic uses connections based on these variables:

- Maximum number of messaging connections per PLC controller configured in RSLinx software
- Number of connections needed to optimize throughput
- Configuration of RSLinx software to use connections for writing to a ControlLogix processor

## IMPORTANT

These variables are per path. For example, if you set up two different DDE/OPC topics, with different paths to the same controller, the variables limit the connections for each path. Therefore, if you have a limit of 5 connections, it is possible to have 10 connections, with 5 over each path.

## Specify Connections per PLC Controller

To specify the maximum messaging connections per PLC controller, perform this procedure.

1. In RSLinx programming software, from the Communication pull-down menu, choose Configure CIP Options.

<!-- image -->

The Configure CIP Options dialog box appears.

<!-- image -->

2. In the Max. Messaging Connections per PLC field, enter the maximum number of read connections you want a particular workstation to make to a ControlLogix controller.
3. Click OK.

Specify Number of Connections Needed to Optimize Throughput

To specify the number of connections needed to optimize throughput, perform this procedure.

1. Repeat step 1 from the previous procedure.
2. In the Configure CIP Options dialog box, click the Use Connections for Writes to ControlLogix processor checkbox.

IMPORTANT

Once you have selected this feature, you cannot limit the number of connections established.

## Number of Connections Needed to Optimize Throughput

RSLinx software only opens the number of connections required to optimize throughput. For example, if you have one tag on scan, but have configured RSLinx software to allow five connections as the maximum number of connections, RSLinx software only opens one connection for the tag. Conversely, if you have thousands of tags on scan and limit the maximum number of CIP connections to five, RSLinx software cannot establish more than five connections to the CompactLogix controller. RSLinx software then funnels all of the tags through those five available connections.

## View the Number of Open Connections

To view the number of open connections made from your workstation to the CompactLogix controller, perform this procedure.

1. In RSLinx programming software, from the Communication pull-down menu, choose CIP Diagnostics.

<!-- image -->

The CIP Diagnostics dialog box appears.

<!-- image -->

2. Click the Connections tab.

Here you see an itemized list of open connections.

## 3. Click the Dispatching tab.

<!-- image -->

In the Connections Established box you see the total number of connections open to the CompactLogix controller.

## Numerics

## CompactFlash

| 1769-L3x controllers                                                     | data storage  125 install  21 read and write user data  reader  125 CompactLogix                          |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| status indicator  131                                                    | 125                                                                                                       |
| A                                                                        |                                                                                                           |
|                                                                          | address I/O data  91                                                                                      |
| add-on instructions  105                                                 | applications development  97                                                                              |
| address data  91                                                         | battery maintenance  127                                                                                  |
| AOI  105                                                                 | configure I/O  87 connections example  79                                                                 |
| applications                                                             | ControlNet network communication  50                                                                      |
| develop  97 architecture  12                                             | ControlNet software combinations  51 COS  87                                                              |
| ASCII devices                                                            | define programs  101                                                                                      |
| serial communication  64                                                 | define routines  101                                                                                      |
| assemble the system  22                                                  | define tasks  99 design a system  13                                                                      |
| B                                                                        | DeviceNet network communication  53 DeviceNet software combinations  54 DH-485 network communication  72  |
|                                                                          | display I/O fault data  93                                                                                |
| battery                                                                  | dynamic memory allocation  137                                                                            |
| connect  20                                                              | 128                                                                                                       |
| life  128                                                                | estimate battery life                                                                                     |
| Lithium  129                                                             | EtherNet/IP network communication                                                                         |
| maintenance  127                                                         | 48 EtherNet/IP software combinations  48                                                                  |
| storage  129 19                                                          | I/O communication format  87 I/O connections  88                                                          |
| before you begin                                                         | I/O electronic keying  87                                                                                 |
| BOOTP  29                                                                | Logix5000 connections  77                                                                                 |
| broadcast messages over serial  67                                       | manage controller communication  75 manage tasks  97                                                      |
| C                                                                        | monitor connections  107 monitor controller status  106 monitor I/O modules  93 network communication  47 |
| cables 86                                                                | organize tags  103 overview  11                                                                           |
| 1769 expansion  serial  42                                               |                                                                                                           |
| cache messages  77                                                       | place local I/O modules  86 RPI  87                                                                       |
| calculate system power consumption                                       | select I/O modules  81 104                                                                                |
| 83                                                                       | select programming language  serial communication  55                                                     |
| total connections  78                                                    |                                                                                                           |
| change                                                                   | serial modbus support  67 serial port configuration                                                       |
| equipment states  116 change of state  87                                | 56 start  11                                                                                              |
| channel 0 default  28                                                    | use CompactFlash reader  125                                                                              |
|                                                                          | 82                                                                                                        |
| check                                                                    | validate I/O layout                                                                                       |
| low battery  128                                                         | CompactLogix controllers                                                                                  |
| communicate                                                              | dynamic memory allocation  137                                                                            |
| EtherNet/IP network  48 over networks  47                                | compatibility  18 configuration                                                                           |
|                                                                          | DF1  55                                                                                                   |
| communication                                                            | serial                                                                                                    |
| ControlNet network  50                                                   | 27 43                                                                                                     |
| determine timeout with any device  107 determine timeout with I/O module | configure                                                                                                 |
| DeviceNet network  53                                                    | distributed I/O on ControlNet  89 distributed I/O on DeviceNet  90 distributed I/O on EtherNet  88        |
| DH-485 network  72                                                       |                                                                                                           |
|                                                                          | I/O  81 ,  87                                                                                             |
| format  87                                                               |                                                                                                           |
|                                                                          | PhaseManager                                                                                              |
|                                                                          | 113                                                                                                       |
|                                                                          | 108                                                                                                       |

## connect

## DeviceNet network

| battery  20                                     |                                                |
|-------------------------------------------------|------------------------------------------------|
|                                                 | communication  53                              |
| ControlNet  32                                  | configure distributed I/O  90                  |
| EtherNet/IP  28                                 | example configuration  55                      |
| programming terminal  35                        | software combinations  54                      |
| RS-232  26                                      | DF1                                            |
| connections  77                                 | configuration  55                              |
| calculate  78                                   | master  67                                     |
| consume data  75                                | radio modem support  61                        |
| ControlNet network  52                          | DH-485 network                                 |
| determine timeout with any device  107          | communication  72                              |
| determine timeout with I/O module  108          | dimensions  24                                 |
| EtherNet/IP network  49                         | DIN rail  25                                   |
| example  79                                     | display                                        |
| monitor  107                                    |                                                |
| number needed to optimize throughput  141       | fault data  93                                 |
| produce data  75                                | dynamic memory allocation  137                 |
| view number of open  141                        | CompactLogix controllers  137                  |
| connections per PLC                             | messages  138                                  |
| specify  139                                    | RSLinx tag optimization  138                   |
| consume data                                    |                                                |
| connection use  75                              |                                                |
| controller                                      | E                                              |
| communication management  75                    | EDS files  36                                  |
| design  13                                      | electronic keying  87                          |
| fault handler  109                              | electrostatis discharge  16                    |
| firmware  36                                    | end cap  94                                    |
| operating modes  39                             | equipment states                               |
| path selection  45                              | 116                                            |
| status monitoring  106                          | change                                         |
| controller properties  67                       | estimate                                       |
| ControlNet network                              | battery life  128 82                           |
| communication  50 configure distributed I/O  89 | requested packet interval  EtherNet/IP network |
| connections  32 ,  52                           | communication  48                              |
| example configuration  51                       | configure distributed I/O  88                  |
| module status indicator  134                    | connections  28 ,  49                          |
| node address  19                                | example configuration  48                      |
| software combinations  51                       | network LED indicators                         |
|                                                 | 136 software combinations  48                  |
| tap  33 COS  87                                 | European hazardous location approval           |
|                                                 | example system  12                             |
| D                                               | expansion cables                               |
| data                                            | configuration  86                              |
| update  92 data storage                         | F                                              |
| CompactFlash  125                               | fault data                                     |
| DDE/OPC topics  139                             | display  93                                    |
| default serial configuration  27                | fault handler  109                             |
| define                                          | FBD  104                                       |
| programs  101                                   | firmware  36                                   |
| routines  101                                   |                                                |
| tasks  99                                       | function block diagram  104                    |
| design  13                                      |                                                |
| CompactLogix system  13                         | G                                              |
| develop                                         | ground  24                                     |
| applications  97                                |                                                |
| develop application                             |                                                |
| fault handler                                   |                                                |
| 109                                             |                                                |

## I

| status indicator  136                    |          |                        |                 |
|------------------------------------------|----------|------------------------|-----------------|
| COS  87                                  |          |                        |                 |
| electronic keying  layout validation  82 |          | 87                     |                 |
| monitor  81                              |          |                        |                 |
| monitor connection                       |          | 108                    |                 |
| place  81                                |          |                        |                 |
| I/O modules                              |          |                        |                 |
| monitor  93                              |          |                        |                 |
| 94                                       |          |                        |                 |
| reconfigure                              |          |                        |                 |
| select  81                               |          |                        |                 |
| install  15                              |          |                        |                 |
| IP address  29                           |          |                        |                 |
| isolator  27                             |          |                        |                 |
| battery  129                             |          |                        |                 |
| place  86                                |          |                        |                 |
| low battery  128                         |          |                        |                 |
| manage controller communications         |          |                        |                 |
| tasks  97                                |          |                        |                 |
| manual state changes                     |          | 117                    |                 |
| 55                                       |          |                        |                 |
| cache  77                                |          |                        |                 |
| 138                                      |          |                        |                 |
| send  76                                 |          |                        |                 |
| 67                                       |          |                        |                 |
| modbus support                           |          |                        |                 |
| radio  67                                |          |                        |                 |
| modem                                    |          |                        |                 |
| 39                                       |          |                        |                 |
| modes                                    |          |                        |                 |
| 23                                       |          |                        |                 |
| receive  76                              |          |                        |                 |
| master mode                              |          |                        |                 |
| broadcast over serial                    |          | 67                     |                 |
| 95                                       | messages | reconfigure I/O module | minimum spacing |

## monitor

connections 107

controller status 106

I/O 81

I/O modules 93

## mount

DIN rail 25

panel 25

system 23

## N

network communication 47

network LED indicators

EtherNet/IP network 136

node address 19

North American Haxardous location approval

17

## O

operating modes 39

optical isolator 27

organize tags 103

## P

parts list 19

path selection controller 45

## PhaseManager

configure 113

terms 113

I/O 81

local I/O modules 86

point-to-point 55

port configuration serial 55 , 56

produce data connection use 75

program definition 101

programming language select 104

programming terminal 35

programs define 101

pushbutton 28

## R

radio modem 67

read and write user data

CompactFlash 125

receive messages 76

reconfigure

I/O module 94

place

## requested packet interval

communication 55 , 67 communication with ASCII devices 64 default configuration 27 driver 43 port configuration 55 , 56 port direct connection to controller 41 28

109

description 87 estimate 82 routines define 101 RS-232 connections 26 RS-232 serial port status indicator 133 RSLinx tag optimization 138 S select controller path 45 I/O modules 81 programming language 104 send messages 76 sequential function chart 104 serial cables 42 pushbutton series B 18 set node address 19 SFC 104 slave 67 slave mode 55 software combinations ControlNet network 51 DeviceNet network 54 spacing 23 specify connections per PLC 139 ST 104 state model 114 comparisons 117 states manually change 117 status indicator 1769-L3x 131 link status indicator 136 LNK 136 module 135 RS-232 serial port 133 store batteries 129 structured text 104 system layout 12 system overhead time slice system power consumption

estimate 83

## T

## tags

organize 103

tasks

define 99

manage 97

management 97

total connections

calculate 78

trends

139

## U

## update

data 92

use

CompactFlash reader 125

## V

## validate

I/O layout 82

verify

compatibility 18

view

number of open connections 141

## W

## wiring 24

## Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products. At http://www.rockwellautomation.com/support, you can find technical manuals, technical and application notes, sample code and links to software service packs, and a MySupport feature that you can customize to make the best use of these tools. You can also visit our Knowledgebase at http://www.rockwellautomation.com/knowledgebase for FAQs, technical information, support chat and forums, software updates, and to sign up for product notification updates.

For an additional level of technical phone support for installation, configuration, and troubleshooting, we offer TechConnectSM support programs. For more information, contact your local distributor or Rockwell Automation representative, or visit http://www.rockwellautomation.com/support/ .

## Installation Assistance

If you experience a problem within the first 24 hours of installation, review the information that is contained in this manual. You can contact Customer Support for initial help in getting your product up and running.

| United States or Canada 1.440.646.3434                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States or Canada Use the Worldwide Locator at http://www.rockwellautomation.com/support/americas/phone_en.html, or contact your local Rockwell Automation representative. |

## New Product Satisfaction Return

Rockwell Automation tests all of its products to ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned, follow these procedures.

| United States Contact your distributor. You must provide a Customer Support case number (call the phone number above to obtain one) to your distributor to complete the return process.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States Please contact your local Rockwell Automation representative for the return procedure.                                                                              |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation.com/literature/ .

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400

<!-- image -->

## 1769 CompactLogix Controllers