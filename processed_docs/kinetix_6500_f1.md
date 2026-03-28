<!-- image -->

## Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drives

Catalog Numbers 2094-BC01-MP5-M, 2094-BC01-M01-M, 2094-BC02-M02-M, 2094-BC04-M03-M, 2094-BC07-M05-M 2094-BMP5-M, 2094-BM01-M, 2094-BM02-M, 2094-BM03-M, 2094-BM05-M, 2094-SE02F-M00-S0, 2094-SE02F-M00-S1, 2094-EN02D-M01-S0, 2094-EN02D-M01-S1, 2094-BSP2, 2094-PRF, 2094-SEPM-B24-S

<!-- image -->

<!-- image -->

## Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with applicable code of practice.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

IMPORTANT Identifies information that is critical for successful application and understanding of the product.

These labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

The following icon may appear in the text of this document.

<!-- image -->

Identifies information that is useful and can help to make a process easier to do or easier to understand.

## Table of Contents

|                            | Preface  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . . . 9               |
|----------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
|                            | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . 9                 |                                                     |
|                            | Summary of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . 9                 |
|                            | Conventions Used in This Manual . . . . . . . .                                                        | . . . . . . . . . . . . .  . . . . . . . . . . . 10 |
|                            | Additional Resources . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . 10                          |
|                            | Chapter 1                                                                                              |                                                     |
| Start                      | About the Kinetix 6200 and Kinetix 6500 Drive Systems . . . . . . . . . . . . 14                       |                                                     |
|                            | Typical Hardware Configurations . . . . . . . . .                                                      | . . . . . . . . . . . . .  . . . . . . . . . . 15   |
|                            | Typical Communication Configurations . . . . .                                                         | . . . . . . . . . . . .  . . . . . . . . . 19       |
|                            | Catalog Number Explanation . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 23                  |
|                            | Kinetix Drive Component Compatibility . . . .                                                          | . . . . . . . . . . . .  . . . . . . . . . . 24     |
|                            | Kinetix 6000M Integrated Drive-Motor System Compatibility. . . . . . . 24                              |                                                     |
|                            | Agency Compliance . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . 25                |
|                            | CE and UK Requirements (system without LIM module) . . . . . . . . 25                                  |                                                     |
|                            | CE and UK Requirements (system with LIM module) . . . . . . . . . . . 25                               |                                                     |
|                            | Chapter 2                                                                                              |                                                     |
| Plan the Kinetix 6200 and  | System Design Guidelines . . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 27                  |
| Kinetix 6500               | System Mounting Requirements .  . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . 27                      |
| Drive System Installation  | Transformer Selection . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . 28                                  |
|                            | AC Line Filter Selection . . . . .  . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . 29                  |
|                            | Circuit Breaker/Fuse Options . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 30                    |
|                            | Enclosure Selection . . . . . . . .  . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . 32                  |
|                            | Minimum Clearance Requirements . . . . . . .                                                           | . . . . . . . . . . .  . . . . . . . . . 35         |
|                            | Electrical Noise Reduction  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . 36                            |
|                            | Bond Modules. . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . 36                            |
|                            | Bond Multiple Subpanels . . . . .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 38                    |
|                            | Establish Noise Zones. . . . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 39                    |
|                            | Cable Categories for Kinetix 6200 and Kinetix 6500 Systems. . . . . 47                                 |                                                     |
|                            | Noise Reduction Guidelines for Drive Accessories . . . . . . . . . . . . . . 49                        |                                                     |
|                            | Chapter 3                                                                                              |                                                     |
| Mount the Kinetix 6200 and | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . . . . . . . . . . . 53                          |
| Kinetix 6500               | Install 2094 Mounting Brackets . . . . . . . .                                                         | . . . . . . . . . . . . .  . . . . . . . . . . 53   |
| Drive System               | Install the 2094 Power Rail. . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 54                  |
|                            | Determine Mounting Order.   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . 54                                  |
|                            | Mount Modules on the                                                                                   |                                                     |
|                            | Power Rail. . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 55                                  |
|                            | Mount the Control Modules .   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . . . . . . . 58                                  |
|                            | Chapter 4                                                                                              |                                                     |
| Connector Data and Feature | 2094 Power Module and                                                                                  |                                                     |
| Descriptions               | Control Module Features . . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 62                |

Connect the Kinetix 6200 and

Kinetix 6500 Drive System

| I/O, Safety, and Auxiliary Feedback Connector Pinout. . . . . . . . . . . 65                           |                                                   |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Motor Feedback Connector Pinout . . . . . . .                                                          | . . . . . . . . . . .  . . . . . . . . . . 66     |
| Ethernet Communication Connector Pinout . . . . . . . . . . . . . . . . . . . 67                       |                                                   |
| IAM Input Connector Pinout . .  . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . 67                  |
| IAM and AM Motor Power and Brake Connector Pinout . . . . . . . . . 68                                 |                                                   |
| Control Signal Specifications . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . .  . . . . . . . . 69           |
| Digital Inputs . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 69              |
| Ethernet Communication Specifications. . .                                                             | . . . . . . . . . . .  . . . . . . . . . 71       |
| Sercos Communication Specifications. . . . .                                                           | . . . . . . . . . . .  . . . . . . . . . 71       |
| Contactor Enable Relay . . . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 72                |
| Power and Relay Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73 |                                                   |
| Motor/Resistive Brake Relay . . . . . . . . . . .                                                      | . . . . . . . . . . . . .  . . . . . . . . . . 73 |
| Input Power Cycle Capability . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . 75                    |
| Peak Current Specifications . .  . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . 76                  |
| Control Power. . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . 78                        |
| Feedback Specifications .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . 79                        |
| Absolute Position Feature . . .  . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . 79                |
| Motor Feedback Specifications. . . . . . . . .                                                         | . . . . . . . . . . . .  . . . . . . . . . . . 80 |
| Auxiliary Position Feedback Specifications                                                             | . . . . . . . . . . .  . . . . . . . . . . 83     |
| Safe Speed Monitor Safety Features . . . . . . . . . . . . .                                           | . . . . . . . . .  . . . . . . . . 84             |
| Safe Torque Off Safety Features  . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . 85                |
| Chapter 5                                                                                              |                                                   |
| Basic Wiring Requirements .   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . . . . . . . 87                                |
| Build Your Own Cables . . . . . .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . 88                |
| Route the Power and Signal Cables . . . . . .                                                          | . . . . . . . . . . . .  . . . . . . . . . . 88   |
| Determine the Input Power Configuration . . .                                                          | . . . . . . . . . . .  . . . . . . . . . . 88     |
| Grounded Power Configurations. . . . . . . .                                                           | . . . . . . . . . . . .  . . . . . . . . . . 89   |
| Ungrounded Power Configurations . . . . . .                                                            | . . . . . . . . . . . .  . . . . . . . . . 91     |
| DC Common Bus Configurations. .  . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . 92                  |
| Common Bus Fusing Requirements . . . . . . .                                                           | . . . . . . . . . . .  . . . . . . . . . 93       |
| Set the Ground Jumper in Select Power Configurations. . . . . . . . . . . . . 93                       |                                                   |
| Set the Ground Jumper. . . . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 94                |
| Ground the Modular Drive System. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96      |                                                   |
| Ground the Power Rail to the System Subpanel . . . . . . . . . . . . . . . . . 96                      |                                                   |
| Ground Multiple Subpanels. . . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 97                  |
| Power Wiring Requirements . . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 98                  |
| Power Wiring Guidelines . . . . . . . . . . . . .  . . . . . . . . . . . . . .                         | . . . . . . . . . . . . 100                       |
| Wire the IAM/AM Module Connectors . . . . . . . . . . . . . . . . . . . . . . . . . . . 101            |                                                   |
| Wire the Control Power (CPD) Connector. . . . . . . . . . . . . . . . . . . . . 101                    |                                                   |
| Wire the Input Power (IPD) Connector . . .                                                             | . . . . . . . . . . .  . . . . . . . . . 102      |
| Wire the Contactor Enable (CED) Connector . . . . . . . . . . . . . . . . . . 104                      |                                                   |
| Wire the Motor Power (MP) Connector . . . . . . . . . . . . . . . . . . . . . . . 105                  |                                                   |
| Wire the Motor/Resistive Brake (BC) Connector . . . . . . . . . . . . . . . . 111                      |                                                   |
| Apply the Motor Cable Shield Clamp . . . . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . . 114  |
| Feedback and I/O Cable Connections . . . . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . 115    |
| Flying-lead Feedback Cable Pinouts . . . . . . . . . . . . . . . . . . . . . . . . . . 117             |                                                   |
| Wire the Feedback and I/O Connectors . . . . . . . . . . . . . . . . . . . . . . . . . . 118           |                                                   |
| Connect Premolded Motor Feedback Cables. . . . . . . . . . . . . . . . . . . 118                       |                                                   |

|                               | Connect Panel-mounted Breakout Board Kits                                                         | . . . . . . . . . .  . . . . . . . 119         |
|-------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------|
|                               | Wire Low-profile Connector Kits . . . . . . . .                                                   | . . . . . . . . . . . .  . . . . . . . . . 120 |
|                               | External Shunt Module Connections . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . 123                  |
|                               | IPIM Module Connections . .  . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 124            |
|                               | RBM Module Connections . . . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . 125                |
|                               | Sercos Fiber-optic Cable Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126  |                                                |
|                               | Kinetix 6000M Integrated Drive-Motor Sercos Connections . . . . . . . 129                         |                                                |
|                               | Ethernet Cable Connections . . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . 130                |
|                               | Chapter 6                                                                                         |                                                |
| Configure and Start the       | Configure the Kinetix 6000M Integrated Drive-Motor System. . . . . . 135                          |                                                |
| Kinetix 6200 and Kinetix 6500 | Configure the Drive Modules. . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . 136                |
| Drive System                  | Configure the Logix 5000 Sercos interface Module . . . . . . . . . . . . . . . . 142              |                                                |
|                               | Configure the Logix 5000 Controller . . . . .                                                     | . . . . . . . . . . . .  . . . . . . . . 142   |
|                               | Configure the Logix 5000 Controller Module  . . . . . . . . . . .                                 | . . . . . . . 144                              |
|                               | Configure the Kinetix 6200 and Kinetix 6500 Drive Modules. . . . 146                              |                                                |
|                               | Configure the Motion Group. . . . . . . . . . . . . . . . .                                       | . . . . . . . . .  . . . . . . . 150           |
|                               | Configure Axis Properties . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . 151                |
|                               | Download the Program . .  . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . 154            |
|                               | Apply Power to the                                                                                |                                                |
|                               | Kinetix 6200 and Kinetix 6500 Drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155 |                                                |
|                               | Test and Tune the Axes . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . . . . . . . . . . . 157                      |
|                               | Test the Axes . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . 157            |
|                               | Tune the Axes . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . 159                      |
|                               | Chapter 7                                                                                         |                                                |
| Configure and Start the       | Configure the Drive Modules. . . .  . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . 161                |
| Kinetix 6200 and Kinetix 6500 | Configure the Logix EtherNet/IP Module. . . . .                                                   | . . . . . . . . . . . .  . . . . . . . . 165   |
|                               | Configure the Logix Controller. . . . . . . . . .                                                 | . . . . . . . . . . . .  . . . . . . . . . 165 |
| Drive System                  | Configure the Logix Module . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . 167                  |
|                               | Configure the Kinetix 6200 and Kinetix 6500 Drive Modules. . . . 169                              |                                                |
|                               | Configure the Motion Group. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174   |                                                |
|                               | Configure Axis Properties . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . 175                |
|                               | Download the Program . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . 180                              |
|                               | Apply Power to the                                                                                |                                                |
|                               | Kinetix 6200 and Kinetix 6500 Drive . . . . . . . . . . . . .                                     | . . . . . . . . .  . . . . . . . 180           |
|                               | Test and Tune the Axes . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . . . . . . . . . . . 181                      |
|                               | Test the Axes . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | . . . . . . . 182                              |
|                               | Tune the Axes . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . 184                      |
|                               | Chapter 8                                                                                         |                                                |
| Troubleshoot the Kinetix 6200 | Safety Precautions . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . . . . 187                      |
| and Kinetix 6500 Drive System | Interpret Status Indicators.  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . 188                              |
|                               | Kinetix 6000M IDM System Error Codes. . . . . . . . . . . . . . . . . . . . . . 188               |                                                |
|                               | Four-character Display Messages . . . . . . .                                                     | . . . . . . . . . . . .  . . . . . . . . . 188 |
|                               | Fault Codes . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . 189            |
|                               | Control Module Status Indicators   . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . 198                  |
|                               | Shunt Module Status Indicators . . . . . . . .                                                    | . . . . . . . . . . . .  . . . . . . . . . 199 |

|                               | General System Anomalies . . . . .  . . . . . . . . . . . . . . . . . .                                                                                                                  | . . . . . . . . . . . . . . 200                      |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
|                               | Logix 5000 Controller and Drive Behavior . . .                                                                                                                                           | . . . . . . . . . . . .  . . . . . . . . . 202       |
|                               | Kinetix 6500 Drive Exception Behavior . . . . . . . . . . . . . . . . . . . . . . . 202                                                                                                  |                                                      |
|                               | Kinetix 6200 Drive Fault Behavior . . . . . . .                                                                                                                                          | . . . . . . . . . . . .  . . . . . . . . . 203       |
|                               | Drive Exception/Fault Behavior . . . . . . . . .                                                                                                                                         | . . . . . . . . . . . .  . . . . . . . . . 204       |
|                               | Chapter 9                                                                                                                                                                                |                                                      |
| Remove and Replace the        | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                    | . . . . . . . . . . . . 209                          |
| Kinetix 6200 and Kinetix 6500 | Remove Kinetix 6200 and Kinetix 6500 Drive Modules. . . . . . . . . . . . . 210                                                                                                          |                                                      |
| Drive Modules                 | Remove the Control Module . . .  . . . . . . . . . . . . . . . . .                                                                                                                       | . . . . . . . . . . . . . 211                        |
|                               | Remove the Drive Modules . . . .  . . . . . . . . . . . . . . . . .                                                                                                                      | . . . . . . . . . . . . . 212                        |
|                               | Replace Kinetix 6200 and Kinetix 6500 Drive Modules . . . . . . . . . . . . . 213                                                                                                        |                                                      |
|                               | Replace the Drive Modules . . . .  . . . . . . . . . . . . . . . . .                                                                                                                     | . . . . . . . . . . . . . 213                        |
|                               | Replace the Control Modules . . . . . . . . . . .                                                                                                                                        | . . . . . . . . . . . .  . . . . . . . . . 213       |
|                               | Remove the Power Rail . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                     | . . . . . . . . . . 214                              |
|                               | Replace the Power Rail . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                    | . . . . . . . . . . 214                              |
|                               | Appendix A                                                                                                                                                                               |                                                      |
| Interconnect Diagrams         | Interconnect Diagram Notes .   . . . . . . . . . . . . . . . . . . .                                                                                                                     | . . . . . . . . . . . . . . . . 216                  |
|                               | Power Wiring Examples . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                       | . . . . . . . . . . 217                              |
|                               | DC Common Bus Wiring Examples . . . . . . . . . . . . . . . . . . . . . . . . . . 221                                                                                                    |                                                      |
|                               | Shunt Module Wiring Examples  . . . . . . . . . . . . . . .                                                                                                                              | . . . . . . . . . . . . . . 225                      |
|                               | Axis Module/Rotary Motor Wiring Examples  . . . . . . . . . . .                                                                                                                          | . . . . . . . . . . 226                              |
|                               | Axis Module/Linear Motor/Actuator Wiring Examples. . . . . . . . . . . . . 231                                                                                                           |                                                      |
|                               | Kinetix 6000M Integrated Drive-Motor Wiring Example . . . . . . . . . . 236                                                                                                              |                                                      |
|                               | Brake Control Example . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                       | . . . . . . . . . . . 237                            |
|                               | System Block Diagrams. . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                                                  | . . . . . . . . . . . . . . . . 238                  |
|                               | Appendix B                                                                                                                                                                               |                                                      |
| Upgrade the Drive Firmware    | Upgrade Kinetix 6000M System Firmware . . . . . . . . . . . . . . . . . . . . . . . 241                                                                                                  |                                                      |
|                               | Upgrade Kinetix 6200 and Kinetix 6500 Drive Firmware . . . . . . . . . . . 242                                                                                                           |                                                      |
|                               | Before You Begin . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                | . . . . . . . 242                                    |
|                               | Configure Logix 5000 Communication . . . . . . . . . . . . . . . . . . . . . . . 243                                                                                                     |                                                      |
|                               | Upgrade Firmware. . . . . . . . . .  . . . . . . . . . . . . . . . . .                                                                                                                   | . . . . . . . . . . . . . . . 244                    |
|                               | Verify the Firmware Upgrade . . . . . . . . . . . . . . . .                                                                                                                              | . . . . . . . . .  . . . . . . . 248                 |
|                               | Appendix C                                                                                                                                                                               |                                                      |
| DC Common-bus Applications    | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                    | . . . . . . . . . . . . 249                          |
|                               | Calculate Total Bus Capacitance . . . . . . . . .                                                                                                                                        | . . . . . . . . . . . . .  . . . . . . . . . . . 250 |
|                               | Calculate Additional Bus Capacitance . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251                                                                                         |                                                      |
|                               | Bulletin 2094 Drive Capacitance Values . . . . . . . . . . . . . . . . . . . . . . . . . . 251                                                                                           |                                                      |
|                               | Common Bus Capacitance Example . . . . . . .                                                                                                                                             | . . . . . . . . . . . .  . . . . . . . . . . 252     |
|                               | Appendix D                                                                                                                                                                               |                                                      |
| Configure the Load Observer   | Benefits . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                          | . . . . . . . . . . . . 253                          |
| Feature                       | How it Works. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  Configuration . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 253 . . . . . . . . . . . . . 254    |

|                                  | Remaining IDN Parameter Descriptions. . .                                                         | . . . . . . . . . .  . . . . . . . . . 256         |
|----------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------|
|                                  | Out-of-Box Gain Settings. . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 258                  |
|                                  | Auto-tune Gain Settings. . . . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 260                  |
|                                  | Tuning Mode Summary . . . . . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 263                  |
|                                  | Manual Tuning for Further Optimization . .                                                        | . . . . . . . . . .  . . . . . . . . . 263         |
|                                  | Setting Gains with Sercos IDN Write Messages . . . . . . . . . . . . . . . . . . . 265            |                                                    |
|                                  | Compensate for High Frequency Resonances .                                                        | . . . . . . . . . . .  . . . . . . . . . 266       |
|                                  | Appendix E                                                                                        |                                                    |
| Web Server Interface             | Overview . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .     | . . . . . . . . . . . . 269                        |
|                                  | Web Server Interface Categories   . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . 270                    |
|                                  | Home Category . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . . . . . . . 271                                  |
|                                  | Diagnostics Category. . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . . 272                                |
|                                  | Drive Indicators . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 272                |
|                                  | Drive Information . . . . . . . . .  . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . 273                  |
|                                  | Motor Information . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . . . . . . 274                                  |
|                                  | Network Settings . . . . . . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 275                |
|                                  | Ethernet Statistics . . . . . . . .  . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 276                |
|                                  | CIP Statistics. . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . 277                                |
|                                  | Encoder Statistics . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . 278                        |
|                                  | Peak Detection . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . 279                                |
|                                  | Monitor Signals . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . 280                                  |
|                                  | Oscilloscope. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . 281                                |
|                                  | Fault Logs Category . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . 282                                |
|                                  | Configure Fault Log. . . . . . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 282                |
|                                  | Data Logs Category . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . . . . . . . . 283                                |
|                                  | Temperatures . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 283                |
|                                  | Administrative Settings Category. . . . . . . . .                                                 | . . . . . . . . . . . .  . . . . . . . . . . . 284 |
|                                  | Browse Power Rail Category . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . . . . . . 284                                  |
|                                  | Safety Category . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . . . . . . . . 285                                |
|                                  | Safety Main . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . 285                                |
|                                  | Safety Configuration. . . . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 286                |
|                                  | Configuration Summary . . . . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 287                  |
|                                  | Change Safety Password . . . . .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 288                  |
|                                  | Appendix F                                                                                        |                                                    |
| Change Kinetix 6200 Default IDN  | Before You Begin . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . . . . . . . . . . . . . 289                      |
| Parameter Values                 | Change IDN Parameter Values . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 290                  |
|                                  | Read the Present IDN Parameter Value . . . . . . . . . . . . . . . . . . . . . . . 290            |                                                    |
|                                  | Calculate/Select the New IDN Value . . . . .                                                      | . . . . . . . . . . .  . . . . . . . . . . 292     |
|                                  | Write the New IDN Parameter Value . . . . .                                                       | . . . . . . . . . . .  . . . . . . . . . 293       |
|                                  | Appendix G                                                                                        |                                                    |
| Kinetix 6500 CIP Axis Attributes | Standard Attributes . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . . 295                        |
|                                  | Kinetix 6500 Drive Specific Attributes. . . . . . . . . . . . . . . . . . . . . . . . . . . . 295 |                                                    |

| RBM Module Interconnect Diagrams   | Appendix H Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . 303 RBM Module Wiring Examples. . . . . . . . . . . . . . . . . .  . . . . . . . . .  . . . . . . . 304   |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

This manual provides detailed installation instructions to mount, wire, and troubleshoot the Kinetix® 6200 and Kinetix 6500 servo drives, and system integration for your drive and motor/actuator combination with a Logix 5000™ controller.

For information on wiring, configuring, and troubleshooting the Safe Speed Monitor functions, refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Safety Reference Manual, publication 2094-RM001 .

For information on wiring, configuring, and troubleshooting the Safe Torque Off functions, refer to the Kinetix 6200 and Kinetix 6500 Safe Torque-off Safety Reference Manual, publication 2094-RM002 .

This manual is intended for engineers or technicians directly involved in the installation and wiring of the Kinetix 6200 and Kinetix 6500 drives, and programmers directly involved in the operation, field maintenance, and integration of these drives with the EtherNet/IP™ communication module or controller.

If you do not have a basic understanding of Kinetix 6200 and Kinetix 6500 servo drives, contact your local Rockwell Automation sales representative for information on available training courses.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic                                         | Page   |
|-----------------------------------------------|--------|
| Added UK certification information throughout |        |

## Conventions Used in This Manual

## Additional Resources

Table 1 - Additional Resoures

|                                                                                                                               | Resource Description                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001                                                    | Product specifications for Kinetix VPL, VPC, VPF, VPH, and VPS; Kinetix MPL, MPM, MPF, and MPS; Kinetix TLY and TL; Kinetix HPK; and Kinetix MMA rotary motors.                                                                                                                                                                                                                                          |
| Kinetix Linear Motion Specifications Technical Data, publication KNX-TD002                                                    | Product specifications for Kinetix MPAS and MPMA linear stages, Kinetix MPAR and MPAI electric cylinders, and Kinetix LDC and LDL linear motors.                                                                                                                                                                                                                                                         |
| Kinetix 5700, 5500, 5300, 5100 Servo Drives Specifications, publication KNX-TD003                                             | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP network and EtherNet/IP networking servo drive families.                                                                                                                                                                                                                                                              |
| Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNX-TD004                                   | Product specifications for Kinetix 2090 motor and interface cables.                                                                                                                                                                                                                                                                                                                                      |
| Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications, publication KNX-TD005                          | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP network (Kinetix 6500 and Kinetix 350), Integrated Motion over Sercos interface (Kinetix 6200, Kinetix 6000, Kinetix 2000, and Kinetix 7000), and component (Kinetix 3) servo drive families.                                                                                                                         |
| Kinetix Servo Drive Performance Specifications per Ecodesign Regulation (EU) 2019/ 1781 technical data, publication KNX-TD006 | Provides energy efficiency performance data for Rockwell Automation Kinetix Servo drives. This data supports IE2 compliance of Kinetix Servo drives per EU 2019/1781.                                                                                                                                                                                                                                    |
| Kinetix 5700 Drive Systems Design Guide, publication KNX-RM010                                                                | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 5500 Drive Systems Design Guide, publication KNX-RM009                                                                | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 5300 Drive Systems Design Guide, publication KNX-RM012                                                                | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 5100 Drive Systems Design Guide, publication KNX-RM011                                                                | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 6000 and Kinetix 6200/6500 Drive Systems Design Guide, publication KNX-RM003                                          | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 300/350 Drive Systems Design Guide, publication KNX-RM004                                                             | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 3 Drive Systems Design Guide, publication KNX-RM005                                                                   | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 2000 Drive Systems Design Guide, publication KNX-RM006                                                                | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix 7000 Drive Systems Design Guide, publication KNX-RM007                                                                | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Kinetix Halogen-free PUR and PVC Single Motor Cables Quick Reference, publication 2090-QR002                                  | Provides product specifications comparing 2090-CSBM1Dx - xxLFxx (Halogen-free PUR) and 2090-CSxM1Dx - xxVAxx (PVC) single motor cables.                                                                                                                                                                                                                                                                  |
| Kinetix 5700 Safe Monitor Functions Safety Reference Manual, publication 2198-RM001                                           | Provides a description of integrated stopping functions and safe monitoring functions with a Logix 5000 controller and Kinetix 5700 servo drives.                                                                                                                                                                                                                                                        |
| Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Servo Drives Safety Reference Manual, publication 2094-RM001              | Provides information on how to wire, configure, and troubleshoot the safe-speed features of your Kinetix 6200 and Kinetix 6500 drives.                                                                                                                                                                                                                                                                   |
| Kinetix 6200 and Kinetix 6500 Safe Torque-off Servo Drives Safety Reference Manual, publication 2094-RM002                    | Provides information on how to wire, configure, and troubleshoot the safe torque-off features of your Kinetix 6200 and Kinetix 6500 drives.                                                                                                                                                                                                                                                              |
| System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001                                         | Provides information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                                                                                                                                                                                                                                                          |

The conventions starting below are used throughout this manual.

- Bulleted lists such as this one provide information, not procedural steps.
- Numbered lists provide sequential steps or hierarchical information.
- Acronyms for the Kinetix 6200 and Kinetix 6500 drive modules are shown in the table below and are used throughout this manual.

| Acronym  Kinetix 6200 and Kinetix 6500 Drive Modules  Cat. No.   |
|------------------------------------------------------------------|
| IAM Integrated Axis Module 2094-xBCxx-Mxx-xM                     |
| AM Axis Module 2094-xBMxx - xM                                   |
| LIM Line Interface Module 2094-xBLxx and 2094-xBLxxS-xx          |
| RBM Resistive Brake Module 2090-XBxx - xx                        |

| Acronym Kinetix 6000M Drive Modules Cat. No.    |
|-------------------------------------------------|
| IDM Integrated Drive-Motor MDF-SBxxxxx          |
| IPIM IDM Power Interface Module 2094-SEPM-B24-S |

These documents contain additional information concerning related products from Rockwell Automation.

Table 1 - Additional Resoures (continued)

|                                                                              | Resource Description                                                                                                                                                    |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Industrial Ethernet Media Brochure, publication 1585-BR001                   | Provides information to determine the Bulletin 1585 Ethernet cable that fits your application and the product specifications to help select the appropriate components. |
| Ethernet Reference Manual, ENET-RM002                                        | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                              |
| Access Motion Analyzer from: https://motionanalyzer.rockwellautomation.com . | Provides comprehensive motion application sizing tool used for analysis, optimization, selection, and validation of your Kinetix Motion Control system.                 |
| Rockwell Automation Product Selection website, rok.auto/systemtools          | Provides online product selection and system configuration tools, including AutoCAD (DXF) drawings.                                                                     |
| Product Certifications website, rok.auto/certifications                      | Provides declarations of conformity, certificates, and other certification details.                                                                                     |

You can view or download publications at rok.auto/literature.

## Notes:

## Start

Use this chapter to become familiar with the design and installation requirements for Kinetix® 6200/6500 drive systems.

| Topic Page                                                   |
|--------------------------------------------------------------|
| About the Kinetix 6200 and Kinetix 6500 Drive Systems 14     |
| Typical Hardware Configurations 15                           |
| Typical Communication Configurations 19                      |
| Catalog Number Explanation 23                                |
| Kinetix Drive Component Compatibility 24                     |
| Kinetix 6000M Integrated Drive-Motor System Compatibility 24 |
| Agency Compliance 25                                         |

1

## About the Kinetix 6200 and Kinetix 6500 Drive Systems

The Kinetix 6200 and Kinetix 6500 modular multi-axis servo drives are designed to provide a Kinetix Integrated Motion solution for your drive/ motor/actuator applications.

Table 2 - Kinetix 6200 and Kinetix 6500 Drive System Overview

| System Component         |                                                           | Cat. No. Description                                                                                                                                                                                                                                                                                                                                   |
|--------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integrated Axis Module   | 2094-BCxx-Mxx-M                                           | Integrated Axis (power) Modules (IAM) with Safe Speed Monitor are available with 400V-class AC input power and contains an inverter and converter section. The IAM power module requires one control module.                                                                                                                                           |
|                          | Axis Module 2094-BMxx-M                                   | Axis (power) Modules (AM) are a shared DC-bus inverter rated for 400V-class input power. The AM power modules each require one control module and must be used with an IAM power module.                                                                                                                                                               |
| Control Module           | 2094-SE02F-M00-Sx                                         | Interchangeable modular components for wiring I/O, safety, and feedback options using Sercos interface.                                                                                                                                                                                                                                                |
|                          | 2094-EN02D-M01-Sx                                         | Interchangeable modular components for wiring I/O, safety, and feedback options using EtherNet/IP networking.                                                                                                                                                                                                                                          |
|                          |                                                           | Shunt Module 2094-BSP2 The Bulletin 2094 shunt module mounts to the power rail and provides additional shunting in regenerative applications.                                                                                                                                                                                                          |
| Kinetix 6000M IDM System | 2094-SEPM-B24-S Bulletin MDF                              | The Kinetix 6000M integrated drive-motor (IDM) system consists of the IDM power interface module (IPIM) and up to 16 (Bulletin MDF) IDM units. The IPIM module mounts on the Bulletin 2094 power rail and provides power and communication to the IDM units. The IPIM module also monitors power output and provides overload protection.              |
| Power Rail               | 2094-PRSx 2094-PRx                                        | The Bulletin 2094 power rail consists of copper bus bars and a circuit board with connectors for each module. The power rail provides power and control signals from the converter section to adjacent inverters. The IAM and AM power modules, shunt module, slot-filler modules mount to the power rail.                                             |
|                          | Slot-filler Module 2094-PRF                               | The Bulletin 2094 slot-filler module is used when one or more slots on the power rail are empty after all the other power rail modules are installed. One slot-filler module is required for each empty slot.                                                                                                                                          |
| Logix 5000™ Controllers  | 1756-MxxSE modules 1768-M04SE module 1784-PM16SE PCI card | The Sercos interface module/PCI card serves as a link between the ControlLogix®/CompactLogix™/SoftLogix™ controllers and the Kinetix 6200 drive system. The communication link uses the EN/IEC 61491 Serial Real-time Communication System (Sercos) protocol over a fiber-optic cable.                                                                 |
| Logix 5000™ Controllers  | 1756-ENxTx modules                                        | The EtherNet/IP network module serves as a link between the ControlLogix platform and Kinetix 6500 drive system. Linear, Device Level Ring (DLR), and star topology is supported. The Kinetix 6000M IPIM module connects to the EtherNet/IP network for monitoring, diagnostics, and firmware upgrades.                                                |
| Studio 5000® Environment | 9324-RLD300xxE                                            | The Studio 5000 Logix Designer® application provides support for programming, commissioning, and maintaining the Logix 5000 family of controllers.                                                                                                                                                                                                     |
| Rotary Servo Motors      | Kinetix MP, Kinetix RDB, 1326AB                           | Compatible rotary motors include the Kinetix MPL, MPM, MPF, and MPS; Kinetix RDB; and 1326AB (M2L/S2L) 400V-class motors.                                                                                                                                                                                                                              |
|                          |                                                           | Linear Motors Kinetix LDC Compatible motors include Kinetix LDC iron core (400V-class) linear motors.                                                                                                                                                                                                                                                  |
| Linear Actuators         | Kinetix MP                                                | Compatible actuators include Kinetix MPAS (400V-class) single-axis and Kinetix MPMA multi-axis integrated linear stages, and Kinetix MPAR and MPAI (400V-class) electric cylinders.                                                                                                                                                                    |
| Linear Actuators         |                                                           | Kinetix LDAT Kinetix LDAT integrated linear actuators are compatible with 400V-class drive systems.                                                                                                                                                                                                                                                    |
| Cables                   | Kinetix 2090 power and feedback cables                    | Kinetix 2090 power and feedback cables are available with bayonet, threaded, and SpeedTec connectors. Power/brake cables have flying leads on the drive end and straight connectors that connect to servo motors. Feedback cables have flying leads that wire to low-profile connector kits on the drive end and straight connectors on the motor end. |
| Cables                   | Kinetix 6000M integrated drive-motor cables               | Kinetix 2090 integrated drive-motor (IDM) hybrid and network cables connect between the 2094 IPIM module and the Kinetix 6000M IDM units. Bulletin 889D and 879D cables connect between digital input connectors and sensors.                                                                                                                          |
| Cables                   | Communication                                             | Bulletin 2090 Sercos fiber-optic cables are available as enclosure only, PVC, nylon, and glass with connectors at both ends.                                                                                                                                                                                                                           |
| Cables                   | Communication                                             | Ethernet cables are available in standard lengths for Kinetix 6500, Kinetix 6200, and Kinetix 6000M IPIM modules. Shielded cable is recommended.                                                                                                                                                                                                       |
|                          | AC Line Filters 2090-XXLF-xxxx                            | Bulletin 2090-XXLF-xxxx three-phase AC line filters are required to meet CE in all 400V-class drive systems.                                                                                                                                                                                                                                           |
| Line Interface Modules   | 2094-xLxx 2094-xLxxS 2094-XL75S-Cx                        | Line interface modules (LIM) include the circuit breakers, AC line filter (catalog number 2094-BL02 only), power supplies, and safety contactor required for Kinetix 6200 and Kinetix 6500 operation. The LIM module does not mount to the power rail. You can purchase individual components separately in place of the LIM module.                   |
| External Shunt Modules   | 1394-SRxxxx                                               | You can use Bulletin 1394 external passive shunt modules when the IAM/AM power module internal shunt and power rail mounted 2094-BSP2 shunt module capability is exceeded.                                                                                                                                                                             |
| Resistive Brake Module   | 2090-XBxx-xx                                              | Resistive Brake Modules (RBM) include a safety contactor for use in a control circuit. Contactors and resistors reside in this module such that the motor leads can be disconnected from the drive with the permanent magnet motor brought to an immediate stop. This module does not mount to the power rail.                                         |

## Typical Hardware Configurations

Typical Kinetix 6200 and Kinetix 6500 system installations include threephase AC configurations, with and without the line interface module (LIM), and DC common-bus configurations.

<!-- image -->

SHOCK HAZARD: To avoid personal injury due to electrical shock, place a 2094PRF slot-filler module in all empty slots on the power rail. Any power rail connector without a module installed disables the Bulletin 2094 system; however, control power is still present.

Figure 1 - Typical Kinetix 6200 or Kinetix 6500 System Installation (with LIM)

<!-- image -->

Figure 2 - Typical Kinetix 6200 or Kinetix 6500 System Installation (without LIM)

<!-- image -->

This configuration illustrates the Kinetix 6000M integrated drive-motor (IDM) system with IDM power interface module (IPIM) installed on the Bulletin 2094 power rail. The IPIM module is included in the drive-to-drive fiber-optic cable installation along with the axis modules.

Figure 3 - Typical Kinetix 6000M Integrated Drive-Motor System Installation

<!-- image -->

For more information on Kinetix 6000M integrated drive-motor system installation, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Figure 4 - Typical DC Common Bus System Installation

<!-- image -->

In the example above, the leader IAM module is connected to the follower IAM module via the DC common-bus. The follower system also includes the Kinetix 6000M integrated drive-motor (IDM) power interface module (IPIM) that supports up to 16 IDM units.

When planning your panel layout, you must calculate the total bus capacitance of your DC common-bus system to be sure that the leader IAM module is sized sufficiently to precharge the entire system. Refer to Appendix C, beginning on page 249, for more information.

## IMPORTANT

If total bus capacitance of your system exceeds the leader IAM power module precharge rating, the IAM module four-character display scrolls a power cycle user limit condition. If input power is applied, the display scrolls a power cycle fault limit condition.

To correct this condition, you must replace the leader IAM power module with a larger module or decrease the total bus capacitance by removing the IPIM module or AM power modules.

## Typical Communication Configurations

In this example, drive-to-drive Sercos cables and catalog numbers are shown when Kinetix 6000, Kinetix 6000M, and Kinetix 6200 drive modules exist on the same power rail.

The Kinetix 6200 control modules use Sercos interface for configuring the Logix 5000 module and the EtherNet/IP network for diagnostics and configuring safety functions. An Ethernet cable is connected to each control module during safety configuration. For more information on Ethernet cables, refer to the Industrial Ethernet Media Brochure, publication 1585-BR001 .

Figure 5 - Typical Kinetix 6000 and Kinetix 6200 Communication (Sercos)

<!-- image -->

The Kinetix 6500 control modules can use any Ethernet topology including star, linear, and Device Level Ring (DLR). DLR is an ODVA standard and provides fault tolerant connectivity.

<!-- image -->

1756-EN2F modules are available for applications that require fiber-optic cable for noise immunity.

In this example, all devices are connected in linear topology. The Kinetix 6500 control module includes dual-port connectivity. Devices without dual ports should include the 1783-ETAP module or be connected at the end of the line.

- Up to 64 devices in linear configurations.
- No redundancy. If any device becomes disconnected, all the devices downstream loose communication.

Figure 6 - Kinetix 6500 Linear Communication Installation (EtherNet/IP network)

<!-- image -->

In this example, the devices are connected by using Device Level Ring (DLR) topology. DLR topology is fault redundant. For example, if a device in the ring is disconnected, the rest of the devices in the ring continue to maintain communication.

- Up to 64 devices in the DLR configurations.
- All Devices in a DLR ring should have dual-port connectivity or be connected in the ring by using a 1783-ETAP module.

Figure 7 - Kinetix 6500 Ring Communication Installation (EtherNet/IP network)

<!-- image -->

In this example, the devices are connected by using star topology. Each device is connected directly to the switch, making this topology fault tolerant. The 2094 power rail modules and other devices operate independently. The loss of one device does not impact the operation of the other devices.

Figure 8 - Kinetix 6500 Star Communication Installation (EtherNet/IP network)

<!-- image -->

Catalog Number Explanation Kinetix 6200 and Kinetix 6500 (Bulletin 2094) modular drive catalog numbers and descriptions are listed in the tables below. All power modules are compatible with the Kinetix 6200 and Kinetix 6500 control modules.

Table 3 - Kinetix 6200 and Kinetix 6500 Drive Catalog Numbers

| Integrated Axis Modules (460V) Cat. No.                                             |
|-------------------------------------------------------------------------------------|
| IAM power module, 400V-class, 6 kW converter, 4 A (0-pk) inverter 2094-BC01-MP5-M   |
| IAM power module, 400V-class, 6 kW converter, 9 A (0-pk) inverter  2094-BC01-M01-M  |
| IAM power module, 400V-class, 15 kW converter, 15 A (0-pk) inverter 2094-BC02-M02-M |
| IAM power module, 400V-class, 28 kW converter, 30 A (0-pk) inverter 2094-BC04-M03-M |
| IAM power module, 400V-class, 45 kW converter, 49 A (0-pk) inverter 2094-BC07-M05-M |
| Axis Modules (460V)                                                                 |
| AM power module, 400V-class, 4 A (0-pk) 2094-BMP5-M                                 |
| AM power module, 400V-class, 9 A (0-pk) 2094-BM01-M                                 |
| AM power module, 400V-class, 15 A (0-pk) 2094-BM02-M                                |
| AM power module, 400V-class, 30 A (0-pk) 2094-BM03-M                                |
| AM power module, 400V-class, 49 A (0-pk) 2094-BM05-M                                |
| Kinetix 6200 Control Modules                                                        |
| Control module, Sercos interface, Safe Torque Off 2094-SE02F-M00-S0                 |
| Control module, Sercos interface, Safe Speed Monitor 2094-SE02F-M00-S1              |
| Kinetix 6500 Control Modules                                                        |
| Control module, EtherNet/IP network, Safe Torque Off 2094-EN02D-M01-S0              |
| Control module, EtherNet/IP network, Safe Speed Monitor 2094-EN02D-M01-S1           |

Table 4 - Kinetix 6000 Drive Component Catalog Numbers

| Drive Components Cat. No.                                                               |
|-----------------------------------------------------------------------------------------|
| Integrated power interface (IPIM) module, 400V-class, 15 kW, 24 A (rms) 2094-SEPM-B24-S |
| Kinetix 6000 shunt module, 200/400V-class, 200 W 2094-BSP2                              |
| Kinetix 6000 slot-filler module, 200/400V-class 2094-PRF                                |

## Kinetix Drive Component Compatibility

## Kinetix 6000M Integrated Drive-Motor System Compatibility

The 2094-BCxx-Mxx-M and 2094-BMxx-M power modules contain the same power structure as the 2094-BCxx-Mxx-S and 2094-BMxx-S drive modules. Because of this, the 2094-BSP2 shunt module, 2094-PRF slot-filler module, and 2094-PRSx power rails are supported by both drive families.

In addition, 2094-BMxx-M AM power modules with Sercos interface are supported on power rails with a 2094-BCxx-Mxx-S IAM drive module. Conversely, 2094-BMxx-S AM drive modules are supported on power rails with a 2094-BCxx-Mxx-M IAM power module with Sercos interface.

## IMPORTANT

Kinetix 6500 EtherNet/IP control modules (catalog numbers 2094-EN02D-M01-Sx) are not compatible with IAM/AM modules on the same Bulletin 2094 power rail with Kinetix 6000 or Kinetix 6200 Sercos drives.

Table 5 - IAM and AM Module/Network Compatibility

|                                      | IAM Module Control Module                                                | 2094-BMxx-S            | 2094-BMxx-M AM Power Modules                     | 2094-BMxx-M AM Power Modules                   |
|--------------------------------------|--------------------------------------------------------------------------|------------------------|--------------------------------------------------|------------------------------------------------|
|                                      |                                                                          | Kinetix 6000 AM Module | 2094-SE02F-M00-Sx Kinetix 6200 Control Module    | 2094-EN02D-M01-Sx Kinetix 6500 Control Module  |
| 2094-BCxx-Mxx-S (series B, C, and D) | –                                                                        |                        | Fully compatible Fully compatible Not compatible |                                                |
| 2094-BCxx-Mxx-M (IAM power module)   | 2094-SE02F-M00-Sx Sercos interface 2094-EN02D-M01-Sx EtherNet/IP network |                        |                                                  | Not compatible Not compatible Fully compatible |

For additional information on the 2094-BCxx-Mxx-S IAM and 2094-BMxx-S AM modules, refer to the Kinetix 6000 Multi-axis Servo Drives User Manual, publication 2094-UM001 .

Bulletin 2094 power rails with Kinetix 6000 (series B, C, and D) or Kinetix 6200 drives are compatible with Kinetix 6000M integrated drive-motor (IDM) systems. The IDM power interface module (IPIM) mounts to the power rail and connects to as many as 16 IDM units.

Table 6 - IPIM Module Compatibility

|                                      | IAM Module Control Module                                                               | 2094-SEPM-B24-S IDM Power Interface Module (IPIM)   |
|--------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------|
| 2094-BCxx-Mxx-S (series B, C, and D) | –                                                                                       | Fully compatible                                    |
| 2094-BCxx-Mxx-M (IAM power module)   | 2094-SE02F-M00-Sx Sercos interface 2094-EN02D-M01-Sx EtherNet/IP network Not compatible | Fully compatible                                    |

For more information on Kinetix 6000M integrated drive-motor system installation, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

## Agency Compliance

If this product is installed within the European Union and has the CE mark, or within the United Kingdom and has the UKCA mark, the following regulations apply.

<!-- image -->

ATTENTION: Meeting CE and UK requires a grounded system, and the method of grounding the AC line filter and drive must match. Failure to do this renders the filter ineffective and can cause damage to the filter. For grounding examples, refer to Grounded Power Configurations on page 89 .

For more information on electrical noise reduction, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## CE and UK Requirements (system without LIM module)

To meet CE and UK requirements when your Kinetix 6200 and Kinetix 6500 system does not include the LIM module, these requirements apply.

- Install 2090-XXLF-xxxx AC line filters for three-phase input power and single-phase control power (for example, Schaffner P/N FN 355-10-05 or Roxburgh P/N RES5F08) as close to the IAM module as possible.
- Use Kinetix 2090 series motor power cables or use connector kits and terminate the cable shields to the chassis clamp provided.
- Combined motor power cable lengths for all Kinetix 6200 and Kinetix 6500 axes and hybrid cable lengths for all IDM units on the same DC bus must not exceed 240 m (787 ft) with 400V-class systems. Drive-tomotor power cables must not exceed 90 m (295.5 ft).
- Use Kinetix 2090 motor feedback cables or use connector kits and properly terminate the feedback cable shield. Drive-to-motor feedback cables must not exceed 90 m (295.5 ft).
- Install the Kinetix 6200 and Kinetix 6500 system inside an enclosure. Run input power wiring in conduit (grounded to the enclosure) outside of the enclosure. Separate signal and power cables.

Refer to Appendix A on page 215 for interconnect diagrams, including input power wiring and drive/motor interconnect diagrams.

## CE and UK Requirements (system with LIM module)

To meet CE and UK requirements when your Kinetix 6200 and Kinetix 6500 system includes the LIM module, follow all the requirements as stated in CE and UK Requirements (system without LIM module) and these additional requirements as they apply to the AC line filter.

- Install the LIM module (catalog numbers 2094-BL02) as close to the IAM module as possible.
- Install the LIM module (catalog numbers 2094-BLxxS or 2094-XL75S-Cx) with line filter (catalog number 2090-XXLF-xxxx) as close to the IAM module as possible.

When the LIM module (catalog numbers 2094-BLxxS or 2094-XL75S-Cx) supports two IAM modules, each IAM module requires an AC line filter installed as close to the IAM module as possible.

## Notes:

## System Design Guidelines

<!-- image -->

## Plan the Kinetix 6200 and Kinetix 6500 Drive System Installation

This chapter describes system installation guidelines used in preparation for mounting your Kinetix® 6200/6500 drive components.

| Topic Page                    |
|-------------------------------|
| System Design Guidelines 27   |
| Electrical Noise Reduction 36 |

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

Use the information in this section when designing your enclosure and planning to mount your system components on the panel.

For on-line product selection and system configuration tools, including AutoCAD (DXF) drawings of the product, refer to http://www.rockwellautomation.com/en/e-tools .

## System Mounting Requirements

- To comply with UL, CE, and UK requirements, the Kinetix 6200 and Kinetix 6500 drive systems must be enclosed in a grounded conductive enclosure offering protection as defined in standard EN/IEC 60529 to IP54 such that they are not accessible to an operator or unskilled person. A NEMA 4X enclosure exceeds these requirements providing protection to IP66.
- The panel you install inside the enclosure for mounting your system components must be on a flat, rigid, vertical surface that won't be subjected to shock, vibration, moisture, oil mist, dust, or corrosive vapors.
- Size the drive enclosure so as not to exceed the maximum ambient temperature rating. Consider heat dissipation specifications for all drive components.
- Combined motor power cable lengths for all axes and hybrid cable lengths for all IDM units on the same DC bus must not exceed 240 m (787

ft) with 400V-class systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).

| IMPORTANT   | System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|

- Combined length of Ethernet cables on Kinetix 6500 systems connecting drive-to-drive, drive-to-controller, or drive-to-switch must not exceed 100 m (328 ft).
- Segregate input power wiring and motor power cables from control wiring and motor feedback cables. Use shielded cable for power wiring and provide a grounded 360° clamp termination.
- Use high-frequency (HF) bonding techniques to connect the modules, enclosure, machine frame, and motor housing, and to provide a lowimpedance return path for high-frequency (HF) energy and reduce electrical noise.

Refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, to better understand the concept of electrical noise reduction.

## Transformer Selection

The IAM power module does not require an isolation transformer for threephase input power. However, a transformer can be required to match the voltage requirements of the controller to the available service.

To size a transformer for the main AC power inputs, refer to the Kinetix 6200/6500 power specifications in the Kinetix Servo Drives Technical Data, publication KNX-TD003 .

| IMPORTANT   | If using an autotransformer, make sure that the phase to neutral/ground voltages do not exceed the input voltage ratings of the drive.                                                                                                 |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Use a form factor of 1.5 for three-phase power (where form factor is used to compensate for transformer, drive module, and motor losses, and to account for utilization in the intermittent operating area of the torque speed curve). |

For example, to size a transformer to the voltage requirements of a 2094-BC01-M01-M integrated axis module:

2094-BC01-M01-M = 6 kW continuous x 1.5 = 9.0 KVA transformer

## AC Line Filter Selection

These AC line filters are available for your servo drive input power.

Table 7 - Kinetix 6200/6500 (three-phase) AC Line Filter Selection

| Drive Cat. No.                                | Voltage          | Current A @ 50 °C (122 °F)   | Weight, approx kg (lb)   | AC Line Filter Cat. No.      |
|-----------------------------------------------|------------------|------------------------------|--------------------------|------------------------------|
| 2094-BC01-MP5-M                               | 500V AC 50/60 Hz |                              |                          | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-BC01-M01-M                               | 500V AC 50/60 Hz |                              |                          | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-BC02-M02-M                               | 500V AC 50/60 Hz |                              |                          | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-BC04-M03-M 75 5.2 (11.4) 2090-XXLF-375B  | 500V AC 50/60 Hz |                              |                          |                              |
| 2094-BC07-M05-M 100 9.5 (20.9) 2090-XXLF-3100 | 500V AC 50/60 Hz |                              |                          |                              |

Refer to the Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for additional AC line filter specifications.

## Circuit Breaker/Fuse Options

The 2094-BCxx-Mxx-M and 2094-BMxx-M drive modules, and the Kinetix 6000M integrated drive-motor system (2094-SEPM-B24-S IPIM module and MDF-SBxxxxx IDM units) use internal solid-state motor shortcircuit protection and, when protected by suitable branch circuit protection, are rated for use on a circuit capable of delivering up to 200,000 A (fuses) and 65,000 A (circuit breakers).

Table 8 - Control and DC-bus Circuit Protection Specifications

| IAM Module Cat. No.                        | Control Input Power DC-bus Power     | Control Input Power DC-bus Power             |                                |
|--------------------------------------------|--------------------------------------|----------------------------------------------|--------------------------------|
| IAM Module Cat. No.                        | Bussmann Fuse (1)                    | Allen-Bradley® Circuit Breaker  (2) (non-UL) | Bussmann Fuse  Mersen Fuse (3) |
| 2094-BC01-MP5-M                            | FNQ-R-10 (10 A) or FNQ-R-7.5 (7.5 A) | 1492-SPM2D060 or 1492-SPM1D150 FNQR10 (10 A) or FNQR75 (75 A) 1492SPM2D060 or 1492SPM1D150 2094-BC02-M02-M FWJ-40A A70QS40-4 HSJ40                                              | FWJ-20A14F DCT20-2 HSJ20       |
| 2094-BC01-M01-M                            | FNQ-R-10 (10 A) or FNQ-R-7.5 (7.5 A) | 1492-SPM2D060 or 1492-SPM1D150 FNQR10 (10 A) or FNQR75 (75 A) 1492SPM2D060 or 1492SPM1D150 2094-BC02-M02-M FWJ-40A A70QS40-4 HSJ40                                              |                                |
| 2094-BC04-M03-M FWJ-70A A70QS70-4 HSJ70    | FNQ-R-10 (10 A) or FNQ-R-7.5 (7.5 A) | 1492-SPM2D060 or 1492-SPM1D150 FNQR10 (10 A) or FNQR75 (75 A) 1492SPM2D060 or 1492SPM1D150 2094-BC02-M02-M FWJ-40A A70QS40-4 HSJ40                                              |                                |
| 2094-BC07-M05-M FWJ-125A A70QS125-4 HSJ125 | FNQ-R-10 (10 A) or FNQ-R-7.5 (7.5 A) | 1492-SPM2D060 or 1492-SPM1D150 FNQR10 (10 A) or FNQR75 (75 A) 1492SPM2D060 or 1492SPM1D150 2094-BC02-M02-M FWJ-40A A70QS40-4 HSJ40                                              |                                |

(1) Use FNQ-R-7.5 circuit breaker for higher single -cycle inrush current capability. This is recommended when the continuous control-power current exceeds 3.0 A.

(2) Use 1492-SPM1D150 circuit breaker for higher single -cycle inrush current capability. This is recommended when the continuous control-power current exceeds 3.0 A.

(3) Mersen fuses were formerly known as Ferraz-Shawmut.

## Input Power Circuit Protection (LIM)

The 2094-BL02 line interface module (LIM) contains supplementary protection devices and, when protected by suitable branch circuit protection, is rated for use on a circuit capable of delivering up to 5000 A. When this module is used, protection on the line side of the LIM module is required. Fuses must be class J or CC only.

The 2094-BLxxS and 2094-XL75S-Cx LIM modules contain branch circuit rated devices suitable for use on a circuit capable of delivering up to 65,000 A (400Vclass).

Refer to the Line Interface Module Installation Instructions, publication 2094-IN005, for power specifications and more information on using the LIM module.

Refer to Input Power Circuit Protection (without LIM) on page 31 when your drive system does not include the LIM module.

Table 9 - UL/CSA Circuit Protection Specifications

| IAM Module Cat. No. Drive Voltage (three-phase) nom   | Fuses (Bussmann) Cat. No.   | Miniature CB Cat. No.   | Motor Protection CB, Self-protected CMC Cat. No.   | Molded Case CB Cat. No.   |
|-------------------------------------------------------|-----------------------------|-------------------------|----------------------------------------------------|---------------------------|
| 2094-BC01-MP5-M 360…480V                              | KTK-R-20 (20 A) Class CC    | 1489-M3D300             | 140M-F8E-C32                                       | –                         |
| 2094-BC01-M01-M 360…480V                              | KTK-R-20 (20 A) Class CC    | 1489-M3D300             | 140M-F8E-C32                                       | –                         |
| 2094-BC02-M02-M 360…480V                              | KTK-R-30 (30 A) Class CC    | –                       | 140M-F8E-C45                                       | –                         |
| 2094-BC04-M03-M 360…480V                              | LPJ-45SP (45 A) Class J     | –                       | –                                                  | 140G-G6C3-C50             |
| 2094-BC07-M05-M 360…480V                              | LPJ-80SP (80 A) Class J     | –                       | –                                                  | 140G-G6C3-C90             |

## Table 10 - EN/IEC (non-UL/CSA) Circuit Protection Specifications

| IAM Module Cat. No. Drive Voltage (three-phase) nom   | Miniature CB Cat. No.     | Motor Protection CB Cat. No.   | Molded Case CB Cat. No.   |
|-------------------------------------------------------|---------------------------|--------------------------------|---------------------------|
| 2094-BC01-MP5-M 360…480V                              | 1492-SPM3D300 1489-M3D300 | 140M-F8E-C32                   | –                         |
| 2094-BC01-M01-M 360…480V 140M-F8E-C32                 | 1492-SPM3D300 1489-M3D300 |                                | –                         |
| 2094-BC02-M02-M 360…480V 1492-SPM3D400                |                           | 140M-F8E-C45                   | –                         |
| – 2094-BC04-M03-M 360…480V                            | – –                       |                                | 140G-G6C3-C50             |
| 2094-BC07-M05-M 360…480V                              | – –                       |                                | 140G-G6C3-C90             |

Refer to the Kinetix Servo Drives Technical Data, publication KNX-TD003, for additional power specifications for your IAM power module.

Input Power Circuit Protection (without LIM)

The fuses and Allen-Bradley circuit breakers shown in Table 9 and Table 10 are recommended for use with 2094-BCxx-Mxx-M IAM power modules when the line interface module (LIM) is not used.

## IMPORTANT

LIM Module (catalog number 2094-BLxxS) provides branch circuit protection to the IAM power module. Follow all applicable NEC and local codes.

## Enclosure Selection

This example is provided to assist you in sizing an enclosure for your Bulletin 2094 drive system. The example system consists of these components:

- 6-axis Bulletin 2094 servo drive system
- Line Interface Module (LIM)
- ControlLogix® chassis and modules (controller)

Size the Bulletin 2094 servo drive and LIM module and use the results to predict the amount of heat dissipated into the enclosure. You also need heat dissipation data from other equipment inside the enclosure (such as the ControlLogix controller). Once the total amount of heat dissipation (in watts) is known, you can calculate the minimum enclosure size.

Table 11 - Bulletin 2094 System Heat Dissipation Example

| Enclosure Component Description                                             | Loading (1)  Heat Dissipation  (1) watts               |
|-----------------------------------------------------------------------------|--------------------------------------------------------|
| 2094-BC02-M02-M  Integrated axis module (IAM), 400/460V                     | 15 kW (converter section) 20% 44                       |
| 2094-BC02-M02-M  Integrated axis module (IAM), 400/460V                     | 15 A (inverter section) 40% 72                         |
| 2094-BM02-M Axis module (AM), 400/460V, 15 A 60% 93                         |                                                        |
| 2094-BM02-M Axis module (AM), 400/460V, 15 A 60% 93                         |                                                        |
| 2094-BM01-M Axis module (AM), 400/460V, 9 A 40% 73                          |                                                        |
| 2094-BM01-M Axis module (AM), 400/460V, 9 A 40% 73                          |                                                        |
| 2094-BM01-M Axis module (AM), 400/460V, 9 A 20% 57                          |                                                        |
| 2094-BL25S Line interface module (LIM), 400/460V, 25 A; 24V DC 20 A 100% 43 |                                                        |
| 2094-PRS6 Power rail, 460V, 6 axis – 0                                      |                                                        |
| 2090-XB33-32 Resistive brake module (RBM), 33 A, 32                        | – 30                                                   |
|                                                                             | Total Kinetix 6200 and Kinetix 6500 system wattage 578 |

Table 12 - ControlLogix System Heat Dissipation Example

| Enclosure Component  Description                | Backplane Power Load  (1) watts        | Heat Dissipation  (1) watts            |
|-------------------------------------------------|----------------------------------------|----------------------------------------|
| 1756-M08SE 8-axis Sercos interface module 3.2 0 |                                        |                                        |
| 1756-L5563 L63 ControlLogix processor 4.5 0     |                                        |                                        |
| 1756-IB16D 16 -point input module 0.84 5.8      |                                        |                                        |
| 1756-OB16D 16 -point output module 4.64 3.3     |                                        |                                        |
| 1756-ENxTx                                      | EtherNet/IP communication module 4.0 0 |                                        |
| Backplane total                                 | 17.18 (2)                              | –                                      |
| 1756-PB72 24V DC ControlLogix power supply –    |                                        | 25 (2)                                 |
| 1756-A7 7-slot mounting chassis – –             |                                        |                                        |
| Total ControlLogix system wattage 34.1          | Total ControlLogix system wattage 34.1 | Total ControlLogix system wattage 34.1 |

Figure 9 - ControlLogix Real Power

<!-- image -->

For backplane power loading requirements of other ControlLogix power supplies, refer to the ControlLogix Selection Guide, publication 1756-SG001 .

In this example, the amount of power dissipated inside the cabinet is the sum of the Bulletin 2094 system value (578 W) and the ControlLogix system value (34 W) for a total of 612 W.

With no active method of heat dissipation (such as fans or air conditioning) either of these approximate equations can be used.

|                                                                                                                     | Metric Standard English   |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|
| Where T is temperature difference between inside air and ° p outside ambient (°C), Q is heat generated in enclosure (Watts), and A is enclosure surface area (m 2 ). The exterior surface of all six sides of an enclosure is calculated as: A =  0.38Q 1.8T - 1.1                                                                                                                     | A =  4.08Q T - 1.1        |
| A = 2dw + 2dh + 2wh A = (2dw + 2dh + 2wh) / 144                                                                     | Where T is temperature difference between inside air and ° p outside ambient (°F), Q is heat generated in enclosure ² g (Watts), and A is enclosure surface area (ft²). The exterior surface of all six sides of an enclosure is calculated as:                           |
| Where d (depth), w (width), and h (height) are in meters. Where d (depth), w (width), and h (height) are in inches. |                           |

Total system watts dissipated (Q) was calculated at 612 W. The maximum ambient rating of the Bulletin 2094 system is 50 °C (122 °F) and if the maximum environmental temperature is 30 °C (86 °F), then T=20 in the equation below.

<!-- formula-not-decoded -->

In this example, the enclosure must have an exterior surface of 6.66 m 2 . If any portion of the enclosure is not able to transfer heat, do not include that portion in the calculation.

Because the minimum cabinet depth to house the 460V drive (selected for this example) is 302 mm (11.9 in.), then the cabinet needs to be approximately 2500 mm (high) x 950 mm (wide) x 302 mm (deep).

<!-- formula-not-decoded -->

Because this cabinet size is considerably larger than what is necessary to house the system components, consider some means of cooling in a smaller cabinet to be more efficient. Contact your cabinet manufacturer for options available to cool your cabinet.

Table 13 - Power Dissipation Specifications

| Bulletin 2094 Drive Modules (1)                    | Usage as % of Rated Power Output (watts)                                                                                                                       | Usage as % of Rated Power Output (watts)                                                                                                                       | Usage as % of Rated Power Output (watts)                                                                                                                       | Usage as % of Rated Power Output (watts)                                                                                                                       | Usage as % of Rated Power Output (watts)                                                                                                                       |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                    |                                                                                                                                                                | 20% 40% 60% 80% 100%                                                                                                                                           |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| IAM (converter) power module  (2)                  |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC01-MP5-M                                    | 18 21 25 29                                                                                                                                                    | 34                                                                                                                                                             |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC01-M01-M                                    | 18 21 25 29                                                                                                                                                    | 33                                                                                                                                                             |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC02-M02-M 36 44 54 64 75                     |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC04-M03-M 50 67 87 110 135                   |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC07-M05-M 71 101 137 179 226                 |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| IAM (inverter) module or AM power module  (2)      |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC01-MP5-S or 2094-BMP5-M 46 54 61 69 77      |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC01-M01-S or 2094-BM01-M 57 73 90 108 126    |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC02-M02-S or 2094-BM02-M 53 72 93 116 142    |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC04-M03-S or 2094-BM03-M 94 130 169 211 255  |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| 2094-BC07-M05-S or 2094-BM05-M 121 183 252 326 407 |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| Shunt module - 2094-BSP2 68 121 174 227 280        |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                |
| IPIM module - 2094-SEPM-B24-S                      | To calculate power dissipation for IPIM modules on your 2094 power rail, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 | To calculate power dissipation for IPIM modules on your 2094 power rail, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 | To calculate power dissipation for IPIM modules on your 2094 power rail, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 | To calculate power dissipation for IPIM modules on your 2094 power rail, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 | To calculate power dissipation for IPIM modules on your 2094 power rail, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 |

Table 14 - Minimum Cabinet Depth

2094-BSP2 272 mm (10.7 in.) 2094-SEPM-B24-S 263 mm (10.3 in.)

| Drive Cat. No.                                                          | Cabinet Depth, min (1)   |
|-------------------------------------------------------------------------|--------------------------|
| 2094-BC01-Mxx-M, 2094-BC02-M02-M, 2094-BMP5-M, 2094-BM01-M, 2094-BM02-M | 302 mm (11.9 in.)        |

| Drive Cat. No.                                               | Cabinet Depth, min (1)   |
|--------------------------------------------------------------|--------------------------|
| 2094-BC04-M03 - M, 2094-BC07-M05-M, 2094-BM03-M, 2094-BM05-M | 302 mm (11.9 in.)        |

## Minimum Clearance Requirements

This section provides information to assist you in sizing your cabinet and positioning your Bulletin 2094 system components.

| IMPORTANT   | Mount the module in an upright position. Do not mount the module on its side.   |
|-------------|---------------------------------------------------------------------------------|

Figure 10 illustrates minimum clearance requirements for proper airflow and installation:

- Additional clearance is required for the cables and wires connected to the top and front of the drive.
- Additional clearance left and right of the power rail is required when the drive is mounted adjacent to noise sensitive equipment or clean wireways.

Figure 10 - Minimum Clearance Requirements

Clearance above for airflow and installation.

<!-- image -->

| Drive Cat. No. F                       |                   |
|----------------------------------------|-------------------|
| 2094-BC01-Mxx-M 2094-BC02-M02 - M (11.2) in. 2094-BMP5-M, 2094BM01M , 2094-BM01-M ,  2094-BM02-M                                        | 285 mm            |
| 2094-SEPM-B24-S 2094-BSP2              | 287 mm (11.3) in. |
| 2094-BC04-M03 - M 2094-BM03-M          | 375 mm            |
| (14.7) in. 2094-BC07-M05-M 2094-BM05-M | 375 mm            |

Refer to Power Dissipation Specifications on page 34 , and Kinetix Servo Drive Specifications Technical Data, publication KNX-TD003, for Kinetix 6000 drive dimensions.

- (1) The power rail (slim), catalog number 2094-PRSx, extends left and right of the first and last module 5.0 mm (0.20 in.). The Bulletin 2094-PRx power rail extends approximately 25.4 mm (1.0 in.) left of the IAM module and right of the last module mounted on the rail.

Minimum Cabinet Depth

## Electrical Noise Reduction

This section outlines best practices that minimize the possibility of noiserelated failures as they apply specifically to Kinetix 6200 and Kinetix 6500 system installations. For more information on the concept of high-frequency (HF) bonding, the ground plane principle, and electrical noise reduction, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## Bond Modules

Bonding is the practice of connecting metal chassis, assemblies, frames, shields, and enclosures to reduce the effects of electromagnetic interference (EMI).

Unless specified, most paints are not conductive and act as insulators. To achieve a good bond between power rail and the subpanel, surfaces need to be paint-free or plated. Bonding metal surfaces creates a low-impedance return path for high-frequency energy.

## IMPORTANT

To improve the bond between the power rail and subpanel, construct your subpanel out of zinc plated (paint-free) steel.

Improper bonding of metal surfaces blocks the direct return path and allows high-frequency energy to travel elsewhere in the cabinet. Excessive highfrequency energy can affect the operation of other microprocessor-controlled equipment.

These illustrations show details of recommended bonding practices for painted panels, enclosures, and mounting brackets.

Figure 11 - Recommended Bonding Practices for Painted Panels

<!-- image -->

## Bond Multiple Subpanels

Bonding multiple subpanels creates a common low impedance exit path for the high frequency energy inside the cabinet. If subpanels are not bonded together, and do not share a common low impedance path, the difference in impedance can affect networks and other devices that span multiple panels:

- Bond the top and bottom of each subpanel to the cabinet by using 25.4 mm (1.0 in.) by 6.35 mm (0.25 in.) wire braid. As a rule, the wider and shorter the braid is, the better the bond.
- Scrape the paint from around each fastener to maximize metal-to-metal contact.

Figure 12 - Multiple Subpanels and Cabinet Recommendations

<!-- image -->

## Establish Noise Zones

Observe these guidelines when the 2094-BLxxS or 2094-XL75S-Cx LIM module is used in the Bulletin 2094 system and mounted left of the IAM module with the AC (EMC) line filter mounted above the LIM module:

- The clean zone (C) is to the right and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the left and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is from the filter output to IAM module. Shielded cable is required on the EMC filter (load side) and the braided shield attached to the clamp provided.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.
- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Figure 13 - Noise Zones (LIM mounted left of IAM module)

<!-- image -->

Observe these guidelines when the 2094-BLxxS or 2094-XL75S-Cx LIM module is used in the Bulletin 2094 system and mounted right of the IAM module with the AC (EMC) line filter mounted behind the IAM module:

- The clean zone (C) is to the left and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the right and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is from the filter output to IAM module. Shielded cable is required on the EMC filter (load side) and the braided shield attached to the clamp provided.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.
- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Figure 14 - Noise Zones (LIM with EMC filter behind IAM module)

<!-- image -->

Observe these guidelines when the 2094-BLxxS or 2094-XL75S-Cx LIM module is used in the Bulletin 2094 system and mounted right of the drive with the AC (EMC) line filter mounted behind the LIM module:

- The clean zone (C) is to the left and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the right and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is from the filter output to drive. Shielded cable is required on the EMC filter (load side) and the braided shield attached to the clamp (when provided).
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.
- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (3) Only the 2094-ALxxS and 2094-XL75S-Cx LIM modules are compatible with the 2094 mounting brackets. The 2094-BLxxS, 2094AL09, and 2094-BL02 LIM modules are not compatible.

Figure 15 - Noise Zones (EMC filter behind LIM module)

<!-- image -->

Keep the DC common-bus cable (very dirty) segregated from all other cables (not in a wireway) when the 2094-BLxxS or 2094-XL75S-Cx LIM module is used in a DC common-bus configuration and the follower IAM module is mounted below the leader IAM module.

Figure 16 - Noise Zones (DC common bus)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when the 2094-BL02 LIM module is used in the Bulletin 2094 system and mounted left of the IAM module:

- The clean zone (C) is to the right and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the left and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is limited to where the LIM module VAC output jumpers over to the IAM module. Shielded cable is required only if the very dirty cables enter a wireway.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.

This layout is preferred due to the reduced size of the very dirty zone.

Figure 17 - Noise Zones (LIM mounted left of IAM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when the 2094-BL02 LIM module is used in the Bulletin 2094 system and mounted above the IAM module:

- The clean zone (C) is to the right and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the left and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The LIM VAC output is very dirty (VD). Use shielded cable with a braid clamp attached at both ends of the cable to reduce the rating to dirty (D).
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.
- (1) For examples of shield clamp attachment, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (2) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.

Figure 18 - Noise Zones (LIM mounted above IAM module)

<!-- image -->

(3) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when your system includes the 2094-SEPM-B24-S IPIM module. In this example, a 2094-BL02 LIM module is used in the Bulletin 2094 system and mounted left of the IAM module:

- Establish clean (C) and dirty zones (D) similar to other Bulletin 2094 drive systems.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.
- IPIM digital input wires are noise sensitive and belong with the fiberoptic cables in the clean zone.
- Ethernet cables are noise sensitive and belong in the clean zone, however, they are connected only when programming the IPIM module.
- IDM network cables, although noise sensitive by nature, are shielded and can be routed with the hybrid cables outside of the enclosure.
- The Bulletin 2090 hybrid cable is dirty and belongs in the dirty zone.

This layout is preferred due to the reduced size of the very dirty zone.

Figure 19 - Noise Zones (Bulletin 2094 power rail with IPIM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when individual input power components are used in the Bulletin 2094 system and the Bulletin 2094 LIM module is not used:

- The clean zone (C) is beneath the Bulletin 2094 system and includes the I/O wiring, feedback cable, and DC filter (gray wireway).
- The dirty zone (D) is above the Bulletin 2094 system (black wireway) and includes the circuit breakers, transformer, 24V DC power supply, contactors, AC line filter, and motor power cables.
- The very dirty zone (VD) is limited to where the AC line (EMC) filter VAC output jumpers over to the IAM module. Shielded cable is required only if the very dirty cables enter a wireway.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.
- (1) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.
- (2) When space to the right of the IAM does not permit 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (3) This is a clean 24V DC available for any device that requires it. The 24V enters the clean wireway and exits to the right.
- (4) This is a dirty 24V DC available for motor brakes and contactors. The 24V enters the dirty wireway and exits to the left.

Figure 20 - Noise Zones (without LIM module)

<!-- image -->

Observe these guidelines when installing your Logix 5000™ Sercos interface module:

- The clean zone (C) is beneath the less noisy modules (I/O, analog, encoder, registration, an so forth (gray wireway).
- The dirty zone (D) is above and below the power supply and noisy modules (black wireway).
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone. Ethernet cables are noise sensitive and belong in the clean zone.

Figure 21 - Noise Zones (ControlLogix chassis)

<!-- image -->

## Cable Categories for Kinetix 6200 and Kinetix 6500 Systems

These tables indicate the zoning requirements of cables connecting to the Kinetix 6200 and Kinetix 6500 drive components.

Table 15 - IAM Power Module (converter side)

|                                            | Zone Method   | Zone Method   | Zone Method    |                |
|--------------------------------------------|---------------|---------------|----------------|----------------|
| Wire/Cable Connector                       | Very Dirty    | Dirty Clean   | Ferrite Sleeve | Shielded Cable |
| CTRL 1 and 2 CPD X                         |               |               |                |                |
| DC-/DC+ (unshielded cable)                 | X             |               |                |                |
| IPD IPDL1, L2, L3 (shielded cable) X X     |               |               |                |                |
| L1, L2, L3 (unshielded cable) X            |               |               |                |                |
| CONT EN- and CONT EN+ (M1 contactor) CED X |               |               |                |                |

Table 16 - AM Power Module or Axis Module (inverter side)

|                                   |    | Zone Method   | Zone Method   | Zone Method   |                |                |
|-----------------------------------|----|---------------|---------------|---------------|----------------|----------------|
| Wire/Cable Connector              |    | Very Dirty    |               | Dirty Clean   | Ferrite Sleeve | Shielded Cable |
| U, V, W (motor power) MP X X      |    |               |               |               |                |                |
| COM, PWR (24V DC), filtered (1)   | BC |               |               | X             |                |                |
| COM, PWR (24V DC), unfiltered (2) | BC |               | X             |               |                |                |
| DBRK-, DBRK+ (resistive brake) X  | BC |               |               |               |                |                |
| MBRK-, MBRK+ (motor brake) X      | BC |               |               |               |                |                |

## Table 17 - Control Module

|                                                | Zone Method   | Zone Method   | Zone Method               |                |
|------------------------------------------------|---------------|---------------|---------------------------|----------------|
| Wire/Cable Connector                           | Very Dirty    | Dirty Clean   | Ferrite Sleeve            | Shielded Cable |
| Motor feedback MF X X                          |               |               |                           |                |
| Auxiliary feedback                             |               |               | X X                       |                |
| IOD IODRegistration and I/O X X                |               |               |                           |                |
|                                                | Safety X      |               |                           |                |
| Fiber-optic (Sercos) Rx and Tx No restrictions |               |               |                           |                |
|                                                |               |               | Ethernet PORT1, PORT2 X X |                |

## Table 18 - Line Interface Module (LIM)

|                                 | Zone Method   | Zone Method   | Zone Method    |                |
|---------------------------------|---------------|---------------|----------------|----------------|
| Wire/Cable Connector            | Very Dirty    | Dirty Clean   | Ferrite Sleeve | Shielded Cable |
| VAC line (main input) IPL X     |               |               |                |                |
| Aux power input APL X           |               |               |                |                |
| VAC load (shielded option)  OPL |               |               | X X            |                |
| OPL VAC load (unshielded option) X                                 |               |               |                |                |
| Control power output CPL X      |               |               |                |                |
| MBRK PWR, MBRK COM P1L/PSL X    |               |               |                |                |
| Status I/O IOL X                |               |               |                |                |
| Aux power output P2L X          |               |               |                |                |

## Table 19 - Shunt Module

|                                  | Zone Method   | Zone Method    | Zone Method    |
|----------------------------------|---------------|----------------|----------------|
| Wire/Cable Connector Dirty Clean | Very Dirty    | Ferrite Sleeve | Shielded Cable |
| COL, DC+ (shielded option)  RC   |               | X X            |                |
| RC COL, DC+ (unshielded option) X                                  |               |                |                |
| Thermal switch TS X X            |               |                |                |
| Fan (if present) – X             |               |                |                |

## Table 20 - IDM Power Interface Module (IPIM)

| Wire/Cable                                                                               | Zone Method                 | Zone Method                                          | Zone Method                 |                             |                             |
|------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|-----------------------------|-----------------------------|-----------------------------|
|                                                                                          |                             | Very Dirty Dirty Clean Ferrite Sleeve Shielded Cable |                             |                             |                             |
| Hybrid DC bus power, control power, inter-module communication, and Safe Torque Off  (1) |                             | X X                                                  |                             |                             |                             |
|                                                                                          |                             | Enable input X X                                     |                             |                             |                             |
|                                                                                          | Fiber-optic No restrictions | Fiber-optic No restrictions                          | Fiber-optic No restrictions | Fiber-optic No restrictions | Fiber-optic No restrictions |
| Ethernet network X X                                                                     |                             |                                                      |                             |                             |                             |
| IDM network (1)                                                                          |                             | X X                                                  |                             |                             |                             |

## Table 21 - Resistive Brake Module (RBM)

| Wire/Cable Connections                              |    | Zone Method                                                  | Zone Method   |
|-----------------------------------------------------|----|--------------------------------------------------------------|---------------|
|                                                     |    | Very Dirty Dirty Clean Ferrite Sleeve Shielded Cable         |               |
| Resistive brake module coil power TB3-6 and TB3-7 X |    |                                                              |               |
| Resistive brake module I/O  TB1-1…TB1-5 and TB3-8   | X  |                                                              |               |
|                                                     |    | Resistive brake module drive and motor power TB1 and TB2 X X |               |
| 230V power TB4 X                                    |    |                                                              |               |

## Noise Reduction Guidelines for Drive Accessories

Refer to this section when mounting an AC (EMC) line filter or external shunt module for guidelines designed to reduce system failures caused by excessive electrical noise.

AC Line Filters

Observe these guidelines when mounting your AC (EMC) line filter (refer to the figure on page 46 for an example):

- Mount the AC line filter on the same panel as the Kinetix 6200 and Kinetix 6500 drive and as close to the power rail as possible.
- Good HF bonding to the panel is critical. For painted panels, refer to the examples on page 37 .
- Segregate input and output wiring as far as possible.

## IMPORTANT

CE and UK test certification applies only to AC line filter and single power rail. Sharing a line filter with multiple power rails can perform satisfactorily, but the user takes legal responsibility.

## External Shunt Modules

Observe these guidelines when mounting your external shunt module outside the enclosure:

- Mount circuit components and wiring in the very dirty zone or in an external shielded enclosure. Run shunt power and fan wiring inside metal conduit to minimize the effects of EMI and RFI.
- Mount resistors (other than metal-clad) in a shielded and ventilated enclosure outside the cabinet.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.
- Route thermal switch and fan wires separate from shunt power.

Figure 22 - External Shunt Module Outside the Enclosure

<!-- image -->

When mounting your shunt module inside the enclosure, follow these additional guidelines:

- Mount metal-clad modules anywhere in the dirty zone, but as close to the Bulletin 2094 drive system as possible.
- Route shunt power wires with motor power cables.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.
- Separate shunt power cables from other sensitive, low voltage signal cables.

Figure 23 - External Shunt Module Inside the Enclosure

<!-- image -->

## Resistive Brake Modules

## Observe these guidelines when mounting your RBM module:

- Mount circuit components and wiring in the dirty zone or in an external shielded enclosure. If mounting the RBM module in a separate ventilated shielded enclosure, run wiring inside metal conduit to minimize the effects of EMI and RFI.
- Keep unshielded wiring as short as possible. Keep wiring as flat to the cabinet as possible.
- Route RBM module power and I/O cables separate from other sensitive low voltage signal cables.

Figure 24 - Noise Zones (RBM mounted above AM power module)

<!-- image -->

## Motor Brake and Thermal Switch

The thermal switch and brake are mounted inside the motor, but how you connect to the axis module depends on the motor series.

Refer to Wire the Motor/Resistive Brake (BC) Connector on page 111 for wiring guidelines. Refer to Axis Module/Rotary Motor Wiring Examples beginning on page 226 for the interconnect diagram of your drive/motor combination.

## Before You Begin

<!-- image -->

## Mount the Kinetix 6200 and Kinetix 6500 Drive System

This chapter provides the system installation procedures for mounting your Kinetix® 6200/6500 drive components on the Bulletin 2094 power rail.

| Topic Page                         |
|------------------------------------|
| Before You Begin 53                |
| Determine Mounting Order 54        |
| Mount Modules on the Power Rail 55 |
| Mount the Control Modules 58       |

This procedure assumes you have prepared your panel, mounted your Bulletin 2094 power rail, and understand how to bond your system. For installation instructions regarding equipment and accessories not included here, refer to the instructions that came with those products.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Bulletin 2094 power rail and drive modules prior to applying power. Once power is applied, connector terminals can have voltage present even when not in use.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

Before you begin, consider your Bulletin 2094 power rail installation and using 2094 mounting brackets.

## Install 2094 Mounting Brackets

You can use Bulletin 2094 mounting brackets to mount the power rail or LIM module over the AC line filter. Refer to the 2094 Mounting Brackets Installation Instructions, publication 2094-IN008, when using mounting brackets with your Kinetix 6200 and Kinetix 6500 drive system.

## Determine Mounting Order

## Install the 2094 Power Rail

The Bulletin 2094 power rail comes in lengths to support one IAM module and up to seven additional AM/IPIM modules, or up to six additional AM/IPIM modules and one shunt module. The connector pins for each slot are covered by a protective cover. The cover is designed to protect the pins from damage and make sure that no foreign objects lodge between the pins during installation. Refer to the Kinetix 6000 Power Rail Installation Instructions, publication 2094-IN003, when installing your power rail.

<!-- image -->

ATTENTION: To avoid damage to the power rail during installation, do not remove the protective covers until the module for each slot is ready for mounting.

The Kinetix 6000M integrated drive-motor (IDM) system is supported by Bulletin 2094 (400V-class) power rail configurations. You can mount up to four IDM power interface (IPIM) modules on the Bulletin 2094 power rail. Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for more information.

Mount IAM, AM/IPIM, shunt, and slot-filler modules in the order (left to right) as shown in Figure 25. Mount axis modules and the IPIM module according to power utilization (highest to lowest) from left to right starting with the highest power utilization.

Power utilization is the average power (kW) consumed by a servo axis. If Motion Analyzer software was used to size the axis, the calculated axis power required can be used for the power utilization value. If Motion Analyzer software was not used, you can use the continuous power value (kW) for each module to determine mounting order.

Table 22 - Kinetix 6200/6500 (400V-class) Axis Modules

|                              | Attribute 2094-BMP5-M 2094-BM01-M 2094-BM02-M 2094-BM03-M 2094-BM05-M   |
|------------------------------|-------------------------------------------------------------------------|
| Continuous Power Output, nom | 1.8 kW 3.9 kW 6.6 kW 13.5 kW 22.0 kW                                    |

Table 23 - Kinetix 6000M (400V-class) IPIM Module

| Attribute 2094-SEPM-B24-S            |
|--------------------------------------|
| Continuous Power Output, nom 15.0 kW |

## Mount Modules on the Power Rail

Figure 25 - Module Mounting Order Example

<!-- image -->

## IMPORTANT

The IAM module must be positioned in the leftmost slot of the power rail. Position your AM/IPIM modules, shunt module, and slot-filler modules to the right of the IAM module.

The shunt module must be installed to the right of the last AM/IPIM module. Only slot-filler modules can be installed to the right of the shunt module.

Do not mount the shunt module on power rails with a follower IAM module. Common-bus follower IAM modules disable the internal, rail mounted, and external shunt modules.

SHOCK HAZARD: To avoid personal injury due to electrical shock, place a 2094-PRF slot-filler module in all empty slots on the power rail. Any power rail connector without a module installed disables the Bulletin 2094 system; however, control power is still present.

<!-- image -->

Follow these steps to mount the IAM, AM, IPIM, shunt, and slot-filler modules.

<!-- image -->

All modules mount to the power rail by using the same technique; however, only the IAM module is used in the examples.

1. Remove the protective covers from the power rail connectors.

## IMPORTANT

The IAM module must be positioned in the leftmost slot of the power rail. Position your axis modules, shunt module, and slot-filler modules to the right of the IAM module.

2. Determine the next available slot and module for mounting.

<!-- image -->

ATTENTION: To avoid damage to the pins on the back of each IAM, AM, IPIM, shunt, and slot-filler module and to make sure that module pins mate properly with the power rail, hang modules as shown in step 3 through step 6 .

The power rail must be mounted vertically on the panel before hanging modules on the power rail. Do not mount modules if the power rail is horizontal.

3. Hang the mounting bracket from the slot on the power rail.
4. Pivot module downward and align the guide pins on the power rail with the guide pin holes in the back of the module.

<!-- image -->

<!-- image -->

<!-- image -->

The IAM module can have two or three power rail connectors and guide pins, the AM module can have one or two, all other modules have one.

5. Gently push the module against the power rail connectors and into the final mounting position.
6. Use 2.26 N·m (20 lb·in) torque to tighten the mounting screws.

<!-- image -->

<!-- image -->

## IMPORTANT

There are two mounting screws when mounting 2094-BC04-M03-M, and 2094-BC07-M05-M (double-wide) IAM modules, and 2094-BM03-M and 2094BM05-M (double-wide) AM modules.

Repeat step 1 through step 6 for each AM, IPIM, shunt, or slot-filler module in your Bulletin 2094 drive system

## Mount the Control Modules

The IAM and AM power modules are equipped with two mounting hooks and a threaded hole. The control module has two mounting studs, guide pins, and a captive screw for mating the control module with a power module.

## IMPORTANT

For convenience and ease of use, mount the IAM and AM power modules on the power rail before mounting the control modules.

When the power modules are placed on a flat surface, with the power-rail connectors facing down, the mounting screw that extends from the front of the drive and fastens to the power rail pushes back and interferes with the control module installation.

Follow these steps to mount control modules to either IAM (inverter) power modules or AM power modules. In this procedure, an IAM power module is shown.

1. Remove all input power from the IAM power module.

Verify that the Power-applied indicator is off. When the indicator is on, voltage is present on the IAM and AM power module signal connectors.

<!-- image -->

ATTENTION: To avoid damage to equipment, do not mount your Bulletin 2094 control module to the power module when the Power-applied indicator is on. Remove all input power from the IAM power module before mounting the control module.

2. Position the control module in front of the power module.

<!-- image -->

3. Guide the control module mounting studs so they engage with the power module hooks.
4. Pivot the control module toward the power module to engage the signal connectors and guide pins.
6. Repeat step 2 through step 5 to mount a control module onto each IAM and AM power module installed on your Bulletin 2094 power rail.

<!-- image -->

<!-- image -->

## Notes:

<!-- image -->

## Connector Data and Feature Descriptions

This chapter illustrates drive connectors and indicators, including connector pinouts, and provides descriptions for Kinetix® 6200/6500 drive features.

| Topic Page                                       |
|--------------------------------------------------|
| 2094 Power Module and Control Module Features 62 |
| Control Signal Specifications 69                 |
| Power and Relay Specifications 73                |
| Feedback Specifications 79                       |
| Safe Speed Monitor Safety Features 84            |
| Safe Torque Off Safety Features 85               |

For the Kinetix 6000M integrated drive-motor (IDM) unit and IDM power interface module (IPIM) connector locations and signal descriptions, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

## 2094 Power Module and Control Module Features

Use these illustrations to identify the connectors and indicators for the IAM/AM power modules and control modules. Sercos interface and Ethernet network connectors for the Kinetix 6000M IPIM module are also shown. For the remainder of the IPIM module features and indicators, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Figure 26 - IAM Power Module Features and Indicators

<!-- image -->

| Item Description                       |
|----------------------------------------|
| 1 Motor cable shield clamp             |
| 2 Motor power (MP) connector           |
| 3 Motor/resistive brake (BC) connector |
| 4 Power-applied indicator              |
| 5 Mounting screw                       |

Figure 27 - AM Power Module Features and Indicators

<!-- image -->

## Figure 28 - Control Module Features and Indicators (Sercos)

|    | Item Description                                     |
|----|------------------------------------------------------|
|    | 1 Guide pins (2x)                                    |
|    | 2 Captive screw                                      |
| 3  | Sercos communication rate and optical power switches |
| 4  | Sercos transmit (Tx) Connector (1)                   |
| 5  | Sercos receive (Rx) Connector (1)                    |

(1) For the remainder of the IPIM module features and indicators, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 .

| Item Description                                                  |
|-------------------------------------------------------------------|
| 6 Four-character status display                                   |
| 7 PORT 1 status indicator                                         |
| 8 Drive status indicator                                          |
| 9 Comm status indicator                                           |
| 10 DC bus status indicator                                        |
| 11  Safety lock status indicator (2094-SE02F-M00-S1 modules only) |
| 12 I/O, safety, and aux feedback (IOD) connector                  |
| 13 Power module mounting screw access hole                        |
| 14 Motor feedback (MF) connector                                  |

|    | Item Description               |
|----|--------------------------------|
| 15 | Ethernet (PORT1) connector (1) |

(1) The Kinetix 6000M IPIM module has two Ethernet ports. They provide the same function on the IPIM module as the Ethernet port on the Kinetix 6200 control module. Refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094UM003, for more information.

<!-- image -->

Figure 29 - Control Module Features and Indicators (Ethernet)

<!-- image -->

| Designator Description Connector Module                                                           |
|---------------------------------------------------------------------------------------------------|
| IOD User I/O (drive), safety, and auxiliary feedback 44-pin high-density D-shell (female) Control |
| MF Motor feedback 15-pin high-density D-shell (female) Control                                    |
| CPD Control input power (drive) 2-position plug/header IAM                                        |
| IPD VAC input power (drive) and DC bus 6-position plug/header IAM                                 |
| CED Contactor enable 2-position plug/header IAM                                                   |
| MP Motor power 4-position plug/header IAM/AM                                                      |
| BC Motor/Resistive brake 6-position plug/header IAM/AM                                            |
| Tx and Rx Sercos transmit and receive Sercos fiber-optic (2) Control                              |
| PORT1 and PORT2 EtherNet/IP network RJ45 Ethernet (2) Control                                     |

Table 24 - Kinetix 6200 and Kinetix 6500 Power Module and Control Module Connectors

| Item Description   |
|--------------------|
| 1 Guide pins (2x)  |
| 2 Captive screw    |

| Item Description                                                 |
|------------------------------------------------------------------|
| 3 Four-character status display                                  |
| 4 PORT 1 status indicator                                        |
| 5 PORT 2 status indicator                                        |
| 6 Module status indicator                                        |
| 7 Network status indicator                                       |
| 8 DC bus status indicator                                        |
| 9  Safety lock status indicator (2094-EN02D-M01-S1 modules only) |
| 10 I/O, safety, and aux feedback (IOD) connector                 |
| 11 Power module mounting screw access hole                       |
| 12 Motor feedback (MF) connector                                 |

| Item Description              |
|-------------------------------|
| 13 Ethernet (PORT1) connector |
| 14 Ethernet (PORT2) connector |

## I/O, Safety, and Auxiliary Feedback Connector Pinout

7 Clock output + AUX\_CLK+ 29 (68) Safe limited speed output 0 SLS\_OUT\_CH0

8 Clock output - AUX\_CLK- 30 (78) Safe limited speed output 1 SLS\_OUT\_CH1

10 Encoder common ECOM 32 (S42) Door monitor input 1 DM\_IN\_CH1

12 Reserved – 34 (X42) Lock monitor input 1 LM\_IN\_CH1

13 Reserved – 35 (51) Door control channel output- DC\_OUT\_CH0

16 Reserved – 38 (S82) Enabling switch monitor input 1 ESM\_IN\_CH1

17 (A1) Safety 24V power input SPWR 39 24V power out

18 (A2) Safety 24V common SCOM 40 24V common

20 (S22) Safe stop input 1 SS\_IN\_CH1 42 Digital input 2 (home)

21 (34) Safe stop output 0 SS\_OUT\_CH0 43 Digital input 3 (registration 1)

22 (44) Safe stop output 1 SS\_OUT\_CH1 44 Digital input 4 (registration 2)

| IOD Pin (1)   | Description Signal                                   |                  |
|---------------|------------------------------------------------------|------------------|
| 1             | Sine differential input + A differential input +     | AUX_SIN+ AUX_A+  |
| 2             | Sine differential input - A differential input -     | AUX_SIN AUX_A-                  |
| 3             | Cosine differential input + B differential input +   | AUX_COS+ AUX_B+  |
| 4             | Cosine differential input - B differential input -   | AUX_COS AUX_B-                  |
| 5             | Data differential input + Index differential input + | AUX_DATA+ AUX_I+ |
| 6             | Data differential input - Index differential input - | AUX_DATA AUX_I-                  |
|               | 9 Encoder 5V power output                            | EPWR5V (3)       |
|               | 11 Encoder 9V power output                           | EPWR9V (3)       |
|               | 14 24V power out                                     | 24VPWR (2)       |
|               | 15 24V common                                        | 24VCOM (2)       |
|               | 19 (S12) Safe stop input 0 SS_IN_CH0                 |                  |

| IOD Pin (1)                       | Description Signal                                  |
|-----------------------------------|-----------------------------------------------------|
| 23                                | (S52) Safe limited speed input 0 SLS_IN_CH0         |
| Safe stop input 2                 | SS_IN_CH2 (2)                                       |
| 24                                | (S62) Safe limited speed input 1 SLS_IN_CH1         |
| Safe stop input 3                 | SS_IN_CH3 (2)                                       |
|                                   | 25 Reset reference RESET_REF                        |
|                                   | 26 (S34) Reset input RESET_IN                       |
|                                   | 27 (S11) Pulse test output 0 TEST_OUT_0             |
|                                   | 28 (S21) Pulse test output 1 TEST_OUT_1             |
|                                   | 31 (S32) Door monitor input 0 DM_IN_CH0             |
|                                   | 33 (X32) Lock monitor input 0 LM_IN_CH0             |
|                                   | 36 (52) Door control channel output+ DC_OUT_CH1     |
|                                   | 37 (S72) Enabling switch monitor input 0 ESM_IN_CH0 |
|                                   | 24VPWR (4)                                          |
|                                   | 24VCOM (4)                                          |
| 41 Digital input 1 (drive enable) | INPUT1 (5)                                          |
|                                   | INPUT2 (5)                                          |
|                                   | INPUT3 (5)                                          |
|                                   | INPUT4 (5)                                          |

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect to either the 5V or 9V supply, but not both.

Refer to Additional Resources on page 10 for links to Kinetix 6200 and Kinetix 6500 safety reference manuals.

Figure 30 - Pin Orientation for 44-pin I/O, Safety, and Auxiliary Feedback (IOD) Connector

<!-- image -->

## Motor Feedback Connector Pinout

MF Pin Description Signal MF Pin Description Signal

6 Encoder common MTR\_ECOM 14 Encoder 5V power output

| 1   | Sine differential input + A differential input +            | MTR_SIN+ MTR_AM+   |
|-----|-------------------------------------------------------------|--------------------|
| 2   | Sine differential input - A differential input -            | MTR_SIN MTR_AM-                    |
| 3   | Cosine differential input + B differential input +          | MTR_COS+ MTR_BM+   |
| 4   | Cosine differential input - B differential input -          | MTR_COS MTR_BM-                    |
| 5   | Data differential input/output + Index differential input + | MTR_DATA+ MTR_IM+  |
|     | 7 Encoder 9V power output                                   | MTR_EPWR9V (2)     |
|     | 8 Hall commutation S3 input MTR_S3                          |                    |

| 9 Clock output + MTR_CLK+                                       |                |
|-----------------------------------------------------------------|----------------|
| 10  Data differential input/output - Index differential input - | MTR_DATA MTR_IM                |
| 11  Motor thermostat (normally closed)  (1)                     | MTR_TS         |
| 12 Hall commutation S1 input MTR_S1                             |                |
| 13 Hall commutation S2 input MTR_S2                             |                |
|                                                                 | MTR_EPWR5V (2) |
| 15 Clock output - MTR_CLK                                                                 |                |

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect to either the 5V or 9V supply, but not both.

## IMPORTANT

Combined motor-power cable length for all axes on the same DC bus must not exceed 240 m (787 ft) with 460V systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).

System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.

## Figure 31 - Pin Orientation for 15-pin Motor Feedback (MF) Connector

<!-- image -->

## Ethernet Communication Connector Pinout

| Pin Description Signal   |
|--------------------------|
| 1 Transmit+ TD+          |
| 2 Transmit- TD                          |
| 3 Receive+ RD+           |
| 4 Reserved —             |
| 5 Reserved —             |
| 6 Receive- RD                          |
| 7 Reserved —             |
| 8 Reserved —             |

Figure 32 - Pin Orientation for 8-pin Ethernet PORT1 and PORT2 Connectors

<!-- image -->

## IAM Input Connector Pinout

Table 25 - Control Power Connector

| CPD Pin Description Signal   |
|------------------------------|
| Control power VAC input pp 2 CTRL 1                              |
| Control power VAC input pp 2 CTRL 1                              |

Table 26 - DC Bus and Input Power Connector

|    | IPD Pin Description Signal                            |      |
|----|-------------------------------------------------------|------|
| 1  | An integral, unregulated power supply, consisting of AC line input, three-phase bridge rectifier, and filter capacitors. three-phase bridge rectifier, and filter capacitors. 2 DC+                                                       | DC      |
|    | 3 Chassis ground.                                     |      |
| 4  | Three-phase input power. Three-phase input power.5 L2 | L3   |
|    | Three-phase input power. Three-phase input power.5 L2 | 6 L1 |
|    | Three-phase input power. Three-phase input power.5 L2 |      |

Table 27 - Contactor Enable Connector

| CED Pin Description Signal                                               |    |
|--------------------------------------------------------------------------|----|
| 1  Relay-driven dry contact used in the control string for a three-phase | CONT EN    |
| power contactor. power contactor. 2 CONT EN+                                                                          |    |

## IAM and AM Motor Power and Brake Connector Pinout

## Table 28 - Motor Power Connector

|    | MP Pin Description Signal                          |     |
|----|----------------------------------------------------|-----|
|    | 4 Chassis ground                                   |     |
| 3  | Three-phase motor power Three-phase motor power2 V | W   |
|    | Three-phase motor power Three-phase motor power2 V | 1 U |
|    | Three-phase motor power Three-phase motor power2 V |     |

## IMPORTANT

Combined motor-power cable length for all axes on the same DC bus must not exceed 240 m (787 ft) with 460V systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).

System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.

## Table 29 - Motor Brake/Resistive Brake Connector

|    | BC Pin Description Signal                                     |     |
|----|---------------------------------------------------------------|-----|
| 6  | Motor brake connections 5 MBRK+                               | MBRK     |
|    | 4 Motor brake common COM                                      |     |
| 3  | +24V brake input power (from LIM module or customer supplied) | PWR |
| 2  | RBM module connections                                        | DBRK     |
|    | (from RBM module and safety string) (from RBM module and safety string) 1 DBRK+                                                               |     |

Control Signal Specifications This section provides a description of the Kinetix 6200 and Kinetix 6500 drive I/O (IOD), communication, contactor enable (CED), brake (BC), and control power (CPD) connectors.

## Digital Inputs

Four assignable inputs are available for the machine interface on the control module. Each IAM and AM module supplies 24V DC @ 200 mA for the purpose of registration, home, enable, over-travel positive, and over-travel negative inputs. These are sinking inputs that require a sourcing device. A 24V DC power and common connection is provided for the digital inputs.

IMPORTANT

To improve registration input EMC performance, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

IMPORTANT

Over-travel limit input devices must be normally closed.

The four digital inputs (IOD-41 through IOD-44) have default assignments, however, you can reassign them according to the needs of your specific application.

Table 30 - Digital Input Default IDN Assignments

|                   | IOD Pin Input IDN Type Default   |
|-------------------|----------------------------------|
| 41 1 P-0-052      | Enable                           |
| 42 2 P-0-053 Home |                                  |
|                   | 43 3 P-0-054 Registration 1      |
|                   | 44 4 P-0-055 Registration 2      |

You can change the digital input default settings on Kinetix 6200 control modules by using a Sercos IDN Write instruction. For example, digital input 4 (IOD-44) is configured by IDN P-0-055. By default the value is 4 (Registration 2). You can use the Sercos IDN Write instruction to change IDN P-0-055 value to 7, and then digital input 4 is configured as Regeneration OK. Digital input IDN values are in Table 32 on page 70. Refer to Appendix F on page 289 for more information on changing default IDN values.

You can change the digital input default settings on Kinetix 6500 control modules by using the Logix Designer application. Refer to Configure the Drive Modules on page 161 for more information on changing default values.

Table 31 - Understanding Digital Input Functions

|                      |                                                                                                                                                                                                                                                                                                                                                                    | Function Description Default Behavior                                                                                                                                                                                             |   IDN Value |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Enable               | If the controller configuration specifies checking of the enable input, an active state enables the power electronics to control the motor and an inactive state prevents motion. The drive generates an exception if the input is inactive when the controller commands motion and has authorized checking. The drive behavior in this situation is programmable. | The function is always inactive. If the controller instructs the drive to monitor the Enable input, the drive issues a vendor-specific initialization fault (Enable Input Assignment).                                            |           1 |
| Home                 | An active state indicates to a homing sequence that the referencing sensor has been seen. Typically, a transition of this signal is used to establish a reference position for the machine axis.                                                                                                                                                                   | The function is always inactive. If the controller instructs the drive to perform a home procedure, the drive issues a vendor-specific exception (Sensor Assignment).                                                             |           2 |
|                      | Registration 1 An inactive-to-active transition (also known as a positive transition) or active to-inactive transition (also known as a negative transition) is used to latch position values for use in registration moves.                                                                                                                                                                                                                                                                                                                                                                    | The function is always inactive. If the controller instructs the drive to perform a registration procedure, the drive issues a vendor specific exception (Sensor Assignment).                                                                                                                                                                                                                                   |           3 |
| Registration 2       | Registration 1 An inactive-to-active transition (also known as a positive transition) or active to-inactive transition (also known as a negative transition) is used to latch position values for use in registration moves.                                                                                                                                                                                                                                                                                                                                                                    | The function is always inactive. If the controller instructs the drive to perform a registration procedure, the drive issues a vendor specific exception (Sensor Assignment).                                                                                                                                                                                                                                   |           4 |
| Positive Over-travel | If the controller configuration specifies checking of the hardware over-travel inputs, an inactive state indicates that a position limit has been exceeded in the positive direction. The drive generates an exception if the input is inactive when the controller authorizes checking. The drive behavior in this situation is programmable.                     | The function is always inactive. If the controller instructs the drive to monitor the hardware over-travel inputs, the drive issues a vendor-specific initialization fault (Over-travel Input Assignment).                        |           5 |
| Negative Over-travel | If the controller configuration specifies checking of the hardware overtravel inputs, an inactive state indicates that a position limit has been exceeded in the negative direction. The drive generates an exception if the input is inactive when the controller authorizes checking. The drive behavior in this situation is programmable.                      | The function is always inactive. If the controller instructs the drive to monitor the hardware over-travel inputs, the drive issues a vendor-specific initialization fault (Over-travel Input Assignment).                        |           6 |
| Regeneration OK      | An inactive state indicates that an external regenerative power supply has a fault and a regenerative power supply exception is generated by the drive.                                                                                                                                                                                                            | The function is always active. If the controller instructs the drive that a regenerative power supply with a fault output is present, the drive issues a vendor-specific initialization fault (Regeneration OK Input Assignment). |           7 |

Table 32 - Digital Input Specifications

| Attribute Value                                                                           |                                                                                                               |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Type                                                                                      | Active high, single-ended, current sinking                                                                    |
| Assignable functions                                                                      | Enable, Home, Positive Over-travel, Negative Over-travel, Registration 1, Registration 2, and Regeneration OK |
| Default function assignments (Sercos)  (1)                                                | Input 1 = EnableInput 3 = Registration 1 Input 2 = HomeInput 4 = Registration 2                               |
| Input current (with 24V applied) 11 mA, typical                                           |                                                                                                               |
|                                                                                           | On-state input voltage 21.6…26.4V @ 200 mA total                                                              |
| Off-state input voltage -1.0…3.0V                                                         |                                                                                                               |
| Pulse reject filtering Home Registration All other functions                              | 15 ms 1.0 µs, nom 1.0 ms, nom                                                                                 |
| Propagation delay (Registration functions only) 10 µs                                     |                                                                                                               |
| Registration repeatability 500 ns                                                         |                                                                                                               |
| Windowed registration invalid-to-valid event delay 125 µs, min                            |                                                                                                               |
| Home-to-marker event delay 10 µs, min                                                     |                                                                                                               |
| Input reaction time (Disable) 25 ms, max                                                  |                                                                                                               |
| Input reaction time (Enable, Positive Over-travel, and Regeneration OK inputs) 20 ms, max |                                                                                                               |

Figure 33 - Digital Input Circuitry

<!-- image -->

## Ethernet Communication Specifications

The PORT1 and PORT2 (RJ-45) Ethernet connectors are provided for communication with the Logix controller (Kinetix 6500 control modules) and for programming the safety configuration (Kinetix 6200 and Kinetix 6500 control modules).

| Attribute Value                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Communication 100BASE-TX, full duplex                                                                                                                    |
| Cyclic update period 1.0 ms, min                                                                                                                         |
| Embedded switch features  Three-port, cut-through, time correction on IEEE-1588 packets, limited filtering, quality of service with four priority levels |
| Auto MDI/MDIX crossover detection/ correction  Yes                                                                                                       |
| Port-to-port time synchronization variation 100 ns, max                                                                                                  |
| Cabling CAT5e shielded, 100 m (328 ft) max                                                                                                               |

## Sercos Communication Specifications

The Rx and Tx Sercos connectors are provided on the Kinetix 6200 control module for communication with the Logix 5000™ controller.

| Attribute Value                  |                                                                    |
|----------------------------------|--------------------------------------------------------------------|
| Data rates                       | 4 and 8 Mbps, selectable via DIP switch (1)                        |
|                                  | Light intensity Low power or high power, selectable via DIP switch |
| Cyclic update period 500 µs, min |                                                                    |
| Node addresses                   | 001…099 (2)                                                        |

## Contactor Enable Relay

Contactor enable is a relay-driven contact used in the three-phase powerenable control string to protect the drive electronics during certain fault conditions. It is capable of handling 120V AC or 24V DC at 1 A or less. Contactor enable is a function of the converter and is not available in the axis modules. An active state indicates the drive is operational and does not have a fault.

<!-- image -->

ATTENTION: Wiring the contactor enable relay is required. To avoid personal injury or damage to the drive, wire the contactor enable relay into your three-phase power-enable control string so that:

- Three-phase power is removed from the drive in the event of shutdown fault conditions.
- Drive operation is prevented when the power rail is not fully populated.
- Control power is applied to the drive prior to three-phase power. Refer to IAM Module (without LIM module) on page 220 for a wiring example.

IMPORTANT All power rail slots must have a module installed or the contactor enable relay does not close.

Figure 34 - Contactor Enable Relay Circuit

<!-- image -->

Table 33 - Contactor Enable Relay Output Specifications

| Attribute Value Min Max   |                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------|
|                           | On-state current Current flow when the relay is closed – 1 A                             |
| On-state resistance       | Contact resistance when the relay is closed – 1                                         |
|                           | Off-state voltage Voltage across the contacts when the relay is open – 120V AC or 24V DC |

## Power and Relay Specifications

Table 34 - Brake Relay Output Specifications

|                                                                          | Attribute Description IAM/AM Power Module Value, Max                                                                                                      |       |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| Current flow when the relay is closed                                    | On-state current (1)  2094-BC01-Mxx-M, 2094-BC02-M02-M, 2094-BMP5-M, 2094-BM01-M, 2094-BM02-M  2094-BC04-M03-M, 2094-BC07-M05-M, 2094-BM03-M, 2094-BM05-M | 3.0 A |
| On-state resistance Contact resistance when the relay is closed 1       | On-state resistance Contact resistance when the relay is closed 1                                                                                        |       |
| Off-state voltage Voltage across the contacts when the relay is open 30V | Off-state voltage Voltage across the contacts when the relay is open 30V                                                                                  |       |

## Figure 35 - Brake Relay Circuit

<!-- image -->

IMPORTANT

Motor parking-brake switching frequency must not exceed 10 cycles/min.

This section provides a description of the Bulletin 2094 power module brake relay (BC), input power (IPD), motor power (MP), and control power (CPD) connectors.

## Motor/Resistive Brake Relay

The brake option is a spring-set holding brake that releases when voltage is applied to the brake coil in the motor. The customer-supplied 24V power supply drives the brake output through a solid-state relay. The solid-state brake driver circuit provides the following:

- Brake current-overload protection
- Brake over-voltage protection

Two connections are required for the (customer-supplied) motor/resistive brake input power (BC-3 and BC-4) and two connections each for the motor and resistive brake output, as shown in Figure 35. Wiring is consistent with all series releases. Connections are rated for +24V and current as shown in Table 34 .

Control of the relay to release the motor brake (BC-5 and BC-6) is configurable in the Logix Designer application (refer to Configure Axis Properties on page 151). An active signal releases the motor brake. Turn-on and turn-off delays are specified by the BrakeEngageDelayTime and BrakeReleaseDelayTime settings. Refer to Brake Control Example on page 237 for brake coil currents.

## IMPORTANT

Holding brakes that are available on Allen-Bradley rotary motors are designed to hold a motor shaft at 0 rpm for up to the rated brake-holding torque, not to stop the rotation of the motor shaft, or be used as a safety device.

You must command the servo drive to 0 rpm and engage the brake only after verifying that the motor shaft is at 0 rpm.

The resistive brake relay (BC-1 and BC-2) controls the resistive brake module (RBM) contactor. The RBM module is wired between the drive and motor by using an internal contactor to switch the motor between the drive and a resistive load. The RBM module contact delay is the time that it takes to fully close the contactor across the motor power input lines, and must be configured in the software. Refer to RBM Module Interconnect Diagrams beginning on page 303 for wiring examples.

These steps provide one method you can use to control a brake.

1. Wire the mechanical brake according to the appropriate interconnect diagram in Appendix A beginning on page 215 .
2. Enter the BrakeEngageDelay and BrakeReleaseDelay times in the Logix Designer application.

Refer to Axis Properties&gt;Parameter List. For delay times, refer to the appropriate motor family brake specifications table in Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001 .

3. Use the drive stop-action default setting (Current Decel &amp; Disable). Refer to Axis Properties&gt;Actions&gt;Stop Action in the Logix Designer application (this step applies to only Kinetix 6500 servo drives).
4. Use the motion instruction Motion Axis Stop (MAS) to decelerate the servo motor to 0 rpm.
5. Use the motion instruction Motion Servo Off (MSF) to engage the brake and disable drive.

## Input Power Cycle Capability

The power cycle capability is inversely proportional to the system capacitance (including DC bus follower), but cannot exceed 2 contactor cycles per minute with up to 4 axes or 1 contactor cycle per minute with 5…8 axes.

The cycle capability also depends on the converter power rating and the total system capacitance. Refer to Appendix C on page 249 to calculate total system capacitance.

Table 35 - Maximum Input Power Cycling Specifications (460V)

| Attribute                                                     | 2094-BC01-MP5-M, 2094-BC01-M01-M   | 2094-BC02-M02-M 2094-BC04-M03-M 2094-BC07-M05-M   |
|---------------------------------------------------------------|------------------------------------|---------------------------------------------------|
| Main AC input power cycling (cycles per minute for 10,000 µf) |                                    | 0.12 0.52 2.15 4.30                               |

For example, in a 4 axis system with a 2094-BC02-M02-M IAM power module and 2,000 μF total capacitance, the calculated capability is 0.52 x 10,000/2000 = 2.6 cycles per minute. However, this value is reduced to 2.0 by the 4 axes per system limitation.

## Peak Current Specifications

Figure 36 - Load Duty-cycle Profile Example

<!-- image -->

Table 36 - Peak Duty Cycle Definition of Terms

| Term                              | Definition (1)                                                                                                                                                                                                                  |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous Current Rating (ICont) | The maximum value of current that can be output continuously.                                                                                                                                                                   |
| Peak Current Rating (IPKmax)      | The maximum value of peak current that the drive can output. This rating is valid only for overload times less than TPKmax .                                                                                                    |
| Duty Cycle (D)                    | The ratio of time at peak to the Application Period and is defined as: D = T P T T PK  x 100%                                                                                                                                                                                                                                 |
| Time at Peak (T PK )              | The time at peak current (IPK) for a given loading profile. Must be less than or equal to TPKmax .                                                                                                                              |
| Peak Current (I PK )              | The level of peak current for a given loading profile. IPK must be less than or equal to the Peak Current Rating (TPKMAX)   of the drive.                                                                                                                                                                                                                                 |
| Base Current (I Base )            | The level of current between the pulses of peak current for a given loading profile. IBase must be less than or equal to the continuous current rating (ICont) of the drive.                                                    |
| Loading Profile                   | The loading profile is comprised of IPK, IBase, TPK, and D (or T) values and completely specify the operation of the drive in an overload situation. These values are collectively defined as the Loading Profile of the drive. |
| Application Period (T)            | The sum of the times at IPK (TPK) and IBase .                                                                                                                                                                                   |

(1) All current values are specified as RMS.

Figure 37 - Peak Inverter Overload (TPK &lt; 2.0 s)

<!-- image -->

(1) Base current (I Base ) and peak current (IPK) are a percentage of the continuous drive current rating (ICont).

Figure 38 - Peak Inverter Overload (TPK &lt; 2.0 s)

<!-- image -->

(1) Base current (I Base ) and peak current (IPK) are a percentage of the continuous drive current rating (ICont).

## Control Power

The IAM power module requires AC input power for logic circuitry.

| IMPORTANT   | The control power input requires an AC (EMC) line filter for CE and UK certification. For filter examples, refer to Agency Compliance on page 25 .                                                                                                                                                 |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | 2094-BCxx-Mxx-M (460V) IAM modules require a step down transformer for single-phase control power input. The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder. |

Table 37 - Control Power Input Power Specifications

| Attribute Value                                                                              |                                            |
|----------------------------------------------------------------------------------------------|--------------------------------------------|
|                                                                                              | Input voltage 95…264V AC rms, single-phase |
| Input power frequency 47…63 Hz                                                               |                                            |
| Control power AC input current Nom @ 220/230V AC rms Nom @ 110/115V AC rms Max inrush (0-pk) | 6 A 6 A 98 A (1)                           |

I PK = 0.043 x (V IN ) + 6.72 x (# of axes) + 0.000333 x (V IN 2 ) - 0.816 x (# of axes) 2 + 0.0358 x (# of axes x V IN )

Table 38 - Control Power Current Requirements

|                                                               | 110/115V AC Input 220/230V AC Input                                                                                                                                           | 110/115V AC Input 220/230V AC Input   |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Modules on Power Rail Input Current A Input VA VA Input VA VA | Input Current A                                                                                                                                                               |                                       |
| IAM module only 0.56 67 0.36 85                               |                                                                                                                                                                               |                                       |
| IAM and 1 AM module 0.99 119 0.64 153                         |                                                                                                                                                                               |                                       |
| IAM and 2 AM module 1.43 172 0.92 220                         |                                                                                                                                                                               |                                       |
| IAM and 3 AM module 1.87 224 1.20 287                         |                                                                                                                                                                               |                                       |
| IAM and 4 AM module 2.31 277 1.48 354                         |                                                                                                                                                                               |                                       |
| IAM and 5 AM module 2.74 329 1.75 421                         |                                                                                                                                                                               |                                       |
| IAM and 6 AM module 3.18 382 2.03 488                         |                                                                                                                                                                               |                                       |
| IAM and 7 AM module 3.62 434 2.31 555                         |                                                                                                                                                                               |                                       |
| IDM power interface module (IPIM)                             | For specifications and an example for calculating the IPIM module current requirements, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 |                                       |

For Kinetix 6000M systems, calculate the sum of the control power current requirements for each IPIM module on the power rail and add that value with the appropriate value from Table 38 for the number of axes on the power rail.

## Feedback Specifications

The control module accepts motor and auxiliary feedback signals from the following types of encoders with these general specifications.

Table 39 - Motor and Auxiliary Feedback General Specifications

|                                        |                                                                                                                                  | Attribute Motor Feedback Auxiliary Position Feedback                                                    |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Feedback device support                | • Hiperface • Generic TTL Incremental • Generic Sine/Cosine Incremental • Tamagawa 17-bit Serial • EnDat Sin/Cos • EnDat Digital | • Hiperface • Generic TTL Incremental • Generic Sine/Cosine Incremental • EnDat Sin/Cos • EnDat Digital |
| Power supply voltage (MTR_EPWR5V)  (1) | 5.1…5.4V                                                                                                                         | 5.1…5.4V                                                                                                |
| Power supply current (MTR_EPWR5V)  (1) | 300 mA, max                                                                                                                      | 300 mA, max                                                                                             |
| Power supply voltage (MTR_EPWR9V)  (1) | 8.3…9.9V                                                                                                                         | 8.3…9.9V                                                                                                |
| Power supply current (MTR_EPWR9V)  (1) | 150 mA, max                                                                                                                      | 150 mA, max                                                                                             |
| Thermostat                             | Single-ended, under 500 = no fault, over 10 k= fault                                                                         | –                                                                                                       |

<!-- image -->

Auto-configuration in the Logix Designer application of intelligent absolute, highresolution, incremental, and EnDat encoders is possible only with Allen-Bradley motors.

## Absolute Position Feature

The drive's absolute position feature tracks the position of the motor, within the multi-turn retention limits, while the drive is powered off. The absolute position feature is available with only these multi-turn encoders.

Table 40 - Absolute Position Designator Examples

| Encoder Type   | Cat. No.   | Motor/Actuator Cat. No.                                                                    | Retention Limits (turns)   | Retention Limits (turns)   |
|----------------|------------|--------------------------------------------------------------------------------------------|----------------------------|----------------------------|
|                | Designator |                                                                                            | Kinetix 6200 Kinetix 6500  |                            |
| Hiperface      | -M         | MPL-Bxxxxx-M, MPM-Bxxxxx-M, MPF-Bxxxxx-M, MPS-Bxxxxx-M, MPAR B3xxxx-M, MPAI-BxxxxxM                                                                                            | 4096 (±2048) 2048 (±1024)  |                            |
| Hiperface      | -V         | MPL-Bxxxxx-V, MPAS-Bxxxx1-V05, MPAS-Bxxxx2-V20, MPAR-B1xxxx-V, MPAR-B2xxxx-V, MPAI-BxxxxxV | 4096 (±2048) 4096 (±2048)  |                            |
|                |            | EnDat -7 RDB-Bxxxxxx-7 4096 (±2048) 1024 (±512)                                            |                            |                            |

Figure 39 - Absolute Position Limits (measured in turns)

<!-- image -->

Table 41 - Motor Feedback Signals by Device Type

| MF Pin Hiperface  Generic TTL Incremental Generic Sine/Cosine Incremental Tamagawa 17-bit Serial  EnDat Sine/Cosine EnDat Digital   |
|-------------------------------------------------------------------------------------------------------------------------------------|
| 1 MTR_SIN+ MTR_AM+ MTR_AM+ – MTR_SIN+ –                                                                                             |
| 2 MTR_SIN- MTR_AM- MTR_AM- – MTR_SIN- –                                                                                             |
| 3 MTR_COS+ MTR_BM+ MTR_BM+ – MTR_COS+ –                                                                                             |
| 4 MTR_COS- MTR_BM- MTR_BM- – MTR_COS- –                                                                                             |
| 5 MTR_DATA+ MTR_IM+ MTR_IM+ MTR_DATA+ MTR_DATA+ MTR_DATA+                                                                           |
| 6 MTR_ECOM MTR_ECOM MTR_ECOM MTR_ECOM MTR_ECOM MTR_ECOM                                                                             |
| 7 MTR_EPWR9V – – – – –                                                                                                              |
| 8 – MTR_S3 MTR_S3 – – –                                                                                                             |
| 9 – – – – MTR_CLK+ MTR_CLK+                                                                                                         |
| 10 MTR_DATA- MTR_IM- MTR_IM- MTR_DATA- MTR_DATA- MTR_DATA                                                                                                                                     |
| 11 MTR_TS MTR_TS MTR_TS MTR_TS MTR_TS MTR_TS                                                                                        |
| 12 – MTR_S1 MTR_S1 – – –                                                                                                            |
| 13 – MTR_S2 MTR_S2 – – –                                                                                                            |
| 14 – MTR_EPWR5V MTR_EPWR5V MTR_EPWR5V MTR_EPWR5V MTR_EPWR5V                                                                         |
| 15 – – – – MTR_CLK- MTR_CLK                                                                                                                                     |

## IMPORTANT

For motors with generic incremental encoders without Hall signals (for example, self-sense commutation alignment), configured as Motor Feedback Only, the drive reports an Incremental Position Loss fault (FLTM07), while ignoring a Feedback Loss fault (FLT-S43), if the motor is running at or near maximum speed. Once the motor speed is reduced, the FLT-S43 fault is enunciated.

Although the thermostat signal (MTR\_TS) is shown for all feedback types, some motors cannot support this feature because it is not part of the feedback device.

Table 42 - Hiperface Specifications

| Attribute Value                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------|
| Protocol Hiperface                                                                                                                |
| Memory support Not programmed, or programmed with Allen-Bradley motor data                                                        |
| Hiperface data communication 9600 baud, 8 data bits, no parity                                                                    |
| Sine/cosine interpolation 2048 counts/sine period                                                                                 |
| Input frequency (AM/BM) 250 kHz, max                                                                                              |
| Input voltage (AM/BM) 0.6...1.2V, p-p, measured at the drive inputs                                                               |
| Line loss detection (AM/BM)  Average (sin 2 + cos 2 ) > constant                                                                  |
| Noise filtering (AM and BM) Two-stage coarse count pulse reject filter with rejected pulse tally                                  |
| Incremental position verification  Position compare between incremental accumulator and serial data performed every 50 ms or less |

## Motor Feedback Specifications

The Kinetix 6200 and Kinetix 6500 control modules support multiple types of feedback devices by using the 15-pin (MF) motor feedback connector and sharing connector pins in many cases.

Table 43 - Generic TTL Incremental Specifications

| Attribute Value                                           |                                                                                                   |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| TTL incremental encoder support 5V, differential A quad B |                                                                                                   |
|                                                           | Quadrature interpolation 4 counts / square wave period                                            |
| Differential input voltage (MTR_AM, MTR_BM, and MTR_IM)   | 1.0…7.0V                                                                                          |
| DC current draw (MTR_AM, MTR_BM, and MTR_IM)              | 30 mA, max                                                                                        |
| Input signal frequency (MTR_AM, MTR_BM, and MTR_IM)       | 5.0 MHz, max                                                                                      |
| Edge separation (MTR_AM and MTR_BM)                       | 42 ns min, between any two edges                                                                  |
| Line loss detection (MTR_AM and MTR_BM)                   | Average (MTR_AM 2 + MTR_BM 2 ) > constant                                                         |
| Noise filtering (MTR_AM and MTR_BM)                       | Two-stage coarse count pulse reject filter with rejected pulse tally                              |
|                                                           | Commutation verification Commutation angle verification performed at every Hall signal transition |
| Hall inputs (MTR_S1, MTR_S2, and MTR_S3)                  | Single-ended, TTL, open collector, or none                                                        |

Table 44 - Generic Sine/Cosine Incremental Specifications

| Attribute Value                                  |                                                                                                   |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
|                                                  | Sine/Cosine interpolation 2048 counts/sine wave period                                            |
| Input frequency (MTR_SIN and MTR_COS)            | 250 kHz, max                                                                                      |
| Differential input voltage (MTR_SIN and MTR_COS) | 0.6…1.2V, p-p                                                                                     |
| Line loss detection (MTR_SIN and MTR_COS)        | Average (sin 2 + cos 2 ) > constant                                                               |
| Noise filtering (MTR_SIN and MTR_COS)            | Two-stage coarse count pulse reject filter with rejected pulse tally                              |
|                                                  | Commutation verification Commutation angle verification performed at every Hall signal transition |
| Hall inputs (MTR_S1, MTR_S2, and MTR_S3)         | Single-ended, TTL, open collector, or none                                                        |

Table 45 - Tamagawa 17-bit Serial Specifications

| Attribute Value                                                      |
|----------------------------------------------------------------------|
| Tamagawa model support TS5669N124                                    |
| Protocol Tamagawa proprietary                                        |
| Memory support Programmed with Allen-Bradley motor data              |
| Differential input voltage 1.0…7.0V                                  |
| Data communication 2.5 Mbps, 8 data bits, no parity                  |
| Battery 3.6V, located external to drive in low-profile connector kit |

Table 46 - EnDat Sine/Cosine Interface Specifications

| Attribute Value                                          |                                                                                                 |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------|
|                                                          | Protocol EnDat Sine/Cosine                                                                      |
| Memory support Unprogrammed                              |                                                                                                 |
| EnDat Sine/Cosine data communication 4 Mbps, synchronous |                                                                                                 |
|                                                          | Sine/Cosine interpolation 2048 counts/sine wave period                                          |
| Input frequency (MTR_SIN and MTR_COS)                    | 250 kHz, max                                                                                    |
| Differential input voltage (MTR_SIN and MTR_COS)         | 0.6…1.2V, p-p                                                                                   |
| Line loss detection (MTR_SIN and MTR_COS)                | Average (sin 2 + cos 2 ) > constant                                                             |
| Noise filtering (MTR_SIN and MTR_COS)                    | Two-stage coarse count pulse reject filter with rejected pulse tally                            |
| Incremental position verification                        | Position compare between incremental accumulator and serial data performed every 50 ms or less. |

Table 47 - EnDat Digital Interface Specifications

| Attribute Value                                      |
|------------------------------------------------------|
| Memory support Unprogrammed                          |
| EnDat Digital data communication 4 Mbps, synchronous |

Table 48 - Support Requirements for EnDat Encoders on Third-party Motors

| Requirement EnDat Sine/Cosine EnDat Digital                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                            | EnDat Digital (with sine/cosine)                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ECI1319 / EQI1331 ECI1118 / EQI1130 ECI119 (1)                                                                                                                                                                                                                                                                                                                                                                             | Supported models LC483 LIC4000 ECN125 ROQ437 ECN1123 / EQN1135 ECN1325 / EQN1337                                                                                                                                                                                                                                                                                                                                           | ECN113 ECN1313 / EQN1325 ECN413 / EQN425 ROQ425                                                                                                                                                                                                                                                                                                                                                                            |
| Cable length, max 50 m (164 ft)                                                                                                                                                                                                                                                                                                                                                                                            | Cable length, max 50 m (164 ft)                                                                                                                                                                                                                                                                                                                                                                                            | Cable length, max 50 m (164 ft)                                                                                                                                                                                                                                                                                                                                                                                            |
| Position initialization Digital                                                                                                                                                                                                                                                                                                                                                                                            | Position initialization Digital                                                                                                                                                                                                                                                                                                                                                                                            | Position initialization Digital                                                                                                                                                                                                                                                                                                                                                                                            |
| Position tracking Uses sine/cosine signals Digital Uses sine/cosine signals                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                            | Cabling Shielded, twisted pair EnDat Digital cable only Shielded, twisted pair                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Blob programming Not required                                                                                                                                                                                                                                                                                                                                                                                              | Blob programming Not required                                                                                                                                                                                                                                                                                                                                                                                              | Blob programming Not required                                                                                                                                                                                                                                                                                                                                                                                              |
| Kinetix 6200 or Kinetix 6500 drives: A one-time procedure must be executed via message instructions to program the blob file in the encoder (using a Kinetix 6500 drive) so that it can be operated like any other Rockwell Automation® motor. This is similar to the Hiperface encoder third-party motor requirement, except that a Kinetix 6500 drive is used instead of a Kinetix 6000 drive. Kinetix 6500 drives only: | Kinetix 6200 or Kinetix 6500 drives: A one-time procedure must be executed via message instructions to program the blob file in the encoder (using a Kinetix 6500 drive) so that it can be operated like any other Rockwell Automation® motor. This is similar to the Hiperface encoder third-party motor requirement, except that a Kinetix 6500 drive is used instead of a Kinetix 6000 drive. Kinetix 6500 drives only: | Kinetix 6200 or Kinetix 6500 drives: A one-time procedure must be executed via message instructions to program the blob file in the encoder (using a Kinetix 6500 drive) so that it can be operated like any other Rockwell Automation® motor. This is similar to the Hiperface encoder third-party motor requirement, except that a Kinetix 6500 drive is used instead of a Kinetix 6000 drive. Kinetix 6500 drives only: |
|                                                                                                                                                                                                                                                                                                                                                                                                                            | Data frequency 100 kHz 4.125 MHz 100 kHz                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Sine/cosine frequency 0…250 kHz – 0…250 kHz                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                            |

## IMPORTANT

## IMPORTANT

To properly support system EnDat feedback, the keying configuration on the drive Module Properties tab of the Logix Designer application must be selected to the correct firmware revision as follows:

- For EnDat Sine/Cosine encoders, use Kinetix 6200 drive firmware revision 1.35 or later
- For or EnDat Digital encoders, use Kinetix 6200 drive firmware revision 1.40 or later

To make sure your drive and motor integration is successful, refer to commissioning notes relative to EnDat encoders on third-party motors.

## Auxiliary Position Feedback Specifications

The Kinetix 6200 and Kinetix 6500 control modules support multiple types of feedback devices by using the 44-pin (IOD) connector and sharing connector pins in many cases.

Table 49 - Auxiliary Feedback Signals by Device Type

| IOD Pin Hiperface Generic TTL Incremental       | Generic Sine/Cosine Incremental  EnDat Sine/Cosine EnDat Digital   |
|-------------------------------------------------|--------------------------------------------------------------------|
| 1 AUX_SIN+ AUX_AM+ AUX_SIN+ AUX_SIN+ –          |                                                                    |
| 2 AUX_SIN- AUX_AM- AUX_SIN- AUX_SIN- –          |                                                                    |
| 3 AUX_COS+ AUX_BM+ AUX_COS+ AUX_COS+ –          |                                                                    |
| 4 AUX_COS- AUX_BM- AUX_COS- AUX_COS- –          |                                                                    |
| 5 AUX_DATA+ AUX_IM+ AUX_IM+ AUX_DATA+ AUX_DATA+ |                                                                    |
| 6 AUX_DATA- AUX_IM- AUX_IM- AUX_DATA- AUX_DATA                                                 |                                                                    |
| 7 – – – AUX_CLK+ AUX_CLK+                       |                                                                    |
| 8 – – – AUX_CLK- AUX_CLK                                                 |                                                                    |
| 9  AUX_EPWR5V (1)                               | AUX_EPWR5V AUX_EPWR5V AUX_EPWR5V AUX_EPWR5V                        |
| 10 AUX_ECOM AUX_ECOM AUX_ECOM AUX_ECOM AUX_ECOM |                                                                    |
| 11  AUX_EPWR9V (1)                              | ––––                                                               |

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect to either the 5V or 9V supply, but not both.

Specifications for the auxiliary feedback channel are identical to the motor feedback channel, except for specifications related to commutation.

The 9.0V and 5.0V power supplies for auxiliary feedback devices are shared with the motor feedback channel, and the total current capability is outlined in Table 39 on page 79 .

Allen-Bradley Bulletin 842HR, 844D, 847H, and 847T encoders are the preferred encoders for auxiliary feedback connections.

Table 50 - Allen-Bradley Auxiliary Feedback Encoders

|                                                                | Cat. No. Description                                                                                                                                                       |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 842HR-MJDZ115FWYD (multi-turn) 842HR-SJDZ115FWYD (single-turn) | Size 25, sine/cosine (serial), square flange, 3/8 in. solid shaft with flat, 5…12V DC, digital RS-485 interface, M23, 17-pin connector                                     |
| 844D-B5CC1FW                                                   | HS35, hollow-shaft incremental encoders, rear (through-shaft), 5/8 inch, tether, 3/8 in. bolt on a 2.5…4.0 in. diameter, 10-pin connector, 5V DC in, 5V DC DLD out         |
| 844D-B5CC1CS                                                   | HS35, hollow-shaft incremental encoders, rear (through-shaft), 5/8 inch, tether, 3/8 in. bolt on a 2.5…4.0 in. diameter, 10-pin connector, 5V DC in, 5V DC DLD out         |
| 844D-B5CC1DR                                                   | HS35, hollow-shaft incremental encoders, rear (through-shaft), 5/8 inch, tether, 3/8 in. bolt on a 2.5…4.0 in. diameter, 10-pin connector, 5V DC in, 5V DC DLD out         |
| 847H-DN1A-RH01024                                              | Size 25, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z gated with BN), MS connector, 10-pin |
| 847H-DN1A-RH02048                                              | Size 25, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z gated with BN), MS connector, 10-pin |
| 847H-DN1A-RH05000                                              | Size 25, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z gated with BN), MS connector, 10-pin |
|                                                                | 847T-DN1A-RH01024 Size 20, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z ,  gated with BN), MS connector, 10-pin 847T-DN1A-RH02048                                                                                                                                                                            |
|                                                                | 847T-DN1A-RH01024 Size 20, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z ,  gated with BN), MS connector, 10-pin 847T-DN1A-RH02048                                                                                                                                                                            |

Refer to the Kinetix Motion Accessories Technical Data, publication KNX-TD004, for more information on these Allen-Bradley encoders.

## Safe Speed Monitor Safety Features

Kinetix 6200 and Kinetix 6500 control modules with Safe Speed Monitoring, catalog number 2094-xx02x-Mxx-S1, incorporate Safe Torque Off functionality as well as Safe Speed Monitor and door control/monitoring. Speed monitoring allows for other stop categories such as a controlled stop and disable or even a controlled stop and hold position.

Table 52 on page 85 summarizes the safety modes of operation supported by the Safe Speed Monitor control modules. The table also describes which I/O is active depending on the operation mode. In addition to the modes listed in the table, the Safe Speed Monitor control modules support two additional safety features.

- Safe Maximum Speed
- Safe Direction Monitoring

You can operate these features independent of the other modes, relying on the Safe Stop function.

When the Safe Maximum Speed feature is activated through a software configuration, the feedback velocity is monitored and compared against a user-programmable limit. If the measured velocity exceeds the limit, the Safe Stop function is executed.

Safe Direction Monitoring is also activated through software configuration and monitors the feedback direction and executes the Safe Stop function when motion in the illegal direction is detected.

When a new Safe Speed Monitor control module is installed, it is preconfigured in the Disabled operation mode. When installing a new module, you must first complete the basic drive configuration by using the Logix Designer application. Next, you use the safety configuration tool to configure the safety functions. As a part of the safety configuration process, you verify that the safety functions are configured, operate correctly, and you lock the safety circuitry.

Connections for safety functions are made at the IOD connector by using the 2090-K6CK-D44M low-profile connector kit. A customer-supplied 24V power supply (IOD-17 and IOD-18) is required to support the safety inputs and outputs.

Table 51 - Safety I/O Power Supply Specifications

| Attribute Value                                                             |
|-----------------------------------------------------------------------------|
| Voltage rating  21.6…28.8V DC (24V nom) per IEC/EN 60204 and IEC/EN 61558-1 |
| Current rating 0.105 A max                                                  |

Table 52 - Safety Modes of Operation

|                                                          | Safety Mode Description                                                                                                                                                                                                                                                                                            | SS InputSLS InputESM InputLM Input ( (1) DM InputDC Output   |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
|                                                          | Disabled In this mode, all safety functions are disabled. – – – – – –                                                                                                                                                                                                                                              |                                                              |
| Safe Stop                                                | The drive activates the configured Stop Category upon deactivation of the Safe Stop input or the occurrence of a Stop Category Fault.                                                                                                                                                                              | X––X–X                                                       |
|                                                          | Safe Stop with Door Monitoring In addition to monitoring for Safe Stop, the drive monitors the status of the door. X – – X X X                                                                                                                                                                                     |                                                              |
| Safe Limited Speed                                       | In addition to monitoring for Safe Stop, the drive monitors the feedback velocity and compares it to a configurable Safe Speed Limit. If the velocity exceeds the limit, the drive initiates the configured Stop Category.                                                                                         | XX–X–X                                                       |
| Safe Limited Speed with Door Monitoring                  | In addition to monitoring for Safe Stop and Safe Limited Speed, the drive monitors the status of the door.                                                                                                                                                                                                         | XX–XXX                                                       |
| Safe Limited Speed with Enabling Switch Control          | In addition to monitoring for Safe Stop and Safe Limited Speed, the drive monitors the status of the Enabling Switch input.                                                                                                                                                                                        | XXXX–X                                                       |
| Safe Limited Speed with Door Monitor and Enabling Switch | In addition to monitoring for Safe Stop and Safe Limited Speed, the drive monitors the status of the door and the Enabling Switch input.                                                                                                                                                                           | XXXXXX                                                       |
| Safe Limited Speed (status only)                         | In addition to monitoring for Safe Stop, the drive monitors the feedback velocity and compares it to a configurable Safe Speed Limit. If the velocity exceeds the limit, the system status is made available as a safe output intended for a safety programmable logic controller. No stopping action takes place. | XX–X–X                                                       |
| Slave, Safe Stop                                         | The drive performs the same functions as Safe Stop. However, it regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.                                                          | X––––X                                                       |
| Slave, Safe Limited Speed                                | The drive performs the same functions as Safe Limited Speed mode. However, it regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.                                            | XX–––X                                                       |
| Slave, Safe Limited Speed (status only)                  | The drive performs the same functions as Safe Limited Speed Status Only mode. However, it regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.                                | XX–––X                                                       |

## Safe Torque Off Safety Features

Refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Safety Reference Manual, publication 2094-RM001, for more information on configuring and wiring the safety functions.

Kinetix 6200 and Kinetix 6500 control modules with Safe Torque Off, catalog numbers 2094-xx02x-Mxx-S0, incorporate the capability to safely turn off the power transistors on the inverter board in response to a monitored digital input, also known as a Category 0 Stop. These drives also support dual-channel outputs that allow for cascading of the Safe Torque Off function to additional axes, and a safety circuit reset input. The 2090-K6CK-D44S0 connector kit and 2090-CS0DSDS-AAxx cable were designed specifically for this purpose. Refer to Figure 64 on page 122 for more information.

Refer to the Kinetix 6200 and Kinetix 6500 Safe Torque-off Safety Reference Manual, publication 2094-RM002, for more information on configuring and wiring the safety functions.

## Notes:

## Basic Wiring Requirements

<!-- image -->

## Connect the Kinetix 6200 and Kinetix 6500 Drive System

This chapter provides procedures for wiring your Kinetix® 6200/6500 drive system components and making cable connections.

| Topic Page                                                  |
|-------------------------------------------------------------|
| Basic Wiring Requirements 87                                |
| Determine the Input Power Configuration 88                  |
| Set the Ground Jumper in Select Power Configurations 93     |
| Ground the Modular Drive System 96                          |
| Power Wiring Requirements 98                                |
| Power Wiring Guidelines 100                                 |
| Wire the IAM/AM Module Connectors 101                       |
| Apply the Motor Cable Shield Clamp 114                      |
| Feedback and I/O Cable Connections 115                      |
| Wire the Feedback and I/O Connectors 118                    |
| External Shunt Module Connections 123                       |
| IPIM Module Connections 124                                 |
| RBM Module Connections 125                                  |
| Sercos Fiber-optic Cable Connections 126                    |
| Kinetix 6000M Integrated Drive-Motor Sercos Connections 129 |
| Ethernet Cable Connections 130                              |

This section contains basic wiring information for the Kinetix 6200 and Kinetix 6500 drive modules.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Bulletin 2094 power rail and drive modules prior to applying power. Once power is applied, connector terminals can have voltage present even when not in use.

## IMPORTANT

This section contains common PWM servo system wiring configurations, size, and practices that can be used in a majority of applications. National Electrical Code, local electrical codes, special operating temperatures, duty cycles, or system configurations take precedence over the values and methods provided.

## Determine the Input Power Configuration

## Build Your Own Cables

## IMPORTANT

Factory-made cables are designed to minimize EMI and are recommended over hand-built cables to optimize system performance.

Building your own cables is not an option for the hybrid and network cables used in Kinetix 6000M integrated drive-motor systems.

Follow these guidelines when building cables for compatible motors and actuators:

- Connect the cable shield to the connector shells on both ends of the cable with a complete 360° connection.
- Use twisted pair cable whenever possible. Twist differential signals with each other and twist single-ended signals with the appropriate ground return.

Refer to the Kinetix Motion Accessories Technical Data, publication KNX-TD004, for low-profile connector kit, drive-end (mating) connector kit, and motor-end connector kit catalog numbers.

## Route the Power and Signal Cables

Be aware that when you route power and signal wiring on a machine or system, radiated noise from nearby relays, transformers, and other electronic drives can be induced into motor or encoder feedback signals, input/output communication, or other sensitive low voltage signals. This can cause system faults and communication anomalies.

Refer to Electrical Noise Reduction on page 36 for examples of routing high and low voltage cables in wireways. Refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, for more information.

Before wiring input power to your Kinetix 6200 or Kinetix 6500 system, you must determine the type of input power you are connecting to. The IAM power module is designed to operate in both grounded and ungrounded environments.

<!-- image -->

ATTENTION: When you are using a LIM module for input power, the VAC LINE input power must come from a grounded configuration. When you are not using a LIM module for input power, ungrounded, corner-grounded, and impedancegrounded power configurations are permitted, but you must set the ground jumper to the ungrounded position for proper drive operation. In addition, set the ground jumper when an active converter supplies the DC-bus voltage. Refer to Set the Ground Jumper in Select Power Configurations on page 93 for more information.

<!-- image -->

ATTENTION: For EN/IEC 61800-3 category C3 compliance, use the appropriate AC line filter with a grounded WYE configuration. The use of a line filter in an ungrounded, corner-grounded, or impedance-grounded configuration can affect the line filter components and result in equipment damage.

## Grounded Power Configurations

The grounded (WYE) power configuration lets you ground your three-phase power at a neutral point. This type of grounded power configuration is preferred.

Figure 40 - Grounded Power Configuration (WYE Secondary)

<!-- image -->

The IAM power module has a factory-installed ground jumper for grounded power distribution.

IMPORTANT If you determine that you have grounded power distribution in your facility, you do not need to move the ground jumper.

Refer to Power Wiring Examples beginning on page 217 for input power interconnect diagrams with and without the LIM module.

Figure 41 - Corner-grounded Power Configuration (Delta Secondary)

<!-- image -->

Figure 42 - Impedance-grounded Power Configuration (WYE Secondary)

<!-- image -->

IMPORTANT

Even though impedance-grounded and corner-grounded power configurations have a ground connection, treat them as ungrounded when installing Kinetix 6200 and Kinetix 6500 drive systems.

## Ungrounded Power Configurations

The ungrounded power configuration (Figure 43) does not provide a neutral ground point. Ungrounded, impedance-grounded, and corner-grounded power configurations are allowed, but you must move a jumper (internal to the IAM power module) across a 120 k resistor. The IAM power module ground jumper (default configuration) is set for grounded power distribution.

## IMPORTANT

If you determine that you have ungrounded, impedance-grounded, or corner-grounded power distribution in your facility, you must move the ground jumper (configured for grounded power) to the ungrounded power position inside the IAM power module.

Refer to Set the Ground Jumper in Select Power Configurations on page 93 for more information.

Figure 43 - Ungrounded Power Configuration

<!-- image -->

<!-- image -->

ATTENTION: Ungrounded systems do not reference each phase potential to a power distribution ground. This can result in an unknown potential to earth ground.

Refer to Power Wiring Examples beginning on page 217 for input power interconnect diagrams with and without the LIM module.

## DC Common Bus Configurations

Table 53 - IAM Module Terminology and Use

| This Module Is Wired And is   |                                                                                              |                                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|                               | IAM With three-phase input power.                                                            | Not wired in Common-bus mode.                                                    |
| Leader IAM                    | With three-phase input power, but has DC common-bus connections to a follower IAM module.    | Wired in Common-bus mode.                                                        |
| Follower IAM                  | Without three-phase input power, but has DC common-bus connections from a leader IAM module. | Wired in Common-bus mode and configured by using the Logix Designer application. |

The Bulletin 2094 leader IAM power module can operate with non-Bulletin 2094 follower drives, as can the Bulletin 2094 follower IAM module operate with non-Bulletin 2094 common-bus leader drives. However, non-Bulletin 2094 leader and follower drives must meet the same functional requirements as the Bulletin 2094 leader and follower IAM modules.

## IMPORTANT

Any non-Bulletin 2094 common-bus leader IAM module that does not provide precharge is required to add an additional external precharge circuit before connecting to any Bulletin 2094 common-bus follower IAM module.

Figure 44 - Typical DC Common-bus Configuration

<!-- image -->

When the IAM power module is used in a DC common-bus configuration, the IAM module is known as a leader IAM or follower IAM module. The IAM (noncommon bus) and leader IAM module have identical three-phase input power connections. The leader IAM module is responsible for discharging the DC bus, and for providing common-bus follower drives with DC bus precharge, bus regulation, phase-loss detection, and ground fault detection. Follower IAM modules do not have three-phase input power connections, but have DC bus connections from a leader IAM module.

## Set the Ground Jumper in Select Power Configurations

## Common Bus Fusing Requirements

When using a Bulletin 2094 leader IAM power module, DC-bus fuses are required only when wiring to more than one Bulletin 2094 follower IAM module. When wiring multiple follower IAM modules, terminal blocks are required to extend the DC common-bus power to additional drives. Install fuses in both lines of the DC bus between the DC bus terminal block and each follower IAM module. Base these fuse ratings on the DC input current of each follower IAM module.

When using a non-Bulletin 2094 common-bus leader drive, DC bus fuses are required in both lines of the DC bus, between the common-bus leader drive and follower IAM module. Base these fuse ratings on the common-bus leader drive DC output current. When using more than one follower IAM module, install fuses in both lines of the DC bus between the non-Bulletin 2094 common-bus leader and the terminal block as well as between the DC bus terminal block and each follower IAM module.

Refer to Circuit Breaker/Fuse Options on page 30, for recommended circuit breaker/fuse sizes. Refer to DC Common Bus Wiring Examples on page 221 for interconnect diagrams.

Setting the ground jumper is required when using an ungrounded, cornergrounded, and impedance-grounded power configurations. Setting the ground jumper is also required when the Bulletin 8720MC regenerative power supply or any active converter provides DC-bus power.

Setting the jumper involves removing the IAM power module from the power rail, opening the IAM module, and moving the jumper.

## IMPORTANT

If you have grounded power distribution, you do not need to set the ground jumper. Go to Ground the Modular Drive System on page 96 .

<!-- image -->

ATTENTION: Because the unit no longer maintains line-to-neutral voltage protection, risk of equipment damage exists when you move the ground jumper.

Setting the ground jumper is best done when the IAM power module is removed from the power rail and placed face-up on a solid surface equipped as a grounded static-safe workstation.

<!-- image -->

ATTENTION: This drive contains electrostatic discharge (ESD) sensitive parts and assemblies. You are required to follow static-control precautions when you install, test, service, or repair this assembly. If you do not follow ESD control procedures, components can be damaged. If you are not familiar with static control procedures, refer to Guarding Against Electrostatic Damage, publication 8000-4.5.2, or any other applicable ESD awareness handbook.

Table 55 - Ground Jumper Configurations

|                                                            |                                                                |                                  | Ground Configuration Example Diagram Ground Jumper Configuration Benefits of Correct Configuration                                   |
|------------------------------------------------------------|----------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Grounded (wye)                                             | Figure 40 on page 89                                           | Grounded power (default setting) | • UL and EMC compliance • Reduced electrical noise • Most stable operation • Reduced voltage stress on components and motor bearings |
| • AC-fed ungrounded • Corner grounded • Impedance grounded | Figure 43 on page 91 Figure 41 on page 90 Figure 42 on page 90 | Set for ungrounded power         | • Helps avoid severe equipment damage when ground faults occurs • Reduced leakage current                                            |
| DC-bus from active converter                               | Figure 92 on page 224                                          | Set for ungrounded power         | • Helps avoid severe equipment damage when ground faults occurs • Reduced leakage current                                            |

## Set the Ground Jumper

<!-- image -->

ATTENTION: To avoid personal injury, the ground jumper access area must be kept closed when power is applied. If power was present and then removed, wait at least 5 minutes for the DC-bus voltage to dissipate and verify that no DC-bus voltage exists before accessing the ground jumper.

Follow these steps to set the ground jumper for ungrounded power.

1. Remove the IAM power module from the power rail. For detailed instructions, refer to Remove Kinetix 6200 and Kinetix 6500 Drive Modules on page 210 .
2. Remove the top and bottom front-panel screws. Refer to the figure on page 95 for an illustration of your actual hardware.
3. Swing the front panel open to the right, as shown, and locate the ground jumper.

## IMPORTANT

Do not attempt to remove the front panel from the IAM module. The front panel status indicators and switches are also connected to the IAM module with a ribbon cable. The ribbon cable acts like a hinge and lets you swing the front panel open to access the ground jumper.

When using ungrounded input power in common-bus configurations, use this table to determine where to set the ground jumper.

Table 54 - Ground Jumper to Set

|                                    |                                          | Leader Drive Follower Drive Set the Jumper in This Drive   |
|------------------------------------|------------------------------------------|------------------------------------------------------------|
| Kinetix 6200/6500 IAM power module | Kinetix 6200/6500 IAM power module       | Leader drive                                               |
| Kinetix 6200/6500 IAM power module | Non-Kinetix 6200/6500 drive Leader drive |                                                            |
| Non-Kinetix 6200/6500 drive        | Kinetix 6200/6500 IAM power module       | Follower drive (if no setting exists in the leader drive)  |

<!-- image -->

ATTENTION: Risk of equipment damage exists. The facility ground configuration must be accurately determined. Do not move the ground jumper for grounded power configurations (default). Move the ground jumper for ungrounded, corner-grounded, and impedance-grounded power, or when an active converter supplies the DC-bus voltage.

4. Move the ground jumper.
5. Replace the IAM module front panel and two screws. Apply 1.6 N·m (14 lb·in) torque.
6. Mount the IAM module back on the power rail. For detailed instructions, refer to Replace Kinetix 6200 and Kinetix 6500 Drive Modules on page 213 .

|                        | Configuration                 | Configuration   |
|------------------------|-------------------------------|-----------------|
| IAM Module             | Grounded (default) Ungrounded |                 |
| 2094-BC01-MP5-M (460V) | P16 and P17 P18 and P19       |                 |
| 2094-BC01-M01-M (460V) | P16 and P17 P18 and P19       |                 |
| 2094-BC02-M02-M (460V) | P16 and P17 P18 and P19       |                 |
| 2094-BC04-M03-M (460V) | P16 and P17 P18 and P19       |                 |
| 2094-BC07-M05-M (460V) | P16 and P17 P18 and P19       |                 |

Figure 45 - Setting the Ground Jumper (460V IAM power modules)

<!-- image -->

IMPORTANT

Use the default jumper setting for grounded power configurations. Move the jumper, as shown above, for ungrounded power.

## Ground the Modular Drive System

All equipment and components of a machine or process system must have a common earth ground point connected to chassis. A grounded system provides a ground path for short circuit protection. Grounding your modules and panels minimize shock hazard to personnel and damage to equipment caused by short circuits, transient overvoltages, and accidental connection of energized conductors to the equipment chassis.

<!-- image -->

ATTENTION: The National Electrical Code contains grounding requirements, conventions, and definitions. Follow all applicable local codes and regulations to safely ground your system.

For CE and UK grounding requirements, see Agency Compliance on page 25 .

## Ground the Power Rail to the System Subpanel

The 2094-PRx and 2094-PRSx power rail ships with a braided ground strap, 100 mm (3.9 in.), that connects to the bonded cabinet ground bus. Connect the other end to either the power rail ground stud or mounting bracket ground stud, if mounting brackets are used.

Figure 46 - Connecting the Braided Ground Strap Examples

<!-- image -->

For power rail dimensions, refer to the Kinetix 6000 Power Rail Installation Instructions, publication 2094-IN003 .

For mounting bracket dimensions, refer to the 2094 Mounting Brackets Installation Instructions, publication 2094-IN008 .

## IMPORTANT

When 2094 mounting brackets are used to mount the power rail or LIM module over the AC line filter, the braided ground strap must be removed from the power rail and attached to a mounting bracket ground stud.

## Ground Multiple Subpanels

In this figure, the chassis ground is extended to multiple subpanels.

Figure 47 - Subpanels Connected to a Single Ground Point

<!-- image -->

High-frequency (HF) bonding is not illustrated. For HF bonding information, refer to Bond Multiple Subpanels on page 38 .

## Power Wiring Requirements

Table 56 - IAM Power Wiring Requirements

| Bulletin 2094 Drive Cat. No.    |                                | Connects to Terminals Recommended Wire   | Connects to Terminals Recommended Wire   | Size mm 2 (AWG)      | Strip Length mm (in.)   | Torque Value N•m (lb•in)                 |
|---------------------------------|--------------------------------|------------------------------------------|------------------------------------------|----------------------|-------------------------|------------------------------------------|
| Description                     |                                |                                          | Pin Signal                               | Size mm 2 (AWG)      | Strip Length mm (in.)   | Torque Value N•m (lb•in)                 |
| 2094-BC01-Mxx-M 2094-BC02-M02-M | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4                  | L3 L2 L1 DC DC+                                          | 10…2.5 (8…14)        | 10 (0.38)               | 1.2…1.5 (10.6…13.2)                      |
| 2094-BC04-M03-M                 | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4                  | L3 L2 L1 DC DC+                                          | 10…6 (8…10)          | 16 (0.63)               | 2.4…3.0 (21.6…26.5)                      |
| IPD-6 IPD-6 2094-BC07-M05-M 30 (3) L1                                 | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4                  | L3 L2 L1 DC DC+                                          |                      | 16 (0.63)               | 2.4…3.0 (21.6…26.5)                      |
| 2094-BCxx-Mxx-M                 | Control input power            |                                          | CPD-1 CTRL 2                             | 4…2.5 (12…14)  4…2.5 | 10 (0.38)               | 0.5…0.6 (12…14) 10(4.4…5.3) CPD-2 CTRL 1 |
| 2094-BCxx-Mxx-M                 | Contactor Enable               |                                          | CED-1 CONT EN-                           | (12…14) (2) (12…14) (2) (4.4…5.3) CED-2 CONT EN+                      | 10 (0.38)               | 0.5…0.6                                  |
| 2094-BCxx-Mxx-M                 | Contactor Enable               |                                          |                                          | (12…14) (2) (12…14) (2) (4.4…5.3) CED-2 CONT EN+                      | 10 (0.38)               | 0.5…0.6                                  |
| 2094-BCxx-Mxx-M                 |                                |                                          |                                          |                      | 10 (0.38)               |                                          |

<!-- image -->

ATTENTION: To avoid personal injury and/or equipment damage, make sure installation complies with specifications regarding wire types, conductor sizes, branch circuit protection, and disconnect devices. The National Electrical Code (NEC) and local codes outline provisions for safely installing electrical equipment.

ATTENTION: To avoid personal injury and/or equipment damage, make sure motor power connectors are used for connection purposes only. Do not use them to turn the unit on and off.

ATTENTION: To avoid personal injury and/or equipment damage, make sure shielded power cables are grounded to prevent potentially high voltages on the shield.

Wire must be copper with 75 °C (167 °F) minimum rating. Phasing of main AC power is arbitrary and earth ground connection is required for safe and proper operation.

For IPIM module power wiring requirements, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Refer to Power Wiring Examples on page 217 for interconnect diagrams.

IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

Table 57 - IAM/AM Power Wiring Requirements

| Bulletin 2094 Drive Cat. No.                                                 | Description   | Connects to Terminals Recommended Wire   | Connects to Terminals Recommended Wire   | Size mm 2 (AWG)                                                      | Strip Length mm (in.)   | Torque Value        |
|------------------------------------------------------------------------------|---------------|------------------------------------------|------------------------------------------|----------------------------------------------------------------------|-------------------------|---------------------|
| Bulletin 2094 Drive Cat. No.                                                 | Description   |                                          | Pin Signal                               |                                                                      |                         | N•m (lb•in)         |
| 2094-BC01-Mxx-M , 2094-BC02-M02-M , 2094-BMP5-M, 2094-BM01-M ,  2094- BM02-M | Motor power   | MP-4 MP-3 MP-2 MP-1                      | W V U                                    | Motor power cable depends on motor/ drive combination. 6…1.5 (10…16) | 10 (0.38)               | 0.5…0.6 (4.4…5.3)   |
| 2094-BC04-M03-M ,  2094-BM03-M                                               | Motor power   | MP-4 MP-3 MP-2 MP-1                      | W V U                                    | 10…1.5 (8…16)                                                        | 10 (0.38)               | 1.2…1.5 (10.6…13.2) |
| 2094-BC07-M05-M , 2094-BM05-M                                                | Motor power   | MP-4 MP-3 MP-2 MP-1                      | W V U                                    | 30…2.5 (3…14)                                                        | 16 (0.63)               | 2.4…3.0 (21.6…26.5) |
| IAM or AM (230 or 460V) 2094-BCxx-Mxx-M and 2094-BMxx-M                      | Brake power   | BC-6 BC-5 BC-4 BC-3 BC-2 BC-1            | MBRK MBRK+ COM PWR DBRK DBRK+                                          |                                                                      | 0.75 (18) 10 (0.38)     | 0.22…0.25 (1.9…2.2) |

Table 58 - Shunt Module Power Wiring Requirements

| Drive Module Cat. No. Description       |                                           | Connects to Terminals   | Recommended Wire Size mm 2   | Torque Value N•m (lb•in)   |
|-----------------------------------------|-------------------------------------------|-------------------------|------------------------------|----------------------------|
| Drive Module Cat. No. Description       |                                           | Pin Signal              | (AWG)                        |                            |
| 2094-BSP2 Shunt module (200/400V-class) | 1394-SRxxxx External passive shunt module | RC-1 DC+                | 10 (8) (1)                   | 1.2…1.5 (10.6…13.2)        |
| 2094-BSP2 Shunt module (200/400V-class) | 1394-SRxxxx External passive shunt module | RC-2 INT                | 10 (8) (1)                   | 1.2…1.5 (10.6…13.2)        |
| 2094-BSP2 Shunt module (200/400V-class) | 1394-SRxxxx External passive shunt module | RC-3 COL                | 10 (8) (1)                   | 1.2…1.5 (10.6…13.2)        |
| 2094-BSP2 Shunt module (200/400V-class) | Thermal switch                            | TS-1 TS1                | 0.75 (18)                    | 0.22…0.25 0.75 (18)  (1.9…2.2) TS-2 TS2                            |
| 2094-BSP2 Shunt module (200/400V-class) | Thermal switch                            |                         | 0.75 (18)                    | 0.22…0.25 0.75 (18)  (1.9…2.2) TS-2 TS2                            |

(1) 105 °C (221 °F), 600V.

## Power Wiring Guidelines

Use these guidelines as a reference when wiring the power connectors on your IAM and AM power modules.

For IPIM module power wiring guidelines, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

## IMPORTANT

## IMPORTANT

For connector locations of the Kinetix 6200 and Kinetix 6500 drive modules, refer to 2094 Power Module and Control Module Features on page 62 .

When tightening screws to secure the wires, refer to the tables beginning on page 98 for torque values.

When removing insulation from wires, refer to the tables beginning on page 98 for strip lengths.

To improve system performance, run wires and cables in the wireways as established in Establish Noise Zones on page 39 .

Follow these steps when wiring the connectors on your IAM and AM power modules.

1. Prepare the wires for attachment to each connector plug by removing insulation equal to the recommended strip length.

## IMPORTANT

Use caution not to nick, cut, or otherwise damage strands as you remove the insulation.

2. Route the cable/wires to your IAM and AM power modules.
3. Insert wires into connector plugs.
3. Refer to connector pinout tables in Chapter 4 or the interconnect diagrams in Appendix A .
4. Tighten the connector screws.
5. Gently pull on each wire to make sure it does not come out of its terminal; reinsert and tighten any loose wires.
6. Insert the connector plug into the module connector.

## Wire the IAM/AM Module Connectors

Table 59 - Control Power (CPD) Connector

| CPL Connector (LIM module(1)) or Other Single-phase Input   | CPL Connector (LIM module(1)) or Other Single-phase Input   | CPD Connector (IAM module)         | CPL Connector (LIM module(1)) or Other Single-phase Input   |                    |    |
|-------------------------------------------------------------|-------------------------------------------------------------|------------------------------------|-------------------------------------------------------------|--------------------|----|
| 2094-ALxxS, 2094-BLxxS or 2094-XL75S-Cx LIM Module          | 2094-AL09 and 2094-BL02 LIM Module                          | 2094-AL09 and 2094-BL02 LIM Module |                                                             |                    |    |
|                                                             | CPL Pin Signal CPL Pin Signal CPD Pin Signal                |                                    |                                                             |                    |    |
|                                                             |                                                             |                                    | 1 CTRL 1 2 L1 1 CTRL 2                                      | 2.5 (14) 10 (0.38) | 0.5…0.6 2.5 (14) 10 (0.38)  (4.4…5.3) 2 CTRL 2 1 L2/N 2 CTRL 1    |
|                                                             |                                                             |                                    |                                                             | 2.5 (14) 10 (0.38) | 0.5…0.6 2.5 (14) 10 (0.38)  (4.4…5.3) 2 CTRL 2 1 L2/N 2 CTRL 1    |

This section provides examples and wiring tables to assist you in making connections to the IAM and AM power modules.

## Wire the Control Power (CPD) Connector

This example applies to any IAM, leader IAM, or follower IAM power module.

Figure 48 - IAM Power Module (CPD connector)

<!-- image -->

## IMPORTANT

The 2094-BL75S and 2094-XL75S-C2 LIM modules can supply input power for up to eight axes. The 2094-XL75S-C1 LIM module can supply up to sixteen axes.

The IPIM module control power load must be calculated for Kinetix 6000M systems and the LIM module control power input must have a sufficient current rating. If no LIM module can support the current requirement, then discrete components must be used.

The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder.

Refer to Control Power on page 78 for more information and IAM Module (without LIM module) on page 220 for the interconnect drawing.

## Wire the Input Power (IPD) Connector

This example applies to any IAM module or common-bus leader IAM power module.

<!-- image -->

ATTENTION: Make sure the input power connections are correct when wiring the IPD connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause explosion or damage to equipment.

Figure 49 - IAM Power Module (IPD connector)

<!-- image -->

Table 60 - Input Power (IPD) Connections

| OPL Connector (LIM module(1)) or Other Three-phase Input   | OPL Connector (LIM module(1)) or Other Three-phase Input   | IPD Connector                                        | IPD Connector              |
|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------|----------------------------|
| 2094-AL09  LIM Module                                      | 2094-ALxxS, 2094-BLxxS or 2094- XL75S-Cx LIM Modules       | 2094-ALxxS, 2094-BLxxS or 2094- XL75S-Cx LIM Modules | (IAM or leader IAM module) |
|                                                            | OPL Pin Signal OPL Pin Signal IPD Pin Signal               |                                                      |                            |
|                                                            | 1 L1’ 4 L1’ 6 L1                                           |                                                      |                            |
|                                                            | 2 L2’ 3 L2’ 5 L2                                           |                                                      |                            |
|                                                            | 3 L3’ 2 L3’ 4 L3                                           |                                                      |                            |
|                                                            | 41 3                                                       |                                                      |                            |
|                                                            |                                                            | 2 DC+                                                |                            |
| –                                                          |                                                            | 1 DC                                                      |                            |

Table 61 - Termination Specifications

| IAM Module Cat. No. Input VAC   |         | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|---------------------------------|---------|------------------------------------|-------------------------|----------------------------|
| 2094-BC01-Mxx-M 2094-BC02-M02-M | 460V AC |                                    | 2.5 (14) 10 (0.38)      | 1.2…1.5 (10.6…13.2)        |
| 460V AC 2094-BC04-M03-M 6 (10)                                 | 460V AC |                                    | 16 (0.63)               | 2.4…3.0                    |
| 16 (0.63)  (21.6…26.5) 2094-BC07-M05-M 30 (3)                                 | 460V AC |                                    | 16 (0.63)               |                            |

This example applies to a common-bus follower IAM power module.

<!-- image -->

ATTENTION: Make sure the common-bus power connections are correct when wiring the IPD connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause explosion or damage to equipment.

Figure 50 - IAM Power Module (IPD connector)

<!-- image -->

Table 62 - Input Power (IPD) Connections

| IPD Connector (IAM or follower IAM module)   | IPD Connector (IAM or follower IAM module)   |
|----------------------------------------------|----------------------------------------------|
| IPD Pin Signal                               |                                              |
| 6 N.C.                                       |                                              |
| 5 N.C.                                       |                                              |
| 4 N.C.                                       |                                              |
| 3                                            |                                              |
| 2 DC+                                        |                                              |
| 1 DC                                              |                                              |

## IMPORTANT

Do not connect three-phase input power to the common-bus follower IAM module.

Table 63 - Termination Specifications

| IAM Module Cat. No. Input VAC   |         | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|---------------------------------|---------|------------------------------------|-------------------------|----------------------------|
| 2094-BC01-Mxx-M 2094-BC02-M02-M | 460V AC |                                    | 2.5 (14) 10 (0.38)      | 1.2…1.5 (10.6…13.2)        |
| 460V AC 2094-BC04-M03-M 6 (10)                                 | 460V AC |                                    | 16 (0.63)               | 2.4…3.0                    |
| 16 (0.63)  (21.6…26.5) 2094-BC07-M05-M 30 (3)                                 | 460V AC |                                    | 16 (0.63)               |                            |

Table 64 - Contactor Enable (CED) Connector

| LIM Module (1) I/O (IOL) Connector or Other Control String   | LIM Module (1) I/O (IOL) Connector or Other Control String   |                | Recommended Wire Size mm 2 (AWG)   | Strip Length   |                          |
|--------------------------------------------------------------|--------------------------------------------------------------|----------------|------------------------------------|----------------|--------------------------|
| 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM Module          | 2094-AL09 and 2094-BL02 LIM Module                           | CED Pin Signal |                                    | mm (in.)       | Torque Value N•m (lb•in) |
|                                                              | IO_COM1 IO_COM 1 CONT EN                                                              |                | 2.5 (14) (2)                       | 10 (0.38)      | 0.5…0.6 2.5 (14) ( ) 10 (0.38)  (4.4…5.3) COIL_E2 COIL_A2 2 CONT EN+                          |
|                                                              |                                                              |                | 2.5 (14) (2)                       | 10 (0.38)      | 0.5…0.6 2.5 (14) ( ) 10 (0.38)  (4.4…5.3) COIL_E2 COIL_A2 2 CONT EN+                          |

## Wire the Contactor Enable (CED) Connector

This example applies to any IAM, common-bus leader IAM, or common-bus follower IAM power module.

Figure 51 - IAM Power Module (CED connector)

<!-- image -->

<!-- image -->

ATTENTION: Wiring the contactor enable relay is required. To avoid personal injury or damage to the drive, wire the contactor enable relay into your control string. Refer to Contactor Enable Relay on page 72 .

In common-bus configurations, the contactor enable (CED) connections for leader and follower drives must be wired in series to the control string. For interconnect diagrams, refer to Interconnect Diagram Notes beginning on page 216 .

## Wire the Motor Power (MP) Connector

Connections to the motor power (MP) connector include rotary motors, linear motors, and motor driven actuators.

<!-- image -->

ATTENTION: Make sure the motor power connections are correct when wiring the MP connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause explosion or damage to equipment.

This example applies to AM modules and the inverter section of IAM power modules.

Figure 52 - IAM/AM Power Module (MP connector)

<!-- image -->

Cable Shield Terminations

Factory-supplied Bulletin 2090 motor power cables for motors and actuators are shielded, and the braided cable shield must terminate at the drive during installation. A small portion of the cable jacket must be removed to expose the shield braid. The exposed area must be clamped (with the clamp provided) on top of the IAM or AM modules and the power wires terminated in the motor power (MP) connector plug.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, make sure shielded power cables are grounded at a minimum of one point for safety.

Table 65 - Kinetix MPL Motor Catalog Numbers

|                                                                             | Motor Cat. No. /SpeedTec DIN Connectors Motor Cat. No. /Threaded DIN Connectors Motor Cat. No. /Bayonet Connectors   |                                                                             |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| MPL-B15xxx - xx7xAA MPL-B2xxx - xx7xAA                                      | MPL-B15xxx - xx4xAA MPL-B2xxx - xx4xAA                                                                               | –                                                                           |
| MPL-B3xxx - xx7xAA, MPL-B4xxx-xx7xAA, MPL-B45xxx - xx7xAA, MPL-B5xxx-xx7xAA | –                                                                                                                    | MPL-B3xxx - xx2xAA, MPL-B4xxx-xx2xAA, MPL-B45xxx - xx2xAA, MPL-B5xxx-xx2xAA |
| MPL-B6xxx - xx7xAA, MPL-B8xxx-xx7xAA, MPL-B9xxx - xx7xAA                    | –                                                                                                                    | MPL-B6xxx - xx2xAA, MPL-B8xxx-xx2xAA, MPL-B9xxx - xx2xAA                    |

Bayonet connectors can be mounted facing the motor shaft or end plate and provide a separate connector for power, feedback, and brake connections. Circular DIN connectors rotate up to 180° and combine power and brake wires in the same connector, eliminating the brake connector.

Figure 53 - Bayonet and Circular DIN Motor Connectors

Bayonet Connectors

<!-- image -->

Feedback/Power/Brake Connectors

<!-- image -->

Feedback/Power Connectors

Threaded (M4) Connectors

<!-- image -->

SpeedTec (M7) Connectors

<!-- image -->

## Kinetix MP Motor and Actuator Connectors

Kinetix MPL motors equipped with circular DIN connectors (specified by 4 or 7 in the catalog number) are not compatible with cables designed for motors equipped with bayonet connectors (specified by 2 in the catalog number). The motors with bayonet connectors are being discontinued.

Side View

<!-- image -->

<!-- image -->

Side View

<!-- image -->

Kinetix MPAR and Kinetix MPAS linear actuators and Kinetix MPS stainlesssteel motors have also transitioned from threaded (M4) to SpeedTec (M7) connectors.

## Motor Power Wiring Examples

The procedure for wiring motor power varies slightly, depending on the motor family. The cables compatible with your motor or actuator depend on the connectors installed on the motor or actuator. Refer to Kinetix MP Motor and Actuator Connectors on page 106 for more information on circular DIN and bayonet connectors.

Table 66 - Motor Power Cable Compatibility - Bayonet Connectors

| Motor/Actuator   | Connector Type   | Motor/Actuator Cat. No.                                                                                                                                                                       | Motor Power Cables (with brake wires)   | Motor Power Cables (without brake wires)   |
|------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|--------------------------------------------|
| Kinetix MPL      | Bayonet          | MPL-B3xxx - xx2xAA, MPL-B4xxx-xx2xAA, MPL-B45xxx - xx2xAA, MPL-B5xxx-xx2xAA, MPL-B6xxx - xx2xAA, MPL-B8xxx-xx2xAA, MPL-B960B-xx2xAA, MPL-B960C-xx2xAA, MPL-B980B-xx2xAA, and MPL-B980C-xx2xAA | –                                       | 2090-XXxPMP-xxSxx (1)                      |
| Kinetix MPL      |                  | MPL-B960D-xx2xAA, MPL-B980D-xx2xAA 2090-MCNPMP-6Sxx                                                                                                                                           | –                                       |                                            |
|                  |                  | 1326AB (M2L/S2L) 1326AB-Bxxxx-M2L/S2L                                                                                                                                                         | –                                       | 2090-XXxPMP-xxSxx (1)                      |

(1) For Kinetix MPL or 1326AB motors equipped with bayonet connectors. These cables are available as standard (catalog number 2090-XXNPMP-xxSxx) and continuous-flex (catalog number 2090-XXTPMP-xxSxx).

Table 67 - Motor Power Cable Compatibility - Threaded DIN Connectors

| Motor/Actuator   | Connector Type   | Motor/Actuator Cat. No.                           | Motor Power Cables (with brake wires)                                 | Motor Power Cables (without brake wires)   |
|------------------|------------------|---------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------|
| Kinetix MPL      | Circular (threaded) DIN Circular Kinetix MPS MPS-Bxxxx (threaded) DIN Kinetix MPAS MPAS-Bxxxx                  | MPL-B15xxx - xx4xAA, MPL-B2xxx-xx4xAA             | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex) | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
|                  | Circular (threaded) DIN Circular Kinetix MPS MPS-Bxxxx (threaded) DIN Kinetix MPAS MPAS-Bxxxx                  | Kinetix MPAR MPAR-B1xxx and MPAR-B2xxx (series A) | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex) | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
|                  | Circular (threaded) DIN Circular Kinetix MPS MPS-Bxxxx (threaded) DIN Kinetix MPAS MPAS-Bxxxx                  |                                                   | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex) | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
|                  | Circular (threaded) DIN Circular Kinetix MPS MPS-Bxxxx (threaded) DIN Kinetix MPAS MPAS-Bxxxx                  |                                                   | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex) | 2090-CPWM4DF-xxAFxx (continuous-flex)      |

Table 68 - Motor Power Cable Compatibility - SpeedTec DIN Connectors

| Motor/Actuator                                 | Connector Type         | Motor/Actuator Cat. No.                                                                                                                                                     | Motor Power Cables (1) (with brake wires)                    | Motor Power Cables (1) (without brake wires)                            |
|------------------------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------|
| Kinetix MPL                                    | Circular (SpeedTec)DIN | MPL-B15xxx - xx7xAA, MPL-B2xxx-xx7xAA, MPL-B3xxx - xx7xAA, MPL-B4xxx-xx7xAA, MPL-B45xxx - xx7xAA, MPL-B5xxx-xx7xAA, MPL-B6xxx - xx7xAA, MPL-B8xxx-xx7xAA MPL-B9xxx - xx7xAA | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPM MPM-Bxxxx                          | Circular (SpeedTec)DIN |                                                                                                                                                                             | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPF MPF-Bxxxx                          | Circular (SpeedTec)DIN |                                                                                                                                                                             | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPS MPS-Bxxxx                          | Circular (SpeedTec)DIN |                                                                                                                                                                             | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAS (ballscrew)                       | Circular (SpeedTec)DIN | MPAS-Bxxxx1-V05SxA MPAS-Bxxxx2-V20SxA                                                                                                                                       | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAI MPAI-Bxxxx                        | Circular (SpeedTec)DIN |                                                                                                                                                                             | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAR                                   | Circular (SpeedTec)DIN | MPAR-B3xxx, MPAR-B1xxx and MPAR-B2xxx (series B)                                                                                                                            | 2090-CPBM7DF-xxAFxx (continuous-flex)                        | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix RDB RDB-Bxxxx                          | Circular (SpeedTec)DIN |                                                                                                                                                                             | Does not apply. These devices do not include a brake option. | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAS (direct drive) MPAS-Bxxxxx-ALMx2C | Circular (SpeedTec)DIN |                                                                                                                                                                             | Does not apply. These devices do not include a brake option. | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix LDAT                                   | Circular (SpeedTec)DIN | LDAT-Sxxxxxx - xDx LDAT-Sxxxxxx - xBx                                                                                                                                       | Does not apply. These devices do not include a brake option. | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                | Circular (SpeedTec)DIN | Kinetix LDC LDC-Cxxxxxx                                                                                                                                                     | Does not apply. These devices do not include a brake option. | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |

(1) You must remove the motor-side o-ring when using 2090-CPxM7DF-xxAxxx cables.

These cables contain only the three-phase power wires. The motors/actuators either have no brake or a separate connector for brake connections. Thermal switch wires are included in the feedback cable.

Refer to Axis Module/Rotary Motor Wiring Examples beginning on page 226 for interconnect diagrams.

Figure 54 - Motor Power Terminations (cables without brake wires)

<!-- image -->

The cable shield clamp shown above is mounted to an IAM module. Cables attach to the clamp on each AM module in the same way.

These cables contain three-phase power wires and brake wires. The brake wires have a shield braid (shown below as gray) that folds back under the cable clamp before the conductors are attached to the motor brake (BC) connector. Thermal switch wires are included in the feedback cable.

Refer to Axis Module/Rotary Motor Wiring Examples beginning on page 226 for interconnect diagrams.

Figure 55 - Motor Power Terminations (cables with brake wires)

<!-- image -->

The cable shield clamp shown above is mounted to an IAM module. Cables attach to the clamp on each AM module in the same way.

Cable shield and lead preparation is provided with most Allen-Bradley® cable assemblies. Follow these guidelines if your motor power cable shield and wires require preparation.

Figure 56 - Cable Shield and Lead Preparation

<!-- image -->

Refer to Axis Module/Rotary Motor Wiring Examples beginning on page 226 for interconnect diagrams.

Table 69 - Motor Power (MP) Connector

|                                               | Servo Motor MP Connector (IAM/AM module)   | Servo Motor MP Connector (IAM/AM module)   |
|-----------------------------------------------|--------------------------------------------|--------------------------------------------|
| Kinetix MP, Kinetix LDC, and 1326AB (M2L/S2L) | MP Pin Signal                              |                                            |
| U / Brown 1 U                                 |                                            |                                            |
| V / Black 2 V                                 |                                            |                                            |
| W / Blue 3 W                                  |                                            |                                            |
| Green/Yellow                                  | 4                                          |                                            |

Table 70 - Termination Specifications

| IAM/AM Module Cat. No.                                                   | Recommended Wire Size mm 2 (AWG)                                  | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|--------------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------|----------------------------|
| 2094-BC01-Mxx-M, 2094-BMP5-M, 2094-BM01-M 2094-BC02-M02-M ,  2094-BM02-M | Motor power cable depends on motor/ drive combination. 6 (10) max | 10 (0.38)               | 0.5…0.6 (4.4…5.3)          |
| 2094-BC04-M03-M, 2094-BM03-M 10 (8) max 10 (0.38)                        |                                                                   |                         | 1.2…1.5 (10.6…13.2)        |
| 2094-BC07-M05-M, 2094-BM05-M 30 (3) max 16 (0.63)                        |                                                                   |                         | 2.4…3.0 (21.6…26.5)        |

## Wire the Motor/Resistive Brake (BC) Connector

This example applies to AM modules and the inverter section of IAM power modules.

Figure 57 - IAM/AM Power Module (BC connector)

<!-- image -->

24V DC Brake Input Power Connections

| IMPORTANT   | If your system includes a LIM module, you can source the 24V DC from the LIM module (P1L or PSL connector).   |
|-------------|---------------------------------------------------------------------------------------------------------------|

Table 71 - Motor/Resistive Brake (BC) Connector

| 2094-BLxxS or 2094-XL75S-Cx LIM Module   | 2094-BL02 LIM Module                        | BC Connector (IAM/AM modules)   | BC Connector (IAM/AM modules)   |
|------------------------------------------|---------------------------------------------|---------------------------------|---------------------------------|
|                                          | P1L Pin Signal PSL Pin Signal BC Pin Signal |                                 |                                 |
|                                          |                                             |                                 | 1 IO_PWR2 1 MBRK PWR 3 PWR      |
|                                          |                                             |                                 | 2 IO_COM2 2 MBRK COM 4 COM      |

## RBM Module Connections

Table 72 - Motor/Resistive Brake (BC) Connector

| RBM Module I/O Connections   | BC Connector (IAM/AM power modules)   | BC Connector (IAM/AM power modules)   |
|------------------------------|---------------------------------------|---------------------------------------|
|                              | TB3 Pin Signal MP Pin                 | Signal (1)                            |
|                              |                                       | 6 COIL_A1 1 DBRK+                     |
|                              |                                       | 7 COIL_A2 2 DBRK-                     |

(1) Firmware revision 1.071 or later is required to use the DBRK outputs on the Kinetix 6200 and Kinetix 6500 IAM/AM power module.

## Motor Brake Connections

The procedure for wiring your motor brake varies slightly, depending on the motor family. The cables compatible with your motor or actuator depend on the connectors installed on the motor or actuator. Refer to Kinetix MP Motor and Actuator Connectors on page 106 for more information on circular DIN and bayonet connectors.

Table 73 - Motor Brake Cable Compatibility - Bayonet Connectors

| Motor Series                                                                                                                                          | Connector Type   |                                                                      | Brake Wires Cable Cat. No.        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------------------------------------------|-----------------------------------|
| MPL-B3xxx - xx2xAA, MPL-B4xxx-xx2xAA, MPL-B45xxx - xx2xAA, MPL-B5xxx-xx2xAA, MPL-B6xxx - xx2xAA, MPL-B8xxx-xx2xAA, MPL-B9xxx-xx2xAA  1326AB (M2L/S2L) | Bayonet          | The motor has a brake connector. Brake wires are in the brake cable. | 2090-UXxBMP-18Sxx brake cable (1) |

Table 74 - Motor Brake Cable Compatibility - Threaded DIN and Circular Plastic Connectors

| Motor Series                                                                                             | Connector Type          |                                                                                                  | Brake Wires Cable Cat. No.                                            |
|----------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| MPL-B15xxx - xx4xAA, MPL-B2xxx-xx4xAA MPS-Bxxx , MPAS-Bxxx, MPMA-Bxxx, MPAR-B1xxx, MPAR-B2xxx (series A) | Circular (threaded) DIN | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex) |

Table 75 - Motor Brake Cable Compatibility - SpeedTec DIN Connectors

| Motor Series                                                                                                                                                                                                                                                       | Connector Type          | Brake Wires                                                                                      | Cable Cat. No. (1)                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| MPL-B15xxx - xx7xAA, MPL-B2xxx-xx7xAA MPL-B3xxx - xx7xAA, MPL-B4xxx-xx7xAA, MPL-B45xxx - xx7xAA, MPL-B5xxx-xx7xAA, MPL-B6xxx - xx7xAA, MPL-B8xxx-xx7xAA MPL-B9xxx - xx7xAA MPM-Bxxx, MPF-Bxxx, MPS-Bxxx MPAS-Bxxx , MPAR-B1xxx, MPAR-B2xxx (series B), MPAR-B3xxx, | Circular (SpeedTec) DIN | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) |

| IMPORTANT   | Use surge suppression when controlling a brake coil. Refer to Brake Control Example on page 237 .   |
|-------------|-----------------------------------------------------------------------------------------------------|

Table 76 - Motor/Resistive Brake (BC) Connector

| Motor Brake Wires             | Motor Brake Wires                                 | Motor Brake Wires               | BC Connector (IAM/AM module)   | BC Connector (IAM/AM module)   |
|-------------------------------|---------------------------------------------------|---------------------------------|--------------------------------|--------------------------------|
| 2090-UXxBMP-18Sxx Brake Cable | 2090-XXNPMF-xxSxx 2090-CPBMxDF-xxAxxx Power Cable | 2090-CPBM6DF-16AAxx Power Cable |                                | BC Pin Signal                  |
|                               | BR+ BR+/MBRK+ MBRK+ 5 MBRK+                       |                                 |                                |                                |
|                               | BR- BR-/MBRK- MBRK- 6 MBRK                                                   |                                 |                                |                                |

Table 77 - Termination Specifications

| BC Connector (IAM/AM module) Recommended Wire   | BC Connector (IAM/AM module) Recommended Wire   | Size mm 2 (AWG)   | Strip Length        | Torque Value        |
|-------------------------------------------------|-------------------------------------------------|-------------------|---------------------|---------------------|
|                                                 | BC Pin Signal                                   |                   | mm (in.)            | N•m (lb•in)         |
| BC-6 BC-5 BC-4 BC-3 BC-2 BC-1                   | MBRK MBRK+ COM PWR DBRK DBRK+                                                 |                   | 0.75 (18) 10 (0.38) | 0.22…0.25 (1.9…2.2) |

Figure 58 - Brake Cable Preparation

<!-- image -->

## Apply the Motor Cable Shield Clamp

This procedure assumes you have completed wiring your motor power (MP) connector and are ready to apply the cable shield clamp.

<!-- image -->

Your drive can be equipped with either the pivot-open or slide-open cable clamp.

Follow these steps to apply the motor cable shield clamp.

1. Depress the spring loaded clamp.
2. Position the exposed portion of the cable braid directly in line with the clamp.
3. Release the spring, making sure the cable and cable braid are held secure by the clamp.
4. Attach tie wrap (slide-open clamp only) around cable and clamp for additional strain relief.
5. Repeat step 1 through step 4 for each IAM, AM, or IPIM module.

<!-- image -->

<!-- image -->

## Feedback and I/O Cable Connections

Factory made cables with premolded connectors are designed to minimize EMI and are recommended over hand-built cables to improve system performance. However, other options are available for building your own feedback and I/O cables.

Table 78 - Options for Connecting Motor Feedback and I/O

|                                                  |                                                                                                | Connection Option Connector Kit Cat. No. Cable Using this Type of Cable            |
|--------------------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Premolded connector – Motor feedback             | 2090-K6CK-D15M Motor feedback                                                                  | Refer to Table 79 and Table 80 for the flying-lead cable available for your motor. |
| Low-profile connector kit 2090-K6CK-D44M         | I/O interface, safety, and auxiliary feedback                                                  | User-supplied flying-lead cable.                                                   |
|                                                  | Low-profile connector kit 2090-K6CK-D44S0 I/O and cascading safe-off signals 2090-CS0DSDS-AAxx |                                                                                    |
| Panel-mounted breakout board kit 2090-UXBK-D15xx | Motor feedback                                                                                 | Refer to Table 79 … Table 81 for the flying-lead cable available for your motor.   |

The procedure for wiring your motor feedback varies slightly, depending on the motor family. The cables compatible with your motor or actuator depend on the connectors installed on the motor or actuator. Refer to Kinetix MP Motor and Actuator Connectors on page 106 for more information on circular DIN and bayonet connectors.

Table 79 - Motor Feedback Cable Compatibility - Bayonet Connectors

|                                    | Motor/Actuator Connector Type Feedback Type   |                                                               | Feedback Cable   | Feedback Cable                          |
|------------------------------------|-----------------------------------------------|---------------------------------------------------------------|------------------|-----------------------------------------|
|                                    |                                               |                                                               |                  | Premolded Flying-lead                   |
| MPL-Bxxxx-S/Mx2xAA                 | Bayonet                                       | High-resolution encoder                                       | 2090-UXNFBMP-Sxx | 2090-UXNFBMP-Sxx 2090-XXxFMP-Sxx MPL-A3xxx-Hx2xAA  MPLA4H2AAItl d (1)                                         |
| MPL-A4xxx-Hx2xAA MPL-A45xxx-Hx2xAA | Bayonet                                       | 1326AB-Bxxxx-M2L/S2L High-resolution encoder 2090-UXNFBMP-Sxx |                  | Incremental encoder 2090-XXxFMP-Sxx (1) |
|                                    | Bayonet                                       | F-Series Incremental encoder 2090-UXNFBHF-Sxx                 |                  | 2090-XXNFHF-Sxx                         |
|                                    | Bayonet                                       |                                                               |                  |                                         |

Refer to Flying-lead Feedback Cable Pinouts beginning on page 117 for the motor-to-drive feedback cable pinout used in your application.

Refer to Kinetix MP Motor and Actuator Connectors on page 106 for more information on circular DIN and bayonet connectors.

Table 80 - Motor Feedback Cable Compatibility - Threaded DIN Connectors

|                                            |                         | Motor/Actuator Connector Type Feedback Type   | Feedback Cable (1)   | Feedback Cable (1)                                                  |
|--------------------------------------------|-------------------------|-----------------------------------------------|----------------------|---------------------------------------------------------------------|
|                                            |                         |                                               |                      | Premolded Flying-lead                                               |
| MPL-B15xxx-V/Ex4xAA MPL-B2xxx-V/Ex4xAA     | Circular (threaded) DIN | High-resolution encoder                       | –                    | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPL-B15xxx-Hx4xAA MPL-B2xxx-Hx4xAA         | Circular (threaded) DIN | Incremental encoder                           | –                    | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPS-Bxxxx-S/M                              | Circular (threaded) DIN | High-resolution encoder                       | –                    | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPAS-Bxxxxx-V/A                            | Circular (threaded) DIN | High-resolution encoder                       | –                    | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPAR-B1xxxx-V and MPAR-B2xxxx-V (series A) | Circular (threaded) DIN | High-resolution encoder                       | –                    | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |

Table 81 - Motor Feedback Cable Compatibility - SpeedTec DIN Connectors

|                                                                                                                                            | Motor/Actuator Connector Type Feedback Type   |                                                    | Feedback Cable (1)                                                      | Feedback Cable (1)                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
|                                                                                                                                            |                                               |                                                    |                                                                         | Premolded Flying-lead                                                   |
| MPL-B15xxx-V/Ex7xAA MPL-B2xxx-V/Ex7xAA                                                                                                     | Circular (SpeedTec) DIN                       | High-resolution encoder                            | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPL-B15xxx-Hx7xAA MPL-B2xxx-Hx7xAA                                                                                                         | Circular (SpeedTec) DIN                       | Incremental encoder                                | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPL-B3xxx-S/Mx7xAA, MPL-B4xxx-S/Mx7xAA, MPL-B45xxx-S/Mx7xAA, MPL-B5xxx-S/Mx7xAA, MPL-B6xxx-S/Mx7xAA, MPL-B8xxx-S/Mx7xAA MPL-B9xxx-S/Mx7xAA | Circular (SpeedTec) DIN                       | High-resolution encoder                            | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPL-B3xxx-Hx7xAA (2) MPL-B4xxx-Hx7xAA (2) MPL-B45xxx-Hx7xAA (2) LDAT-Sxxxxxx - xBx (2)                                                     | Circular (SpeedTec) DIN                       | Incremental encoder –                              |                                                                         | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |
| MPF-Bxxxx-S/M                                                                                                                              | Circular (SpeedTec) DIN                       | High-resolution encoder                            | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPS-Bxxxx-S/M                                                                                                                              | Circular (SpeedTec) DIN                       | High-resolution encoder                            | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPM-Bxxxxx-S/M MPAS-Bxxxxx-V                                                                                                               | Circular (SpeedTec) DIN                       | High-resolution encoder                            | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-BxxxxxM3                                                                                                                              | Circular (SpeedTec) DIN                       | High-resolution encoder                            | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| RDB-Bxxxx-7/3                                                                                                                              | Circular (SpeedTec) DIN                       | High-resolution encoder                            | –                                                                       | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |
| MPAS-Bxxxxx-A                                                                                                                              | Circular (SpeedTec) DIN                       | High-resolution encoder                            | –                                                                       | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |
| LDC-Cxxxx (2)                                                                                                                              | Circular (SpeedTec) DIN                       | Incremental encoder Sin/Cos encoder or TTL encoder | –                                                                       | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |

## Flying-lead Feedback Cable Pinouts

Refer to the following tables for the motor-to-drive feedback cable pinout used in your application.

Table 82 - 2090-XXxFMP-Sxx Feedback Cables

| Bayonet Connector High-resolution Feedback  Drive MF   |
|--------------------------------------------------------|
| Connector Pin Rotary Motor i MPL-B3xxx…MPL-B9xxx-M/Sx2xAA, Connector Pin MPL-B3xxx…MPL-B9xxx-M/Sx2xAA, 1326AB-Bxxx-M2L/S2L                                                        |
| A Sin+ 1                                               |
| B Sin- 2                                               |
| C Cos+ 3                                               |
| D Cos- 4                                               |
| E Data+ 5                                              |
| F Data- 10                                             |
| K Reserved 14                                          |
| L Reserved 6                                           |
| N EPWR_9V 7                                            |
| P ECOM 6                                               |
| R TS+ 11                                               |
| S TS- –                                                |
| T Reserved 12                                          |
| U Reserved 13                                          |
| V Reserved 8                                           |

Table 83 - 2090-XXNFMF-Sxx or 2090-CFBMxDF-xxAxxx Feedback Cables

| High-resolution Feedback Incremental Feedback                                                                       | High-resolution Feedback Incremental Feedback                                              |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Drive MF Rotary Motors MPL-B15xxx…MPL-B2xxx-V/Ex4/7xAA MPF/MPS-Bxxx-M/S RDB-Bxxxxx-3/7 MPL-B3xxx…MPL-B9xxx-M/Sx7xAA | MPL-B15xxx-Hx4/7xAA MPL-B2xxx-Hx4/7xAA MPL-A3xxx-Hx7xAA MPL-A4xxx-Hx7xAA MPL-A45xxx-Hx7xAA |
| Connector Pin MPM-Bxxxxx-M/S                                                                                        | MPL-B15xxx-Hx4/7xAA MPL-B2xxx-Hx4/7xAA MPL-A3xxx-Hx7xAA MPL-A4xxx-Hx7xAA MPL-A45xxx-Hx7xAA |
| Linear Motors – LDC-Cxxxx                                                                                           | LDC-Cxxxx                                                                                  |
| Linear Actuators  MPAS-Bxxxxx-VxxSxA MPAR-Bxxxx, MPAI-Bxxxx  –                                                      | MPAS-Bxxxxx-ALMx2C LDAT-Sxxxxxx-xBx                                                        |
| 1 Sin+ Sin+ AM+ 1                                                                                                   |                                                                                            |
| 2 Sin- Sin- AM- 2                                                                                                   |                                                                                            |
|                                                                                                                     | 3 Cos+ Cos+ BM+ 3                                                                          |
| 4 Cos- Cos- BM- 4                                                                                                   |                                                                                            |
| 5 Data+ Data+ IM+ 5                                                                                                 |                                                                                            |
| 6 Data- Data- IM- 10                                                                                                |                                                                                            |
| 7 Reserved  CLK+ (1)                                                                                                | Reserved 9                                                                                 |
| 8 Reserved  CLK- (1)                                                                                                | Reserved 15                                                                                |
| 9 Reserved EPWR_5V EPWR_5V 14                                                                                       |                                                                                            |
| 10 Reserved ECOM ECOM 6                                                                                             |                                                                                            |
| 11 EPWR_9V Reserved Reserved 7                                                                                      |                                                                                            |
|                                                                                                                     | 12 ECOM Reserved Reserved 6                                                                |
| 13 TS+ TS+ TS+ 11                                                                                                   |                                                                                            |
| 14 TS- TS- TS- –                                                                                                    |                                                                                            |
| 15 Reserved Reserved S1 12                                                                                          |                                                                                            |
| 16 Reserved Reserved S2 13                                                                                          |                                                                                            |
| 17 Reserved Reserved S3 8                                                                                           |                                                                                            |

## Wire the Feedback and I/O Connectors

These procedures assume you have mounted your Kinetix 6200 and Kinetix 6500 system, completed all power wiring, and are ready to connect your feedback and I/O cables.

| For This Connection Go to                                                            |
|--------------------------------------------------------------------------------------|
| Premolded cable Connect Premolded Motor Feedback Cables on page 118 .                |
| Panel-mounted breakout board Connect Panel-mounted Breakout Board Kits on page 119 . |
| Low-profile connector Wire Low-profile Connector Kits on page 120 .                  |

## Connect Premolded Motor Feedback Cables

Motor feedback cables with premolded connectors plug directly into 15-pin motor feedback (MF) connectors on the control modules (no wiring is necessary).

## IMPORTANT

When using Bulletin 2090 cables with premolded connectors, tighten the mounting screws (finger tight) to improve system performance.

Figure 59 - IAM/AM Power Module/Control Module (MF connector)

<!-- image -->

## Connect Panel-mounted Breakout Board Kits

The 2090-UXBK-D15xx panel-mounted breakout board kit includes a DIN-rail breakout board and cable. The cable connects between the breakout board and the motor feedback (MF) connector. Wires from your flying-lead motor feedback cable connect to the terminals.

Figure 60 - IAM/AM Power Module/Control Module (MF connector)

<!-- image -->

Table 84 - Low-profile Connector Kits

| Connector Kit Cat. No.   | Description                                                                                                                                                                                       | Cable Compatibility                                   |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| 2090-K6CK-D15M           | Low-profile connector kit for motor feedback (15-pin, male, D-sub). Use with any Kinetix 6200 and Kinetix 6500 control module and compatible motors with incremental or high-resolution feedback. | 2090-XXxFMP-Sxx, 2090-XXNFMF-Sxx, 2090-CFBMxDF-CxAxxx |
| 2090-K6CK-D44M           | Low-profile connector kit for I/O (44-pin, male, D-sub). Use with any Kinetix 6200 and Kinetix 6500 control module for making I/O, safety, and auxiliary feedback connections.                    | Customer supplied                                     |
| 2090-K6CK-D44S0          | Low-profile connector kit for I/O and cascading Safe Torque Off signals (44-pin, male, D-sub). For use with any Kinetix 6200 or Kinetix 6500 (Safe Torque Off, -S0 control module).               | 2090-CS0DSDS-AAxx                                     |

Figure 61 - IAM/AM Power Module with Control Module (IOD/MF connectors)

<!-- image -->

IMPORTANT

Tightening the mounting screws is essential to ensure shield integrity of the low-profile connector covers with the drive feedback connector D-shells. Use 0.4 N·m (3.5 lb·in) torque.

## Wire Low-profile Connector Kits

The 2090-K6CK-DxxM low-profile connector kits are suitable for terminating flying-lead motor feedback, auxiliary feedback, and I/O connections. They also apply to I/O connections on the 2094-BL02 LIM module.

## Figure 62 - Wiring (15-pin) Flying-lead Feedback Cable Connections 2090-K6CK-D15M Connector Kit

<!-- image -->

Figure 63 - Wiring (44-pin) I/O, Safety, and Auxiliary Feedback Cable Connections 2090-K6CK-D44M Connector Kit

<!-- image -->

Figure 64 - Wiring (44-pin) I/O and Cascading Safe Torque Off Feedback Connections 2090-K6CK-D44S0 Connector Kit

<!-- image -->

In this example, three Safe Torque Off drives are shown using the Bulletin 2090 low-profile connector kit and cables. The right-angled cable connectors are keyed to exit left as shown. Cables loop back and cascade to the next drive or other cascading device.

Figure 65 - Cascading Safe Torque Off Cable Example

<!-- image -->

## External Shunt Module Connections

Table 85 - Shunt Module Wiring

| Use This Shunt Module                                                   | Cat. No.    | With This Drive Module   | Do This                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------|-------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power rail mounted shunt module.                                        | 2094-BSP2 – |                          | • Verify the internal shunt jumper is in place between RC-2 and RC-3 (refer to Figure 66). • Verify the thermal switch jumper is in place between TS-1 and TS-2 (refer to Figure 66).                                                                                                                                                                                                                                   |
| External passive shunt module connected to the power rail shunt module. | 1394-SRxxxx | 2094-BSP2 Shunt module   | • Remove the internal shunt jumper between RC-2 and RC-3. • Remove the thermal switch jumper between TS-1 and TS-2 (if your shunt module includes a thermal switch). • Refer to External Shunt Modules on page 50 for noise zone considerations. • Refer to Shunt Module Wiring Examples on page 225 . • Refer to the installation instructions provided with your Bulletin 1394 shunt module, publication 2090-IN004 . |

Figure 66 - Shunt Module Jumper Settings

<!-- image -->

Follow these guidelines when wiring your external passive shunt module.

| IMPORTANT   | When tightening screws to secure the wires, refer to the tables beginning on page 98 for torque values.   |
|-------------|-----------------------------------------------------------------------------------------------------------|
| IMPORTANT   | To improve system performance, run wires and cables in the wireways as established in Chapter 2 .         |

## IPIM Module Connections

An overview of the Kinetix 6000M integrated drive-motor (IDM) system connections are shown here.

- Refer to Chapter 2 on page 27, for noise zone considerations.
- Refer to Appendix A, on page 236, for an interconnect diagram featuring the Kinetix 6000M integrated drive-motor (IDM) system.
- Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for more information when wiring your IPIM module.

## IMPORTANT

To improve system performance, run wires and cables in the wireways as established in Chapter 2 .

Figure 67 - IPIM Module Connections

<!-- image -->

## RBM Module Connections

Follow these guidelines when wiring your Bulletin 2090 Resistive Brake Module (RBM).

IMPORTANT To be sure of system performance, run wires and cables in the wireways as established in Chapter 2 .

If your application requires an RBM module and you are wiring to a Bulletin 2094 IAM/AM power module, then refer to the following:

- Cable Categories for Kinetix 6200 and Kinetix 6500 Systems on page 47 to establish noise zones when mounting the RBM module on your panel.
- Resistive brake module to Bulletin 2094 drive interface cable (catalog number 2090-XXNRB-xxF0Px).
- The example diagram below and others in Appendix H, beginning on page 303 .
- The installation instructions provided with your RBM module, publication 2090-IN009 .

Figure 68 - RBM Module Connections

<!-- image -->

## Sercos Fiber-optic Cable Connections

This procedure assumes you have your Logix 5000™ Sercos interface module/ PCI card and Kinetix 6200 control modules mounted and are ready to connect the fiber-optic cables.

The Sercos fiber-optic ring is connected by using the Sercos receive (Rx) and transmit (Tx) connectors. Refer to page 62 to locate the Sercos connectors on your Kinetix 6200 control module and IPIM module. Refer to the figure below to locate the connectors on your Logix 5000 Sercos interface module or PCI card.

Plastic cable is available in lengths up to 32 m (105.0 ft). Glass cable is available in lengths between 50 m (164.2 ft) and 200 m (656.7 ft).

Figure 69 - CompactLogix, ControlLogix, and SoftLogix Sercos Connectors

<!-- image -->

Connect the cable from transmit on the Logix 5000 module to receive on the control or IPIM module, then transmit to receive (drive to drive), and from transmit on the last drive back to receive on the Logix 5000 module.

<!-- image -->

ATTENTION: To avoid damage to the Sercos Rx and Tx connectors, use only finger-tight torque when attaching the fiber-optic cables to the Kinetix 6200 control module and IPIM module. Do not use a wrench or any other mechanical assistance.

For more information, refer to Fiber-optic Cable Installation and Handling Instructions, publication 2090-IN010 .

SoftLogix and ControlLogix controllers are used in the following examples; however, CompactLogix controllers connect in the same manner.

When connecting 2094-SE02F-M00-Sx control modules, use 2090-SCEP0-2, 0.2 m (7.1 in.) cables.

Figure 70 - Fiber-optic Cable Example - SoftLogix Platform

<!-- image -->

In this example, two Logix 5000 modules are installed in separate chassis.

Figure 71 - Fiber-optic Cable Example - Two Logix Platforms

<!-- image -->

IMPORTANT

Clean the fiber-optic cable connectors prior to installation. Dust in the connectors can reduce signal strength. For more information, refer to Fiberoptic Cable Installation and Handling Instructions, publication 2090-IN010 .

When connecting 2094-BM03-M and 2094-BM05-M (double-wide) axis modules, use 2090-SCEP0-3, 0.3 m (12.0 in.) cables. When connecting 2094-BMP5-M, 2094-BM01-M, and 2094-BM02-M (single-wide) axis modules, use 2090-SCEP0-2, 0.2 m (7.1 in.) cables.

Figure 72 - Fiber-optic Cable Example - Logix Platform with Double-wide Modules

<!-- image -->

In this example, the second Kinetix 6200 system is mounted in a separate cabinet and connected with bulkhead adapters.

IMPORTANT

To avoid signal loss, do not use bulkhead adapters to connect glass cables. Use only bulkhead adapters for making plastic-to-plastic cable connections.

Figure 73 - Fiber-optic Cable Example - Logix Platform with Bulkhead Adapters

<!-- image -->

## Kinetix 6000M Integrated Drive-Motor Sercos Connections

The Kinetix 6200 Sercos ring includes the Kinetix 6000M integrated drivemotor (IDM) units and IDM power interface modules (IPIM). Fiber-optic connections are made from drive-to-drive and drive-to-IPIM module. IDM network connections continue from the IPIM module to the IDM units.

When connecting from the IPIM module to Kinetix 6200 (2094-BMxx-M) drives, you must use the 0.2 m (7.1 in.) cables.

Figure 74 - Fiber-optic Cable Example - Logix 5000 Platform with Kinetix 6000M (IPIM) Modules

<!-- image -->

In this example, all the drive modules and the IPIM module are on the same Sercos ring. The ring begins and ends at the 1756-M16SE Sercos module. IDM units (not shown for simplicity) connected to the IPIM module, are also part of this Sercos ring.

For more Kinetix 6000 IDM system examples including the IDM units, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

## Ethernet Cable Connections

This procedure assumes you have your ControlLogix or CompactLogix EtherNet/IP module and Bulletin 2094 control modules mounted and are ready to connect the Ethernet network cables.

The EtherNet/IP network is connected by using the PORT 1 and/or PORT 2 connectors.

Table 86 - EtherNet/IP Connector Location

|                                | Drive Family Cat. No. EtherNet/IP Network Refer to                           |         |
|--------------------------------|------------------------------------------------------------------------------|---------|
| Kinetix 6500 2094-EN02D-M01-Sx | Programming the safety configuration and the Logix Designer application      | page 64 |
| Kinetix 6200 2094-SE02F-M00-Sx | Programming the safety configuration                                         | page 63 |
|                                | Kinetix 6000M 2094-SEPM-B24-S Monitoring, diagnostics, and firmware upgrades | page 63 |

Shielded Ethernet cable is available in lengths up to 78 m (256 ft). However, the total length of Ethernet cable connecting drive-to-drive, drive-to-controller, or drive-to-switch must not exceed 100 m (328 ft).

If the entire channel is constructed of stranded cable (no fixed cable), then this is the equation for calculating maximum length:

Maximum Length = (113-2N)/y, meters where N = the number of connections in the channel and y = the loss factor compared to fixed cable (typically 1.2…1.5).

Figure 75 - ControlLogix and CompactLogix Ethernet Port Locations

<!-- image -->

The 1756-ENxT EtherNet/IP modules accept linear and star network configurations. The 1756-ENxTR modules and CompactLogix 5370 controllers accept linear, ring (DLR), and star network configurations.

## IMPORTANT

When using an external Ethernet switch for routing traffic between the controller and the drive, switches with IEEE-1588 time synchronization features must be used.

In this example, all devices are connected in linear topology. The Kinetix 6500 control module includes dual-port connectivity for drive-to-drive connections.

Figure 76 - Ethernet Wiring Example - Linear

<!-- image -->

2094-EN02D-M01-Sx Control Modules (bottom view)

In this example, the drives are connected by using device-level ring (DLR) topology. DLR topology is fault redundant. For example, if a device in the ring is disconnected, the rest of the devices in the ring continue to maintain communication.

IMPORTANT DLR topology requires the dual-port 1756-ENxTR module.

Figure 77 - Ethernet Wiring Example - DLR Ring

<!-- image -->

2094-EN02D-M01-Sx Control Modules (bottom view)

In this example, the devices are connected by using star topology. Each device is connected directly to the switch, making this topology fault tolerant. The 2094 power rail modules and other devices operate independently. The loss of one device does not impact the operation of the other devices.

Figure 78 - Ethernet Wiring Example - Star

<!-- image -->

2094-EN02D-M01-Sx Control Modules (bottom view)

## Notes:

## Configure the Kinetix 6000M Integrated Drive-Motor System

## Configure and Start the Kinetix 6200 and Kinetix 6500 Drive System

This chapter provides procedures for configuring the Kinetix® 6200 drive components with your Logix 5000™ Sercos communication module.

| Topic Page                                                    |
|---------------------------------------------------------------|
| Configure the Kinetix 6000M Integrated Drive-Motor System 135 |
| Configure the Drive Modules 136                               |
| Configure the Logix 5000 Sercos interface Module 142          |
| Apply Power to the Kinetix 6200 and Kinetix 6500 Drive 155    |
| Test and Tune the Axes 157                                    |

<!-- image -->

Before you begin, make sure you know the catalog number for each drive component, the Logix 5000 module, and the servo motor/actuator in your motion control application.

Configuration for the Kinetix 6000M integrated drive-motor (IDM) system follows a procedure similar to what is described in this chapter. You'll assign each IDM unit a node address and configure the IDM system in the Logix Designer application.

The IPIM module does not require configuration for your IDM units to be configured in the Sercos ring. However, you can include the IPIM module in your project by connecting it to a configured Ethernet module in the Logix 5000 chassis and adding it under the Ethernet module in the I/O configuration tree. An Add-On Profile is also needed to use the IPIM module in the project, but as a result you can view IPIM module status information in the configuration software and use it in your application program. The Ethernet connection is also used to upgrade the IPIM module firmware by using ControlFLASH™ software.

For system configuration and startup procedures specific to the IDM system, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

<!-- image -->

## Configure the Drive Modules

Follow these steps to configure the IAM power module and the control modules attached to your IAM and AM power modules.

## IMPORTANT

If you have one or more IDM power interface modules (IPIM) on your power rail, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for system configuration information specific to the Kinetix 6000M IDM system.

1. Verify that no power is applied to the IAM and AM power modules and that the communication cables are plugged into the appropriate connectors.

To verify communication, refer to Sercos Fiber-optic Cable Connections on page 126 .

| To Configure Begin With       |                                                                            |
|-------------------------------|----------------------------------------------------------------------------|
| The IAM module                | step 2                                                                     |
| Any control module            | step 4                                                                     |
| Kinetix 6000M IDM system  (1) | Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 . |

2. Set the base node address for the IAM power module by setting the Node Address switches.

Valid node addresses for Sercos communication are 001…099. The left switch sets the most significant digit (MSD) and the right switch sets the least significant digit (LSD).

| To Press                                                   |
|------------------------------------------------------------|
| Increment the (MSD/LSD) node address The plus (+) switch.  |
| Decrement the (MSD/LSD) node address The minus (-) switch. |

<!-- image -->

Setting the base node address on the IAM power module determines the node address for the control module mounted on the IAM (inverter) module. Node addressing for all slot locations on the same power rail increment (from the IAM inverter) left to right.

3. Cycle control power to initialize the IAM module.

| IMPORTANT   | The base node address setting takes effect only after the IAM power module is initialized.                                                                                            |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | When two or more IAM power modules are connected to the same Sercos interface module, each node address must be unique. Refer to the node addressing examples beginning on page 138 . |

4. Set the Sercos communication rate by using DIP switches 1 and 2.
- (1) The Kinetix 6000M IDM system supports only 8 Mbps and is hardwired for this setting.

|                                   | Setting Switch Switch Position   |
|-----------------------------------|----------------------------------|
| 4 Mbps baud rate SW2 ON           |                                  |
| 8 Mbps baud rate  (1)             | SW2 OFF                          |
| Low power light intensity SW1 OFF |                                  |
| High power light intensity SW1 ON |                                  |

The optical power setting you use depends on the type of Sercos cable you're using and the length of the cable.

| Power Setting  (1)   | Plastic (2)      | Glass (3)                              |
|----------------------|------------------|----------------------------------------|
| Low                  | ≤ 15 m (49.2 ft) | ≤ 100 m (382 ft)                       |
|                      |                  | High > 15 m (49.2 ft) > 100 m (382 ft) |

(1) Other factors include attenuation caused by the use of bulkhead connectors and cable bending.

(2) Catalog numbers 2090-SCxP.

(3) Catalog numbers 2090-SCVG.

5. Repeat step 4 for each 2094-BMxx-M axis module with 2094-SE02F-M00-Sx control module.

<!-- image -->

Figure 79 - Node Addressing Example 1

<!-- image -->

In Example 1, the Kinetix 6200 and Kinetix 6500 (6-axis) drive system 1 power rail contains four control modules, one shunt module, and one slot-filler module. The shunt module and slot-filler modules are not assigned a Sercos node address, but the system identifies them with a slot location.

Kinetix 6200 and Kinetix 6500 (2-axis) drive system 2 power rail contains two control modules. The base node address of the (system 2) control module must be set for an address of 007.

## IMPORTANT

## IMPORTANT

The node address for each AM (control) module is determined by the base node-address switch setting on the IAM power module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiber-optic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM power modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

Figure 80 - Node Addressing Example 2

<!-- image -->

In this example, Sercos interface module 1 controls axes 1…4 and module 2 controls axes 5…7. The slot-filler module is not assigned a Sercos node address, but the system identifies it with a slot location.

You can mount the two Sercos interface modules in two separate ControlLogix chassis (as shown) or you can mount them in the same chassis.

## IMPORTANT

## IMPORTANT

The node address for each AM (control) module is determined by the base node-address switch setting on the IAM power module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiber-optic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM power modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

Figure 81 - Node Addressing Example 3

<!-- image -->

In this example, the Kinetix 6200 and Kinetix 6500 (8-axis) power rail contains a double-wide IAM module, two double-wide AM modules, one single-wide AM module, and one slot-filler module. The slot-filler module is not assigned a Sercos node address, but the system identifies it with a slot location.

The leftmost slot of a double-wide module determines the node address. So, in the example above, node addresses 02, 04, and 06 (the rightmost slots of the double-wide modules) are not used.

## IMPORTANT

## IMPORTANT

The node address for each AM (control) module is determined by the base node-address switch setting on the IAM power module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiber-optic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM power modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

Figure 82 - Node Address Example 4

<!-- image -->

In this example, the Kinetix 6200 and Kinetix 6500 (5-axis) power rail contains two single-wide axis modules and one IDM system. Neither the slot-filler or IPIM module is assigned a Sercos node address, but the system identifies them with a slot location.

Node addressing on the power rail is no different than the previous examples. Node addresses 002 and 005 are available for any of the IDM units, but to avoid confusion, the node addressing for the IDM units was started at 20. Unlike the axis modules, each IDM unit has switches that determine its node address. In this example, the IDM unit node addressing is sequential, but that's optional.

## IMPORTANT

Creating a duplicate node address between the axis modules mounted on the power rail and the IDM system (in the same Sercos ring) generates error code NODE FLT 133. Each node address on the Sercos ring must be unique within the range of 001…099. Axes on the same power rail as the IPIM module do not have to be in the same Sercos ring as the IDM units.

## IMPORTANT

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM power modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

## Configure the Logix 5000 Sercos interface Module

This procedure assumes that you have wired your Kinetix 6200 and Kinetix 6500 system and have configured the communication rate and optical power switches.

For help with using the Logix Designer application as it applies to configuring the ControlLogix, CompactLogix™, or SoftLogix™ Sercos modules, refer to Additional Resources on page 10 .

## Configure the Logix 5000 Controller

Follow these steps to configure the Logix 5000 controller.

1. Apply power to your Logix 5000 chassis containing the Sercos interface module/PCI card and open your Logix Designer application.
2. From the File menu, choose New.

The New Controller dialog box opens.

<!-- image -->

3. Configure the new controller.
- a. From the Type pull-down menu, choose the controller type.
- b. From the Revision pull-down menu, choose the revision.
- c. Type the file Name.
- d. From the Chassis Type pull-down menu, choose the chassis.
- e. Enter the Logix 5000 processor slot.
4. Click OK.
5. From the Edit menu, choose Controller Properties.

The Controller Properties dialog box opens.

<!-- image -->

6. Click the Date/Time tab.
7. Check Enable Time Synchronization.

This assigns the controller as the Grandmaster clock. The motion modules set their clocks to the module you assign as the Grandmaster.

IMPORTANT

You can assign only one module in the Logix 5000 chassis as the Grandmaster clock.

8. Click OK.

## Configure the Logix 5000 Controller Module

Follow these steps to configure the Logix 5000 module.

1. Right-click I/O Configuration in the Controller Organizer and choose New Module.

The Select Module dialog box opens.

<!-- image -->

2. Expand the Motion category and select 1756-MxxSE, 1756-L60M03SE, 1768-M04SE, or 1784-PM16SE as appropriate for your actual hardware configuration.

In this example, the 1756-M16SE module is selected.

3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new module.
- a. Type the module Name.
- b. Enter the Logix 5000 Sercos module slot (leftmost slot = 0).
- c. Check Open Module Properties.
5. Click OK.

Your new module appears under the I/O Configuration folder in the Controller Organizer and the Module Properties dialog box opens.

6. Click the Sercos Interface tab and reference the table below.
7. Verify that the Data Rate setting matches DIP switch 1 (communication rate), as set on the control module, or choose the Auto Detect setting.
8. From the Cycle Time pull-down menu, choose the Cycle Time according to the table below.

<!-- image -->

| Logix 5000 Sercos Module Number of Axes Data Rate   |          |             |
|-----------------------------------------------------|----------|-------------|
| 1756-M03SE or 1756-L60M03SE                         | Up to 3  | 4 or 8 Mbps |
| 1756-M08SE Up to 8                                  |          | 4 or 8 Mbps |
| 1756-M16SE or 1784-PM16SE                           | Up to 16 | 4 or 8 Mbps |
| 1768-M04SE Up to 4                                  |          | 4 or 8 Mbps |

<!-- image -->

|             | Data Rate Number of Axes Cycle Time   |                          |
|-------------|---------------------------------------|--------------------------|
| 4 Mbps      | Up to 2 0.5 ms                        |                          |
| 4 Mbps      | Up to 4 1 ms                          |                          |
| 4 Mbps      | Up to 8 2 ms                          |                          |
| 4 Mbps      | No support for axes 9…16              | No support for axes 9…16 |
| 8 Mbps  (1) | Up to 4 0.5 ms                        |                          |
| 8 Mbps  (1) | Up to 8 1 ms                          |                          |
| 8 Mbps  (1) | Up to 16 2 ms                         |                          |

<!-- image -->

The number of axes/module is limited to the number of axes as shown in step 6 .

<!-- image -->

9. From the Transmit Power pull-down menu, choose High.
2. The default setting is High, however this setting is dependent on the cable length (distance to next receiver) and cable type (glass or plastic).
10. Enter the Transition to Phase setting.

The Transition to Phase default setting is 4 (phase 4). The Transition to Phase setting stops the ring in the phase specified.

11. Click OK.
12. Repeat step 1 through step 11 for each Logix 5000 module.

## Configure the Kinetix 6200 and Kinetix 6500 Drive Modules

Follow these steps to configure the Kinetix 6200 and Kinetix 6500 drive modules.

1. Right-click the Logix 5000 module you just created and choose New Module.

The Select Module dialog box opens.

<!-- image -->

2. Expand the Drives category and select drive components appropriate for your actual hardware configuration.

## IMPORTANT

To configure Kinetix 6200 drive modules (catalog numbers 2094SE02F-M00-Sx, 2094-BCxx-Mxx-M, and 2094-BMxx-M) you must be using the Logix Designer application or RSLogix 5000® software, version 17.00 or later.

To configure Kinetix 6000M IDM units (catalog numbers MDFSBxxxxx) you must be using the Logix Designer application or RSLogix 5000 software, version 20.01 or later.

For Kinetix 6200 and Kinetix 6500 drive modules, selection is based on your control module and power module combination. In this example, the 2094-SE02F-M00-S1 control module and 2094-BC02-M02-M IAM power module are selected.

3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new module.

a. Type the module Name.

- b. Enter the Node address.

Set the node address in the software to match the node setting on the drive. Refer to Configure the Drive Modules, step 2, on page 136 .

- c. Check Open Module Properties.
5. Click OK.
6. Click the Associated Axes tab.
7. Click New Axis.

<!-- image -->

The New Tag dialog box opens.

<!-- image -->

8. Type the axis Name.

AXIS\_SERVO\_DRIVE is the default Data Type.

9. Click OK.

The axis appears under the Ungrouped Axes folder in the Controller Organizer.

10. Assign your axis to Node 1.
11. Click Apply.

<!-- image -->

<!-- image -->

It is possible to configure the Auxiliary Axis feedback port as a Feedback Only axis. With this feature, you can configure each drive module to appear as two axes/nodes on the Sercos ring. The base node is the servo axis using the motor feedback, and the base node (plus 128) is a feedback-only axis that uses the auxiliary feedback port. Auxiliary feedback is not supported by the Kinetix 6000M IDM units.

<!-- image -->

The Auxiliary Axis (Node 129) is configured identical to Node 1 by clicking New Axis and creating a new tag.

12. Click Apply if you made changes.
13. Click the Power tab.
14. From the Bus Regulator Catalog Number pull-down menu, choose the shunt option appropriate for your actual hardware configuration.

<!-- image -->

|                                                                 | If your IAM power module is And your hardware configuration includes this shunt option Then choose   |             |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------|
| Configured as an IAM module or common-bus leader IAM module (1) | Internal shunt resistors only Internal or <none>                                                     |             |
| Configured as an IAM module or common-bus leader IAM module (1) | Bulletin 2094 (rail mounted) shunt module (2)                                                        | 2094-BSP2   |
| Configured as an IAM module or common-bus leader IAM module (1) | Bulletin 1394 passive shunt module (connected to the 2094-BSP2 shunt module)                         | 1394-SRxxxx |
| Configured as an IAM module or common-bus leader IAM module (1) | External active shunt module Internal or <none>                                                      |             |
| Configured as a common-bus follower IAM module  (3)             | Does not apply. Shunts are disabled on follower IAM module CommonBus Follow                          |             |

<!-- image -->

To avoid damage to your Bulletin 1394 external shunt module when wired to the 2094-BSP2 shunt module, verify that the proper 460V fuse is installed prior to applying power.

Refer to Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for more information.

## IMPORTANT

When configured to use the Bulletin 1394 or 2094 shunt modules, the IAM bus regulator capacity attribute displays the utilization of total shunt power available (as a percent) based on the power rail configuration.

Refer to Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for shunt power specification and examples.

15. Calculate additional bus capacitance, if this applies to your application, and enter the value here (version 20.00 or later), or refer to Appendix F on page 289 to set the Add Bus Cap parameter.

The Additional Bus Capacitance field applies only to the IAM power module.

## IMPORTANT

16. Click OK.
17. Repeat step 1 through step 16 for each Bulletin 2094 AM power module and control module combination, and each IDM unit.

DC common-bus applications must calculate Total Bus Capacitance and Additional Bus Capacitance and set the Add Bus Cap parameter in the leader IAM power module. However, you can set the parameter as shown in step 15 or by using the Logix Designer application, as shown in Appendix F.

Refer to Appendix C beginning on page 249, for more information on making the calculations. Refer to Appendix F beginning on page 289 , for more information on setting the Add Bus Cap parameter.

## Configure the Motion Group

Follow these steps to configure the motion group.

1. Right-click Motion Groups in the Controller Organizer and choose New Motion Group.

The New Tag dialog box opens.

<!-- image -->

2. Type the new motion group Name.
3. Click OK.

The new motion group appears under the Motion Groups folder.

4. Right-click the new motion group and choose Properties.
2. The Motion Group Properties dialog box opens.
5. Click the Axis Assignment tab and move your axes (created earlier) from Unassigned to Assigned.
6. Click the Attribute tab and edit the default values as appropriate for your application.
7. Click OK.

<!-- image -->

## Configure Axis Properties

Follow these steps to configure Axis properties for motor feedback.

1. Right-click an axis in the Controller Organizer and choose Properties. The Axis Properties dialog box opens.
2. Click the Drive/Motor tab.
3. Click Change Catalog.

<!-- image -->

The Change Catalog Number dialog box opens.

<!-- image -->

4. Select the motor catalog number appropriate for your application. To verify the motor catalog number, refer to the motor nameplate.
5. Click OK.
6. On the Drive/Motor tab, check Drive Enable Input Checking. When checked (default), means a hard drive-enable input signal is required. Uncheck to remove that requirement.
7. Click Apply.
8. Click the Motor Feedback tab and verify the Feedback Type shown is appropriate for your actual hardware configuration.
9. Click the Units tab and edit default values as appropriate for your application.

10. Click the Conversion tab and edit default values as appropriate for your application.

<!-- image -->

In this example, Rotary is chosen from the Positioning Mode pull-down menu.

11. Click Apply if you made changes.
12. Click the Fault Actions tab.
13. Click Set Custom Stop Action.

<!-- image -->

The Custom Stop Action Attributes dialog box opens and lets you set delay times for servo motors and RBM modules.

14. Configure the delay times.
- a. Type the Brake Engage Delay Time.
- b. Type the Brake Release Delay Time.
- c. Set the Resistive Brake Contact Delay time (0...1000 ms range).

<!-- image -->

For recommended motor brake response times, refer to the Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001. The recommended delay time for 2090-XB33-xx and 2090-XB120-xx RBM modules is 71 ms.

d. Click Close to close the Custom Stop Action Attributes dialog box.

15. Click Apply.
16. Repeat step 1 through step 15 for each Bulletin 2094 AM power module and control module combination.

Follow these steps to configure Auxiliary Axis properties.

IMPORTANT Auxiliary feedback is not supported by the Kinetix 6000M IDM units.

1. Right-click an auxiliary axis in the Controller Organizer and choose Properties.

The Axis Properties dialog box opens on the General tab.

2. If an axis is associated to the auxiliary axis node, set the Axis Configuration on the General tab of the Axis Properties dialog box to Feedback Only.
3. Click the Drive/Motor tab.

<!-- image -->

The Drive/Motor tab displays the amplifier being used and the Loop Configuration is Aux Feedback Only. This is the only choice if the amplifier is using the primary node for Servo (motor) configuration.

<!-- image -->

4. Click the Aux Feedback tab.

<!-- image -->

## IMPORTANT

The Aux Feedback tab must be configured for the auxiliary feedback type being used. In this example, an SRM feedback device is being used.

5. From the Feedback Type pull-down menu, choose the feedback type appropriate for your auxiliary feedback motor.
6. Click OK.
7. Verify your Logix 5000 program and save the file.

## Download the Program

After completing the Logix 5000 configuration you must download your program to the Logix 5000 processor.

## Apply Power to the Kinetix 6200 and Kinetix 6500 Drive

This procedure assumes that you have wired and configured your Kinetix 6200 and Kinetix 6500 system (with or without the LIM module) and your Sercos interface module.

<!-- image -->

ATTENTION: Capacitors on the DC bus can retain hazardous voltages after input power has been removed. Before working on the drive, measure the DC bus voltage to verify it has reached a safe level or wait the full time interval as indicated in the warning on the front of the drive. Failure to observe this precaution could result in severe bodily injury or loss of life.

Refer to the Line Interface Module Installation Instructions, publication 2094-IN005, when troubleshooting the LIM module status indicators, and for the location of LIM module circuit breakers, connectors, and status indicators.

Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for connector locations and when troubleshooting the IPIM module and IDM unit status indicators.

Follow these steps to apply power to the Kinetix 6200 and Kinetix 6500 drive system.

1. Disconnect the load to the motor.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, disconnect the load to the motor. Make sure each motor is free of all linkages when initially applying power to the system.

2. Determine your source of control power.
3. Observe the control module four-character status indicator.

| If Your Control Power Then       |                                                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sourced from a LIM module     | 1. Verify that CB1, CB2, and CB3 are in the OFF position. 2. Apply three-phase input power to the LIM module VAC Line connector. 3. Set CB3 to the ON position. 4. Set CB2 to the ON position. 5. Go to main step 3. |
| Is not sourced from a LIM module | 1. Apply (95…264V AC) control power to the IAM module (CPD connector). 2. Go to main step 3.                                                                                                                         |

<!-- image -->

The four-character status indicator displays several messages, for example BOOT, INIT, and LOAD, while the control module powers-up.

| If the Four-character Status Display is  (1)   | Then                                                                 |
|------------------------------------------------|----------------------------------------------------------------------|
|                                                | ON Go to step 4 .                                                    |
| Not ON                                         | 1. Check your control power connections. 2. Go back to main step 2 . |

4. Determine your source of three-phase input power.
5. Observe the control module four-character status display. The four-character status display scrolls the node address, then cycles through phases until final configuration is reached.
6. Observe the status indicators on the front of the control module. Refer to troubleshooting tables for the Drive, Comm, and Bus status indicators in Control Module Status Indicators on page 198. Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for IPIM module and IDM unit status indicator troubleshooting tables.
7. Observe the three Sercos indicators on the Logix 5000 Sercos module.

| If Your Three-phase Power Then   |                                                                                                                                                                                |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sourced from a LIM module     | 1. Set CB1 to the ON position. 2. Verify the Hardware Enable Input signal for each axis is at 0 volts.  (1) 3. Go to main step 5 .                                             |
| Is not sourced from a LIM module | 1. Apply 324…528V AC (460V) input power to the IAM module (IPD connector). 2. Verify the Hardware Enable Input signal for each axis is at 0 volts.  (1) 3. Go to main step 5 . |

| Four-character Status Indicator Status Do This                       |                                                                                                                            |                                                                                |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Scrolling CP-0                                                       | The drive is looking for a closed Sercos ring (phase 0). Wait for CONFIGURING or take corrective action.                   | Check fiber-optic connections.                                                 |
| Scrolling CP-1                                                       | The drive is looking for active nodes (phase 1). Wait for CONFIGURING or take corrective action.                           | Check node addressing.                                                         |
| Scrolling CP-2                                                       | The drive is configuring nodes for communication (phase 2). Wait for CONFIGURING or take corrective action.                | Check program motor and drive configuration against installed hardware.        |
| Scrolling C O N F I G U R I N G                                      | The drive is configuring device-specific parameters (phase 3). When phase 4 is reached the drive displays the drive state. | Check motor catalog number against selection.  (1)                             |
| Scrolling drive state (for example S H U T D O W N or S T O P P E D) | The drive is configured and active (phase 4). Go to step 6                                                                 | .                                                                              |
|                                                                      |                                                                                                                            | Scrolling error code message Drive is faulted. Go to Fault Codes on page 189 . |

| Three Sercos Indicators Status Do This       |                                                   |                                                                                        |
|----------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------------|
|                                              | Flashing green and red Establishing communication | Wait for steady green on all three indicators.                                         |
|                                              | Steady green Communication ready                  | Go to Test and Tune the Axes on page 157 .                                             |
| Not flashing green and red/ not steady green | Sercos module is faulted                          | Go to the appropriate Logix 5000 manual for specific instructions and troubleshooting. |

## Test and Tune the Axes

These procedures assume that you have configured your Kinetix 6200 and Kinetix 6500 drive, your Logix 5000 Sercos interface module, and applied power to the system.

For help with using the Logix Designer application, as it applies to testing and tuning your axes with ControlLogix, CompactLogix, or SoftLogix Sercos modules, refer to Additional Resources on page 10 .

## Test the Axes

Follow these steps to test the axes.

1. Verify that the load was removed from each axis.
2. Right-click an axis in your Motion Group folder and choose Properties. The Axis Properties dialog box opens.
3. Click the Hookup tab.
4. Type 2.0 as the number of revolutions for the test or another number more appropriate for your application.
5. Apply Hardware Enable Input signal for the axis you are testing.

<!-- image -->

|                         | This Test Performs this Test                                                                                                          |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Test Marker (1)         | Verifies marker detection capability as you rotate the motor shaft.                                                                   |
| Test Feedback (1)       | Verifies feedback connections are wired correctly as you rotate the motor shaft. Also, lets you define polarity.                      |
| Test Command & Feedback | Verifies motor power and feedback connections are wired correctly as you command the motor to rotate. Also, lets you define polarity. |

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply 24V ENABLE signal only to the axis you are testing.

6. Click the desired test (Marker/Feedback/Command &amp; Feedback) t to verify connections.

The Online Command dialog box opens. Follow the on-screen test instructions. When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

7. Click OK.

The Online Command - Apply Test dialog box opens (Feedback and Command &amp; Feedback tests only). When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

8. Click OK.
9. Determine if your test completed successfully.

<!-- image -->

## Tune the Axes

The load observer feature (available with drive firmware revision 1.049 or later) can provide good performance without having to tune your axis. Using load observer with auto-tuned gains can maximize system performance. Refer to Appendix D beginning on page 253 for more load observer information.

Follow these steps to tune the axes.

1. Verify that the load is still removed from the axis being tuned.

<!-- image -->

ATTENTION: To reduce the possibility of unpredictable motor response, tune your motor with the load removed first, then re-attach the load and perform the tuning procedure again to provide an accurate operational response.

2. Click the Tune tab.
3. Type values for Travel Limit and Speed.
3. In this example, Travel Limit = 5 and Speed = 10. The actual value of programmed units depend on your application.
4. From the Direction pull-down menu, choose a setting. Forward Uni-directional is default.
5. Check Tune boxes as appropriate for your application.
6. Apply Hardware Enable Input signal for the axis you are tuning.

<!-- image -->

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply 24V ENABLE signal only to the axis you are tuning.

IMPORTANT Hardware Enable input for IDM units is on the IPIM module.

7. Click Start Tuning to auto-tune your axis.

The Online Command - Tune Servo dialog box opens. When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

8. .Click OK.

The Tune Bandwidth dialog box opens.

<!-- image -->

Actual bandwidth values (Hz) depend on your application and can require adjustment once motor and load are connected.

9. Record your bandwidth data for future reference.
10. Click OK.

The Online Command - Apply Tune dialog box opens. When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

11. Click OK.
12. Determine if your test completed successfully.
13. Repeat Test and Tune the Axes for each axis.

<!-- image -->

## Configure the Drive Modules

<!-- image -->

## Configure and Start the Kinetix 6200 and Kinetix 6500 Drive System

This chapter provides procedures for configuring your Kinetix 6200 and Kinetix 6500 system components with your ControlLogix® EtherNet/IP module.

| Topic Page                                                 |
|------------------------------------------------------------|
| Configure the Drive Modules 161                            |
| Configure the Logix EtherNet/IP Module 165                 |
| Apply Power to the Kinetix 6200 and Kinetix 6500 Drive 180 |
| Test and Tune the Axes 181                                 |

<!-- image -->

Before you begin make sure you know the catalog number for each drive component, the Logix module, and the servo motor/actuator in your motion control application.

Follow these steps to configure the node address of your IAM power module. This setting establishes the node address for each control module installed on the Bulletin 2094 power rail.

1. Verify that there is no power applied to the IAM and AM power modules and that the communication cables are plugged into the appropriate connectors.

To verify communication, refer to Ethernet Cable Connections on page 130 .

| To Configure Begin With   |        |
|---------------------------|--------|
| The IAM module            | step 2 |
| Any control module        | step 4 |

2. Set the base node address for the IAM power module by setting the Node Address switches.

Valid node addresses for EtherNet/IP network communication are 001…254. The left switch sets the most significant digit (MSD) and the right switch sets the least significant digit (LSD).

| To Press                                                   |
|------------------------------------------------------------|
| Increment the (MSD/LSD) node address The plus (+) switch.  |
| Decrement the (MSD/LSD) node address The minus (-) switch. |

<!-- image -->

<!-- image -->

Setting the base node address on the IAM power module determines the node address for the control module mounted on the IAM (inverter) module. Node addressing for all slot locations on the same power rail increment (from the IAM inverter) left to right. The Kinetix 6500 drives have a private network address of http://192.168.1.x, although you do not have to use it.

The final octet of the IP address is determined by the IAM base node address. For example, if using the private network and your node address switches are set to 001, the IP address is http://192.168.1.1. If your base node address switches are set to 002, the IP address is http:// 192.168.1.2, and so on.

3. Cycle control power to initialize the IAM module.

## IMPORTANT

The base node address setting takes effect only after the IAM power module is initialized.

## IMPORTANT

When two or more IAM power modules are connected to the same EtherNet/IP module, each node address must be unique.

Refer to the node addressing examples beginning on page 163 .

To configure the IP address without using the private network, refer to Knowledgebase Technote: Kinetix 6500: Procedure for Setting the Ethernet IP address .

4. Verify the node address for the IAM and each AM control module. The node address scrolls across the four-character display. If your IAM power module base node address is 001, then the node address for the adjacent AM control module is 192.168.1.2, and so on.

Figure 83 - Node Addressing Example 1

<!-- image -->

In Example 1, the Kinetix 6200 and Kinetix 6500 (6-axis) drive system 1 power rail contains four control modules, one shunt module, and one slot-filler module. The shunt module and slot-filler modules are not assigned an IP address, but the system identifies them with a slot location.

Kinetix 6200 and Kinetix 6500 (2-axis) drive system 2 power rail contains two control modules. The base node address of the (system 2) control module must be set for an address of 007.

## IMPORTANT

## IMPORTANT

The IP address for each AM (control) module is determined by the basenode address switch setting on the IAM power module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiber-optic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail; however, you can replace slot-filler modules with AM power modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

Figure 84 - Node Addressing Example 2

<!-- image -->

In this example, EtherNet/IP module 1 controls axes 1…4 and module 2 controls axes 5…7. The slot-filler module is not assigned an IP address, but the system identifies it with a slot location.

You can mount the two EtherNet/IP modules in two separate ControlLogix chassis (as shown) or you can mount them in the same chassis.

## IMPORTANT

Slot-filler modules must be used to fill any unoccupied slot on the power rail; however, you can replace slot-filler modules with AM power modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

## Configure the Logix EtherNet/IP Module

This procedure assumes that you have wired your Kinetix 6200 and Kinetix 6500 drive system.

For help using the Logix Designer application as it applies to configuring the ControlLogix EtherNet/IP modules, refer to Additional Resources on page 10 .

## Configure the Logix Controller

Follow these steps to configure the Logix controller.

1. Apply power to your Logix chassis containing the EtherNet/IP module and open the Logix Designer application.
2. From the File menu, choose New.
3. The New Controller dialog box opens.
3. Configure the new controller.
- a. From the Type pull-down menu, choose the controller type.
- b. From the Revision pull-down menu, choose the revision.
- c. Type the file Name.
- d. From the Chassis Type pull-down menu, choose the chassis.
- e. Enter the Logix processor slot (leftmost slot = 0).
4. Click OK.
5. From the Edit menu, choose Controller Properties.

<!-- image -->

The Controller Properties dialog box opens.

<!-- image -->

6. Click the Date/Time tab.
7. Check Enable Time Synchronization.

This assigns the controller as the Grandmaster clock. The motion modules set their clocks to the module you assign as the Grandmaster.

IMPORTANT

You can assign only one module in the Logix chassis as the Grandmaster clock.

8. Click OK.

## Configure the Logix Module

Follow these steps to configure the Logix module.

1. Right-click I/O Configuration in the Controller Organizer and choose New Module.

The Select Module dialog box opens.

<!-- image -->

2. Expand the Communications category and select 1756-EN2F, 1756-EN2T, 1756-EN2TR, or 1756-EN3TR as appropriate for your actual hardware configuration.

In this example, the 1756-EN2T module is selected.

3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new module.
- a. Type the module Name.
- b. Enter the Logix EtherNet/IP module slot (leftmost slot = 0).
- c. Select an Ethernet Address option.

In this example, the Private Network address is selected.

- d. Enter the address of your EtherNet/IP module.
2. In this example, the last octet of the address is 100.
5. Click Change in the Module Definition area.

The Module Definition dialog box opens.

<!-- image -->

6. From the Time Sync Connection pull-down menu, choose Time Sync and Motion.

IMPORTANT Time Sync functionality is what enables motion control on an Ethernet network. Without this setting, you won't be able to run your motion application.

7. Click OK to close the Module Definition dialog box.
8. Click Yes when prompted to confirm your module definition changes.
9. Click OK to close the New Module dialog box.

<!-- image -->

Your new module appears under the I/O Configuration folder in the Controller Organizer.

10. Repeat step 1 through step 9 for each Logix module.

## Configure the Kinetix 6200 and Kinetix 6500 Drive Modules

IMPORTANT

To configure Kinetix 6200 and Kinetix 6500 drive modules (catalog numbers 2094-EN02D-M01-Sx, 2094-BCxx-Mxx-M, and 2094-BMxx-M) you must be using the Logix Designer application or RSLogix 5000® software, version 18 or later.

Follow these steps to configure the Kinetix 6200 and Kinetix 6500 drive modules.

1. Right-click the Logix EtherNet/IP module you just created and choose New Module.

The Select Module dialog box opens.

<!-- image -->

2. Expand the Motion category and select your 2094-EN02D-M01-Sx control module as appropriate for your actual hardware configuration.
3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new control module.
- a. Type the module Name.
- b. Select an Ethernet Address option.

In this example, the Private Network address is selected.

<!-- image -->

To configure the IP address without using the private network, refer to Knowledgebase Technote: Kinetix 6500: Procedure for Setting the Ethernet IP address .

- c. Enter the address of your EtherNet/IP module.

In this example, the last octet of the address is 1. This must match the base node address of the IAM power module.

5. Click Change in the Module Definition area.
2. The Module Definition dialog box opens.
6. From the Power Structure pull-down menu, choose the Bulletin 2094 power module appropriate for your application.
4. In the example, the 2094-BC02-M02-M IAM module is chosen.
7. Click OK to close the Module Definition dialog box.
8. Click Yes when prompted to confirm your module definition changes.
9. Click OK to close the Module Properties dialog box.
8. The 2094-EN02D-M01-S1 module appears under the EtherNet/IP module in the I/O Configuration folder.
10. Right-click the 2094-EN02D-M01-S1 module you just created and choose Properties.
10. The Module Properties dialog box opens.
11. Click the Associated Axes tab.
12. Click New Axis.

<!-- image -->

<!-- image -->

<!-- image -->

The New Tag dialog box opens.

<!-- image -->

13. Type the axis Name.

AXIS\_CIP\_DRIVE is the default Data Type.

14. Click OK.

The new axis (Axis\_1) appears under Motion Groups&gt;Ungrouped Axes in the Controller Organizer and is assigned as Axis 1.

<!-- image -->

<!-- image -->

- It is possible to configure Axis 2 as a Feedback Only axis. With this optional feature, you can configure each control module to appear as two axes on the EtherNet/IP network. Axis 1 is the servo axis using the motor feedback port, and Axis 2 is a feedback-only axis using the auxiliary feedback port.

<!-- image -->

Axis 2 is configured identical to Axis 1 by clicking New Axis and creating a new tag.

15. Click Apply.

16. Click the Digital Input tab.

<!-- image -->

The digital inputs (1…4) are assigned default values. You can reassign them, using the pull-down menus, according to the needs of your application.

They can also be unassigned, if your application does not use them or you want to remove the default assignments.

17. From the Digital Input 1 pull-down menu, choose Unassigned. This removes the Enable assignment from IOD-41.
18. Click Apply.
19. Click the Power tab.

<!-- image -->

<!-- image -->

20. From the Bus Regulator Action pull-down menu, choose the shunt option appropriate for your actual hardware configuration.

| Choose To                                                                                       |
|-------------------------------------------------------------------------------------------------|
| Disable Disable the shunt resistor internal to the IAM power module.                            |
| Shunt Regulator Choose an internal or external shunt option.                                    |
| Common Bus Follower (1) To configure your IAM power module as a common-bus follower IAM module. |

(1) Drive will not accept CommonBus Follower selection if three-phase power or DC bus power is applied.

| If You Choose Then   |                                                                                                                                                                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shunt Regulator      | Select Internal to use the shunt resistor internal to the IAM power module. Select External to use the External Shunt pull-down menu and choose between the Bulletin 1394 shunt modules and the Bulletin 2094-BSP2 shunt module. (1) |

- (1) Drive will not accept Internal, 2094-BSP2, or 1394-SRxxxx selection if DC bus voltage is present without having threephase power applied.

<!-- image -->

To avoid damage to your Bulletin 1394 external shunt module when wired to the 2094-BSP2 shunt module, verify that the proper 460V fuse is installed prior to applying power.

Refer to Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for more information.

## IMPORTANT

When configured to use the Bulletin 1394 or 2094 shunt modules, the IAM bus regulator capacity attribute displays the utilization of total shunt power available (as a percent) based on the power rail configuration. Refer to Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for more information.

21. Calculate additional bus capacitance, if this applies to your application, and enter the value here (version 18.00 or later), or refer to Appendix F on page 289 to set the Add Bus Cap parameter.

The Additional Bus Capacitance field only applies to the IAM power module.

## IMPORTANT

22. Click OK.

23. Repeat step 1 through step 18 for each 2094-EN02D-M01-Sx control module.

DC common-bus applications must calculate Total Bus Capacitance and Additional Bus Capacitance and set the Add Bus Cap parameter in the leader IAM power module. However, you can set the parameter as shown in step 21 or by using the Logix Designer application as shown in Appendix F.

Refer to Appendix C beginning on page 249, for more information on making the calculations. Refer to Appendix F beginning on page 289 , for more information on setting the Add Bus Cap parameter.

## Configure the Motion Group

Follow these steps to configure the motion group.

1. Right-click Motion Groups in the Controller Organizer and choose New Motion Group.

The New Tag dialog box opens.

<!-- image -->

2. Type the new motion group Name.
3. Click OK.

The new motion group appears under the Motion Groups folder.

4. Right-click the new motion group and choose Properties.
2. The Motion Group Properties dialog box opens.
5. Click the Axis Assignment tab and move your axes (created earlier) from Unassigned to Assigned.
6. Click the Attribute tab and edit the default values as appropriate for your application.
7. Click OK.

<!-- image -->

## Configure Axis Properties

Follow these steps to configure auxiliary axis properties.

1. Right-click an auxiliary axis in the Controller Organizer and choose Properties.
2. The Axis Properties dialog box opens on the General category.
3. If an axis is associated to the auxiliary axis node, set the Axis Configuration to Feedback Only.
2. Click the Master Feedback category.
3. Configure the auxiliary axis feedback.
- a. From the Type pull-down menu, choose the auxiliary feedback type.
- b. From the Startup Method pull-down menu, choose the auxiliary feedback startup method.

<!-- image -->

<!-- image -->

## IMPORTANT

The Aux Feedback tab must be configured for the auxiliary feedback type being used. In this example, a Hiperface feedback device is being used.

Follow these steps to configure axis properties.

1. Right-click an axis in the Controller Organizer and choose Properties.
2. Click the General category.

The General and Associated Module dialog box opens.

<!-- image -->

3. From the General pull-down menus, change configuration settings as needed for your application.
4. From the Associated Module&gt;Module pull-down menu, choose your Kinetix 6500 drive.
3. The drive catalog number populates the Module Type and Power Structure fields.
5. Click Apply.
6. Click the Motor category.
6. The Motor Device Specification dialog box opens.
7. From the Data Source pull-down menu, choose Catalog Number.
8. Click Change Catalog.

<!-- image -->

The Change Catalog Number dialog box opens.

<!-- image -->

9. Select the motor catalog number appropriate for your application. To verify the motor catalog number, refer to the motor name plate.
10. Click OK to close the Change Catalog Number dialog box.
11. Click Apply.
4. Motor data specific to your motor appears in the Nameplate / Datasheet Phase to Phase parameters field.
12. Click the Scaling category and edit the default values as appropriate for your application.

13. Click Apply, if you make changes.

<!-- image -->

14. Click the Load category and edit the default values as appropriate for your application.
15. Click Apply, if you make changes.
16. Click the Actions category.

<!-- image -->

The Actions to Take Upon Conditions dialog box opens.

<!-- image -->

From this dialog box, you can program actions and change the action for exceptions (faults). Refer to Logix 5000 Controller and Drive Behavior on page 202 for more information.

17. Click the Exceptions category.

The Action to Take Upon Exception Condition dialog box opens.

<!-- image -->

From this dialog box you can change the action for exceptions (faults). Refer to Logix 5000 Controller and Drive Behavior on page 202 for more information.

<!-- image -->

In the Logix Designer application, version 32 and later, Disable replaced StopDrive as the default Action.

18. Select the Parameter List category.

The Motion Axis Parameters dialog box opens.

<!-- image -->

19. From the Parameter Group pull-down menu, choose the appropriate group. By default, all parameters are shown in the dialog box.

## Apply Power to the Kinetix 6200 and Kinetix 6500 Drive

From the Parameter List category you can set delay times for servo motors and RBM modules. For recommended motor brake delay times, refer to the Kinetix Rotary Motion Specifications Technical Data, publication GMC-TD001 .

For example, The recommended ResistiveBrakeContactDelay time (0…1000 ms) is 71 ms.

20. Click OK.
21. Repeat step 1 through step 20 for each Bulletin 2094 AM power module and control module combination.
22. Verify your Logix program and save the file.

## Download the Program

After completing the Logix configuration, you must download your program to the Logix processor.

This procedure assumes that you have wired and configured your Kinetix 6200 and Kinetix 6500 system (with or without the LIM module) and your EtherNet/ IP module.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Bulletin 2094 power rail and drive modules prior to applying power. Once power is applied, connector terminals may have voltage present even when not in use.

Refer to the Line Interface Module Installation Instructions, publication 2094-IN005, when troubleshooting the LIM module status indicators, and for the location of LIM module circuit breakers, connectors, and status indicators.

Follow these steps to apply power to the Kinetix 6200 and Kinetix 6500 system.

1. Disconnect the load to the motor.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, disconnect the load to the motor. Make sure each motor is free of all linkages when initially applying power to the system.

2. Determine your source of control power.
3. Observe the control module four-character status display.

| If Your Control Power Then       |                                                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sourced from a LIM module     | 1. Verify that CB1, CB2, and CB3 are in the OFF position. 2. Apply three-phase input power to the LIM module VAC Line connector. 3. Set CB3 to the ON position. 4. Set CB2 to the ON position. 5. Go to main step 3. |
| Is not sourced from a LIM module | 1. Apply (95…264V AC) control power to the IAM module (CPD connector). 2. Go to main step 3.                                                                                                                         |

<!-- image -->

Four-character Status Display

## Test and Tune the Axes

The four-character status display provides several messages, for example BOOT, INIT, LOAD, DONE, and TEST while the control module powersup.

| If the Four-character Status Display is   | Then                                                                 |
|-------------------------------------------|----------------------------------------------------------------------|
|                                           | ON Go to step 4 .                                                    |
| Not ON                                    | 1. Check your control power connections. 2. Go back to main step 2 . |

4. Determine your source of three-phase input power.
5. Observe the control module four-character status display.
6. Observe the status indicators on the front of the control module. Refer to troubleshooting tables for the PORT1, PORT2, OK, DC Bus, and Safety Lock status indicators in Control Module Status Indicators on page 198 .
7. Observe the four-character display and status indicators on the Logix EtherNet/IP module.

| If Your Three-phase Power Then   |                                                                                                                                                                                 |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sourced from a LIM module     | 1. Set CB1 to the ON position. 2. Verify the Hardware Enable Input signal for each axis is at 0 volts. 3. Go to main step 5 .                                                   |
| Is not sourced from a LIM module | 1. Apply 324…528V AC (460V) input power to the IAM power module (IPD connector). 2. Verify the Hardware Enable Input signal for each axis is at 0 volts. 3. Go to main step 5 . |

| Four-character Status Display Drive Status   |                                                                                                         |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------|
| BOOT, INIT, LOAD, DONE, TEST                 | The drive is initializing. This sequence of four-character words continues to scroll up to three times. |
| Scrolling FW Version: x.xxx                  | The drive is scrolling the current drive firmware revision.                                             |
|                                              | Scrolling IP = 192.168.1.1 The drive is scrolling the drive IP address.                                 |
|                                              | Scrolling CONFIGURING The drive is receiving configuration information from the controller.             |
| Scrolling STANDBY                            | The drive is trying to establish communication with the Logix EtherNet/IP module.                       |
|                                              | Scrolling STOPPED The drive is fully configured, but the control loops are not enabled.                 |
| Scrolling error code message                 | The drive is faulted. Refer to Interpret Status Indicators beginning on page 188 .                      |

Refer to troubleshooting tables for the four-character display and LINK, NET, and OK EtherNet/IP module status indicators in the ControlLogix Enhanced Redundancy System User Manual, publication 1756-UM535 .

This procedure assumes that you have configured your Kinetix 6200 and Kinetix 6500 drive, your ControlLogix EtherNet/IP module, and applied power to the system.

## IMPORTANT

Before proceeding with testing and tuning your axes, verify that the control module status indicators are operating as described in Control Module Status Indicators on page 198 .

For help using the Logix Designer application as it applies to testing and tuning your axes with ControlLogix EtherNet/IP modules, refer to Additional Resources on page 10 .

## Test the Axes

Follow these steps to test the axes.

1. Verify that the load was removed from each axis.
2. Right-click an axis in your Motion Group folder and choose Properties. The Axis Properties dialog box opens.
3. Click the Hookup Tests category.
4. In the Test Distance field, enter the desired test distance. The Position Units are defined in Axis Properties&gt;Scaling category.

<!-- image -->

<!-- image -->

| Hookup Test Definitions   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Marker                    | Verifies marker detection capability as you manually rotate the motor shaft. The test completes when the drive either detects the marker or when the motor moves the distance specified in the Test Distance field. If the marker remains undetected and the test completes successfully, it means the motor moved the full test distance. If the marker remains undetected and the test fails, the motor did not move the full test distance. Run this test after running the Motor Feedback and Motor and Feedback tests. |
| Commutation               | Verifies the commutation offset and commutation polarity of the motor. This test is required for third-party or custom permanent-magnet motors that are not available as a catalog number in the Motion Database.                                                                                                                                                                                                                                                                                                           |
| Motor Feedback            | Verifies feedback connections are wired correctly as you manually rotate the motor shaft. The test completes when the drive determines that the motor moved the full distance specified in the Test Distance field. Run this test before the Motor and Feedback Test to verify that the feedback can be read properly.                                                                                                                                                                                                      |
| Motor and Feedback        | Verifies motor power and feedback connections are wired correctly as the drive commands the motor to rotate. Because the drive is rotating the motor, this test requires full bus power to run. Run the Motor Feedback test before running this test to verify that the feedback is being read correctly.                                                                                                                                                                                                                   |

5. Determine your need for a hardware enable input at IOD-41 on the I/O connector.

Digital input 1 (IOD-41) is configured as Enable in the Logix Designer application by default. You may have changed that on page 172 .

<!-- image -->

| If Digital Input 1 is configured as Then   |
|--------------------------------------------|
| Enable Go to step 6 .                      |
| Unassigned Go to step 7 .                  |

6. Apply Hardware Enable Input signal for the axis you are testing.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply 24V ENABLE signal only to the axis you are testing.

7. Click the desired test to verify connections.

The Motor and Feedback test is chosen in this example.

8. Click Start.

The Logix Designer - Motor and Feedback Test dialog box opens. The Test State is Executing.

<!-- image -->

When the test completes successfully, the Test State changes from Executing to Passed.

<!-- image -->

9. Click OK.

This dialog box opens asking if the direction was correct.

10. Click Yes.
11. If the test fails, this dialog box opens.
12. Click OK.
- a. Verify the Bus status indicator turned solid green during the test.
- b. Verify that the Hardware Enable Input signal is applied to the axis you are testing.
- c. Verify unit values entered in the Scaling category.
- d. Return to step 7 and run the test again.

<!-- image -->

<!-- image -->

## Tune the Axes

The load observer feature (available with drive firmware revision 2.001 or later) can provide good performance without having to tune your axis. Using load observer with auto-tuned gains can maximize system performance. Refer to Motion System Tuning Application Techniques, publication MOTION-AT005 , for more load observer information. Refer to the Load Observer Feature section.

Follow these steps to tune the axes.

1. Verify that the load is still removed from the axis being tuned.

<!-- image -->

ATTENTION: To reduce the possibility of unpredictable motor response, tune your motor with the load removed first, then re-attach the load and perform the tuning procedure again to provide an accurate operational response.

2. Click the Autotune category.
3. Type values for Travel Limit and Speed.
3. In this example, Travel Limit = 50 and Speed = 2. The actual value of programmed units depends on your application.
4. From the Direction pull-down menu, choose a setting appropriate for your application.
5. Forward Uni-directional is default.
5. Edit other fields as appropriate for your application.
6. Determine your need for a hardware enable input at IOD-41 on the I/O connector.

<!-- image -->

Digital input 1 (IOD-41) is configured as Enable in the Logix Designer application by default. You may have changed that on page 172 .

<!-- image -->

7. Apply Hardware Enable Input signal for the axis you are tuning.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply 24V ENABLE signal only to the axis you are tuning.

8. Click Start.

The RSLogix - Autotune dialog box opens. When the test completes, the Test State changes from Executing to Success.

<!-- image -->

Tuned values populate the Loop and Load parameter tables. Actual bandwidth values (Hz) depend on your application and may require adjustment once motor and load are connected.

9. Click OK to close the RSLogix 5000 - Autotune dialog box.
10. Click OK to close the Axis Properties dialog box.
11. If the test fails, this dialog box opens.
- a. Click OK.
- b. Make an adjustment to motor velocity.
- c. Refer to the appropriate Logix motion module user manual for more information.
- d. Return to step 8 and run the test again.
12. Repeat Test and Tune the Axes for each axis.

<!-- image -->

## Notes:

## Safety Precautions

## Troubleshoot the Kinetix 6200 and Kinetix 6500 Drive System

This chapter provides troubleshooting tables for your Kinetix® 6200 and Kinetix 6500 system components.

| Topic Page                                   |
|----------------------------------------------|
| Safety Precautions 187                       |
| Interpret Status Indicators 188              |
| General System Anomalies 200                 |
| Logix 5000 Controller and Drive Behavior 202 |

Observe the following safety precautions when troubleshooting your Kinetix 6200 and Kinetix 6500 drive.

<!-- image -->

ATTENTION: Capacitors on the DC bus may retain hazardous voltages after input power has been removed. Before working on the drive, measure the DC bus voltage to verify it has reached a safe level or wait the full time interval as indicated in the warning on the front of the drive. Failure to observe this precaution could result in severe bodily injury or loss of life.

<!-- image -->

<!-- image -->

ATTENTION: Do not attempt to defeat or override the drive fault circuits. You must determine the cause of a fault and correct it before you attempt to operate the system. Failure to correct the fault could result in personal injury and/or damage to equipment as a result of uncontrolled machine operation.

ATTENTION: Provide an earth ground for test equipment (oscilloscope) used in troubleshooting. Failure to ground the test equipment could result in personal injury.

## Interpret Status Indicators

Refer to these troubleshooting tables to identify faults, potential causes, and the appropriate actions to resolve the fault. If the fault persists after attempting to troubleshoot the system, please contact your Rockwell Automation sales representative for further assistance.

## Kinetix 6000M IDM System Error Codes

The IAM module reports a single, generic IPIM Fault whenever a fault occurs on any IPIM in the same backplane as the IAM module. All IPIM faults result in an open contactor. The Logix Axis Tag for this fault is IPIMFault.

The IPIM module is not a Sercos device, so the IAM module reports any IPIM faults to the Logix motion subsystem. IPIM faults are reset by performing a fault reset on the IAM module. Issuing a fault reset command to the IAM module also generates a fault reset to all the IPIM modules in the same backplane as the IAM. Detailed information about the IPIM fault status may be obtained by messaging to the IAM module.

Connecting the IPIM module into the Logix environment as an EtherNet/IP™ device does not disable fault reporting through the IAM module. Only the IAM fault reporting lets the Logix motion sub-system take action based on the IPIM module fault status. IPIM faults are also reported to Logix over the Ethernet connection. However, IPIM faults must be reset by applying a fault reset instruction to the IAM module. The integration of the IPIM module into the Logix environment through the EtherNet/IP network provides additional capabilities you may choose to take advantage of in your Logix program.

Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for more information on troubleshooting the IDM drive-motor system.

## Four-character Display Messages

The control modules include a four-character display for status and fault messages. The display scrolls to display long text strings.

The Four-character Display Messages table lists the messages along with their priorities. When messages of different priorities need to be displayed, for example, when the drive has both a fault and an alarm, only the higher priority message is displayed. When messages of equal priority are needed, for example, when there is more than one fault, the messages are displayed in a round-robin fashion.

The IP address is displayed only once after powerup and an IP address has been acquired. The safety signature ID is displayed for 20 seconds when a new safety configuration is applied from the safety configuration tool.

Table 87 - Four-character Display Messages

| Drive Condition                                          | Display String                                                                   |                                                                                  |                                                                                  |          |                                      |
|----------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------|--------------------------------------|
| Drive Condition                                          | Auxiliary Feedback Not Configured as Feedback Only                               | Auxiliary Feedback Configured as Feedback Only                                   | Axis 1 Axis 1 Axis 2                                                             | Priority | Maximum Number of Messages Displayed |
| IP Address Display  (1)                                  | IP = xxx.xxx.xxx.xxx                                                             |                                                                                  |                                                                                  |          | 1 2                                  |
| Sercos Node Address Display  (2)                         | Sercos NODE = xx                                                                 |                                                                                  |                                                                                  | 1 2      |                                      |
| Safety Signature ID  (3)                                 | SAFETY SIGNATURE = xxxxxxx                                                       |                                                                                  |                                                                                  | 1 2      |                                      |
|                                                          | Firmware Upgrade FIRMWARE UPDATE                                                 |                                                                                  |                                                                                  | 1 2      | 2 2                                  |
| Decelerating to a Stop as a Result of a Fault ABORTING   |                                                                                  |                                                                                  | Refer to footnote (4)                                                            | 1 2      | 2 2                                  |
| Initialization Fault - Std. and Fault Code (5)           | INIT FLT Sxx                                                                     | X1:INIT FLT Sxx                                                                  | X2:INIT FLT Sxx                                                                  | 3        | 4 (6)                                |
| Initialization Fault - Mfg. and Fault Code  (5)          | INIT FLT Mxx                                                                     | X1:INIT FLT Mxx                                                                  | X2:INIT FLT Mxx                                                                  | 3        | 4 (6)                                |
| Safety Fault  (5)                                        | SAFE FLT xx                                                                      |                                                                                  | Refer to footnote (4)                                                            | 3        | 4 (6)                                |
| Node Fault (5)                                           | NODE FLT xx                                                                      |                                                                                  | Refer to footnote (4)                                                            | 3        | 4 (6)                                |
| Major Fault - Std. and Fault Code  (5)                   | FLT Sxx                                                                          | X1:FLT Sxx                                                                       | X2:FLT Sxx                                                                       | 3        | 4 (6)                                |
| Major Fault - Mfg. and Fault Code  (5)                   | FLT Mxx                                                                          | X1:FLT Mxx                                                                       | X2:FLT Mxx                                                                       | 3        | 4 (6)                                |
| Minor Fault - Std. and Fault Code (5)                    | FLT Sxx                                                                          | X1:FLT Sxx                                                                       | X2:FLT Sxx                                                                       | 4        | 3 (7)                                |
| Minor Fault - Mfg. and Fault Code  (5)                   | FLT Mxx                                                                          | X1:FLT Mxx                                                                       | X2:FLT Mxx                                                                       | 4        | 3 (7)                                |
| Inhibit - Std. and Fault Code (5)                        | INHIBIT Sxx                                                                      |                                                                                  | Refer to footnote (4)                                                            | 4        |                                      |
| Inhibit Fault - Mfg. and Fault Code  (5)                 | INHIBIT Mxx                                                                      |                                                                                  | Refer to footnote (4)                                                            | 4        | 5 2                                  |
|                                                          | Safe Limited Speed SAFE LIMITED SPEED                                            |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |
| Power-up  (8)                                            | ‘BOOT’…’INIT’…’LOAD’…’DONE’…’BOOT’…’INIT’…’DONE’…‘LOAD’…’TEST’…FW Version: X.XXX | ‘BOOT’…’INIT’…’LOAD’…’DONE’…’BOOT’…’INIT’…’DONE’…‘LOAD’…’TEST’…FW Version: X.XXX | ‘BOOT’…’INIT’…’LOAD’…’DONE’…’BOOT’…’INIT’…’DONE’…‘LOAD’…’TEST’…FW Version: X.XXX | 6 10     |                                      |
| Waiting for CIP™ connection STANDBY                      |                                                                                  |                                                                                  |                                                                                  | 6 10     |                                      |
|                                                          | Connecting CONNECTING                                                            |                                                                                  |                                                                                  | 6 10     |                                      |
| Configuring Drive Attributes CONFIGURING                 |                                                                                  |                                                                                  |                                                                                  | 6 10     |                                      |
| Synchronizing  (1)                                       | SYNCING                                                                          |                                                                                  |                                                                                  | 6 10     |                                      |
| Waiting for DC-bus Up PRE-CHARGE                         |                                                                                  |                                                                                  |                                                                                  | 6 10     |                                      |
| Drive has been Shutdown SHUTDOWN                         |                                                                                  |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |
| Drive Axis has Stopped STOPPED                           |                                                                                  |                                                                                  | Refer to footnote (9)                                                            | 6 10     |                                      |
| Drive is Starting STARTING                               |                                                                                  |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |
| Drive is Running RUNNING                                 |                                                                                  |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |
| Drive is Executing a Test Procedure TESTING              |                                                                                  |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |
| Decelerating to a Stop as a Result of a Disable STOPPING |                                                                                  |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |
| Alarm Fault - Standard Fault Code (5)                    | ALARM Sxx                                                                        | X1:ALARM Sxx                                                                     | X2:ALARM Sxx                                                                     | 6 10     |                                      |
| Alarm Fault - Mfg. Specific Fault Code  (5)              | ALARM Mxx                                                                        | X1:ALARM Mxx                                                                     | X2:ALARM Mxx                                                                     | 6 10     |                                      |
|                                                          | Node Alarm NODE ALARM xx                                                         |                                                                                  | Refer to footnote (4)                                                            | 6 10     |                                      |

Refer to the table on page 181 for a description of the messages that scroll across the display during powerup.

## Fault Codes

These fault code tables are designed to help you resolve anomalies. When a fault is detected, the four-character status indicator scrolls the display message. This is repeated until the fault code is cleared.

Table 89 - FLT Sxx Fault Codes

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                          |                                                                                                                                                                                   |                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                      |                          | FLT S02…MTR COMMUTATION Illegal Hall State State of Hall feedback inputs is incorrect. Improper connections.                                                                      |                                                                                                | • Check Hall wiring at motor feedback (MF) connector. • Check 5V power supply to the encoder.                                                 |
|                                                                                                                      |                          | FLT S03…MTR OVERSPEED FL Motor Overspeed Motor speed has exceeded 125% of maximum rated speed.                                                                                    | FLT S03…MTR OVERSPEED FL Motor Overspeed Motor speed has exceeded 125% of maximum rated speed. | • Check cables for noise.                                                                                                                     |
| (Kinetix 6500 drives only)                                                                                           |                          | • Check tuning. FLT S04…MTR OVERSPEED UL (Kiti6500 dil) Motor Overspeed Motor speed has exceeded user velocity limits. Motor Overspeed Motor speed has exceeded user velocity limits.                                                                                                                                                                                   | • Check tuning. FLT S04…MTR OVERSPEED UL (Kiti6500 dil) Motor Overspeed Motor speed has exceeded user velocity limits. Motor Overspeed Motor speed has exceeded user velocity limits.                                                                                                | • Check cables for noise.                                                                                                                     |
| FLT S05…MTR OVERTEMP FL nn Motor Overtemperature                                                                     |                          | The motor thermostat, motor thermistor, or encoder temperature sensor indicates that the motor factory temperature limit has been exceeded. The nn subcode is defined as follows: | High motor ambient temperature and/or Excessive Current.                                       | • Operate within (not above) the continuous torque rating for the ambient temperature. • Lower ambient temperature or increase motor cooling. |
| FLT S05…MTR OVERTEMP FL nn Motor Overtemperature                                                                     |                          | 01: Motor Thermostat or Thermistor. Motor wiring error.                                                                                                                           |                                                                                                | Check motor wiring at motor feedback (MF) connector.                                                                                          |
| FLT S05…MTR OVERTEMP FL nn Motor Overtemperature                                                                     |                          |                                                                                                                                                                                   |                                                                                                | 02: Encoder Temperature Sensor. Incorrect motor selection. Verify the proper motor has been selected.                                         |
| FLT S06…MTR OVERTEMP UL nn (Kinetix 6500 drives only)                                                                | Motor Overtemperature    | The motor thermostat, motor thermistor, or encoder temperature sensor indicates that the motor factory temperature limit has been exceeded. The nn subcode is defined as follows: | High motor ambient temperature and/or Excessive Current.                                       | • Operate within (not above) the continuous torque rating for the ambient temperature. • Lower ambient temperature or increase motor cooling. |
| FLT S06…MTR OVERTEMP UL nn (Kinetix 6500 drives only)                                                                | Motor Overtemperature    | 01: Motor Thermostat or Thermistor. Motor wiring error.                                                                                                                           |                                                                                                | Check motor wiring at motor feedback (MF) connector.                                                                                          |
| FLT S06…MTR OVERTEMP UL nn (Kinetix 6500 drives only)                                                                | Motor Overtemperature    |                                                                                                                                                                                   |                                                                                                | 02: Encoder Temperature Sensor. Incorrect motor selection. Verify the proper motor has been selected.                                         |
| FLT S07…MTR OVERLOAD FL Motor Thermal Protection                                                                     |                          | The thermal model for the motor indicates that the temperature has exceeded 110% of its rating.                                                                                   | The machine duty cycle requires an RMS current exceeding the continuous rating of the motor.   | Change the command profile to reduce speed or increase time.                                                                                  |
| FLT S08…MTR OVERLOAD UL (Kinetix 6500 drives only)                                                                   | Motor Thermal Protection | The thermal model for the motor indicates that the temperature has exceeded a user programmable limit.                                                                            | The machine duty cycle requires an RMS current exceeding the continuous rating of the motor.   | Change the command profile to reduce speed or increase time.                                                                                  |

For information on troubleshooting SAFE FLT fault codes, refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Safety Reference Manual, publication 2094-RM001 .

Table 88 - Fault Code Summary

| Fault Code Type Description   |                                                                                                                                                            |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FLT Sxx                       | Standard runtime anomalies.                                                                                                                                |
| FLT Mxx                       | Standard runtime anomalies.                                                                                                                                |
| INIT FLT Sxx                  | Anomalies that prevent normal operation and occur during the initialization process.                                                                       |
| INIT FLT Mxx                  | Anomalies that prevent normal operation and occur during the initialization process.                                                                       |
| NODE FLTxx                    | Anomalies that prevent normal operation of all drives on the power rail.                                                                                   |
| NODE ALARM xx                 | Anomalies that prevent normal operation of all drives on the power rail, but do not result in any action other than reporting the alarm to the controller. |
| INHIBIT Sxx                   | Conditions that prevent normal operation and indicate that the drive module is prevented from being enabled. INHIBIT Mxx                                   |
| ALARM Sxx ALARM Mxx           | Warnings of conditions that may affect normal operation, but do not result in any action other than reporting the alarm to the controller.                 |

<!-- image -->

Fault codes triggered by conditions that fall outside factory-set limits are identified by FL at the end of the display message. For example, FLT S03…MTR OVERSPEED FL.

Fault codes triggered by conditions that fall outside user-set limits are identified by UL at the end of the display message. For example, FLT S04…MTR OVERSPEED UL.

Table 89 - FLT Sxx Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                                                                                                                          |                                                                               |                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                      |                                                                                                                                                          | Motor cables shorted.                                                         | Verify continuity of motor power cable and connector.                                                                                                                                                                                                                        |
|                                                                                                                      |                                                                                                                                                          | Motor winding shorted internally.                                             | Disconnect motor power cables from the motor. If the motor is difficult to turn by hand, it may need to be replaced.                                                                                                                                                         |
| FLT S10…INV OVERCURRENT IPM Fault                                                                                    | The IPM fault output indicates that the power transistors were turned off because of overcurrent, overtemperature, or power supply                       | The drive temperature is too high.                                            | • Check for clogged vents or defective fan. • Make sure cooling is not restricted by insufficient space around the unit. • Verify ambient temperature is not too high.                                                                                                       |
|                                                                                                                      | problems.                                                                                                                                                | Operation above continuous power rating and/or product environmental ratings. | • Operate within the continuous power rating. • Reduce acceleration rates. • Reduce deceleration rates.                                                                                                                                                                      |
|                                                                                                                      |                                                                                                                                                          | The drive has a short circuit, overcurrent, or failed component.              | Remove all power and motor connections, and preform a continuity check from the DC bus to the U, V, and W motor outputs. If a continuity exists, check for wire fibers between terminals, or send drive in for repair.                                                       |
|                                                                                                                      |                                                                                                                                                          | IAM or AM power module fan failed.                                            | Replace the failed module.                                                                                                                                                                                                                                                   |
|                                                                                                                      | FLT S11…INV OVERTEMP FL Inverter Overtemperature Inverter thermal switch tripped.                                                                        | The cabinet ambient temperature is above rating.  The machine duty cycle      | Check the cabinet temperature.                                                                                                                                                                                                                                               |
|                                                                                                                      |                                                                                                                                                          | requires an RMS current exceeding the continuous rating of the inverter.      | Change the command profile to reduce speed or increase time.                                                                                                                                                                                                                 |
|                                                                                                                      |                                                                                                                                                          | The airflow access to the drive system is limited or blocked.                 | Check airflow and re-route cables away from the drive system.                                                                                                                                                                                                                |
| FLT S13…INV OVERLOAD FL Inverter Thermal Protection                                                                  | The thermal model for the power transistors indicates that the temperature has exceeded 110% of its rating.                                              | The machine duty cycle requires an RMS current                                | Change the command profile to reduce speed or                                                                                                                                                                                                                                |
| FLT S14…INV OVERLOAD UL (Kinetix 6500 drives only)                                                                   | Inverter Thermal Protection The thermal model for the power transistors indicates that the temperature has exceeded the user programable limit.                                                                                                                                                          | exceeding the continuous rating of the inverter.                              | increase time.                                                                                                                                                                                                                                                               |
|                                                                                                                      |                                                                                                                                                          | Wiring error.                                                                 | • Check motor power wiring. • Check input power wiring.                                                                                                                                                                                                                      |
| FLT S16…GROUND CURRENT Ground Fault                                                                                  | Excessive ground current was detected in the converter.                                                                                                  | Motor internal ground short. Replace motor.                                   |                                                                                                                                                                                                                                                                              |
|                                                                                                                      |                                                                                                                                                          | Internal malfunction.                                                         | Disconnect motor power cable from drive and enable drive with current limit set to 0. If fault clears, then a wiring error or motor internal anomaly exists. If fault remains, call your sales representative.                                                               |
|                                                                                                                      | FLT S18…CONV OVERTEMP FL Converter Overtemperature Converter thermal switch tripped.                                                                     | Excessive heat exists in the power circuitry.                                 | • Reduce acceleration rates. • Reduce duty cycle (ON/OFF) of commanded motion. • Increase time permitted for motion. • Use larger IAM power module. • Check for clogged vents or defective fan. • Make sure cooling is not restricted by insufficient space around the unit. |
| FLT S20…CONV OVERLOAD FL Converter Thermal Protection                                                                | The thermal model for the converter indicates that the temperature has exceeded its rating.                                                              | Excessive current is being                                                    | • Reduce acceleration rates. • Reduce duty cycle (ON/OFF) of commanded motion.                                                                                                                                                                                               |
| FLT S21…CONV OVERLOAD UL (Kinetix 6500 drives only)                                                                  | Converter Thermal Protection The thermal model for the converter indicates that the temperature has exceeded a user-programmable limit.                  | drawn by the power circuitry.                                                 | • Increase time permitted for motion. • Use larger IAM power module.                                                                                                                                                                                                         |
| FLT S22…AC POWER LOSS AC Power Loss                                                                                  | All three AC input phases are detected as absent when an axis is enabled.                                                                                | Axis was enabled when main (three-phase) power was removed.                   | Disable axis before removing power.                                                                                                                                                                                                                                          |
| FLT S23…AC PHASE LOSS nn AC Phase Loss                                                                               | Some, but not all AC input phases are detected as absent. The nn subcode is defined as follows: 01: L1 is missing. 02: L2 is missing. 03: L3 is missing. | Faulty AC line control equipment.                                             | Check input AC voltage on all phases.                                                                                                                                                                                                                                        |
| FLT S25…PRECHARGE FAILURE Pre-charge Failure                                                                         | The converter precharge circuit detected that the DC bus did not reach an appropriate voltage level after charging for a period of time.                 |                                                                               | Low AC input voltage. Check input AC voltage on all phases Internal malfunction. Call your sales representative.                                                                                                                                                             |

Table 89 - FLT Sxx Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                     |                                                                                                                                                                            |                                                                                                                                                                             |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FLT S29…SHUNT OVERLOAD FL Shunt Thermal Protection                                                                   |                                                     | The thermal model for the shunt circuitry indicates that the temperature has exceeded its rating.                                                                          |                                                                                                                                                                             | • Use a properly sized shunt or modify duty cycle of the application.                                                                                                 |
| FLT S30…SHUNT OVERLOAD UL (Kinetix 6500 drives only)                                                                 | Shunt Thermal Protection                            | The thermal model for the shunt circuitry indicates that the temperature has exceeded a user-programmable limit.                                                           |                                                                                                                                                                             | • System uses internal shunt and requires external shunt for additional capacity.                                                                                     |
| FLT S31…SHUNT MODULE Shunt Module Fault                                                                              |                                                     | The shunt module in a multi-axis system has a fault.                                                                                                                       | Over-temperature fault indicator on Bulletin 2094 shunt module is steady red. Shunt-fault indicator on Bulletin 2094 shunt module is                                        | Refer to Temperature Fault Status Indicator on page 200 . Refer to Shunt Fault Status Indicator on page 200                                                           |
| FLT S33…BUS UNDERVOLT FL Bus Undervoltage                                                                            |                                                     | With three-phase power present, the DC bus voltage is below limits. DC bus voltage fell below the undervoltage limit while an axis on the follower power rail was enabled. | DC bus voltage for 460V system is below 275V.                                                                                                                               | • Verify voltage level of the incoming AC power. • Check AC power source for glitches or line drop. • Install an uninterruptible power supply (UPS) on your AC input. |
| (Kinetix 6500 drives only)                                                                                           | Bus Undervoltage                                    | yp • Disable follower axis before removing power. FLT S34…BUS UNDERVOLT UL (Kiti6500 dil) Bus Undervoltage The DC bus voltage is measured below a user limit when the DC bus was expected The DC bus voltage is measured below a user limit when the DC bus was expected to be charged.                                                                                                                                                                            | power.                                                                                                                                                                      | Change the deceleration or motion profile.                                                                                                                            |
| FLT S35…BUS OVERVOLT FL Bus Overvoltage                                                                              |                                                     | The DC bus voltage is measured above a factory limit.                                                                                                                      | Excessive regeneration of When the motor is driven by an external mechanical power source, it may regenerate too much peak energy through the drive power supply. The       | Use a larger system (motor and drive).                                                                                                                                |
|                                                                                                                      | FLT S38…FUSE BLOWN Blown Fuse (Bus Loss)            | A blown fuse was detected in the power structure.                                                                                                                          | Blown fuse.                                                                                                                                                                 | Call your Rockwell Automation sales representative to return module for repair.                                                                                       |
| factory limit. FLT S42…MTR AQB STATE UL Motor Feedback State Error                                                   |                                                     | The number of illegal state transitions of the AQB encoder signals has exceeded a                                                                                          |                                                                                                                                                                             | • Use shielded cables with twisted pair wires.                                                                                                                        |
| FLT S41…AUX AQB STATE FL Aux Feedback State Error                                                                    | FLT S41…MTR AQB STATE FL Motor Feedback State Error | The number of illegal state transitions of the AQB encoder signals has exceeded a user limit.                                                                              | The motor feedback wiring is open, shorted, or missing. The auxiliary feedback wiring is open, shorted, or missing. The motor feedback wiring is open, shorted, or missing. | • Route the feedback away from potential noise sources. • Check the system grounds. • Replace the motor/encoder.  • Use shielded cables with twisted pair wires.      |
| FLT S42…AUX AQB STATE UL Aux Feedback State Error                                                                    |                                                     | • On sin/cos encoders, the sum of the square of the sin/cos signals has been                                                                                               | The auxiliary feedback wiring is open, shorted, or missing.                                                                                                                 | • Route the feedback away from potential noise sources. • Check the system grounds. • Replace the motor/encoder.                                                      |
| FLT S43…MTR FDBK LOSS FL                                                                                             | Feedback Loss                                       | measured below a factory limit. • On sin/cos encoders, the sum of the square of the sin/cos signals has been measured below a user limit.                                  | The motor feedback wiring is open, shorted, or missing.                                                                                                                     | • Check motor encoder wiring. • Run Hookup test in the Logix Designer                                                                                                 |
|                                                                                                                      |                                                     | • On TTL encoders, the absolute value of the differential A/B signals is below a factory limit. • On TTL encoders, the absolute value of the differential A/B signals is below a application. FLT S43…AUX FDBK LOSS FL The auxiliary feedback wiring is openshortedor missing                                                                                                                                                                            | The auxiliary feedback wiring is open, shorted, or missing.                                                                                                                 |                                                                                                                                                                       |
| FLT S44…MTR FDBK LOSS UL (Kinetix 6500 drives only)                                                                  | Motor Feedback Loss                                 |                                                                                                                                                                            | The motor feedback wiring is open, shorted, or missing.                                                                                                                     | • Check motor encoder wiring. • Run Hookup test in the Logix Designer                                                                                                 |
| (Kinetix 6500 drives only)                                                                                           | Aux Feedback Loss                                   | • On TTL encoders, the absolute value of the differential A/B signals is below a user limit. • On TTL encoders, the absolute value of the differential A/B signals is below a p  application. FLT S44…AUX FDBK LOSS UL (Kiti6500 dil) Aux Feedback Loss The auxiliary feedback wiring ihtdii                                                                                                                                                                            | The auxiliary feedback wiring is open, shorted, or missing.                                                                                                                 |                                                                                                                                                                       |
| FLT S45…MTR FDBK COMM FL FLT S45…AUX FDBK COMM FL                                                                    | Feedback Serial Comms                               | The number of consecutive missed or corrupted serial data packets from the feedback device has exceeded a factory set limit.                                               | Communication was not established with an intelligent encoder.                                                                                                              | • Verify motor selection. • Verify the motor supports automatic identification. • Verify motor encoder wiring. • Consult Possible Solutions for FLT S47               |
|                                                                                                                      | Motor Fdbk Serial Comms                             |                                                                                                                                                                            |                                                                                                                                                                             |                                                                                                                                                                       |
| FLT S46…MTR FDBK COMM UL (Kinetix 6500 drives only)  FLT S46…AUX FDBK COMM UL                                        |                                                     | The number of consecutive missed or corrupted serial data packets from the feedback device has exceeded a user set limit.                                                  | Communication was not established with an intelligent encoder.                                                                                                              | • Verify motor selection. • Verify the motor supports automatic identification.                                                                                       |
| (Kinetix 6500 drives only)                                                                                           | Aux Feedback Serial Comms                           |                                                                                                                                                                            |                                                                                                                                                                             | • Verify motor encoder wiring.                                                                                                                                        |

Table 89 - FLT Sxx Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                       |                                                                                                                                                                 |                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FLT S47…MTR ENC SELF TEST nn                                                                                         | Feedback Self Test                                    | The Hiperface feedback device has detected an internal error. The nn subcode is defined as follows: 01: INCORRECT ALIGNMENT DATA 02: INCORRECT INTERNAL ANGULAR OFFSET 03: DATA FIELD PARTITIONING TABLE DESTROYED 04: ANALOG LIMIT VALUES NOT AVAILABLE 05: INTERNAL I2C BUS INOPERATIVE 06: INTERNAL CHECKSUM ERROR 07: ENCODER RESET OCCURRED AS A RESULT OF PROGRAM MONITORING 08: COUNTER OVERFLOW 09: PARITY ERROR 10: CHECKSUM OF TRANSMITTED DATA IS INCORRECT 11: UNKNOWN COMMAND CODE 12: NUMBER OF TRANSMITTED DATA IS INCORRECT 13: TRANSMITTED COMMAND AGRUMENT IS NOT ALLOWED 14: THE SELECTED DATA FIELD MAY NOT BE WRITTEN TO 15: INCORRECT ACCESS CODE 16: SIZE OF SPECIFIED DATA FIELD CANNOT BE CHANGED 17: SPECIFIED WORD ADDRESS LIES OUTSIDE THE DATA FIELD 18: ACCESS TO NON-EXISTENT DATA FIELD 28: VALUE MONITORING OF THE ANALOG SIGNALS (process data) 29: TRANSMITTER CURRENT CRITICAL (contamination, transmitter breakage) 29: TRANSMITTER CURRENT CRITICAL () • Replace motor if fault continues FLT S47…AUX ENC SELF TEST nn                                                                                                                                                                 | The Hiperface feedback device has detected an internal error. The nn subcode is defined as follows: 01: INCORRECT ALIGNMENT DATA 02: INCORRECT INTERNAL ANGULAR OFFSET 03: DATA FIELD PARTITIONING TABLE DESTROYED 04: ANALOG LIMIT VALUES NOT AVAILABLE 05: INTERNAL I2C BUS INOPERATIVE 06: INTERNAL CHECKSUM ERROR 07: ENCODER RESET OCCURRED AS A RESULT OF PROGRAM MONITORING 08: COUNTER OVERFLOW 09: PARITY ERROR 10: CHECKSUM OF TRANSMITTED DATA IS INCORRECT 11: UNKNOWN COMMAND CODE 12: NUMBER OF TRANSMITTED DATA IS INCORRECT 13: TRANSMITTED COMMAND AGRUMENT IS NOT ALLOWED 14: THE SELECTED DATA FIELD MAY NOT BE WRITTEN TO 15: INCORRECT ACCESS CODE 16: SIZE OF SPECIFIED DATA FIELD CANNOT BE CHANGED 17: SPECIFIED WORD ADDRESS LIES OUTSIDE THE DATA FIELD 18: ACCESS TO NON-EXISTENT DATA FIELD 28: VALUE MONITORING OF THE ANALOG SIGNALS (process data) 29: TRANSMITTER CURRENT CRITICAL (contamination, transmitter breakage) 29: TRANSMITTER CURRENT CRITICAL () • Replace motor if fault continues FLT S47…AUX ENC SELF TEST nn                                                                                                                                                                 | • Check motor feedback cable for proper connectivity and continuity • Check motor phasing (U, V, W) and Hiperface feedback 15-pin wire connections at the drive • Review Electrical Noise Reduction on page 36 – See bonding painted panels on page 37 – See wire-braid bonding on page 38 • Cycle control power • Check feedback shield connection • Reduce shock and vibration to motor • Upgrade firmware, revision 2.045 or later (Kinetix 6200 drives) • Upgrade firmware, revision 2.010 or later (Kinetix 6500 drives) |
|                                                                                                                      | FLT S50…POS HW OTRAVEL Hardware Overtravel - Positive | Axis moved beyond the physical travel limits in the positive direction.                                                                                         | Dedicated overtravel input is inactive.                                                                                                                         | • Check wiring. • Verify motion profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                      |                                                       | inactive. • Verify axis configuration in software. FLT S51…NEG HW OTRAVEL Hardware Overtravel - Negative Axis moved beyond the physical travel limits in the negative direction Axis moved beyond the physical travel limits in the negative direction.                                                                                                                                                                 | Dedicated overtravel input is inactive.                                                                                                                         | • Check wiring. • Verify motion profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| FLT S52…POS SW OTRAVEL (Kinetix 6200 drives only)                                                                    | Software Overtravel - Positive                        |                                                                                                                                                                 |                                                                                                                                                                 | • Verify motion profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| (Kinetix 6200 drives only)                                                                                           | Software Overtravel - Negative                        | Axis position exceeded maximum software setting.  Axis position exceeded maximum software setting.  • Verify overtravel settings are appropriate. FLT S53…NEG SW OTRAVEL Software Overtravel Negative                                                                                                                                                                 | Axis position exceeded maximum software setting.  Axis position exceeded maximum software setting.  • Verify overtravel settings are appropriate. FLT S53…NEG SW OTRAVEL Software Overtravel Negative                                                                                                                                                                 | • Verify motion profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                      |                                                       | FLT S54…POSN ERROR Excessive Position Error Position error limit was exceeded.                                                                                  | Improperly sized drive or motor.                                                                                                                                | • Increase the feed forward gain. • Increase following error limit or time. • Check position loop tuning. • Verify sizing of system.                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                      |                                                       | FLT S54…POSN ERROR Excessive Position Error Position error limit was exceeded.                                                                                  | Mechanical system out of specifications.                                                                                                                        | • Verify mechanical integrity of system within specification limits. • Check motor power wiring.                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                      | FLT S55…VEL ERROR nn Excessive Velocity Error         | The velocity error has exceeded a limit for a period of time. The nn subcode is defined as follows: 00:Velocity error referenced to the velocity loop feedback. | Improperly sized drive or motor.                                                                                                                                | • Increase velocity error limit or time. • Check velocity loop tuning. • Verify sizing of system.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| configurations).                                                                                                     | FLT S55…VEL ERROR nn Excessive Velocity Error         | 01:Velocity error referenced to the nonvelocity feedback (in dual-feedback                                                                                      | Mechanical system out of specifications.                                                                                                                        | • Verify mechanical integrity of system within specification limits. • Check motor power wiring. • Reduce acceleration.                                                                                                                                                                                                                                                                                                                                                                                                       |
| FLT S56…OVERTORQUE (Kinetix 6500 drives only)                                                                        | Overtorque Limit                                      | Motor torque has exceeded a user programmable setting.                                                                                                                                                                 | • Overly aggressive motion profile • Mechanical binding                                                                                                         | • Verify motion profile. • Verify Overtorque settings are appropriate. • Verify sizing of system. • Verify torque offset                                                                                                                                                                                                                                                                                                                                                                                                      |
| FLT S56…OVERTORQUE (Kinetix 6500 drives only)                                                                        | Overtorque Limit                                      | Motor torque has exceeded a user programmable setting.                                                                                                                                                                 | Mechanical system out of specifications.                                                                                                                        | • Verify mechanical integrity of system within specification limits.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FLT S57…UNDERTORQUE (Kinetix 6500 drives only)                                                                       | Undertorque Limit                                     | Motor torque has fallen below a user programmable setting.                                                                                                                                                                 | • Improperly configured limit • Improperly configured motion • Improperly drive/motor sizing                                                                    | • Verify motion profile. • Verify Overtorque settings are appropriate. • Verify sizing of system.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| FLT S57…UNDERTORQUE (Kinetix 6500 drives only)                                                                       | Undertorque Limit                                     | Motor torque has fallen below a user programmable setting.                                                                                                                                                                 | Mechanical system out of specifications.                                                                                                                        | • Verify mechanical integrity of system within specification limits.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FLT S60…ILLEGAL MODE Illegal Control mode                                                                            |                                                       | An illegal mode of operation was attempted.                                                                                                                     | Axis 1 was configured for dual feedback or load feedback with Axis 2 also configured for Feedback Only operation, but with different feedback attribute values. | • Use Aux Feedback for one axis only. • Verify Axis 1 and Axis 2 have identical feedback configuration for aux feedback.                                                                                                                                                                                                                                                                                                                                                                                                      |
| FLT S60…ILLEGAL MODE Illegal Control mode                                                                            |                                                       | An illegal mode of operation was attempted.                                                                                                                     |                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Table 89 - FLT Sxx Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                |                                                                        |                                                                                                             |                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| FLT S61…ENABLE INPUT Drive Enable Input                                                                              |                                | The hardware enable input was deactivated while the drive was enabled. | An attempt was made to enable the axis through software while the Drive Enable hardware input was inactive. | Disable the Drive Enable Input fault.                                                                                                               |
| FLT S61…ENABLE INPUT Drive Enable Input                                                                              |                                | The hardware enable input was deactivated while the drive was enabled. | The Drive Enable input transitioned from active to inactive while the axis was enabled.                     | Verify that Drive Enable hardware input is active whenever the drive is enabled through software.                                                   |
| FLT S62…CONTROLLER (Kinetix 6500 drives only)                                                                        | Controller Initiated Exception | The controller has requested the drive to generate an exception.       | User configured software overtravel                                                                         | • Move axis out of soft overtravel range. • Clear soft overtravel fault. • Check soft overtravel configuration. • Consult controller documentation. |

Table 90 - FLT Mxx Fault Codes

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                          |                                                                                                                                |                                                                                                          |                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                      | FLT M01…SELF SENSING Self-sensing Startup Fault          | The self-sensing commutation start-up algorithm failed.                                                                        | Extremely light or heavy load on the motor.                                                              | Clear faults and re-try.                                                                                                           |
|                                                                                                                      | FLT M01…SELF SENSING Self-sensing Startup Fault          | The self-sensing commutation start-up algorithm failed.                                                                        | Mechanical obstruction.                                                                                  | • Reduce friction. • Check for mechanical obstruction.                                                                             |
| FLT M02…MOTOR VOLTAGE Motor Voltage Mismatch                                                                         |                                                          | Motor voltage incompatible with drive voltage.                                                                                 | Check the Logix Designer configuration.                                                                  | Correct the Logix Designer configuration.                                                                                          |
| FLT M02…MOTOR VOLTAGE Motor Voltage Mismatch                                                                         |                                                          | Motor voltage incompatible with drive voltage.                                                                                 |                                                                                                          | Wrong motor connected to drive. Connect appropriate motor to drive.                                                                |
| FLT M04…MTR FDBK FILTER nn (Kinetix 6500 drives only)                                                                |                                                          | Motor Feedback Filter Excessive levels of noise have been detected by the digital feedback filter. The nn field is             | The motor feedback wiring is open, shorted, or missing.                                                  | • Use shielded cables with twisted pair wires. • Route the feedback away from potential noise sources. • Check the system grounds. |
| FLT M04…AUX FDBK FILTER nn (Kinetix 6500 drives only)                                                                | Aux Feedback Filter                                      | defined as follows: 01: Sine or A channel 02: Cosine or B channel                                                              | The auxiliary feedback wiring is open, shorted, or missing.                                              | • Replace the motor/encoder.                                                                                                       |
| FLT M05…MTR FDBK BATT LOSS Motor Encoder Battery Loss                                                                |                                                          | The battery voltage on a battery-backed motor encoder is low enough such that absolute position is no longer available.        | Weak battery or poor battery connection.                                                                 | • Replace battery. • Check battery connection.                                                                                     |
|                                                                                                                      | FLT M06…MTR FDBK BATT LOW Motor Encoder Battery Caution  | The battery voltage on a battery-backed motor encoder is below a caution level.                                                | Weak battery or poor battery connection.                                                                 | • Replace battery. • Check battery connection.                                                                                     |
|                                                                                                                      | FLT M07…MTR INCR LOSS Motor Incremental Position Loss    | The periodic check of the incremental encoder position against the absolute                                                    | The motor feedback wiring is open, shorted, or missing.                                                  | • Check motor encoder wiring. • Run Hookup test in the Logix                                                                       |
|                                                                                                                      |                                                          | encoder position or Hall edges (when available) indicates they are out of tolerance. encoder position or Hall edges (when available) indicates they are out of tolerance Designer application. FLT M07…AUX INCR LOSS Aux Incremental Position Loss The auxiliary feedback wiring is openshortedor missing                                                                                                                                | The auxiliary feedback wiring is open, shorted, or missing.                                              | • Check motor encoder wiring. • Run Hookup test in the Logix                                                                       |
|                                                                                                                      | FLT M10…CTRL OVERTEMP FL Control Module Overtemperature  | The control module temperature has exceeded its limit.                                                                         | Cabinet ambient temperature °° p has exceeded 50 °C (122 °F).                                                                                                          | Reduce cabinet ambient temperature.                                                                                                |
| FLT M11…CTRL OVERTEMP UL (Kinetix 6500 drives only)                                                                  |                                                          | Control Module Overtemperature The control module temperature has exceeded a user limit.                                       | Control Module Overtemperature The control module temperature has exceeded a user limit.                 | Reduce cabinet ambient temperature.                                                                                                |
| FLT M12…POWER CYCLE FL Pre-charge Overload                                                                           |                                                          | The converter estimates that the precharge circuit has exceeded its limit due to excessive power cycling.                      | The DC bus power has been cycled too frequently.                                                         | Limit power cycles to two per minute maximum.                                                                                      |
| FLT M13…POWER CYCLE UL (Kinetix 6500 drives only)                                                                    | Pre-charge Overload                                      | The converter estimates that the precharge circuit is approaching its user-defined limit due to excessive power cycling.       | The DC bus power has been cycled too frequently.                                                         | Limit power cycles to two per minute maximum.                                                                                      |
|                                                                                                                      |                                                          | FLT M14…CURR FDBK OFFSET Excessive Current Feedback Offset Current feedback hardware fault detected. Replace the power module. |                                                                                                          |                                                                                                                                    |
|                                                                                                                      | FLT M15…REGEN PWR SUPPLY Regenerative Power Supply Fault | The hardware Regeneration OK input was deactivated while the drive was enabled.                                                |                                                                                                          | Regen unit faulted. Reset faulted regen unit.                                                                                      |
| FLT M18…TORQUE PROVE FAILURE (Kinetix 6500 drives only)                                                              |                                                          | Torque Prove Failure Torque prove test has failed.                                                                             | One or more phases of motor wiring is open or incorrect.                                                 | Check motor power wiring.                                                                                                          |
|                                                                                                                      | FLT M19…DC BUS LIMIT DC Bus Limited Position Error       | During a DC bus limit condition, the position error exceeded a user limit for a programmable period of time.                   | Excessive load drawn from DC bus by application.                                                         | Modify application to reduce loading on DC Bus. Increase converter size to provide additional bus capacity.                        |
| FLT M25…COMMON BUS DC Common Bus Fault                                                                               |                                                          | AC Power was detected by the drive while configured for Common Bus Follower operation.                                         | Improper configuration or connection.                                                                    | Check IAM power configuration and wire accordingly.                                                                                |
|                                                                                                                      |                                                          | FLT M26…RUNTIME ERROR Runtime Drive Error The drive firmware encountered an unrecoverable runtime error.                       | FLT M26…RUNTIME ERROR Runtime Drive Error The drive firmware encountered an unrecoverable runtime error. | Cycle control power. Replace Module                                                                                                |
|                                                                                                                      | FLT M27…BACKPLANE COMM Backplane COM                     | Communication over the backplane detected a problem.                                                                           |                                                                                                          | Electrical Noise. Cycle control power.                                                                                             |
|                                                                                                                      | FLT M27…BACKPLANE COMM Backplane COM                     | Communication over the backplane detected a problem.                                                                           | Poor module connection.                                                                                  | With power off, reseat power module in rail and control module in power module.                                                    |
|                                                                                                                      | FLT M27…BACKPLANE COMM Backplane COM                     | Communication over the backplane detected a problem.                                                                           |                                                                                                          | Faulty module. Replace module.                                                                                                     |

Table 90 - FLT Mxx Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                                                                                                                                                |                                                              |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
|                                                                                                                      | FLT M28…SAFETY COMM Internal Safety Communication Communication with the safety hardware within the drive malfunctioned.                                                       | Cycle control power. Replace module.                         |
| FLT M64…SENSOR ASSIGNMENT No Quick View message                                                                      | • The Home, Registration1, or Registration2 digital input function has been requested but is not assigned to an input. • Multiple inputs have been assigned the same function. | Assign proper function to the four available digital inputs. |
|                                                                                                                      | FLT M68…IPIM IPIM Module Fault A fault has occurred in one or more IPIM modules on the power rail.                                                                             | Refer to the troubleshooting chapter in the Kinetix 6000M Integrated Drive Motor System User Manual, publication 2094-UM003 .                                                              |

## Table 91 - INIT FLT Fault Codes

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                      |                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| INIT FLT S03…NVMEM CHKSUM                                                                                            | User Non-volatile Memory Checksum                            | Data in the user nonvolatile memory has a checksum error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Non-volatile memory is corrupt due to control board software error.                                                  | • Cycle power or reset the drive. • Contact your Rockwell Automation sales representative and return module for repair. |
| INIT FLT M01…ENCODER DATA                                                                                            | Smart Encoder Data Corruption Fault                          | The motor data stored in a smart encoder has a checksum error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Faulty intelligent encoder.                                                                                          | • Cycle power or reset the drive. • Replace motor if faulting continues.                                                |
| INIT FLT M02…MTR DATA RANGE nn Motor Data Range Error                                                                |                                                              | Data within a motor data blob is out of range. The nn subcode is defined as follows: 01: Memory map revision of the blob is not supported by the firmware. 02: Rated current is out of range. 03: Peak current is out of range. 04: Rated power is out of range. 05: Overload limit is out of range. 06: Thermal capacitance is out of range. 07: Thermal resistance is out of range. 08: Motor resistance is out of range. 09: Motor inductance is out of range. 10: Inertia is out of range. 11: Rated speed is out of range. 12: Max speed is out of range. 13: Rated torque is out of range. 14: Torque constant is out of range. 15: Back EMF is out of range. 16: Pole pitch is out of range. If there is error in the blob that comes from the controller, then 50 is added to the | Faulty intelligent encoder or incorrect motor file.                                                                  | • Cycle power or reset the drive. • Check validity of the motion database. • Replace motor if faulting continues.       |
| INIT FLT M03…MTR ENC STARTUP                                                                                         | Motor Feedback Communication Startup                         | Communication with a smart encoder could not be established on the motor feedback port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Incorrect motor selected or connected.                                                                               | Check motor selection.                                                                                                  |
| INIT FLT M03…MTR ENC STARTUP                                                                                         | Motor Feedback Communication Startup                         | Communication with a smart encoder could not be established on the motor feedback port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                      | Faulty wiring. Check motor encoder wiring.                                                                              |
| INIT FLT M03…AUX ENC STARTUP                                                                                         | Auxiliary Feedback Communication Startup                     | Communication with a smart encoder could not be established on the auxiliary feedback port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Incorrect motor selected or connected.                                                                               | Check motor selection.                                                                                                  |
| INIT FLT M03…AUX ENC STARTUP                                                                                         | Auxiliary Feedback Communication Startup                     | Communication with a smart encoder could not be established on the auxiliary feedback port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                      | Faulty wiring. Check motor encoder wiring.                                                                              |
| INIT FLT M04…MTR ABS SPEED                                                                                           | Motor Absolute Encoder Overspeed Fault                       | Excessive speed was detected in the motor battery-backed encoder while power was off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | High motor speed while power was off.                                                                                | Clear faults and rehome.                                                                                                |
| INIT FLT M05…MTR ABS TRAVEL                                                                                          | Motor Absolute Encoder Power-off Travel                      | The power-off travel range of the motor battery-backed encoder has been exceeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Large travel distance while power was off.                                                                           | Clear faults and rehome.                                                                                                |
|                                                                                                                      | INIT FLT M06…MTR ABS STARTUP Motor Absolute Startup Speed    | The motor absolute encoder was not able to accurately determine the position after powerup due to motor speed greater than 100 rpm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Mechanical movement of machine causing excessive rotation of motor during powerup.                                   | Allow machine motion to stop before powerup.                                                                            |
| INIT FLT M07…COMMUTATION OFFSET (Kinetix 6500 drive only)                                                            | Uninitialized Commutation Offset                             | The commutation offset stored in a third party motor has not been initialized.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Third party motors do not contain Rockwell Automation® motor data.                                                   | Run Commutation Test from the Logix Designer application.                                                               |
|                                                                                                                      |                                                              | INIT FLT M12…INVALID KCL REV Invalid KCL revision The FPGA image is incompatible with hardware operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | INIT FLT M12…INVALID KCL REV Invalid KCL revision The FPGA image is incompatible with hardware operation.            | • Flash control module with correct firmware. • Replace module.                                                         |
|                                                                                                                      |                                                              | INIT FLT M13…INVALID BSP REV Invalid BSP revision The board support package is incompatible with hardware operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | INIT FLT M13…INVALID BSP REV Invalid BSP revision The board support package is incompatible with hardware operation. | • Flash control module with correct firmware. • Replace module.                                                         |
| INIT FLT M14…SAFETY FIRMWARE Invalid Safety Firmware                                                                 |                                                              | The loaded Safety firmware is not a valid revision for the rev of drive firmware.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The loaded Safety firmware is not a valid revision for the rev of drive firmware.                                    | Flash control module with correct revision of safety firmware.                                                          |
|                                                                                                                      | INIT FLT M19…VOLTAGE MISMATCH Voltage Mismatch on Power Rail | The IAM detected that both 230V and 460V modules have been installed on the same power rail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The IAM detected that both 230V and 460V modules have been installed on the same power rail.                         | Replace the mismatched AM module with one that matches the IAM module.                                                  |
| INIT FLT M20…UNKNOWN MODULE Unknown Axis on Backplane                                                                |                                                              | Unknown module is detected on the modular backplane.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Faulty Module.                                                                                                       | • Recycle control power. • Replace module.                                                                              |

## Table 91 - INIT FLT Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                               |                                                                                                                                                                                                                                                                                      |                                                                                                                                                                        |                                                                                           |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| INIT FLT M21…FACTORY CFG Factory Configuration                                                                       |                               | Factory Configuration Data is missing or invalid.                                                                                                                                                                                                                                    | Defective memory in module. Replace defective module.                                                                                                                  |                                                                                           |
|                                                                                                                      |                               | INIT FLT M22…ILLEGAL ADDRESS Illegal Node Switch Setting AM Node Address is out of range (>254).                                                                                                                                                                                     | IAM node switch set such that an AM node address is greater than 254.                                                                                                  | Select IAM node address that permits all AM node addresses to be less than 254.           |
|                                                                                                                      |                               | INIT FLT M23…SERIES MISMATCH Series Mismatch on Power Rail Sercos and EtherNet/IP control modules exist on the same power rail. Replace the mismatched control module.                                                                                                               | INIT FLT M23…SERIES MISMATCH Series Mismatch on Power Rail Sercos and EtherNet/IP control modules exist on the same power rail. Replace the mismatched control module. |                                                                                           |
|                                                                                                                      |                               | INIT FLT M24…OPEN SLOT Open Power Rail Slot IAM detects an open slot on the power rail.                                                                                                                                                                                              | Missing module or bent pins on module.                                                                                                                                 | • Check control pin on back of module. • Install slot filler module in open slot.         |
| INIT FLT M32…MTR KEYING nn (Kinetix 6200 drives only)                                                                | Motor Keying Fault            | The attached motor model does not match the model in the axis configuration. The nn subcode is defined as follows: 01: Encoder communication expected but not operational. 02: Feedback type does not match. 03: Motor ID does not match. 04: Single-turn resolution does not match. | Incorrect motor selected from motor database.                                                                                                                          | Verify motor selection in Axis Properties configuration.                                  |
| INIT FLT M33…ENABLE UNASSIGNED (Kinetix 6200 drives only)                                                            | Enable Input Not Assigned     | The enable function has been requested for use but has not been assigned to a digital input.                                                                                                                                                                                         | The enable function has been requested for use but has not been assigned to a digital input.                                                                           | Assign an available digital input as Enable.                                              |
| INIT FLT M34…OTRAVEL UNASSIGNED (Kinetix 6200 drives only)                                                           | Overtravel Input Not Assigned | The positive or negative overtravel function has been requested for use but has not been assigned to a digital input.                                                                                                                                                                | The positive or negative overtravel function has been requested for use but has not been assigned to a digital input.                                                  | Assign an available digital input for the desired overtravel function.                    |
| INIT FLT M35... NAND FLASH nn Storage failure                                                                        |                               | The nn subcode is defined as follows: 01: Main application storage failed. 02: Log file storage failed. 03: Web file storage failed.                                                                                                                                                 | Faulty memory component.                                                                                                                                               | • Recycle control power or reset the drive. • Replace control module if problem persists. |

## Table 92 - NODE FLT Fault Codes

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                             |                                                                                                                            |                                                                                                                            |                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NODE FLT 01…LATE CTRL UPDATE (Kinetix 6500 drives only)                                                              | Control Update Fault        | Several consecutive updates from the controller have been lost.                                                            | Excessive network traffic.                                                                                                 | • Remove unnecessary network devices from the motion network. • Change the network topology so that fewer devices share common paths. • Use faster/higher performance network equipment. |
| NODE FLT 01…LATE CTRL UPDATE (Kinetix 6500 drives only)                                                              | Control Update Fault        | Several consecutive updates from the controller have been lost.                                                            | Noisy environment.                                                                                                         | • Segregate signal wiring from power wiring. • Use shielded cables. • Add snubbers to power devices.                                                                                     |
|                                                                                                                      |                             | NODE FLT 02…PROC WATCHDOG Processor Watchdog Fault The watchdog circuit monitoring processor operation detected a problem. | NODE FLT 02…PROC WATCHDOG Processor Watchdog Fault The watchdog circuit monitoring processor operation detected a problem. | • Recycle control power or reset the drive. • Replace control module if problem persists.                                                                                                |
| NODE FLT 03…HARDWARE nn Hardware Fault                                                                               |                             | The drive has an internal hardware problem. The nn subcode is defined as follows:                                          | The drive has an internal hardware problem. The nn subcode is defined as follows:                                          | • Recycle control power or reset the drive.                                                                                                                                              |
| NODE FLT 03…HARDWARE nn Hardware Fault                                                                               |                             | 01: Invalid slot ID.                                                                                                       | Faulty power rail or power module. 02: Cannot read slot ID.                                                                | • Replace power module or power rail if problem persists                                                                                                                                 |
| NODE FLT 03…HARDWARE nn Hardware Fault                                                                               |                             | 03: Nonvolatile write to memory failed.                                                                                    | Faulty memory component.                                                                                                   | • Recycle control power or reset the drive. • Replace control module if problem                                                                                                          |
| NODE FLT 03…HARDWARE nn Hardware Fault                                                                               |                             | 04: Nonvolatile memory read failed.                                                                                        | Faulty memory component.                                                                                                   | persists.                                                                                                                                                                                |
| NODE FLT 04…DATA FORMAT ERROR (Kinetix 6200 drives only)                                                             | Data Format Error           | A data format error was discovered in the controller-to-drive message.                                                     | Faulty memory component.                                                                                                   | • Recycle control power or reset the drive. • Replace control module if problem persists.                                                                                                |
| NODE FLT 06…LOST CTRL CONN (Kinetix 6500 drives only)                                                                | Lost Controller Connection  | communication with the controller has been lost                                                                            | • Faulty Ethernet cable. • Ethernet cable disconnected.                                                                    | Check Ethernet connection.                                                                                                                                                               |
| NODE FLT 06…LOST CTRL CONN (Kinetix 6500 drives only)                                                                | Lost Controller Connection  | communication with the controller has been lost                                                                            |                                                                                                                            | Controller lost power. Check controller operation.                                                                                                                                       |
| NODE FLT 08…LOGIC WATCHDOG (Kinetix 6500 drives only)                                                                | Custom Logic Update Timeout | The watchdog circuit monitoring custom logic operation detected a problem.                                                 | Faulty control module.                                                                                                     | • Recycle control power or reset the drive. • Replace control module if problem persists.                                                                                                |
| NODE FLT 09…IP ADDRESS (Kinetix 6500 drives only)                                                                    | Duplicate IP Address        | This drive and another EtherNet device on the same subnet have identical IP addresses.                                     | Incorrect node switch setting.                                                                                             | Select a node address not already in use on the network.                                                                                                                                 |
| NODE FLT 128…DRAM TEST DRAM Test Fault                                                                               |                             | A power-up test of the DRAM indicated a memory problem.                                                                    | Faulty memory component.                                                                                                   | • Recycle control power or reset the drive. • Replace Control module if problem persists.                                                                                                |

## Table 92 - NODE FLT Fault Codes (continued)

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                                                                                                |                                                                                                     |                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
|                                                                                                                      | NODE FLT 129…FPGA CONFIG FPGA Configuration Fault The FPGA could not be configured properly. Faulty component. Replace module. |                                                                                                     |                                                                                                        |
| NODE FLT 133…SERCOS ADDRESS (Kinetix 6200 drives only)                                                               | Duplicate Sercos Node Address This axis and one or more other axes have identical Sercos addresses.                            | Duplicate Sercos Node Address This axis and one or more other axes have identical Sercos addresses. | Check Node Switch configuration of all axes on the Sercos ring and adjust for no overlap of addresses. |
| NODE FLT 139…SERCOS RING (Kinetix 6200 drives only)                                                                  | Sercos Ring Fault  The Sercos ring is not active after being active and operational.                                           | Loose or damaged Sercos cable.                                                                      | Check that fiber-optic cable is present and connected properly.                                        |

## Table 93 - NODE ALARM Fault Codes

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                                                                  |                                                                                                               |                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NODE ALARM 01…CTRL UPDATE Control Connection Update Alarm                                                            | The Control Update Alarm bit is used to indicate that updates from the controller have been late | Excessive network traffic.                                                                                    | • Remove unnecessary network devices from the motion network. • Change the network topology so that fewer devices share common paths. • Use faster/higher performance network equipment. |
| NODE ALARM 01…CTRL UPDATE Control Connection Update Alarm                                                            | The Control Update Alarm bit is used to indicate that updates from the controller have been late | Noisy environment.                                                                                            | • Segregate signal wiring from power wiring. • Use shielded cables. • Add snubbers to power devices.                                                                                     |
| NODE ALARM 05…CLOCK SYNC Clock Jitter Alarm                                                                          | Sync Variance has exceeded the Sync Threshold while the device is running in Sync mode.          | • Switched to grandmaster clock of significantly different frequency. • Lost connection to grandmaster clock. | • Drive auto-corrects upon time synchronization. • Restore network connections.                                                                                                          |
| NODE ALARM 128…NODE SWITCH No Quick View message                                                                     | The node address switches have been altered because they were first read after powerup.          | Node Switches adjusted after powerup.                                                                         | Return node switches to power-up setting.                                                                                                                                                |

## Table 94 - INHIBIT Fault Codes

| Four-character Display Message Logix Designer Fault Message Problem or Symptom Potential Cause Possible Resolution   |                                                                  |                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                      | INHIBIT S01…ENABLE INPUT Axis Enable Input Fault - Start Inhibit | When Enable Input Checking is enabled, the drive displays Axis Enable Input start inhibit when it detects the enable input is inactive and while the axis is in Starting/Running/Testing/Hold sub-state of Stopped state. | • Confirm that the digital input assigned to the Enable is active • Check module enable input wiring • Check digital input assignments                                                                                                                                        |
|                                                                                                                      |                                                                  | INHIBIT S02…MOTOR NOT CONFIGURED Motor Not Configured The motor has not been properly configured for use.                                                                                                                 | Verify motor configuration in the Logix Designer application.                                                                                                                                                                                                                 |
| INHIBIT S03…FEEDBACK NOT CONFIGURED                                                                                  |                                                                  | Feedback Not Configured The feedback has not been properly configured for use.                                                                                                                                            | Verify feedback configuration in the Logix Designer application.                                                                                                                                                                                                              |
| INHIBIT S04…COMMUTATION NOT CONFIGURED                                                                               | Commutation Not Configured - Standard Start Inhibit              | • Associated permanent magnet motor commutation has not been configured for use. • After commutation test, the offset value stored on the motor encoder differs from value sent from the controller by 15° or more.       | 1. Verify that the proper motor feedback commutation alignment has been selected. To run the commutation test and to measure the commutation offset it should be set as Controller Offset. 2. Download project or power-cycle drive after accepting commutation test results. |
|                                                                                                                      |                                                                  | INHIBIT M05…SAFE TORQUE OFF Start Inhibit – Safe Torque Off The safety function has disabled the power structure.                                                                                                         | • Check safety input wiring • Check state of safety devices                                                                                                                                                                                                                   |
| INHIBIT M07…SAFETY NOT CONFIGURED                                                                                    | Start Inhibit – Safety Not Configured Inhibit                    | Drive firmware was uploaded.                                                                                                                                                                                              | Reapply safety configuration signature by using Apply File from the Safety Main web page.                                                                                                                                                                                     |

## Table 95 - ALARM Fault Codes

| Four-character Display Message                                                                            | Logix Designer Fault Message                                  | Problem or Symptom Potential Cause Possible Resolution                                                    |                                                  |                                                                         |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------------------------|
| ALARM S52…POS SW OTRAVEL (Kinetix 6200 drives only)  ALARM S53…NEG SW OTRAVEL  (Kinetix 6200 drives only) | Software Overtravel - Positive Software Overtravel - Negative | Axis position exceeded maximum software setting.                                                          | Axis position exceeded maximum software setting. | • Verify motion profile. • Verify overtravel settings are  appropriate. |
| ALARM M13…POWER CYCLE UL (Kinetix 6200 drives only)                                                       | Does not apply  (1)                                           | The converter estimates that the precharge circuit has exceeded its limit due to excessive power cycling. | The DC bus power has been cycled too frequently. | Limit power cycles to two per minute maximum.                           |

## Control Module Status Indicators

Table 96 - Drive Status Indicator (Sercos control modules)

| Condition Drive Status Possible Resolution                                      |
|---------------------------------------------------------------------------------|
| Off No power Apply power.                                                       |
| Alternating green/red Self-test (power-up diagnostics) Wait for steady green.   |
| Flashing green  (1)  Standby (device not configured) Wait for steady green.     |
| Steady green Normal operation, no faults –                                      |
| Flashing red Minor fault (recoverable) Refer to four-character fault message.   |
| Steady red Major fault (non-recoverable) Refer to four-character fault message. |

Table 97 - Comm Status Indicator (Sercos control modules)

|                     |                                                           |                                                                                          | Condition Drive Status Potential Cause Possible Resolution                        |
|---------------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
|                     |                                                           |                                                                                          | Loose fiber-optic connection. Verify proper fiber-optic cable connections.        |
| Off                 | No communication (1)                                      | Broken fiber-optic cable.                                                                | Replace fiber-optic cable.                                                        |
|                     |                                                           | Receive fiber-optic cable connected to Sercos transmit connector and vice versa.         | Check proper Sercos fiber-optic cable connections.                                |
| Flashing green  (2) | Establish communication                                   | System is still in the process of establishing Sercos communication.                     | Wait for steady green indicator.                                                  |
|                     |                                                           | Node address setting on the drive module does not match Sercos controller configuration. | Verify proper node switch setting.                                                |
|                     | Steady green Communication ready No faults or failures. – |                                                                                          |                                                                                   |
|                     |                                                           | Steady red No communication Duplicate node address                                       | Verify proper node addressing. Refer to Configure the Drive Modules on page 161 . |

Table 98 - Bus Status Indicator

|                | Condition Bus Status Condition                        |                                                                                                                                                                                                             |
|----------------|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off            | No power or DC bus is not present.                    | • Normal when bus power is not applied. • Fault exists, refer to Fault Codes troubleshooting on page 189 . • Follower IAM power module is not configured as CommonBus Follow in Logix Designer application. |
| Flashing green | Bus power is present, axis disabled. No major faults. | Normal when: • 24V is not applied to Hardware Enable Input. • MSO instruction is not commanded in the Logix Designer application.                                                                           |
| Steady green   | Bus power is present, axis enabled. No major faults.  | Normal when: • 24V is applied to Hardware Enable Input. • MSO instruction is commanded in the Logix Designer application.                                                                                   |

Table 102 - General Shunt Module Troubleshooting

|        | Module Status Under These Conditions                                                                                                                                                                                                                           |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shunt  | Fault is latched. Until fault condition is corrected and cleared.                                                                                                                                                                                              |
| Shunt  | Fault is cleared. • Using MASR, MAFR, MGSR instructions or the HIM (red stop button). • Only after the DC bus is discharged (bus status indicator is flashing). • Drive must be configured with 2094-BSP2 shunt module or Bulletin 1394 external shunt module. |
| IAM/AM | Disabled (for DC bus regulation). • When the 2094-BSP2 shunt module is used on a 230V system. • When either 230V or 460V system is configured with a Bulletin 1394 external shunt module. • When configured in Common-bus Follower mode.                       |
| IAM/AM | Enabled to discharge the DC bus. Drive (IAM or leader IAM module) three-phase power is removed.                                                                                                                                                                |
| IAM/AM | Disabled from discharging the DC bus. When configured in Common-bus Follower mode.                                                                                                                                                                             |

## IMPORTANT

Under some fault conditions, two reset commands can be required to clear drive and shunt module faults.

Table 99 - Safety Lock Status Indicator

| Condition (1) Status                                        |
|-------------------------------------------------------------|
| Off No power or safety circuitry not configured.            |
| Flashing amber Safety circuitry configured, but not locked. |
| Steady amber Safety circuitry locked.                       |

## Table 100 - Port 1 and Port 2 Ethernet Communication Status Indicators

| Condition Status                                               |
|----------------------------------------------------------------|
| Off No link partner present.                                   |
| Flashing green Link partner present, communication occurring.  |
| Steady green Link partner present, no communication occurring. |

Table 101 - Module and Network Status Indicators (EtherNet/IP control modules)

| Condition Status                                                               |
|--------------------------------------------------------------------------------|
| Off No power or no IP address defined.                                         |
| Alternating green/red Self-test mode (powerup diagnostics).                    |
| Flashing green Standby (device not configured, or connection not established.  |
| Steady green Normal operation. Device has at least one established connection. |
| Flashing red Recoverable minor fault or connection timeout.                    |
| Steady red Non-recoverable major fault or duplicate IP address.                |

## Shunt Module Status Indicators

Each of the shunt module status indicators provide specific troubleshooting information.

## Table 103 - Bus Status Indicator

|                                                                                                       | Bus Status Indicator Status Potential Cause Possible Resolution                                       |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Flashing Normal condition when control power is applied and bus voltage is less than 60V DC. –        | Flashing Normal condition when control power is applied and bus voltage is less than 60V DC. –        |
| Steady Green Normal condition when control power is applied and bus voltage is greater than 60V DC. – | Steady Green Normal condition when control power is applied and bus voltage is greater than 60V DC. – |
|                                                                                                       | Off Control power is not present. Internal power supply failure. Replace shunt module.                |

## Table 104 - Temperature Fault Status Indicator

| Over-Temp Fault Indicator   |                                                                                |                                                | Status Potential Cause Possible Resolution                                                        |
|-----------------------------|--------------------------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------|
|                             | Off Normal condition. –                                                        | Off Normal condition. –                        |                                                                                                   |
| Steady Red                  | Shunt module internal temperature exceeds operating temperature specification. | Shunt module fan failed. Replace shunt module. |                                                                                                   |
| Steady Red                  | Shunt module internal temperature exceeds operating temperature specification. | Shunt module temperature exceeds rating.       | • Wait for shunt module to cool. • Reset faults. • Verify IAM module bus regulator configuration. |
| Steady Red                  | External over temperature condition.                                           | External temperature switch is open.           | • Wait for shunt module to cool. • Reset faults. • Verify IAM module bus regulator configuration. |
| Steady Red                  | External over temperature condition.                                           | TS jumper is not present. Install jumper.      |                                                                                                   |

## Table 105 - Shunt Fault Status Indicator

|                                              |                                                                                                    | Shunt Fault Indicator Status Potential Cause Possible Resolution                                 |
|----------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Off Normal condition –                       | Off Normal condition –                                                                             |                                                                                                  |
| Shorted internal or external shunt resistor. | Mis-wired shunt jumper or other short on RC connector.  Mis-wired (shorted) external shunt wiring. | Steady Red  • Correct mis-wire (shorted) condition. • If problem persists, replace shunt module. |

## Table 106 - All Shunt Module Status Indicators

| Shunt Module Status Indicator                |                                                   |                                | Status Potential Cause Possible Resolution                  |
|----------------------------------------------|---------------------------------------------------|--------------------------------|-------------------------------------------------------------|
| • Bus Status • Over-Temp Fault • Shunt Fault | All three status indicators flash simultaneously. | Shunt module hardware failure. | • Cycle power. • If problem persists, replace shunt module. |

## General System Anomalies

## Table 107 - General System Anomalies

|                             |                                                                                                                                                                     | Condition Potential Cause Possible Resolution                                                                                      |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Axis or system is unstable. | The position feedback device is incorrect or open. Check wiring.                                                                                                    |                                                                                                                                    |
| Axis or system is unstable. | Unintentionally in Torque mode.                                                                                                                                     | Check to see what primary operation mode was programmed.                                                                           |
| Axis or system is unstable. |                                                                                                                                                                     | Motor tuning limits are set too high. Run Tune in the Logix Designer application.                                                  |
| Axis or system is unstable. | Position loop gain or position controller accel/decel rate is improperly set. Run Tune in the Logix Designer application.                                           |                                                                                                                                    |
| Axis or system is unstable. | Improper grounding or shielding techniques are causing noise to be transmitted into the position feedback or velocity command lines, causing erratic axis movement. | Check wiring and ground.                                                                                                           |
| Axis or system is unstable. | Motor Select limit is incorrectly set (servo motor is not matched to axis module).                                                                                  | • Check setups. • Run Tune in the Logix Designer application.                                                                      |
| Axis or system is unstable. | Mechanical resonance.                                                                                                                                               | Notch filter or output filter may be required (refer to Axis Properties dialog box, Output tab in the Logix Designer application). |

These anomalies do not always result in a fault code, but may require troubleshooting to improve performance.

Table 107 - General System Anomalies (continued)

|                                                                |                                                                                                                                                                                                                                                              | Condition Potential Cause Possible Resolution                                                                                               |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                |                                                                                                                                                                                                                                                              | Torque Limit limits are set too low. Verify that current limits are set properly.                                                           |
|                                                                | Incorrect motor selected in configuration.                                                                                                                                                                                                                   | Select the correct motor and run Tune in the Logix Designer application again.                                                              |
| You cannot obtain the motor acceleration/deceleration that you | The system inertia is excessive.                                                                                                                                                                                                                             | • Check motor size versus application need. • Review servo system sizing.                                                                   |
| want.                                                          | The system friction torque is excessive.                                                                                                                                                                                                                     | Check motor size versus application need.                                                                                                   |
|                                                                | Available current is insufficient to supply the correct accel/decel rate.                                                                                                                                                                                    | • Check motor size versus application need. • Review servo system sizing.                                                                   |
|                                                                |                                                                                                                                                                                                                                                              | Acceleration limit is incorrect. Verify limit settings and correct them, as necessary.                                                      |
|                                                                |                                                                                                                                                                                                                                                              | Velocity Limit limits are incorrect. Verify limit settings and correct them, as necessary.                                                  |
|                                                                | The axis cannot be enabled for 1.5 seconds after disabling.                                                                                                                                                                                                  | Disable the axis, wait for 1.5 seconds, and enable the axis.                                                                                |
|                                                                | Enable signal has not been applied or the enable wiring is incorrect.                                                                                                                                                                                        | • Check the controller. • Check the wiring.                                                                                                 |
|                                                                | The motor wiring is open. Check the wiring.                                                                                                                                                                                                                  |                                                                                                                                             |
| Motor does not respond to a velocity command.                  | The motor thermal switch has tripped.                                                                                                                                                                                                                        | • Check for a fault. • Check the wiring.                                                                                                    |
|                                                                | The motor has malfunctioned.                                                                                                                                                                                                                                 | Repair or replace the motor.                                                                                                                |
|                                                                | The coupling between motor and machine has broken (for example, the motor moves, but the load/machine does not).                                                                                                                                             | Check and correct the mechanics.                                                                                                            |
|                                                                | Primary operation mode is set incorrectly. Check and properly set the limit.                                                                                                                                                                                 |                                                                                                                                             |
|                                                                | Velocity or current limits are set incorrectly. Check and properly set the limits.                                                                                                                                                                           |                                                                                                                                             |
|                                                                | Recommended grounding per installation instructions have not been followed.                                                                                                                                                                                  | • Verify grounding. • Route wire away from noise sources. • Refer to System Design for Control of Electrical Noise, publication GMC-RM001 . |
| Presence of noise on command or motor feedback signal wires.   | Line frequency may be present.                                                                                                                                                                                                                               | • Verify grounding. • Route wire away from noise sources.                                                                                   |
|                                                                | Variable frequency may be velocity feedback ripple or a disturbance caused by gear teeth or ballscrew balls, and so forth. The frequency may be a multiple of the motor power transmission components or ballscrew speeds resulting in velocity disturbance. | • Decouple the motor for verification. • Check and improve mechanical performance, for example, the gearbox or ballscrew mechanism.         |
|                                                                | The motor connections are loose or open. Check motor wiring and connections.                                                                                                                                                                                 |                                                                                                                                             |
|                                                                | Foreign matter is lodged in the motor. Remove foreign matter.                                                                                                                                                                                                |                                                                                                                                             |
|                                                                |                                                                                                                                                                                                                                                              | The motor load is excessive. Verify the servo system sizing.                                                                                |
| No rotation                                                    |                                                                                                                                                                                                                                                              | The bearings are worn. Return the motor for repair.                                                                                         |
|                                                                | The motor brake is engaged (if supplied).                                                                                                                                                                                                                    | • Check brake wiring and function. • Return the motor for repair.                                                                           |
|                                                                | The motor is not connected to the load. Check coupling.                                                                                                                                                                                                      |                                                                                                                                             |
| Motor overheating                                              | The duty cycle is excessive.                                                                                                                                                                                                                                 | Change the command profile to reduce accel/decel or increase time.                                                                          |
|                                                                | The rotor is partially demagnetized causing excessive motor current. Return the motor for repair.                                                                                                                                                            |                                                                                                                                             |
|                                                                |                                                                                                                                                                                                                                                              | Motor tuning limits are set too high. Run Tune in the Logix Designer application.                                                           |
| Abnormal noise                                                 |                                                                                                                                                                                                                                                              | Loose parts are present in the motor. • Return motor for repair. • Replace motor.                                                           |
|                                                                | Through bolts or coupling is loose. Tighten bolts.                                                                                                                                                                                                           |                                                                                                                                             |
|                                                                | The bearings are worn. Return motor for repair.                                                                                                                                                                                                              |                                                                                                                                             |
|                                                                | Mechanical resonance.                                                                                                                                                                                                                                        | Notch filter may be required (refer to Axis Properties dialog box, Output tab in Logix Designer application).                               |
| Erratic operation - Motor                                      |                                                                                                                                                                                                                                                              |                                                                                                                                             |
| locks into position, runs without control or with              | Motor power phases U and V, U and W, or V and W reversed. Check and correct motor power wiring.                                                                                                                                                              |                                                                                                                                             |
| reduced torque.                                                | Sine, Cosine or Rotor leads are reversed in the feedback cable connector. Check and correct motor feedback wiring.                                                                                                                                           |                                                                                                                                             |

## Logix 5000 Controller and Drive Behavior

By using the Logix Designer application, you can configure how the Bulletin 2094 control modules respond when a drive fault/exception occurs. The set of drive actions that apply depends on the whether you are using an integrated motion on EtherNet/IP (Kinetix 6500) servo drive or Sercos (Kinetix 6200) servo drive.

<!-- image -->

The INIT FLT xxx faults are always generated after powerup, but before the drive is enabled, so the stopping behavior does not apply.

ALARM xxx and NODE ALARM xxx faults do not apply because they do not trigger stopping behavior.

## Kinetix 6500 Drive Exception Behavior

For Kinetix 6500 (integrated motion on EtherNet/IP) drives, you can configure exception behavior in the Logix Designer application from the Axis Properties dialog box, Actions category.

Table 108 - Kinetix 6500 Drive Exception Action Definitions

| Exception Action Definition   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ignore                        | The controller completely ignores the exception condition. For some exceptions that are fundamental to the operation of the planner, Ignore will not be an available option.                                                                                                                                                                                                                                       |
| Alarm                         | The controller sets the associated bit in the Motion Alarm Status word but does not otherwise affect axis behavior. Like Ignore, if the exception is so fundamental to the drive, Alarm will not be an available option. When an exception action is set to Alarm, the Alarm will go away by itself when the exceptional condition has cleared.                                                                    |
| Fault Status Only             | Like Alarm, Fault Status Only instructs the controller to set the associated bit in the Motion Fault Status word, but does not otherwise affect axis behavior. However, unlike Alarm an explicit Fault Reset is required to clear the fault once the exceptional condition has cleared. Like Ignore and Alarm, if the exception is so fundamental to the drive, Fault Status Only will not be an available option. |
| Stop Planner                  | The controller sets the associated bit in the Motion Fault Status word and instructs the Motion Planner to perform a controlled stop of all planned motion at the configured maximum deceleration rate. An explicit Fault Reset is required to clear the fault once the exceptional condition has cleared. If the exception is so fundamental to the drive, Stop Planner will not be an available option.          |
| Stop Drive                    | When the exception occurs, the associated bit in the Fault Status word is set and the axis will come to a stop by using the stopping action defined by the drive for the particular exception that occurred. There is no controller based configuration to specify what the stopping action is, the stopping action is device dependant.                                                                           |
| Shutdown                      | When the exception occurs, the drive brings the motor to a stop by using the stopping action defined by the drive (as in Stop Drive) and the power module is disabled. Optionally, if the Shutdown Action attribute is configured for Drop DC Bus, the contactor will open. An explicit Shutdown Reset is required to restore the drive to operation.                                                              |

Only selected drive exceptions are configurable. In the Drive Exception/Fault Behavior tables beginning on page 204, the controlling attribute is given for programmable fault actions.

Figure 85 - Logix Designer Axis Properties - Exceptions Category

<!-- image -->

This dialog box applies to Kinetix 6500 (EtherNet/IP network) servo drives.

## Kinetix 6200 Drive Fault Behavior

For Kinetix 6200 (Sercos) drives, you can configure fault behavior in the Logix Designer application from the Axis Properties dialog box, Fault Actions tab.

Table 109 - Kinetix 6200 Drive Fault Action Definitions

<!-- image -->

| Drive Fault Action Definition   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shutdown                        | The drive disables the axis as defined in the Drive Exception/Fault Behavior tables below (Table 110 … Table 113). In addition, the axis in Logix Designer enters the Shutdown state, which disables any axes that are using this axis as a camming or gearing master. In addition, the AxisHomedStatus tag for the faulted axis is cleared. Shutdown is the most severe action to a fault and it is usually reserved for faults that could endanger the machine or operator if power is not removed as quickly as possible. |
|                                 | Disable Drive The drive disables the axis as defined in the Drive Exception/Fault Behavior ,  Table 110 .                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Stop Motion                     | The axis decelerates at the maximum deceleration rate (set in the Logix Designer application>Axis Properties>Dynamics tab). Once the axis has come to a stop, the servo loops remain enabled but no further motion can be generated until the fault is reset. This is the gentlest stopping mechanism in response to a fault. It is usually used for less severe faults.                                                                                                                                                     |
| Status Only                     | The drive continues to operate. Status is provided by the four-character fault status indicator and drive status indicator. The application program must handle any motion faults. In general this setting should only be used in applications where the standard fault actions are not appropriate.                                                                                                                                                                                                                         |

Only selected drive faults are configurable. In the Drive Exception/Fault Behavior tables beginning on page 204, the controlling attribute is given for programmable fault actions. All faults that are not configurable have a fault action of Shutdown.

Table 110 - Drive Behavior, FLT Sxx Fault Codes

| Four-character Display Message                        | Logix Designer Fault Message                          | Description                                                                                                                                                                        | Integrated Motion Exception Behavior        | Sercos Fault Behavior                       |
|-------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|
|                                                       |                                                       | FLT S02…MTR COMMUTATION Illegal Hall State The motor encoder Hall inputs are all high or all low. Coast/Disable Coast/Disable                                                      |                                             |                                             |
| FLT S03…MTR OVERSPEED FL Motor Overspeed              |                                                       | The motor speed has exceeded 125% of the motor maximum speed ratings.                                                                                                              |                                             | Coast/Disable Coast/Disable                 |
| FLT S04…MTR OVERSPEED UL (Kinetix 6500 drives only)   | Motor Overspeed                                       | Motor speed has exceeded 125% of maximum rated speed. The 100% trip point is dictated by the lesser of the user velocity limits or the motor rated base speed.                     | Decel/Hold –                                |                                             |
|                                                       |                                                       | FLT S05…MTR OVERTEMP FL nn Motor Overtemperature The motor thermostat, motor thermistor, or encoder temperature sensor indicates that the motor factory temperature limit has been |                                             | Coast/Disable Coast/Disable                 |
| FLT S06…MTR OVERTEMP UL nn (Kinetix 6500 drives only) |                                                       | exceeded. The nn subcode is defined as follows: 01: Motor Thermostat or Thermistor. 02: Encoder Temperature Sensor. 01: Motor Thermostat or Thermistor. Motor Overtemperature Decel/Hold –                                                                                                                                                                                    |                                             |                                             |
| FLT S07…MTR OVERLOAD FL Motor Thermal Protection      |                                                       | The thermal model for the motor indicates that the temperature has exceeded 110% of its rating.                                                                                    |                                             | Decel/Disable Decel/Disable                 |
| FLT S08…MTR OVERLOAD UL (Kinetix 6500 drives only)    | Motor Thermal Protection                              | The thermal model for the motor indicates that the temperature has exceeded a user programmable limit.                                                                             | Decel/Hold –                                |                                             |
| FLT S10…INV OVERCURRENT IPM Fault                     |                                                       | The IPM fault output indicates that the power transistors were turned off because of overcurrent, overtemperature, or power supply problems.                                       | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay) |
|                                                       |                                                       | FLT S11…INV OVERTEMP FL Inverter Overtemperature The inverter temperature has exceeded its limit.                                                                                  | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay) |
|                                                       | FLT S13…INV OVERLOAD FL Inverter Thermal Protection   | The thermal model for the power transistors indicates that the temperature has exceeded 110% of its rating.                                                                        | Coast/Disable Coast/Disable                 |                                             |
| FLT S14…INV OVERLOAD UL (Kinetix 6500 drives only)    | Inverter Thermal Protection                           | The thermal model for the power transistors indicates that the temperature has exceeded the user-programable limit.                                                                | Decel/Hold –                                |                                             |
|                                                       |                                                       | FLT S16…GROUND CURRENT Ground Fault Excessive ground current was detected in the converter.                                                                                        | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay) |
|                                                       |                                                       | FLT S18…CONV OVERTEMP FL Converter Overtemperature The converter temperature has exceeded its limit.                                                                               | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay) |
|                                                       | FLT S20…CONV OVERLOAD FL Converter Thermal Protection | The thermal model for the converter indicates that the temperature has exceeded its rating.                                                                                        | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay) |
| FLT S21…CONV OVERLOAD UL (Kinetix 6500 drives only)   | Converter Thermal Protection                          | The thermal model for the converter indicates that the temperature has exceeded a user-programmable limit.                                                                         | Decel/Hold –                                |                                             |
| FLT S22…AC POWER LOSS AC Power Loss                   |                                                       | All three AC input phases are detected as absent when an axis is enabled.                                                                                                          |                                             | Coast/Disable Decel/Disable                 |

Figure 86 - Logix Designer Axis Properties - Fault Actions Tab

<!-- image -->

This dialog box applies to Kinetix 6200 (Sercos) servo drives.

## Drive Exception/Fault Behavior

Table 110 - Drive Behavior, FLT Sxx Fault Codes (continued)

| Four-character Display Message                                                                               | Logix Designer Fault Message                        | Description                                                                                                                                                                                                                                                   | Integrated Motion Exception Behavior                                              | Sercos Fault Behavior                                                             |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| FLT S23…AC PHASE LOSS nn AC Phase Loss                                                                       |                                                     | Some, but not all AC input phases are detected as absent. The nn subcode is defined as follows: 01: L1 is missing. 02: L2 is missing. 03: L3 is missing.                                                                                                      | Coast/Disable (open contactor enable relay) (IAM modules) Decel/Hold (AM modules) | Coast/Disable (open contactor enable relay) (IAM modules) Decel/Hold (AM modules) |
| FLT S25…PRECHARGE FAILURE Pre-charge Failure                                                                 |                                                     | The converter precharge circuit detected that the DC bus did not reach an appropriate voltage level after charging for a period of time.                                                                                                                      | Coast/Disable (open contactor enable relay)                                       | Coast/Disable (open contactor enable relay)                                       |
| FLT S29…SHUNT OVERLOAD FL Shunt Thermal Protection                                                           |                                                     | The thermal model for the shunt circuitry indicates that the temperature has exceeded its rating.                                                                                                                                                             | Coast/Disable (open contactor enable relay)                                       | Coast/Disable (open contactor enable relay)                                       |
| FLT S30…SHUNT OVERLOAD UL (Kinetix 6500 drives only)                                                         | Shunt Thermal Protection                            | The thermal model for the shunt circuitry indicates that the temperature has exceeded a user-programmable limit.                                                                                                                                              | Decel/Hold –                                                                      |                                                                                   |
|                                                                                                              |                                                     | FLT S31…SHUNT MODULE Shunt Module Fault The shunt module in a multi-axis system has a fault.                                                                                                                                                                  | Coast/Disable (open contactor enable relay)                                       | Coast/Disable (open contactor enable relay)                                       |
| FLT S33…BUS UNDERVOLT FL Bus Undervoltage                                                                    |                                                     | The DC bus voltage is measured below a factory limit when the DC bus was expected to be charged.                                                                                                                                                              | Decel/Disable (open contactor enable relay)                                       | Decel/Disable (open contactor enable relay)                                       |
| FLT S34…BUS UNDERVOLT UL (Kinetix 6500 drives only)                                                          | Bus Undervoltage                                    | The DC bus voltage is measured below a user limit when the DC bus was expected to be charged.                                                                                                                                                                 | Decel/Hold –                                                                      |                                                                                   |
|                                                                                                              |                                                     | FLT S35…BUS OVERVOLT FL Bus Overvoltage The DC bus voltage is measured above a factory limit.                                                                                                                                                                 | Coast/Disable (open contactor enable relay)                                       | Coast/Disable (open contactor enable relay)                                       |
| FLT S38…FUSE BLOWN                                                                                           | Blown Fuse (Bus Loss)                               | A blown fuse was detected in the power structure.                                                                                                                                                                                                             | Coast/Disable (open contactor enable relay)                                       | Coast/Disable (open contactor enable relay)                                       |
|                                                                                                              | FLT S41…MTR AQB STATE FL Motor Feedback State Error | The number of illegal state transitions of the AQB encoder signals has exceeded a factory limit.                                                                                                                                                              | Coast/Disable Coast/Disable                                                       |                                                                                   |
| FLT S41…AUX AQB STATE FL                                                                                     | Aux Feedback State Error                            | The number of illegal state transitions of the AQB encoder signals has exceeded a factory limit.                                                                                                                                                              | Coast/Disable Coast/Disable                                                       |                                                                                   |
|                                                                                                              | exceeded a factory limit. FLT S42…MTR AQB STATE UL Motor Feedback State Error Decel/Hold Coast/Disable                                                     | The number of illegal state transitions of the AQB encoder signals has exceeded a factory limit.                                                                                                                                                              |                                                                                   |                                                                                   |
| FLT S42…AUX AQB STATE UL                                                                                     | Aux Feedback State Error                            | The number of illegal state transitions of the AQB encoder signals has exceeded a factory limit.                                                                                                                                                              |                                                                                   | Decel/Hold Coast/Disable                                                          |
| FLT S43…MTR FDBK LOSS FL Feedback Loss On sin/cos encoders, the sum of the square of the sin/cos signals has |                                                     | The number of illegal state transitions of the AQB encoder signals has exceeded a factory limit.                                                                                                                                                              |                                                                                   | Coast/Disable Coast/Disable                                                       |
|                                                                                                              |                                                     | been measured below a user limit. On TTL encoders, the absolute value of the differential A/B signals is been measured below a user limit. On TTL encodersthe absolute value of the differential A/B signals is FLT S43…AUX FDBK LOSS FL Feedback Loss Coast/Disable Coast/Disable                                                                                                                                                                                                                                                               |                                                                                   |                                                                                   |
| FLT S44…MTR FDBK LOSS UL (Kinetix 6500 drives only)                                                          |                                                     | below a user limit. IMPORTANT: Motors with non-intelligent SIN/COS encoders or below a user limit. IMPORTANTMotors with nonintelligent SIN/COS encoders or Motor Feedback Loss Decel/Hold –                                                                                                                                                                                                                                                               |                                                                                   |                                                                                   |
| FLT S44…AUX FDBK LOSS UL (Kinetix 6500 drives only)                                                          |                                                     | incremental encoders without Hall effect sensors do not see the feedback loss fault if the motor is running at high speed and if only one line in the feedback cable is opened. feedback loss fault if the motor is running at high speed and if only one Aux Feedback Loss Decel/Hold –                                                                                                                                                                                                                                                               |                                                                                   |                                                                                   |
| FLT S45…MTR FDBK COMM FL Feedback Serial Comms                                                               |                                                     | The number of consecutive missed or corrupted serial data packets                                                                                                                                                                                             | Coast/Disable Coast/Disable                                                       |                                                                                   |
|                                                                                                              |                                                     | from the feedback device has exceeded a factory set limit. from the feedback device has exceeded a factory set limit. FLT S45…AUX FDBK COMM FL Feedback Serial Comms Coast/Disable Coast/Disable                                                                                                                                                                                                                                                               |                                                                                   |                                                                                   |
| FLT S46…MTR FDBK COMM UL (Kinetix 6500 drives only)                                                          | Motor Fdbk Serial Comms                             | The number of consecutive missed or corrupted serial data packets from the feedback device has exceeded a user set limit.                                                                                                                                     | Decel/Hold –                                                                      |                                                                                   |
| FLT S46…AUX FDBK COMM UL (Kinetix 6500 drives only)                                                          | Aux Feedback Serial Comms Decel/Hold –              | The number of consecutive missed or corrupted serial data packets from the feedback device has exceeded a user set limit.                                                                                                                                     |                                                                                   |                                                                                   |
| FLT S47…MTR ENC SELF TEST nn Feedback Self Test                                                              |                                                     | The feedback device has detected an internal error. Sub code (nn) is                                                                                                                                                                                          | Coast/Disable Coast/Disable                                                       |                                                                                   |
| available for factory use. FLT S47…AUX ENC SELF TEST nn Feedback Self Test Coast/Disable Coast/Disable                                                                                                              |                                                     | available for factory use.                                                                                                                                                                                                                                    |                                                                                   |                                                                                   |
|                                                                                                              |                                                     | FLT S50…POS HW OTRAVEL Hardware Overtravel Positive The positive hardware overtravel input is monitored. Decel/Disable Coast/Disable                                                                                                                          |                                                                                   |                                                                                   |
|                                                                                                              |                                                     | FLT S51…NEG HW OTRAVEL Hardware Overtravel Negative The negative hardware overtravel input is monitored. Decel/Disable Coast/Disable                                                                                                                          |                                                                                   |                                                                                   |
| FLT S52…POS SW OTRAVEL (Kinetix 6200 drives only)                                                            |                                                     | Software Overtravel Positive The feedback position is compared to the positive limit. – Coast/Disable                                                                                                                                                         |                                                                                   |                                                                                   |
| FLT S53…NEG SW OTRAVEL (Kinetix 6200 drives only)                                                            |                                                     | Software Overtravel Negative The feedback position is compared to the negative limit. – Coast/Disable                                                                                                                                                         |                                                                                   |                                                                                   |
|                                                                                                              | FLT S54…POSN ERROR Excessive Position Error         | The position error has exceeded a user limit for a programmable period of time.                                                                                                                                                                               |                                                                                   | Coast/Disable Decel/Disable                                                       |
| FLT S55…VEL ERROR nn Excessive Velocity Error                                                                |                                                     | The velocity error has exceeded a limit for a period of time. The nn subcode is defined as follows: 00: Velocity error referenced to the velocity loop feedback. 01: Velocity error referenced to the nonvelocity feedback (in dual-feedback configurations). |                                                                                   | Coast/Disable Decel/Disable                                                       |
| FLT S56…OVERTORQUE (Kinetix 6500 drives only)                                                                |                                                     | Overtorque Limit Motor torque has exceeded a user-programmable setting. Decel/Hold –                                                                                                                                                                          |                                                                                   |                                                                                   |
| FLT S57…UNDERTORQUE (Kinetix 6500 drives only)                                                               |                                                     | Undertorque Limit Motor torque has fallen below a user-programmable setting. Decel/Hold –                                                                                                                                                                     |                                                                                   |                                                                                   |
|                                                                                                              |                                                     | FLT S60…ILLEGAL MODE Illegal Control mode An illegal mode of operation was attempted. Decel/Hold Decel/Hold                                                                                                                                                   |                                                                                   |                                                                                   |
| FLT S61…ENABLE INPUT Drive Enable Input                                                                      |                                                     | The hardware enable input was deactivated while the drive was enabled.                                                                                                                                                                                        |                                                                                   | Decel/Disable Decel/Disable                                                       |
| FLT S62…CONTROLLER (Kinetix 6500 drives only)                                                                |                                                     | Controller Initiated Exception The controller has requested the drive to generate an exception. Coast/Disable –                                                                                                                                               |                                                                                   |                                                                                   |

Table 111 - Drive Behavior, FLT Mxx Fault Codes

| Four-character Display Message                          | Logix Designer Fault Message                            | Description                                                                                                                                                                 | Integrated Motion Exception Behavior        | Sercos Fault Behavior                                                  |
|---------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|------------------------------------------------------------------------|
|                                                         |                                                         | FLT M01…SELF SENSING Self-sensing Startup Fault The self-sensing commutation startup algorithm failed. Coast/Disable Coast/Disable                                          |                                             |                                                                        |
|                                                         |                                                         | FLT M02…MOTOR VOLTAGE Motor Voltage Mismatch Motor voltage is incompatible with drive voltage.                                                                              | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
| FLT M04…MTR FDBK FILTER nn (Kinetix 6500 drives only)   | Motor Feedback Filter                                   | Excessive levels of noise have been detected by the digital feedback filter. The nn field is defined as follows:                                                            | Coast/Disable –                             |                                                                        |
| FLT M04…AUX FDBK FILTER nn (Kinetix 6500 drives only)   |                                                         | 01: Sine or A channel 02: Cosine or B channel 02: Cosine or B channel Aux Feedback Filter Coast/Disable –                                                                                                                                                                             |                                             |                                                                        |
| FLT M05…MTR FDBK BATT LOSS Motor Encoder Battery Loss   |                                                         | The battery voltage on a battery-backed motor encoder is low enough such that absolute position is no longer available.                                                     |                                             | Decel/Hold Decel/Disable                                               |
|                                                         | FLT M06…MTR FDBK BATT LOW Motor Encoder Battery Caution | The battery voltage on a battery-backed motor encoder is below a caution level.                                                                                             |                                             | Decel/Hold Decel/Disable                                               |
| FLT M07…MTR INCR LOSS                                   | Motor Incremental Position Loss                         | The periodic check of the incremental encoder position against the absolute encoder position or Hall edges (when available) indicates they                                  |                                             | Coast/Disable Coast/Disable                                            |
|                                                         |                                                         | are out of tolerance. are out of tolerance. FLT M07…AUX INCR LOSS Aux Incremental Position Loss Coast/Disable Coast/Disable                                                                                                                                                                             |                                             |                                                                        |
| FLT M10…CTRL OVERTEMP FL                                | Control Module Overtemperature                          | The control module temperature has exceeded its limit. Coast/Disable Coast/Disable                                                                                          |                                             |                                                                        |
| FLT M11…CTRL OVERTEMP UL (Kinetix 6500 drives only)     | Control Module Overtemperature                          | The control module temperature has exceeded a user limit. Decel/Hold –                                                                                                      |                                             |                                                                        |
| FLT M12…POWER CYCLE FL Pre-charge Overload              |                                                         | The converter estimates that the precharge circuit has exceeded its limit due to excessive power cycling.                                                                   | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
| FLT M13…POWER CYCLE UL (Kinetix 6500 drives only)       | Pre-charge Overload                                     | The converter estimates that the precharge circuit is approaching its user-defined limit due to excessive power cycling.                                                    | Decel/Hold –                                |                                                                        |
| FLT M14…CURR FDBK OFFSET                                | Excessive Current Feedback Offset                       | The current feedback circuitry requires excessive offset compensation.                                                                                                      | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
| FLT M15…REGEN PWR SUPPLY                                | Regenerative Power Supply Fault                         | The hardware Regeneration OK input was deactivated while the drive was enabled.                                                                                             | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
| FLT M18…TORQUE PROVE FAILURE (Kinetix 6500 drives only) | Torque Prove Failure                                    | Torque prove test has failed. One or more phases of motor wiring is open or incorrect.                                                                                      | Coast/Disable –                             |                                                                        |
|                                                         | FLT M19…DC BUS LIMIT DC Bus Limited Position Error      | During a DC bus limit condition, the position error has exceeded a user limit for a programmable period of time.                                                            |                                             | Decel/Hold Decel/Disable                                               |
|                                                         | FLT M25…COMMON BUS DC Common Bus Fault                  | AC Power was detected by the drive while configured for Common Bus Follower operation.                                                                                      | Coast/Disable (open contactor enable relay) | Coast/Disable                                                          |
|                                                         |                                                         | FLT M26…RUNTIME ERROR Runtime Drive Error The drive firmware encountered an unrecoverable runtime error.                                                                    | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
|                                                         |                                                         | FLT M27…BACKPLANE COMM Backplane COM Communication over the backplane detected a problem.                                                                                   | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
| FLT M28…SAFETY COMM                                     | Internal Safety Communication                           | Communication with the safety hardware within the drive malfunctioned.                                                                                                      | Coast/Disable (open contactor enable relay) | Coast/Disable (open contactor enable relay)                            |
| FLT M64…SENSOR ASSIGNMENT Sensor Assignment             |                                                         | The Home, Registration1, or Registration 2 digital input function has been requested but is not assigned to an input. Multiple inputs have been assigned the same function. |                                             | Coast/Disable Coast/Disable                                            |
|                                                         |                                                         | FLT M68…IPIM IPIM Module Fault A fault has occurred in one or more IPIM modules on the power rail. –                                                                        |                                             | Coast/Disable (open contactor enable relay) Applies to the IAM module. |

Table 112 - Drive Behavior, NODE FLT Fault Codes

| Four-character Display Message  Logix Designer Fault Message                         | Description                                                                                                                                                                                                 | Integrated Motion and Sercos Drive Behavior   |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| NODE FLT 01…LATE CTRL UPDATE (Kinetix 6500 drives only)                              | Control Update Fault Several consecutive updates from the controller have been lost. Decel/Disable                                                                                                          |                                               |
|                                                                                      | NODE FLT 02…PROC WATCHDOG Processor Watchdog Fault The watchdog circuit monitoring processor operation detected a problem. Coast/Disable                                                                    |                                               |
| NODE FLT 03…HARDWARE nn Hardware Fault                                               | The drive has an internal hardware problem. The nn subcode is defined as follows: 01: Invalid slot ID. 02: Cannot read slot ID. 03: Nonvolatile write to memory failed. 04: Nonvolatile memory read failed. | Coast/Disable (open contactor enable relay)   |
| NODE FLT 04…DATA FORMAT ERROR (Kinetix 6200 drives only)                             | Data Format Error A data format error was discovered in the controller-to-drive message. Coast/Disable                                                                                                      |                                               |
| NODE FLT 06…LOST CTRL CONN (Kinetix 6500 drives only)                                | Lost Controller Connection communication with the controller have been lost Decel/Disable                                                                                                                   |                                               |
| NODE FLT 08…LOGIC WATCHDOG (Kinetix 6500 drives only)                                | Custom Logic Update Timeout The watchdog circuit monitoring custom logic operation detected a problem.                                                                                                      | Coast/Disable (open contactor enable relay)   |
| NODE FLT 09…IP ADDRESS (Kinetix 6500 drives only)                                    | Duplicate IP Address This drive and another EtherNet device on the same subnet have identical IP addresses. Coast/Disable                                                                                   |                                               |
|                                                                                      | NODE FLT 128…DRAM TEST DRAM Test Fault A power-up test of the DRAM indicated a memory problem.                                                                                                              | Coast/Disable (open contactor enable relay)   |
|                                                                                      | NODE FLT 129…FPGA CONFIG FPGA Configuration Fault The FPGA could not be configured properly.                                                                                                                | Coast/Disable (open contactor enable relay)   |
| NODE FLT 133…SERCOS ADDRESS (Kinetix 6200 drives only) Duplicate Sercos Node Address | This axis and one or more other axes have identical Sercos addresses. Coast/Disable                                                                                                                         |                                               |
| NODE FLT 139…SERCOS RING (Kinetix 6200 drives only)                                  | Sercos Ring Fault The Sercos ring is not active after being active and operational. Decel/Disable                                                                                                           |                                               |

Table 113 - Drive Behavior, SAFE FLT Fault Codes

| Four-character Display Message  Logix Designer Fault Message   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integrated Motion and Sercos Drive Behavior   |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| SAFE FLT 01…INTERNAL HDWR nn Internal Hardware                 | An internal hardware fault has been detected. On Safe Torque Off (-S0) models, the nn subcode is defined as follows: 01: Internal SPI communication fault. 02: Internal SPI write buffer overrun detected. 03: Internal SPI buffer write collision detected. 04: Internal SPI read buffer error detected. 05: Internal SPI read buffer overflow detected. 06: Internal SPI data integrity failure detected. 07: Internal watchdog time out reset occurred. 08: Internal stack overflow reset occurred. 09: Internal stack underflow detected. 10: Power supply brown out detected. 11: Over voltage monitor circuit test failure. 12: Under voltage monitor circuit test failure. 13: Error occurred during flash download. 14: Internal flash programming failure detected. 15: Safety firmware failed checksum verify. 16: Boot block is active. | Coast-Disable (open contactor enable relay)   |
|                                                                | SAFE FLT 02…INVALID CONFIG Invalid Configuration Fault One or more safety attributes have illegal values. Coast-Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                               |
| SAFE FLT 03…MP OUT nn Motion Power Output Fault                | A fault has been detected on the motion power output circuitry. On Safe Torque Off (-S0) models, the nn subcode is defined as follows: 01: Gate power evaluation fault. 02: Gate enable evaluation fault.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Coast-Disable                                 |
|                                                                | SAFE FLT 04…RESET AT POWERUP Reset at Powerup The reset was detected as active at powerup. Coast-Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                               |
|                                                                | SAFE FLT 05…FEEDBACK 1 Motor Feedback Fault Feedback loss or an illegal state change has been detected on the motor AQB inputs. Coast-Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                               |
|                                                                | SAFE FLT 06…FEEDBACK 2 Auxiliary Feedback Fault Feedback loss or an illegal state change has been detected on the auxiliary AQB inputs. Coast-Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                               |
| SAFE FLT 07…DUAL FB SPEED  Feedback Speed Compare Fault        | A speed miss-compare was detected between the two feedback devices. Coast-Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                               |
| SAFE FLT 08…DUAL FB POSITION  Feedback Position Compare Fault  | A position miss-compare was detected between the two feedback devices. Coast-Disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                               |
| SAFE FLT 09…SS IN nn SS Input Fault                            | The safe stop (SS) input circuitry has detected a problem. On Safe Torque Off (-S0) models, the nn subcode is defined as follows: 01: Input 0 failed pulse test. 02: Input 0 failed optocoupler test. 03: Input 1 failed pulse test. 04: Input 1 failed optocoupler test. 05: Input 3 failed optocoupler test. 06: Input 4 failed optocoupler test.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Coast-Disable (1)                             |

Table 113 - Drive Behavior, SAFE FLT Fault Codes (continued)

| Four-character Display Message  Logix Designer Fault Message   | Description                                                                                                                                                                                  | Integrated Motion and Sercos Drive Behavior   |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| SAFE FLT 10…SS OUT nn SS Output Fault                          | The safe stop (SS) output circuitry has detected a problem. On Safe Torque Off (-S0) models, the nn subcode is defined as follows: 01: Output 0 fault detected. 02: Output 1 fault detected. | Coast-Disable (1)                             |
|                                                                | SAFE FLT 11…DECELERATION Deceleration Fault The motor was detected to be not decelerating fast enough. Coast-Disable                                                                         |                                               |
|                                                                | SAFE FLT 12…STOP SPEED Zero Speed Fault Zero speed was not detected by the end of the stop delay. Coast-Disable                                                                              |                                               |
| SAFE FLT 13…MOTION AFTER STOP Motion After Stopped Fault       | Motion has been detected after the axis was already detected as stopped and the door was unlocked.                                                                                           | Coast-Disable                                 |
|                                                                | SAFE FLT 14…SLS IN SLS Input Fault The Safely-limited Speed (SLS) input circuitry has detected a problem.                                                                                    | Coast-Disable (1)                             |
|                                                                | SAFE FLT 15…SLS OUT SLS Output Fault The Safely-limited Speed (SLS) output circuitry has detected a problem.                                                                                 | Coast-Disable (1)                             |
|                                                                | SAFE FLT 16…SLS SPEED SLS Speed Fault The monitored speed has exceeded the Safely-limited Speed (SLS) limit.                                                                                 | Coast-Disable (1)                             |
|                                                                | SAFE FLT 17…SMS SPEED SMS Speed Fault The monitored speed has exceeded the Safe Maximum Speed (SMS) limit.                                                                                   | Coast-Disable (1)                             |
|                                                                | SAFE FLT 18…ACCELERATION Acceleration Fault The motor was detected not accelerating fast enough.                                                                                             | Coast-Disable (1)                             |
|                                                                | SAFE FLT 19…DIRECTION Direction Fault The monitored direction was found to be in the restricted direction.                                                                                   | Coast-Disable (1)                             |
|                                                                | SAFE FLT 20…DM IN DM Input Fault The door monitor (DM) input was detected as OFF when it should have been ON.                                                                                | Coast-Disable (1)                             |
|                                                                | SAFE FLT 21…DOOR MONITORING Door Monitoring The door monitor (DM) input was detected as being in the wrong state.                                                                            | Coast-Disable (1)                             |
|                                                                | SAFE FLT 22…DC OUT DC Output Fault The door control (DC) output circuitry has detected a problem.                                                                                            | Coast-Disable (1)                             |
|                                                                | SAFE FLT 23…LM IN LM Input Fault The lock monitor (LM) input circuitry has detected a problem.                                                                                               | Coast-Disable (1)                             |
| SAFE FLT 24…LOCK MONITORING LM Input State Fault               | The lock monitor (LM) input was detected as OFF when the Door should have been locked or detected as ON when the door was opened.                                                            | Coast-Disable (1)                             |
|                                                                | SAFE FLT 25…ESM IN ESM Input Fault The enabling switch monitor (ESM) input was detected as OFF when it should have been ON.                                                                  | Coast-Disable (1)                             |
|                                                                | SAFE FLT 26…ESM MONITORING ESM Input State Fault The enabling switch monitor (ESM) input was detected as being in the wrong state .                                                          | Coast-Disable (1)                             |
|                                                                | SAFE FLT 27…ENCODER 1 VOLTAGE Encoder 1 Voltage Fault Encoder voltage is outside of the limits. Coast-Disable                                                                                |                                               |
|                                                                | SAFE FLT 28…ENCODER 2 VOLTAGE Encoder 2 Voltage Fault Encoder voltage is outside of the limits. Coast-Disable                                                                                |                                               |

## Before You Begin

<!-- image -->

## Remove and Replace the Kinetix 6200 and Kinetix 6500 Drive Modules

This chapter provides remove and replace procedures for your Kinetix® 6200 and Kinetix 6500 drive system components.

| Topic Page                                              |
|---------------------------------------------------------|
| Before You Begin 209                                    |
| Remove Kinetix 6200 and Kinetix 6500 Drive Modules 210  |
| Replace Kinetix 6200 and Kinetix 6500 Drive Modules 213 |
| Remove the Power Rail 214                               |
| Replace the Power Rail 214                              |

<!-- image -->

ATTENTION: This drive contains electrostatic discharge (ESD) sensitive parts and assemblies. You are required to follow static-control precautions when you install, test, service, or repair this assembly. If you do not follow ESD control procedures, components can be damaged. If you are not familiar with static control procedures, refer to Guarding Against Electrostatic Damage, publication 8000-4.5.2, or any other applicable ESD awareness handbook.

These tools are required before you begin removal and replacement procedures:

- Screwdriver, 3.5 mm (0.14 in.)
- Voltmeter

## Remove Kinetix 6200 and Kinetix 6500 Drive Modules

<!-- image -->

Follow these steps to remove the control modules, power modules, IPIM, shunt, and slot-filler modules from the Bulletin 2094 power rail.

1. Verify that all control and input power has been removed from the system.

<!-- image -->

ATTENTION: To avoid shock hazard or personal injury, assure that all power has been removed before proceeding. This system can have multiple sources of power. More than one disconnect switch can be required to de-energize the system.

2. Wait five minutes for the DC bus to discharge completely before proceeding.

<!-- image -->

ATTENTION: This product contains stored energy devices. To avoid hazard of electrical shock, verify that all voltage on capacitors has been discharged before attempting to service, repair, or remove this unit. Do not attempt the procedures in this document unless you are qualified to do so and are familiar with solid-state control equipment and the safety procedures in publication NFPA 70E.

3. Label and remove all connectors from the IAM/AM module you are removing.

To identify each connector, refer to page 62 .

4. Remove the motor cable from the cable shield clamp, as shown in these examples.

<!-- image -->

## Remove the Control Module

You can remove the control module from the power module (to replace the control module) or you can remove the control module and power module as a single unit, for example, to move an axis to another slot on the power rail. To remove the control module and power module as a single unit, refer to Remove the Drive Modules on page 212 .

This procedure assumes that you are starting with the Kinetix 6200 or Kinetix 6500 drive system mounted on the power rail.

Follow these steps to remove the control module.

1. Loosen the captive screw on top of the control module.
2. Grasp the control module and power module, and gently pull the control module away from the connectors enough to clear the guide pins.

The control module mounting studs pivot on the hooks.

3. Lift the control module off of the hooks and remove the control module from the power module.

<!-- image -->

## Remove the Drive Modules

You can remove the control module from the power module (to replace the power module) or you can remove the control module and power module as a single unit.

<!-- image -->

If you intend to reuse any control module and power module pair, you can remove them as a single unit, for example, to move an axis to another slot on the power rail.

IMPORTANT

This procedure also applies to Bulletin 2094-BSP2 shunt module, 2094-PRF slot-filler module, and 2094-SEPM-B24-S IPIM module.

Follow these steps to remove the power modules.

1. Loosen the mounting screw (bottom center of each module).
2. Grasp the top and bottom of the module with both hands and gently pull the module away from the connectors enough to clear the guide pins (module pivots on top bracket).
3. Lift the bracket out of the power rail slot and remove the module from the power rail.

<!-- image -->

## Replace Kinetix 6200 and Kinetix 6500 Drive Modules

Follow these steps to replace control modules, power modules, shunt modules, and slot-filler modules from the Bulletin 2094 power rail.

## Replace the Drive Modules

Follow these steps to replace the drive modules.

1. Determine your power module, shunt module, or slot-filler module replacement.
2. Prepare to mount your replacement drive module by removing the protective covers from the power rail connectors.
3. Hang the mounting bracket from the slot on the power rail.

| If you are Then                                                   |
|-------------------------------------------------------------------|
| Replacing a drive module on an existing power rail Go to step 3 . |
| Replacing a drive module on a new power rail Go to step 2 .       |

IMPORTANT

Power rails must be in vertical orientation before replacing drive modules for pins to seat properly.

4. Align the guide pins on the power rail with the guide pin holes in the back of the drive module (refer to the figure above).

<!-- image -->

The IAM power module can have two or three power rail connectors and guide pins, the AM power module can have one or two, all other modules have only one connector and one guide pin.

5. Use 2.26 N·m (20 lb·in) torque to tighten the mounting screw.

## Replace the Control Modules

Refer to Mount the Control Modules on page 58 to replace your control modules.

Follow these steps when you have finished replacing your control modules.

1. Reconnect the module connectors.
2. Reapply power to the system.
3. Verify that the system is operating properly.

<!-- image -->

However, after you replace a 2094-xx02x-M0x-S1 Safe Speed Monitor control module, the safety configuration (web page) can be from the previous control module of the same IP address. To correct this condition, go to Internet Explorer/Tools/Internet Options and under Browsing history, click Delete, to delete temporary files, cookies, and web form information.

## Remove the Power Rail

## Replace the Power Rail

This procedure assumes you have removed all modules from the power rail.

Follow these steps to remove the power rail.

1. Disconnect the braided grounding strap from the grounding stud on the right side of the power rail.
2. Loosen the mounting bolts (removing the bolts is not necessary).
3. Lift the power rail up and off of the mounting bolts.

<!-- image -->

This procedure assumes you do not need to change the location of the power rail on the panel and you intend to reuse the mounting bolts of the power rail you just removed.

## IMPORTANT

If you need to change the location of the power rail, or if you are installing a power rail designed for additional or fewer modules than you removed, refer to Kinetix 6000 Power Rail Installation Instructions, publication 2094-IN003 .

<!-- image -->

ATTENTION: To avoid damage to the power rail during installation, do not remove the protective covers until the module for each slot is ready for mounting.

Follow these steps to replace the power rail.

1. Align the replacement power rail over the existing mounting bolts.

IMPORTANT

To improve the bond between the power rail and subpanel, construct your subpanel out of zinc-plated (paint-free) steel.

2. Tighten the mounting bolts.
3. Reattach the braided grounding strap to the power rail grounding stud (refer to page 214).

## Interconnect Diagrams

This appendix provides wiring examples and system block diagrams for your Kinetix® 6200 and Kinetix 6500 drive system components.

| Topic Page                                              |
|---------------------------------------------------------|
| Interconnect Diagram Notes 216                          |
| Power Wiring Examples 217                               |
| Axis Module/Rotary Motor Wiring Examples 226            |
| Axis Module/Linear Motor/Actuator Wiring Examples 231   |
| Kinetix 6000M Integrated Drive-Motor Wiring Example 236 |
| Brake Control Example 237                               |
| System Block Diagrams 238                               |

<!-- image -->

Interconnect Diagram Notes This appendix provides wiring examples to assist you in wiring the Kinetix 6200 and Kinetix 6500 drive systems. These notes apply to the wiring examples on the following pages.

<!-- image -->

<!-- image -->

| Note Information                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 For power wiring specifications, refer to Power Wiring Requirements on page 98 .                                                                                                                                                                                                                                                                                                                        |
| 2 For input fuse and circuit breaker sizes, refer to Circuit Breaker/Fuse Options on page 30 .                                                                                                                                                                                                                                                                                                            |
| 3 Place AC (EMC) line filters as close to the drive as possible and do not route very dirty wires in wireway. If routing in wireway is unavoidable, use shielded cable with shields grounded to the drive chassis and filter case. For AC line filter specifications, refer to the Kinetix Motion Accessories Technical Data, publication KNX-TD004 .                                                     |
| 4 Terminal block is required to make connections.                                                                                                                                                                                                                                                                                                                                                         |
| 5 2094-BCxx-Mxx-M (460V) IAM modules require a step-down transformer for single-phase control power input. The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder.                                                                                                      |
| 6 2094-BLxxS and 2094-XL75S-C2 LIM modules can supply input power for up to eight axes. 2094-XL75S-C1 LIM modules can supply input power for up to sixteen axes. For common-bus systems with more than sixteen axes, multiple LIM modules (or control power transformers) are required. For Kinetix 6000M systems, the control power current needs to be calculated and the LIM module needs to be sized. |
| 7 2094-BLxxS, and 2094-XL75S-Cx LIM modules are capable of connecting to two IAM modules, providing each IAM module has its own line filter and the maximum current specification is not exceeded.                                                                                                                                                                                                        |
| 8 Contactor coil (M1) needs integrated surge suppressors for AC coil operation. Refer to the Kinetix Servo Drives Technical Data, publication KNX-TD003 .                                                                                                                                                                                                                                                 |
| 9 Drive Enable input must be opened when main power is removed, or a drive fault occurs. A delay of at least 1.0 second must be observed before attempting to enable the drive after main power is restored.                                                                                                                                                                                              |
| 10 Cable shield clamp must be used to meet CE requirements. No external connection to ground is required.                                                                                                                                                                                                                                                                                                 |
| 11 Default configuration for jumper is for grounded power at user site. Ungrounded sites must jumper the bleeder resistor to prevent high electrostatic buildup. Refer to Determine the Input Power Configuration on page 88 for more information.                                                                                                                                                        |
| 12 Leave jumper between PR2 and PR3 as shown to use the internal precharge resistor. Remove jumper when external precharge/circuit is required. For more information, refer to the 8720MC Regenerative Power Supply Installation Manual, publication 8720MC-RM001 .                                                                                                                                       |
| ATTENTION: Implementation of safety circuits and risk assessment is the responsibility of the machine builder. Please reference international standards IEC 62061 and ISO 13849-1 estimation and safety performance categories.                                                                                                                                                                           |
| 14  ATTENTION: Wiring the contactor enable relay is required. To avoid personal injury or damage to the drive, wire the contactor enable relay into your safety control string. Refer to Contactor Enable Relay on page 72, for more information. The recommended minimum 2 wire size for wiring the three-phase power enable control circuit to the contactor enable connector is 1.5 mm 2 (16 AWG).                                                                                                                                                                                                                                                                                                                                                                                                           |
| 15 The Bulletin 2094 power module referenced is either an individual axis module (catalog number 2094-BMxx-M) or the same axis module that resides within an integrated axis module (catalog number 2094-BCxx-Mxx-M).                                                                                                                                                                                     |
| 16 For motor cable specifications, refer to the Kinetix Motion Accessories Technical Data, publication KNX-TD004 .                                                                                                                                                                                                                                                                                        |
| 17 Wire colors are for flying-lead cable and can vary from the premolded cable connectors.                                                                                                                                                                                                                                                                                                                |
| 18 Motor power cables (2090-XXNPMF-xxSxx and 2090-CPBM6DF-16AAxx) have a drain wire that must be folded back under the cable shield clamp.                                                                                                                                                                                                                                                                |
| 19 MPL-B15xx-H…MPL-B45xx-H, MPAS-Bxxx (direct drive) encoders use the +5V DC supply.                                                                                                                                                                                                                                                                                                                      |
| 20 MPL-B15xx-V/E…MPL-B2xx-V/E, MPL-B3xx-S/M…MPL-B9xx-S/M, MPL-A5xx, MPM-Bxx, MPF-Bxx, MPS-Bxxx, MPAR-Bxxx, and MPAS-Bxxx (ballscrew) encoders use the +9V DC supply.                                                                                                                                                                                                                                      |
| 21 Brake connector pins are labeled plus (+) and minus (-) or F and G respectively. Power connector pins are labeled U, V, W, and GND or A, B, C, and D respectively.                                                                                                                                                                                                                                     |

## Power Wiring Examples

These examples apply to power wiring configurations with and without the Bulletin 2094 line interface module (LIM), DC common bus wiring, and shunt module wiring.

Figure 87 - Single IAM Module with 2094-BL02 LIM Module

<!-- image -->

* Indicates User Supplied Component

Figure 88 - Multiple IAM Module with LIM Module

<!-- image -->

## Multiple IAM Module with LIM Module (continued)

<!-- image -->

This configuration does not include a LIM module. You must supply input power components. The single-phase and three-phase line filters are wired downstream of fusing and the M1 contactor.

<!-- image -->

ATTENTION: Wiring the contactor enable (CED) relay is required. To avoid injury or damage to the drive, wire the contactor enable relay into your control string. Refer to Contactor Enable Relay on page 72 for more information.

Figure 89 - IAM Module (without LIM module)

<!-- image -->

* Indicates User Supplied Component

## DC Common Bus Wiring Examples

Figure 90 - Leader IAM Module with Single Follower IAM Module

<!-- image -->

Figure 91 - Leader IAM Module with Multiple Follower IAM Modules

<!-- image -->

## Leader IAM Module with Multiple Follower IAM Modules (continued)

<!-- image -->

* Indicates User Supplied Component

Figure 92 - 8720MC-RPS Leader Drive with Single Follower IAM Module

<!-- image -->

## Shunt Module Wiring Examples

Refer to Kinetix Motion Accessories Technical Data, publication KNX-TD004 for the Bulletin 1394 external shunt module catalog numbers available for the Kinetix 6200 and Kinetix 6500 drive systems.

Figure 93 - Shunt Module Wired for Internal Operation (default configuration)

<!-- image -->

Refer to the Kinetix 6000 Shunt Module Installation Instructions, publication 2094-IN004, for additional installation information.

Figure 94 - Shunt Module with External Passive Shunt

<!-- image -->

## IMPORTANT

Only passive shunts with a thermal switch are wired to the TS connector on the Kinetix 6000 shunt module. If your external passive shunt does not have a thermal switch, leave the jumper (default configuration) in place on the TS connector.

Refer to the External Shunt Module Installation Instructions, publication 2090-IN004, for additional installation information.

## Axis Module/Rotary Motor Wiring Examples

These examples apply to Kinetix 6200 and Kinetix 6500 drives with Allen-Bradley® rotary motors.

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with bayonet connectors.

Figure 95 - AM Module with Kinetix MPL-B Rotary Motors

<!-- image -->

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with circular DIN (threaded) connectors.

Figure 96 - AM Module with Kinetix MPL-B and Kinetix MPS-B Rotary Motors

<!-- image -->

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with circular DIN (SpeedTec) connectors.

Figure 97 - AM Module with Kinetix MPL-B, MPM-B, MPF-B, and MPS-B Rotary Motors

<!-- image -->

Note 16

Figure 98 - AM Module with Kinetix RDB Direct-drive Servo Motors

<!-- image -->

<!-- image -->

Refer to Low Profile Connector Kit Installation Instructions, publication 2094IN007, for connector kit specifications.

Figure 99 - AM Module (460V) Wiring Examples with 1326AB Motors

<!-- image -->

## Axis Module/Linear Motor/ Actuator Wiring Examples

These examples apply to Kinetix 6200 and Kinetix 6500 drives with Allen-Bradley linear motors and actuators.

Figure 100 - AM Module with Kinetix MPAS-Integrated Linear Stages

<!-- image -->

Figure 101 - AM Module with Kinetix MPAR and MPAI Electric Cylinders

<!-- image -->

<!-- image -->

fer to Low Profile Connector Kit Installation Instructions, publication 2094-IN007, for connector kit specifications.

Table 114 - Kinetix MPAR and MPAI Electric Cylinder Power and Feedback Cables

| Electric Cylinder Cat. No.                       | Fram e   | Power Cable Cat. No.                                                    | Feedback Cable Cat. No.                                                 |
|--------------------------------------------------|----------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| MPAR-B1xxx (series A and B) 32 2090-XXNPMF-16Sxx |          | (standard) or 2090-CPxM4DF-16AFxx (continuous-flex)                     | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-B2xxx (series A and B) 40                   |          | (standard) or 2090-CPxM4DF-16AFxx (continuous-flex)                     | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-B1xxx (series B and C) 32                   |          | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-B2xxx (series B and C) 40                   |          | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-B3xxx                                       | 63       | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B2xxxx                                      | 64       | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B3xxxx                                      | 83       | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B4xxxx                                      | 110      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B5xxxx                                      | 144      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |

Figure 102 - AM Module with Kinetix LDAT Linear Thrusters

<!-- image -->

Refer to Low Profile Connector Kit Installation Instructions, publication 2094-IN007, for connector kit specifications.

Figure 103 - AM Module with Kinetix LDC Linear Motors (cable connectors)

<!-- image -->

Figure 104 - AM Module with Kinetix LDC Linear Motors (flying-lead cables)

<!-- image -->

## Kinetix 6000M Integrated Drive-Motor Wiring Example

<!-- image -->

This example applies to Kinetix 6200 drives with Kinetix 6000M integrated drive-motor (IDM) systems.

ATTENTION: When using the Kinetix 6000M IDM system, with Kinetix 6200 drives, the IPIM module only forwards the safetyfeedback monitoring signals to the adjacent (downstream) drive on the power rail. To avoid personal injury due to unexpected motion, make sure that the safety-feedback connections are fed through each drive on the power rail so that safety devices can recognize when the Kinetix 6200 drive opens the feedback contactor in the cascaded safety string.

## Figure 105 - IPIM Module with IDM Unit

<!-- image -->

## Brake Control Example

The relay output of the Bulletin 2094 IAM/AM module (MBRK± BC-5 and BC-6) is suitable for directly controlling a motor brake, subject to the relay voltage limit of 30V DC, and the relay current limit as shown below.

## Table 115 - Brake Relay Current Limit

| Bulletin 2094 IAM/AM Power Module Brake Current Rating, max             |       |
|-------------------------------------------------------------------------|-------|
| 2094-BC01-Mxx-M, 2094-BC02-M02-M, 2094-BMP5-M, 2094-BM01-M, 2094-BM02-M | 3.0 A |
| 2094-BC04-M03-M, 2094-BC07-M05-M, 2094-BM03-M, 2094-BM05-M              | 3.0 A |

## Table 116 - Coil Currents Rated at &lt;1.0 A

| Compatible Brake Motors/Actuators Coil Current                 |               |
|----------------------------------------------------------------|---------------|
| MPL-B1510, MPL-B1520, MPL-B1530 0.43…0.53 A                    |               |
| MPL-B210, MPL-B220, MPL-B230 0.46…0.56 A                       |               |
| MPL/MPF-B310, MPL/MPF-B320, MPL/MPF-B330                       | 0.45…0.55 A   |
| MPS-B330, MPM-B115, MDF-SB1003                                 | 0.45…0.55 A   |
| MPL-B420, MPL-B430, MPL-B4520, MPL-B4530, MPL-B4540, MPL-B4560 | 0.576…0.704 A |
| MPS-B4540, MPM-B130, MDF-SB1153, MDF-SB1304                    | 0.576…0.704 A |
| 1326AB-B4xxx                                                   | 0.88 A        |

## Table 117 - Coil Currents Rated at &gt;1.0 A and   1.3 A

| Compatible Brake Motors Coil Current         |
|----------------------------------------------|
| MPL-B520, MPL-B540, and MPM-B165 1.05…1.28 A |
| 1326AB-B5xxx  1.20 A                         |

## System Block Diagrams

This section provides block diagrams of the Kinetix 6200 and Kinetix 6500 drive modules. For block diagrams of the LIM module, refer to Additional Resources on page 10 for the documentation available for those products.

Figure 106 - IAM/AM Power Module (inverter) Block Diagram

<!-- image -->

Figure 107 - IAM Power Module (converter) Block Diagram

<!-- image -->

Figure 108 - Shunt Module Block Diagram

<!-- image -->

## Upgrade Kinetix 6000M System Firmware

## Upgrade the Drive Firmware

This appendix provides procedures for upgrading Kinetix® 6200/6500 drive firmware by using ControlFLASH™ software.

| Topic Page                                               |
|----------------------------------------------------------|
| Upgrade Kinetix 6000M System Firmware 241                |
| Upgrade Kinetix 6200 and Kinetix 6500 Drive Firmware 242 |

Upgrading firmware for the Kinetix 6000M integrated drive-motor (IDM) system is done by using ControlFLASH software. The procedure for upgrading the IDM units uses the Sercos interface, similar to the axis modules. However, upgrading firmware on the IPIM module is accomplished over the EtherNet/IP™ network.

For the firmware upgrade procedure specific to the IDM system, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

<!-- image -->

## Upgrade Kinetix 6200 and Kinetix 6500 Drive Firmware

Upgrading axis module firmware by using ControlFLASH software involves configuring your controller communication, selecting the drive to upgrade, and upgrading the firmware.

## IMPORTANT

If the xx02x-Mxx-S0 (Safe Torque Off) drive firmware contains updated safety firmware, you must de-energize the safety inputs first or the upgrade will fail.

## Before You Begin

The firmware revision for software and modules varies, depending on whether your drive system uses Sercos or EtherNet/IP networks.

Table 118 - Kinetix 6200 (Sercos interface) System Requirements

|                                                                              | Description Cat. No. Firmware Revision                                       |                                                                              |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| RSLogix 5000®software or Studio 5000 Logix Designer® application            | RSLogix 5000software 17.x or later                                          |                                                                              |
| RSLogix 5000®software or Studio 5000 Logix Designer® application            | Logix Designer application 21.x or later                                     |                                                                              |
| ControlLogix® Sercos module                                                  | 1756-MxxSE 17.16 or later                                                    |                                                                              |
| ControlLogix® Sercos module                                                  | 1756-L60M03SE 17.2 or later                                                  |                                                                              |
| CompactLogix™ Sercos module 1768-M04SE 17.16 or later                        |                                                                              |                                                                              |
| SoftLogix™ Sercos PCI card 1784-PM16SE 17.10 or later                        |                                                                              |                                                                              |
| RSLinx® software 2.54 or later                                               | RSLinx® software 2.54 or later                                               |                                                                              |
| ControlFLASH software kit (1)                                                | 4.00.00 or later                                                             |                                                                              |
| Catalog numbers of the targeted Kinetix 6200 drive module you want to flash. | Catalog numbers of the targeted Kinetix 6200 drive module you want to flash. | Catalog numbers of the targeted Kinetix 6200 drive module you want to flash. |

Network path to the targeted Kinetix 6200 drive module you want to flash.

(1) Download the ControlFLASH software kit from the Product Compatibility and Download Center at: rok.auto/pcdc. For more ControlFLASH software information (not Kinetix 6200 specific), refer to the ControlFLASH Firmware Upgrade Kit User Manual, publication 1756-UM105 .

Table 119 - Kinetix 6500 (EtherNet/IP network) System Requirements

|                                                                              | Description Cat. No. Firmware Revision                                       |                                                                              |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| RSLogix 5000software or                                                     | RSLogix 5000software 18.x or later                                          |                                                                              |
| Studio 5000 Logix Designer                                                   | Logix Designer application 21.x or later                                     |                                                                              |
| RSLinx software 2.54 or later                                                |                                                                              |                                                                              |
| ControlFLASH software kit (1)                                                | 8.00.017 or later                                                            |                                                                              |
| Catalog numbers of the targeted Kinetix 6500 drive module you want to flash. | Catalog numbers of the targeted Kinetix 6500 drive module you want to flash. | Catalog numbers of the targeted Kinetix 6500 drive module you want to flash. |

Network path to the targeted Kinetix 6500 drive module you want to flash.

(1) Download the ControlFLASH software kit from the Product Compatibility and Download Center at: rok.auto/pcdc. For more ControlFLASH software information (not Kinetix 6500 specific), refer to the ControlFLASH Firmware Upgrade Kit User Manual, publication 1756-UM105 .

## IMPORTANT

Control power must be present at CPD-1 and CPD-2 prior to upgrading your target drive.

For Sercos drives, the four-character status indicator on the target IAM (inverter) module or AM module must be scrolling CP-2, CONFIGURING, STOPPED, RUNNING, or PRE-CHARGE before beginning this procedure.

For EtherNet/IP drives, the four-character status indicator on target the IAM (inverter) module or AM module must be scrolling STANDBY, CONFIGURING, CONNECTING, STOPPED, RUNNING, or PRE-CHARGE before beginning this procedure.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment during the firmware upgrade due to unpredictable motor activity, do not apply threephase AC or common-bus DC input power to the drive.

## Configure Logix 5000 Communication

This procedure assumes that your communication method to the Logix 5000™ controller is using the Ethernet protocol. It is also assumed that your Logix 5000 Ethernet module has already been configured.

For more information, refer to the ControlLogix System User Manual, publication 1756-UM001 .

Follow these steps to configure Logix 5000 communication.

1. Open your RSLinx Classic software.
2. From the Communications pull-down menu, choose Configure Drivers. The Configure Drivers dialog box opens.
3. From the Available Drive Types pull-down menu, choose Ethernet devices.
4. Click Add New.

<!-- image -->

The Add New RSLinx Classic Driver dialog box opens.

5. Type the new driver name.
6. Click OK.

<!-- image -->

The Configure driver dialog box opens.

<!-- image -->

7. Type the IP address.

For Kinetix 6200 drive systems, type the IP address of your Logix Ethernet module.

For Kinetix 6500 drive systems, type the IP address of your IAM power module.

8. Click OK.

The new Ethernet driver appears under Configured Drivers.

<!-- image -->

9. Click Close.
10. Minimize the RSLinx application dialog box.

## Upgrade Firmware

Follow these steps to select the drive module to upgrade.

1. Open your ControlFLASH software.

You can access the ControlFLASH software by either of these methods:

- From the Tools menu in the Logix Designer application, choose ControlFLASH.
- Choose Start&gt;Programs&gt;FLASH Programming Tools&gt; ControlFLASH.

The Welcome to ControlFLASH dialog box opens.

<!-- image -->

2. Click Next.

The Catalog Number dialog box opens.

<!-- image -->

3. Select your drive module.

In this example, the Kinetix 6500 control module is selected. If you are flashing a Kinetix 6200 control module, you'll select your Bulletin 2094 power module and control module combination.

4. Click Next.

The Select Device to Update dialog box opens.

<!-- image -->

5. Expand your Ethernet node, Logix 5000 backplane, and EtherNet/IP network module.
6. Select the servo drive to upgrade.
7. Click OK.

The Firmware Revision dialog box opens.

<!-- image -->

8. Select the firmware revision to upgrade.
9. Click Next.

The Summary dialog box opens.

<!-- image -->

10. Confirm the drive catalog number and firmware revision.
11. Click Finish.

This ControlFLASH warning dialog box opens.

<!-- image -->

12. Click Yes (only if you are ready).

This ControlFLASH warning dialog box opens.

<!-- image -->

In this example, the warning applies to the Kinetix 6500 control modules. If you are flashing a Kinetix 6200 control module, the warning will be different.

13. Acknowledge the warning and click OK.

The Progress dialog box opens and flashing begins.

<!-- image -->

The control module four-character status indicator changes from CP-2, CONFIGURING, STOPPED, RUNNING, or PRE-CHARGE to FIRMWARE UPDATE, which indicates that upgrading is in progress.

After the flash information is sent to the drive, the drive resets and performs diagnostic checking.

14. Wait for the Progress dialog box to time out.

It is normal for this process to take several minutes.

IMPORTANT

<!-- image -->

Do not cycle power to the drive during this process or the firmware upgrade will not complete successfully.

15. The Update Status dialog box opens and indicates success or failure as described below.
16. Click OK.

<!-- image -->

| Upgrading Status If   |                                                                                                                                                                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Success               | 1. Update complete appears in a GREEN Status dialog box. 2. Go to step 16 .                                                                                               |
| Failure               | 1. Update failure appears in a RED Status dialog box. 2. Refer to ControlFLASH Firmware Upgrade Kit Quick Start, publication 1756-QS105, for troubleshooting information. |

<!-- image -->

## Verify the Firmware Upgrade

Follow these steps to verify your firmware upgrade was successful.

<!-- image -->

Verifying the firmware upgrade is optional.

1. Open your RSLinx software.
2. From the Communications pull-down menu, choose RSWho.
3. Expand your Ethernet node, Logix 5000 backplane, and EtherNet/IP network module.
4. Right-click the drive module and choose Device Properties.
5. The Device Properties dialog box opens.
5. Verify the new firmware revision level.
6. Click Close.

<!-- image -->

<!-- image -->

## Before You Begin

## DC Common-bus Applications

This appendix provides information and an example for calculating additional bus capacitance specific to the Kinetix® 6200 and Kinetix 6500 modular drive systems configured for DC common bus.

| Topic Page                                 |
|--------------------------------------------|
| Before You Begin 249                       |
| Calculate Total Bus Capacitance 250        |
| Calculate Additional Bus Capacitance 251   |
| Bulletin 2094 Drive Capacitance Values 251 |
| Common Bus Capacitance Example 252         |

Calculating capacitance, as it applies to the Bulletin 2094 shunt module and Kinetix 6000M IPIM module, is also included in this appendix.

These procedures assume you have mounted and wired your Kinetix 6200 or Kinetix 6500 DC common-bus system.

Before you set the Additional Bus Capacitance (Add Bus Cap) parameter in the Logix Designer application, you need to calculate these values:

- Total bus capacitance
- Additional bus capacitance

<!-- image -->

## Calculate Total Bus Capacitance

Total bus capacitance is the sum of all capacitance values for your Bulletin 2094 common-bus modules. Specifically, this includes the capacitance values for each of these modules:

- Leader IAM (converter and inverter) module
- Each AM and shunt module (if present) on the leader IAM power rail
- Each IPIM module (if present) on the leader IAM power rail
- Each follower IAM (converter and inverter) module
- Each AM module on the follower IAM power rail
- Each IPIM module (if present) on the follower IAM power rail

Refer to Bulletin 2094 Drive Capacitance Values on page 251 for IAM, AM, IPIM, and shunt module capacitance values.

## IMPORTANT

If total bus capacitance of your system exceeds the leader IAM power module precharge rating, the IAM module four-character display scrolls a power cycle user limit condition. If input power is applied, the display scrolls a power cycle fault limit condition.

To correct this condition, you must replace the leader IAM power module with a larger module or decrease the total bus capacitance by removing AM power modules or IPIM modules.

## Table 120 - Maximum IAM Module Bus Capacitance

| Leader IAM (400V-class) Module Cat. No.   | Bus Capacitance, max µF   |
|-------------------------------------------|---------------------------|
| 2094-BC01-MP5-M                           | 4585                      |
| 2094-BC01-M01-M                           |                           |
| 2094-BC02-M02-M 8955                      |                           |
| 2094-BC04-M03-M 8955                      |                           |
| 2094-BC07-M05-M 17,915                    |                           |

| IMPORTANT   | If your total bus capacitance value exceeds the value in the table above, you must increase the size of the leader IAM module or decrease the total bus capacitance by removing other modules on the power rail.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Calculate Additional Bus Capacitance

## Bulletin 2094 Drive Capacitance Values

Additional bus capacitance is the sum of all follower IAM, AM, and IPIM module capacitance values for your Bulletin 2094 common-bus modules. Specifically, this includes the capacitance values for each of these modules:

- Each follower IAM (converter and inverter) module
- Each AM module on the follower IAM module power rail
- Each IPIM module on the follower IAM module power rail

If you are using Kinetix 6200 (Sercos) drives or Kinetix 6500 (integrated motion on EtherNet/IP) drives, calculate additional bus capacitance in this appendix and enter the value in Module Properties&gt;Power tab&gt;Bus Capacitance.

In the example on page 252, the value is 790 μF.

Figure 109 - Module Properties&gt;Power Tab

<!-- image -->

Use these tables when calculating total bus capacitance and additional bus capacitance for your Bulletin 2094 common-bus application.

Table 121 - IAM/AM (400V-class) Modules

| IAM Converter (400V-class) Cat. No.   | Capacitance µF   | AM Inverter (400V-class) Cat. No. Capacitance µF   |
|---------------------------------------|------------------|----------------------------------------------------|
| 2094-BC01-MP5-M                       | 110              | 2094-BMP5-M 75                                     |
| 2094-BC01-M01-M 2094-BM01-M 150       | 110              |                                                    |
| 2094-BC02-M02-M 220 2094-BM02-M 270   |                  |                                                    |
| 2094-BC04-M03-M 940 2094-BM03-M 840   |                  |                                                    |
| 2094-BC07-M05-M 1410 2094-BM05-M 1175 |                  |                                                    |

Table 122 - Shunt Module (400V-class)

| Shunt Module (200/400V-class) Cat. No.   | Capacitance µF   |
|------------------------------------------|------------------|
| 2094-BSP2 470                            |                  |

Table 123 - IPIM Module (400V-class)

| IPIM Module (400V-class) Cat. No.   | Capacitance µF   |
|-------------------------------------|------------------|
| 2094-SEPM-B24-S 840                 |                  |

## Common Bus Capacitance Example

In this example, the sum of the leader IAM power rail modules capacitance (1335 μF) and the follower IAM power rail modules capacitance (790 μF) equals 2125 μF total bus capacitance.

The sum of the follower IAM module power rail equals 790 μF additional bus capacitance.

Figure 110 - Calculating Common Bus Capacitance

<!-- image -->

## Benefits

## How it Works

<!-- image -->

## Configure the Load Observer Feature

The load observer feature is a control loop inside the Kinetix® 6200 drive (firmware revision 1.049 or later) that estimates the mechanical load on the motor and compensates for it, thereby forcing the motor to behave as if it is unloaded and relatively easy to control. As a result, load observer automatically compensates for disturbances and load dynamics, such as sudden inertia/ torque changes, compliance, backlash, and resonances.

| Topic Page                                       |
|--------------------------------------------------|
| Benefits 253                                     |
| How it Works 253                                 |
| Configuration 254                                |
| Setting Gains with Sercos IDN Write Messages 265 |
| Compensate for High Frequency Resonances 266     |

You can use load observer with out-of-box controller gains, where the load is unknown and thus the Load Inertia Ratio = 0, or with auto-tuned controller gains, where the Load Inertia Ratio is known or calculated by performing an auto-tune procedure.

When used with out-of-box controller gains, load observer does the following.

- Provides relatively high-performance motion control without tuning
- Automatically compensates for load resonances and machine wear over time

When used with auto-tuned controller gains, load observer does the following.

- Increases controller bandwidth
- Reduces tracking errors, so line speeds can be increased
- Provides tighter control of moving parts, reducing wear and saving material costs

Load observer acts on the acceleration signal within the control loops and monitors the Acceleration Reference and the Actual Position Feedback. Load observer models an ideal unloaded motor and generates a load Torque Estimate, in torque units, that represents any deviation in response of the actual motor and mechanics from the ideal model. This deviation represents the reaction torque placed on the motor shaft by the load mechanics. It is estimated in real time and compensated by closed loop operation.

## Configuration

Figure 111 - Load Observer and Control Loop Signals Relationship Block Diagram

<!-- image -->

Load observer also generates a Velocity Estimate signal that you can apply to the velocity loop. The Velocity Estimate has less delay than the Velocity Feedback signal derived from the actual feedback device. It also helps to reduce high frequency output noise caused by load observer's aggressive action on the acceleration reference. Together, load observer with the Velocity Estimate setting provides the best overall performance.

You can configure the load observer feature in a variety of ways by writing to a set of configuration IDN parameters. The overall behavior of load observer is controlled by Load Observer Configuration (IDN P-431). This parameter is used to select the load observer mode. It can be set to the following values.

Table 124 - Load Observer Modes

|                                      | Mode Value Description                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      | Disabled (default) 0 Load Observer is inactive                                          | Disabled (default) 0 Load Observer is inactive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Load Observer Only 1                 | Provides a Torque Estimate only                                                         | This setting is a filtered acceleration feedback with the addition of integral action in the acceleration forward path that is active below the observer bandwidth. This greatly increases the disturbance rejection properties (stiffness) over the acceleration feedback setting. However, it is also fairly aggressive and the observer bandwidth must be decreased for stable operation.                                                                                                                                                                                                                        |
| Load Observer with Velocity Estimate | 2 Standard Operation: Provides Torque and Velocity Estimates                            | This setting combines the best of the Load Observer Only and Velocity Estimate Only settings. Separately, load observer removes error, but increases phase lag and is fairly aggressive, whereas velocity estimate provides a smooth response and reduces phase lag, but creates error. Together, they remove error and provide a smooth response. Load observer performs well in situations that require adapting to changing inertia and velocity integrator anti-windup.                                                                                                                                         |
| Velocity Estimate Only 3             | Provides a Velocity Estimate only                                                       | This setting creates a filtered velocity feedback signal that is void of phase lag. Less phase lag (delay around the loop) allows for higher performance. However, the signal is modeled at frequencies above the observer bandwidth, producing error in velocity feedback. This generates a fictitiously lower velocity error since velocity error equals velocity command minus velocity feedback. Nevertheless, the steady state error disappears when used in position mode with either the position integrator or the observer integrator. This configuration is not desirable for Velocity mode applications. |
| Acceleration Feedback 4              | Provides acceleration feedback by disconnecting Acceleration Reference to load observer | This setting creates a filtered acceleration feedback signal. This setting is fairly aggressive and the observer bandwidth must be decreased significantly for stable operation. The Load Observer Only setting is similar, but without the additional phase lag (delay) created by necessary filtering.                                                                                                                                                                                                                                                                                                            |

The following figures illustrate the high-level operation of each observer mode.

Figure 112 - Load Observer Disabled Configuration (Value 0)

<!-- image -->

<!-- image -->

You can configure the load observer feature in a variety of ways by writing to a set of configuration IDN parameters. The overall behavior of load observer is controlled by Load Observer Configuration (IDN P-431). This parameter is used to select the Load Observer mode. Use it to set the IDN values listed in Table 124 on page 254 .

## Remaining IDN Parameter Descriptions

Load observer gains that require user interaction are Load Observer Bandwidth (Kop) and Load Observer Integral Bandwidth (Koi). They are set by IDN P-432 and IDN P-433, respectively. Guidelines for setting these gains are provided in the following sections. In general, Kop acts like a velocity integrator without windup and Koi acts a like a position integrator without windup. Typically, Koi = 0.

Figure 117 - Load Observer Gains

<!-- image -->

Load observer gains that do not require user interaction are Load Observer Feedback Gain (Kof) and the Load Observer Input Gain (Kou). They are automatically set internally based on the Load Observer Configuration. However, when in Acceleration Feedback mode, Kof can also be set manually by IDN P-434 with typical values between zero and one.

Table 125 - Load Observer Gain Parameters

|                                                      |                     |    | IDN Name Units Format Value, min Value, max   |
|------------------------------------------------------|---------------------|----|-----------------------------------------------|
| P:0:432 Load Observer Bandwidth (Kop) Rad/s          | 16 bit unsigned int |  0 | 12,500                                        |
| P:0:433 Load Observer Integral Bandwidth (Koi) Rad/s | 16 bit unsigned int |  0 | 65,535                                        |
| P:0:434 Load Observer Feedback Gain (Kof) – 200      | 16 bit unsigned int |  0 |                                               |

## IMPORTANT

You must validate the input parameter to the message instruction when executing message instructions to the attributes in Table 125 .

The value being sent is interpreted by the drive as an unsigned 16-bit integer. Attempting to write negative values results in the binary-equivalent positive value being used by the drive.

The Acceleration Estimate and Torque Estimate signals are read by using IDN-435 and P-436, respectively. Definitions for these IDN parameters are given in the following table.

Table 126 - Load Observer Output Signals

|                                                          |                   |        | IDN Name Units Format Value, min Value, max   |
|----------------------------------------------------------|-------------------|--------|-----------------------------------------------|
| P:0:435 Load Observer Acceleration Estimate Acceleration | 32bit signed int  | -2  31 | 2  31  -1                                     |
| P:0:436 Load Observer Torque Estimate Torque             | 16 bit signed int | -2  15 | 2  15  -1                                     |

When load observer and the torque low-pass filter are both enabled, and the low-pass filter bandwidth is less than 5 times the load observer bandwidth, their interaction can interfere with each other, causing instability. The lowpass filter is always limited to a bandwidth under 400 Hz in drive firmware. IDN P-065 can be used to override the torque low-pass filter bandwidth limiting. The filter is also bypassed if the override IDN P-065 is set to 1 and the torque low-pass filter bandwidth is set to zero.

Table 127 - Torque Low-pass Filter Bandwidth

|   IDN P:0:065 | Bandwidth in the Logix Designer Application Actual Bandwidth in Drive   |
|---------------|-------------------------------------------------------------------------|
|             0 | = 0 400 Hz                                                              |
|             0 | > 0 Limited to 400 Hz                                                 |
|             1 | = 0 Filter bypassed                                                     |
|             1 | > 0 Limited to 10,430 Hz                                              |

Refer to Appendix F on page 289 for more information on changing IDN parameter values with read/write messages in the Logix Designer application.

## Out-of-Box Gain Settings

This method of setting controller gains works for unknown loads or when an auto-tune is not performed. It produces a relatively high level of performance in 90% of motion applications. Most of the time, there is no need to perform an auto-tune procedure or further optimize gain settings.

<!-- image -->

Try this method before executing Auto-tune.

Follow these steps to configure the drive for high performance right out of the box. This procedure uses load observer to automatically account for the unknown load. As a result, you must be familiar with creating an axis in the Logix Designer application and accessing drive IDN parameters.

1. Create a new axis with type AXIS\_SERVO\_DRIVE.
2. If you need more information to create a new axis, refer to Configure the Kinetix 6200 and Kinetix 6500 Drive Modules on page 146 .
2. Click the Drive/Motor tab in the Axis Properties dialog box and add a motor.

<!-- image -->

If you need more information to add a motor, refer to Configure Axis Properties on page 151 .

3. Click the Gains tab in the Axis Properties dialog box.
2. The current Velocity Proportional Gain (Initial Kvp) value is used to recalculate other gain values.
4. Make the following calculations:
- a. Load Observer Bandwidth: Kop = Velocity Proportional Gain x 2.56 b. Velocity Loop Bandwidth: Kvp = Kop/4

<!-- image -->

- c. Position Loop Bandwidth: Kpp = Kvp/4
5. Configure these settings and values on the Gains tab.
- a. Position Proportional Gain = Kpp
- b. Velocity Proportional Gain = Kvp
- c. Velocity Feedforward Gain = 100%
- d. Integrator Hold = Disabled
6. Configure these IDN parameter values.
- a. IDN P-431 = 2 (load observer with velocity estimate)
- b. IDN P-432 = Kop
- c. IDN P-433 = 0
- d. IDN P-065 = 1
7. Click the Output tab in the Axis Properties dialog box and verify these settings.
- a. Load Inertia Ratio = 0
- b. Enable Low-pass Output Filter = Unchecked

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

8. If required, reduce the Maximum Acceleration and Maximum Deceleration values to meet application requirements and protect the drive and motor from overload.

Acceleration limits, by default, are set to their maximum value, providing the best performance for a Load Inertia Ratio of zero. However, your application loads the motor and it will not be able to accelerate as fast.

<!-- image -->

9. Refer to Compensate for High Frequency Resonances on page 266, to tune-out resonant frequencies.

## Auto-tune Gain Settings

This procedure explains how to configure the load observer feature after running Auto-tune. This method also works for any existing set of gains where the Load Inertia Ratio is known or manually calculated, for example, when the Load Inertia Ratio &gt; 0.

<!-- image -->

Try the out-of-box method before executing Auto-tune. Refer to Out-of-Box Gain Settings on page 258 .

1. Click the Tune tab in the Axis Properties dialog box and perform Autotune.

For variable inertia loads, perform Auto-tune at the point of lowest mechanical inertia. If you manually calculate the Load Inertia Ratio, use the minimum load inertia.

2. Click the Output tab in the Axis Properties dialog box and verify that the Load Inertia Ratio &gt; 0.
3. Click the Gains tab in the Axis Properties dialog box.

<!-- image -->

The current Position and Velocity gain values are used to recalculate other gain values.

<!-- image -->

4. Determine if the mechanical load connected to the motor is rigid or compliant.
- Rigid systems typically involve high-performance load mechanics that are tightly coupled directly to the motor shaft and there is no lost motion. Refer to Rigid Mechanical Loads on page 261, for rigid applications.
- Everything else is compliant, including systems with belts and pulleys, long shafts, short shafts with heavy loads, and couplings and gearboxes with backlash and/or lost motion. Refer to Compliant Mechanical Loads on page 262, for compliant applications.

## Rigid Mechanical Loads

Follow these steps if the load is rigid.

1. Calculate the Load Observer Bandwidth. Load Observer Bandwidth: Kop = Velocity Proportional Gain
2. Configure these IDN parameter values.
- a. IDN P-431 = 2 (Load Observer with Velocity Estimate)
- b. IDN P-432 = Kop
- c. IDN P-433 = 0
- d. IDN P-065 = 1
3. If the Low-pass Output Filter is enabled, verify that the Low-pass Output Filter Bandwidth is  the Velocity Proportional Gain x 2/(2pi).
8. Sercos IDN P-065 has an impact on how the Low-pass Output Filter functions. Refer to Torque Low-pass Filter Bandwidth on page 257 for more information.
4. Refer to Compensate for High Frequency Resonances on page 266, to tune-out resonant frequencies.

<!-- image -->

<!-- image -->

## Compliant Mechanical Loads

The compliant setting reduces all of the gains by a factor of (Load Inertia Ratio +1) and then calculates the Load Observer Bandwidth. Typically, this reduction is too conservative, making the loop response sluggish and the error too large. However, it does assure stability.

Follow these steps if the load is compliant.

1. Make the following calculations to de-tune all gains by a factor of the (Load Inertia Ratio + 1):
- a. Position Loop Bandwidth: Kpp = Position Proportional Gain/(Load Inertia Ratio + 1)
- b. Position Integral Bandwidth: Kpi = Position Integral Gain/(Load Inertia Ratio + 1) 2
- c. Velocity Loop Bandwidth: Kvp = Velocity Proportional Gain/(Load Inertia Ratio + 1)
- d. Velocity Integral Bandwidth: 2

Kvi = Velocity Integral Gain/(Load Inertia Ratio + 1)

- e. Load Observer Bandwidth: Kop = Kvp
2. Configure these settings and values on the Gains tab.
- a. Set the Position Proportional Gain = Kpp
- b. Position Integral gain = Kpi
- c. Velocity Proportional Gain = Kvp
- d. Velocity Integral Gain = Kvi

<!-- image -->

<!-- image -->

To manually increase the gains by some factor to optimize the response, refer to Manual Tuning for Further Optimization on page 263 .

3. Configure these IDN parameter values.
- a. IDN P-431 = 2 (Load Observer with Velocity Estimate)
- b. IDN P-432 = Kop
- c. IDN P-433 = 0
- d. IDN P-065 = 1
4. If the Low-pass Output Filter is enabled, verify that the Low-pass Output Filter Bandwidth  Velocity Proportional Gain x 5/(2pi).
7. Sercos IDN P-065 has an impact on how the Low-pass Output Filter functions. Refer to Torque Low-pass Filter Bandwidth on page 257 for more information.
5. Refer to Compensate for High Frequency Resonances on page 266, to tune-out resonant frequencies.

<!-- image -->

## Tuning Mode Summary

This table summarizes the primary difference between the two tuning modes.

Table 128 - Tuning Mode Comparison

| Tuning Mode Description                           |                                                                               |
|---------------------------------------------------|-------------------------------------------------------------------------------|
| Out-of-box or unknown load Load Inertia Ratio = 0 | Load Observer Bandwidth Kop = 4 times the new Velocity Proportional Gain, Kvp |
| Auto-tuning or known load Load Inertia Ratio > 0  | Load Observer Bandwidth = Velocity Proportional Gain                          |

## Manual Tuning for Further Optimization

The out-of-box and auto-tune rigid methods achieve relatively high performance. However, the manual tuning method can help to optimize performance for the auto-tune compliant method, or if every ounce of performance is required. It involves incrementally increasing controller gains to the point of marginal stability, then backing them off by a given percentage. Typical ranges for various gains are also given to provide guidelines.

Follow these steps to manually tune your drive.

1. Select a factor (N) that you can incrementally increase the gains by in an iterative process, for example, 1.5&gt;N&gt;2.
2. Create a trend to monitor Torque Reference.
3. Manually tune the velocity loop.
- a. Make note of the Position and Feedforward Gains. You must change them temporarily to isolate the velocity loop and later restore them to the original values.

## b. Isolate the velocity loop.

- Zero out the Position Proportional Gain, Position Integral Gain, and Acceleration Feedforward Gain
- Set the Velocity Feedforward = 100
- c. While Jogging the axis and monitoring the Torque Reference trend, incrementally increase the following gains simultaneously and stop when the Torque Reference begins to become oscillatory or unstable:
- Low-pass Output Filter Bandwidth = Low-pass Output Filter Bandwidth x N
- Load Observer Proportional Gain = Load Observer Proportional Gain x N
- Load Observer Integral Gain = Load Observer Integral Gain x N
- Velocity Proportional Gain = Velocity Proportional Gain x N
- Velocity Integral Gain = Velocity Integral Gain x N 2
- d. Decrease the gains by using the previous equations with N = 0.5. A typical range of values for various integral gains are given:
- 0  Load Observer Integral Gain  Load Observer Proportional Gain/4
- 0  Velocity Integral Gain  Velocity Proportional Gain 2 /4000
- e. If the Low-pass Output Filter is enabled, a typical range of values for the Low-pass Output Filter Bandwidth are given:
- Rigid: Low-pass Output Filter Bandwidth  Velocity Proportional Gain x 2/(2pi)
- Compliant: Low-pass Output Filter Bandwidth  Velocity Proportional Gain x 5/(2pi)
4. Manually tune the position loop.
- a. Restore the Position and Feedforward Gains to the original values to re-enable the position loop.
- b. While Jogging the axis and monitoring the Torque Reference trend, incrementally increase the following gains simultaneously and stop when the Torque Reference begins to become oscillatory or unstable:
- Position Proportional Gain = Position Proportional Gain x N
- Position Integral Gain = Position Integral Gain x N 2
- c. Decrease the gains by using the previous equations with an N = 0.5. A typical range of values for the Position Integral Gain is given:
- 0  Position Integral Gain  Position Proportional Gain 2 /4000

## Setting Gains with Sercos IDN Write Messages

Write the Load Observer Configuration attribute and the Load Observer gains each time the drive gets initialized after applying power.

The Sercos IDN write instruction is accomplished by using RSLogix 5000® software or the Logix Designer application. Refer to Appendix F on page 289 for more information on changing IDN parameter values by using this method.

1. Upon initialization of the drive, read the INT value of the configuration of the drive at Sercos IDN P:0:431.
2. If the value is not what you want, latch it and write the new value back to the drive at the same address, again as type INT.

<!-- image -->

<!-- image -->

## Compensate for High Frequency Resonances

3. Verify the change with another Sercos IDN Read Message from IDN P:0:431.

<!-- image -->

<!-- image -->

The procedure for setting each of the gains is similar.

Approximately 15% of all motion applications exhibit a high-frequency resonance that is apparent by an audible high-frequency squealing of the load mechanics.

Follow these steps to identify and reduce the presence of high-frequency resonances.

1. Perform the following move sequence by using Motion Direct Commands:
- a. Enable the axis with an MSO
- b. Slowly jog the axis with an MAJ
- c. Stop the axis with an MAS
- d. Disable the axis with a MSO

## IMPORTANT

Sometimes an audible resonance is heard before the axis is jogged, making the MAJ and MAS unnecessary.

2. Determine if an audible high-frequency resonance exists in your motion application.
- If an audible high frequency resonance is not present during the move sequence, skip the remaining steps and tuning is complete.
- If an audible high frequency resonance is present during the move sequence, use an FFT smart phone or tablet application to identify the dominant resonant frequencies.

<!-- image -->

3. Click the Output tab in the Axis Properties dialog box.
- a. Check Enable Notch Filter Frequency and set the Notch Filter Frequency to the resonant frequency with the largest amplitude.
- b. If multiple resonances have nearly the same amplitude, set the Notch Filter Frequency to the lowest resonant frequency.
- c. If the problem persists, also check Enable Low-pass Output Filter and set the Low-pass Output Filter Frequency to the next largest resonant frequency.
- d. Click OK.

<!-- image -->

## Notes:

## Overview

## Web Server Interface

The Kinetix® 6200 and Kinetix 6500 drives support a web server interface for common status reporting and network configuration attributes. The web server also supports the safety configuration for 2094-SE02F-M00-S1 and 2094-EN02D-M01-S1 control modules.

| Topic Page                           |
|--------------------------------------|
| Overview 269                         |
| Home Category 271                    |
| Diagnostics Category 272             |
| Fault Logs Category 282              |
| Data Logs Category 283               |
| Administrative Settings Category 284 |
| Browse Power Rail Category 284       |
| Safety Category 285                  |

The web server interface is accessed through an Ethernet connection between the drive and your personal computer. The drive has a private IP address, with the final octet determined by the drive node address or Ethernet address (configured in the Logix Designer application&gt;Axis Properties). For example, with http://192.168.1.1, the IAM power module node address is 001.

Refer to Chapter 6 (for Sercos drives) or Chapter 7 (for EtherNet/IP™ drives) for more information on setting the node address of your Kinetix 6200 servo drive or Ethernet address of your Kinetix 6500 servo drive.

The web server interface provides a Home page that displays the current status of the safety configuration and buttons to lock/unlock the configuration, save the configuration to a file, apply a specific configuration, and set an optional password. Though optional, you can configure a password to help protect the system configuration from unauthorized modifications. Use the Change Safety Password page to change the password.

<!-- image -->

## Web Server Interface Categories

Table 129 describes how the categories are organized on the web server interface.

Table 129 - Web Server Interface Categories

| Main Categories Sub-categories Page         |                            |
|---------------------------------------------|----------------------------|
| Home 271                                    | Home 271                   |
| Diagnostics                                 | Drive Indicators 272       |
| Diagnostics                                 | Drive Information 273      |
| Diagnostics                                 | Motor Information 274      |
| Diagnostics                                 | Network Settings 275       |
| Diagnostics                                 | Ethernet Statistics 276    |
| Diagnostics                                 | CIP Statistics 277         |
| Diagnostics                                 | Encoder Statistics 278     |
| Diagnostics                                 | Peak Detection 279         |
| Diagnostics                                 | Monitor Signals 280        |
| Diagnostics                                 | Oscilloscope 281           |
| Fault logs                                  | Fault Log 282              |
| Fault logs                                  | Configure Fault Log 282    |
|                                             | Data logs Temperatures 283 |
| Administrative settings Device Identity 284 |                            |
| Browse power rail 284                       | Browse power rail 284      |
| Safety configuration  (1)                   | Safety Main 285            |
| Safety configuration  (1)                   | Safety Configuration 286   |
| Safety configuration  (1)                   | Configuration Summary 287  |
| Safety configuration  (1)                   | Change Safety Password 288 |

## Home Category

## Table 130 - Home Features

| Field Name Description                                                                                                                                                                           | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                                                                                                                                           | -S0 -S1 -S0 -S1                   |                                   |
| Device Name User-defined information from the device identity page. – – X X                                                                                                                      |                                   |                                   |
| Device Description User-defined information from the device identity page. – – X X                                                                                                               |                                   |                                   |
| Device Location User-defined information from the device identity page. – – X X                                                                                                                  |                                   |                                   |
| Ethernet MAC Address Media Access Control (MAC) hardware address X X X X                                                                                                                         |                                   |                                   |
| Ethernet IP Address IP address X X X X                                                                                                                                                           |                                   |                                   |
| SERCOS Node Address SERCOS node address X X – –                                                                                                                                                  |                                   |                                   |
| SERCOS Phase 0, 1, 2, 3, or 4 X X – –                                                                                                                                                            |                                   |                                   |
| Product Revision Complete firmware revision X X X X                                                                                                                                              |                                   |                                   |
| Control Module Control module catalog number and series X X X X                                                                                                                                  |                                   |                                   |
| Control Module Serial Number Control module serial number X X X X                                                                                                                                |                                   |                                   |
| Power Module Power module catalog number and series X X X X                                                                                                                                      |                                   |                                   |
| Power Module Serial Number Power module serial number X X X X                                                                                                                                    |                                   |                                   |
| Status Aborting, firmware update, Safe Torque Off, safe limited speed, self test, connecting, configuring, syncing, pre-charge, shutdown, stopped, starting, running, testing. stopping, faulted | XXXX                              |                                   |
| Safety Signature ID Advanced safety signature identifier – X – X                                                                                                                                 |                                   |                                   |
| Safety Lock Status Advanced safety lock status – X – X                                                                                                                                           |                                   |                                   |
| Uptime Cumulative time with control power applied X X X X                                                                                                                                        |                                   |                                   |

From the Home tab, you can monitor many of the drive characteristics.

## Figure 118 - Home Tab

<!-- image -->

## Diagnostics Category

Table 131 - Drive Indicators Features

| Field Name Description                                                                                   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|----------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                                                   | -S0 -S1 -S0 -S1                   |                                   |
| Dot Matrix Display String that matches the dot matrix display identically. X X X X                       |                                   |                                   |
| COMM Status State of the COMM status indicator on SERCOS models. X X – –                                 |                                   |                                   |
| DRIVE Status State of the DRIVE status indicator on SERCOS models. X X – –                               |                                   |                                   |
| Module Status State of the MODULE status indicator on EtherNet/IP models. – – X X                        |                                   |                                   |
| Network Status State of the NETWORK status indicator on EtherNet/IP models. – – X X                      |                                   |                                   |
| SAFETY LOCK Status State of the SAFETY LOCK status indicator on Safe Speed Monitor (-S1) models. – X – X |                                   |                                   |
| DC BUS Status State of the DC BUS status indicator. X X X X                                              |                                   |                                   |

The Diagnostics category includes several tabs for monitoring drive, motor, network, encoder, and signal status.

## Drive Indicators

From the Drv. Ind tab, you can monitor the control module status indicators.

Figure 119 - Diagnostics&gt;Drv. Ind Tab

<!-- image -->

Table 132 - Drive Information Features

| Field Name Description                                                                        | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-----------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                                        | -S0 -S1 -S0 -S1                   |                                   |
| Main Power Cycles Cumulative number of main power cycles X X X X                              |                                   |                                   |
| Control Power Cycles Cumulative number of control power cycles X X X X                        |                                   |                                   |
| Cumulative Time with Control Power Applied Cumulative time with control power applied X X X X |                                   |                                   |
| Elapsed Time since Last Control Power Cycle Time since control power was last applied X X X X |                                   |                                   |
| Cumulative Time with Main Power Applied Cumulative time with main power applied X X X X       |                                   |                                   |
| Elapsed Time since Last Main Power Cycle Time since main power was last applied X X X X       |                                   |                                   |
| Cumulative Time with Power Stage Enabled Cumulative time with power stage enabled X X X X     |                                   |                                   |
| Elapsed Time with Power Stage Enabled Time since power stage was last enabled X X X X         |                                   |                                   |
| Cumulative Energy Usage Cumulative amount of energy consumed by the inverter X X X X          |                                   |                                   |
| Motor Brake Relay Cycles Cumulative number of motor brake relay cycles X X X X                |                                   |                                   |
| Control Module Date Code Manufacturing date code X X X X                                      |                                   |                                   |
| Power Module Date Code Manufacturing date code X X X X                                        |                                   |                                   |
| Safety Firmware Version Safety firmware revision X X X X                                      |                                   |                                   |
| KCL Version KCL build X X X X                                                                 |                                   |                                   |
| Processor Board Hardware Version PCBA part number and revision X X X X                        |                                   |                                   |
| I/O Board Hardware Version PCBA part number and revision X X X X                              |                                   |                                   |
| Power Module Part Number / Revision Final assembly part number and revision X X X X           |                                   |                                   |
| Control Module Part Number / Revision Final assembly part number and revision X X X X         |                                   |                                   |

## Drive Information

From the Drv. Info tab, you can monitor data that can assist with troubleshooting drive faults.

Figure 120 - Diagnostics&gt;Drv. Info Tab

<!-- image -->

Table 133 - Motor Information Features

| Field Name Description                                                                                                        | SERCOS (2094-SE02F-M00-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-------------------------------------------------------------------------------------------------------------------------------|------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                                                                        |                              | -S0 -S1 -S0 -S1                   |                                   |
| Motor Catalog Number Motor catalog number and series from encoder-based motor BLOB. X X X X                                   |                              |                                   |                                   |
| Motor Serial Number Motor serial number from encoder-based motor BLOB. X X X X                                                |                              |                                   |                                   |
| Motor Manufacturing Date Code Manufacturing date code from encoder-based motor BLOB. X X X X                                  |                              |                                   |                                   |
| Cumulative Motor Revolutions  Cumulative number of motor revolutions since last motor catalog number or serial number change. |                              | XXXX                              |                                   |

## Motor Information

From the Mot. Info tab, you can monitor data that can assist with troubleshooting drive faults.

Figure 121 - Diagnostics&gt;Mtr. InfoTab

<!-- image -->

Table 134 - Network Settings Features

| Field Name Description                                                           | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|----------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                           | -S0 -S1 -S0 -S1                   |                                   |
| Ethernet Address (MAC) Media Access Control (MAC) hardware address X X X X       |                                   |                                   |
| IP Address IP address of the drive X X X X                                       |                                   |                                   |
| Subnet Mask Subnet mask X X X X                                                  |                                   |                                   |
| Default Gateway IP address of the default gateway X X X X                        |                                   |                                   |
| Primary Name Server IP address of the primary name server X X X X                |                                   |                                   |
| Secondary Name Server IP address of the secondary name server X X X X            |                                   |                                   |
| Default Domain Name Name representing the IP resource. X X X X                   |                                   |                                   |
| Host Name Name representing the host encapsulated in the domain. X X X X         |                                   |                                   |
| Name Resolution Mechanism used for name resolution. X X X X                      |                                   |                                   |
| SMTP Server IP address of the SMTP server X X X X                                |                                   |                                   |
| Obtain Network Configuration IP settings Static or Automatic. X X X X            |                                   |                                   |
| Autonegotiate Status Negotiation status bits of the Ethernet link object X X X X |                                   |                                   |
| Port Speed 10 Mbps or 100 Mbps X X X X                                           |                                   |                                   |
| Duplex Mode Full duplex or half duplex X X X X                                   |                                   |                                   |

## Network Settings

From the Net. Set tab, you can monitor the EtherNet/IP network settings.

Figure 122 - Diagnostics&gt;Net. Set Tab

<!-- image -->

## Ethernet Statistics

The Enet. Stat tab displays counters that assist with troubleshooting EtherNet/IP network problems. The interface counters reflect the state of the packets received and transmitted to the local MAC address, but do not include packets that traverse the switch, destined for another device.

Figure 123 - Diagnostics&gt;Enet. Stat Tab

Table 135 - Ethernet Statistics Attributes

<!-- image -->

Speed Speed

Duplex Duplex

Autonegotiate Status Autonegotiate Status

Alignment Errors Alignment Errors

FCS Errors FCS Errors

Single Collisions Single Collisions

Multiple Collisions Multiple Collisions

Excessive Collisions Excessive Collisions

Frame Too Long Frame Too Long

In Octets In Octets

In Ucast Packets In Ucast Packets

In NUcast Packets In NUcast Packets

In Errors In Errors

Out Octets Out Octets

Out Ucast Packets Out Ucast Packets

Out NUcast Packets Out NUcast Packets

Out Errors Out Errors

<!-- image -->

|                                  | Field Name Port 1 Attributes   |
|----------------------------------|--------------------------------|
| Ethernet                         |                                |
| Media Counters                   |                                |
| Interface Counters               |                                |
| Storm Protection (1) Diagnostics | Broadcast Storms Observed      |
| Storm Protection (1) Diagnostics | Multicast Storms Observed      |
| Interface Counters               |                                |
| Interface Counters               |                                |
| Interface Counters               |                                |
| Interface Counters               |                                |
| Interface Counters               |                                |

| Port 2 Attributes (2)   |
|-------------------------|

Table 136 - CIP Statistics Features

| Field Name Description                                                   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|--------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                   | -S0 -S1 -S0 -S1                   |                                   |
| Current TCP Connections Current TCP connection – – X X                   |                                   |                                   |
| TCP Connection Limit TCP connection limit – – X X                        |                                   |                                   |
| Maximum Observed Number of maximum observed connections – – X X          |                                   |                                   |
| Current CIP™ Connections Current CIP connections – – X X                 |                                   |                                   |
| CIP Connection Limit CIP connection limit – – X X                        |                                   |                                   |
| Max. Connections Observed Number of maximum observed connections – – X X |                                   |                                   |
| Connection Opens Total connection opened since powerup – – X X           |                                   |                                   |
| Open Errors Total errors since powerup – – X X                           |                                   |                                   |
| Connection Closes Total connection closed since powerup – – X X          |                                   |                                   |
| Close Errors Total connection closed since powerup – – X X               |                                   |                                   |
| Connection Timeouts Connection timeout since powerup – – X X             |                                   |                                   |

## CIP Statistics

The CIP. Stat tab displays counters that assist with troubleshooting EtherNet/IP network problems.

Figure 124 - Diagnostics&gt;CIP. Stat Tab

<!-- image -->

Table 137 - Encoder Statistics Features

| Field Name Description                                                                                                                              | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| Field Name Description                                                                                                                              | -S0 -S1 -S0 -S1                   |                                   |
| Rejected LF Motor Enc Pulses, Ch. A Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                        |                                   |                                   |
| Rejected HF Motor Enc Pulses, Ch. A Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                        |                                   |                                   |
| Rejected LF Motor Enc Pulses, Ch. B Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                        |                                   |                                   |
| Rejected HF Motor Enc Pulses, Ch. B Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                        |                                   |                                   |
| Rejected LF Aux Enc Pulses, Ch. A Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                          |                                   |                                   |
| Rejected HF Aux Enc Pulses, Ch. A Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                          |                                   |                                   |
| Rejected LF Aux Enc Pulses, Ch. B Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                          |                                   |                                   |
| Rejected HF Aux Enc Pulses, Ch. B Cumulative number of rejected encoder pulses since the last control power cycle. X X X X                          |                                   |                                   |
| Motor Encoder Line Loss Current state of the motor encoder line-loss algorithm, in units of % of trip level. X X X X                                |                                   |                                   |
| Auxiliary Encoder Line Loss Current state of the auxiliary encoder line-loss algorithm, in units of % of trip level. X X X X                        |                                   |                                   |
| Motor Encoder Missed Communication Cycles Cumulative number of missed motor-encoder communication responses since the last control power cycle.     | XXXX                              |                                   |
| Auxiliary Encoder Missed Communication Cycles Cumulative number of missed motor-encoder communication responses since the last control power cycle. | XXXX                              |                                   |

## Encoder Statistics

The Enc. Stat tab displays counters that assist with troubleshooting motor encoder problems.

Figure 125 - Diagnostics&gt;Enc. Stat Tab

<!-- image -->

Table 138 - Peak Detection Features

|                               | Field Name Description                                                                           | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------|
|                               | Field Name Description                                                                           | -S0 -S1 -S0 -S1                   |                                   |
| DC Bus Voltage  (1)           | Maximum value of the DC-bus voltage since control power was last applied. X X X X                |                                   |                                   |
|                               | Control Module Temperature Maximum value of the control module temperature. X X X X              |                                   |                                   |
|                               | Power Module Temperature Maximum value of the power module temperature. X X X X                  |                                   |                                   |
| Motor Current, Positive  (1)  | Maximum positive value of the motor current since control power was last applied. X X X X        |                                   |                                   |
| Motor Current, Negative  (1)  | Minimum negative value of the motor current since control power was last applied. X X X X        |                                   |                                   |
| Motor Current, Foldback  (1)  | True if the motor current has experienced foldback since control power was last applied. X X X X |                                   |                                   |
| Position Error, Positive  (1) | Maximum positive value of the position error since control power was last applied. X X X X       |                                   |                                   |
| Position Error, Negative  (1) | Minimum negative value of the position error since control power was last applied. X X X X       |                                   |                                   |

## Peak Detection

The Peak. Det tab displays attributes that have integrated peak detection for troubleshooting. All peaks are measured with 5 ms resolution.

Figure 126 - Diagnostics&gt;Peak. Det Tab

<!-- image -->

## Monitor Signals

The Mon. Sig tab displays dynamic attributes that can assist field troubleshooting.

Figure 127 - Diagnostics&gt;Mon. Sig Tab

Table 139 - Dynamic Attributes

<!-- image -->

Motion Attributes Safety Inputs

Position Command SS Input 0

Position feedback SS Input 1

Velocity Command SS Input 2

Velocity feedback SS Input 3

Current Command SLS Input 0

Current feedback SLS Input 1

Commutation angle DM Input 0

Bus voltage DM Input 1

LM Input 0

Encoder temperature LM Input 1

Control module temperature ESM Input 0

Power module temperature ESM Input 1

Converter duty cycle Reset Input

Safety Outputs

Motor duty cycle SS Output 0

SS Output 1

Input 1 SLS Output 0

Input 2 SLS Output 1

Input 3 DC Output 0

Input 4 DC Output 1

| Motion Attributes Safety Inputs        |
|----------------------------------------|
| Position Command SS Input 0            |
| Position feedback SS Input 1           |
| Velocity Command SS Input 2            |
| Velocity feedback SS Input 3           |
| Current Command SLS Input 0            |
| Current feedback SLS Input 1           |
| Commutation angle DM Input 0           |
| Bus voltage DM Input 1                 |
| Temperature Attributes  LM Input 0     |
| Encoder temperature LM Input 1         |
| Control module temperature ESM Input 0 |
| Power module temperature ESM Input 1   |
| Converter duty cycle Reset Input       |
| Inverter duty cycle  Safety Outputs    |
| Motor duty cycle SS Output 0           |
| Digital Inputs  SS Output 1            |
| Input 1 SLS Output 0                   |
| Input 2 SLS Output 1                   |
| Input 3 DC Output 0                    |
| Input 4 DC Output 1                    |

## Oscilloscope

The Scope tab provides a data collection mechanism for viewing up to four channels of dynamic attribute data collected synchronously. The triggering methods are positive edge, negative edge, and immediate, with programmable trigger thresholds. The capture can be done in either single-shot or continuous mode. Click Save to export the window to a spreadsheet. The trigger and collected data attributes include the following

Figure 128 - Diagnostics&gt;Scope Tab

Table 140 - Trigger and Collected Data Attributes

<!-- image -->

Motion Attributes Digital Inputs

Position Command Input 1

Position feedback Input 2

Velocity Command Input 3

Velocity feedback Input 4

| Current Command   |
|-------------------|
| Current feedback  |
| Commutation angle |
| Bus voltage       |

## Fault Logs Category

Table 141 - Fault Log Features

|       | Field Name Description                                                                                                                                                                                                                                                                                       | SERCOS (2094-SE02F-M00-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-----------------------------------|-----------------------------------|
|       |                                                                                                                                                                                                                                                                                                              |                              | -S0 -S1 -S0 -S1                   |                                   |
| Fault | A 20-sample non-volatile fault log with programmable 8-channel variable tracing. Each log entry includes the following: • Fault code and sub-code • 4 channels of variables collected at the servo update rate • 4 channels collected at a programmable sample rate • CIP time stamp  (1) • Local time stamp |                              | XXXX                              |                                   |

## Configure Fault Log

The Configure Fault Log tab lets you select channels to capture during a fault that are listed in the fault log. You can select channels for:

- Servo Update and User Rate Log
- Snap Shot Log

A maximum of four channels can be selected for each mode. Once you have selected the channels, click Apply to save the settings to the drive. These settings are persistent over power cycles.

Figure 130 - Fault Logs&gt;Configure Fault Log Tab

<!-- image -->

The Fault Log tab provides access to faults logged by the drive for future retrieval. Each log in the list is a link and you can view the details. You can configure individual channels in the fault log via the Configure Fault Log page. All logs can be exported separately into spreadsheets.

Figure 129 - Fault Logs&gt;Fault Log Tab

<!-- image -->

## Data Logs Category

Table 142 - Temperatures Features

|                             | Field Name Description                                                                                                                                                                            | SERCOS (2094-SE02F-M00-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-----------------------------------|-----------------------------------|
|                             | Field Name Description                                                                                                                                                                            |                              | -S0 -S1 -S0 -S1                   |                                   |
|                             | Control Module Temperature A 2048-sample log of control module temperature sampled at 1-minute intervals. X X X X                                                                                 |                              |                                   |                                   |
|                             | Power Module Temperature A 2048-sample log of power module temperature sampled at 1-minute intervals. X X X X                                                                                     |                              |                                   |                                   |
|                             | Encoder Temperature A 2048-sample log of encoder temperature sampled at 1-minute intervals. X X X X                                                                                               |                              |                                   |                                   |
| Firmware Change             | A 16-sample non-volatile log of firmware updates. Each log entry stores the firmware version, CIP time stamp, and local time stamp.                                                               |                              | XXXX                              |                                   |
| Safety Configuration Change | A 16-sample non-volatile log of safety configuration changes. Each log entry stores the signature, CIP time stamp, and local time stamp.                                                          |                              | –X–X                              |                                   |
| Motor Connection            | An 8-sample log of motor catalog number or serial number changes. Each log entry stores the motor catalog number, motor serial number, CIP time stamp, and local time stamp.                      |                              | XXXX                              |                                   |
| Main Power Cycling          | A 16-sample non-volatile log of main power cycle events. Each log entry stores the type (on or off), CIP time stamp, and local time stamp.                                                        |                              | XXXX                              |                                   |
| Power Module Connection     | An 8-sample non-volatile log of power module catalog number or serial number changes. Each log entry stores the power module catalog number, serial number, CIP time stamp, and local time stamp. |                              | XXXX                              |                                   |

The Data Logs pages provides access to data that is logged by the drive for future retrieval.

## Temperatures

The Temperatures tab reports temperatures from the control module, power module, and encoder.

Figure 131 - Data Logs&gt;Temperatures Tab

<!-- image -->

## Administrative Settings Category

Table 143 - Device Identity Features

| Field Name Description                                              | SERCOS (2094-SE02F-M00-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|---------------------------------------------------------------------|------------------------------|-----------------------------------|-----------------------------------|
|                                                                     |                              | -S0 -S1 -S0 -S1                   |                                   |
| Device Identity A non-volatile identification of the drive. – – X X |                              |                                   |                                   |

Browse Power Rail Category When connected to an integrated axis module (IAM), you are able to browse the power rail and see the axis modules and their respective location (slot) on the power rail. Click the link and you are directed to the specific axis module web page.

IMPORTANT

The axis modules must be connected to the EtherNet/IP network for the link to work.

Figure 133 - Power Rail Tab

<!-- image -->

Table 144 - Power Rail Features

| Field Name Description                                                                       | SERCOS (2094-SE02F-M00-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|----------------------------------------------------------------------------------------------|------------------------------|-----------------------------------|-----------------------------------|
|                                                                                              |                              | -S0 -S1 -S0 -S1                   |                                   |
| Browse Power Rail Link to all the AM modules that are connected to the same network. X X X X |                              |                                   |                                   |

From the Administrative Settings web pages, you can update the drive identification settings.

The Device Identity tab lets you update the device description and name that appears on the Home page. By default, all the fields are blank on first power up (or if they have never been updated). Click Apply to save the values to the drive.

Figure 132 - Administrative Settings&gt;Device Configuration&gt;Device Identity Tab

<!-- image -->

## Safety Category

Table 145 - Safety Main Features

|                 | Field Name Description                                                                                                                                                                                                                                                                                                                                             | SERCOS (2094-SE02F-M00-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   | EtherNet/IP (2094-EN02D-M01-Sx)   |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-----------------------------------|-----------------------------------|
|                 | Field Name Description                                                                                                                                                                                                                                                                                                                                             |                              | -S0 -S1 -S0 -S1                   |                                   |
| Save File       | Click Safe File to save a data file containing the safety configuration information. This file can be used to configure additional drives with the same safety configuration.                                                                                                                                                                                      |                              | –X–X                              |                                   |
| Apply File      | Click Apply File to directly apply safety configuration settings from a previously saved file to the drive's safety circuitry. The safety circuitry must be unlocked before a safety configuration can be applied.                                                                                                                                                 |                              | –X–X                              |                                   |
| Refresh         | Click Refresh to update the page after reading the safety configuration signature from the safety processor. This makes sure that the page does not show a stale value that was cached when the web page was first opened. Depending on the web browser in use, you might have to click the Refresh the very first time this page is opened to populate to values. |                              | –X–X                              |                                   |
| Lock and Unlock | Click Lock or Unlock to change the lock status of the safety circuitry, prompting for the Lock/Unlock password, if necessary. The safety circuitry must be unlocked before a safety configuration can be applied.                                                                                                                                                  |                              | –X–X                              |                                   |

This appendix provides an overview of the safety configuration web pages. For information on how to configure the safety functions, refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Multi-axis Servo Drives Safety Reference Manual, publication 2094-RM001 .

## Safety Main

The Safety Main tab lets you lock or unlock the safety configuration, save the configuration to a file, apply a safety configuration, and enter a password. The default [Safety Lock Status] parameter setting is Unlock.

Figure 134 - Safety Main Tab

<!-- image -->

## Safety Configuration

The 2094-SE02F-M00-S1 and 2094-EN02D-M01-S1 control modules require a safety configuration. For an example of how to configure the safety functions, refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Multi-axis Servo Drives Safety Reference Manual, publication 2094-RM001 .

Figure 135 - Safety Tab

<!-- image -->

The Java-script running in the web browser prepares an HTML request containing the safety configuration assembly, the safety configuration ID, and the date and time. If the drive is enabled when it receives this request, a response is sent indicating that the drive is enabled, and must be disabled to apply the safety configuration. The web server puts the drive in an inhibit state while applying the safety configuration. While inhibited, the drive cannot be enabled by the controller. The web server releases the inhibit after applying the safety configuration. For this sequence to complete successfully, you must first make sure that the safety circuitry is unlocked. If it is locked, the configuration attempt fails, and an appropriate response is generated.

The web server creates a data file containing the configuration settings within the safety circuitry, including the Safety Configuration ID, and the date and time it was applied. This file can be downloaded from the web server to your personal computer by using a standard browser file-download mechanism. The web server can also upload a previously saved file, and apply the configuration settings it contains to the safety circuitry.

When you apply a safety configuration by uploading a previously saved file, the web server recalculates the Safety Configuration ID based on the configuration data in the file. This calculated ID is compared to the original Safety Configuration ID stored in the file, and if they do not match, the web server reports an error. A mismatch could be caused by manually editing the configuration file, which is not allowed. After the configuration is successfully applied from the file, the drive redisplays the main web page, with the safety signature information defined by the file. The date and time portions of the safety signature are the same date and time as the original drive that was used to generate the configuration file.

## Configuration Summary

Use the Configuration Summary tab to verify the configuration or manually compare the configuration with a previously saved or printed summary report. The reports can be saved or printed from within the Configuration Summary page.

For more information on how to configure the safety functions, refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Multi-axis Servo Drives Safety Reference Manual, publication 2094-RM001 .

Figure 136 - Configuration Summary Tab

<!-- image -->

## Change Safety Password

From the Change Safety Password page you can send a request to the web server to change the safety password. You must provide the old password and the new password. The web page requires you to enter the new password twice, and compares the two entries to minimize the risk of setting the password to something other than what you intended.

Figure 137 - Change Safety Password Tab

<!-- image -->

For more information on how to configure the safety functions, refer to the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Multi-axis Servo Drives Safety Reference Manual, publication 2094-RM001 .

## Before You Begin

<!-- image -->

## Change Kinetix 6200 Default IDN Parameter Values

This appendix provides a procedure, specific to the Kinetix® 6200 (Sercos) drive systems, for changing IDN parameter values to non-default values when your application does not match the default configuration. The procedure also applies when one or more Kinetix 6000M IDM systems are present.

| Topic Page                      |
|---------------------------------|
| Before You Begin 289            |
| Change IDN Parameter Values 290 |

The Logix 5000™ processor contains a motion planner that sends real-time and non real-time data to the drive. This drive communication is performed via a set of Sercos interface telegrams. Each telegram has an identification or Ident (IDN) number. All parametric data, such as scaling and loop gains, and realtime loop closure information is configured this way.

## Table 146 - IDN Instruction Format in the IEC Standard Document

| IDN Number   | Name                 | Name                                     | Name                     | Name                 |
|--------------|----------------------|------------------------------------------|--------------------------|----------------------|
| IDN Number   | Function/Description | Function/Description                     | Function/Description     | Function/Description |
| IDN Number   | Length in bytes      | Minimum input value/ Maximum input value | Scaling/resolution Units |                      |

There are default parameters in the Logix 5000-to-Kinetix 6200 drive product structure that you can reconfigure when the default configuration does not match the Integrated Architecture® machine configuration.

The drive functions you can change by using this procedure include:

- Additional bus capacitance in common-bus configurations
- With RSLogix 5000® software, version 20.00 or greater, or the Logix Designer application, you can configure bus capacitance values from I/O configuration&gt;Sercos module&gt;Drive module properties&gt;Power tab (refer to Chapter 6)
- Digital input assignments for I/O configurations

## IMPORTANT

IDN values return to default settings whenever the Sercos ring phases up. If your program includes a message instruction to change default IDN values, you must re-execute that instruction during phase-up to maintain those values.

## Change IDN Parameter Values

Use this flowchart to determine if changing your default configuration is required.

Figure 138 - Configuration Flowchart

<!-- image -->

In this section you follow the Configuration Flowchart on page 290 to determine if you need to use the Sercos IDN Write instruction in the Logix Designer application to change the IDN parameter values.

## Read the Present IDN Parameter Value

Follow these steps to read the present IDN value.

1. Start your Logix Designer application program.
2. Configure a Message Configuration (MSG) instruction to read your present IDN parameter values.

In this example, the Message Configuration (MSG) instruction is set to read the digital input assignments of your control module.

<!-- image -->

- a. From the Message Type pull-down menu, choose Sercos IDN Read. b. From the Identification Number pull-down menus, choose P-0-052. This example is for reading the assignment for IOD-41 (Enable is the default setting, 1 is the Enable IDN value). Refer to Digital Inputs on page 69 for other digital input IDN assignments and values.
3. Click New Tag.
4. The New Tag dialog box opens.
5. Type the name of your Destination tag. In this example, the tag name is Read\_Value.
6. Click OK.

<!-- image -->

In this example, the MSG instruction reads the P-0-052 IDN value, which is tied to digital input 1 (IOD-41), and places it in the destination as specified by the new tag.

7. Click the Communication tab.

## 8. Click Browse.

<!-- image -->

9. Select the Bulletin 2094 module to read the MSG instruction.
10. Click OK.

## Calculate/Select the New IDN Value

Changing the additional bus capacitance value requires calculations. Determine the sum of all capacitance values for the follower IAM module, each AM module, and each IPIM module on the follower IAM power rail.

Refer to Calculate Additional Bus Capacitance on page 251 for more information.

Changing the digital input assignments does not require calculations, only the selection of new values.

## Write the New IDN Parameter Value

Follow these steps to write the new IDN parameter value.

1. Configure a Message Configuration (MSG) instruction to write the IDN parameter value required for your application.
2. In this example, the Message Configuration (MSG) instruction is set to write the digital input assignments of your control module.
- a. From the Message Type pull-down menu, choose Sercos IDN Write b. From the Identification Number pull-down menus, choose P-0-052.
2. Click New Tag.
3. The New Tag dialog box opens.
4. Type the name of your Source tag. In this example, the tag name is Write\_Value.
5. Click OK.

<!-- image -->

<!-- image -->

In this example, the new tag creates a source value (that you entered) that the MSG instruction uses to overwrite the existing P-0-052 IDN value and is tied to digital input 1 (IOD-41).

6. Click the Communication tab.

## The Communication tab opens.

<!-- image -->

7. Click Browse.
8. Select your Bulletin 2094 module.
9. Click OK.

The MSG instruction writes the new IDN value to your drive.

<!-- image -->

To verify your Sercos IDN Write instruction was successful, you can perform another Sercos IDN Read instruction for the IDN in question.

10. Click OK to close the Message Configuration dialog box.

## Standard Attributes

## Kinetix 6500 Drive Specific Attributes

## Kinetix 6500 CIP Axis Attributes

This appendix provides CIP™ axis attribute information, specific to the Kinetix® 6500 (integrated motion on EtherNet/IP™) drive systems. CIP axis attributes let you configure motion-control system devices, for example, feedback devices and servo drives.

| Topic Page                                 |
|--------------------------------------------|
| Standard Attributes 295                    |
| Kinetix 6500 Drive Specific Attributes 295 |
| Change CIP Attributes 300                  |

For standard and optional CIP axis attributes and attribute definitions, see Integrated Motion on the EtherNet/IP Network Reference Manual, publication MOTION-RM003 .

- See Interpret the Attribute Tables (chapter 3) for the required and optional attributes with the attribute ID
- See the optional attributes supported by Kinetix 6500 drives (chapter 3) that are listed in a separate table
- See CIP Axis Attributes (chapter 4) for attribute definitions

The following attributes are implemented in the Kinetix 6500 as drive-specific attributes. You can access these attributes via MSG instructions.

Table 147 - Torque Prove Configuration

| Attribute ID Access Data Type Default Minimum Maximum   |                    |                                                   | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|--------------------|---------------------------------------------------|--------------------------------------------------|
| 1100 (dec) / 44c (hex)                                  | Set/Get UINT 0 – – | Enumeration: 0= Disabled 1 = Enabled 2 = Reserved | Firmware revision 2.013                          |

This attribute enables operation of the drive's Torque Proving function that works in conjunction with mechanical brake control. When enabled, the drive performs a Torque Prove test of the motor current while in the Starting state to 'prove' that current is properly flowing through each of the motor phases before releasing the brake. Should the Torque Prove test fail, a Torque Prove exception (FLT M18) is generated.

The Torque Prove feature is not able to detect all possible motor wiring problems. Perform the appropriate Hookup tests to verify proper motor wiring. Torque Prove is primarily meant to detect a loose or broken motor connection.

<!-- image -->

<!-- image -->

ATTENTION: The Torque Prove feature is not supported for motors without a brake. Enabling the torque prove feature on a motor without a brake results in unintended motion when the drive transitions to Servo On. The motor typically moves incrementally in both directions.

Table 148 - Safety Config Fault Codes

| Attribute ID Access Data Type Default Minimum Maximum   |                              | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|------------------------------|--------------------------------------------------|
| 3000 (dec) / bb8 (hex)                                  | Get UINT 0 – – See Table 149 | . –                                              |

This attribute contains the Safety Configuration fault codes. A zero value indicates no error is present.

Table 149 - Safety Configuration Fault Codes

| Fault Code Description                                                |
|-----------------------------------------------------------------------|
| 0 No Fault                                                            |
| 2 SM_Mode value not legal based on SM_Sys_Config                      |
| 5 DC_Type value not legal based on SM_Sys_Config                      |
| 7 SS_Monitor_Delay value not legal based on SS_Stop_Type              |
| 9 SS_Decel_Reference_Speed value not legal based on FB1_Resolution    |
| 11 SS_Standstill_Speed value not legal based on SM_Sys_Config         |
| 13 SLS_Monitor_Delay value not legal based on SM_Mode                 |
| 14 SLS_Speed_Limit_value not legal based on SM_Mode or FB1_Resolution |
| 15 SLS_Low_Limit value not legal based on SM_Mode                     |
| 17 SMS_Speed_Limit value not legal based on SM_Mode                   |
| 22 SDM_Type value not legal based on SM_Mode                          |
| 24 LM_Enable value not legal based on SM_Mode                         |
| 28 FB2_Resolution value not legal based on Feedback_Mode              |
| 30 FB2_Direction_Polarity value not legal based on Feedback_Mode      |
| 33 Dual_Feedback_Ratio value not legal based on Feedback_Mode         |
| 34 Dual_FB_Position_Tolerance value not legal based on Feedback_Mode  |
| 35 Dual_FB_Speed_Tolerance value not legal based on Feedback_Mode     |
| 38 SS_Input_Type value not legal based on SM_Mode                     |
| 39 SLS_Input_Type value not legal based on SM_Mode                    |
| 40 DM_Input_Type value not legal based on SM_Sys_Config and SM_Mode   |
| 41 ESM_Input_Type value not legal based on SM_Mode                    |
| 42 LM_Input_Type value not legal based on LM_Enable and SM_Mode       |
| 1001 Illegal SM_Sys_Config value                                      |
| 1003 Illegal Reset_Type value                                         |
| 1004 Illegal Reset_Qualification value                                |
| 1006 Illegal SS_Stop_Type value                                       |
| 1010 Illegal SS_Deceleration_Tolerance value                          |
| 1025 Illegal Feedback_Mode value                                      |
| 1026 Illegal Encoder_1_Type value                                     |
| 1027 Illegal FB1_Resolution value                                     |
| 1031 Illegal Encoder_1_Voltage value                                  |
| 1032 Illegal Encoder_2_Voltage value                                  |
| 1036 Illegal Over_Speed_Reaction_Time value                           |
| 1088 Illegal MP_Out_Mode value                                        |

## Table 150 - Safety Config Signature

| Attribute ID Access Data Type Default Minimum Maximum   |                                    | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|------------------------------------|--------------------------------------------------|
| 3003 (dec) / bbb (hex)                                  | Get BYTEARRAY (10 bytes) 0 – – – – |                                                  |

This attribute is a 10 byte array containing the ID (first 4 bytes), the Time (next 4 bytes) and the Date (next two bytes) of the safety configuration signature.

## Table 151 - Self Sense Angle Start

| Attribute ID Access Data Type Default Minimum Maximum   |                              | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|------------------------------|--------------------------------------------------|
| 3004 (dec) / bbc (hex)                                  | Set/Get REAL Degrees 0 0 – – |                                                  |

This attribute determines the initial commutation angle. We recommend leaving this at 0°.

## Table 152 - Self Sense Angle Increment

| Attribute ID Access Data Type Default Minimum Maximum   |                             | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|-----------------------------|--------------------------------------------------|
| 3005 (dec) / bbd (hex)                                  | Set/Get REAL 45° 5° 45° – – |                                                  |

This attribute determines the width of commutation angle increments. It is possible to vary the angle from 5 to 45 degrees, however the value must be 5, 10, 15, 30, or 45 degrees, otherwise it defaults to 10 degrees. The smaller the angle, the smaller the angle evaluation, and the longer the time.

## Table 153 - Self Sense On Time

| Attribute ID Access Data Type Default Minimum Maximum   |                                       | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|---------------------------------------|--------------------------------------------------|
| 3006 (dec) / bbe (hex)                                  | Set/Get DINT (ms) 5 ms 5 ms 50 ms – – |                                                  |

This attribute determines how long (ms) continuous torque is applied at a given commutation angle. The higher the value, the longer the acceleration time. To change this value, start at 5 ms and increase in 5 ms increments.

## Table 154 - Self Sense Hold Time

| Attribute ID Access Data Type Default Minimum Maximum   |                                               | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|-----------------------------------------------|--------------------------------------------------|
| 3007 (dec) / bbf (hex)                                  | Set/Get DINT (ms) 500 ms 250 ms 30,000 ms – – |                                                  |

This attribute determines the length of the Current Final Ramping Phase.

Table 155 - Self Sense Minimum Acceleration Angle

| Attribute ID Access Data Type Default Minimum Maximum   |                             | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|-----------------------------|--------------------------------------------------|
| 3008 (dec) / bc0 (hex)                                  | Set/Get REAL 2° 1° 360° – – |                                                  |

This attribute determines the minimum angular displacement to accept commutation test. The Self-Sensing Procedure is strongly dependent on the magnitude of the load connected to the motor and mechanical connection. A higher torque can induce oscillations in the load. It is also dependent on the encoder resolution.

Table 156 - Hookup Test Ramp Time

| Attribute ID Access Data Type Default Minimum Maximum   |                    |          | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|--------------------|----------|--------------------------------------------------|
| 3010 (dec) / bc2 (hex)                                  | Set/Get REAL 0.5 0 | 1000 (1) | Seconds Firmware revision 2.010                  |

(1) These are recommended values. There is no code that prevents you from violating the limits.

This attribute determines the amount of time that the Commutation Test waits for a motor to ramp up.

Table 157 - Hookup Test Ramp Time

| Attribute ID Access Data Type Default Minimum Maximum   |                  |          | Semantics of Values Conditional Implementation   |
|---------------------------------------------------------|------------------|----------|--------------------------------------------------|
| 3011 (dec) / bc3 (hex)                                  | Set/Get REAL 1 0 | 1000 (1) | Seconds Firmware revision 2.010                  |

(1) These are recommended values. There is no code that prevents you from violating the limits.

This attribute determines the amount of time that the Commutation Test waits for shaft stabilization after the motor is ramped up.

Table 158 - Current Decel Stopped Velocity

| Attribute ID Access Data Type Default Minimum Maximum   | Semantics of Values Conditional Implementation              |
|---------------------------------------------------------|-------------------------------------------------------------|
| 3012 (dec) / bc4 (hex)                                  | Set/Get REAL 1 0 100% % Motor Rated Firmware revision 2.023 |

This attribute sets the speed threshold associated with the zero-speed criteria of the (category 1) Current Decel &amp; Disable stop sequence. The stopped velocity is specified as a percentage of motor rated speed. This attribute sets the speed threshold where the zero-speed timer starts. When the axis speed has been below the Current Decel Stopped Velocity threshold for Current Decel Stopped Time, the axis has satisfied the zero speed criteria. This results in action to engage the mechanical brake. Axis speed in the above description is based on the Velocity Feedback signal.

Table 159 - Current Decel Stopped Time

| Attribute ID Access Data Type Default Minimum Maximum   | Semantics of Values Conditional Implementation            |
|---------------------------------------------------------|-----------------------------------------------------------|
| 3013 (dec) / bc5 (hex)                                  | Set/Get REAL 0.003 0 1000 Seconds Firmware revision 2.023 |

This attribute sets the amount of time that is associated with the zero speed criteria of the (category 1) Current Decel &amp; Disable stop sequence. The axis speed must be below the zero speed threshold, set by the Current Decel Stopped Velocity attribute, for the Current Decel Stopped Time to satisfy the zero speed criteria. When the zero speed criteria are met, this results in action to engage the mechanical brake.

## Table 160 - Disable Coast Stopped Velocity

| Attribute ID Access Data Type Default Minimum Maximum   | Semantics of Values Conditional Implementation              |
|---------------------------------------------------------|-------------------------------------------------------------|
| 3014 (dec) / bc6 (hex)                                  | Set/Get REAL 1 0 100% % Motor Rated Firmware revision 2.023 |

This attribute sets the speed threshold associated with the zero speed criteria of the (category 0) Disable &amp; Coast stop sequence. The stopped velocity is specified as a percent of motor rated speed. This attribute sets the speed threshold where the zero-speed timer starts. When the axis speed has been below the Disable Coast Stopped Velocity threshold for Disable Coast Stopped Time, the axis has satisfied the zero speed criteria. This results in action to engage the mechanical brake. Axis speed in the above description is based on the Velocity Feedback signal.

Table 161 - Disable Coast Stopped Time

| Attribute ID Access Data Type Default Minimum Maximum   | Semantics of Values Conditional Implementation            |
|---------------------------------------------------------|-----------------------------------------------------------|
| 3015 (dec) / bc7 (hex)                                  | Set/Get REAL 0.003 0 1000 Seconds Firmware revision 2.023 |

This attribute sets the amount of time associated with the zero speed criteria of the (category 0) Disable &amp; Coast stop sequence. The axis speed must be below the zero speed threshold, set by the Disable Coast Stopped Velocity attribute, for the Disable Coast Stopped Time to satisfy the zero speed criteria. When the zero speed criteria are met, this results in action to engage the mechanical brake.

<!-- image -->

ATTENTION: Use caution when setting the Stopped Velocity parameters. They are critical settings that determine when the holding brake is applied. If these values are set incorrectly, the brake can engage prematurely and eventually damage the motor. The holding brake can withstand infrequent use as a stopping brake. However, use of the holding brake as a stopping brake creates rotational mechanical backlash that is potentially damaging to the system, increases brake pad wear, and reduces brake life.

Refer to Vertical Load and Holding Brake Management Application Technique, publication MOTION-AT003, for more information.

## Change CIP Attributes

Many of the attributes can be accessed with Set System Value (SSV) and Get System Value (GSV) instructions. If the attribute is available in the Attribute Name field of an SSV or GSV, then use the SSV or GSV function to write or read the attribute value. In general, these attributes can also be changed in Axis Properties.

Figure 139 - Example SSV instruction to write the Torque Limit Positive

<!-- image -->

Figure 140 - Example GSV instruction to read the Feedback 1 Polarity

<!-- image -->

<!-- image -->

Attributes that are not accessible with SSV/GSV instuctions can be accessed with message (MSG) instructions.

Table 162 - Settings for Write CIP\_Axis\_Drive MSG Instruction

| Attribute Value                                                                                     |
|-----------------------------------------------------------------------------------------------------|
| Message Type CIP Generic Service                                                                    |
| Service Type Set Attribute Single                                                                   |
| Class 42                                                                                            |
| Instance 1                                                                                          |
| Attribute Hex value of attribute                                                                    |
| Source Element User tag with datatype from attribute definition                                     |
| Source Length Number of bytes to write – Datatypes DINT and REAL = 4 bytes – Datatype INT = 2 bytes |
| Communication Path Drive module                                                                     |

Table 163 - Settings for Read CIP\_Axis\_Drive MSG Instruction

| Attribute Value                                                      |
|----------------------------------------------------------------------|
| Message Type CIP Generic Service                                     |
| Service Type Set Attribute Single                                    |
| Class 42                                                             |
| Instance 1                                                           |
| Attribute Hex value of attribute                                     |
| Destination Element User tag with datatype from attribute definition |
| Communication Path Drive module                                      |

Figure 141 - Example Message to Read Attribute Current Decel Stopped Velocity

<!-- image -->

Figure 142 - Example Message to Write Attribute Torque Prove Configuration

<!-- image -->

IMPORTANT

Attributes that are set with SSV or MSG instructions are not retained through a drive power cycle. They revert back to their default values upon power up and must be set again.

## Notes:

## Before You Begin

<!-- image -->

## RBM Module Interconnect Diagrams

This appendix provides Bulletin 2090 Resistive Brake Module (RBM) interconnect diagrams specific to Kinetix® 6200 and Kinetix 6500 modular servo-drive systems.

| Topic Page                     |
|--------------------------------|
| Before You Begin 303           |
| RBM Module Wiring Examples 304 |

These procedures assume you have installed your RBM module with the Kinetix 6200 or Kinetix 6500 servo-drive system. For RBM module installation instructions, refer to the Resistive Brake Module Installation Instructions, publication 2090-IN009 .

<!-- image -->

ATTENTION: Use the interconnection diagrams as a general recommendation of how the control circuit can be implemented. Actual applications can vary due to requirements based on the machine builders risk assessment. The machine builder must perform a risk assessment and determine a category level of safety that must be applied to the machine.

For Kinetix 6200 drive systems, you can set the delay time for your RBM module in the Logix Designer application. Refer to Configure Axis Properties on page 151 .

For Kinetix 6500 drive systems, you can set the delay time for your RBM module in the Logix Designer application. Refer to Configure Axis Properties on page 175 .

## RBM Module Wiring Examples

This example diagram shows 2094-BCxx-Mxx-M and 2094-BMxx-M drives and 2094-BLxxS or 2094-XL75S LIM modules wired with the Bulletin 2090 RBM module.

Figure 143 - RBM Wiring Example

<!-- image -->

<!-- image -->

## Notes:

## History of Changes

This appendix contains the new or updated information for each revision of this publication. These lists include substantive updates only and are not intended to reflect all changes. Translated versions are not always available for each revision.

## 2094-UM002H-EN-P, March 2021

| Change                                                   |
|----------------------------------------------------------|
| Added IMPORTANT statement regarding motor feedback loss. |
| Added FLT M18…TORQUE PROVE fault code.                   |
| Added FLT M18…TORQUE PROVE drive behavior.               |
| Added Appendix G - Kinetix 6500 CIP™ Axis Attributes.    |
| Added Appendix I - History of Changes.                   |

## 2094-UM002G-EN-P, August 2016

|                                                                                                                                                | Change                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Added publication MOTION-RM003 to Additional Resources.                                                                                        | Added publication MOTION-RM003 to Additional Resources.                                                                                        |
| Added line-filter part numbers for systems without LIM modules and single-phase control power.                                                 | Added line-filter part numbers for systems without LIM modules and single-phase control power.                                                 |
| Updated the internal solid-state motor short-circuit protection rating to include 200,000 A (fuses) and 65,000 A (circuit breakers).           | Updated the internal solid-state motor short-circuit protection rating to include 200,000 A (fuses) and 65,000 A (circuit breakers).           |
| Corrected errors in the Absolute Position Feature table and figure.                                                                            | Corrected errors in the Absolute Position Feature table and figure.                                                                            |
| Updated all instances of EnDat 2.1 and EnDat 2.2 to read EnDat Sine/Cosine and EnDat Digital, respectively.                                    | Updated all instances of EnDat 2.1 and EnDat 2.2 to read EnDat Sine/Cosine and EnDat Digital, respectively.                                    |
| Added a footnote regarding supported model ECI119 in Support Requirements for EnDat Encoders on Third-party motors.                            | Added a footnote regarding supported model ECI119 in Support Requirements for EnDat Encoders on Third-party motors.                            |
| Corrected pinouts in Auxiliary Feedback Signals by Device Type table (pins 6…15). Also, added footnote and ATTENTION for wiring encoder power. | Corrected pinouts in Auxiliary Feedback Signals by Device Type table (pins 6…15). Also, added footnote and ATTENTION for wiring encoder power. |
| Updated intro text in Tune the Axes with reference to Kinetix® 6200 drive firmware 1.049 and link to Appendix D.                               | Updated intro text in Tune the Axes with reference to Kinetix® 6200 drive firmware 1.049 and link to Appendix D.                               |
| Updated FLT S47 fault code Possible Resolutions and added sub-code definitions.                                                                | Updated FLT S47 fault code Possible Resolutions and added sub-code definitions.                                                                |
| Updated Symptom and Resolution columns for INHIBIT S04 fault code.                                                                             | Updated Symptom and Resolution columns for INHIBIT S04 fault code.                                                                             |
| Added INHIBIT M07 fault code.                                                                                                                  | Added INHIBIT M07 fault code.                                                                                                                  |
| Added Appendix D, Configure the Load Observer Feature.                                                                                         | Added Appendix D, Configure the Load Observer Feature.                                                                                         |
| Updated the torque low-pass filter bandwidth value for Kinetix 6200 drives and removed references to Kinetix 6000 drive firmware revisions.    | Updated the torque low-pass filter bandwidth value for Kinetix 6200 drives and removed references to Kinetix 6000 drive firmware revisions.    |
| Added Appendix E, Web Server Interface.                                                                                                        | Added Appendix E, Web Server Interface.                                                                                                        |
| Added Appendix H, EC Certifications.                                                                                                           | Added Appendix H, EC Certifications.                                                                                                           |

## 2094-UM002F-EN-P, September 2015

| Change                                                                                       |
|----------------------------------------------------------------------------------------------|
| Updated all instances of RSLogix 5000® software with Studio 5000 Logix Designer® application |
| Updated system diagrams including the line interface module (LIM) with new LIM artwork       |
| Corrected Bulletin MDF drive-motor catalog number                                            |
| Added AC Line Filter Selection table                                                         |
| Updated Circuit Breaker/Fuse Options section                                                 |
| Updated auxiliary feedback connector pinout tables with 5V/9V footnote                       |

I

## 2094-UM002F-EN-P, September 2015 (continued)

| Change                                                                                                                                                    |                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Updated motor feedback connector pinout tables with 5V/9V footnote                                                                                        | Updated motor feedback connector pinout tables with 5V/9V footnote                                                                                        |
| Updated pulse reject filtering specification values                                                                                                       | Updated pulse reject filtering specification values                                                                                                       |
| Updated cyclic update period specification value                                                                                                          | Updated cyclic update period specification value                                                                                                          |
| Updated Motor Brake Relay with additional motor brake control information                                                                                 | Updated Motor Brake Relay with additional motor brake control information                                                                                 |
| Updated absolute position limit specifications to include all compatible multi-turn encoders                                                              | Updated absolute position limit specifications to include all compatible multi-turn encoders                                                              |
| Updated EnDat 2.1 sine/cosine supported models specifications                                                                                             | Updated EnDat 2.1 sine/cosine supported models specifications                                                                                             |
| Updated the input power section for consistency with other drive-family user manuals and added the impedance grounded power configuration                                                                                                                                                           | Updated the input power section for consistency with other drive-family user manuals and added the impedance grounded power configuration                                                                                                                                                           |
| Updated motor connector view examples with side views                                                                                                     | Updated motor connector view examples with side views                                                                                                     |
| Added Bulletin MPS motors and MPAS linear stages to the SpeedTec DIN connector tables                                                                     | Added Bulletin MPS motors and MPAS linear stages to the SpeedTec DIN connector tables                                                                     |
| Updated the ControlLogix® 1756-ENxT EtherNet/IP module line art with new design                                                                           | Updated the ControlLogix® 1756-ENxT EtherNet/IP module line art with new design                                                                           |
| Updated Sercos optical power DIP switch settings                                                                                                          | Updated Sercos optical power DIP switch settings                                                                                                          |
| Added reference to MOTION-AT005 for load observer alternative to autotune procedure                                                                       | Added reference to MOTION-AT005 for load observer alternative to autotune procedure                                                                       |
| Added TIP with reference to Knowledgebase document for non-private IP address configuration                                                               | Added TIP with reference to Knowledgebase document for non-private IP address configuration                                                               |
| Updated error code FLT S10 possible resolutions with ‘reduce deceleration rates’                                                                          | Updated error code FLT S10 possible resolutions with ‘reduce deceleration rates’                                                                          |
| Added INHIBIT Sxx and INHIBIT Mxx fault codes                                                                                                             | Added INHIBIT Sxx and INHIBIT Mxx fault codes                                                                                                             |
| Added IMPORTANT message to FLT S43 and FLT S44 description                                                                                                | Added IMPORTANT message to FLT S43 and FLT S44 description                                                                                                |
| Updated Bulletin MPS rotary motor wiring diagram with SpeedTec DIN cable catalog numbers                                                                  | Updated Bulletin MPS rotary motor wiring diagram with SpeedTec DIN cable catalog numbers                                                                  |
| Updated Bulletin MPAS linear stage wiring diagram with SpeedTec DIN cable catalog numbers                                                                 | Updated Bulletin MPAS linear stage wiring diagram with SpeedTec DIN cable catalog numbers                                                                 |
| Updated linear motor wiring diagram with correct motor feedback pinout                                                                                    | Updated linear motor wiring diagram with correct motor feedback pinout                                                                                    |
| Added ATTENTION statement, corrected Kinetix 6000M IDM catalog number, and added (internal) jumper circuitry to pins 1…4 of the safe torque-off connector | Added ATTENTION statement, corrected Kinetix 6000M IDM catalog number, and added (internal) jumper circuitry to pins 1…4 of the safe torque-off connector |
| Updated system requirements tables with Studio 5000 Logix Designer                                                                                        | Updated system requirements tables with Studio 5000 Logix Designer                                                                                        |
| Added History of Changes appendix                                                                                                                         | Added History of Changes appendix                                                                                                                         |

## 2094-UM002E-EN-P, May 2012

| Change                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added acronyms for the Kinetix 6000M integrated drive-motor (IDM) system.                                                                                                                                                              | Added acronyms for the Kinetix 6000M integrated drive-motor (IDM) system.                                                                                                                                                              |
| Added the IPIM module to About the Kinetix 6200 and Kinetix 6500 Drive Systems.                                                                                                                                                        | Added the IPIM module to About the Kinetix 6200 and Kinetix 6500 Drive Systems.                                                                                                                                                        |
| Added the Kinetix 6000M integrated drive-motor (IDM) to typical system installation diagrams and catalog number explanation.                                                                                                           | Added the Kinetix 6000M integrated drive-motor (IDM) to typical system installation diagrams and catalog number explanation.                                                                                                           |
| Added the IPIM module to Minimum Clearance Requirements.                                                                                                                                                                               | Added the IPIM module to Minimum Clearance Requirements.                                                                                                                                                                               |
| Added the IPIM module to Establishing Noise Zones.                                                                                                                                                                                     | Added the IPIM module to Establishing Noise Zones.                                                                                                                                                                                     |
| Added the IPIM module to Determine Mounting Order.                                                                                                                                                                                     | Added the IPIM module to Determine Mounting Order.                                                                                                                                                                                     |
| Revised motor power, brake, and feedback cable compatibility tables to include the MPL-A/B15xxx - xx7xAA and MPL-A/B2xxx-xx7xAA low-inertia motors and MPAR-A/B1xxx and MPAR-A/B2xxx electric cylinders with SpeedTec (M7) connectors. | Revised motor power, brake, and feedback cable compatibility tables to include the MPL-A/B15xxx - xx7xAA and MPL-A/B2xxx-xx7xAA low-inertia motors and MPAR-A/B1xxx and MPAR-A/B2xxx electric cylinders with SpeedTec (M7) connectors. |
| Added 2090-K6CK-D44S0 with 2090-CS0DSDS-AAxx cable for cascading safe torque-off signals from drive-to-drive.                                                                                                                          | Added 2090-K6CK-D44S0 with 2090-CS0DSDS-AAxx cable for cascading safe torque-off signals from drive-to-drive.                                                                                                                          |
| Added IPIM Module Connections with summary of installation connections and links to other diagrams and publications with additional information.                                                                                       | Added IPIM Module Connections with summary of installation connections and links to other diagrams and publications with additional information.                                                                                       |
| Added Kinetix 6000M Integrated Drive-Motor Sercos Connections                                                                                                                                                                          | Added Kinetix 6000M Integrated Drive-Motor Sercos Connections                                                                                                                                                                          |
| Added Ethernet Cable Connections                                                                                                                                                                                                       | Added Ethernet Cable Connections                                                                                                                                                                                                       |
| Updated the introduction with an overview of IDM system configuration.                                                                                                                                                                 | Updated the introduction with an overview of IDM system configuration.                                                                                                                                                                 |
| Updated the introduction with an overview of the IDM system troubleshooting                                                                                                                                                            | Updated the introduction with an overview of the IDM system troubleshooting                                                                                                                                                            |
| Updated existing circular DIN (SpeedTec) interconnect diagram with Bulletin MPL-A/B15xxx - xx7xAA and MPL-A/B2xxx-xx7xAA low-inertia motors with SpeedTec (M7) connectors.                                                             | Updated existing circular DIN (SpeedTec) interconnect diagram with Bulletin MPL-A/B15xxx - xx7xAA and MPL-A/B2xxx-xx7xAA low-inertia motors with SpeedTec (M7) connectors.                                                             |
| Updated the Kinetix MPAI electric cylinders interconnect diagram with frame 64 and 144 cable catalog numbers.                                                                                                                          | Updated the Kinetix MPAI electric cylinders interconnect diagram with frame 64 and 144 cable catalog numbers.                                                                                                                          |
| Updated the Kinetix MPAR electric cylinders interconnect diagram with cable catalog number changes for SpeedTec (M7) connector                                                                                                         | Updated the Kinetix MPAR electric cylinders interconnect diagram with cable catalog number changes for SpeedTec (M7) connector                                                                                                         |
| Added Kinetix 6000M Integrated Drive-Motor Wiring Example.                                                                                                                                                                             | Added Kinetix 6000M Integrated Drive-Motor Wiring Example.                                                                                                                                                                             |
| Added Bulletin MDF catalog numbers to Controlling a Brake Example                                                                                                                                                                      | Added Bulletin MDF catalog numbers to Controlling a Brake Example                                                                                                                                                                      |
| Added an overview for IDM system firmware upgrades.                                                                                                                                                                                    | Added an overview for IDM system firmware upgrades.                                                                                                                                                                                    |
| Updated the procedure and tables with IPIM module values.                                                                                                                                                                              | Updated the procedure and tables with IPIM module values.                                                                                                                                                                              |

## 2094-UM002D-EN-P, February 2011

| Change                                                                                                                                                                              |                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Updated system configuration diagrams with power rail and cable clamp redesign features. Support for EnDat high-resolution feedback with Kinetix RDB direct-drive motors was added. | Updated system configuration diagrams with power rail and cable clamp redesign features. Support for EnDat high-resolution feedback with Kinetix RDB direct-drive motors was added. |
| Updated communication diagrams with drive-to-drive double-wide configurations.                                                                                                      | Updated communication diagrams with drive-to-drive double-wide configurations.                                                                                                      |
| Updated mounting diagrams with power rail and cable clamp redesign features.                                                                                                        | Updated mounting diagrams with power rail and cable clamp redesign features.                                                                                                        |
| Updated IAM and AM power module illustrations with cable clamp redesign features.                                                                                                   | Updated IAM and AM power module illustrations with cable clamp redesign features.                                                                                                   |
| Updated power cable catalog numbers with standard (non-flex) SpeedTec DIN cables.                                                                                                   | Updated power cable catalog numbers with standard (non-flex) SpeedTec DIN cables.                                                                                                   |
| Updated brake cable catalog numbers with standard (non-flex) SpeedTec DIN cables.                                                                                                   | Updated brake cable catalog numbers with standard (non-flex) SpeedTec DIN cables.                                                                                                   |
| Updated feedback cable catalog numbers with standard (non-flex) SpeedTec DIN cables.                                                                                                | Updated feedback cable catalog numbers with standard (non-flex) SpeedTec DIN cables.                                                                                                |
| Removed Bulletin 1336 external active shunt modules. Added reference to Rockwell Automation Encompass partner solutions.                                                            | Removed Bulletin 1336 external active shunt modules. Added reference to Rockwell Automation Encompass partner solutions.                                                            |
| Updated dimension drawings with power rail and cable clamp redesign features.                                                                                                       | Updated dimension drawings with power rail and cable clamp redesign features.                                                                                                       |
| Updated Axis Module/Rotary Motor Wiring Examples with standard (non-flex) SpeedTec DIN motor power and feedback cables.                                                             | Updated Axis Module/Rotary Motor Wiring Examples with standard (non-flex) SpeedTec DIN motor power and feedback cables.                                                             |

## 2094-UM002C-EN-P, May 2010

| Change                                                                        |
|-------------------------------------------------------------------------------|
| Catalog Number Explanation                                                    |
| Peak Current Specifications                                                   |
| Set the Ground Jumper                                                         |
| Kinetix MPL Motor Connectors                                                  |
| Motor Power Cable Compatibility                                               |
| Motor Brake Cable Compatibility                                               |
| Motor Feedback Cable Compatibility - Bayonet                                  |
| Motor Feedback Cable Compatibility - Circular DIN/Plastic                     |
| IAM Module (460V) Power Specifications IAM Module (460V) Power Specifications |
| AM Module (inverter) 460V Power Specifications                                |
| Product Dimensions                                                            |

## 2094-UM002B-EN-P, March 2010

| Change                                                                                               |
|------------------------------------------------------------------------------------------------------|
| Typical EtherNet/IP installations                                                                    |
| Kinetix 6200 and Kinetix 6500 catalog numbers                                                        |
| Kinetix 6000, Kinetix 6200, and Kinetix 6500 drive compatibility                                     |
| Limitations for Ethernet cable lengths                                                               |
| Addition of Ethernet cable in noise zone diagrams                                                    |
| EtherNet/IP control module features and indicators                                                   |
| Understanding safe torque-off safety features                                                        |
| Motor power cable compatibility                                                                      |
| Wiring motor brake cable connections                                                                 |
| Motor and feedback cable combinations                                                                |
| Connecting Ethernet cables                                                                           |
| Updates for RSLogix 5000 software, version 18                                                        |
| Configure and Start Up the Kinetix 6500 Drive System (new chapter) RSLogix 5000 software, version 18 |
| Fault code and status indicator troubleshooting tables to support Kinetix 6500 drives systems        |
| Maximum feedback cable length specifications for Kinetix MPM and RDB rotary motors                   |
| Interconnect diagrams for Kinetix MPM rotary motors                                                  |
| Interconnect diagrams for Kinetix RDB direct-drive motors                                            |
| Coil current ratings for Kinetix MPM motor brake applications                                        |
| Revised ControlFLASH procedure to include Kinetix 6500 drives                                        |
| Revised Calculating Additional Bus Capacitance procedure to include Kinetix 6500 drives              |

## Numerics

1756-EN2T 165

1756-EN2TR 165

1756-EN3TR 165

1756-MxxSE 142

1768-M04SE 142

1784-PM16SE 142

2090-CS0DSDS-AAxx 115 , 120 , 122

2090-K6CK-D15M 115 , 120 , 121 , 226

2090-K6CK-D44M 115 , 120 , 121

2090-K6CK-D44S0 115 , 120 , 122

2094 power rail 54

## A

## about this publication 9 AC line filters

noise reduction 49 selection 29

## acceleration

feedback 256

reference 253

acronyms 10

actions tab 178

k 253

## actual position feedback actuators

LDAT 233

MPAI 232

MPAR 232

MPAS 231

## additional

bus capacitance calculating 251

example 252

resources 10

alarm 202

applying power 155 , 180

audience for this manual 9

## auxiliary feedback

encoders 83

pinouts

65

## axis module

axis properties 151 , 153 , 175 , 176

64

connector designators, Ethernet connector designators, sercos 63 connector locations 62 mounting 55 remove from power rail 210 replacing on power rail 213 status indicators 198 wiring requirements 99

axis unstable 200

## B

bandwidth 160

Kop 256

## base node address, EtherNet/IP 161

example with two ControlLogix chassis 164 163

example with two power rails

## base node address, sercos 136

example with double-wide modules 140

example with IDM system 141

example with two ControlLogix chassis 139

example with two power rails 138

baud rate 137

bayonet connector 106

## block diagrams

converter 239

inverter 238

shunt module 240

## bonding

EMI (electromagnetic interference) examples 37 high-frequency energy 38 subpanels 38

36

braided strap 96

brake relay 73

building your own cables 88

## bus

regulator 148 , 173 status indicator 156 , 181 , 198

## C

## cables

88

building your own cables categories 47 CE requirements 25 Ethernet cable length 130 fiber-optic cable length 126 noise zones 39 routing 28 shield clamp 114 shield, EMC 108 , 109 UK requirements 25

capacitance values

251

## catalog number

control module 23

integrated axis module

IPIM module 23

shunt module 23

slot-filler module 23

CB1, CB2, CB3 155 , 180

CE compliance 25

certification website 11

change safety password 288

## CIP attribute changes

GSV 300

MSG 300

SSV 300

23

## CIP axis attributes

CIP attribute changes 300

current decel stopped time 298

current decel stopped velocity 298

disable coast stopped time 299

disable coast stopped velocity hookup test ramp time 298

hookup test wait time 298

Kinetix 6500 specific attributes 295

standard attributes 295

torque prove configuration 295

CIP statistics 277

## circuit breaker

LIM 155 , 180

selection 30

clamp 114

comm status indicator 156 , 198

common bus (refer to DC common bus)

commutation offset 182

compatibility

IDM system 24

network 24

compliant mechanical loads 262

configuration 254

summary tab 287

configure fault log 282

configuring axis properties 151 , 175

delay times 152 , 180

drive modules 146 , 169

EtherNet/IP 165

exceptions category 179

feedback only axis 148 , 171

## configuring EtherNet/IP

base node address 161

control module 161

EtherNet/IP module 167

IAM 161

private network 162

## configuring sercos

base node address 136

baud rate 137

control module 136

IAM 136

IDM system 135

sercos module 142 , 144

## connecting

Ethernet cables 130

examples 131

external shunt resistor 123

feedback 115

I/O 115

IPIM module 124

motor shield clamp 114

panel-mounted breakout kit 119

premolded feedback cables 118

resistive brake module 125

sercos cables 126

examples 127

examples, bulkhead 128

## connector designators

axis module 64

control module 64

integrated axis module 64

299

## connector locations

axis module 62

axis module, Ethernet 64

axis module, sercos 63

integrated axis module 62

IPIM module 63

## contactor enable relay 72

## control module

catalog number 23 configuring EtherNet/IP 161 configuring sercos 136 connector designators 64 mounting 58 remove from power module

211

replace on power module 213

## control power

input specifications 78

## ControlFLASH

241

firmware upgrade software kit 242 troubleshooting 247

verify upgrade 248

controller properties 142 , 165

conversion tab 152

converter 239

current decel stopped time 298

current decel stopped velocity 298

cycle time 145

## D

## data

rate 145

type 147 , 171

date/time tab 143 , 166

DC common bus capacitance values 251

configuring 148 , 173

follower IAM 18 , 92

fuse requirements 93

interconnect diagram 221 , 222 , 223 , 224

leader IAM 18 , 92

precharge 18 , 92 , 250

total bus capacitance 18

typical installation 18

delay times 152 , 180

device identity 284

digital inputs 69

IDN assignments 69

IDN values 70

DIN-style connector 106

dip switches 145

disable coast stopped time 299

disable coast stopped velocity 299

disable drive 203

download program 154 , 180

download Motion Analyzer 11

## drive

compatibility 24 indicators tab 272 information tab 273 status indicator 156 , 181 , 198 tab 151

| E                                                                | ground                                                               |              |                      |
|------------------------------------------------------------------|----------------------------------------------------------------------|--------------|----------------------|
| earth ground  96                                                 | jumper setting  93 grounded power configuration  89                  |              |                      |
| EMC 108 ,  109                                                   | grounding multiple subpanels  97 GSV  300                            | cable shield |                      |
| motor ground termination  105 EMI (electromagnetic interference) |                                                                      |              |                      |
| bonding  36 enable time synchronization  143 ,  166              | H                                                                    |              |                      |
| enclosure                                                        | hardware                                                             |              |                      |
| requirements  27 32                                              | enable input  157 ,  159 hardware enable input  183 ,  185           |              |                      |
| selection                                                        | HF bonding  36                                                       | 83           | encoders             |
| statistics tab  278                                              | high-frequency                                                       |              |                      |
| erratic operation  201                                           | energy  38                                                           |              |                      |
| establish communication  198                                     | resonances  266 271                                                  |              |                      |
| Ethernet statistics  276                                         | Home tab                                                             |              |                      |
| EtherNet/IP                                                      | hookup                                                               |              |                      |
| connecting cables  130                                           | tab  157                                                             |              |                      |
| connections  71                                                  | test  182                                                            |              |                      |
| module  165                                                      | hookup test ramp time  298                                           |              |                      |
| module properties  167                                           | 298                                                                  |              |                      |
| PORT1 and PORT2 connectors                                       | hookup test wait time                                                |              |                      |
| 130 exceptions category  179                                     |                                                                      |              |                      |
| external shunt resistor  r  50                                   | I                                                                    |              |                      |
| wiring  123                                                      | I/O connections                                                      |              |                      |
| F                                                                | 115 pinouts  65 specifications  69 188                               |              |                      |
| fault                                                            | IDM fault codes  IDM system                                          |              |                      |
| action tab  152 code summary  190                                | compatibility                                                        |              |                      |
| IDM system  188                                                  | 24 configuring sercos                                                |              |                      |
| 282 202                                                          | 135 firmware upgrade  241                                            |              |                      |
| log tab  status only                                             | interconnect diagram  236                                            |              |                      |
| feedback                                                         | IDN                                                                  |              |                      |
| cables CE                                                        | assignments  69 calculate value                                      |              |                      |
| 25 UK  25                                                        | 292 change values  289 253                                           |              |                      |
| cables and pinouts  feedback only axis                           | load observer  read value  290                                       |              |                      |
| 115 148 ,                                                        |                                                                      |              |                      |
| 171 gain (Kof)  256                                              |                                                                      |              |                      |
| motor feedback connector  64 79                                  | read/write messages  265 values, digital inputs  70 write value  293 |              |                      |
| specifications                                                   |                                                                      |              |                      |
| tab  151                                                         | 202                                                                  |              |                      |
|                                                                  | ignore                                                               |              |                      |
| fiber-optic 126                                                  | input connector pinouts, IAM  67                                     |              |                      |
| signals  71                                                      | gain (Kou)  256 power source  156 ,  181                             |              |                      |
| fiber-optic cables drive-to-drive                                |                                                                      |              |                      |
| 128 drive-to-IPIM  129                                           | input power wiring 90                                                |              |                      |
|                                                                  | 3-phase delta                                                        |              |                      |
| firmware upgrade  241 248                                        | determining input power  ground jumper setting                       |              |                      |
| verify upgrade                                                   | 88 93                                                                |              |                      |
| follower                                                         | high/low resistance  90                                              |              |                      |
| IAM  18 ,  92                                                    | grounded power configuration                                         |              |                      |
| 155 ,  156                                                       | ungrounded power configuration                                       |              |                      |
| four-character status display  fuse selection  30                | installing drive accessories AC line filters  49                     |              |                      |
|                                                                  | external shunt resistor  50 low-profile connector kits               |              |                      |
|                                                                  | motor brake  52                                                      |              |                      |
|                                                                  | RBM  52                                                              |              |                      |
| gains  256                                                       |                                                                      |              |                      |
| general                                                          | thermal switch                                                       |              |                      |
| category  176                                                    |                                                                      |              |                      |
| get system value (GSV)  300                                      |                                                                      |              |                      |
|                                                                  | 120                                                                  |              |                      |
|                                                                  | 52                                                                   |              |                      |
|                                                                  | 89                                                                   | G            | Rx and Tx connectors |

## installing your drive 27

| bonding examples  37                                 | drive-specific axis attributes  295                   |
|------------------------------------------------------|-------------------------------------------------------|
| bonding subpanels  38                                |                                                       |
| cable categories  47 circuit breakers  30            | L                                                     |
| clearance requirements  35                           | leader IAM  18 ,  92                                  |
| enclosure selection  32                              | line filter selection                                 |
| fuse selection  30                                   | 29                                                    |
| HF bonding  36                                       | line interface module                                 |
| line filter  29                                      | circuit breakers  155 ,  180                          |
| noise zones  39                                      | interconnect diagram  217 ,  218 ,  220               |
| system mounting requirements  27                     | three-phase power  156 ,  181                         |
| transformer  28                                      | linear motors                                         |
| integral bandwidth (Koi)  256                        | Kinetix LDC  234 ,  235                               |
| integrated axis module                               | load inertia ratio  253                               |
| catalog number  23                                   | acceleration                                          |
| configuring EtherNet/IP  161 configuring sercos  136 | feedback  256                                         |
| 64                                                   | reference  253                                        |
| connector designators                                | actual position feedback  253                         |
| connector locations  62                              | auto-tuning  263                                      |
| interconnect diagram  217 ,  218 ,  220              | bandwidth (Kop)  256                                  |
| 223 ,  224 mounting  55                              | configuration  254 feedback gain (Kof)  256           |
| removing from power rail  210                        | gains  256                                            |
| replace on power rail  213                           | auto-tune                                             |
| status indicators  198                               | 260 compliant mechanical loads  262                   |
| wiring BC connector  111                             | high-frequency resonances  266                        |
| wiring CED connector  104                            | manual tuning  263                                    |
| wiring CPD connector  101                            | out-of-box  258                                       |
| wiring IPD connector  102                            | rigid mechanical loads  261                           |
| wiring MP connector  105                             | IDN read/write messages  265                          |
| wiring requirements  98 ,  99                        | input gain (Kou)  256                                 |
| interconnect diagrams                                | integral bandwidth (Koi)  256 load inertia ratio  253 |
| 2094 with 1326AB  230 2094 with Kinetix RDB  229     | mechanical load  253                                  |
| 2094 with LDAT  233                                  | no auto-tuning  263                                   |
| 2094 with LDC  234 ,  235                            | torque estimate  253                                  |
| 2094 with MPAI  232                                  | velocity                                              |
| 2094 with MPAR  232                                  | estimate  254 feedback  254                           |
| 2094 with MPAS  231                                  | Logix Designer application  14 ,  142 165             |
| 2094 with MPL  226 2094 with MPL/MPM/MPF  228        | ,                                                     |
| 2094 with MPL/MPS  227                               | low profile connector kits                            |
| IDM system  236                                      | wiring  120                                           |
| notes  216 ,  304                                    |                                                       |
| power, DC common bus  ,  223                         | M                                                     |
| 221 ,  222 power, IAM with LIM  217 ,  218           | 271                                                   |
| power, IAM without LIM  220                          | MAC address                                           |
| RBM  304 shunt module                                | manual tuning  263 mechanical load                    |
|                                                      | 253                                                   |
| 2094  225 passive  225                               | message instruction (MSG)  300 module                 |
| interpreting status indicators  188 inverter  238    | mounting order                                        |
|                                                      | 54 properties                                         |
| IP address  269                                      | drive modules                                         |
| IPIM module                                          | 146 ,  169 EtherNet/IP module  167 sercos module  144 |
| catalog number  24                                   | 280                                                   |
| 23                                                   | monitor signals                                       |
| compatibility                                        | Motion Analyzer                                       |
| connector designators  63 mounting  55               | download  11                                          |
| removing from power rail  212                        |                                                       |
| wiring  124                                          | motion group properties  150 ,                        |
|                                                      | 174                                                   |

## K

## Kinetix 6000M system

compatibility 24

## Kinetix 6500

## motors

accel/decel problems 201

brake 52

cable length 25 , 27

feedback pinouts 66 , 117

ground termination 105

information tab 274

interconnect diagram

1326AB 230

Kinetix RDB 229

MPL 226

MPL/MPM/MPF 228

MPL/MPS 227

motor and feedback tab 151

MPL connectors bayonet 106

DIN-style 106

overheating 201

power and brake pinouts 68

power wiring

3-phase and brake 109

3-phase only 108

shield clamp wiring 114

tab 176

testing 157 , 181

thermal specifications 80

tuning 157 , 181

velocity 201

mounting brackets 53

## mounting your drive 55

2094 power rail 54

axis module 55

control modules 58

IAM module 55

IPIM module 55

module mounting order 54

mounting brackets 53

shunt module 55

slot-filler module 55

## MPL connectors

bayonet 106

DIN-style 106

## N

## network

compatibility 24

settings tab 275

status indicator 199

node address 147

## noise

abnormal 201

feedback 201

reduction 49

zones 39

## O

OK status indicator 181 , 199

oscilloscope 281

## P

## panel

mounted breakout kit 119

requirements 27

## parameters 179

drive, IDN 289

load observer 253

peak detection 279

peak enhancement definition of terms 76

inverter overload curve 77

load duty cycle 76

specifications

76

## pinouts

I/O, safety, aux fdbk 65 input connector, IAM 67

motor and brake connector 68

motor feedback connector 66 , 117

planning your installation 27

PORT 1 status indicator 156 , 181 , 199

PORT 2 status indicator 156 , 181 , 199

## power

cables

CE 25

UK 25

cycling 75

dissipation 34

power rail 284

connecting braided strap 96

removing 214

replacing 214

power up 155 , 180

precharge 18 , 92 , 250

premolded feedback cables 118

private network k 162

product selection website 11

publications, related 10

## R

RBM 52

related publications 10

relay output 237

remove

control module 211

modules from power rail 210

## replace

control module 213

modules on power rail 213

## resistive brake module

interconnect diagrams 304 wiring 125

rigid mechanical loads 261

routing power and signal wiring 88

RSLinx software 242

RSLogix 5000 software 242

## S

Safe Speed Monitor 84

Safe Torque Off 85

| safety  84 ,  85                             | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         | status indicators  156 ,  181 ,  188 ,  198         |
|----------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| configuration tab  286                       | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     | bus status  198                                     |
| lock status indicator  156                   | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    | comm status  198                                    |
| main tab  285                                | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   | drive status  198                                   |
| modes of operation  85                       | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             | EtherNet/IP module  181                             |
| pinouts  65                                  | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 | four-character  155 ,  156 ,  180 ,                 |
| safety lock status indicator  181 ,  199     | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  | PORT 1 status  199                                  |
| selection                                    | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  | PORT 2 status  199                                  |
| AC line filters  29                          | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             | safety lock status  199                             |
| sercos                                       | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        | sercos interface module  156                        |
| connecting cables  126                       | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    | status only  203                                    |
| connections  71                              | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                | stop                                                |
| module  142                                  | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          | drive  202                                          |
| module properties  144                       | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         | motion  203                                         |
| set system value (SSV)  300                  | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        | planner  202                                        |
| shield clamp  114                            | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 | Studio 5000 Logix Designer  14 ,  142 ,  165 ,  242 |
| shunt module  240                            | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              | surge suppression  112                              |
| bus status indicator  200                    | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            | switches                                            |
| catalog number  23                           | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   | base node address                                   |
| interconnect diagram                         | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      | baud rate  137                                      |
| 2094  225                                    | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 | optical power level                                 |
| passive  225                                 | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              | system                                              |
| mounting  55                                 | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          | components                                          |
| removing from power rail  212                | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          | ground  96                                          |
| replacing on power rail  213                 | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               | mounting requirements                               |
| shunt fault status indicator  200 200        | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           | system block diagrams 239                           |
| temperature status indicator                 | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           | converter                                           |
| troubleshooting  199                         | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       | inverter  238                                       |
| wiring requirements  99                      | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   | shunt module  240                                   |
| shutdown  202                                | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     | system overview                                     |
| slot-filler module                           | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             | DC common bus  18 20 21                             |
| catalog number  23                           | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         | EtherNet/IP                                         |
| mounting  55                                 | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          | sercos  19                                          |
| removing from power rail  212 213            | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     | with IDM system                                     |
| replacing on power rail                      | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        | with LIM  15                                        |
| software                                     | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         | without LIM                                         |
| Logix Designer application  14 ,  142 ,  165 | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              | RSLinx                                              |
| RSLogix 5000  242                            |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
| specifications                               | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   | T                                                   |
|                                              | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             | temperatures  test axes                             |
| brake relay  73                              | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     | hookup tab  157                                     |
| contactor enable relay  72                   | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    | hookup test  182                                    |
| control power input  78                      | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  | thermal switch  52                                  |
| digital inputs  69                           |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
| EtherNet/IP connections  71                  | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                | torque estimate  253                                |
| feedback                                     | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          | torque prove configuration                          |
| motor and auxiliary, general  79             | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           | total bus capacitance  18                           |
| motor feedback                               | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    | calculating  250                                    |
| EnDat digital  82                            | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        | example  252                                        |
| EnDat sin/cos  82                            | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         | training  9                                         |
| generic TTL  81                              | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         | transformer                                         |
| Hiperface  80                                | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              | sizing                                              |
| sin/cos incremental  81 Tamagawa  81         | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             | 28 transmit power level                             |
| 80                                           |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
|                                              | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 | 145                                                 |
| motor thermal  peak enhancement  76          |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
|                                              | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         | cycling  75 dissipation  34                         |
| power                                        | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            | 84 ,  85                                            |
| safety  I/O power supply  84                 |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
| 85                                           |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
| modes of operation                           |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
| sercos connections                           |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |                                                     |
|                                              | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  | 71                                                  |

## troubleshooting

## alarm 202 bus status indicator 198 comm status indicator 198 ControlFLASH 247 disable drive 203 drive status indicator 198 exception behavior 202 fault behavior 203 fault code summary 190 fault codes 189 fault status only 202 four-character display messages 188 general system problems 200 abnormal noise 201 axis unstable 200 erratic operation 201 feedback noise 201 motor accel/decel 201 motor overheating 201 motor velocity 201 no rotation 201 ignore 202 Logix/drive fault behavior 202 network status indicator 199 OK status indicator 199 PORT 1 status indicator 199 PORT 2 status indicator 199 safety lock status indicator 199 safety precautions 187 shunt module 199 bus status indicator 200 shunt fault status indicator 200 temperature status indicator 200 shutdown 202 status only 203 stop drive 202 stop motion 203 stop planner 202 tune axes autotune tab 184 bandwidth 160 tune tab 159 typical installation DC common bus 18 EtherNet/IP 20 , 21 , 22 sercos 19 with IDM system 17 with LIM 15 without LIM 16 U UK compliance 25 ungrounded power configuration 91 units tab 151 V velocity estimate 254 feedback 254

## W

## web server

## categories 270 change safety password 288 CIP statistics 277 configuration summary 287 configure fault log 282 device identity 284 drive indicators 272 drive information 273 encoder statistics 278 Ethernet Statistics 276 fault log 282 Home tab 271 IP address 269 MAC address 271 monitor signals 280 motor information 274 network settings 275 oscilloscope 281 peak detection 279 power rail 284 safety configuration 286 safety main 285 temperatures 283 website certifications 11 product selection 11 wiring building your own cables 88 earth ground 96 Ethernet cables 130 external shunt resistor 123 ground jumper setting 93 grounded power configuration 89 I/O connections 115 IAM BC connector 111 CED connector 104 CPD connector 101 IPD connector 102 MP connector 105 input power type 88 IPIM module 124 low profile connectors 120 motor cable shield clamp 114 motor power 108 , 109 requirements 87 IAM 98 IAM/AM 99 shunt module 99 resistive brake module 125 routing power and signal wiring 88 sercos fiber optic cables 126 ungrounded power configuration 91 wiring guidelines 100

## Notes:

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, Knowledgebase, and product notification updates.   | rok.auto/support      |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------|
| Local Technical Support Phone Numbers            | Locate the telephone number for your country.                                                             | rok.auto/phonesupport |
| Technical Documentation Center                   | Quickly access and download technical specifications, installation instructions, and user manuals.        | rok.auto/techdocs     |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.                      | rok.auto/literature   |
| Product Compatibility and Download Center (PCDC) | Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes.        | rok.auto/pcdc         |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Allen-Bradley, CompactLogix, ControlFLASH, ControlLogix, expanding human possibility, Guardmaster, Integrated Architecture, Kinetix, Logix 5000, PanelView, POINT I/O, PowerFlex, Rockwell Automation, RSLinx, RSLogix 5000, SoftLogix, Studio 5000 Logix Designer, Studio 5000, and Stratix are trademarks of Rockwell Automation, Inc.

CIP and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan 12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIA PACIFIC: RockwellAutomation, Level 14, Core F, Cyberport 3, 100 Cyberport Road, Hong Kong, Tel:(852)2887 4788,Fax:(852)2508 1846 UNITEDKINGD0M:Rockwell Automation Ltd.Pitfield,Kiln Farm MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800,Fax:(44)(1908)261-917