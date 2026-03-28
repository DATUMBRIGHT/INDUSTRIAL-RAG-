<!-- image -->

## Kinetix 6000 Multi-axis Servo Drives

Catalog Numbers 2094-ACxx-Mxx-S, 2094-BCxx-Mxx-S, 2094-AMxx-S, 2094-BMxx-S, 2094-ACxx-Mxx, 2094-BCxxMxx, 2094-AMxx, 2094-BMxx, 2094-BSP2, 2094-PRF, 2094-SEPM-B24-S

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

|                              | Preface                                                                                         |                                                      |
|------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------|
|                              | Summary of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . 9                  |
|                              | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . 9          |                                                      |
|                              | Conventions Used in This Manual . . . . . . . .                                                 | . . . . . . . . . . . . .  . . . . . . . . . . . . 9 |
|                              | Additional Resources . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . . . . . 10                           |
|                              | Chapter 1                                                                                       |                                                      |
| Start                        | IAM/AM Module Series Changes . . . . . . . . . .                                                | . . . . . . . . . . . . .  . . . . . . . . . . 11    |
|                              | About the Kinetix 6000 Drive Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 |                                                      |
|                              | Typical Hardware Configurations . . . . . . . . .                                               | . . . . . . . . . . . . .  . . . . . . . . . . 13    |
|                              | Typical Communication Configurations . . . . .                                                  | . . . . . . . . . . . .  . . . . . . . . . 17        |
|                              | Catalog Number Explanation . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 18                     |
|                              | Kinetix Drive Component Compatibility . . . . . . . . . . . . . . . . . . . . . . . . . . 19    |                                                      |
|                              | Kinetix 6000M Integrated Drive-Motor System Compatibility. . . . . . . 19                       |                                                      |
|                              | Agency Compliance . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | . . . . . . . . 20                                   |
|                              | CE and UK Requirements (system without LIM module) . . . . . . . . 20                           |                                                      |
|                              | CE and UK Requirements (system with LIM module) . . . . . . . . . . . 20                        |                                                      |
|                              | Chapter 2                                                                                       |                                                      |
| Plan the Kinetix 6000 Drive  | System Design Guidelines . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . 21                   |
| System Installation          | System Mounting Requirements .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . 21                         |
|                              | Transformer Selection . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . . . . . . . . 22                                   |
|                              | AC Line Filter Selection . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 22                   |
|                              | Circuit Breaker/Fuse Options . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 23                     |
|                              | Enclosure Selection . . . . . . . .  . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . 24                   |
|                              | Minimum Clearance Requirements . . . . . . .                                                    | . . . . . . . . . . .  . . . . . . . . . 26          |
|                              | Electrical Noise Reduction  . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . . . . . . . . . . . . 27                           |
|                              | HF Bond for Modules . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 27                   |
|                              | HF Bond for Multiple Subpanels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28   |                                                      |
|                              | Establish Noise Zones. . . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 29                   |
|                              | Cable Categories for Kinetix 6000 Systems.                                                      | . . . . . . . . . . .  . . . . . . . . . 38          |
|                              | Noise Reduction Guidelines for Drive Accessories . . . . . . . . . . . . . . 39                 |                                                      |
|                              | Chapter 3                                                                                       |                                                      |
| Mount the Kinetix 6000 Drive | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . . . . . . . 43                           |
| System                       | Use the 2094 Mounting Brackets . . . . . . . .                                                  | . . . . . . . . . . . .  . . . . . . . . . . 43      |
|                              | Install the 2094 Power Rail. . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 43                     |
|                              | Determine Mounting Order.   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . . 44                                   |
|                              | Mount Modules on the                                                                            |                                                      |
|                              | Power Rail. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . . . . . . . . . . . . 45                           |
|                              | Chapter 4                                                                                       |                                                      |
| Connector Data and Feature   | 2094 IAM/AM Module Connector Data . . . . . .                                                   | . . . . . . . . . . . .  . . . . . . . . . . 47      |
| Descriptions                 | Safe Torque-off Connector Pinout. . . . . . .                                                   | . . . . . . . . . . . .  . . . . . . . . . . 49      |

|                                | I/O Connector Pinout . . . . . . .  . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . 50                                       |
|--------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
|                                | Motor Feedback Connector Pinout . . . . . . .                                                          | . . . . . . . . . . .  . . . . . . . . . . 50                            |
|                                | Auxiliary Feedback Connector Pinout. . . . .                                                           | . . . . . . . . . . .  . . . . . . . . . . 52                            |
|                                | IAM Input Connector Pinout . . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . 53                                           |
|                                | IAM and AM Motor Power and Brake Connector Pinout . . . . . . . . . 53                                 |                                                                          |
|                                | Control Signal Specifications . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . .  . . . . . . . . 54                                  |
|                                | Digital Inputs . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . . . 54                                                       |
|                                | Sercos Communication Specifications. . . . .                                                           | . . . . . . . . . . .  . . . . . . . . . 55                              |
|                                | Analog Outputs. . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 55                                       |
|                                | Contactor Enable Relay . . . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 56                                       |
|                                | Power and Relay Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 |                                                                          |
|                                | Motor/Resistive Brake Relay . . . . . . . . . . .                                                      | . . . . . . . . . . . . .  . . . . . . . . . . 57                        |
|                                | Input Power Cycle Capability . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 58                                         |
|                                | Peak Enhancement Specifications. . . . . . .                                                           | . . . . . . . . . . . .  . . . . . . . . . . 59                          |
|                                | Control Power. . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . 61                                               |
|                                | Feedback Specifications .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . 62                                               |
|                                | Absolute Position Feature . . . .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . 63                                         |
|                                | Motor Feedback Specifications. . . . . . . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . . 63                          |
|                                | Feedback Power Supply Specifications. . . .                                                            | . . . . . . . . . . .  . . . . . . . . . . 64                            |
|                                | Auxiliary Position Feedback Encoders . . . . . . . . . . . . . . . . . . . . . . . . . 64              |                                                                          |
|                                | Chapter 5                                                                                              |                                                                          |
| Connect the Kinetix 6000 Drive | Basic Wiring Requirements .   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . . . . . . . 65                                                       |
| System                         | Building Your Own Cables. . . . .  . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . 66                                         |
|                                | Routing the Power and Signal Cables . . . . .                                                          | . . . . . . . . . . .  . . . . . . . . . . 66                            |
|                                | Determine the Input Power Configuration . . .                                                          | . . . . . . . . . . .  . . . . . . . . . . 66                            |
|                                | Grounded Power Configurations. . . . . . . .                                                           | . . . . . . . . . . . .  . . . . . . . . . . 67                          |
|                                | Ungrounded Power Configurations . . . . . .                                                            | . . . . . . . . . . .  . . . . . . . . . . 68                            |
|                                | DC Common Bus Configurations. .  . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . 69                                         |
|                                | Common Bus Fusing Requirements . . . . . .                                                             | . . . . . . . . . . .  . . . . . . . . . . 70                            |
|                                | Set the Ground Jumper in Select Power Configurations. . . . . . . . . . . . . 70                       |                                                                          |
|                                | Set the Ground Jumper. . . . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 72                                       |
|                                | Grounding the Kinetix 6000 Drive System. . . .                                                         | . . . . . . . . . . . .  . . . . . . . . . 75                            |
|                                | Ground the Power Rail to the System Subpanel . . . . . . . . . . . . . . . . . 75                      |                                                                          |
|                                | Ground Multiple Subpanels. . . .  . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . 76                                         |
|                                | Power Wiring Requirements . . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 77                                         |
|                                | Power Wiring Guidelines . . . . . . . . . . . . .  . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . 78                                             |
|                                | Wiring the IAM/AM Module Connectors . . . . . . . . . . . . . . . . . . . . . . . . . . 79             |                                                                          |
|                                | Wire the Control Power (CPD) Connector. . . . . . . . . . . . . . . . . . . . . . 79                   |                                                                          |
|                                | Wire the Input Power (IPD) Connector . . .                                                             | . . . . . . . . . . .  . . . . . . . . . . 80                            |
|                                | Wire the Contactor Enable (CED) Connector . . . . . . . . . . . . . . . . . . . 81                     |                                                                          |
|                                | Wiring the Safe Torque-off (STO) Connector . . . . . . . . . . . . . . . . . . . 82                    |                                                                          |
|                                | Wire the Motor Power (MP) Connector . . . . . . . . . . . . . . . . . . . . . . . . 83                 |                                                                          |
|                                | Wire the Motor/Resistive Brake (BC) Connector . . . . . . . . . . . . . . . . 88                       |                                                                          |
|                                | Apply the Motor Cable Shield Clamp . . . . . . .                                                       | . . . . . . . . . . . .  . . . . . . . . . . . 90 . . . . . . . . . . 91 |
|                                | Feedback and I/O Cable Connections . . . . . . .                                                       | . . . . . . . . . . . .                                                  |
|                                | Flying-lead Feedback Cable Pinouts . . . . . . . . . . . . . . . . . . . . . . . . . . . 93            |                                                                          |
|                                | Wiring the Feedback and                                                                                |                                                                          |
|                                | I/O Connectors . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . . 95                                                       |

|                               | Connect Premolded Motor Feedback Cables. . . . . . . . . . . . . . . . . . . . 96                |                                                    |
|-------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------|
|                               | Connect Panel-mounted Breakout Board Kits                                                        | . . . . . . . . .  . . . . . . . . . 96            |
|                               | Wire Low-profile Connector Kits . . . . . . . .                                                  | . . . . . . . . . . . .  . . . . . . . . . . 97    |
|                               | External Shunt Module Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99  |                                                    |
|                               | IPIM Module Connections .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           | . . . . . . . 100                                  |
|                               | RBM Module Connections . . . . . .  . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . 101                    |
|                               | Sercos Fiber-optic Cable Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102 |                                                    |
|                               | Kinetix 6000M Integrated Drive-Motor Sercos Connections . . . . . . . 104                        |                                                    |
|                               | Ethernet Cable Connections . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . 105                                    |
|                               | Chapter 6                                                                                        |                                                    |
| Configure and Start the       | Configure the Kinetix 6000M Integrated Drive-Motor System. . . . . . 107                         |                                                    |
| Kinetix 6000                  | Configure the Drive Modules. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . 108                                    |
|                               | Configure the Logix 5000 Sercos interface Module . . . . . . . . . . . . . . . . 114             |                                                    |
| Drive System                  | Configure the Logix 5000 Controller . . . .                                                      | . . . . . . . . . . . .  . . . . . . . . . 114     |
|                               | Configure the Logix 5000 Module . . . . . . .                                                    | . . . . . . . . . . . .  . . . . . . . . . 115     |
|                               | Configure the Kinetix 6000 Drive Modules . . . . . . . . . . . . . . . . . . . . 117             |                                                    |
|                               | Configure the Motion Group. . . . . . . . . . . . . . . . .                                      | . . . . . . . . .  . . . . . . . 120               |
|                               | Configure Axis Properties . . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . 121                    |
|                               | Download the Program . .  . . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . 124                |
|                               | Apply Power to the                                                                               |                                                    |
|                               | Kinetix 6000 Drive . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . . . . . . 124                          |
|                               | Test and Tune the Axes . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . 126                          |
|                               | Test the Axes . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . 126                |
|                               | Tune the Axes . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . . . . . . . . . . 128                          |
|                               | Configure Drive Parameters and System Variables . . . . . . . . . . . . . . . . 130              |                                                    |
|                               | Tools for Changing Parameters . . . . . . . . . .                                                | . . . . . . . . . . . .  . . . . . . . . 130       |
|                               | Monitor System Variables with Analog Test Points. . . . . . . . . . . . . 131                    |                                                    |
|                               | Chapter 7                                                                                        |                                                    |
| Troubleshoot the Kinetix 6000 | Safety Precautions . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . . . . . . 133                          |
| Drive System                  | Interpret Status Indicators.  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . 133                                  |
|                               | Kinetix 6000M IDM System Error Codes. . .                                                        | . . . . . . . . . . .  . . . . . . . . 133         |
|                               | Kinetix 6000 Drive System Error Codes. . . . . . . . . . . . . . . . . . . . . . . 134           |                                                    |
|                               | IAM/AM Module Status Indicators . . . . . . .                                                    | . . . . . . . . . . . .  . . . . . . . . 138       |
|                               | Shunt Module Status Indicators . . . . . . . .                                                   | . . . . . . . . . . . .  . . . . . . . . . 139     |
|                               | General System Anomalies . . . . .  . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . 140                  |
|                               | Logix 5000/Drive Fault Behavior . . . . . . . . .                                                | . . . . . . . . . . . . .  . . . . . . . . . . 142 |
|                               | Chapter 8                                                                                        |                                                    |
| Remove and Replace the        | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . . . . . . . . . . . 147                          |
| Kinetix 6000                  | Remove Kinetix 6000 Drive Modules. . . . . . . .                                                 | . . . . . . . . . . . .  . . . . . . . . . 147     |
| Drive Modules                 | Replace Kinetix 6000 Drive Modules .   . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . 148                      |
|                               | Remove the Power Rail . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . . . . . . . . . . 149                            |
|                               | Replace the Power Rail . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . . . . 150                          |
|                               | Appendix A                                                                                       |                                                    |
| Interconnect Diagrams         | Interconnect Diagram Notes .   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . . . . . . 151                                    |

|                              | Power Wiring Examples . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . 152                            |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
|                              | DC Common Bus Wiring Examples . . . . . . .                                                                                                   | . . . . . . . . . . .  . . . . . . . . 156         |
|                              | Shunt Module Wiring Examples  . . . . . . . . . . . . . . . .                                                                                 | . . . . . . . . . . . . . 159                      |
|                              | Axis Module/Rotary Motor Wiring Examples .                                                                                                    | . . . . . . . . . . .  . . . . . . . . . 160       |
|                              | Axis Module/Linear Motor/Actuator Wiring Examples. . . . . . . . . . . . . 169                                                                |                                                    |
|                              | Kinetix 6000M Integrated Drive-Motor Wiring Example . . . . . . . . . . 175                                                                   |                                                    |
|                              | Brake Current Example. . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                     | . . . . . . . . . . . . . . . 176                  |
|                              | System Block Diagrams. . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                     | . . . . . . . . . . . . . . . 176                  |
|                              | Appendix B                                                                                                                                    |                                                    |
| Upgrade the Drive Firmware   | Upgrade Kinetix 6000M System Firmware . . . . . . . . . . . . . . . . . . . . . . . 181                                                       |                                                    |
|                              | Upgrade Drive Firmware with ControlFLASH Software. . . . . . . . . . . . 181                                                                  |                                                    |
|                              | Before You Begin . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                           | . . . . . . . . . . 181                            |
|                              | Configure Logix 5000 Communication . . . . . . . . . . . . . . . . . . . . . . . 182                                                          |                                                    |
|                              | Upgrade Firmware. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                                                      | . . . . . . . . . . . . . . 183                    |
|                              | Verify the Firmware Upgrade . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186                                               |                                                    |
|                              | Appendix C                                                                                                                                    |                                                    |
| DC Common-bus Applications   | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . 189                          |
|                              | Calculate Total Bus Capacitance . . . . . . . . . .                                                                                           | . . . . . . . . . . . . .  . . . . . . . . . . 189 |
|                              | Calculate Additional Bus Capacitance . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190                                              |                                                    |
|                              | Bulletin 2094 Drive Capacitance Values . . . . . . . . . . . . . . . . . . . . . . . . . . 190                                                |                                                    |
|                              | Common Bus Capacitance Example . . . . . . . .                                                                                                | . . . . . . . . . . . .  . . . . . . . . . 191     |
|                              | Set the Additional Bus Capacitance Parameter . . . . . . . . . . . . . . . . . . . . 192                                                      |                                                    |
|                              | Remove Sercos Communication . . . . . . . . .                                                                                                 | . . . . . . . . . . . .  . . . . . . . . 193       |
|                              | Set the Additional Bus Capacitance Parameter . . . . . . . . . . . . . . . . 193                                                              |                                                    |
|                              | Save the Add Bus Cap Parameter to Nonvolatile Memory . . . . . . . 194                                                                        |                                                    |
|                              | Verify the Parameter Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195                                                |                                                    |
|                              | Reconnect Sercos Communication . . . . . . .                                                                                                  | . . . . . . . . . . . .  . . . . . . . . 195       |
|                              | Appendix D                                                                                                                                    |                                                    |
| Configure the Load Observer  | Benefits . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . 197                            |
| Feature                      | How it Works. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                            | . . . . . . . 197                                  |
|                              | Configuration . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . 198                          |
|                              | Remaining IDN Parameter Descriptions. . .                                                                                                     | . . . . . . . . . . .  . . . . . . . 200           |
|                              | Out-of-Box Gain Settings. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . .                                                          | . . . . . . 201                                    |
|                              | Auto-tune Gain Settings. . . . . .  . . . . . . . . . . . . . . . . .                                                                         | . . . . . . . . . . . . . . 204                    |
|                              | Tuning Mode Summary . . . . . . .  . . . . . . . . . . . . . . . .                                                                            | . . . . . . . . . . . . . . 206                    |
|                              | Manual Tuning for Further Optimization . .                                                                                                    | . . . . . . . . . . .  . . . . . . . . 207         |
|                              | Set Gains with Sercos IDN Write Messages . . . . . . . .                                                                                      | . . . . . . . . .  . . . . . . 208                 |
|                              | Appendix E                                                                                                                                    |                                                    |
| Change Default IDN Parameter | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . 211                          |
| Values                       | Change IDN Parameter Values . . .  . . . . . . . . . . . . . . . . .                                                                          | . . . . . . . . . . . . . . 212                    |
|                              | Read the Present IDN Parameter Value . . . . . . . . . . . . . . . . . . . . . . . 212                                                        |                                                    |
|                              | Calculate the New IDN Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213 Write the New IDN Parameter Value . . . . . . | . . . . . . . . . . .  . . . . . . . . 214         |

|                           | Appendix F                                                                                                                    |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Enhanced Peak Performance | Before You Begin . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . 217            |
|                           | Enhanced Peak Example. . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 218                    |
|                           | Enhanced Peak Example Calculation . . . . . . . . . . . . . . . . . . . . . . . . . 221                                       |
|                           | Change the Drive Parameter . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 222                      |
|                           | Sercos IDN Write Instruction. . . . . . . . .  . . . . . . . . . . . .  . . . . . . . . . . . 223                             |
|                           | DriveExplorer Software . . . . . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 224                        |
|                           | Appendix G                                                                                                                    |
| RBM Module Interconnect   | Before You Begin . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 225            |
| Diagrams                  | RBM Module Wiring Examples. . . . . . . . . . . . . . . . .  . . . . . . . . .  . . . . . . . . 225                           |
|                           | Appendix H                                                                                                                    |
| History of Changes        | History of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 237             |
|                           | Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . 241 |

## Notes:

## Summary of Changes

## Download Firmware, AOP, EDS, and Other Files

## Conventions Used in This Manual

This manual provides detailed installation instructions for mounting, wiring, and troubleshooting Kinetix® 6000 drives; and system integration for your drive and motor/actuator combination with a Logix 5000™ controller.

For information on wiring and troubleshooting your Kinetix 6000 servo drive with the safe torque-off feature, refer to the Kinetix Safe Torque-off Feature Safety Reference Manual, publication GMC-RM002 .

This manual is intended for engineers or technicians directly involved in the installation and wiring of the Kinetix 6000 drives; and programmers directly involved in the operation, field maintenance, and integration of these drives with a Sercos interface module.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic Page                                           |
|------------------------------------------------------|
| Added information about UK certification. throughout |

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

The conventions starting below are used throughout this manual.

- Bulleted lists such as this one provide information, not procedural steps.
- Numbered lists provide sequential steps or hierarchical information.
- Acronyms for the Kinetix 6000 drive modules are shown in these tables and are used throughout this manual

| Acronym Kinetix 6000 Drive Modules Cat. No.           |
|-------------------------------------------------------|
| IAM Integrated Axis Module 2094-xCxx-Mxx-x            |
| AM Axis Module 2094-xMxx - x                          |
| LIM Line Interface Module 2094-xLxx and 2094-xLxxS-xx |
| RBM Resistive Brake Module 2090-XBxx - xx             |

| Acronym Kinetix 6000M Drive Modules Cat. No.    |
|-------------------------------------------------|
| IDM Integrated Drive-Motor MDF-SBxxxxx          |
| IPIM IDM Power Interface Module 2094-SEPM-B24-S |

## IMPORTANT

Throughout this publication, when the IAM or AM module catalog number is followed by -x, for example 2094-BMP5-x , the variable (x) indicates that the drive catalog number (using this example) is either 2094-BMP5-S or 2094-BMP5.

.

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature.

|                                                                                                                    | Resource Description                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix Rotary Motion Specifications , publication KNX-TD001                                                       | Product specifications for Kinetix VPL, VPC, VPF, VPH, and VPS; Kinetix MPL, MPM, MPF, and MPS; Kinetix TLY and TL; Kinetix HPK; and Kinetix MMA rotary motors.                                                                                                                                                                                                                              |
| Kinetix Linear Motion Specifications, publication KNX-TD002                                                        | Provides product specifications for Kinetix MPAS and MPMA linear stages, Kinetix MPAR and MPAI electric cylinders, and Kinetix LDC and Kinetix LDL linear motors.                                                                                                                                                                                                                            |
| Kinetix Rotary and Linear Motion Cable Specifications, publication KNX-TD004                                       | Product specifications for Kinetix 2090 motor and interface cables.                                                                                                                                                                                                                                                                                                                          |
| Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications publication KNX-TD005                | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP™ network (Kinetix 6500 and Kinetix 350), Integrated Motion over Sercos interface (Kinetix 6200, Kinetix 6000, Kinetix 2000, and Kinetix 7000), and component (Kinetix 3) servo drive families.                                                                                                            |
| Line Interface Module Installation Instructions, publication 2094-IN005                                            | Provides information on the installation and troubleshooting of Bulletin 2094 line interface modules (LIM).                                                                                                                                                                                                                                                                                  |
| 2094 Mounting Bracket Installation Instructions, publication 2094-IN008                                            | Provides information on the installation of Bulletin 2094 mounting brackets.                                                                                                                                                                                                                                                                                                                 |
| Resistive Brake Module Installation Instructions, publication 2090-IN009                                           | Provides information on the installation and wiring of Bulletin 2090 Resistive Brake Modules.                                                                                                                                                                                                                                                                                                |
| Fiber-optic Cable Installation and Handling Instructions, publication 2090-IN010                                   | Provides information on proper handling, installing, testing, and troubleshooting fiber-optic cables.                                                                                                                                                                                                                                                                                        |
| External Shunt Modules Installation Instructions, publication 2090-IN004                                           | Provides information on mounting and wiring the Bulletin 1394 shunt modules with Bulletin 2094 servo drive systems.                                                                                                                                                                                                                                                                          |
| System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001                              | Provides information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                                                                                                                                                                                                                                              |
| Servo Drive Installation Best Practices Application Technique, publication MOTION-AT004                            | Best practice examples to help reduce the number of potential noise or electromagnetic interference (EMI) sources in your system and to make sure that the noise sensitive components are not affected by the remaining noise.                                                                                                                                                               |
| Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003                                           | Provides information on installing, configuring, startup, troubleshooting, and applications for your Kinetix 6000M integrated drive-motor (IDM) system.                                                                                                                                                                                                                                      |
| Kinetix Safe Torque-off Feature Safety Reference Manual, publication GMC-RM002                                     | Provides information on wiring and troubleshooting your Kinetix 6000 servo drives with the safe torque-off feature.                                                                                                                                                                                                                                                                          |
| Kinetix Motion Control Selection Guide, publication KNX-SG001                                                      | Provides overview of Kinetix servo drives, motors, actuators, and motion accessories designed to help make initial decisions for the motion control products best suited for your system requirements.                                                                                                                                                                                       |
| Kinetix 6000 and Kinetix 6200/6500 Drive Systems Design Guide, publication KNX-RM003                               | Provides information to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Includes system performance specifications and torque/speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application. |
| Motion Analyzer System Sizing and Selection Tool website https://motionanalyzer.rockwellautomation.com/            | Comprehensive motion application sizing tool used for analysis, optimization, selection, and validation of your Kinetix Motion Control system.                                                                                                                                                                                                                                               |
| Rockwell Automation® Configuration and Selection Tools, website rok.auto/systemtools                               | Provides online product selection and system configuration tools, including AutoCad (DXF) drawings.                                                                                                                                                                                                                                                                                          |
| Sercos and Analog Motion Configuration User Manual, publication MOTION-UM001                                       | Provides information on configuring and troubleshooting your ControlLogix®, CompactLogix™, and SoftLogix™ Sercos interface modules.                                                                                                                                                                                                                                                          |
| Motion Coordinate System User Manual, publication MOTION - UM002                                                   | Provides information to create a motion coordinate system with Sercos or analog motion modules.                                                                                                                                                                                                                                                                                              |
| SoftLogix Motion Card Setup and Configuration Manual, publication 1784-UM003                                       | Provides information on configuring and troubleshooting SoftLogix PCI cards.                                                                                                                                                                                                                                                                                                                 |
| ControlFLASH Firmware Upgrade Kit User Manual, publication 1756-QS105                                              | For ControlFLASH™ information not specific to any drive family.                                                                                                                                                                                                                                                                                                                              |
| EtherNet/IP Network Devices User Manual, ENET-UM006                                                                | Describes how to configure and use EtherNet/IP devices to communicate on the EtherNet/IP network.                                                                                                                                                                                                                                                                                            |
| Ethernet Reference Manual, ENET-RM002                                                                              | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                                                                                                                                                                                   |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                                                                                                                             |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-State Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components.                                                                                                              |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                                                                                                                                          |
|                                                                                                                    | Product Certifications website, rok.auto/certifications. Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                                                                                 |

## IAM/AM Module Series Changes

## Start

Use this chapter to become familiar with the design and installation requirements for Kinetix® 6000 drive systems.

| Topic Page                                                   |
|--------------------------------------------------------------|
| IAM/AM Module Series Changes 11                              |
| About the Kinetix 6000 Drive Systems 12                      |
| Typical Hardware Configurations 13                           |
| Typical Communication Configurations 17                      |
| Catalog Number Explanation 18                                |
| Kinetix Drive Component Compatibility 19                     |
| Kinetix 6000M Integrated Drive-Motor System Compatibility 19 |
| Agency Compliance 20                                         |

Kinetix 6000 series B and later (460V) drives include the peak current enhancement. The peak current ratings of the Kinetix 6000 (460V) drives are configured at the factory as 150% of continuous current. However, you can program 460V AM modules and the equivalent IAM (inverter) modules, for up to 250% of continuous inverter current.

Table 1 - Kinetix 6000 Enhanced Peak Performance Series Change

| IAM Module Cat. No.                    |                               |
|----------------------------------------|-------------------------------|
| AM Module Cat. No. Series A (inverter) | Series B and later (inverter) |
| 2094-BC01-MP5-S 2094-BMP5-S 150% 250%  |                               |
| 2094-BC01-M01-S 2094-BM01-S 150% 250%  |                               |
| 2094-BC02-M02-S 2094-BM02-S 150% 250%  |                               |
| 2094-BC04-M03-S 2094-BM03-S 150% 250%  |                               |
| 2094-BC07-M05-S 2094-BM05-S 150% 200%  |                               |

## IMPORTANT

Before your drive can deliver enhanced peak performance, you must enable the peak enhancement feature by configuring your drive with DriveExplorer™ software or the Logix Designer application.

Refer to Appendix F on page 217 to recalculate torque and acceleration or deceleration limit values, and paste them into the appropriate Axis Properties dialog box in the Logix Designer application.

For more information on setting axis properties, refer to Configure Axis Properties on page 121 .

In series C and later, a mechanical relay for the brake circuit and another for the safe torque-off inputs are replaced by solid-state relays to add robustness. All wiring is consistent with previous series releases.

<!-- image -->

## About the Kinetix 6000 Drive Systems

Table 2 - Kinetix 6000 Drive System Overview

| System Component         |                                                                                                                                                                      | Cat. No. Description                                                                                                                                                                                                                                                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integrated Axis Module   | 2094-xCxx-Mxx-S                                                                                                                                                      | Integrated Axis Modules (IAM) with the safe torque-off feature with 200V or 400V-class AC input power. Contains an inverter and  converter section. The peak enhancement feature is available on 400V-class (series B and later) IAM modules.                                                                                                          |
| Integrated Axis Module   | 2094-xCxx-Mxx                                                                                                                                                        | Integrated Axis Modules (IAM), with 200V or 400V-class AC input power (does not include the safe torque-off or peak-enhanced feature). Contains an inverter and converter section.                                                                                                                                                                     |
| Axis Module              | 2094-xMxx-S                                                                                                                                                          | Axis Modules (AM) with safe torque-off are shared DC-bus inverters and rated for 200 or 400V-class operation. The AM module must be used with an IAM module. The peak enhancement feature is available on 400V-class (series B and later) AM modules.                                                                                                  |
| Axis Module              | 2094-xMxx                                                                                                                                                            | Axis Modules (AM) are shared DC-bus inverters rated for 200V or 400V-class input power (does not include the safe torque-off or peak-enhanced feature). The AM module must be used with an IAM module.                                                                                                                                                 |
|                          |                                                                                                                                                                      | Shunt Module 2094-BSP2 The Bulletin 2094 shunt module mounts to the power rail and provides additional shunting in regenerative applications.                                                                                                                                                                                                          |
| Kinetix 6000M IDM System | 2094-SEPM-B24-S Bulletin MDF                                                                                                                                         | The Kinetix 6000M integrated drive-motor (IDM) system consists of the IDM power interface module (IPIM) and up to 16 (Bulletin MDF) IDM units. The IPIM module mounts on the Bulletin 2094 power rail and provides power and communication to the IDM units. The IPIM module also monitors power output and provides overload protection.              |
| Power Rail               | 2094-PRSx 2094-PRx                                                                                                                                                   | The Bulletin 2094 power rail consists of copper bus bars and a circuit board with connectors for each module. The power rail provides power and control signals from the converter section to adjacent inverters. The IAM and AM power modules, shunt module , slot-filler modules mount to the power rail.                                            |
| Slot-filler Module       | 2094-PRF                                                                                                                                                             | The Bulletin 2094 slot-filler module is used when one or more slots on the power rail are empty after all the other power rail modules are installed. One slot-filler module is required for each empty slot.                                                                                                                                          |
| Logix 5000™ Controllers  | 1756-MxxSE modules 1768-M04SE module 1784-PM16SE PCI card                                                                                                            | The Sercos interface module/PCI card serves as a link between the ControlLogix®/CompactLogix™/SoftLogix™ controllers and the Kinetix 6000 drive system. The communication link uses the IEC 61491 SErial Real-time COmmunication System (Sercos) protocol over a fiber-optic cable.                                                                    |
| Logix 5000™ Controllers  |                                                                                                                                                                      | 1756-ENxTx modules The Kinetix 6000M IPIM module connects to the EtherNet/IP™ network for monitoring, diagnostics, and firmware upgrades.                                                                                                                                                                                                              |
| Studio 5000® Environment | 9324-RLD300xxE                                                                                                                                                       | The Studio 5000 Logix Designer® application provides support for programming, commissioning, and maintaining the Logix 5000 family of controllers.                                                                                                                                                                                                     |
| Rotary Servo Motors      | Kinetix MP, Kinetix TL/TLY, Kinetix RDB, 1326AB, F-Series                                                                                                            | Compatible rotary motors include the Kinetix MPL, MPM, MPF, and MPS 200V and 400V-class motors; Kinetix RDB; Kinetix TL and TLY; 1326AB (M2L/S2L) and 1326AB (resolver); and F-Series motors.                                                                                                                                                          |
|                          | Linear Motors Kinetix LDC and Kinetix LDL Compatible motors include Kinetix LDC iron core (200V and 400V-class) and Kinetix LDL ironless (200V-class) linear motors. | Linear Motors Kinetix LDC and Kinetix LDL Compatible motors include Kinetix LDC iron core (200V and 400V-class) and Kinetix LDL ironless (200V-class) linear motors.                                                                                                                                                                                   |
| Linear Actuators         | Kinetix MP                                                                                                                                                           | Compatible actuators include Kinetix MPAS (200V and 400V-class) single-axis and Kinetix MPMA multi-axis integrated linear stages, and Kinetix MPAR and MPAI (200V and 400V-class) electric cylinders.                                                                                                                                                  |
| Linear Actuators         |                                                                                                                                                                      | Kinetix LDAT Kinetix LDAT integrated linear actuators are compatible with 200V and 400V-class drive systems.                                                                                                                                                                                                                                           |
| Cables                   | Kinetix 2090 power and feedback cables                                                                                                                               | Kinetix 2090 power and feedback cables are available with bayonet, threaded, and SpeedTec connectors. Power/brake cables have flying leads on the drive end and straight connectors that connect to servo motors. Feedback cables have flying leads that wire to low-profile connector kits on the drive end and straight connectors on the motor end. |
| Cables                   | Kinetix 6000M integrated drive-motor cables                                                                                                                          | Kinetix 2090 integrated drive-motor (IDM) hybrid and network cables connect between the 2094 IPIM module and the Kinetix 6000M IDM units. Bulletin 889D and 879D cables connect between digital input connectors and sensors.                                                                                                                          |
| Cables                   | Communication                                                                                                                                                        | Kinetix 2090 Sercos fiber-optic cables are available as enclosure only, PVC, nylon, and glass with connectors at both ends.                                                                                                                                                                                                                            |
| Cables                   | Communication                                                                                                                                                        | Ethernet cables are available in standard lengths for Kinetix 6000M IPIM modules. Shielded cable is recommended.                                                                                                                                                                                                                                       |
|                          | AC Line Filters 2090-XXLF-xxxx                                                                                                                                       | Bulletin 2090-XXLF-xxxx three-phase AC line filters are required to meet CE and UK in all 200V and 400V-class drive systems.                                                                                                                                                                                                                           |
| Line Interface Modules   | 2094-xLxx 2094-xLxxS 2094-XL75S-Cx                                                                                                                                   | Line interface modules (LIM) include the circuit breakers, AC line filter (catalog numbers 2094-AL09 and 2094-BL02 only), power supplies, and safety contactor required for Kinetix 6000 operation. The LIM module does not mount to the power rail. You can purchase individual components separately in place of the LIM module.                     |
| External Shunt Modules   | 1394-SRxxxx                                                                                                                                                          | You can use Bulletin 1394 external passive shunt modules when the IAM/AM module internal shunt and power rail mounted 2094- BSP2 shunt module capability is exceeded.                                                                                                                                                                                  |
| Resistive Brake Module   | 2090-XBxx-xx                                                                                                                                                         | Resistive Brake Modules (RBM) include a safety contactor for use in a control circuit. Contactors and resistors reside in this module such that the motor leads can be disconnected from the drive with the permanent magnet motor brought to an immediate stop. This  module does not mount to the power rail.                                        |

The Kinetix 6000 multi-axis servo drives are designed to provide a Kinetix Integrated Motion solution for your drive/motor/actuator applications.

## Typical Hardware Configurations

Typical Kinetix 6000 system installations include three-phase AC configurations, with and without the line interface module (LIM), and DC common-bus configurations.

<!-- image -->

SHOCK HAZARD: To avoid personal injury due to electrical shock, place a 2094-PRF slot-filler module in all empty slots on the power rail. Any power rail connector without a module installed disables the Bulletin 2094 system; however, control power is still present.

Figure 1 - Typical Kinetix 6000 System Installation (with LIM)

<!-- image -->

(1) Kinetix RDB direct-drive servo motors require the 2090-K6CK-KENDAT low-profile feedback module.

Figure 2 - Typical Kinetix 6000 System Installation (without LIM)

<!-- image -->

(1) Kinetix RDB direct-drive servo motors require the 2090-K6CK-KENDAT low-profile feedback module.

This configuration illustrates the Kinetix 6000M integrated drive-motor (IDM) system with IDM power interface module (IPIM) installed on the Bulletin 2094 power rail. The IPIM module is included in the drive-to-drive fiber-optic cable installation along with the axis modules.

<!-- image -->

For more information on Kinetix 6000M integrated drive-motor system installation, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Figure 4 - Typical (400V-class) DC Common Bus System Installation

Axis Modules (5)

<!-- image -->

In the example above, the leader IAM module is connected to the follower IAM module via the DC common-bus. The follower system also includes the Kinetix 6000M integrated drive-motor (IDM) power interface module (IPIM) that supports up to 16 IDM units.

When planning your panel layout, you must calculate the total bus capacitance of your DC common-bus system to be sure that the leader IAM module is sized sufficiently to precharge the entire system. Refer to Appendix C for more information.

## IMPORTANT

If total bus capacitance of your system exceeds the leader IAM module precharge rating and input power is applied, the IAM module seven-segment status indicator displays error code E90 (precharge timeout fault).

To correct this condition, you must replace the leader IAM module with a larger module or decrease the total bus capacitance by removing the IPIM module or AM modules.

## Typical Communication Configurations

In this example, drive-to-drive Sercos cables and catalog numbers are shown when Kinetix 6000, Kinetix 6000M, and Kinetix 6200 drive modules exist on the same power rail.

The Kinetix 6200 control modules use Sercos interface for configuring the Logix 5000 module and the EtherNet/IP network for diagnostics and configuring safety functions. An Ethernet cable is connected to each control module during safety configuration. For more information on Ethernet cables, refer to the Industrial Ethernet Media Brochure, publication 1585-BR001 .

Figure 5 - Typical Kinetix 6000 and Kinetix 6200 Communication (Sercos)

2094-BMxx-S Single-wide AM Module

<!-- image -->

Catalog Number Explanation Kinetix 6000 (Bulletin 2094) drive catalog numbers and descriptions are listed
ihfllibl in the following tables.

## IMPORTANT

Throughout this publication, when the IAM or AM module catalog number is followed by -x, for example 2094-BMP5-x, the variable (x) indicates that the drive module may or may not include the safe torque-off feature.

Table 3 - Kinetix 6000 Drive Catalog Numbers

| Integrated Axis Modules (230V)                                                              | Cat. No. (with safe torque-off feature)   | Cat. No. (without safe torque-off feature)   |
|---------------------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------------|
| Kinetix 6000, IAM, 200V-class, 3 kW converter, 5 A inverter 2094-AC05-MP5-S 2094-AC05-MP5   |                                           |                                              |
| Kinetix 6000, IAM, 200V-class, 3 kW converter, 9 A inverter 2094-AC05-M01-S 2094-AC05-M01   |                                           |                                              |
| Kinetix 6000, IAM, 200V-class, 6 kW converter, 15 A inverter 2094-AC09-M02-S 2094-AC09-M02  |                                           |                                              |
| Kinetix 6000, IAM, 200V-class, 11 kW converter, 24 A inverter 2094-AC16-M03-S 2094-AC16-M03 |                                           |                                              |
| Kinetix 6000, IAM, 200V-class, 23 kW converter, 49 A inverter 2094-AC32-M05-S 2094-AC32-M05 |                                           |                                              |
| Integrated Axis Modules (460V)                                                              |                                           |                                              |
| Kinetix 6000, IAM, 400V-class, 6 kW converter, 4 A inverter                                 | 2094-BC01-MP5-S (1)                       | 2094-BC01-MP5                                |
| Kinetix 6000, IAM, 400V-class, 6 kW converter, 9 A inverter                                 | 2094-BC01-M01-S (1)                       | 2094-BC01-M01                                |
| Kinetix 6000, IAM, 400V-class, 15 kW converter, 15 A inverter                               | 2094-BC02-M02-S (1)                       | 2094-BC02-M02                                |
| Kinetix 6000, IAM, 400V-class, 28 kW converter, 30 A inverter                               | 2094-BC04-M03-S (1)                       | 2094-BC04-M03                                |
| Kinetix 6000, IAM, 400V-class, 45 kW converter, 49 A inverter                               | 2094-BC07-M05-S (2)                       | 2094-BC07-M05                                |
| Axis Modules (230V)                                                                         |                                           |                                              |
| Kinetix 6000, AM, 200V-class, 5 A 2094-AMP5-S 2094-AMP5                                     |                                           |                                              |
| Kinetix 6000, AM, 200V-class, 9 A 2094-AM01-S 2094-AM01                                     |                                           |                                              |
| Kinetix 6000, AM, 200V-class, 15 A 2094-AM02-S 2094-AM02                                    |                                           |                                              |
| Kinetix 6000, AM, 200V-class, 24 A 2094-AM03-S 2094-AM03                                    |                                           |                                              |
| Kinetix 6000, AM, 200V-class, 49 A 2094-AM05-S 2094-AM05                                    |                                           |                                              |
| Axis Modules (460V)                                                                         |                                           |                                              |
| Kinetix 6000, AM, 400V-class, 4 A                                                           | 2094-BMP5-S (1)                           | 2094-BMP5                                    |
| Kinetix 6000, AM, 400V-class, 9 A                                                           | 2094-BM01-S (1)                           | 2094-BM01                                    |
| Kinetix 6000, AM, 400V-class, 15 A                                                          | 2094-BM02-S (1)                           | 2094-BM02                                    |
| Kinetix 6000, AM, 400V-class, 30 A                                                          | 2094-BM03-S (1)                           | 2094-BM03                                    |
| Kinetix 6000, AM, 400V-class, 49 A                                                          | 2094-BM05-S (2)                           | 2094-BM05                                    |

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
| 2094-BCxx-Mxx-S (series B and later) | N/A                                                                      |                        | Fully compatible Fully compatible Not compatible |                                                |
| 2094-BCxx-Mxx-M (IAM power module)   | 2094-SE02F-M00-Sx Sercos interface 2094-EN02D-M01-Sx EtherNet/IP network |                        |                                                  | Not compatible Not compatible Fully compatible |

For additional information on the 2094-BCxx-Mxx-M (IAM) and 2094-BMxx-M (AM) modules, refer to the Kinetix 6200 and Kinetix 6500 Multi-axis Servo Drives User Manual, publication 2094-UM002 .

Bulletin 2094 power rails with Kinetix 6000 (series B and later) or Kinetix 6200 drives are compatible with Kinetix 6000M integrated drive-motor (IDM) systems. The IDM power interface module (IPIM) mounts to the power rail and connects to as many as 16 IDM units.

## Table 6 - IPIM Module Compatibility

|                                      | IAM Module Control Module                                                               | 2094-SEPM-B24-S IDM Power Interface Module (IPIM)   |
|--------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------|
| 2094-BCxx-Mxx-S (series B and later) | N/A                                                                                     | Fully compatible                                    |
| 2094-BCxx-Mxx-M (IAM power module)   | 2094-SE02F-M00-Sx Sercos interface 2094-EN02D-M01-Sx EtherNet/IP network Not compatible | Fully compatible                                    |

For more information on Kinetix 6000M integrated drive-motor system installation, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

## Agency Compliance

If this product is installed within the European Union and has the CE mark, or within the United Kingdom and has the UKCA mark, the following regulations apply.

<!-- image -->

ATTENTION: Meeting CE and UK requires a grounded system, and the method of grounding the AC line filter and drive must match. Failure to do this renders the filter ineffective and can cause damage to the filter. For grounding examples, refer to Grounded Power Configurations on page 67 .

For more information on electrical noise reduction, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## CE and UK Requirements (system without LIM module)

To meet CE and UK requirements when your Kinetix 6000 system does not include the LIM module, these requirements apply.

- Install 2090-XXLF-xxxx AC line filters for three-phase input power and single-phase control power (for example, Schaffner P/N FN 355-10-05 or Roxburgh P/N RES5F08) as close to the IAM module as possible.
- Use Kinetix 2090 motor power cables or use connector kits and terminate the cable shields to the chassis clamp provided.
- Combined motor power cable lengths for all Kinetix 6000 axes and hybrid cable lengths for all IDM units on the same DC bus must not exceed 240 m (787 ft) with 400V-class systems or 160 m (525 ft) with 200V-class systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).
- Use Kinetix 2090 motor feedback cables or use connector kits and properly terminate the feedback cable shield. Drive-to-motor feedback cables must not exceed 90 m (295.5 ft).
- Install the Kinetix 6000 system inside an enclosure. Run input power wiring in conduit (grounded to the enclosure) outside of the enclosure. Separate signal and power cables.

See Appendix A for interconnect diagrams, including input power wiring and drive/motor interconnect diagrams.

## CE and UK Requirements (system with LIM module)

To meet CE and UK requirements when your Kinetix 6000 system includes the LIM module, follow all the requirements as stated in CE and UK Requirements (system without LIM module) and these additional requirements as they apply to the AC line filter.

- Install the LIM module (catalog numbers 2094-AL09 or 2094-BL02) as close to the IAM module as possible.
- Install the LIM module (catalog numbers 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx) with line filter (catalog number 2090-XXLF-xxxx) as close to the IAM module as possible.

When the LIM module (catalog numbers 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx) supports two IAM modules, each IAM module requires an AC line filter installed as close to the IAM module as possible.

## System Design Guidelines

<!-- image -->

## Plan the Kinetix 6000 Drive System Installation

This chapter describes system installation guidelines used in preparation for mounting your Kinetix® 6000 drive components.

| Topic Page                    |
|-------------------------------|
| System Design Guidelines 21   |
| Electrical Noise Reduction 27 |

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

Use the information in this section when designing your enclosure and planning to mount your system components on the panel.

For on-line product selection and system configuration tools, including AutoCAD (DXF) drawings of the product, refer to http://www.rockwellautomation.com/en/e-tools .

## System Mounting Requirements

- To comply with UL, CE, and UK requirements, the Kinetix 6000 drive system must be enclosed in a grounded conductive enclosure offering protection as defined in standard EN/IEC 60529 to IP54 such that they are not accessible to an operator or unskilled person. A NEMA 4X enclosure exceeds these requirements providing protection to IP66.
- The panel you install inside the enclosure for mounting your system components must be on a flat, rigid, vertical surface that won't be subjected to shock, vibration, moisture, oil mist, dust, or corrosive vapors.
- Size the drive enclosure so as not to exceed the maximum ambient temperature rating. Consider heat dissipation specifications for all drive components.
- Combined motor power cable lengths for all axes and hybrid cable lengths for all IDM units on the same DC bus must not exceed 240 m (787 ft) with 400V-class systems or 160 m (525 ft) with 200V-class systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).

## IMPORTANT

System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.

- Segregate input power wiring and motor power cables from control wiring and motor feedback cables. Use shielded cable for power wiring and provide a grounded 360° clamp termination.
- Use high-frequency (HF) bonding techniques to connect the modules, enclosure, machine frame, and motor housing, and to provide a lowimpedance return path for high-frequency (HF) energy and reduce electrical noise.

Refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, to better understand the concept of electrical noise reduction.

## Transformer Selection

The IAM module does not require an isolation transformer for three-phase input power. However, a transformer can be required to match the voltage requirements of the controller to the available service.

To size a transformer for the main AC power inputs, refer to the Kinetix 6000 power specifications in the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications, publication KNX-TD005 .

IMPORTANT If using an autotransformer, make sure that the phase to neutral/

ground voltages do not exceed the input voltage ratings of the drive.

## IMPORTANT

Use a form factor of 1.5 for three-phase power (where form factor is used to compensate for transformer, drive module, and motor losses, and to account for utilization in the intermittent operating area of the torque speed curve).

For example, to size a transformer to the voltage requirements of a 2094-BC01-M01-S integrated axis module:

2094-BC01-M01-S = 6 kW continuous x 1.5 = 9.0 KVA transformer

## AC Line Filter Selection

These AC line filters are available for your servo drive input power.

Table 7 - Kinetix 6000 (three-phase) AC Line Filter Selection

| Drive Cat. No.  Current A @ 50 °C (122 °F) Weight, approx kg (lb)   | Voltage          | AC Line Filter Cat. No.      |
|---------------------------------------------------------------------|------------------|------------------------------|
| 2094-AC05-MP5-S                                                     | 500V AC 50/60 Hz | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-AC05-M01-S                                                     | 500V AC 50/60 Hz | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-AC09-M02-S                                                     | 500V AC 50/60 Hz | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-AC16-M03-S 75 5.2 (11.4) 2090-XXLF-375                         | 500V AC 50/60 Hz |                              |
| 2094-AC32-M05-S 100 9.5 (20.9) 2090-XXLF-3100                       | 500V AC 50/60 Hz |                              |
| 2094-BC01-MP5-S                                                     | 500V AC 50/60 Hz | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-BC01-M01-S                                                     | 500V AC 50/60 Hz | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-BC02-M02-S                                                     | 500V AC 50/60 Hz | 30 2.7 (5.9) 2090-XXLF-X330B |
| 2094-BC04-M03-S 75 5.2 (11.4) 2090-XXLF-375B                        | 500V AC 50/60 Hz |                              |
| 2094-BC07-M05-S 100 9.5 (20.9) 2090-XXLF-3100                       | 500V AC 50/60 Hz |                              |

Refer to the Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for additional AC line filter specifications.

## Circuit Breaker/Fuse Options

The 2094-xCxx-Mxx-S and 2094-xMxx-S drive modules, and the Kinetix 6000M integrated drive-motor system (2094-SEPM-B24-S IPIM module and MDF-SBxxxxx IDM units) use internal solid-state motor short-circuit protection and, when protected by suitable branch circuit protection, are rated for use on a circuit capable of delivering up to 200,000 A (fuses) and 65,000 A (circuit breakers).

Table 8 - Control and DC-bus Circuit Protection Specifications

| IAM Module Cat. No.                             | Control Input Power DC-bus Power     |                                              |                                |
|-------------------------------------------------|--------------------------------------|----------------------------------------------|--------------------------------|
|                                                 | Bussmann Fuse (1)                    | Allen-Bradley® Circuit Breaker  (2) (non-UL) | Bussmann Fuse  Mersen Fuse (3) |
| 2094-AC05-MP5-S                                 | FNQ-R-10 (10 A)                      | 1492-SPM2D060                                | N/A A50P20-1                   |
| 2094-AC05-M01-S                                 |                                      |                                              |                                |
| FNQ-R-10 (10 A)2094-AC09-M02-S FWH-35B A50P35-4 |                                      |                                              |                                |
| 2094-AC16-M03-S                                 |                                      | 1492-SPM2D200                                | FWH-60B A50P60-4               |
| 2094-AC32-M05-S FWH-125B A50P125-4              |                                      |                                              |                                |
| 2094-BC01-MP5-S                                 | FNQ-R-10 (10 A) or FNQ-R-7.5 (7.5 A) | 1492-SPM2D060 or 1492-SPM1D150 FNQR10 (10 A) or FNQR75 (75 A) 1492SPM2D060 or 1492SPM1D150 2094-BC02-M02-S FWJ-40A A70QS40-4 HSJ40                                              | FWJ-20A14F DCT20-2 HSJ20       |
| 2094-BC01-M01-S                                 |                                      |                                              |                                |
| 2094-BC04-M03-S FWJ-70A A70QS70-4 HSJ70         |                                      |                                              |                                |
| 2094-BC07-M05-S FWJ-125A A70QS125-4 HSJ125      |                                      |                                              |                                |

(2) Use 1492-SPM1D150 circuit breaker for higher single -cycle inrush current capability. This is recommended when the continuous control-power current exceeds 3.0 A.

(3) Mersen fuses were formerly known as Ferraz Shawmut.

## Input Power Circuit Protection (LIM)

The 2094-AL09 and 2094-BL02 line interface modules (LIM) contain supplementary protection devices and, when protected by suitable branch circuit protection, are rated for use on a circuit capable of delivering up to 5000 A. When these modules are used, protection on the line side of the LIM module is required. Fuses must be class J or CC only.

The 2094-ALxxS, 2094-BLxxS, and 2094-XL75S-Cx LIM modules contain branch circuit rated devices suitable for use on a circuit capable of delivering up to 65,000 A (400V-class) or 100,000 A (200V-class).

Refer to the Line Interface Module Installation Instructions, publication 2094-IN005, for power specifications and more information on using the LIM module.

Refer to Input Power Circuit Protection (without LIM) on page 23 when your drive system does not include the LIM module.

## Input Power Circuit Protection (without LIM)

The fuses and Allen-Bradley circuit breakers shown in Table 9 are recommended for use with 2094-xCxx-Mxx-S IAM modules when the line interface module (LIM) is not used.

## IMPORTANT

LIM Modules (catalog numbers 2094-ALxxS, 2094-BLxxS, and 2094-XL75S-Cx) provide branch circuit protection to the IAM module. Follow all applicable NEC and local codes.

Table 9 - Input Power Circuit Protection Specifications

|                                                     | Kinetix 6000 Drives UL Applications IEC (non-UL) Applications   | Kinetix 6000 Drives UL Applications IEC (non-UL) Applications   | Kinetix 6000 Drives UL Applications IEC (non-UL) Applications   | Kinetix 6000 Drives UL Applications IEC (non-UL) Applications   |                           |    |                              |                             |
|-----------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|---------------------------|----|------------------------------|-----------------------------|
| IAM Module Cat. No. Drive Voltage (three-phase) nom | Fuses (Bussmann) Cat. No.                                       | Miniature CB Cat. No.                                           | Motor Protection CB, Self-protected CMC Cat. No.                | Molded Case CB Cat. No.                                         | Miniature CB Cat. No.     |    | Motor Protection CB Cat. No. | Molded Case CB Cat. No.     |
| 2094-AC05-MP5-S 230V                                | KTK-R-20 (20 A) Class CC                                        | 1489-M3D300                                                     | 140M-F8E-C16                                                    | – – 140M-F8E-C16 140M-F8E-C16                                                                 | 1492-SPM3D300 1489-M3D300 |    | 140M-F8E-C16                 | –                           |
| 2094-AC05-M01-S 230V                                | KTK-R-20 (20 A) Class CC                                        | 1489-M3D300                                                     |                                                                 | – – 140M-F8E-C16 140M-F8E-C16                                                                 | 1492-SPM3D300 1489-M3D300 |    |                              | –                           |
| 2094-AC09-M02-S 230V                                | KTK-R-30 (30 A) Class CC                                        | –                                                               |                                                                 | 140M-F8E-C20 1492-SPM3D400                                      |                           | –  | 140M-F8E-C20                 |                             |
| 2094-AC16-M03-S 230V                                | LPJ-45SP (45 A) Class J                                         | –                                                               | –                                                               | 140G-G6C3-C50 140G-G6C3-C90 140G-G6C3-C90                       |                           | –  | – –                          | 140G-G6C3-C50               |
| 2094-AC32-M05-S 230V                                | LPJ-80SP (80 A) Class J                                         | –                                                               | –                                                               |                                                                 |                           | –  | – –                          |                             |
| 2094-BC01-MP5-S 360…480V                            | KTK-R-20 (20 A) Class CC                                        | 1489-M3D300                                                     | 140M-F8E-C32                                                    | – – 140M-F8E-C32 140M-F8E-C32                                                                 | 1492-SPM3D300 1489-M3D300 |    | 140M-F8E-C32                 | –                           |
| 2094-BC01-M01-S 360…480V                            | KTK-R-20 (20 A) Class CC                                        | 1489-M3D300                                                     |                                                                 | – – 140M-F8E-C32 140M-F8E-C32                                                                 | 1492-SPM3D300 1489-M3D300 |    |                              | –                           |
| 2094-BC02-M02-S 360…480V                            | KTK-R-30 (30 A) Class CC                                        | –                                                               |                                                                 | 140M-F8E-C45 1492-SPM3D400                                      |                           |    | 140M-F8E-C45                 |                             |
| 2094-BC04-M03-S 360…480V                            | LPJ-45SP (45 A) Class J                                         | –                                                               | –                                                               | 140G-G6C3-C50                                                   | – –                       |    |                              | – 140G-G6C3-C50             |
| 2094-BC07-M05-S 360…480V                            | LPJ-80SP (80 A) Class J                                         | –                                                               | –                                                               |                                                                 | – –                       |    |                              | 140G-G6C3-C90 140G-G6C3-C90 |

Refer to the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications, publication KNX-TD005, for additional power specifications for your IAM module.

## Enclosure Selection

This example is provided to assist you in sizing an enclosure for your Bulletin 2094 drive system. The example system consists of these components:

- 6-axis Bulletin 2094 servo drive system
- Line Interface Module (LIM)
- ControlLogix® chassis and modules (controller)

Size the Bulletin 2094 servo drive and LIM module and use the results to predict the amount of heat dissipated into the enclosure. You also need heat dissipation data from other equipment inside the enclosure (such as the ControlLogix controller). Once the total amount of heat dissipation (in watts) is known, you can calculate the minimum enclosure size.

Table 10 - Bulletin 2094 System Heat Dissipation Example

| Enclosure Component Description   |                                                                             | Loading (1)  Heat Dissipation  watts   |
|-----------------------------------|-----------------------------------------------------------------------------|----------------------------------------|
| 2094-BC02-M02-x                   | Integrated axis module (IAM), 400/460V                                      | 15 kW (converter section) 20% 44       |
| 2094-BC02-M02-x                   | Integrated axis module (IAM), 400/460V                                      | 15 A (inverter section) 40% 72         |
| 2094-BM02-x                       | Axis module (AM), 400/460V, 15 A 60% 93                                     |                                        |
| 2094-BM02-x                       | Axis module (AM), 400/460V, 15 A 60% 93                                     |                                        |
| 2094-BM01-x                       | Axis module (AM), 400/460V, 9 A 40% 73                                      |                                        |
| 2094-BM01-x                       | Axis module (AM), 400/460V, 9 A 40% 73                                      |                                        |
| 2094-BM01-x                       | Axis module (AM), 400/460V, 9 A 20% 57                                      |                                        |
|                                   | 2094-BL25S Line interface module (LIM), 400/460V, 25 A; 24V DC 20 A 100% 43 |                                        |

Table 10 - Bulletin 2094 System Heat Dissipation Example (Continued)

| Enclosure Component Description                       | Loading (1)  Heat Dissipation  (1) watts   |                                   |
|-------------------------------------------------------|--------------------------------------------|-----------------------------------|
| 2094-PRS6 Power rail, 460V, 6 axis N/A 0              |                                            |                                   |
| 2090-XB33-32 Resistive brake module (RBM), 33 A, 32  | N/A 30                                     |                                   |
| Total Kinetix 6000 system wattage                     | 578                                        | Total Kinetix 6000 system wattage |

Table 11 - ControlLogix System Heat Dissipation Example

| Enclosure Component Description                 | Backplane Power Load  (1) watts         | Heat Dissipation  (1) watts            |
|-------------------------------------------------|-----------------------------------------|----------------------------------------|
| 1756-M08SE 8-axis Sercos interface module 3.2 0 |                                         |                                        |
| 1756-L5563 L63 ControlLogix processor 4.5 0     |                                         |                                        |
| 1756-IB16D 16 -point input module 0.84 5.8      |                                         |                                        |
| 1756-OB16D 16 -point output module 4.64 3.3     |                                         |                                        |
| 1756-ENxTx                                      | EtherNet/IP™ communication module 4.0 0 |                                        |
| Backplane total                                 | 17.18 (2)                               | N/A                                    |
| 1756-PB72 24V DC ControlLogix power supply N/A  |                                         | 25 (2)                                 |
| 1756-A7 7-slot mounting chassis N/A N/A         |                                         |                                        |
| Total ControlLogix system wattage 34.1          | Total ControlLogix system wattage 34.1  | Total ControlLogix system wattage 34.1 |

## Figure 6 - ControlLogix Real Power

<!-- image -->

For backplane power loading requirements of other ControlLogix power supplies, refer to the ControlLogix Selection Guide, publication 1756-SG001 .

In this example, the amount of power dissipated inside the cabinet is the sum of the Bulletin 2094 system value (578 W) and the ControlLogix system value (34 W) for a total of 612 W.

With no active method of heat dissipation (such as fans or air conditioning) either of these approximate equations can be used.

|                                                                                                                     | Metric Standard English   |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|
| Where T is temperature difference between inside air ° p and outside ambient (°C), Q is heat generated in enclosure (Watts), and A is enclosure surface area (m 2 ). The exterior surface of all six sides of an enclosure is calculated as:                                                                                                                     | Where T is temperature difference between inside air ° p and outside ambient (°F), Q is heat generated in g enclosure (Watts), and A is enclosure surface area (ft²). The exterior surface of all six sides of an enclosure is calculated as:                           |
| A = 2dw + 2dh + 2wh A = (2dw + 2dh + 2wh) / 144                                                                     |                           |
| Where d (depth), w (width), and h (height) are in meters. Where d (depth), w (width), and h (height) are in inches. |                           |

Total system watts dissipated (Q) was calculated at 612 W. The maximum ambient rating of the Bulletin 2094 system is 50 °C (122 °F) and if the maximum environmental temperature is 30 °C (86 °F), then T=20 in the equation below.

<!-- formula-not-decoded -->

Table 12 - Power Dissipation Specifications

| Bulletin 2094 Drive Modules (1)             | Usage as % of Rated Power Output (watts)   | Usage as % of Rated Power Output (watts)   | Usage as % of Rated Power Output (watts)   | Usage as % of Rated Power Output (watts)   | Usage as % of Rated Power Output (watts)   |
|---------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| Bulletin 2094 Drive Modules (1)             |                                            | 20% 40% 60% 80% 100%                       |                                            |                                            |                                            |
| IAM (converter) module (2)                  |                                            |                                            |                                            |                                            |                                            |
| 2094-AC05-MP5-S                             |                                            | 8 11 15 19 24                              |                                            |                                            |                                            |
| 2094-AC05-M01-S                             |                                            | 9 12 16 20 25                              |                                            |                                            |                                            |
| 2094-AC09-M02-S                             |                                            | 14 20 28 36 46                             |                                            |                                            |                                            |
| 2094-AC16-M03-S                             |                                            | 19 30 43 58 74                             |                                            |                                            |                                            |
| 2094-AC32-M05-S                             |                                            | 41 68 100 136 176                          |                                            |                                            |                                            |
| 2094-BC01-MP5-S                             |                                            | 18 21 25 29                                | 34                                         |                                            |                                            |
| 2094-BC01-M01-S                             |                                            | 18 21 25 29                                | 33                                         |                                            |                                            |
| 2094-BC02-M02-S                             |                                            | 36 44 54 64 75                             |                                            |                                            |                                            |
| 2094-BC04-M03-S                             |                                            | 50 67 87 110 135                           |                                            |                                            |                                            |
| 2094-BC07-M05-S                             |                                            | 71 101 137 179 226                         |                                            |                                            |                                            |
| IAM (inverter) module or AM module (2)      | IAM (inverter) module or AM module (2)     |                                            |                                            |                                            |                                            |
| 2094-AC05-MP5-S or 2094-AMP5-S              |                                            | 28 32 37 41 46                             |                                            |                                            |                                            |
| 2094-AC05-M01-S or 2094-AM01-S              |                                            | 31 38 46 54 62                             |                                            |                                            |                                            |
| 2094-AC09-M02-S or 2094-AM02-S              |                                            | 34 45 57 70 84                             |                                            |                                            |                                            |
| 2094-AC16-M03-S or 2094-AM03-S              |                                            |                                            | 48 68 91 116 144                           |                                            |                                            |
| 2094-AC32-M05-S or 2094-AM05-S              |                                            | 104 156 212 274 342                        |                                            |                                            |                                            |
| 2094-BC01-MP5-S or 2094-BMP5-S              |                                            | 46 54 61 69 77                             |                                            |                                            |                                            |
| 2094-BC01-M01-S or 2094-BM01-S              |                                            | 57 73 90 108 126                           |                                            |                                            |                                            |
| 2094-BC02-M02-S or 2094-BM02-S              |                                            | 53 72 93 116 142                           |                                            |                                            |                                            |
| 2094-BC04-M03-S or 2094-BM03-S              |                                            |                                            | 94 130 169 211 255                         |                                            |                                            |
| 2094-BC07-M05-S or 2094-BM05-S              |                                            | 121 183 252 326 407                        |                                            |                                            |                                            |
| Shunt module - 2094-BSP2 68 121 174 227 280 |                                            |                                            |                                            |                                            |                                            |

IPIM module - 2094-SEPM-B24-S To calculate power dissipation for IPIM modules on your 2094 power rail, refer to the Kinetix 6000M Integrated DriveMotor User Manual, publication 2094-UM003 .

(1) Power dissipation for the Bulletin 2094 control modules, catalog numbers 2094-SE02F-M00-Sx and 2094-EN02D-M01-Sx, is included in the IAM and AM power module specifications.

(2) Internal shunt power is not included in the calculations and must be added based on utilization.

## Minimum Clearance Requirements

This section provides information to assist you in sizing your cabinet and positioning your Bulletin 2094 system components.

IMPORTANT

Mount the module in an upright position. Do not mount the module on its side.

In this example, the enclosure must have an exterior surface of 6.66 m 2 . If any portion of the enclosure is not able to transfer heat, do not include that portion in the calculation.

Because the minimum cabinet depth to house the 460V drive (selected for this example) is 302 mm (11.9 in.), then the cabinet needs to be approximately 2500 mm (high) x 950 mm (wide) x 302 mm (deep).

<!-- formula-not-decoded -->

Because this cabinet size is considerably larger than what is necessary to house the system components, consider some means of cooling in a smaller cabinet to be more efficient. Contact your cabinet manufacturer for options available to cool your cabinet.

Figure 7 illustrates minimum clearance requirements for proper airflow and installation:

- Additional clearance is required for the cables and wires connected to the top and front of the drive.
- Additional clearance left and right of the power rail is required when the drive is mounted adjacent to noise sensitive equipment or clean wireways.

Figure 7 - Minimum Clearance Requirements

<!-- image -->

Refer to Table 12 on page 26, and Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications, publication KNX-TD005, for Kinetix 6000 drive dimensions.

- (1) The power rail (slim), catalog number 2094-PRSx, extends left and right of the first and last module 5.0 mm (0.20 in.). The Bulletin 2094-PRx power rail extends approximately 25.4 mm (1.0 in.) left of the IAM module and right of the last module mounted on the rail.

Table 13 - Minimum Cabinet Depth

2094-BSP2 272 mm (10.7 in.) 2094-SEPM-B24-S 263 mm (10.3 in.)

| Drive Cat. No.                                                             | Cabinet Depth, min (1)   |
|----------------------------------------------------------------------------|--------------------------|
| 2094-AC05-Mxx-x, 2094-AC09-M02-x, x, 2094-AMP5-x, 2094-AM01-x, 2094-AM02-x | 198 mm (7.8 in.)         |
| 2094-BC01-Mxx-x, 2094-BC02-M02-x , 2094-BMP5-x, 2094-BM01-x, 2094-BM02-x   | 272 mm (10.7 in.)        |

| Drive Cat. No. Series F                                  |                   |                   |
|----------------------------------------------------------|-------------------|-------------------|
| 2094-AC05-Mxx-x 2094-AC09-M02-x 2094-AM01-x,             | A, C, D, and E  A, C, D, and E  (9.3) in. 2094-AMP5-x, 2094AM01                   | 237 mm            |
| 2094-AC16-M03-x 2094-AC32-M05-x                          | A, C, D, and E  A, C, D, and E  (16.5) in. 2094-AM03-x,                   | 420 mm            |
| 2094-AM05-x 2094-BC01-Mxx-x 2094-BC02-M02-x 2094-BMP5-x, | A, B, C, D, and E | 285 mm (11.2) in. |
| 2094-SEPM-B24-S 2094-BSP2                                | A                 | 285 mm (11.2) in. |
| 2094-BC04-M03-x 2094-BM03-x                              | B, C, D, and E  B, C, D, and E  (14.7) in. 2094-BC07-M05-x                   | 375 mm            |
| 2094-BM05-x 2094-BC07-M05-x 2094-BM05-x                  | A, D, and E       | 436 mm (17.2) in. |

| Drive Cat. No.                                                | Cabinet Depth, min (1)   |
|---------------------------------------------------------------|--------------------------|
| 2094-AC16-M03-x, 2094-AC32-M05-x, x, 2094-AM03-x, 2094-AM05-x | 198 mm (7.8 in.)         |
| 2094-BC04-M03-x, 2094-BC07-M05-x , 2094-BM03-x, 2094-BM05-x   | 272 mm (10.7 in.)        |

## Electrical Noise Reduction

This section outlines best practices that minimize the possibility of noiserelated failures as they apply specifically to Kinetix 6000 system installations. For more information on the concept of high-frequency (HF) bonding, the ground plane principle, and electrical noise reduction, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## HF Bond for Modules

Bonding is the practice of connecting metal chassis, assemblies, frames, shields, and enclosures to reduce the effects of electromagnetic interference (EMI).

Unless specified, most paints are not conductive and act as insulators. To achieve a good bond between power rail and the subpanel, surfaces need to be paint-free or plated. Bonding metal surfaces creates a low-impedance return path for high-frequency energy.

## IMPORTANT

To improve the bond between the power rail and subpanel, construct your subpanel out of zinc plated (paint-free) steel.

Improper bonding of metal surfaces blocks the direct return path and allows high-frequency energy to travel elsewhere in the cabinet. Excessive highfrequency energy can effect the operation of other microprocessor controlled equipment.

These illustrations show details of recommended bonding practices for painted panels, enclosures, and mounting brackets.

Figure 8 - Recommended Bonding Practices for Painted Panels

<!-- image -->

## HF Bond for Multiple Subpanels

Bonding multiple subpanels creates a common low impedance exit path for the high frequency energy inside the cabinet. If subpanels are not bonded together, and do not share a common low impedance path, the difference in impedance can affect networks and other devices that span multiple panels:

- Bond the top and bottom of each subpanel to the cabinet by using 25.4 mm (1.0 in.) by 6.35 mm (0.25 in.) wire braid. As a rule, the wider and shorter the braid is, the better the bond.

- Scrape the paint from around each fastener to maximize metal-to-metal contact.

Figure 9 - Multiple Subpanels and Cabinet Recommendations

<!-- image -->

## Establish Noise Zones

Observe these guidelines when the 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM module is used in the Bulletin 2094 system and mounted left of the IAM module with the AC (EMC) line filter mounted above the LIM module:

- The clean zone (C) is to the right and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the left and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is from the filter output to IAM module. Shielded cable is required on the EMC filter (load side) and the braided shield attached to the clamp provided.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

Figure 10 - Noise Zones (LIM mounted left of IAM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when the 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM module is used in the Bulletin 2094 system and mounted right of the IAM module with the AC (EMC) line filter mounted behind the IAM module:

- The clean zone (C) is to the left and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the right and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is from the filter output to IAM module. Shielded cable is required on the EMC filter (load side) and the braided shield attached to the clamp provided.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

Figure 11 - Noise Zones (LIM with EMC filter behind IAM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when the 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM module is used in the Bulletin 2094 system and mounted right of the drive with the AC (EMC) line filter mounted behind the LIM module:

- The clean zone (C) is to the left and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the right and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is from the filter output to drive. Shielded cable is required on the EMC filter (load side) and the braided shield attached to the clamp (when provided).
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

Figure 12 - Noise Zones (EMC filter behind LIM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (3) Only the 2094-ALxxS and 2094-XL75S-Cx LIM modules are compatible with the 2094 mounting brackets. The 2094-BLxxS, 2094AL09, and 2094-BL02 LIM modules are not compatible.

Keep the DC common-bus cable (very dirty) segregated from all other cables (not in a wireway) when the 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM module is used in a DC common-bus configuration and the follower IAM module is mounted below the leader IAM module.

Figure 13 - Noise Zones (DC common bus)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when the 2094-AL09 or 2094-BL02 LIM module is used in the Bulletin 2094 system and mounted left of the IAM module:

- The clean zone (C) is to the right and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the left and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The very dirty zone (VD) is limited to where the LIM module VAC output jumpers over to the IAM module. Shielded cable is required only if the very dirty cables enter a wireway.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

This layout is preferred due to the reduced size of the very dirty zone.

Figure 14 - Noise Zones (LIM mounted left of IAM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway.
- (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when the 2094-AL09 or 2094-BL02 LIM module is used in the Bulletin 2094 system and mounted above the IAM module:

- The clean zone (C) is to the right and beneath the Bulletin 2094 system (gray wireway).
- The dirty zone (D) is to the left and above the Bulletin 2094 system, and above and below the LIM module (black wireway).
- The LIM VAC output is very dirty (VD). Use shielded cable with a braid clamp attached at both ends of the cable to reduce the rating to dirty (D).
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

Figure 15 - Noise Zones (LIM mounted above IAM module)

<!-- image -->

- (1) For examples of shield clamp attachment, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (2) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.
- (3) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when your system includes the 2094-SEPM-B24-S IPIM module. In this example, a 2094-BL02 LIM module is used in the Bulletin 2094 system and mounted left of the IAM module:

- Establish clean (C) and dirty zones (D) similar to other Bulletin 2094 drive systems.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.
- IPIM digital input wires are noise sensitive and belong with the fiberoptic cables in the clean zone.
- Ethernet cables are noise sensitive and belong in the clean zone, however, they are connected only when programming the IPIM module.
- IDM network cables, although noise sensitive by nature, are shielded and can be routed with the hybrid cables outside of the enclosure.
- The Kinetix 2090 hybrid cable is dirty and belongs in the dirty zone.

This layout is preferred due to the reduced size of the very dirty zone.

Figure 16 - Noise Zones (Bulletin 2094 power rail with IPIM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable with LIM module I/O cable in dirty wireway. (2) When space does not permit the 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Observe these guidelines when individual input power components are used in the Bulletin 2094 system and the Bulletin 2094 LIM module is not used:

- The clean zone (C) is beneath the Bulletin 2094 system and includes the I/O wiring, feedback cable, and DC filter (gray wireway).
- The dirty zone (D) is above the Bulletin 2094 system (black wireway) and includes the circuit breakers, transformer, 24V DC power supply, contactors, AC line filter, and motor power cables.
- The very dirty zone (VD) is limited to where the AC line (EMC) filter VAC output jumpers over to the IAM module. Shielded cable is required only if the very dirty cables enter a wireway.
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

Figure 17 - Noise Zones (without LIM module)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.
- (2) When space to the right of the IAM does not permit 150 mm (6.0 in.) segregation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (3) This is a clean 24V DC available for any device that requires it. The 24V enters the clean wireway and exits to the right.
- (4) This is a dirty 24V DC available for motor brakes and contactors. The 24V enters the dirty wireway and exits to the left.

Observe these guidelines when installing your Logix 5000™ Sercos interface module:

- The clean zone (C) is beneath the less noisy modules (I/O, analog, encoder, registration, an so forth (gray wireway).
- The dirty zone (D) is above and below the power supply and noisy modules (black wireway).
- The Sercos fiber-optic cables are immune to electrical noise, but due to their delicate nature, route them in the clean zone.

Figure 18 - Noise Zones (ControlLogix chassis)

<!-- image -->

Table 14 - IAM Module (converter side)

|                                            | Zone Method   | Zone Method   | Zone Method    |                |
|--------------------------------------------|---------------|---------------|----------------|----------------|
| Wire/Cable Connector                       | Very Dirty    | Dirty Clean   | Ferrite Sleeve | Shielded Cable |
| CTRL 1 and 2 CPD X                         |               |               |                |                |
| DC-/DC+ (unshielded cable)                 | X             |               |                |                |
| IPD IPDL1, L2, L3 (shielded cable) X X     |               |               |                |                |
| L1, L2, L3 (unshielded cable) X            |               |               |                |                |
| CONT EN- and CONT EN+ (M1 contactor) CED X |               |               |                |                |
|                                            |               |               | DPI DPI X X    |                |

Table 15 - AM Module or Axis Module (inverter side)

|                                                                                    | Zone Method                           | Zone Method                           | Zone Method                           |                                       |                                       |
|------------------------------------------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| Wire/Cable Connector                                                               | Very Dirty Dirty Clean                | Ferrite Sleeve                        | Shielded Cable                        |                                       |                                       |
| U, V, W (motor power) MP X X                                                       |                                       |                                       |                                       |                                       |                                       |
| COM, PWR (24V DC), filtered (1)                                                    | X                                     |                                       |                                       |                                       |                                       |
| BC COM, PWR (24V DC), unfiltered (2)                                               | X                                     |                                       |                                       |                                       |                                       |
| DBRK-, DBRK+ (resistive brake) X                                                   |                                       |                                       |                                       |                                       |                                       |
| MBRK-, MBRK+ (motor brake) X                                                       |                                       |                                       |                                       |                                       |                                       |
| MBRK-, MBRK+ (motor brake) 1326AB motors with resolver feedback                    | BC X X                                |                                       |                                       |                                       |                                       |
| COM, PWR (24V DC), safety enable, and feedback signals for safe torque-off feature | STO X                                 |                                       |                                       |                                       |                                       |
| Motor feedback MF X X                                                              |                                       |                                       |                                       |                                       |                                       |
| Auxiliary feedback AF X X                                                          |                                       |                                       |                                       |                                       |                                       |
| Registration and analog outputs  IOD                                               |                                       | X X                                   |                                       |                                       |                                       |
|                                                                                    | Others X                              |                                       |                                       |                                       |                                       |
|                                                                                    | Fiber-optic Rx and Tx No restrictions | Fiber-optic Rx and Tx No restrictions | Fiber-optic Rx and Tx No restrictions | Fiber-optic Rx and Tx No restrictions | Fiber-optic Rx and Tx No restrictions |

## Table 16 - Line Interface Module (LIM)

|                                 | Zone Method            | Zone Method    | Zone Method    |
|---------------------------------|------------------------|----------------|----------------|
| Wire/Cable Connector            | Very Dirty Dirty Clean | Ferrite Sleeve | Shielded Cable |
| VAC line (main input) IPL X     |                        |                |                |
| Aux power input APL X           |                        |                |                |
| VAC load (shielded option)  OPL |                        | X X            |                |
| OPL VAC load (unshielded option) X                                 |                        |                |                |
| Control power output CPL X      |                        |                |                |
| MBRK PWR, MBRK COM P1L/PSL X    |                        |                |                |
|                                 | Status I/O IOL X       |                |                |
| Aux power output P2L X          |                        |                |                |

## Cable Categories for Kinetix 6000 Systems

These tables indicate the zoning requirements of cables connecting to the Kinetix 6000 drive components.

Table 17 - Shunt Module

|                                | Zone Method            | Zone Method    | Zone Method    |
|--------------------------------|------------------------|----------------|----------------|
| Wire/Cable Connector           | Very Dirty Dirty Clean | Ferrite Sleeve | Shielded Cable |
| COL, DC+ (shielded option)  RC |                        | X X            |                |
| RC COL, DC+ (unshielded option) X                                |                        |                |                |
| Thermal switch TS X X          |                        |                |                |
| Fan (if present) N/A X         |                        |                |                |

)

## Table 18 - IDM Power Interface Module (IPIM)

| Wire/Cable                                                                          | Zone Method                 | Zone Method                                          | Zone Method                 |                             |                             |
|-------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------|-----------------------------|-----------------------------|-----------------------------|
|                                                                                     |                             | Very Dirty Dirty Clean Ferrite Sleeve Shielded Cable |                             |                             |                             |
| Hybrid DC bus power, control power, inter-module communication, and Safe Torque Off |                             | X X                                                  |                             |                             |                             |
|                                                                                     |                             | Enable input X X                                     |                             |                             |                             |
|                                                                                     | Fiber-optic No restrictions | Fiber-optic No restrictions                          | Fiber-optic No restrictions | Fiber-optic No restrictions | Fiber-optic No restrictions |
|                                                                                     |                             | Ethernet network X X                                 |                             |                             |                             |
| IDM network (1)                                                                     |                             | X X                                                  |                             |                             |                             |

Table 19 - Resistive Brake Module (RBM)

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

Observe these guidelines when mounting your AC (EMC) line filter (refer to the figure on page 37 for an example):

- Mount the AC line filter on the same panel as the Kinetix 6000 drive and as close to the power rail as possible.
- Good HF bonding to the panel is critical. For painted panels, refer to the examples on page 28 .
- Segregate input and output wiring as far as possible.

## IMPORTANT

CE and UK test certification applies only to AC line filter and single power rail. Sharing a line filter with multiple power rails can perform satisfactorily, but the user takes legal responsibility.

## External Shunt Modules

Observe these guidelines when mounting your external shunt module outside the enclosure:

- Mount circuit components and wiring in the very dirty zone or in an external shielded enclosure. Run shunt power and fan wiring inside metal conduit to minimize the effects of EMI and RFI.
- Mount resistors (other than metal-clad) in a shielded and ventilated enclosure outside the cabinet.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.
- Route thermal switch and fan wires separate from shunt power.

Figure 19 - External Shunt Module Outside the Enclosure

<!-- image -->

When mounting your shunt module inside the enclosure, follow these additional guidelines:

- Mount metal-clad modules anywhere in the dirty zone, but as close to the Bulletin 2094 drive system as possible.
- Route shunt power wires with motor power cables.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.

- Separate shunt power cables from other sensitive, low voltage signal cables.

Figure 20 - External Shunt Module Inside the Enclosure

<!-- image -->

## Resistive Brake Modules

Observe these guidelines when mounting your RBM module:

- Mount circuit components and wiring in the dirty zone or in an external shielded enclosure. If mounting the RBM module in a separate ventilated shielded enclosure, run wiring inside metal conduit to minimize the effects of EMI and RFI.
- Keep unshielded wiring as short as possible. Keep wiring as flat to the cabinet as possible.
- Route RBM module power and I/O cables separate from other sensitive low voltage signal cables.

Figure 21 - Noise Zones (RBM mounted above AM module)

<!-- image -->

## Motor Brake and Thermal Switch

The thermal switch and brake are mounted inside the motor, but how you connect to the axis module depends on the motor series.

Refer to Wire the Motor/Resistive Brake (BC) Connector on page 88 or wiring guidelines. Refer to Axis Module/Rotary Motor Wiring Examples on page 160 for the interconnect diagram of your drive/motor combination.

## Before You Begin

<!-- image -->

## Mount the Kinetix 6000 Drive System

This chapter provides the system installation procedures for mounting your Kinetix® 6000 drive components on the Bulletin 2094 power rail.

| Topic Page                         |
|------------------------------------|
| Before You Begin 43                |
| Determine Mounting Order 44        |
| Mount Modules on the Power Rail 45 |

This procedure assumes you have prepared your panel, mounted your Bulletin 2094 power rail, and understand how to bond your system. For installation instructions regarding equipment and accessories not included here, refer to the instructions that came with those products.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Bulletin 2094 power rail and drive modules prior to applying power. Once power is applied, connector terminals can have voltage present even when not in use.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

Before you begin, consider your Bulletin 2094 power rail installation and using 2094 mounting brackets.

## Use the 2094 Mounting Brackets

You can use Bulletin 2094 mounting brackets to mount the power rail or LIM module over the AC line filter. Refer to the 2094 Mounting Brackets Installation Instructions, publication 2094-IN008, when using mounting brackets with your Kinetix 6000 drive system.

## Install the 2094 Power Rail

The Bulletin 2094 power rail comes in lengths to support one IAM module and up to seven additional AM/IPIM modules, or up to six additional AM/IPIM modules and one shunt module. The connector pins for each slot are covered by a protective cover. The cover is designed to protect the pins from damage and make sure that no foreign objects lodge between the pins during installation. Refer to the Kinetix 6000 Power Rail Installation Instructions, publication 2094-IN003, when installing your power rail.

## Determine Mounting Order

<!-- image -->

ATTENTION: To avoid damage to the power rail during installation, do not remove the protective covers until the module for each slot is ready for mounting.

The Kinetix 6000M integrated drive-motor (IDM) system is supported by Bulletin 2094 (400V-class) power rail configurations. You can mount up to four IDM power interface (IPIM) modules on the Bulletin 2094 power rail. Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for more information.

Mount IAM, AM/IPIM, shunt, and slot-filler modules in the order (left to right) as shown in Figure 22. Mount axis modules and the IPIM module according to power utilization (highest to lowest) from left to right starting with the highest power utilization.

Power utilization is the average power (kW) consumed by a servo axis. If Motion Analyzer software was used to size the axis, the calculated axis power required can be used for the power utilization value. If Motion Analyzer software was not used, you can use the continuous power value (kW) for each module to determine mounting order.

Table 20 - Kinetix 6000 (200V-class) Axis Modules

|                              | Attribute 2094-AMP5-S 2094-AM01-S 2094-AM02-S 2094-AM03-S 2094-AM05-S   |
|------------------------------|-------------------------------------------------------------------------|
| Continuous Power Output, nom | 1.2 kW 1.9 kW 3.4 kW 5.5 kW 11.0 kW                                     |

Table 21 - Kinetix 6000 (400V-class) Axis Modules

|                              | Attribute 2094-BMP5-S 2094-BM01-S 2094-BM02-S 2094-BM03-S 2094-BM05-S   |                                      |
|------------------------------|-------------------------------------------------------------------------|--------------------------------------|
| Continuous Power Output, nom |                                                                         | 1.8 kW 3.9 kW 6.6 kW 13.5 kW 22.0 kW |

Table 22 - Kinetix 6000M (400V-class) IPIM Module

| Attribute 2094-SEPM-B24-S            |
|--------------------------------------|
| Continuous Power Output, nom 15.0 kW |

Figure 22 - Module Mounting Order Example

<!-- image -->

## Mount Modules on the Power Rail

Power Rail

## IMPORTANT

<!-- image -->

The IAM module must be positioned in the leftmost slot of the power rail. Position your AM/IPIM modules, shunt module, and slot-filler modules to the right of the IAM module.

The shunt module must be installed to the right of the last AM/IPIM module. Only slot-filler modules can be installed to the right of the shunt module.

Do not mount the shunt module on power rails with a follower IAM module. Common-bus follower IAM modules disable the internal, rail mounted, and external shunt modules.

SHOCK HAZARD: To avoid personal injury due to electrical shock, place a 2094-PRF slot-filler module in all empty slots on the power rail. Any power rail connector without a module installed disables the Bulletin 2094 system; however, control power is still present.

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

<!-- image -->

4. Pivot module downward and align the guide pins on the power rail with the guide pin holes in the back of the module.

<!-- image -->

Repeat step 1 through step 6 for each AM, IPIM, shunt, or slot-filler module in your Bulletin 2094 drive system.

## 2094 IAM/AM Module Connector Data

<!-- image -->

## Connector Data and Feature Descriptions

This chapter illustrates drive connectors and indicators, including connector pinouts, and provides descriptions for Kinetix® 6000 drive features.

| Topic Page                           |
|--------------------------------------|
| 2094 IAM/AM Module Connector Data 47 |
| Control Signal Specifications 54     |
| Power and Relay Specifications 57    |
| Feedback Specifications 62           |

For the Kinetix 6000M integrated drive-motor (IDM) unit and IDM power interface module (IPIM) connector locations and signal descriptions, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Use these illustrations to identify the connectors and indicators for the IAM/AM modules. Sercos interface and Ethernet network connectors for the Kinetix 6000M IPIM module are also shown. For the remainder of the IPIM module features and indicators, refer to the Kinetix 6000M Integrated DriveMotor System User Manual, publication 2094-UM003 .

Although the physical size of the 400V-class module is larger than the 200V-class module, the location of the features and indicators is identical.

Figure 23 - Integrated Axis Module Features and Indicators

<!-- image -->

Item Description Item Description

1 Safe torque-off (STO) connector 11 Sercos receive (Rx) connector

2 Contactor enable (CED) connector 12 Mounting screw

3 DC bus/AC input power (IPD) connector 13 I/O (IOD) connector

4 Control power (CPD) connector 14 Sercos node address switch

5 Motor cable shield clamp 15 Seven-segment fault status indicator

6 Motor power (MP) connector 16 Drive status indicator

7 Motor/resistive brake (BC) connector 17 COMM status indicator

9 Sercos transmit (Tx) connector 19 Motor feedback (MF) connector

10 DPI connector 20 Auxiliary feedback (AF) connector

| 18 Bus status indicator   |
|---------------------------|

Figure 24 - Axis Module Features and Indicators

<!-- image -->

Item Description Item Description

1 Safe torque-off (STO) connector 9 Mounting screw

2 Motor cable shield clamp 10 I/O (IOD) connector

3 Motor power (MP) connector 11 Seven-segment fault status indicator

4 Motor/resistive brake (BC) connector 12 Drive status indicator

|   5 | Sercos communication rate and optical power switches   |
|-----|--------------------------------------------------------|
|   6 | Sercos transmit (Tx) connector (1)                     |
|   7 | Sercos receive (Rx) connector (1)                      |
|   8 | Ethernet (PORT1 and PORT 2) connectors (2)             |

| 13 COMM status indicator             |
|--------------------------------------|
| 14 Bus status indicator              |
| 15 Motor feedback (MF) connector     |
| 16 Auxiliary feedback (AF) connector |

- (1) The Rx and Tx Sercos connectors on the Kinetix 6000M IPIM module are in the same position as on the Kinetix 6000 AM modules. For the remainder of the IPIM module features and indicators, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .
- (2) The Kinetix 6000M IPIM module has two Ethernet ports. These ports are used only for connecting to the EtherNet/IP™ network for Logix 5000™ programming.

| Designator Description Connector Module                           |
|-------------------------------------------------------------------|
| IOD User I/O (drive) 26-pin high-density D-shell (female) IAM/AM  |
| MF Motor feedback 15-pin high-density D-shell (female) IAM/AM     |
| AF Auxiliary feedback 15-pin high-density D-shell (male) IAM/AM   |
| CPD Control input power (drive) 2-position plug/header IAM        |
| IPD VAC input power (drive) and DC bus 6-position plug/header IAM |

Table 23 - Kinetix 6000 IAM/AM Module Connectors

| 8   | Sercos communication rate and optical power switches   |
|-----|--------------------------------------------------------|

Table 23 - Kinetix 6000 IAM/AM Module Connectors (Continued)

| Designator Description Connector Module                             |
|---------------------------------------------------------------------|
| CED Contactor enable 2-position plug/header IAM                     |
| MP Motor power 4-position plug/header IAM/AM                        |
| BC Motor/Resistive brake 6-position plug/header IAM/AM              |
| STO Safe torque-off 9-position plug/header IAM/AM                   |
| Tx and Rx Sercos transmit and receive Sercos fiber-optic (2) IAM/AM |
| DPI DPI DPI IAM                                                     |

## Safe Torque-off Connector Pinout

Each 2094-xCxx-Mxx-S IAM module and 2094-xMxx-S AM module ships with the (9-pin) wiring-plug header and motion-allowed jumper installed in the safe torque-off (STO) connector. With the motion-allowed jumper installed, the safe torque-off feature is not used.

Figure 25 - Motion-allowed Jumper

<!-- image -->

Headers in this table extend the safe torque-off (STO) connector signals for use in wiring single and multiple safe torque-off drive configurations, or to defeat (not use) the safe torque-off feature.

Table 24 - IAM/AM Safe Torque-off 9-pin (STO) Connector

| Safe Torque-off (STO) Connector Pin   | Applies to These STO Connector Headers Description Signal   |                                                                      |
|---------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------|
| 1                                     | • Wiring plug header used in single-drive applications • First-drive wiring header (catalog number 2090-XNSM-W) used in multiple-drive applications (catalog number 2090-XNSM-W) used in multipledrive applications 5 Safety enable 2 input SAFETY ENABLE2+                                                             | One side of the normally-closed monitoring contact of relay 2 FDBK2+ |
|                                       | • Wiring plug header used in single-drive applications • First-drive wiring header (catalog number 2090-XNSM-W) used in multiple-drive applications (catalog number 2090-XNSM-W) used in multipledrive applications 5 Safety enable 2 input SAFETY ENABLE2+                                                             | lhdd ld 2 Other side of the normally-closed monitoring contact of relay 2 FDBK2-                                                                      |
|                                       | • Wiring plug header used in single-drive applications • First-drive wiring header (catalog number 2090-XNSM-W) used in multiple-drive applications (catalog number 2090-XNSM-W) used in multipledrive applications 5 Safety enable 2 input SAFETY ENABLE2+                                                             | Wiring plug header used in singledrive applications 3 One side of the normally-closed monitoring contact of relay 1 FDBK1+                                                                      |
|                                       | • Wiring plug header used in single-drive applications • First-drive wiring header (catalog number 2090-XNSM-W) used in multiple-drive applications (catalog number 2090-XNSM-W) used in multipledrive applications 5 Safety enable 2 input SAFETY ENABLE2+                                                             | • First-drive wiring header 4 Other side of the normally-closed monitoring contact of relay 1 FDBK1-                                                                      |
|                                       | • Wiring plug header used in single-drive applications • First-drive wiring header (catalog number 2090-XNSM-W) used in multiple-drive applications (catalog number 2090-XNSM-W) used in multipledrive applications 5 Safety enable 2 input SAFETY ENABLE2+                                                             | ppp 6 Return for safety enable power (both inputs) SAFETY ENABLE                                                                      |
|                                       | • Wiring plug header used in single-drive applications • First-drive wiring header (catalog number 2090-XNSM-W) used in multiple-drive applications (catalog number 2090-XNSM-W) used in multipledrive applications 5 Safety enable 2 input SAFETY ENABLE2+                                                             | 7 Safety enable 1 input SAFETY ENABLE1+                              |
| 8                                     | • Wiring plug header • Motion-allowed jumper                | Power for continuous enable of the safety function, 500 mA max 24V+  |
|                                       | • Wiring plug header • Motion-allowed jumper                | • Motion-allowed jumper 9 Power return used for continuous enable of safety function 24V_COM                                                                      |

## IMPORTANT

Pins STO-8 and STO-9 (24V+) are used by only the motion-allowed jumper. When wiring to the wiring-plug header, the 24V supply must come from an external source.

Refer to the Kinetix Safe Torque-off Feature Safety Reference Manual, publication GMC-RM002, for more information on wiring safe torque-off headers.

Kinetix 6000 IAM/AM Module (AM module is shown)

Table 25 - IAM/AM I/O 26-pin (IOD) Connector

IOD Pin Description Signal IOD Pin Description Signal

1 Hardware enable 24V DC power supply +24V\_PWR 14 High speed registration 1 input REG1

2 Hardware enable input ENABLE 15 Common for registration REG\_COM

3 Common +24V\_COM 16 24V registration power REG\_24V

4 Home switch 24V DC power supply +24V\_PWR 17 High speed registration 2 input REG2

5 Home switch input HOME 18 Common for registration REG\_COM

6 Common +24V\_COM 19 Reserved –

7 Positive overtravel 24V DC power supply +24V\_PWR 20 Reserved –

8 Positive overtravel limit switch input OT+ 21 Reserved –

9 Common +24V\_COM 22 Reserved –

10 Negative overtravel 24V DC power supply +24V\_PWR 23 Analog output 0 DAC0

11 Negative overtravel limit switch input OT- 24 Analog output common DAC\_COM

12 Common +24V\_COM 25 Analog output 1 DAC1

13 24V registration power REG\_24V 26 Analog output common DAC\_COM

## I/O Connector Pinout

## IMPORTANT

Signals +24V\_PWR and +24V\_COM are a 24V DC source you can use only for the inputs listed above.

Figure 26 - Pin Orientation for 26-pin I/O (IOD) Connector

<!-- image -->

## Motor Feedback Connector Pinout

Table 26 - Stegmann Hiperface (SRS/SRM)

| 10 Hiperface data channel DATA                                                 |
|-------------------------------------------------|
| Motor thermal switch (normally closed) (1)  TS+ |
| EPWR_5V (2)                                     |
| 15 Reserved –                                   |

MF Pin Description Signal MF Pin Description Signal

1 Sine differential input+ SIN+ 9 Reserved –

4 Cosine differential input- COS- 12 Reserved –

5 Hiperface data channel DATA+ 13 Reserved –

6 Common ECOM 14 Encoder power (+5V)

| 2 Sine differential input- SIN-      |
|--------------------------------------|
| 3 Cosine differential input+ COS+ 11 |
| 7 Encoder power (+9V)  EPWR_9V (2)   |
| 8 Reserved –                         |

- (1) Not applicable unless the motor has integrated thermal protection. Common (TS-) signal for thermal switch is tied to MF-6 (ECOM) in Kinetix 2090 cables.
- (2) Determine which power supply your encoder requires and connect to only the specified supply. Do not make connections to both .

Table 27 - TTL or Sine/Cosine with Index Pulse and Hall Commutation

MF Pin Description Signal MF Pin Description Signal

1 AM+ / Sine differential input+ AM+ / SIN+ 9 Reserved –

2 AM- / Sine differential input- AM- / SIN- 10 Index pulse- IM-

5 Index pulse+ IM+ 13 Single-ended 5V hall effect commutation S2

| 3 BM+ / Cosine differential input+ BM+ / COS+ 11   |
|----------------------------------------------------|
| 4 BM- / Cosine differential input- BM- / COS-      |

| Motor thermal switch (normally closed) (1)    | TS+   |
|-----------------------------------------------|-------|
| 12 Single-ended 5V hall effect commutation S1 |       |

Table 27 - TTL or Sine/Cosine with Index Pulse and Hall Commutation (Continued)

MF Pin Description Signal MF Pin Description Signal

6 Common ECOM 14 Encoder power (+5V)

| EPWR_5V (2)   |
|---------------|
| 15 Reserved – |

| 7 Encoder power (+9V)                        | EPWR_9V (2)   |
|----------------------------------------------|---------------|
| 8 Single-ended 5V hall effect commutation S3 |               |

Table 28 - Resolver Transmitter (transformation ratio = 0.25)

<!-- image -->

MF Pin Description Signal MF Pin Description Signal

1 Sine differential input+ S2 9 Reserved –

2 Sine differential input- S4 10 Resolver excitation R2

4 Cosine differential input- S3 12 Reserved –

5 Resolver excitation R1 13 Reserved –

6 Common ECOM 14 Reserved –

7 Reserved – 15 Reserved –

| 3 Cosine differential input+ S1 11   |
|--------------------------------------|
| 8 Reserved –                         |

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect to either the 5V or 9V supply, but not both.

| Motor thermal switch (normally closed) (1) (2)   | TS+   |
|--------------------------------------------------|-------|

Kinetix 6000 drives do not support Heidenhain EnDat high-resolution feedback; however, you can use the 2090-K6CK-KENDAT feedback module to convert Heidenhain EnDat high-resolution feedback to Stegmann Hiperface. Pin numbers in the table below refer to pins in the feedback module.

## IMPORTANT

Only 2094-xCxx-Mxx-S and 2094-xMxx-S drives with firmware revision 1.116 or later support the use of 2090-K6CK-KENDAT feedback modules for Heidenhain EnDat feedback.

| Motor thermal switch+ (1)   | TS+   |
|-----------------------------|-------|
| Motor thermal switch- (2)   | TS       |

Combined motor-power cable length for all axes on the same DC bus must not exceed 240 m (787 ft) with 460V systems or 160 m (525 ft) with 230V systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).

System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.

Table 29 - Heidenhain EnDat

Pin Description Signal Pin Description Signal

1 Sine differential input+ SIN+ 8 Serial data clock signal - CLK-

2 Sine differential input- SIN- 9 Serial data differential signal+ DATA+

3 Cosine differential input+ COS+ 10 Serial data differential signal - DATA-

6 Common ECOM 13 Reserved –

| 4 Cosine differential input- COS- 11   |
|----------------------------------------|
| 5 Encoder power (+5V) EPWR_5V 12       |
| 7 Serial data clock signal + CLK+      |

## IMPORTANT

Figure 27 - Pin Orientation for 15-pin Motor Feedback (MF) Connector

<!-- image -->

## Auxiliary Feedback Connector Pinout

For TTL devices, the position count increases when A leads B. For sinusoidal devices, the position count increases when cosine leads sine.

Table 30 - Stegmann Hiperface (SRS and SRM only)

AF Pin Description Signal AF Pin Description Signal

1 Sine differential input+ SIN+ 9 Reserved –

3 Cosine differential input+ COS+ 11 Reserved –

4 Cosine differential input- COS- 12 Reserved –

5 Hiperface data channel DATA+ 13 Reserved –

6 Common ECOM 14 Encoder power (+5V)

| 2 Sine differential input- SIN-    |
|------------------------------------|
| 7 Encoder power (+9V)  EPWR_9V (1) |
| 8 Reserved –                       |

| 10 Hiperface data channel DATA               |
|---------------|
| EPWR_5V (1)   |
| 15 Reserved – |

Table 31 - TTL or Sine/Cosine with Index Pulse

AF Pin Description Signal AF Pin Description Signal

1 A+ / Sine differential input+ A+ / SIN+ 9 Reserved –

2 A- / Sine differential input- A- / SIN- 10 Index pulse- I-

3 B+ / Cosine differential input+ B+ / COS+ 11 Reserved –

4 B- / Cosine differential input- B- / COS- 12 Reserved –

5 Index pulse+ I+ 13 Reserved –

6 Common ECOM 14 Encoder power (+5V)

| EPWR_5V (1)   |
|---------------|
| 15 Reserved – |

| 7 Encoder power (+9V)   | EPWR_9V (1)   |
|-------------------------|---------------|
| 8 Reserved –            |               |

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect to either the 5V or 9V supply, but not both.

Figure 28 - Pin Orientation for 15-pin Auxiliary Feedback (AF) Connector

<!-- image -->

## IAM Input Connector Pinout

## Table 32 - Control Power Connector

| CPD Pin Description Signal   |
|------------------------------|
| Control power VAC input pp 2 CTRL 1                              |
| Control power VAC input pp 2 CTRL 1                              |

## Table 33 - DC Bus and Input Power Connector

|    | IPD Pin Description Signal                            |      |
|----|-------------------------------------------------------|------|
| 1  | An integral, unregulated power supply, consisting of AC line input, three-phase bridge rectifier, and filter capacitors. input, three-phase bridge rectifier, and filter capacitors. 2 DC+                                                       | DC      |
|    | 3 Chassis ground.                                     |      |
| 4  | Three-phase input power. Three-phase input power.5 L2 | L3   |
|    | Three-phase input power. Three-phase input power.5 L2 | 6 L1 |
|    | Three-phase input power. Three-phase input power.5 L2 |      |

## Table 34 - Contactor Enable Connector

| CED Pin Description Signal   |    |
|------------------------------|----|
| 1  Relay-driven dry contact used in the control string for a three                              | CONT EN    |
| phase power contactor. phase power contactor. 2 CONT EN+                              |    |

## IAM and AM Motor Power and Brake Connector Pinout

## Table 35 - Motor Power Connector

|    | MP Pin Description Signal                          |     |
|----|----------------------------------------------------|-----|
|    | 4 Chassis ground                                   |     |
| 3  | Three-phase motor power Three-phase motor power2 V | W   |
|    | Three-phase motor power Three-phase motor power2 V | 1 U |
|    | Three-phase motor power Three-phase motor power2 V |     |

## IMPORTANT

Combined motor-power cable length for all axes on the same DC bus must not exceed 240 m (787 ft) with 460V systems or 160 m (525 ft) with 230V systems. Drive-to-motor power cables must not exceed 90 m (295.5 ft).

System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.

## Table 36 - Motor Brake/Resistive Brake Connector

|    | BC Pin Description Signal                                     |     |
|----|---------------------------------------------------------------|-----|
| 6  | Motor brake connections 5 MBRK+                               | MBRK     |
|    | 4 Motor brake common COM                                      |     |
| 3  | +24V brake input power (from LIM module or customer supplied) | PWR |
| 2  | RBM module connections (from RBM module and safety string)    | DBRK     |
|    | (from RBM module and safety string) 1 DBRK+                                                               |     |

Control Signal Specifications This section provides a description of the Kinetix 6000 drive
iiblbk I/O (IOD), communication, contactor enable (CED), brake (BC), and control power (CPD) connectors.

## Digital Inputs

Two fast registration inputs and four other inputs are available for the machine interface on the IAM module and AM module. Each IAM and AM module supplies 24V DC @ 250 mA for the purpose of registration, home, enable, over-travel positive, and over-travel negative inputs. These are sinking inputs that require a sourcing device. A 24V DC power and common connection is provided for each input.

IMPORTANT

To improve registration input EMC performance, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

IMPORTANT Over-travel limit input devices must be normally closed.

Table 37 - Understanding Digital Inputs

|               |              | IOD Pin Signal Description Capture Time                                                                                                                                                                                                                                                             | Edge/Level Sensitive   |
|---------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|               | IOD-2 ENABLE | Optically isolated, single-ended active high signal. Current loading is nominally 10 mA. A 24V DC input is applied to this terminal to enable each axis.                                                                                                                                            | 20 ms Level            |
|               | IOD-5 HOME   | Optically isolated, single-ended active high signal. Current loading is nominally 10 mA. Home switch (normally open contact) inputs for each axis require 24V DC (nominal).                                                                                                                         | 20 ms Level            |
| IOD-14 IOD-17 | REG1 REG2    | Fast registration inputs are required to inform the motor interface to capture the positional information with less than 3 s uncertainty. Optically isolated, single-ended active high signal. Current loading is nominally 10 mA. A 24V DC input is applied to this terminal to enable each axis. | 500 ns Edge            |
| IOD-8 IOD-11  | OT+ OT              | Overtravel detection is available as an optically isolated, single-ended active high signal. Current loading is nominally 10 mA per input. The pos/neg limit switch (normally closed contact) inputs for each axis require 24V DC (nominal).                                                        | 30 ms Level            |

Table 38 - Digital Input Specifications

|                                                                                                              | Parameter Description Min Max                                   |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| On-state voltage  Voltage applied to the input, with respect to IOCOM, to guarantee an on-state.             | ENABLE, HOME, and OT+/OT- 10.8V 26.4V REG1 and REG2 21.6V 26.4V |
| On-state current Current flow to guarantee an on-state. 3.0 mA 10.0 mA                                       |                                                                 |
| Off-state voltage Voltage applied to the input, with respect to IOCOM, to guarantee an off-state. -1.0V 3.0V |                                                                 |

Figure 29 - Enable, Home, and Overtravel Digital Input Circuits

<!-- image -->

- (1) 24V DC source (range) = 21.6V - 26.4V (supplied by drive, not to exceed 250 mA total).
- (2) Maximum current input = 10 mA.

Figure 30 - Registration Digital Input Circuits

<!-- image -->

## Sercos Communication Specifications

The Rx and Tx Sercos connectors are provided on the Kinetix 6000 IAM and AM module for communication with the Logix 5000 controller.

| Attribute Value                  |                                                                    |
|----------------------------------|--------------------------------------------------------------------|
| Data rates                       | 4 and 8 Mbps, selectable via DIP switch (1)                        |
|                                  | Light intensity Low power or high power, selectable via DIP switch |
| Cyclic update period 500 µs, min |                                                                    |
| Node addresses                   | 01…99 (2)                                                          |

- (1) The Kinetix 6000M IDM system supports only 8 Mbps and is hardwired for this setting.

(2) Node address assignments begin with the IAM module. Node addresses for additional axes on the same power rail are assigned by incrementing from left to right (starting with the IAM module address).

- Each IDM unit has it's own node address switches and can be set to any valid address. However, node addresses for the IAM and AM modules on the power rail and for IDM units must be unique.

## Analog Outputs

The IAM and AM modules include two analog outputs (IOD-23 and IOD-25) that you can configure through software to represent drive variables.

Figure 31 - Analog Output Circuit

<!-- image -->

## IMPORTANT

Output values can vary during powerup until the specified power supply voltage is reached.

Table 39 - Analog Output Specifications

| Parameter Description Min Max                                                                             |            |
|-----------------------------------------------------------------------------------------------------------|------------|
| Resolution  Number of states that the output signal is divided into, which is 2 (to the number of bits) . | – ±11 bits |
| Output current Current capability of the output. 0 +2 mA                                                  |            |

Table 39 - Analog Output Specifications (Continued)

|                     | Parameter Description Min Max                                                    |        |
|---------------------|----------------------------------------------------------------------------------|--------|
| Output signal range | Range of the output voltage. 2094-xCxx-Mxx and 2094-xMxx drives  2094-xCxx-Mxx-S | 0 +5V  |
|                     | and 2094-xMxx-S                                                                  | 0 +10V |
|                     | Offset error Deviation when the output is expected to be at 0V. – 1 mV           |        |
|                     | Bandwidth Frequency response of the analog output DC 7.2k Hz (3 db)              |        |

Table 40 - Linear Scaling Specifications

| Drive Cat. No.                 | Speed rpm Value V DC   | Torque %   |
|--------------------------------|------------------------|------------|
| 2094-xCxx-Mxx or 2094-xMxx     | 10,000 5.0 1000        |            |
| 2094-xCxx-Mxx or 2094-xMxx     |                        | 0 2.5 0    |
| 2094-xCxx-Mxx or 2094-xMxx     | -10,000 0 -1000        |            |
| 2094-xCxx-Mxx-S or 2094-xMxx-S | 10,000 10.0 1000       |            |
| 2094-xCxx-Mxx-S or 2094-xMxx-S |                        | 0 5.0 0    |
| 2094-xCxx-Mxx-S or 2094-xMxx-S | -10,000 0 -1000        |            |

For configuration/set up of the analog outputs, refer to Configure Drive Parameters and System Variables on page 130 .

## Contactor Enable Relay

Contactor enable is a relay-driven contact used in the three-phase powerenable control string to protect the drive electronics during certain fault conditions. It is capable of handling 120V AC or 24V DC at 1 A or less. Contactor enable is a function of the converter and is not available in the axis modules. An active state indicates the drive is operational and does not have a fault.

<!-- image -->

ATTENTION: Wiring the contactor enable relay is required. To avoid personal injury or damage to the drive, wire the contactor enable relay into your three-phase power-enable control string so that:

- three-phase power is removed from the drive in the event of shutdown fault conditions.
- drive operation is prevented when the power rail is not fully populated.
- control power is applied to the drive prior to three-phase power.

ATTENTION: Refer to IAM Module (without LIM module) on page 155 for a wiring example.

## IMPORTANT

All power rail slots must have a module installed or the contactor enable relay does not close.

Figure 32 - Contactor Enable Relay Circuit

<!-- image -->

## Power and Relay Specifications

Table 42 - Brake Relay Output Specifications

|                                                                          | Attribute Description IAM/AM Module                                           | Brake Current Value, max   | Brake Current Value, max   | Brake Current Value, max             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------|----------------------------|----------------------------|--------------------------------------|
|                                                                          | Attribute Description IAM/AM Module                                           |                            |                            | Series A Series B Series C and later |
| Current flow when the relay is closed                                    | 2094-AC05-Mxx ,-x 2094-AC09-M02-x,  x,  2094-AMP5-x, 2094-AM01-x, 2094-AM02-x | 1.0 A                      | N/A                        | 3.0 A                                |
| Current flow when the relay is closed                                    | 2094-BC01-Mxx - x, 2094-BC02-M02-x, x, 2094-BMP5-x, 2094-BM01-x, 2094-BM02-x  | 1.0 A                      | 3.0 A                      | 3.0 A                                |
| Current flow when the relay is closed                                    | 2094-AC16-M03-x, 2094-AC32-M05-x,  x,  2094-AM03-x, 2094-AM05-x               | 1.3 A N/A                  |                            | 3.0 A                                |
| Current flow when the relay is closed                                    | 2094-BC04-M03-x, 2094-BC07-M05-x, x, 2094-BM03-x, 2094-BM05-x                 |                            | 3.0 A 3.0 A                | 3.0 A                                |
| On-state resistance Contact resistance when the relay is closed 1       | On-state resistance Contact resistance when the relay is closed 1            |                            |                            |                                      |
| Off-state voltage Voltage across the contacts when the relay is open 30V | Off-state voltage Voltage across the contacts when the relay is open 30V      |                            |                            |                                      |

Figure 33 - Brake Relay Circuit (series C and later)

<!-- image -->

Table 41 - Contactor Enable Relay Output Specifications

| Attribute Value Min Max   |                                                                        |
|---------------------------|------------------------------------------------------------------------|
| On-state current          | Current flow when the relay is closed – 1 A                            |
| On-state resistance       | Contact resistance when the relay is closed – 1                       |
| Off-state voltage         | Voltage across the contacts when the relay is open – 120V AC or 24V DC |

This section provides a description of the Kinetix 6000 brake relay (BC), input power (IPD), motor power (MP), and control power (CPD) connectors.

## Motor/Resistive Brake Relay

The brake option is a spring-set holding brake that releases when voltage is applied to the brake coil in the motor. The customer-supplied 24V power supply drives the brake output through a solid-state relay (series C and later) and mechanical relays (series A and B). The solid-state brake driver circuit provides the following:

- Brake current-overload protection
- Brake over-voltage protection

Two connections are required for the (customer-supplied) motor/resistive brake input power (BC-3 and BC-4) and two connections each for the motor and resistive brake output, as shown in Figure 33. Wiring is consistent with all series releases. Connections are rated for +24V and current as shown in Table 42 .

## IMPORTANT

Motor parking-brake switching frequency must not exceed 10 cycles/min.

Control of the relay to release the motor brake (BC-5 and BC-6) is configurable in the Logix Designer application (refer to Configure Axis Properties on page 121). An active signal releases the motor brake. Turn-on and turn-off delays are specified by the BrakeEngageDelayTime and BrakeReleaseDelayTime settings. Refer to Brake Current Example on page 176 for brake coil currents.

## IMPORTANT

Holding brakes that are available on Allen-Bradley rotary motors are designed to hold a motor shaft at 0 rpm for up to the rated brake-holding torque, not to stop the rotation of the motor shaft, or be used as a safety device.

You must command the servo drive to 0 rpm and engage the brake only after verifying that the motor shaft is at 0 rpm.

The resistive brake relay (BC-1 and BC-2) controls the resistive brake module (RBM) contactor. The RBM module is wired between the drive and motor by using an internal contactor to switch the motor between the drive and a resistive load. The RBM module contact delay is the time it takes to fully close the contactor across the motor power input lines, and must be configured in the software. Refer to RBM Module Interconnect Diagrams on page 225 for wiring examples.

These steps provide one method you can use to control a brake.

1. Wire the mechanical brake according to the appropriate interconnect diagram in Appendix A beginning on page 151 .
2. Enter the BrakeEngageDelay and BrakeReleaseDelay times in the Logix Designer application.

Refer to Axis Properties&gt;Parameter List. The delay times must be from the appropriate motor family brake specifications table in the Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001 .

3. Use the motion instruction Motion Axis Stop (MAS) to decelerate the servo motor to 0 rpm.
4. Use the motion instruction Motion Servo Off (MSF) to engage the brake and disable drive.

## Input Power Cycle Capability

The power cycle capability is inversely proportional to the system capacitance (including DC bus follower), but cannot exceed 2 contactor cycles per minute with up to 4 axes or 1 contactor cycle per minute with 5…8 axes.

The cycle capability also depends on the converter power rating and the total system capacitance. Refer to Appendix C on page 189 to calculate total system capacitance.

Table 43 - Maximum Input Power Cycling Specifications (230V)

|                                                               | Attribute 2094-AC05-MP5-S 2094-AC05-M01-S 2094-AC09-M02-S 2094-AC16-M03-S 2094-AC32-M05-S   |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Main AC input power cycling (cycles per minute for 10,000 µf) | 0.69 4.30                                                                                   |

Table 44 - Maximum Input Power Cycling Specifications (460V)

|                                                               | Attribute 2094-BC01-MP5-S 2094-BC01-M01-S 2094-BC02-M02-S 2094-BC04-M03-S 2094-BC07-M05-S   |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Main AC input power cycling (cycles per minute for 10,000 µf) | 0.12 0.52 2.15 4.30                                                                         |

For example, in a 4 axis system with a 2094-BC02-M02-S IAM module and 2,000 μF total capacitance, the calculated capability is 0.52 x 10,000/2000 = 2.6 cycles per minute. However, this value is reduced to 2.0 by the 4 axes per system limitation.

## Peak Enhancement Specifications

Drives that support the Peak-enhanced mode have the capability of increasing the maximum inverter peak current to achieve greater overload performance.

## IMPORTANT

The peak enhancement feature requires the use of RSLogix 5000® software or the Logix Designer application, and drive firmware as specified in Table 45 .

Table 45 - Peak Enhancement Software and Firmware Requirements

| IAM Module Cat. No. AM Module Cat. No. RSLogix 5000 Software Version   | Kinetix 6000 Drive Firmware Revision   |
|------------------------------------------------------------------------|----------------------------------------|
| 2094-BC01-MP5-S 2094-BMP5-S 16 or later 1.111 or later                 |                                        |
| 2094-BC01-M01-S 2094-BM01-S 16 or later 1.111 or later                 |                                        |
| 2094-BC02-M02-S 2094-BM02-S 16 or later 1.111 or later                 |                                        |
| 2094-BC04-M03-S 2094-BM03-S 17 or later 1.117 or later                 |                                        |
| 2094-BC07-M05-S 2094-BM05-S 17 or later 1.117 or later                 |                                        |

Table 46 - Kinetix 6000 Inverter Peak Overload Support

| Kinetix 6000 Drives Cat. No.   | Module   | Safe Torque off Drive                 | Series A Series B and later   |
|--------------------------------|----------|-----------------|-------------------------------|
| 2094-BCxx-Mxx                  | IAM      | Non Safe        | Standard N/A                  |
| 2094-BMxx                      | AM       | Torque-off      | Standard N/A                  |
| 2094-BCxx-Mxx-S IAM            |          | Safe Torque-off | Standard or Peak Enhanced (1) |
| 2094-BMxx-S AM                 |          | Safe Torque-off | Standard or Peak Enhanced (1) |

Table 47 - Kinetix 6000 Peak Current Ratings

| IAM/AM Module Cat. No.              | Peak Inverter Current Rating Peak Converter Current Rating   | Peak Inverter Current Rating Peak Converter Current Rating   |
|-------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| IAM/AM Module Cat. No.              | Standard Peak Enhanced Series A Series B and later           |                                                              |
| 2094-BC01-MP5-S 150% 250% 200% 250% |                                                              |                                                              |
| 2094-BC01-M01-S 150% 250% 200% 250% |                                                              |                                                              |
| 2094-BC02-M02-S 150% 250% 200% 250% |                                                              |                                                              |
| 2094-BC04-M03-S 150% 250% 200% 250% |                                                              |                                                              |
| 2094-BC07-M05-S 150% 200% 200% 300% |                                                              |                                                              |
| 2094-BMP5-S 150% 250% N/A N/A       |                                                              |                                                              |
| 2094-BM01-S 150% 250% N/A N/A       |                                                              |                                                              |
| 2094-BM02-S 150% 250% N/A N/A       |                                                              |                                                              |
| 2094-BM03-S 150% 250% N/A N/A       |                                                              |                                                              |
| 2094-BM05-S 150% 200% N/A N/A       |                                                              |                                                              |

Figure 34 - Load Duty-cycle Profile Example

<!-- image -->

Table 48 - Peak Duty Cycle Definition of Terms

| Term                              | Definition (1)                                                                                                                                                                                                                  |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous Current Rating (ICont) | The maximum value of current that can be output continuously.                                                                                                                                                                   |
| Peak Current Rating (IPKmax)      | The maximum value of peak current that the drive can output. This rating is valid only for overload times less than TPKmax .                                                                                                    |
| Duty Cycle (D)                    | The ratio of time at peak to the Application Period and is defined as: D = T T PK  x 100%                                                                                                                                       |
| Time at Peak (T PK )              | The time at peak current (IPK) for a given loading profile. Must be less than or equal to TPKmax .                                                                                                                              |
| Peak Current (I PK )              | The level of peak current for a given loading profile. IPK must be less than or equal to the Peak Current Rating (TPKMAX)   of the drive.                                                                                                                                                                                                                                 |
| Base Current (I Base )            | The level of current between the pulses of peak current for a given loading profile. IBase must be less than or equal to the continuous current rating (ICont) of the drive.                                                    |
| Loading Profile                   | The loading profile is comprised of IPK, IBase, TPK, and D (or T) values and completely specify the operation of the drive in an overload situation. These values are collectively defined as the Loading Profile of the drive. |
| Application Period (T)            | The sum of the times at IPK (TPK) and IBase .                                                                                                                                                                                   |

(1) All current values are specified as RMS.

Figure 35 - Peak Inverter Overload (TPK &lt; 2.0 s)

<!-- image -->

(1) Base current (I Base ) and peak current (IPK) are a percentage of the continuous drive current rating (ICont).

Figure 36 - Peak Inverter Overload (TPK &lt; 2.0 s)

<!-- image -->

## Control Power

The IAM module requires AC input power for logic circuitry.

## IMPORTANT

The control power input requires an AC (EMC) line filter for CE and UK certification. For filter examples, refer to Agency Compliance on page 20 .

## Feedback Specifications

## IMPORTANT

2094-BCxx-Mxx-x (460V) IAM modules require a step down transformer for single-phase control power input. Source the 2094ACxx-Mxx-x (230V) IAM module control power from the three-phase input power (line-to-line) with neither leg bonded to ground or neutral potential. The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder.

Table 49 - Control Power Input Power Specifications

| Attribute Value                                                                              |                                            |
|----------------------------------------------------------------------------------------------|--------------------------------------------|
|                                                                                              | Input voltage 95…264V AC rms, single-phase |
| Input power frequency 47…63 Hz                                                               |                                            |
| Control power AC input current Nom @ 220/230V AC rms Nom @ 110/115V AC rms Max inrush (0-pk) | 6 A 6 A 98 A (1)                           |

I PK = 0.043 x (V IN ) + 6.72 x (# of axes) + 0.000333 x (V IN 2 ) - 0.816 x (# of axes) 2 + 0.0358 x (# of axes x V IN )

Table 50 - Control Power Current Requirements

| 110/115V AC Input 220/230V AC Input                                                                                                                                             | 110/115V AC Input 220/230V AC Input                                                                                                                                             |                                                                                                                                                                                 |                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Modules on Power Rail Input Current A Input VA VA Input VA VA                                                                                                                   | Input Current A                                                                                                                                                                 |                                                                                                                                                                                 |                                                                                                                                                                                 |
|                                                                                                                                                                                 | IAM module only 0.56 67 0.36 85                                                                                                                                                 |                                                                                                                                                                                 |                                                                                                                                                                                 |
|                                                                                                                                                                                 | IAM and 1 AM module 0.99 119 0.64 153                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |
|                                                                                                                                                                                 | IAM and 2 AM module 1.43 172 0.92 220                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |
|                                                                                                                                                                                 | IAM and 3 AM module 1.87 224 1.20 287                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |
| IAM and 4 AM module 2.31 277 1.48 354                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |                                                                                                                                                                                 |
| IAM and 5 AM module 2.74 329 1.75 421                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |                                                                                                                                                                                 |
|                                                                                                                                                                                 | IAM and 6 AM module 3.18 382 2.03 488                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |
| IAM and 7 AM module 3.62 434 2.31 555                                                                                                                                           |                                                                                                                                                                                 |                                                                                                                                                                                 |                                                                                                                                                                                 |
| For specifications and an example for calculating the IPIM module current requirements, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 . | For specifications and an example for calculating the IPIM module current requirements, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 . | For specifications and an example for calculating the IPIM module current requirements, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 . | For specifications and an example for calculating the IPIM module current requirements, refer to the Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 . |

For Kinetix 6000M systems, calculate the sum of the control power current requirements for each IPIM module on the power rail and add that value with the appropriate value from Table 50 for the number of axes on the power rail.

The IAM and AM modules can accept motor and auxiliary feedback signals from these types of encoders:

- Stegmann Hiperface
- TTL or Sine/Cosine with index pulse and Hall commutation
- Resolver Transmitter TR = 0.25 (motor feedback only)

Motor feedback from Heidenhain EnDat high-resolution encoders is also accepted, but only when using drive firmware revision 1.116 or later and the 2090-K6CK-KENDAT low-profile feedback module for EnDat to Hiperface conversion.

<!-- image -->

Auto-configuration in the Logix Designer application of intelligent absolute, high-resolution, incremental, and EnDat encoders is possible only with Allen-Bradley motors.

Table 51 - Absolute Position Designator Examples

| Encoder Type                                   | Cat. No. Designator   | Motor/Actuator Cat. No.                                                                                | Retention Limits (turns)   |
|------------------------------------------------|-----------------------|--------------------------------------------------------------------------------------------------------|----------------------------|
| Stegmann Hiperface                             | -M                    | MPL-A/Bxxxxx-M, MPM-A/Bxxxxx-M, MPF-A/Bxxxxx-M, MPS-A/Bxxxxx-M, MPAR-A/B3xxxx-M, MPAI-A/BxxxxxM        | 4096 (±2048)               |
|                                                | -V                    | MPL-A/Bxxxxx-V, MPAS-A/Bxxxx1-V05, A/MPAS-Bxxxx2-V20, MPAR-A/B1xxxx-V, MPAR-A/B2xxxx-V, MPAI-A/BxxxxxV | 4096 (±2048)               |
| Heidenhain EnDat -7 RDB-Bxxxxxx-7 4096 (±2048) |                       |                                                                                                        |                            |

Figure 37 - Absolute Position Limits (measured in turns)

<!-- image -->

## Motor Feedback Specifications

AM, BM, and IM input encoder signals are filtered by using analog and digital filtering. The inputs also include illegal state change detection.

Table 52 - Motor Encoder Feedback Specifications

| Attribute Value                                                                       |
|---------------------------------------------------------------------------------------|
| Encoder types Incremental, A quad B, sine/cosine, intelligent, resolver, and absolute |
| Maximum input frequency  500 kHz (TTL input) per channel 250 kHz (sine/cosine input)  |
| Commutation feedback Hall sensor                                                      |

Table 53 - AM, BM, and IM Input Specifications for TTL Encoders

|                                           | Parameter Description Min Max                                                                                                              |               |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| AM, BM, and IM On-state input voltage     | Input voltage difference between the plus (+) input and the minus (-) input that is detected as an on-state.                               | +1.0V +7.0V   |
| AM, BM, and IM Off-state input voltage    | Input voltage difference between the plus (+) input and the minus (-) input that is detected as an off-state.                              | -1.0V -7.0V   |
| Common mode input voltage                 | Potential difference between any encoder signal and logic ground.                                                                          | -7.0V +12.0V  |
|                                           | DC current draw Current draw into the + or - input. -30 mA 30 mA                                                                           |               |
| AM, BM input signal frequency             | Frequency of the AM or BM signal inputs. The count frequency is 4 times this frequency, because the circuitry counts all four transitions. | – 500 kHz     |
| IM pulse width                            | Pulse width of the index input signal. Because the index is active for a percentage of a revolution, the speed determines the pulse width. | 125 nS –      |
| AM, BM phase error 250 KHz line frequency | Amount that the phase relationship between the AM ° pp  and BM inputs can deviate from the nominal 90°.                                                                                                                                            | -22.5° +22.5° |
| AM, BM phase error 100 KHz line frequency | Amount that the phase relationship between the AM ° pp  and BM inputs can deviate from the nominal 90°.                                                                                                                                            | -45° +45°     |

## Absolute Position Feature

The drive's absolute position feature tracks the position of the motor, within the multi-turn retention limits, while the drive is powered off. The absolute position feature is available with only these multi-turn encoders.

Table 54 - AM, BM, and IM Input Specifications for Sine/Cosine Encoders

|                                    | Parameter Description Min Max                             |                       |
|------------------------------------|-----------------------------------------------------------|-----------------------|
| Sine/cosine input signal frequency | Frequency of the Sine or Cosine signal inputs.            | – 250 kHz             |
| Sine/cosine input voltage          | Peak-to-peak input voltages of the Sine or Cosine inputs. | 0.8V (p-p) 1.2V (p-p) |

Table 55 - Specifications for Heidenhain EnDat Encoders

| Command Set   | Order Designation   | Description                                               |
|---------------|---------------------|-----------------------------------------------------------|
|               |                     | EnDat 2.2 EnDat 01 1V p-p Sin/Cos, <2 MHz clock frequency |

## Feedback Power Supply Specifications

The IAM and AM power circuit board generates +5V and +9V DC for motor and auxiliary feedback power. Short circuit protection and separate common mode filtering for each channel is included.

| Supply Reference                  | Voltage Current mA      | Voltage Current mA   |
|-----------------------------------|-------------------------|----------------------|
|                                   | Min Nominal Max Min Max |                      |
| +5V DC EPWR_5V 4.9 5.25 5.4 0 400 |                         |                      |
| +9V DC EPWR_9V 8.3 9.1 9.9 0 275  |                         |                      |

## Auxiliary Position Feedback Encoders

Allen-Bradley Bulletin 842HR, 844D, 847H, and 847T encoders are the preferred encoders for auxiliary feedback connections.

Table 56 - Allen-Bradley Auxiliary Feedback Encoders

|                                                                | Cat. No. Description                                                                                                                                                       |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 842HR-MJDZ115FWYD (multi-turn) 842HR-SJDZ115FWYD (single-turn) | Size 25, sine/cosine (serial), square flange, 3/8 in. solid shaft with flat, 5…12V DC, digital RS-485 interface, M23, 17-pin connector                                     |
| 844D-B5CC1FW                                                   | HS35, hollow-shaft incremental encoders, rear (through-shaft), 5/8 inch, tether, 3/8 in. bolt on a 2.5…4.0 in. diameter, 10-pin connector, 5V DC in, 5V DC DLD out         |
| 844D-B5CC1CS                                                   | HS35, hollow-shaft incremental encoders, rear (through-shaft), 5/8 inch, tether, 3/8 in. bolt on a 2.5…4.0 in. diameter, 10-pin connector, 5V DC in, 5V DC DLD out         |
| 844D-B5CC1DR                                                   | HS35, hollow-shaft incremental encoders, rear (through-shaft), 5/8 inch, tether, 3/8 in. bolt on a 2.5…4.0 in. diameter, 10-pin connector, 5V DC in, 5V DC DLD out         |
| 847H-DN1A-RH01024                                              | Size 25, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z gated with BN), MS connector, 10-pin |
| 847H-DN1A-RH02048                                              | Size 25, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z gated with BN), MS connector, 10-pin |
| 847H-DN1A-RH05000                                              | Size 25, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, CW, Z gated with BN), MS connector, 10-pin |
|                                                                | 847T-DN1A-RH01024 Size 20, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, ,  CW, Z gated with BN), MS connector, 10-pin 847T-DN1A-RH02048                                                                                                                                                                            |
|                                                                | 847T-DN1A-RH01024 Size 20, incremental encoder, standard square flange , 3/8 inch diameter shaft with flat, 4.5…5.5V line driver, TTL (B-Leads-A, ,  CW, Z gated with BN), MS connector, 10-pin 847T-DN1A-RH02048                                                                                                                                                                            |

Refer to the Kinetix Rotary and Linear Motion Cable Specifications, publication KNX-TD004, for more information on these Allen-Bradley encoders.

## Basic Wiring Requirements

<!-- image -->

## Connect the Kinetix 6000 Drive System

This chapter provides procedures for wiring your Kinetix® 6000 drive system components and making cable connections.

| Topic Page                                                  |
|-------------------------------------------------------------|
| Basic Wiring Requirements 65                                |
| Determine the Input Power Configuration 66                  |
| Set the Ground Jumper in Select Power Configurations 70     |
| Grounding the Kinetix 6000 Drive System 75                  |
| Power Wiring Requirements 77                                |
| Power Wiring Guidelines 78                                  |
| Wiring the IAM/AM Module Connectors 79                      |
| Apply the Motor Cable Shield Clamp 90                       |
| Feedback and I/O Cable Connections 91                       |
| Wiring the Feedback and I/O Connectors 95                   |
| External Shunt Module Connections 99                        |
| IPIM Module Connections 100                                 |
| RBM Module Connections 101                                  |
| Sercos Fiber-optic Cable Connections 102                    |
| Kinetix 6000M Integrated Drive-Motor Sercos Connections 104 |
| Ethernet Cable Connections 105                              |

This section contains basic wiring information for the Kinetix 6000 drive modules.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Bulletin 2094 power rail and drive modules prior to applying power. Once power is applied, connector terminals can have voltage present even when not in use.

## Determine the Input Power Configuration

## IMPORTANT

This section contains common PWM servo system wiring configurations, size, and practices that can be used in a majority of applications. National Electrical Code, local electrical codes, special operating temperatures, duty cycles, or system configurations take precedence over the values and methods provided.

## Building Your Own Cables

## IMPORTANT

Factory-made cables are designed to minimize EMI and are recommended over hand-built cables to optimize system performance.

Building your own cables is not an option for the hybrid and network cables used in Kinetix 6000M integrated drive-motor systems.

Follow these guidelines when building cables for compatible motors and actuators:

- Connect the cable shield to the connector shells on both ends of the cable with a complete 360° connection.
- Use twisted pair cable whenever possible. Twist differential signals with each other and twist single-ended signals with the appropriate ground return.

Refer to the Kinetix Rotary and Linear Motion Cable Specifications, publication KNX-TD004, for low-profile connector kit, drive-end (mating) connector kit, and motor-end connector kit catalog numbers.

## Routing the Power and Signal Cables

Be aware that when you route power and signal wiring on a machine or system, radiated noise from nearby relays, transformers, and other electronic drives can be induced into motor or encoder feedback signals, input/output communication, or other sensitive low voltage signals. This can cause system faults and communication anomalies.

Refer to Electrical Noise Reduction on page 27 for examples of routing high and low voltage cables in wireways. Refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, for more information.

Before wiring input power to your Kinetix 6000 system, you must determine the type of input power you are connecting to. The IAM module is designed to operate in both grounded and ungrounded environments.

<!-- image -->

ATTENTION: When you are using a LIM module for input power, the VAC LINE input power must come from a grounded configuration. When you are not using a LIM module for input power, ungrounded, cornergrounded, and impedance-grounded power configurations are permitted, but you must set the ground jumper to the ungrounded position for proper drive operation. In addition, set the ground jumper when an active converter supplies the DC-bus voltage. Refer to Set the Ground Jumper in Select Power Configurations on page 70 for more information.

<!-- image -->

ATTENTION: For IEC 61800-3 category C3 compliance, use the appropriate AC line filter with a grounded WYE configuration. The use of a line filter in an ungrounded, corner-grounded, or impedancegrounded configuration can affect the line filter components and result in equipment damage.

## Grounded Power Configurations

The grounded (WYE) power configuration lets you ground your three-phase power at a neutral point. This type of grounded power configuration is preferred.

Figure 38 - Grounded Power Configuration (WYE Secondary)

<!-- image -->

The IAM module has a factory-installed ground jumper for grounded power distribution.

## IMPORTANT

If you determine that you have grounded power distribution in your facility, you do not need to move the ground jumper.

Refer to Power Wiring Examples on page 152 for input power interconnect diagrams with and without the LIM module.

Figure 39 - Corner-grounded Power Configuration (Delta Secondary)

<!-- image -->

Figure 40 - Impedance-grounded Power Configuration (WYE Secondary)

<!-- image -->

## IMPORTANT

Even though impedance-grounded and corner-grounded power configurations have a ground connection, treat them as ungrounded when installing Kinetix 6000 drive systems.

## Ungrounded Power Configurations

The ungrounded power configuration (Figure 41) does not provide a neutral ground point. Ungrounded, impedance-grounded, and corner-grounded power configurations are allowed, but you must move a jumper (internal to the

## DC Common Bus Configurations

IAM module) across a 120 k resistor. The IAM module ground jumper (default configuration) is set for grounded power distribution.

## IMPORTANT

If you determine that you have ungrounded, impedance-grounded, or corner-grounded power distribution in your facility, you must move the ground jumper (configured for grounded power) to the ungrounded power position inside the IAM module.

Refer to Set the Ground Jumper in Select Power Configurations on page 70 for more information.

Figure 41 - Ungrounded Power Configuration

<!-- image -->

<!-- image -->

ATTENTION: Ungrounded systems do not reference each phase potential to a power distribution ground. This can result in an unknown potential to earth ground.

Refer to Power Wiring Examples on page 152 for input power interconnect diagrams with and without the LIM module.

When the IAM module is used in a DC common-bus configuration, the IAM module is known as a leader IAM or follower IAM module. The IAM (noncommon bus) and leader IAM module have identical three-phase input power connections. The leader IAM module is responsible for discharging the DC bus, and for providing common-bus follower drives with DC bus precharge, bus regulation, phase-loss detection, and ground fault detection. Follower IAM modules do not have three-phase input power connections, but have DC bus connections from a leader IAM module.

Table 57 - IAM Module Terminology and Use

| This Module Is Wired And is   |                                                                                              |                                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|                               | IAM With three-phase input power.                                                            | Not wired in Common-bus mode.                                                    |
| Leader IAM                    | With three-phase input power, but has DC common-bus connections to a follower IAM module.    | Wired in Common-bus mode.                                                        |
| Follower IAM                  | Without three-phase input power, but has DC common-bus connections from a leader IAM module. | Wired in Common-bus mode and configured by using the Logix Designer application. |

## IMPORTANT

Use Kinetix 6000 drive firmware revision 1.85 and the Logix Designer Application or RSLogix 5000® software, version 15 or later, for common-bus power configurations.

## Set the Ground Jumper in Select Power Configurations

The Kinetix 6000 leader IAM module can operate with non-Kinetix 6000 follower drives, as can the Kinetix 6000 follower IAM module operate with non-Kinetix 6000 common-bus leader drives. However, non-Kinetix 6000 leader and follower drives must meet the same functional requirements as the Kinetix 6000 leader and follower IAM modules.

## IMPORTANT

Any non-Kinetix 6000 common-bus leader IAM module that does not provide precharge is required to add an additional external precharge circuit before connecting to any Kinetix 6000 commonbus follower IAM module.

Figure 42 - Typical DC Common-bus Configuration

<!-- image -->

## Common Bus Fusing Requirements

When using a Kinetix 6000 leader IAM module, DC-bus fuses are required only when wiring to more than one Kinetix 6000 follower IAM module. When wiring multiple follower IAM modules, terminal blocks are required to extend the DC common-bus power to additional drives. Install fuses in both lines of the DC bus between the DC bus terminal block and each follower IAM module. Base these fuse ratings on the DC input current of each follower IAM module.

When using a non-Kinetix 6000 common-bus leader drive, DC bus fuses are required in both lines of the DC bus, between the common-bus leader drive and follower IAM module. Base these fuse ratings on the common-bus leader drive DC output current. When using more than one follower IAM module, install fuses in both lines of the DC bus between the non-Kinetix 6000 common-bus leader and the terminal block as well as between the DC bus terminal block and each follower IAM module.

Refer to Circuit Breaker/Fuse Options on page 23, for recommended circuit breaker/fuse sizes. Refer to DC Common Bus Wiring Examples on page 156 for interconnect diagrams.

Setting the ground jumper is required when using an ungrounded, cornergrounded, and impedance-grounded power configurations. Setting the ground jumper is also required when the Bulletin 8720MC regenerative power supply or any active converter provides DC-bus power.

Setting the jumper involves removing the IAM module from the power rail, opening the IAM module, and moving the jumper.

## IMPORTANT

<!-- image -->

If you have grounded power distribution, you do not need to set the ground jumper. Go to Grounding the Kinetix 6000 Drive System on page 75 .

ATTENTION: Because the unit no longer maintains line-to-neutral voltage protection, risk of equipment damage exists when you move the ground jumper.

Setting the ground jumper is best done when the IAM module is removed from the power rail and placed face-up on a solid surface equipped as a grounded static-safe workstation.

<!-- image -->

ATTENTION: This drive contains electrostatic discharge (ESD) sensitive parts and assemblies. You are required to follow static-control precautions when you install, test, service, or repair this assembly. If you do not follow ESD control procedures, components can be damaged. If you are not familiar with static control procedures, refer to Guarding Against Electrostatic Damage, publication 8000-4.5.2, or any other applicable ESD awareness handbook.

When using ungrounded input power in common-bus configurations, use this table to determine where to set the ground jumper.

## Table 58 - Ground Jumper to Set

| Leader Drive Follower Drive Set the Jumper in This Drive                                                  |
|-----------------------------------------------------------------------------------------------------------|
| Kinetix 6000 IAM module Kinetix 6000 IAM module Leader drive                                              |
| Kinetix 6000 IAM module Non-Kinetix 6000 drive Leader drive                                               |
| Non-Kinetix 6000 drive Kinetix 6000 IAM module  Follower drive (if no setting exists in the leader drive) |

<!-- image -->

ATTENTION: Risk of equipment damage exists. The facility ground configuration must be accurately determined. Do not move the ground jumper for grounded power configurations (default). Move the ground jumper for ungrounded, corner-grounded, and impedance-grounded power, or when an active converter supplies the DC-bus voltage.

## Table 59 - Ground Jumper Configurations

|                                                            |                                                                | Ground Configuration Example Diagram Ground Jumper Configuration   | Benefits of Correct Configuration                                                                                                    |
|------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Grounded (wye)                                             | Figure 38 on page 67                                           | Grounded power (default setting)                                   | • UL and EMC compliance • Reduced electrical noise • Most stable operation • Reduced voltage stress on components and motor bearings |
| • AC-fed ungrounded • Corner grounded • Impedance grounded | Figure 41 on page 69 Figure 39 on page 68 Figure 40 on page 68 | Set for ungrounded power                                           | • Helps avoid severe equipment damage when ground faults occurs g • Reduced leakage current DC-bus from active t Figure 92 on page 159                                                                                                                                      |
| converter                                                  | Figure 92 on page 159                                          | Set for ungrounded power                                           |                                                                                                                                      |

## Set the Ground Jumper

<!-- image -->

ATTENTION: To avoid personal injury, the ground jumper access area must be kept closed when power is applied. If power was present and then removed, wait at least 5 minutes for the DC-bus voltage to dissipate and verify that no DC-bus voltage exists before accessing the ground jumper.

Follow these steps to set the ground jumper for ungrounded power.

1. Remove the IAM module from the power rail.
2. For detailed instructions, refer to Remove Kinetix 6000 Drive Modules on page 147 .
2. Remove the top and bottom front-panel screws.

Refer to the figures beginning on page 73 (230V IAM module) or page 74 (460V IAM module) for an illustration of your actual hardware.

3. Swing the front panel open to the right, as shown, and locate the ground jumper

## IMPORTANT

Do not attempt to remove the front panel from the IAM module. The front panel status indicators and switches are also connected to the IAM module with a ribbon cable. The ribbon cable acts like a hinge and lets you swing the front panel open to access the ground jumper.

4. Move the ground jumper.
5. Replace the IAM module front panel and two screws. Apply 1.6 N·m (14 lb·in) torque.
6. Mount the IAM module back on the power rail. For detailed instructions, refer to Replace Kinetix 6000 Drive Modules on page 148 .

| IAM Module (series A)         | Configuration                 | Configuration   |
|-------------------------------|-------------------------------|-----------------|
| IAM Module (series A)         | Grounded (default) Ungrounded |                 |
| 2094-ACxx-Mxx - x  (230V) (1) | P15 and P16 P15 and P17       |                 |
| 2094-BC01-MP5-x (460V)        | P13 and P14 P13 and P12       |                 |
| 2094-BC01-M01-x (460V)        | P13 and P14 P13 and P12       |                 |
| 2094-BC02-M02-x (460V)        | P13 and P14 P13 and P12       |                 |
| 2094-BC04-M03-x (460V)        | P14 and P13 P14 and P12       |                 |
| 2094-BC07-M05-x (460V)        | P14 and P13 P14 and P12       |                 |

| IAM Module (Series B and later)   | Configuration Grounded (default) Ungrounded   |
|-----------------------------------|-----------------------------------------------|
| 2094-BC01-MP5-S (460V)            | P16 and P17 P18 and P19                       |
| 2094-BC01-M01-S (460V)            | P16 and P17 P18 and P19                       |
| 2094-BC02-M02-S (460V)            | P16 and P17 P18 and P19                       |
| 2094-BC07-M05-S (460V)            | P16 and P17 P18 and P19                       |
|                                   | P16 and P17 P18 and P19                       |

.

Figure 43 - Setting the Ground Jumper (230V Series A, C, D, and E IAM modules)

<!-- image -->

IMPORTANT

Use the default jumper setting or remove the jumper entirely for grounded power configurations. Move the jumper, as shown above, for ungrounded power.

<!-- image -->

## IMPORTANT

Use the default jumper setting or remove the jumper entirely for grounded power configurations. Move the jumper, as shown above, for ungrounded power.

<!-- image -->

## Grounding the Kinetix 6000 Drive System

All equipment and components of a machine or process system must have a common earth ground point connected to chassis. A grounded system provides a ground path for short circuit protection. Grounding your modules and panels minimize shock hazard to personnel and damage to equipment caused by short circuits, transient overvoltages, and accidental connection of energized conductors to the equipment chassis.

<!-- image -->

ATTENTION: The National Electrical Code contains grounding requirements, conventions, and definitions. Follow all applicable local codes and regulations to safely ground your system. For CE and UK grounding requirements, refer to Agency Compliance on page 20 .

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

## Power Wiring Requirements

## Table 60 - IAM Power Wiring Requirements

| Kinetix 6000 Drive Cat. No.       |                                | Connects to Terminals Recommended Wire   | Connects to Terminals Recommended Wire   | Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)                 |
|-----------------------------------|--------------------------------|------------------------------------------|------------------------------------------|-------------------|-------------------------|------------------------------------------|
| Kinetix 6000 Drive Cat. No.       |                                |                                          | Pin Signal                               | Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)                 |
| 2094-AC05-Mxx - x                 | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 DC DC+                                          | 6…2.5 (10…14)     | 10 (0.38)               | 0.5…0.6 (4.4…5.3)                        |
| 2094-AC09-M02-x                   | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 DC DC+                                          | 6…4 (10…12)       | 10 (0.38)               | 0.5…0.6 (4.4…5.3)                        |
| 2094-AC16-M03-x                   | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 DC DC+                                          | 30…10 (3…8)       | 16 (0.63)               | 2.4…3.0 (21.6…26.5)                      |
| 2094-AC32-M05-x                   | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 DC DC+                                          | 30 (3)            | 16 (0.63)               | 2.4…3.0 (21.6…26.5)                      |
| 2094-BC01-Mxx - x 2094-BC02-M02-x | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 L1 DC DC+                                          | 10…2.5 (8…14)     | 10 (0.38)               | 1.2…1.5 (10.6…13.2)                      |
| 2094-BC04-M03-x                   | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 L1 DC DC+                                          | 10…6 (8…10)       | 16 (0.63)               | 2.4…3.0 (21.6…26.5)                      |
| 2094-BC07-M05-x                   | DC bus (1) and VAC input power | IPD-1 IPD-2 IPD-3 IPD-4 IPD-5            | L3 L2 L1 DC DC+                                          | 30 (3)            | 16 (0.63)               | 2.4…3.0 (21.6…26.5)                      |
| 2094-xCxx-Mxx - x                 | Control input power            |                                          | CPD-1 CTRL 2                             | 4…2.5 (12…14)     | 10 (0.38)               | 0.5…0.6 (12…14) 10(4.4…5.3) CPD-2 CTRL 1 |
| 2094-xCxx-Mxx - x                 | Contactor Enable               |                                          | CED-1 CONT EN-                           | 4…2.5 (12…14) (2) (12…14) (2) (4.4…5.3) CED-2 CONT EN+                   | 10 (0.38)               | 0.5…0.6                                  |
| 2094-xCxx-Mxx - x                 | Contactor Enable               |                                          |                                          | 4…2.5 (12…14) (2) (12…14) (2) (4.4…5.3) CED-2 CONT EN+                   |                         | 0.5…0.6                                  |
| 2094-xCxx-Mxx - x                 |                                |                                          |                                          |                   |                         |                                          |

<!-- image -->

ATTENTION: To avoid personal injury and/or equipment damage, make sure installation complies with specifications regarding wire types, conductor sizes, branch circuit protection, and disconnect devices. The National Electrical Code (NEC) and local codes outline provisions for safely installing electrical equipment.

ATTENTION: To avoid personal injury and/or equipment damage, make sure motor power connectors are used for connection purposes only. Do not use them to turn the unit on and off.

ATTENTION: To avoid personal injury and/or equipment damage, make sure shielded power cables are grounded to prevent potentially high voltages on the shield.

High-frequency (HF) bonding is not illustrated. For HF bonding information, refer to HF Bond for Multiple Subpanels on page 28 .

Wire must be copper with 75 °C (167 °F) minimum rating. Phasing of main AC power is arbitrary and earth ground connection is required for safe and proper operation.

For IPIM module power wiring requirements, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Refer to Power Wiring Examples on page 152 for interconnect diagrams.

IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

Table 61 - IAM/AM Power Wiring Requirements

| Kinetix 6000 Drive Cat. No.                                                                                                                             | Description     | Connects to Terminals Recommended Wire                | Connects to Terminals Recommended Wire   | Size 2                                                               | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------------------------------------------|------------------------------------------|----------------------------------------------------------------------|-------------------------|----------------------------|
|                                                                                                                                                         |                 |                                                       | Pin Signal                               | mm (AWG)                                                             |                         |                            |
| 2094-AC05-Mxx-x, 2094-AC09-M02-x, 2094-BC01-Mxx - x, 2094-BC02-M02-x, 2094-AMP5-x, 2094-AM01-x, 2094-AM02-x, 2094-BMP5-x,  x,  2094-BM01-x, 2094-BM02-x | Motor power     | MP-4 MP-3 MP-2 MP-1                                   | W V U                                    | Motor power cable depends on motor/ drive combination. 6…1.5 (10…16) | 10 (0.38)               | 0.5…0.6 (4.4…5.3)          |
| 2094-AC16-M03-x, 2094-AC32-M05-x, 2094-BC04-M03-x, 2094-AM03-x, 2094-AM05-x,  2094-BM03-x                                                               | Motor power     | MP-4 MP-3 MP-2 MP-1                                   | W V U                                    | 10…1.5 (8…16)                                                        | 10 (0.38)               | 1.2…1.5 (10.6…13.2)        |
| 2094-BC07-M05-x, 2094-BM05-x                                                                                                                            | Motor power     | MP-4 MP-3 MP-2 MP-1                                   | W V U                                    | 30…2.5 (3…14)                                                        | 16 (0.63)               | 2.4…3.0 (21.6…26.5)        |
| IAM or AM (230 or 460V) 2094-xCxx-Mxx - x and 2094-xMxx - x                                                                                             | Brake power     | BC-6 BC-5 BC-4 BC-3 BC-2 BC-1                         | MBRK MBRK+ COM PWR DBRK DBRK+                                          |                                                                      | 0.75 (18) 10 (0.38)     | 0.22…0.25 (1.9…2.2)        |
| IAM or AM (230 or 460V) 2094-xCxx-Mxx-S and 2094-xMxx-S                                                                                                 | Safe torque-off | STO-1 STO-2 STO-3 STO-4 STO-5 STO-6 STO-7 STO-8 STO-9 | FDBK2+ FDBK2- FDBK1+ FDBK1- SAFETY ENABLE2+ SAFETY ENABLE SAFETY ENABLE1+ 24V + 24V_COM                                          | 0.75 (18) (stranded wire with ferrule) 1.5 (16) (solid wire)         |                         | 7.0 (0.275) 0.235 (2.0)    |

Table 62 - Shunt Module Power Wiring Requirements

|                                         |                                           | Connects to Terminals Recommended Wire   | Size mm 2 (AWG)   | Torque Value N•m (lb•in)   |
|-----------------------------------------|-------------------------------------------|------------------------------------------|-------------------|----------------------------|
| Drive Module Cat. No. Description       |                                           | Pin Signal                               |                   |                            |
| 2094-BSP2 Shunt module (200/400V-class) | 1394-SRxxxx External passive shunt module | RC-1 DC+                                 | 10 (8) (1)        | 1.2…1.5 (10.6…13.2)        |
| 2094-BSP2 Shunt module (200/400V-class) | 1394-SRxxxx External passive shunt module | RC-2 INT                                 | 10 (8) (1)        | 1.2…1.5 (10.6…13.2)        |
| 2094-BSP2 Shunt module (200/400V-class) | 1394-SRxxxx External passive shunt module | RC-3 COL                                 | 10 (8) (1)        | 1.2…1.5 (10.6…13.2)        |
| 2094-BSP2 Shunt module (200/400V-class) | Thermal switch                            | TS-1 TS1                                 | 0.75 (18)         | 0.22…0.25 0.75 (18)  (1.9…2.2) TS-2 TS2                            |
| 2094-BSP2 Shunt module (200/400V-class) | Thermal switch                            |                                          | 0.75 (18)         | 0.22…0.25 0.75 (18)  (1.9…2.2) TS-2 TS2                            |

## Power Wiring Guidelines

Use these guidelines as a reference when wiring the power connectors on your IAM and AM drive modules.

For IPIM module power wiring guidelines, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

| IMPORTANT   | For connector locations of the Kinetix 6000 drive modules, refer to 2094 IAM/AM Module Connector Data on page 47 . When tightening screws to secure the wires, refer to the tables beginning on page 77 for torque values. When removing insulation from wires, refer to the tables beginning on page 77 for strip lengths.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | To improve system performance, run wires and cables in the wireways as established in Establish Noise Zones on page 29 .                                                                                                                                                                                                      |

## Wiring the IAM/AM Module Connectors

Follow these steps when wiring the connectors on your IAM and AM drive modules.

1. Prepare the wires for attachment to each connector plug by removing insulation equal to the recommended strip length.

## IMPORTANT

Use caution not to nick, cut, or otherwise damage strands as you remove the insulation.

2. Route the cable/wires to your IAM and AM drive modules.
3. Insert wires into connector plugs.
3. Refer to connector pinout tables in Chapter 4 or the interconnect diagrams in Appendix A .
4. Tighten the connector screws.
5. Gently pull on each wire to make sure it does not come out of its terminal; reinsert and tighten any loose wires.
6. Insert the connector plug into the module connector.

This section provides examples and wiring tables to assist you in making connections to the IAM and AM modules.

## Wire the Control Power (CPD) Connector

This example applies to any IAM, leader IAM, or follower IAM module.

Figure 48 - IAM Module (CPD connector)

<!-- image -->

## IMPORTANT

The 2094-AL75S, 2094-BL75S, and 2094-XL75S-C2 LIM modules can supply input power for up to eight axes. The 2094-XL75S-C1 LIM module can supply up to sixteen axes.

The IPIM module control power load must be calculated for Kinetix 6000M systems and the LIM module control power input must have a sufficient current rating. If no LIM module can support the current requirement, then discrete components must be used.

The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder.

Refer to Control Power on page 61 for more information and IAM Module (without LIM module) on page 155 for the interconnect drawing.

Table 63 - Control Power (CPD) Connector

| CPL Connector (LIM module) or Other Single-phase Input   | CPL Connector (LIM module) or Other Single-phase Input   | CPD Connector (IAM module)         | CPL Connector (LIM module) or Other Single-phase Input   |    |
|----------------------------------------------------------|----------------------------------------------------------|------------------------------------|----------------------------------------------------------|----|
| 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM Module      | 2094-AL09 and 2094-BL02 LIM Module                       | 2094-AL09 and 2094-BL02 LIM Module |                                                          |    |
|                                                          | CPL Pin Signal CPL Pin Signal CPD Pin Signal             |                                    |                                                          |    |
|                                                          |                                                          | 1 CTRL 1 2 L1 1 CTRL 2             | 2.5 (14) 10 (0.38)                                       | 0.5…0.6 2.5 (14) 10 (0.38)  (4.4…5.3) 2 CTRL 2 1 L2/N 2 CTRL 1    |
|                                                          |                                                          |                                    | 2.5 (14) 10 (0.38)                                       | 0.5…0.6 2.5 (14) 10 (0.38)  (4.4…5.3) 2 CTRL 2 1 L2/N 2 CTRL 1    |

## Wire the Input Power (IPD) Connector

This example applies to any IAM module or common-bus leader IAM module.

<!-- image -->

ATTENTION: Make sure the input power connections are correct when wiring the IPD connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause explosion or damage to equipment.

Figure 49 - IAM Module (IPD connector)

<!-- image -->

Table 64 - Input Power (IPD) Connections

| OPL Connector (LIM module) or Other Three-phase Input   | OPL Connector (LIM module) or Other Three-phase Input                  | IPD Connector (IAM or leader IAM module) 2094-AL09 LIM Mdl 2094-ALxxS, 2094-BLxxS, or 2094XL75SCLIM Mdl       | IPD Connector (IAM or leader IAM module) 2094-AL09 LIM Mdl 2094-ALxxS, 2094-BLxxS, or 2094XL75SCLIM Mdl     |
|---------------------------------------------------------|------------------------------------------------------------------------|-------|-----|
| LIM Module                                              | 2094-XL75S-Cx LIM Modules OPL Pin Signal OPL Pin Signal IPD Pin Signal |       |     |
|                                                         | 1 L1’ 4 L1’ 6 L1                                                       |       |     |
|                                                         | 2 L2’ 3 L2’ 5 L2                                                       |       |     |
|                                                         | 3 L3’ 2 L3’ 4 L3                                                       |       |     |
|                                                         | 41 3                                                                   |       |     |
|                                                         |                                                                        | 2 DC+ |     |
| N/A                                                     | N/A                                                                    | 1 DC       | N/A |

Table 65 - Termination Specifications

| IAM Module Cat. No. Input VAC     |         | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-----------------------------------|---------|------------------------------------|-------------------------|----------------------------|
| 2094-AC05-Mxx - x                 | 230V AC | 2.5 (14)                           | 10 (0.38)               | 0.5…0.6                    |
| 10 (0.38)  (4.4…5.3) 2094-AC09-M02-x 4.0 (12)                                   | 230V AC | 4.0 (12)                           | 10 (0.38)               | 0.5…0.6                    |
| 2094-AC16-M03-x                   | 230V AC | 10 (8)                             | 16 (0.63)               | 2.4…3.0                    |
| 16 (0.63)  (21.6…26.5) 2094-AC32-M05-x 30 (3)                                   | 230V AC | 30 (3)                             | 16 (0.63)               | 2.4…3.0                    |
| 2094-BC01-Mxx - x 2094-BC02-M02-x | 460V AC |                                    | 2.5 (14) 10 (0.38)      | 1.2…1.5 (10.6…13.2)        |
| 2094-BC04-M03-x                   | 460V AC | 6 (10)                             | 16 (0.63)               | 2.4…3.0                    |
| 16 (0.63)  (21.6…26.5) 2094-BC07-M05-x 30 (3)                                   | 460V AC | 30 (3)                             | 16 (0.63)               | 2.4…3.0                    |

This example applies to a common-bus follower IAM module.

<!-- image -->

ATTENTION: Make sure the common-bus power connections are correct when wiring the IPD connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause explosion or damage to equipment.

Figure 50 - IAM Module (IPD connector)

<!-- image -->

Table 66 - Input Power (IPD) Connections

| IPD Connector (IAM or follower IAM module)   | IPD Connector (IAM or follower IAM module)   |
|----------------------------------------------|----------------------------------------------|
| IPD Pin Signal                               |                                              |
| 6 N.C.                                       |                                              |
| 5 N.C.                                       |                                              |
| 4 N.C.                                       |                                              |
| 3                                            |                                              |
| 2 DC+                                        |                                              |
| 1 DC                                              |                                              |

IMPORTANT

Do not connect three-phase input power to the common-bus follower IAM module.

Table 67 - Termination Specifications

| IAM Module Cat. No. Input VAC     |         | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-----------------------------------|---------|------------------------------------|-------------------------|----------------------------|
| 2094-AC05-Mxx - x                 | 230V AC | 2.5 (14)                           | 10 (0.38)               | 0.5…0.6                    |
| 10 (0.38)  (4.4…5.3) 2094-AC09-M02-x 4.0 (12)                                   | 230V AC | 4.0 (12)                           | 10 (0.38)               | 0.5…0.6                    |
| 2094-AC16-M03-x                   | 230V AC | 10 (8)                             | 16 (0.63)               | 2.4…3.0                    |
| 16 (0.63)  (21.6…26.5) 2094-AC32-M05-x 30 (3)                                   | 230V AC | 30 (3)                             | 16 (0.63)               | 2.4…3.0                    |
| 2094-BC01-Mxx - x 2094-BC02-M02-x | 460V AC |                                    | 2.5 (14) 10 (0.38)      | 1.2…1.5 (10.6…13.2)        |
| 2094-BC04-M03-x                   | 460V AC | 6 (10)                             | 16 (0.63)               | 2.4…3.0                    |
| 16 (0.63)  (21.6…26.5) 2094-BC07-M05-x 30 (3)                                   | 460V AC | 30 (3)                             | 16 (0.63)               | 2.4…3.0                    |

## Wire the Contactor Enable (CED) Connector

This example applies to any IAM, common-bus leader IAM, or common-bus follower IAM module.

Table 68 - Contactor Enable (CED) Connector

| LIM Module I/O (IOL) Connector or Other Control String   | LIM Module I/O (IOL) Connector or Other Control String   |                | Recommended Wire Size mm 2   |                       |                          |
|----------------------------------------------------------|----------------------------------------------------------|----------------|------------------------------|-----------------------|--------------------------|
| 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM Module      | 2094-AL09 and 2094-BL02 LIM Module                       | CED Pin Signal | (AWG)                        | Strip Length mm (in.) | Torque Value N•m (lb•in) |
|                                                          |                                                          | IO_COM1 IO_COM 1 CONT EN                | 2.5 (14) (1)                 | 10 (0.38)             | 0.5…0.6 2.5 (14) ( ) 10 (0.38)  (4.4…5.3) COIL_E2 COIL_A2 2 CONT EN+                          |
|                                                          |                                                          |                | 2.5 (14) (1)                 | 10 (0.38)             | 0.5…0.6 2.5 (14) ( ) 10 (0.38)  (4.4…5.3) COIL_E2 COIL_A2 2 CONT EN+                          |

## Wiring the Safe Torque-off (STO) Connector

This example applies to any IAM or AM module equipped with the torque-off (STO) connector.

Figure 52 - IAM/AM Module (STO connector)

<!-- image -->

Each IAM and AM module ships with the (9-pin) wiring-plug header and motion-allowed jumper installed in the safe torque-off connector. With the motion-allowed jumper installed, the safe torque-off feature is not used.

Kinetix 6000 IAM/AM Module (AM module is shown)

Figure 51 - IAM Module (CED connector)

<!-- image -->

<!-- image -->

ATTENTION: Wiring the contactor enable relay is required. To avoid personal injury or damage to the drive, wire the contactor enable relay into your control string. Refer to Contactor Enable Relay on page 56 . In common-bus configurations, the contactor enable (CED) connections for leader and follower drives must be wired in series to the control string.

For interconnect diagrams, refer to Interconnect Diagram Notes on page 151 .

Pinouts for the torque-off (STO) connector are shown on page 49 .

## IMPORTANT

Pins STO-8 and STO-9 (24V+) are used by only the motion-allowed jumper. When wiring to the wiring-plug header, the 24V supply must come from an external source.

Table 69 - Safe Torque-off (STO) Connector

| STO Pin Signal    | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------|------------------------------------|-------------------------|----------------------------|
| 1 FDBK2+          | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 2 FDBK2-          | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 3 FDBK1+          | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 4 FDBK1-          | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 5 SAFETY ENABLE2+ | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 6 SAFETY ENABLE                   | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 7 SAFETY ENABLE1+ | (solid wire)                       |                         | 7.0 (0.275) 0.235 (2.0)    |
| 8 24V +           | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |
| 9 24V_COM         | ferrule) 1.5 (16)                  |                         | 7.0 (0.275) 0.235 (2.0)    |

To wire the safe torque-off connector in single axis or multi-axis configurations, refer to the Kinetix Safe Torque-off Feature Safety Reference Manual, publication GMC-RM002 .

## Wire the Motor Power (MP) Connector

Connections to the motor power (MP) connector include rotary motors, linear motors, and motor driven actuators.

<!-- image -->

ATTENTION: Make sure the motor power connections are correct when wiring the MP connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause explosion or damage to equipment.

This example applies to AM modules and the inverter section of IAM modules.

<!-- image -->

## Cable Shield Terminations

Factory-supplied Kinetix 2090 motor power cables for motors and actuators are shielded, and the braided cable shield must terminate at the drive during installation. A small portion of the cable jacket must be removed to expose the shield braid. The exposed area must be clamped (with the clamp provided) on

Table 70 - Kinetix MPL Motor Catalog Numbers

| Motor Cat. No. /SpeedTec DIN Connectors Motor Cat. No. /Threaded DIN Connectors Motor Cat. No. /Bayonet Connectors   |                                            |                                                                                     |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------|-------------------------------------------------------------------------------------|
| MPL-A/B15xxx - xx7xAA MPL-A/B2xxx - xx7xAA                                                                           | MPL-A/B15xxx - xx4xAA MPL-A/B2xxx - xx4xAA | N/A                                                                                 |
| MPL-A/B3xxx - xx7xAA, MPL-A/B4xxx-xx7xAA, MPL-A/B45xxx - xx7xAA, MPL-A/B5xxx-xx7xAA                                  | N/A                                        | MPL-A/B3xxx - xx2xAA, MPL-A/B4xxx-xx2xAA, MPL-A/B45xxx - xx2xAA, MPL-A/B5xxx-xx2xAA |
| MPL-B6xxx - xx7xAA, MPL-B8xxx-xx7xAA, MPL-B9xxx - xx7xAA                                                             | N/A                                        | MPL-B6xxx - xx2xAA, MPL-B8xxx-xx2xAA, MPL-B9xxx - xx2xAA                            |

Bayonet connectors can be mounted facing the motor shaft or end plate and provide a separate connector for power, feedback, and brake connections. Circular DIN connectors rotate up to 180° and combine power and brake wires in the same connector, eliminating the brake connector.

## Figure 54 - Bayonet and Circular DIN Motor Connectors

Bayonet Connectors

Feedback/Power/Brake Connectors

<!-- image -->

<!-- image -->

Feedback/Power Connectors

## Threaded (M4) Connectors

Feedback Connector

<!-- image -->

<!-- image -->

SpeedTec (M7) Connectors

Power and Brake Connector

<!-- image -->

<!-- image -->

Power and Brake Connector

top of the IAM or AM modules and the power wires terminated in the motor power (MP) connector plug.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, make sure shielded power cables are grounded at a minimum of one point for safety.

## Kinetix MP Motor and Actuator Connectors

Kinetix MPL motors equipped with circular DIN connectors (specified by 4 or 7 in the catalog number) are not compatible with cables designed for motors equipped with bayonet connectors (specified by 2 in the catalog number). The motors with bayonet connectors are being discontinued.

<!-- image -->

<!-- image -->

<!-- image -->

Side View

Kinetix MPAR and MPAS linear actuators and Kinetix MPS) stainless-steel motors have also transitioned from threaded (M4) to SpeedTec (M7) connectors.

## Motor Power Wiring Examples

The procedure for wiring motor power varies slightly, depending on the motor family. The cables compatible with your motor or actuator depend on the connectors installed on the motor or actuator. Refer to Kinetix MP Motor and

Feedback Connector

Actuator Connectors on page 84 for more information on circular DIN and bayonet connectors.

Table 71 - Motor Power Cable Compatibility - Bayonet Connectors

| Motor/Actuator   | Connector Type   | Motor/Actuator Cat. No.                                                                                                                                                                               | Motor Power Cables (with brake wires)                                          | Motor Power Cables (without brake wires)   |
|------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------|
| Kinetix MPL      | Bayonet          | MPL-A/B3xxx - xx2xAA, MPL-A/B4xxx-xx2xAA, MPL-A/B45xxx - xx2xAA, MPL-A/B5xxx-xx2xAA, MPL-B6xxx - xx2xAA, MPL-B8xxx-xx2xAA, MPL-B960B-xx2xAA, MPL-B960C-xx2xAA, MPL-B980B-xx2xAA, and MPL-B980C-xx2xAA | N/A                                                                            | 2090-XXxPMP-xxSxx (1)                      |
| Kinetix MPL      | Bayonet          | MPL-B960D-xx2xAA, MPL-B980D-xx2xAA 2090-MCNPMP-6Sxx                                                                                                                                                   | N/A                                                                            |                                            |
|                  | Bayonet          | 1326AB (M2L/S2L) 1326AB-Bxxxx-M2L/S2L                                                                                                                                                                 | N/A                                                                            | 2090-XXxPMP-xxSxx (1)                      |
| F-Series F-xxxx  | Bayonet          |                                                                                                                                                                                                       | N/A                                                                            | 2090-XXNPHF-xxSxx                          |
|                  |                  |                                                                                                                                                                                                       | 1326AB (resolver) P-LOK 1326AB-Bxxxx-21 1326-CPx1T-L-xxx (continuous-flex) N/A |                                            |

Table 72 - Motor Power Cable Compatibility - Threaded DIN and Circular Plastic Connectors

| Motor/Actuator   | Connector Type          | Motor/Actuator Cat. No.                               | Motor Power Cables (with brake wires)      | Motor Power Cables (without brake wires)   |
|------------------|-------------------------|-------------------------------------------------------|--------------------------------------------|--------------------------------------------|
| Kinetix MPL      | Circular (threaded)DI N | MPL-A/B15xxx - xx4xAA, MPL-A/B2xxx-xx4xAA             | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous flex)                                            | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
|                  | Circular (threaded)DI N | Circular () Kinetix MPS MPS-A/Bxxxx                                                       | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous flex)                                            | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
|                  | Circular (threaded)DI N | () N Kinetix MPAS MPAS-A/Bxxxx                                                       | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous flex)                                            | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
|                  | Circular (threaded)DI N | Kinetix MPAR MPAR-A/B1xxx and MPAR-A/B2xxx (series A) | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous flex)                                            | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
| Kinetix TLY      | Circular Plastic        |                                                       | TLY-Axxxx-H 2090-CPBM6DF-16AAxx (standard) | 2090-CPWM6DF-16AAxx (standard)             |

Table 73 - Motor Power Cable Compatibility - SpeedTec DIN Connectors

| Motor/Actuator                                   | Connector Type          | Motor/Actuator Cat. No.                                                                                                                                                                 | Motor Power Cables (1) (with brake wires)         | Motor Power Cables (1) (without brake wires)                            |
|--------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------|
| Kinetix MPL                                      | Circular (SpeedTec) DIN | MPL-A/B15xxx - xx7xAA, MPL-A/B2xxx-xx7xAA, MPL-A/B3xxx - xx7xAA, MPL-A/B4xxx-xx7xAA, MPL-A/B45xxx - xx7xAA, MPL-A/B5xxx-xx7xAA, MPL-B6xxx - xx7xAA, MPL-B8xxx-xx7xAA MPL-B9xxx - xx7xAA | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                  | Circular (SpeedTec) DIN | Kinetix MPM MPM-A/Bxxxx                                                                                                                                                                 | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                  | Circular (SpeedTec) DIN | Kinetix MPF MPF-A/Bxxxx                                                                                                                                                                 | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                  | Circular (SpeedTec) DIN | Kinetix MPS MPS-A/Bxxxx                                                                                                                                                                 | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAS (ballscrew)                         | Circular (SpeedTec) DIN | MPAS-A/Bxxxx1-V05SxA MPAS-A/Bxxxx2-V20SxA                                                                                                                                               | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                  | Circular (SpeedTec) DIN | (p) DIN Kinetix MPAI MPAI-A/Bxxxx                                                                                                                                                                                         | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAR                                     | Circular (SpeedTec) DIN | MPAR-A/B3xxx, MPAR-A/B1xxx and MPAR-A/B2xxx (series B)                                                                                                                                  | 2090-CPBM7DF-xxAFxx (continuous-flex)             | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix RDB RDB-Bxxxx                            | Circular (SpeedTec) DIN |                                                                                                                                                                                         | N/A (these devices do not include a brake option) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix MPAS (direct drive) MPAS-A/Bxxxxx-ALMx2C | Circular (SpeedTec) DIN |                                                                                                                                                                                         | N/A (these devices do not include a brake option) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| Kinetix LDAT                                     | Circular (SpeedTec) DIN | LDAT-Sxxxxxx - xDx LDAT-Sxxxxxx - xBx                                                                                                                                                   | N/A (these devices do not include a brake option) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                  | Circular (SpeedTec) DIN | Kinetix LDC LDC-Cxxxxxx                                                                                                                                                                 | N/A (these devices do not include a brake option) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
|                                                  | Circular (SpeedTec) DIN | Kinetix LDL LDL-xxxxxxx                                                                                                                                                                 | N/A (these devices do not include a brake option) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |

These cables contain only the three-phase power wires. The motors/actuators either have no brake or a separate connector for brake connections. Thermal switch wires are included in the feedback cable.

Refer to Axis Module/Rotary Motor Wiring Examples on page 160 for interconnect diagrams.

Figure 55 - Motor Power Terminations (cables without brake wires)

<!-- image -->

The cable shield clamp shown above is mounted to an IAM module. Cables attach to the clamp on each AM module in the same way.

These cables contain three-phase power wires and brake wires. The brake wires have a shield braid (shown below as gray) that folds back under the cable clamp before the conductors are attached to the motor brake (BC) connector. Thermal switch wires are included in the feedback cable.

Refer to Axis Module/Rotary Motor Wiring Examples on page 160 for interconnect diagrams.

Figure 56 - Motor Power Terminations (cables with brake wires)

<!-- image -->

The cable shield clamp shown above is mounted to an IAM module. Cables attach to the clamp on each AM module in the same way.

The 1326AB (resolver) power cables (catalog number 1326-CPx1T-L-xxx) contain the three-phase wires, brake wires, and thermal switch wires. To improve the EMC performance of your system, route the wires as shown.

Refer to Axis Module/Rotary Motor Wiring Examples on page 160 for interconnect diagrams.

Low-profile motor feedback connector (2090-K6CK-D15MF) pins 16, 17, and S provide filtering for 1326-CPx1T-L-xxx cables (refer to page 99 for an illustration).

Figure 57 - Motor Power Terminations (1326-CPx1T-L-xxx cable)

<!-- image -->

The cable shield clamp shown above is mounted to an IAM module. Cables attach to the clamp on each AM module in the same way.

## IMPORTANT

We recommend securing the cable shield in the clamp with a tie wrap to improve stress relief.

Cable shield and lead preparation is provided with most Allen-Bradley® cable assemblies. Follow these guidelines if your motor power cable shield and wires require preparation.

Figure 58 - Cable Shield and Lead Preparation

<!-- image -->

Refer to Axis Module/Rotary Motor Wiring Examples on page 160 for interconnect diagrams.

Table 74 - Motor Power (MP) Connector

| Servo Motor MP Connector (IAM/AM module)         |
|--------------------------------------------------|
| 1326AB (resolver) All Other Motors MP Pin Signal |
| 1 / Black U / Brown 1 U                          |
| 2 / Black V / Black 2 V                          |
| 3 / Black W / Blue 3 W                           |
| Green/Yellow  Green/Yellow  4                    |

Table 75 - Termination Specifications

| IAM/AM Module Cat. No.                                                                                                                                | Recommended Wire Size mm 2 (AWG)                                  | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------|----------------------------|
| 2094-AC05-Mxx - x, 2094-AMP5-x, 2094-AM01-x , 2094-AC09-M02-x, 2094-AM02-x , 2094-BC01-Mxx - x, 2094-BMP5-x, 2094-BM01-x 2094-BC02-M02-x, 2094-BM02-x | Motor power cable depends on motor/ drive combination. 6 (10) max | 10 (0.38)               | 0.5…0.6 (4.4…5.3)          |
| 2094-AC16-M03-x, 2094-AM03-x 2094-AC32-M05-x, 2094-AM05-x                                                                                             | 10 (8) max 10 (0.38)                                              |                         | 1.2…1.5 (10.6…13.2)        |
| 2094-BC04-M03-x, 2094-BM03-x                                                                                                                          | 10 (8) max 10 (0.38)                                              |                         | 1.2…1.5 (10.6…13.2)        |
| 2094-BC07-M05-x, 2094-BM05-x                                                                                                                          | 30 (3) max 16 (0.63)                                              |                         | 2.4…3.0 (21.6…26.5)        |

## Wire the Motor/Resistive Brake (BC) Connector

This example applies to AM modules and the inverter section of IAM modules.

Figure 59 - IAM/AM Module (BC connector)

<!-- image -->

24V DC Brake Input Power Connections

| IMPORTANT   | If your system includes a LIM module, you can source the 24V DC from the LIM module (P1L or PSL connector).   |
|-------------|---------------------------------------------------------------------------------------------------------------|

Table 76 - Motor/Resistive Brake (BC) Connector

| 2094-ALxxS, 2094-BLxxS, or 2094-XL75S-Cx LIM Module   | 2094-AL09 and 2094-BL02 LIM Module          | BC Connector (IAM/AM modules)   | BC Connector (IAM/AM modules)   |
|-------------------------------------------------------|---------------------------------------------|---------------------------------|---------------------------------|
|                                                       | P1L Pin Signal PSL Pin Signal BC Pin Signal |                                 |                                 |
|                                                       |                                             |                                 | 1 IO_PWR2 1 MBRK PWR 3 PWR      |
|                                                       |                                             |                                 | 2 IO_COM2 2 MBRK COM 4 COM      |

## RBM Module Connections

Table 77 - Motor/Resistive Brake (BC) Connector

| RBM Module I/O Connections   | BC Connector (IAM/AM modules)   | BC Connector (IAM/AM modules)   |
|------------------------------|---------------------------------|---------------------------------|
|                              | TB3 Pin Signal MP Pin           | Signal (1)                      |
|                              |                                 | 6 COIL_A1 1 DBRK+               |
|                              |                                 | 7 COIL_A2 2 DBRK                                 |

## Motor Brake Connections

The procedure for wiring your motor brake varies slightly, depending on the motor family. The cables compatible with your motor or actuator depend on the connectors installed on the motor or actuator. Refer to Kinetix MP Motor and Actuator Connectors on page 84 for more information on circular DIN and bayonet connectors.

Table 78 - Motor Brake Cable Compatibility - Bayonet Connectors

| Motor Series                                                                                                                                | Connector Type   |                                                                               | Brake Wires Cable Cat. No.             |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------|----------------------------------------|
| MPL-A/B3xxx - xx2xAA, MPL-A/B4xxx-xx2xAA, MPL-A/B45xxx - xx2xAA, MPL-A/B5xxx-xx2xAA, MPL-B6xxx - xx2xAA, MPL-B8xxx-xx2xAA, MPL-B9xxx-xx2xAA | Bayonet          | The motor has a brake connector. Brake wires are in the brake cable.          | 2090-UXxBMP-18Sxx brake cable (1)      |
|                                                                                                                                             | Bayonet          | F-Series The motor has a brake connector. Brake wires are in the brake cable. | Straight brake connector kit 9101-0330 |
|                                                                                                                                             | Bayonet          | F-Series The motor has a brake connector. Brake wires are in the brake cable. | connector. Brake wires are in the brake cable. 1326AB (resolver) P-LOK 1326-CPx1T-L-xxx power cable                                        |

Table 79 - Motor Brake Cable Compatibility - Threaded DIN and Circular Plastic Connectors

| Motor Series                                                                                                             | Connector Type               |                                                                                                  | Brake Wires Cable Cat. No.                                            |
|--------------------------------------------------------------------------------------------------------------------------|------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| MPL-A/B15xxx - xx4xAA, MPL-A/B2xxx-xx4xAA MPS-A/Bxxx, x, MPAS-A/Bxxx, MPMA-A/Bxxx, MPAR-A/B1xxx, MPAR-A/B2xxx (series A) | Circular (threaded) DIN      | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex) |
|                                                                                                                          | TLY-Axxxx-H Circular Plastic | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-CPBM6DF-16AAxx power cable                                       |

Table 80 - Motor Brake Cable Compatibility - SpeedTec DIN Connectors

| Motor Series                                                                                                                                 | Connector Type          | Brake Wires                                                                                      | Cable Cat. No. (1)                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| MPL-A/B15xxx - xx7xAA, MPL-A/B2xxx-xx7xAA                                                                                                    | Circular (SpeedTec) DIN | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) |
| MPL-A/B3xxx - xx7xAA, MPL-A/B4xxx-xx7xAA, MPL-A/B45xxx - xx7xAA, MPL-A/B5xxx-xx7xAA, MPL-B6xxx - xx7xAA, MPL-B8xxx-xx7xAA MPL-B9xxx - xx7xAA | Circular (SpeedTec) DIN | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) |
| MPAS-A/Bxxx , MPAR-A/B1xxx, MPAR-A/B2xxx (series B), MPAR-A/B3xxx, MPAI-A/Bxxx                                                               | Circular (SpeedTec) DIN | The motor/actuator does not have a brake connector. Brake wires are included in the power cable. | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) |

IMPORTANT Use surge suppression when controlling a brake coil. Refer to Brake Current Example on page 176 .

Table 81 - Motor/Resistive Brake (BC) Connector

| Motor Brake Wires              |                                                   |                                 |                               | BC Connector (IAM/AM module)   | BC Connector (IAM/AM module)   |
|--------------------------------|---------------------------------------------------|---------------------------------|-------------------------------|--------------------------------|--------------------------------|
| 2090-UXxBMP-18Sxx  Brake Cable | 2090-XXNPMF-xxSxx 2090-CPBMxDF-xxAFxx Power Cable | 2090-CPBM6DF-16AAxx Power Cable | 1326-CPx1T-L-xxx  Power Cable |                                | BC Pin Signal                  |
|                                | A / BR+ F/+ / BR+/MBRK+ 7 / MBRK+ 6 / B1 5 MBRK+  |                                 |                               |                                |                                |
|                                | C / BR- G/- / BR-/MBRK- 9 / MBRK- 4 / B2 6 MBRK                                                   |                                 |                               |                                |                                |

Table 82 - Termination Specifications

| BC Connector (IAM/AM module) Recommended   | BC Connector (IAM/AM module) Recommended   | Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value        |
|--------------------------------------------|--------------------------------------------|------------------------|-------------------------|---------------------|
|                                            | BC Pin Signal                              |                        |                         | N•m (lb•in)         |
| BC-6 BC-5 BC-4 BC-3 BC-2 BC-1              | MBRK MBRK+ COM PWR DBRK DBRK+                                            |                        | 0.75 (18) 10 (0.38)     | 0.22…0.25 (1.9…2.2) |

This procedure assumes you have completed wiring your motor power (MP) connector and are ready to apply the cable shield clamp.

<!-- image -->

Your drive can be equipped with either the pivot-open or slide-open cable clamp.

Follow these steps to apply the motor cable shield clamp.

1. Depress the spring loaded clamp.

The pivot-open cable clamp was designed to replace the slide-open cable clamp. Pivot-open clamp features include:

- Screwdriver not required for depressing the spring
- Tie wrap not required or recommended
2. Position the exposed portion of the cable braid directly in line with the clamp.
3. Release the spring, making sure the cable and cable braid are held secure by the clamp.

<!-- image -->

## Apply the Motor Cable Shield Clamp

<!-- image -->

4. Attach tie wrap (slide-open clamp only) around cable and clamp for additional strain relief.
5. Repeat step 1 through step 4 for each IAM, AM, or IPIM module.

<!-- image -->

## Feedback and I/O Cable Connections

Factory made cables with premolded connectors are designed to minimize EMI and are recommended over hand-built cables to improve system performance. However, other options are available for building your own feedback and I/O cables.

Table 83 - Options for Connecting Motor Feedback and I/O

|                                              |                                   | Connection Option Connector Kit Cat. No. Cable Using this Type of Cable                          |
|----------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------|
| Premolded connector N/A Motor feedback       |                                   | Refer to Table 84 and Table 85 for the flying-lead cable available for your motor.               |
| Low-profile connector kit                    | 2090-K6CK-D15M Motor feedback     | Refer to Table 84 and Table 85 for the flying-lead cable available for your motor.               |
| Low-profile connector kit                    |                                   | 2090-K6CK-D26M I/O interface User-supplied flying-lead cable.                                    |
| Low-profile connector kit                    | 2090-K6CK-D15F Auxiliary feedback | User-supplied flying-lead cable.                                                                 |
| Low-profile connector kit                    | 2090-K6CK-D15MF                   | 1326-CCUT-L-xxx flying-lead feedback cable.                                                      |
| Low-profile feedback module 2090-K6CK-KENDAT |                                   | Motor feedback Refer to Table 84 … Table 86 for the flying-lead cable available for your motor.  |
| Panel-mounted breakout board kit             | 2090-UXBK-D15xx (1)               | Motor feedback  Refer to Table 84 … Table 86 for the flying-lead cable available for your motor. |

The procedure for wiring your motor feedback varies slightly, depending on the motor family. The cables compatible with your motor or actuator depend on the connectors installed on the motor or actuator. Refer to Kinetix MP Motor and Actuator Connectors on page 84 for more information on circular DIN and bayonet connectors.

Table 84 - Motor Feedback Cable Compatibility - Bayonet Connectors

| Motor/Actuator                                      | Connector Type   | Feedback Type                                                 | Feedback Cable                                     |
|-----------------------------------------------------|------------------|---------------------------------------------------------------|----------------------------------------------------|
| Motor/Actuator                                      |                  |                                                               | Premolded Flying-lead                              |
| MPL-A/Bxxxx-S/Mx2xAA                                | Bayonet          | High-resolution encoder                                       |                                                    |
| 2090-UXNFBMP-Sxx 2090-XXxFMP-Sxx MPL-A3xxx-Hx2xAA  MPLA4H2AAItl d MPL-A4xxx-Hx2xAA MPL-A45xxx-Hx2xAA                                                     | Bayonet          | Incremental encoder                                           | 2090-UXNFBMP-Sxx  (1)                              |
| MPL-B3xxx-Rx2xAA MPL-B4xxx-Rx2xAA MPL-B45xxx-Rx2xAA | Bayonet          |                                                               | Motor resolver N/A 2090-CDNFDMP-Sxx                |
|                                                     | Bayonet          | 1326AB-Bxxxx-M2L/S2L High-resolution encoder 2090-UXNFBMP-Sxx | 2090-XXxFMP-Sxx (1)                                |
|                                                     | Bayonet          |                                                               | 1326AB-Bxxxx-21 Motor resolver N/A 1326-CCUT-L-xxx |
|                                                     | Bayonet          | F-Series Incremental encoder 2090-UXNFBHF-Sxx                 | 2090-XXNFHF-Sxx                                    |

Refer to Flying-lead Feedback Cable Pinouts beginning on page 93 for the motor-to-drive feedback cable pinout used in your application.

Refer to Kinetix MP Motor and Actuator Connectors on page 84 for more information on circular DIN and bayonet connectors.

Table 85 - Motor Feedback Cable Compatibility - Threaded DIN/Plastic Connectors

|                                                | Motor/Actuator Connector Type Feedback Type   |                         | Feedback Cable (1)                                                   | Feedback Cable (1)                                                  |
|------------------------------------------------|-----------------------------------------------|-------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------|
|                                                |                                               |                         |                                                                      | Premolded Flying-lead                                               |
| MPL-A/B15xxx-V/Ex4xAA MPL-A/B2xxx-V/Ex4xAA     | Circular (threaded) DIN                       | High-resolution encoder | N/A                                                                  | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPL-A/B15xxx-Hx4xAA MPL-A/B2xxx-Hx4xAA         | Circular (threaded) DIN                       | Incremental encoder     | N/A                                                                  | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPS-A/Bxxxx-S/M                                | Circular (threaded) DIN                       |                         | N/A                                                                  | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPAS-A/Bxxxxx-V/A                              | Circular (threaded) DIN                       | High-resolution encoder | N/A                                                                  | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
| MPAR-A/B1xxxx-V and MPAR-A/B2xxxx-V (series A) | Circular (threaded) DIN                       | High-resolution encoder | N/A                                                                  | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex) |
|                                                |                                               |                         | TLY-Axxxx-H Circular Plastic Incremental encoder 2090-CFBM6DD-CCAAxx | 2090-CFBM6DF-CBAAxx                                                 |

Table 86 - Motor Feedback Cable Compatibility - SpeedTec DIN Connectors

| Motor/Actuator Connector Type Feedback Type                                                                                                        |                         |                         | Feedback Cable (1)                                                      | Feedback Cable (1)                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|                                                                                                                                                    |                         |                         |                                                                         | Premolded Flying-lead                                                           |
| MPL-A/B15xxx-V/Ex7xAA MPL-A/B2xxx-V/Ex7xAA                                                                                                         | Circular (SpeedTec) DIN | High-resolution encoder | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex)         |
| MPL-A/B15xxx-Hx7xAA MPL-A/B2xxx-Hx7xAA                                                                                                             | Circular (SpeedTec) DIN | Incremental encoder     | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex)         |
| MPL-A/B3xxx-S/Mx7xAA, MPL-A/B4xxx-S/Mx7xAA, MPL-A/B45xxx-S/Mx7xAA, MPL-A/B5xxx-S/Mx7xAA, MPL-B6xxx-S/Mx7xAA, MPL-B8xxx-S/Mx7xAA MPL-B9xxx-S/Mx7xAA | Circular (SpeedTec) DIN | High-resolution encoder | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex)         |
| MPL-A/B3xxx-Hx7xAA (2) MPL-A/B4xxx-Hx7xAA (2) MPL-A/B45xxx-Hx7xAA (2) LDAT-Sxxxxxx - xBx (2)                                                       | Circular (SpeedTec) DIN | Incremental encoder N/A |                                                                         | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)             |
| MPL-B3xxx-Rx7xAA MPL-B4xxx-Rx7xAA MPL-B45xxx-Rx7xAA                                                                                                | Circular (SpeedTec) DIN | Motor resolver N/A      |                                                                         | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) xxxxx-2 |
| MPM-A/B                                                                                                                                            | Circular (SpeedTec) DIN | Motor resolver N/A      |                                                                         | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) xxxxx-2 |

Table 86 - Motor Feedback Cable Compatibility - SpeedTec DIN Connectors (Continued)

|                                                                                 | Motor/Actuator Connector Type Feedback Type   |                                | Feedback Cable (1)                                                      | Feedback Cable (1)                                                      |
|---------------------------------------------------------------------------------|-----------------------------------------------|--------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
|                                                                                 | Motor/Actuator Connector Type Feedback Type   |                                |                                                                         | Premolded Flying-lead                                                   |
| MPF-A/Bxxxx-S/M                                                                 | Circular (SpeedTec) DIN                       | High-resolution encoder        | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPS-A/Bxxxx-S/M                                                                 | Circular (SpeedTec) DIN                       | High-resolution encoder        | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPM-A/Bxxxxx-S/M                                                                | Circular (SpeedTec) DIN                       | High-resolution encoder        | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAS-A/Bxxxxx-V  MPAR-A/B1xxxx-V and MPAR-A/B2xxxx-V (series B) MPAR-A/B3xxxx-M | Circular (SpeedTec) DIN                       | High-resolution encoder        | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/BxxxxxM3                                                                 | Circular (SpeedTec) DIN                       | High-resolution encoder        | 2090-CFBM7DD-CEAAxx (standard) or 2090-CFBM7DD-CEAFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| RDB-Bxxxx-7/3                                                                   | Circular (SpeedTec) DIN                       | High-resolution encoder        | N/A                                                                     | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |
| MPAS-A/Bxxxxx-A                                                                 | Circular (SpeedTec) DIN                       | Incremental encoder            | N/A                                                                     | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |
| LDC-Cxxxx or LDL-xxxxx (2)                                                      | Circular (SpeedTec) DIN                       | Sin/Cos encoder or TTL encoder | N/A                                                                     | 2090-XXNFMF-Sxx (standard) or 2090-CFBM7DF-CDAFxx (continuous-flex)     |

## Flying-lead Feedback Cable Pinouts

Refer to the following tables for the motor-to-drive feedback cable pinout used in your application.

Table 87 - 2090-XXxFMP-Sxx Feedback Cable (1)

| High-resolution Feedback Incremental Feedback                                                                                               | High-resolution Feedback Incremental Feedback                     |
|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Connector Pin MPL-B3xxx…MPL-B9xxx-M/Sx2xAA MPL-A5xxx-M/Sx2xAA 1326AB-Bxxx-M2L/S2L MPL-A3xxx-M/Sx2xAA MPL-A4xxx-M/Sx2xAA MPL-A45xxx-M/Sx2xAA | Rotary Motors MPL-A3xxx-Hx2xAA MPL-A4xxx-Hx2xAA MPL-A45xxx-Hx2xAA |
|                                                                                                                                             | A Sin+ Sin+ AM+ 1                                                 |
|                                                                                                                                             | B Sin- Sin- AM- 2                                                 |
| C Cos+ Cos+ BM+ 3                                                                                                                           |                                                                   |
| D Cos- Cos- BM- 4                                                                                                                           |                                                                   |
| E Data+ Data+ IM+ 5                                                                                                                         |                                                                   |
| F Data- Data- IM- 10                                                                                                                        |                                                                   |
| K Reserved EPWR_5V EPWR_5V 14                                                                                                               |                                                                   |
| L Reserved ECOM ECOM 6                                                                                                                      |                                                                   |
| N EPWR_9V Reserved Reserved 7                                                                                                               |                                                                   |
|                                                                                                                                             | P ECOM Reserved Reserved 6                                        |
|                                                                                                                                             | R TS+ TS+ TS+ 11                                                  |
| S TS- TS- TS- –                                                                                                                             |                                                                   |
| T Reserved Reserved S1 12                                                                                                                   |                                                                   |
| U Reserved Reserved S2 13                                                                                                                   |                                                                   |
| V Reserved Reserved S3 8                                                                                                                    |                                                                   |

Table 88 - 2090-CFBM7DF-CEAAxx Feedback Cable Table 89 - 2090-CDNFDMP-Sxx Feedback Cable

1 S2 1 A S2 1

2 S4 2 B S4 2

3 S1 3 C S1 3

4 S3 4 D S3 4

5 R1 5 G R1 5

6 R2 10 H R2 10

11 EPWR\_9V 7 N EPWR\_9V 7

12 ECOM 6 P ECOM 6

13 TS+ 11 R TS+ 11

14 TS- 6 S TS- 6

| Motor DIN Connector Pin   | Resolver Feedback MPL-Bxxxx-Rx7xAA MPM-xxxxxx-2   | Drive MF Connector Pin   |
|---------------------------|---|--------------------------|

Table 90 - 2090-XXNFMF-Sxx or 2090-CFBMxDF-xxAxxx Feedback Cables

| High-resolution Feedback Incremental Feedback                                                                                                                                | High-resolution Feedback Incremental Feedback                                                                                                                                                          |                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Drive MF Connector Pin MPL-B15xxx…MPL-B2xxx-V/Ex4/7xAA MPF/MPS-Bxxx-M/S MPF-A5xxx-M/S MPL-B3xxx…MPL-B9xxx-M/Sx7xAA MPL-A5xxx-M/Sx7xAA MPM-A165xxx…MPM-A215xxx MPM-Bxxxxx-M/S | MPL-A15xxx…MPL-A2xxx-V/Ex4/7xAA MPF/MPS-A3xx-M/S MPF/MPS-A4xx-M/S MPF/MPS-A45xx-M/S MPS-A5xxx-M/S RDB-Bxxxxx-3/7 MPL-A3xxx-M/Sx7xAA MPL-A4xxx-M/Sx7xAA MPL-A45xxx-M/Sx7xAA MPM-A115xxx…MPM-A130xxx-M/S | Rotary Motors MPL-A15xxx-Hx4/7xAA MPL-A2xxx-Hx4/7xAA MPL-B15xxx-Hx4/7xAA MPL-B2xxx-Hx4/7xAA MPL-A3xxx-Hx7xAA MPL-A4xxx-Hx7xAA MPL-A45xxx-Hx7xAA |
|                                                                                                                                                                              | Linear Motors N/A LDC-Cxxxx and LDL-xxxx                                                                                                                                                               | LDC-Cxxxx and LDL-xxxx                                                                                                                          |
| Linear Actuators  MPAS-Bxxxxx-VxxSxA MPAR-Bxxxx, MPAI-Bxxxx                                                                                                                  | MPAS-Axxxxx-VxxSxA MPAR-Axxxx, MPAI-Axxxx                                                                                                                                                              | MPAS-A/Bxxxxx-ALMx2C LDAT-Sxxxxxx-xBx                                                                                                           |
| 1 Sin+ Sin+ AM+ 1                                                                                                                                                            |                                                                                                                                                                                                        |                                                                                                                                                 |
|                                                                                                                                                                              | 2 Sin- Sin- AM- 2                                                                                                                                                                                      |                                                                                                                                                 |
|                                                                                                                                                                              | 3 Cos+ Cos+ BM+ 3                                                                                                                                                                                      |                                                                                                                                                 |
|                                                                                                                                                                              | 4 Cos- Cos- BM- 4                                                                                                                                                                                      |                                                                                                                                                 |
| 5 Data+ Data+ IM+ 5                                                                                                                                                          |                                                                                                                                                                                                        |                                                                                                                                                 |
| 6 Data- Data- IM- 10                                                                                                                                                         |                                                                                                                                                                                                        |                                                                                                                                                 |
| 7 Reserved                                                                                                                                                                   | CLK+ (1)                                                                                                                                                                                               | Reserved 9                                                                                                                                      |
| 8 Reserved                                                                                                                                                                   | CLK- (1)                                                                                                                                                                                               | Reserved 15                                                                                                                                     |
|                                                                                                                                                                              | 9 Reserved EPWR_5V EPWR_5V 14                                                                                                                                                                          |                                                                                                                                                 |
| 10 Reserved ECOM ECOM 6                                                                                                                                                      |                                                                                                                                                                                                        |                                                                                                                                                 |
| 11 EPWR_9V Reserved Reserved 7                                                                                                                                               |                                                                                                                                                                                                        |                                                                                                                                                 |
|                                                                                                                                                                              |                                                                                                                                                                                                        | 12 ECOM Reserved Reserved 6                                                                                                                     |
|                                                                                                                                                                              |                                                                                                                                                                                                        | 13 TS+ TS+ TS+ 11                                                                                                                               |
|                                                                                                                                                                              | 14 TS- TS- TS- –                                                                                                                                                                                       |                                                                                                                                                 |
| 15 Reserved Reserved S1 12                                                                                                                                                   |                                                                                                                                                                                                        |                                                                                                                                                 |
| 16 Reserved Reserved S2 13                                                                                                                                                   |                                                                                                                                                                                                        |                                                                                                                                                 |
|                                                                                                                                                                              | 17 Reserved Reserved S3 8                                                                                                                                                                              |                                                                                                                                                 |

| Motor Bayonet Connector Pin   | ResolverFeedback MPL-Bxxxx-Rx2xAA   | Drive MF Connector Pin   |
|-------------------------------|-------------------------------------|--------------------------|

Table 91 - 2090-CFBM6DF-CBAAxx Feedback Cable

Connector PinConnector Pin
A Connector Pin xxxx-H TLY-Axxxx-H

9 AM+ 1 15 S1 12

10 AM- 2 17 S2 13

11 BM+ 3 19 S3 8

12 BM- 4 22 EPWR\_5V 14

13 IM+ 5 23 ECOM 6

14 IM- 10 24 Shield Connector housing

Table 92 - 2090-XXNFHF-Sxx Feedback Cable

| Rotary Motor Connector Pin   | Incremental Feedback  TLY-A x   | Drive MF Connector Pin   |
|------------------------------|---------------------------------|--------------------------|

| Rotary Motor Connector Pin   | Incremental Feedback   | Drive MF   |
|------------------------------|------------------------|------------|

Table 93 - 1326-CCUT-L-xxx Feedback Cable Table 94 - 1326-CPx1T-L-xxx Power Cable

| Rotary Motor Incremental Feedback  Drive MF   |
|-----------------------------------------------|
| Connector Pin Connector Pin F-Series Motors   |
| A AM+ 1                                       |
| B AM- 2                                       |
| C BM+ 3                                       |
| D BM- 4                                       |
| E IM+ 5                                       |
| F IM- 10                                      |
| G Reserved –                                  |
| H Reserved –                                  |
| J EPWR_5VM 14                                 |
| K EPWR_5VM 14                                 |
| L ECOMM 6                                     |
| M ECOMM 6                                     |
| N S2 13                                       |
| P S3 8                                        |
| R TS+ 11                                      |
| S TS- 6                                       |
| T S1 12                                       |

A R1 5 5 TS+ 16

B R2 10 9 TS- 17

C – – – Shield S

| Rotary Motor Connector Pin Resolver Feedback 1326AB-Bxxxx-21 Drive MF Connector Pin (1)        |
|--------|
| D S1 3 |
| E S3 4 |
| F– –   |
| G S2 1 |
| H S4 2 |

| Rotary Motor Connector Pin   | Thermal Switch Connections 1326AB-Bxxxx-21   | Drive MF Connector Pin (2)   |
|------------------------------|----------------------------------------------|------------------------------|

## Wiring the Feedback and I/O Connectors

These procedures assume you have mounted your Kinetix 6000 system, completed all power wiring, and are ready to connect your feedback and I/O cables.

| For This Connection Go to                                                           |
|-------------------------------------------------------------------------------------|
| Premolded cable Connect Premolded Motor Feedback Cables on page 96 .                |
| Panel-mounted breakout board Connect Panel-mounted Breakout Board Kits on page 96 . |
| Low-profile connector Wire Low-profile Connector Kits on page 97 .                  |

Kinetix 6000, Front View (IAM module is shown)

## Connect Premolded Motor Feedback Cables

Motor feedback cables with premolded connectors plug directly into 15-pin motor feedback (MF) connectors on either the IAM or AM modules (no wiring is necessary).

## IMPORTANT

When using Kinetix 2090 cables with premolded connectors, tighten the mounting screws (finger tight) to improve system performance.

<!-- image -->

## Connect Panel-mounted Breakout Board Kits

The 2090-UXBK-D15xx panel-mounted breakout board kit includes a DIN-rail breakout board and cable. The cable connects between the breakout board and the motor feedback (MF) connector. Wires from your flying-lead motor feedback cable connect to the terminals.

Figure 62 - IAM/AM Module (MF connector)

<!-- image -->

IMPORTANT

The panel-mounted breakout board kit (2090-UXBK-D15xx) is not compatible with 1326-CCUT-L-xxx cable.

Table 95 - Low-profile Connector Kits

| Connector Kit Cat. No.   | Description                                                                                                                                                                                           | Cable Compatibility                                                    |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| 2090-K6CK-KENDAT         | Low-profile feedback module for EnDat to Hiperface conversion (15-pin, male, D-sub). Use with any Kinetix 6000 IAM/ AM module and Kinetix RDB direct-drive motor with EnDat high-resolution feedback. | 2090-XXNFMF-Sxx, 2090-CFBM7DF-CDAFxx                                   |
| 2090-K6CK-D15M           | Low-profile connector kit for motor feedback (15-pin, male, D-sub). Use with any Kinetix 6000 IAM/AM module and compatible motors with incremental or high-resolution feedback.                       | 2090-XXxFMP-Sxx, 2090-XXNFMF-Sxx, 2090-XXNFHF-Sxx, 2090-CFBMxDF-CxAxxx |
| 2090-K6CK-D15M           | Low-profile connector kit for motor feedback (15-pin, male, D-sub). Use with Kinetix 6000 IAM/AM module and MPL-Bxxxx-R (resolver feedback) motors.                                                   | 2090-CDNFDMP-Sxx 2090-CFBM7DF-CEAAxx 2090-CFBM7DF-CEAFxx               |
| 2090-K6CK-D15MF          | Low-profile connector kit for motor feedback (15-pin, male, D-sub) with filter. Use with Kinetix 6000 IAM/AM module and 1326ABxxxx-21 (resolver feedback) motors.                                     | 1326-CCUT-L-xxx                                                        |
| 2090-K6CK-D15F           | Low-profile connector kit for auxiliary feedback (15-pin, female, D-sub). Use with any Kinetix 6000 IAM/AM module for auxiliary feedback applications.                                                | Customer Supplied                                                      |
| 2090-K6CK-D26M           | Low-profile connector kit for I/O (26-pin, male, D-sub). Use with any Kinetix 6000 IAM/AM module or 2094-AL09 and 2094-BL02 LIM module for making I/O connections.                                    | Customer supplied                                                      |

Figure 63 - IAM/AM Module (IOD/MF/AF connectors)

<!-- image -->

## Wire Low-profile Connector Kits

The 2090-K6CK-xxxx low-profile connector kits are suitable for terminating flying-lead motor feedback, auxiliary feedback, and I/O connections. They also apply to I/O connections on the 2094-AL09 and 2094-BL02 LIM modules.

## Figure 64 - Wiring (15-pin) Flying-lead Feedback Cable Connections 2090-K6CK-D15M and 2090-K6CK-D15F Connector Kit

<!-- image -->

## Figure 65 - Wiring (15-pin) Flying-lead Feedback Cable Connections 2090-K6CK-KENDAT Feedback Module

<!-- image -->

<!-- image -->

## IMPORTANT

The purpose of the cable shield clamp is to provide a proper ground and improve system performance, not stress relief.

Clamping the exposed braid under the shield clamp is critical. Turn clamp over, if necessary, to be sure of a proper ground.

## Figure 67 - Wiring (26-pin) Flying-lead I/O Cable Connections 2090-K6CK-D26M Connector Kit

<!-- image -->

Follow these guidelines when wiring your external active or passive shunt module.

## External Shunt Module Connections

Table 96 - Shunt Module Wiring

| Use This Shunt Module                                                   | Cat. No.      | With This Drive Module   | Do This                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------|---------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power rail mounted shunt module.                                        | 2094-BSP2 N/A |                          | • Verify the internal shunt jumper is in place between RC-2 and RC-3 (refer to Figure 68). • Verify the thermal switch jumper is in place between TS-1 and TS-2 (refer to Figure 68).                                                                                                                                                                                                                                                        |
| External passive shunt module connected to the power rail shunt module. | 1394-SRxxxx   | 2094-BSP2 Shunt module   | • Remove the internal shunt jumper between RC-2 and RC-3. • Remove the thermal switch jumper between TS-1 and TS-2 (if your shunt module includes a thermal switch). • Refer to External Shunt Module Outside the Enclosure on page 40 for noise zone considerations. • Refer to Shunt Module Wiring Examples on page 159 . • Refer to the installation instructions provided with your Bulletin 1394 shunt module, publication 2090-IN004 . |

Figure 68 - Shunt Module Jumper Settings

<!-- image -->

An overview of the Kinetix 6000M integrated drive-motor (IDM) system connections are shown here.

- Refer to Chapter 2 on page 21, for noise zone considerations.
- Refer to Appendix A, on page 151, for an interconnect diagram featuring the Kinetix 6000M integrated drive-motor (IDM) system.
- Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for more information when wiring your IPIM module.

## IMPORTANT

To improve system performance, run wires and cables in the wireways as established in Chapter . 2

## IPIM Module Connections

| IMPORTANT   | When tightening screws to secure the wires, refer to the tables beginning on page 77 for torque values.   |
|-------------|-----------------------------------------------------------------------------------------------------------|
| IMPORTANT   | To improve system performance, run wires and cables in the wireways as established in Chapter  . 2        |

## Figure 69 - IPIM Module Connections

<!-- image -->

## RBM Module Connections

Follow these guidelines when wiring your Kinetix 2090 Resistive Brake Module (RBM).

## IMPORTANT

To be sure of system performance, run wires and cables in the wireways as established in Chapter . 2

If your application requires an RBM module and you are wiring to a Kinetix 6000 IAM/AM module, then refer to the following:

- Cable Categories for Kinetix 6000 Systems on page 38 to establish noise zones when mounting the RBM module on your panel.
- Resistive brake module to Kinetix 6000 drive interface cable (catalog number 2090-XXNRB-xxF0Px).
- The example diagram below and others in Appendix C, beginning on page 189 .
- The installation instructions provided with your RBM module, publication 2090-IN009 .

Figure 70 - RBM Module Connections

<!-- image -->

## Sercos Fiber-optic Cable Connections

This procedure assumes you have your Logix 5000™ Sercos interface module/ PCI card and Kinetix 6000 IAM/AM modules mounted and are ready to connect the fiber-optic cables.

The Sercos fiber-optic ring is connected by using the Sercos receive (Rx) and transmit (Tx) connectors. Refer to Figure 23 on page 47 to locate the Sercos connectors on your Kinetix 6000 IAM/AM module and IPIM module. Refer to the figure below to locate the connectors on your Logix 5000 Sercos interface module or PCI card.

Plastic cable is available in lengths up to 32 m (105.0 ft). Glass cable is available in lengths between 50 m (164.2 ft) and 200 m (656.7 ft).

Figure 71 - CompactLogix, ControlLogix, and SoftLogix Sercos Connectors

<!-- image -->

Connect the cable from transmit on the Logix 5000 module to receive on the IAM/AM or IPIM module, then transmit to receive (drive to drive), and from transmit on the last drive back to receive on the Logix 5000 module.

<!-- image -->

ATTENTION: To avoid damage to the Sercos Rx and Tx connectors, use only finger-tight torque when attaching the fiber-optic cables to the Kinetix 6000 IAM/AM modules and IPIM module. Do not use a wrench or any other mechanical assistance.

For more information, refer to Fiber-optic Cable Installation and Handling Instructions, publication 2090-IN010 .

SoftLogix and ControlLogix controllers are used in the following examples; however, CompactLogix controllers connect in the same manner.

Figure 72 - Fiber-optic Cable Example - SoftLogix Controller

<!-- image -->

In this example, two Logix 5000 modules are installed in separate chassis.

Figure 73 - Fiber-optic Cable Example - Two Logix 5000 Controllers

<!-- image -->

## IMPORTANT

Clean the fiber-optic cable connectors prior to installation. Dust in the connectors can reduce signal strength. For more information, refer to Fiber-optic Cable Installation and Handling Instructions, publication 2090-IN010 .

When connecting 2094-BM03-x and 2094-BM05-x (double-wide) axis modules, use 2090-SCEP0-2, 0.2 m (7.0 in.) cables. When connecting 2094-AMxx-x ,

2094-BMP5-x, 2094-BM01-x, and 2094-BM02-x (single-wide) axis modules, use 2090-SCEP0-1, 0.1 m (5.1 in.) cables.

Figure 74 - Fiber-optic Cable Example - Logix 5000 Controller with Double-wide Drive Modules

<!-- image -->

In this example, the second Kinetix 6000 system is mounted in a separate cabinet and connected with bulkhead adapters.

## IMPORTANT

To avoid signal loss, do not use bulkhead adapters to connect glass cables. Use only bulkhead adapters for making plastic-to-plastic cable connections.

## Figure 75 - Fiber-optic Cable Example - Logix 5000 Controller with Bulkhead Adapters

<!-- image -->

## Kinetix 6000M Integrated Drive-Motor Sercos Connections

The Kinetix 6000 Sercos ring includes the Kinetix 6000M integrated drivemotor (IDM) units and IDM power interface modules (IPIM). Fiber-optic connections are made from drive-to-drive and drive-to-IPIM module. IDM network connections continue from the IPIM module to the IDM units.

Because the Kinetix 6000M (IPIM) module has fiber-optic cable connectors positioned identical to the Kinetix 6000 (2094-BMxx-S) drives, the IPIM module uses the same fiber-optic cable lengths as the drive modules.

## Ethernet Cable Connections

Figure 76 - Fiber-optic Cable Example - Logix 5000 Controller with Kinetix 6000M (IPIM) Module

<!-- image -->

In this example, all the drive modules and the IPIM module are on the same Sercos ring. The ring begins and ends at the 1756-M16SE Sercos module. IDM units (not shown for simplicity) connected to the IPIM module, are also part of this Sercos ring.

For more Kinetix 6000 IDM system examples including the IDM units, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

This procedure assumes you have your ControlLogix or CompactLogix EtherNet/IP™ module and Bulletin 2094 control modules mounted and are ready to connect the Ethernet network cables.

The EtherNet/IP network is connected by using the PORT 1 and/or PORT 2 connectors.

Table 97 - EtherNet/IP Connector Location

|                               | Drive Family Cat. No. EtherNet/IP Network Refer to   |         |
|-------------------------------|------------------------------------------------------|---------|
| Kinetix 6000M 2094-SEPM-B24-S | Monitoring, diagnostics, and firmware upgrades       | page 48 |

Figure 77 - ControlLogix and CompactLogix Ethernet Port Locations

<!-- image -->

## Notes:

## Configure the Kinetix 6000M Integrated Drive-Motor System

<!-- image -->

## Configure and Start the Kinetix 6000 Drive System

This chapter provides procedures for configuring the Kinetix® 6000 drive components with your Logix 5000™ Sercos communication module.

| Topic Page                                                    |
|---------------------------------------------------------------|
| Configure the Kinetix 6000M Integrated Drive-Motor System 107 |
| Configure the Drive Modules 108                               |
| Configure the Logix 5000 Sercos interface Module 114          |
| Apply Power to the Kinetix 6000 Drive 124                     |
| Test and Tune the Axes 126                                    |
| Configure Drive Parameters and System Variables 130           |

<!-- image -->

Before you begin, make sure you know the catalog number for each drive component, the Logix 5000 module, and the servo motor/ actuator in your motion control application.

Configuration for the Kinetix 6000M integrated drive-motor (IDM) system follows a procedure similar to what is described in this chapter. You'll assign each IDM unit a node address and configure the IDM system in the Logix Designer application.

The IPIM module does not require configuration for your IDM units to be configured in the Sercos ring. However, you can include the IPIM module in your project by connecting it to a configured Ethernet module in the Logix 5000 chassis and adding it under the Ethernet module in the I/O configuration tree. An Add-On Profile is also needed to use the IPIM module in the project, but as a result you can view IPIM module status information in the configuration software and use it in your application program. The Ethernet connection is also used to upgrade the IPIM module firmware by using ControlFLASH™ software.

For system configuration and startup procedures specific to the IDM system, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

## Configure the Drive Modules

Follow these steps to configure the integrated axis module (IAM) and axis modules (AM).

IMPORTANT

If you have one or more IDM power interface modules (IPIM) on your power rail, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for system configuration information specific to the Kinetix 6000M IDM system.

1. Verify that no power is applied to the IAM and AM modules and that the communication cables are plugged into the appropriate connectors. To verify communication, refer to Sercos Fiber-optic Cable Connections on page 102 .
2. Set the base node address for the IAM module by setting the Node Address switches.

| To Configure Begin With       |                                                                            |
|-------------------------------|----------------------------------------------------------------------------|
| The IAM module                | step 2                                                                     |
| Any AM module                 | step 4                                                                     |
| Kinetix 6000M IDM system  (1) | Kinetix 6000M Integrated Drive-Motor User Manual, publication 2094-UM003 . |

Valid node addresses for Sercos communication are 01…99. The left switch sets the most significant digit (MSD) and the right switch sets the least significant digit (LSD).

| To Press                                                   |
|------------------------------------------------------------|
| Increment the (MSD/LSD) node address The plus (+) switch.  |
| Decrement the (MSD/LSD) node address The minus (-) switch. |

Decrements MSD

MSD

Increments MSD

<!-- image -->

Setting the base node address on the IAM module determines the node address for the IAM (inverter) module. Node addressing for all slot locations on the same power rail increment (from the IAM inverter) left to right.

3. Cycle control power to initialize the IAM module.

## IMPORTANT

The base node address setting takes effect only after the IAM power module is initialized.

## IMPORTANT

When two or more IAM modules are connected to the same Sercos interface module, each node address must be unique.

Refer to the node addressing examples beginning on page 110 .

4. Set the Sercos communication rate with DIP switches 2 and 3.

| For This Communication Rate Set Switch 2 Set Switch 3   |        |
|---------------------------------------------------------|--------|
| 4 Mbps OFF ON                                           |        |
| 8 Mbps  (1)                                             | ON OFF |

- (1) The Kinetix 6000M IDM system supports only 8 Mbps and is hardwired for this setting.
5. Set the Sercos optical power level with DIP switch 1.

| For This Optical Power Level Set Switch 1   |
|---------------------------------------------|
| Low OFF                                     |
| High ON                                     |

The optical power setting you use depends on the type of Sercos cable you're using and the length of the cable.

| Power Setting  (1)   | Plastic Cable (2)   | Glass Cable (3)                        |
|----------------------|---------------------|----------------------------------------|
| Low                  | ≤ 15 m (49.2 ft)    | ≤ 100 m (382 ft)                       |
|                      |                     | High > 15 m (49.2 ft) > 100 m (382 ft) |

- (1) Other factors include attenuation caused by the use of bulkhead connectors and cable bending.

(2) Catalog numbers 2090-SCxP.

(3) Catalog numbers 2090-SCVG.

<!-- image -->

6. Repeat step 4 and step 5 for each 2094-xMxx-x AM module.

Figure 78 - Node Addressing Example 1

<!-- image -->

In Example 1, the Kinetix 6000 (6-axis) drive system 1 power rail contains one IAM module, three AM modules, one shunt module, and one slot-filler module. The shunt module and slot-filler modules are not assigned a Sercos node address, but the system identifies them with a slot location.

Kinetix 6000 (2-axis) drive system 2 power rail contains one IAM module and one AM module. The base node address of the (system 2) IAM module must be set for an address of 007.

## IMPORTANT

## IMPORTANT

The node address for each axis module is determined by the base node-address switch setting on the IAM module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiberoptic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

Figure 79 - Node Addressing Example 2

<!-- image -->

In this example, Sercos interface module 1 controls axes 1…4 and module 2 controls axes 5…7. The slot-filler module is not assigned a Sercos node address, but the system identifies it with a slot location.

You can mount the two Sercos interface modules in two separate ControlLogix chassis (as shown) or you can mount them in the same chassis.

## IMPORTANT

## IMPORTANT

The node address for each axis module is determined by the base node-address switch setting on the IAM module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiberoptic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

## Figure 80 - Node Addressing Example 3

<!-- image -->

In this example, the Kinetix 6000 (8-axis) power rail contains a double-wide IAM module, two double-wide AM modules, one single-wide AM module, and one slot-filler module. The slot-filler module is not assigned a Sercos node address, but the system identifies it with a slot location.

The leftmost slot of a double-wide module determines the node address. So, in the example above, node addresses 02, 04, and 06 (the rightmost slots of the double-wide modules) are not used.

## IMPORTANT

## IMPORTANT

The node address for each axis module is determined by the base node-address switch setting on the IAM module.

Do not position axis modules to the right of shunt or slot-filler modules. The added distance between non-adjacent axes can increase electrical noise and impedance, and requires longer fiberoptic cable lengths.

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

Figure 81 - Node Addressing Example 4

<!-- image -->

In this example, the Kinetix 6000 (5-axis) power rail contains two single-wide axis modules and one IDM system. Neither the slot-filler or IPIM module is assigned a Sercos node address, but the system identifies them with a slot location.

Node addressing on the power rail is no different than the previous examples. Node address 02 and 05 are available for any of the IDM units, but to avoid confusion, the node addressing for the IDM units was started at 20. Unlike the axis modules, each IDM unit has switches that determine its node address. In this example, the IDM unit node addressing is sequential, but that's optional.

## IMPORTANT

Creating a duplicate node address between the axis modules mounted on the power rail and the IDM system (in the same Sercos ring) generates error code E50. Each node address on the Sercos ring must be unique within the range of 01…99. Axes on the same power rail as the IPIM module do not have to be in the same Sercos ring as the IDM units.

## IMPORTANT

Slot-filler modules must be used to fill any unoccupied slot on the power rail. However, you can replace slot-filler modules with AM modules or the 2094-BSP2 shunt module (maximum one 2094-BSP2 shunt module per power rail).

## Configure the Logix 5000 Sercos interface Module

This procedure assumes that you have wired your Kinetix 6000 system and have configured the communication rate and optical power switches.

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

## Configure the Logix 5000 Module

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
7. Verify that the Data Rate setting matches DIP switches 2 and 3 (communication rate), as set on the IAM and AM module, or choose the Auto Detect setting.
8. From the Cycle Time pull-down menu, choose the Cycle Time according to the table below.

<!-- image -->

<!-- image -->

| Logix 5000 Sercos Module Number of Axes Data Rate   |          |             |
|-----------------------------------------------------|----------|-------------|
| 1756-M03SE or 1756-L60M03SE                         | Up to 3  | 4 or 8 Mbps |
| 1756-M08SE Up to 8                                  |          | 4 or 8 Mbps |
| 1756-M16SE or 1784-PM16SE                           | Up to 16 | 4 or 8 Mbps |
| 1768-M04SE Up to 4                                  |          | 4 or 8 Mbps |

|             | Data Rate Number of Axes Cycle Time   |                          |
|-------------|---------------------------------------|--------------------------|
| 4 Mbps      | Up to 2 0.5 ms                        |                          |
| 4 Mbps      | Up to 4 1 ms                          |                          |
| 4 Mbps      | Up to 8 2 ms                          |                          |
| 4 Mbps      | No support for axes 9…16              | No support for axes 9…16 |
| 8 Mbps  (1) | Up to 4 0.5 ms                        |                          |
| 8 Mbps  (1) | Up to 8 1 ms                          |                          |
| 8 Mbps  (1) | Up to 16 2 ms                         |                          |

- (1) The Kinetix 6000M IDM system supports only 8 Mbps and is hardwired for this setting.

<!-- image -->

The number of axes/module is limited to the number of axes as shown in step 6 .

9. From the Transmit Power pull-down menu, choose High.

The default setting is High, however this setting is dependent on the cable length (distance to next receiver) and cable type (glass or plastic).

10. Enter the Transition to Phase setting.

The Transition to Phase default setting is 4 (phase 4). The Transition to

- Phase setting stops the ring in the phase specified.
11. Click OK.
12. Repeat step 1 through step 11 for each Logix 5000 module.

## Configure the Kinetix 6000 Drive Modules

Follow these steps to configure the Kinetix 6000 drive modules.

1. Right-click the Logix 5000 module you just created and choose New Module.

The Select Module dialog box opens.

<!-- image -->

2. Expand the Drives category and select drive components appropriate for your actual hardware configuration.

## IMPORTANT

In order for the Kinetix 6000 drive to communicate with the Sercos interface module (indicated by three solid-green status indicators on the Sercos module), you must be using RSLogix 5000® software, version 11.00 or later, or the Logix Designer application.

3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new module.
- a. Type the module Name.
- b. Enter the Node address.

Set the node address in the software to match the node setting on the drive. Refer to Configure the Drive Modules, step 2, on page 108 .

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

<!-- image -->

11. Click Apply.

<!-- image -->

With drive firmware revision 1.80 or later, and the Logix Designer application or RSLogix 5000 software, version 13 or later, it is possible to configure the Auxiliary Axis feedback port as a Feedback Only axis. With this feature, you can configure each IAM inverter or AM module to appear as two axes/nodes on the Sercos ring. The base node is the servo axis using the motor feedback, and the base node (plus 128) is a feedback-only axis that uses the auxiliary feedback port.

Auxiliary feedback is not supported by the Kinetix 6000M IDM units.

<!-- image -->

The Auxiliary Axis (Node 129) is configured identical to Node 1 by clicking New Axis and creating a new tag.

12. Click Apply if you made changes.
13. Click the Power tab.
14. From the Bus Regulator Catalog Number pull-down menu, choose the shunt option appropriate for your actual hardware configuration.

<!-- image -->

|                                                                 | If your IAM module is And your hardware configuration includes this shunt option Then choose   |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Configured as an IAM module or common-bus leader IAM module (1) | Internal shunt resistors only Internal or <none>                                               |
| Configured as an IAM module or common-bus leader IAM module (1) | Bulletin 2094 (rail mounted) shunt module 2094-BSP2                                            |
| Configured as an IAM module or common-bus leader IAM module (1) | Bulletin 1394 passive shunt module (connected to the 2094-BSP2 shunt module)  1394-SRxxxx      |
| Configured as an IAM module or common-bus leader IAM module (1) | External active shunt module Internal or <none>                                                |
| Configured as a common-bus follower IAM module  (2)             | N/A. Shunts are disabled on follower IAM module CommonBus Follow                               |

<!-- image -->

To avoid damage to your Bulletin 1394 external shunt module when wired to the 2094-BSP2 shunt module, verify that the proper 230V or 460V fuse is installed prior to applying power.

Refer to Kinetix Motion Accessories Specifications Technical Data, publication

KNX-TD004, for more information.

## IMPORTANT

When configured to use the Bulletin 1394 or 2094 shunt modules, the IAM bus regulator capacity attribute displays the utilization of total shunt power available (as a percent) based on the power rail configuration.

Refer to Kinetix Motion Accessories Specifications Technical Data, publication KNX-TD004, for shunt power specification and examples.

15. Calculate additional bus capacitance, if this applies to your application, and enter the value here (version 20.00 or later), or refer to Appendix E to set the Add Bus Cap parameter.

The Additional Bus Capacitance field applies only to the IAM module.

## IMPORTANT

16. Click OK.
17. Repeat step 1 through step 10 for each Bulletin 2094 AM module and each IDM unit.

## Configure the Motion Group

Follow these steps to configure the motion group.

1. Right-click Motion Groups in the Controller Organizer and choose New Motion Group.

The New Tag dialog box opens.

<!-- image -->

2. Type the new motion group Name.
3. Click OK.

The new motion group appears under the Motion Groups folder.

4. Right-click the new motion group and choose Properties.

DC common-bus applications must calculate Total Bus Capacitance and Additional Bus Capacitance and set the Add Bus Cap parameter in the leader IAM module. However, you can set the parameter as shown in step 15 or by using DriveExplorer™ the Logix Designer application, as shown in Appendix E.

Refer to Appendix C, for more information on making the calculations. Refer to Appendix E, for more information on setting the Add Bus Cap parameter.

The Motion Group Properties dialog box opens.

<!-- image -->

5. Click the Axis Assignment tab and move your axes (created earlier) from Unassigned to Assigned.
6. Click the Attribute tab and edit the default values as appropriate for your application.
7. Click OK.

## Configure Axis Properties

The peak current ratings of the Kinetix 6000 AM modules are configured at the factory as 150% of continuous current. You can program 460V (series B and later) AM modules and the equivalent IAM (inverter) modules, for up to 250% of continuous inverter current.

Refer to Appendix F to recalculate torque and acceleration or deceleration limit values, and paste them into the appropriate Axis Properties dialog box in the Logix Designer application.

Follow these steps to configure Axis properties for motor feedback.

1. Right-click an axis in the Controller Organizer and choose Properties. The Axis Properties dialog box opens.
2. Click the Drive/Motor tab.
3. Click Change Catalog.

<!-- image -->

The Change Catalog Number dialog box opens.

<!-- image -->

4. Select the motor catalog number appropriate for your application. To verify the motor catalog number, refer to the motor name plate.
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

<!-- image -->

13. Click Set Custom Stop Action.

The Custom Stop Action Attributes dialog box opens and lets you set delay times for servo motors and RBM modules.

14. Configure the delay times.
- a. Type the Brake Engage Delay Time.
- b. Type the Brake Release Delay Time.
- c. Set the Resistive Brake Contact Delay time (0 - 1000 ms range).

For recommended motor brake response times, refer to the Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001 . The recommended delay time for 2090-XB33-xx and 2090-XB120-xx RBM modules is 71 ms.

<!-- image -->

- d. Click Close to close the Custom Stop Action Attributes dialog box.
15. Click Apply.
16. Repeat step 1 through step 15 for each Bulletin 2094 AM module.

Follow these steps to configure Auxiliary Axis properties.

## IMPORTANT Auxiliary feedback is not supported by the Kinetix 6000M IDM units.

1. Right-click an auxiliary axis in the Controller Organizer and choose Properties.

The Axis Properties dialog box opens on the General tab.

If an axis is associated to the auxiliary axis node, set the Axis Configuration on the General tab of the Axis Properties dialog box to Feedback Only.

<!-- image -->

2. Click the Drive/Motor tab.

## Apply Power to the Kinetix 6000 Drive

The Drive/Motor tab displays the amplifier being used and the Loop Configuration is Aux Feedback Only. This is the only choice if the amplifier is using the primary node for Servo (motor) configuration.

<!-- image -->

3. Click the Aux Feedback tab.

<!-- image -->

## IMPORTANT

The Aux Feedback tab must be configured for the auxiliary feedback type being used. In this example, an SRM feedback device is being used.

4. From the Feedback Type pull-down menu, choose the feedback type appropriate for your auxiliary feedback motor.
5. Click OK.
6. Verify your Logix 5000 program and save the file.

## Download the Program

After completing the Logix 5000 configuration you must download your program to the Logix 5000 processor.

This procedure assumes that you have wired and configured your Kinetix 6000 system (with or without the LIM module) and your Sercos interface module.

<!-- image -->

ATTENTION: Capacitors on the DC bus can retain hazardous voltages after input power has been removed. Before working on the drive, measure the DC bus voltage to verify it has reached a safe level or wait the full time interval as indicated in the warning on the front of the drive. Failure to observe this precaution could result in severe bodily injury or loss of life.

Refer to the Line Interface Module Installation Instructions, publication 2094IN005, when troubleshooting the LIM module status indicators, and for the location of LIM module circuit breakers, connectors, and status indicators.

Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for connector locations and when troubleshooting the IPIM module and IDM unit status indicators.

Follow these steps to apply power to the Kinetix 6000 drive system.

1. Disconnect the load to the motor.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, disconnect the load to the motor. Make sure each motor is free of all linkages when initially applying power to the system.

2. Determine your source of control power.
3. Observe the IAM/AM module logic power status indicator.
4. Determine your source of three-phase input power
5. Observe the IAM/AM module fault status indicator.

| If Your Control Power Then       |                                                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sourced from a LIM module     | 1. Verify that CB1, CB2, and CB3 are in the OFF position. 2. Apply three-phase input power to the LIM module VAC Line connector. 3. Set CB3 to the ON position. 4. Set CB2 to the ON position. 5. Go to main step 3. |
| Is not sourced from a LIM module | 1. Apply (95…264V AC) control power to the IAM module (CPD connector). 2. Go to main step 3.                                                                                                                         |

<!-- image -->

| If the Logic Power Indicator is  (1)   | Then                                                                 |
|----------------------------------------|----------------------------------------------------------------------|
|                                        | ON Go to step  .                                                     |
| Not ON                                 | 1. Check your control power connections. 2. Go back to main step 2 . |

| If Your Three-phase Power        | Then                                                                                                                                                                                                                                                                     |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Is sourced from a LIM module     | 1. Set CB1 to the ON position. 2. Verify the Hardware Enable Input signal (IOD-2) for each axis is at 0 volts. Remove the connection between IOD-1 and IOD-2 if one exists. (1) 3. Go to main step 5 .                                                                   |
| Is not sourced from a LIM module | 1. Apply 195…265V AC (230V) or 324…528V AC (460V) input power to the IAM module (IPD connector). 2. Verify the Hardware Enable Input signal (IOD-2) for each axis is at 0 volts. Remove the connection between IOD-1 and IOD-2 if one exists. (1) 3. Go to main step 5 . |

.

## Test and Tune the Axes

The status indicator first flashes the Sercos node address, then cycles through ring phases until final configuration (phase 4) is reached.

| IAM/AM Fault Status Indicator Status Do This            |                                                                                                                          |                                                                         |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Actively cycling (phase 0)                              | The drive is looking for a closed Sercos ring. Wait for phase 1 or take corrective action until you reach phase 1.       | Check fiber-optic connections.                                          |
| Displaying a fixed 1 (phase 1)                          | The drive is looking for active nodes. Wait for phase 2 or take corrective action until you reach phase 2.               | Check node addressing.                                                  |
| Displaying a fixed 2 (phase 2)                          | The drive is configuring nodes for communication. Wait for phase 3 or take corrective action until you reach phase 3.    | Check program motor and drive configuration against installed hardware. |
| Displaying a fixed 3 (phase 3)                          | The drive is configuring device specific parameters. Wait for phase 4 or take corrective action until you reach phase 4. | Check motor catalog number against selection.  (1)                      |
|                                                         | Displaying a fixed 4 (phase 4) The drive is configured and active. Go to step 6                                          | .                                                                       |
| Flashing an E followed by two numbers Drive is faulted. |                                                                                                                          | Go to Kinetix 6000 Drive System Error Codes on page 134                 |

6. Observe the status indicators on the front of the IAM/AM module. Refer to troubleshooting tables for the Drive, Comm, and Bus status indicators in IAM/AM Module Status Indicators on page 138. Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for IPIM module and IDM unit status indicator troubleshooting tables.
7. Observe the three Sercos indicators on the Logix 5000 Sercos module.

| Three Sercos Indicators Status Do This       |                                                   |                                                                                        |
|----------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------------|
|                                              | Flashing green and red Establishing communication | Wait for steady green on all three indicators.                                         |
|                                              | Steady green Communication ready                  | Go to Test and Tune the Axes on page 126 .                                             |
| Not flashing green and red/ not steady green | Sercos module is faulted                          | Go to the appropriate Logix 5000 manual for specific instructions and troubleshooting. |

These procedures assume that you have configured your Kinetix 6000 drive, your Logix 5000 Sercos interface module, and applied power to the system.

For help with using the Logix Designer application, as it applies to testing and tuning your axes with ControlLogix, CompactLogix, or SoftLogix Sercos modules, refer to Additional Resources on page 10 .

## Test the Axes

Follow these steps to test the axes.

1. Verify the load was removed from each axis.
2. Right-click an axis in your Motion Group folder and choose Properties.

The Axis Properties dialog box opens.

<!-- image -->

3. Click the Hookup tab.
4. Type 2.0 as the number of revolutions for the test or another number more appropriate for your application.
5. Apply Hardware Enable Input signal (IOD-2) for the axis you are testing.

|                         | This Test Performs this Test                                                                                                          |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Test Marker (1)         | Verifies marker detection capability as you rotate the motor shaft.                                                                   |
| Test Feedback (1)       | Verifies feedback connections are wired correctly as you rotate the motor shaft. Also, lets you define polarity.                      |
| Test Command & Feedback | Verifies motor power and feedback connections are wired correctly as you command the motor to rotate. Also, lets you define polarity. |

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply 24V ENABLE signal (IOD-2) only to the axis you are testing.

IMPORTANT Hardware Enable input for IDM units is on the IPIM module.

6. Click the desired test (Marker/Feedback/Command &amp; Feedback) t to verify connections.

The Online Command dialog box opens. Follow the on-screen test instructions. When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

7. Click OK.

The Online Command - Apply Test dialog box opens (Feedback and Command &amp; Feedback tests only). When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

8. Click OK.
9. Determine if your test completed successfully.
- (1) The hardware enable input for IDM units is on the IPIM module.

<!-- image -->

## Tune the Axes

The load observer feature (available with drive firmware revision 1.124 or later) can provide good performance without having to tune your axis. Using load observer with auto-tuned gains can maximize system performance. Refer to Appendix D for more load observer information.

Follow these steps to tune the axes.

1. Verify the load is still removed from the axis being tuned.

<!-- image -->

ATTENTION: To reduce the possibility of unpredictable motor response, tune your motor with the load removed first, then reattach the load and perform the tuning procedure again to provide an accurate operational response.

2. Click the Tune tab.
3. Type values for Travel Limit and Speed.

<!-- image -->

In this example, Travel Limit = 5 and Speed = 10. The actual value of programmed units depend on your application.

4. From the Direction pull-down menu, choose a setting. Forward Uni-directional is default.
5. Check Tune boxes as appropriate for your application.
6. Apply Hardware Enable Input signal (IOD-2) for the axis you are tuning.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply 24V ENABLE signal (IOD-2) only to the axis you are tuning.

IMPORTANT Hardware Enable input for IDM units is on the IPIM module.

7. Click Start Tuning to auto-tune your axis.

The Online Command - Tune Servo dialog box opens. When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

8. Click OK.

The Tune Bandwidth dialog box opens.

<!-- image -->

Actual bandwidth values (Hz) depend on your application and can require adjustment once motor and load are connected.

9. Record your bandwidth data for future reference.
10. Click OK.

## Configure Drive Parameters and System Variables

The Online Command - Apply Tune dialog box opens. When the test completes, the Command Status changes from Executing to Command Complete.

<!-- image -->

11. Click OK.
12. Determine if your test completed successfully.
- (1) The hardware enable input for IDM units is on the IPIM module.
13. Repeat Test and Tune the Axes for each axis.

<!-- image -->

This section provides information for accessing and changing parameters not accessible through the Logix Designer application.

IMPORTANT Drive parameters for the Kinetix 6000M IDM system are not accessible through the HIM module or DriveExplorer software.

## Tools for Changing Parameters

Most parameters are accessible through the Logix Designer application. Alternatives include the DPI compatible Human Interface Module (HIM) and DriveExplorer software.

Table 98 - Software For Changing Parameters

<!-- image -->

|                | Method Description Cat. No. Firmware Revision                  |                              |
|----------------|----------------------------------------------------------------|------------------------------|
| Software (1)   | DriveExplorer software  (2)                                    | 9306-4EXP02ENE 2.01 or later |
| Software (1)   | Serial to SCANport™ adapter 1203-SSS (Series B) 3.004 or later |                              |
| HIM module (3) | Full numeric LCD HIM 20-HIM-A3 N/A                             |                              |

Change Parameters with DriveExplorer Software

To navigate with DriveExplorer software, refer to the example dialog box below. In this example, the IAM I/O group folder is open, the Analog Outputs parameter group is selected, and the parameter elements are displayed in the box to the right.

IMPORTANT

Parameters are read-only when the Sercos ring is active. You must break the Sercos ring to change parameters.

To save changes, perform a nonvolatile save (NVS) prior to cycling power.

Figure 82 - DriveExplorer Software Example

<!-- image -->

Change Parameters with the HIM Module

When using the HIM module to monitor or change parameters, use the up and  and ) to arrive at selections. Refer to the instructions that came with your HIM module for more information.

Follow these steps to monitor or change parameters with the HIM module.

1. Select parameter, and press  .
2. Select I/O AM1 Group (for IAM module), and press  .
3. Select Analog Outputs, and press  .
- a. Analog Output 1 is displayed, and press  .
- b. For Analog Output 2 use arrows to select, and press  .
4. Press Sel.
5. Enter parameter number, and press  .

## Monitor System Variables with Analog Test Points

There are two analog output test points accessible from the IOD 26-pin connector on the IAM and AM module.

Table 99 - IAM/AM I/O 26-pin (IOD) Connector

| IOD Pin Description Signal      |
|---------------------------------|
| 23 Analog output 0 DAC0         |
| 24 Analog output common DAC_COM |
| 25 Analog output 1 DAC1         |
| 26 Analog output common DAC_COM |

Figure 83 - Pin Orientation for 26-pin I/O (IOD) Connector

<!-- image -->

Refer to Analog Outputs on page 55 for signal specifications.

Parameters begin with a variable to identify a specific axis by slot number, as follows:

- IAM module = 0 for parameters 0…999
- 1st AM module = 1 for parameters 1000…1999
- 2nd AM module = 2 for parameters 2000…2999 and so on
- 7th AM module = 7 for parameter 7000…7999

Table 100 - Monitor System Variables

| Analog Output   | Controlling Parameter Scale Parameter   | Controlling Parameter Scale Parameter   |                      |               |
|-----------------|-----------------------------------------|-----------------------------------------|----------------------|---------------|
| Analog Output   | Parameter Number (1)                    | Default Value (1)                       | Parameter Number (1) | Default Value |
| 1               | x681                                    | xx40                                    |                      | x682 0.0060   |
| 2               | x683                                    | xx84                                    |                      | x684 0.1000   |

(1)

x = slot number

The value entered in Scale Parameter scales the analog output so that you can get a full scale reading of the specific parameter for the dynamic range or values you are testing.

For linear scaling specifications, refer to Table 40 on page 56 .

Table 101 - Monitor Dynamic System Variables

| Attribute          | Parameter Number (1)   |
|--------------------|------------------------|
| Velocity feedback  | xx40                   |
| Velocity commanded | xx36                   |
| Torque feedback    | xx84                   |
| Torque commanded   | xx80                   |

(1) x = slot number.

## Safety Precautions

## Interpret Status Indicators

<!-- image -->

## Troubleshoot the Kinetix 6000 Drive System

This chapter provides troubleshooting tables for your Kinetix® 6000 drive system components.

| Topic Page                          |
|-------------------------------------|
| Safety Precautions 133              |
| Interpret Status Indicators 133     |
| General System Anomalies 140        |
| Logix 5000/Drive Fault Behavior 142 |

Observe these safety precautions when troubleshooting your Kinetix 6000 drive.

<!-- image -->

ATTENTION: Capacitors on the DC bus can retain hazardous voltages after input power has been removed. Before working on the drive, measure the DC bus voltage to verify it has reached a safe level or wait the full time interval as indicated in the warning on the front of the drive. Failure to observe this precaution could result in severe bodily injury or loss of life.

<!-- image -->

<!-- image -->

ATTENTION: Do not attempt to defeat or override the drive fault circuits. You must determine the cause of a fault and correct it before you attempt to operate the system. Failure to correct the fault could result in personal injury and/or damage to equipment as a result of uncontrolled machine operation.

ATTENTION: Provide an earth ground for test equipment (oscilloscope) used in troubleshooting. Failure to ground the test equipment could result in personal injury.

Refer to these troubleshooting tables to identify faults, potential causes, and the appropriate actions to resolve the fault. If the fault persists after attempting to troubleshoot the system, please contact your Rockwell Automation sales representative for further assistance.

## Kinetix 6000M IDM System Error Codes

The IAM module reports a single, generic IPIM Fault whenever a fault occurs on any IPIM in the same backplane as the IAM module. All IPIM faults result in an open contactor. The Logix 5000™ Axis Tag for this fault is IPIMFault.

The IPIM module is not a Sercos device, so the IAM module reports any IPIM faults to the Logix 5000 motion subsystem. IPIM faults are reset by performing

a fault reset on the IAM module. Issuing a fault reset command to the IAM module also generates a fault reset to all the IPIM modules in the same backplane as the IAM. Detailed information about the IPIM fault status can be obtained by messaging to the IAM module.

Connecting the IPIM module into the Logix 5000 environment as an EtherNet/IP™ device does not disable fault reporting through the IAM module. Only the IAM fault reporting lets the Logix 5000 motion sub-system take action based on the IPIM module fault status. IPIM faults are also reported over the Ethernet connection. However, IPIM faults must be reset by applying a fault reset instruction to the IAM module. The integration of the IPIM module into the Logix 5000 environment through the EtherNet/IP network provides additional capabilities you can choose to take advantage of in your program.

Refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003, for more information on troubleshooting the IDM drive-motor system.

## Kinetix 6000 Drive System Error Codes

The following list of problematic symptoms (no error code shown) and faults with assigned error codes is designed to help you resolve anomalies.

When a fault is detected, the seven-segment status indicator displays an E followed by the flashing of the two-digit error code, one digit at a time. This is repeated until the error code is cleared.

Table 102 - Seven-segment Status Indicator Error Codes

| Error Code              | Fault Message - Logix Designer (HIM)   | Anomaly or Symptom Potential Cause Possible Resolution   |                                                             |                                                                                 |
|-------------------------|----------------------------------------|----------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------|
|                         |                                        | Power (PWR) indicator not ON                             | No AC power or auxiliary logic power.                       | Verify AC control power is applied to the Kinetix 6000 system.                  |
|                         |                                        | Power (PWR) indicator not ON                             | Internal power supply malfunction.                          | Call your Rockwell Automation sales representative to return module for repair. |
| No Error Code Displayed | No Error Code Displayed                | Motor jumps when first enabled                           | Motor wiring error.                                         | • Check motor wiring. • Run Hookup test in the Logix Designer application.      |
|                         |                                        | Motor jumps when first enabled                           |                                                             | Incorrect motor chosen. Verify the proper motor is selected.                    |
|                         |                                        | Digital I/O not working correctly                        |                                                             | I/O power supply disconnected. Verify connections and I/O power source.         |
| E00                     | BusUndervoltage Fault (Blown fuse)     | A blown fuse was detected on the inverter PCB            | Blown fuse.                                                 | Call your Rockwell Automation sales representative to return module for repair. |
| E04                     | MotorOvertemp Fault (Motor Overtemp)   | Motor thermal switch tripped                             | • High motor ambient temperature and/or • Excessive current | • Operate within (not above) the continuous torque °° pq rating for the ambient temperature 40 °C (104 °F) maximum. • Lower ambient temperature, increase motor cooling.                                                                                 |
|                         |                                        | Motor thermal switch tripped                             | Motor wiring error.                                         | Check motor wiring at MF connector on the IAM/AM module.                        |
|                         |                                        | Motor thermal switch tripped                             |                                                             | Incorrect motor selection. Verify the proper motor has been selected.           |

Table 102 - Seven-segment Status Indicator Error Codes (Continued)

| Error Code   | Fault Message - Logix Designer (HIM)           | Anomaly or Symptom Potential Cause Possible Resolution                                                                                                         |                                                                                                                                                                                            |                                                                                                                                                                                                                        |
|--------------|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E05          | DriveOvercurrent Fault (Power Fault)           | Self-protection of the Intelligent Power Module (IPM) is indicating a major power related fault condition.                                                     |                                                                                                                                                                                            | Motor cables shorted. Verify continuity of motor power cable and connector.                                                                                                                                            |
| E05          | DriveOvercurrent Fault (Power Fault)           | Self-protection of the Intelligent Power Module (IPM) is indicating a major power related fault condition.                                                     | Motor winding shorted internally.                                                                                                                                                          | Disconnect motor power cables from the motor. If the motor is difficult to turn by hand, consider replacing the motor.                                                                                                 |
| E05          | DriveOvercurrent Fault (Power Fault)           | Self-protection of the Intelligent Power Module (IPM) is indicating a major power related fault condition.                                                     | Kinetix 6000 drive temperature too high.                                                                                                                                                   | • Check for clogged vents or defective fan. • Make sure cooling is not restricted by insufficient space around the unit.                                                                                               |
| E05          | DriveOvercurrent Fault (Power Fault)           | Self-protection of the Intelligent Power Module (IPM) is indicating a major power related fault condition.                                                     | Operation above continuous power rating and/or product environmental ratings.                                                                                                              | • Verify ambient temperature is not too high. • Operate within the continuous power rating. • Reduce acceleration rates. • Reduce deceleration rates.                                                                  |
| E05          | DriveOvercurrent Fault (Power Fault)           | Self-protection of the Intelligent Power Module (IPM) is indicating a major power related fault condition.                                                     | Kinetix 6000 drive has a short circuit, overcurrent, or failed component.                                                                                                                  | Remove all power and motor connections, and preform a continuity check from the DC bus to the U, V, and W motor outputs. If a continuity exists, check for wire fibers between terminals, or send drive in for repair. |
| E06          | HardOvertravel Fault (+/- Hard Overtravel)     | Axis moved beyond the physical travel limits in the positive/negative direction.                                                                               | Dedicated overtravel input is inactive.                                                                                                                                                    | • Check wiring. • Verify motion profile. • Verify axis configuration in software.                                                                                                                                      |
| E07          | MotFeedbackFault (Motor Feedback Loss)         | The feedback wiring is open, shorted, or missing.                                                                                                              | The feedback wiring is open, shorted, or missing.                                                                                                                                          | • Check motor encoder wiring. • Run Hookup test in the Logix Designer application.                                                                                                                                     |
| E09          | BusUndervoltage Fault (Bus Undervoltage)       | With three-phase power present, the DC bus voltage is below limits.                                                                                            | • DC bus voltage for 460V system is below 275V • DC bus voltage for 230V system is below 137V                                                                                              | • Verify voltage level of the incoming AC power. • Check AC power source for glitches or line drop. • Install an uninterruptible power supply (UPS) on your AC input.                                                  |
| E09          | BusUndervoltage Fault (Bus Undervoltage)       | DC bus voltage fell below the undervoltage limit while an axis on the follower power rail was enabled.                                                         | • DC bus voltage for 460V system is below 275V • DC bus voltage for 230V system is below 137V                                                                                              | Disable follower axis before removing power.                                                                                                                                                                           |
| E10          | DriveOvervoltage Fault (Bus Overvoltage)       | The DC bus voltage is above limits.                                                                                                                            | When the motor is driven by an external mechanical power source, it can regenerate too much peak energy through the drive power supply. The system faults to save itself from an overload. | • Change the deceleration or motion profile. • Use a larger system (motor and Kinetix 6000 drive). • Install shunt module.                                                                                             |
| E10          | DriveOvervoltage Fault (Bus Overvoltage)       | The DC bus voltage is above limits.                                                                                                                            | • DC bus voltage for 460V system is over 820V • DC bus voltage for 230V system is over 410V                                                                                                | Verify input is within specifications.                                                                                                                                                                                 |
| E11          | MotFeedbackFault (Illegal Hall State)          | State of Hall feedback inputs is incorrect.                                                                                                                    | Improper connections.                                                                                                                                                                      | • Verify the Hall wiring at the MF connector on the IAM/ AM module. • Verify 5V power supply to the encoder.                                                                                                           |
| E16          | Softovertravel Fault (+/- Software Overtravel) | Axis position exceeded maximum software setting.                                                                                                               | Axis position exceeded maximum software setting.                                                                                                                                           | • Verify motion profile. • Verify overtravel settings are appropriate.                                                                                                                                                 |
| E18          | OverSpeedFault (Overspeed Fault)               | Motor speed has exceeded 150% of maximum rated speed. The 100% trip point is dictated by the lesser of the user velocity limits or the motor rated base speed. | Motor speed has exceeded 150% of maximum rated speed. The 100% trip point is dictated by the lesser of the user velocity limits or the motor rated base speed.                             | • Check cables for noise. • Check tuning.                                                                                                                                                                              |
| E19          | PositionErrorFault (Follow Error)              | Position error limit was exceeded.                                                                                                                             | Position error limit was exceeded.                                                                                                                                                         | • Increase the feed forward gain. • Increase following error limit or time. • Check position loop tuning. • Verify sizing of system. • Verify mechanical integrity of system within specification limits.              |
| E20          | MotFeedbackFault (Mtr Fdbk AQB)                | Motor Encoder State Error                                                                                                                                      | The motor encoder encountered an illegal transition.                                                                                                                                       | • Use shielded cables with twisted pair wires. • Route the feedback away from potential noise sources. • Check the system grounds. • Replace the motor/encoder.                                                        |

## Table 102 - Seven-segment Status Indicator Error Codes (Continued)

| Error Code   | Fault Message - Logix Designer (HIM)                                                                                                                       | Anomaly or Symptom Potential Cause Possible Resolution                                                                                |                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E21          | AuxFeedbackFault (Aux Feedback Comm)  Communication was not established with an intelligent encoder. Verify auxiliary encoder wiring.                      | AuxFeedbackFault (Aux Feedback Comm)  Communication was not established with an intelligent encoder. Verify auxiliary encoder wiring. | AuxFeedbackFault (Aux Feedback Comm)  Communication was not established with an intelligent encoder. Verify auxiliary encoder wiring.                                                                   |                                                                                                                                                                                                                                                                                  |
| E30          | MotFeedbackFault (Motor Feedback Comm) Communication was not established with an intelligent encoder.                                                      | MotFeedbackFault (Motor Feedback Comm) Communication was not established with an intelligent encoder.                                 | MotFeedbackFault (Motor Feedback Comm) Communication was not established with an intelligent encoder.                                                                                                   | • Verify motor selection. • Verify the motor supports automatic identification. • Verify motor encoder wiring.                                                                                                                                                                   |
| E31          | DriveHardFault  Excessive motor shaft movement during power up, Sercos ring phase-up, or after a fault reset.                                              | DriveHardFault  Excessive motor shaft movement during power up, Sercos ring phase-up, or after a fault reset.                         | DriveHardFault  Excessive motor shaft movement during power up, Sercos ring phase-up, or after a fault reset.                                                                                           | Make sure there is no motor shaft movement during power up, Sercos ring phase-up, or during a fault reset.                                                                                                                                                                       |
|              |                                                                                                                                                            | Excessive ground current in                                                                                                           | Wiring error.                                                                                                                                                                                           | • Check motor power wiring. • Check input power wiring.                                                                                                                                                                                                                          |
|              |                                                                                                                                                            | Excessive ground current in                                                                                                           | Motor internal ground short. Replace motor.                                                                                                                                                             |                                                                                                                                                                                                                                                                                  |
| E34          | GroundShortFault (Ground Fault)                                                                                                                            | the converter was detected.                                                                                                           | Internal malfunction.                                                                                                                                                                                   | Disconnect motor power cable from drive and enable drive with current limit set to 0. If fault clears, then a wiring error or motor internal anomaly exists. If fault remains, call your sales representative.                                                                   |
|              |                                                                                                                                                            | Excessive ground current in                                                                                                           | Grounded control power terminal (applies to 230V systems only)                                                                                                                                          | • Remove ground from control power input. • Source control power from three-phase input power (refer to diagram on Figure 88 on page 155).                                                                                                                                       |
| E35          | DriveUndervoltage Fault (Precharge Fault)                                                                                                                  | Converter precharge cycle failed.                                                                                                     |                                                                                                                                                                                                         | Low AC input voltage. Check input AC voltage on all phases.                                                                                                                                                                                                                      |
| E35          | DriveUndervoltage Fault (Precharge Fault)                                                                                                                  | Converter precharge cycle failed.                                                                                                     |                                                                                                                                                                                                         | Internal malfunction. Call your sales representative.                                                                                                                                                                                                                            |
| E36          | DriveOvertemp Fault (System Overtemperature)                                                                                                               | Converter thermal switch tripped.                                                                                                     | Excessive heat exists in the power circuitry.                                                                                                                                                           | • Reduce acceleration rates. • Reduce duty cycle (ON/OFF) of commanded motion. • Increase time permitted for motion. • Use larger IAM converter module. • Check for clogged vents or defective fan. • Make sure cooling is not restricted by insufficient space around the unit. |
| E37          | PowerPhaseLoss Fault (Phase Loss Flt) • One or more phases of the input AC power is missing. • Axis was enabled when main (three-phase) power was removed. | • common-bus follower axis was enabled when DC bus power was removed.                                                                 | PowerPhaseLoss Fault (Phase Loss Flt) • One or more phases of the input AC power is missing. • Axis was enabled when main (three-phase) power was removed.                                              | • Check input AC voltage on all phases. • Disable axis before removing power.                                                                                                                                                                                                    |
| E38          | SercosFault (Sercos Ring Flt)                                                                                                                              | The Sercos ring is not active after being active and operational.                                                                     | Cable disconnected.                                                                                                                                                                                     | Check that fiber-optic cable is present and connected properly.                                                                                                                                                                                                                  |
| E39          | DriveHardFault (Self Sense Flt)                                                                                                                            | Self-sensing Commutation Start-up Error                                                                                               | Motion required for self-sensing start-up commutation was obstructed.                                                                                                                                   | • Verify that there are no impediments to motion at startup, such as hard limits. • Increase self-sensing current if high friction or load conditions exist. • Check motor or encoder wiring by using wiring diagnostics.                                                        |
| E43          | DriveEnableInput Fault (Drive Enable Flt)                                                                                                                  | Missing Drive Enable Input Signal                                                                                                     | • An attempt was made to enable the axis through software while the Drive Enable hardware input was inactive. • The Drive Enable input transitioned from active to inactive while the axis was enabled. | • Disable the Drive Enable Input fault. • Verify that Drive Enable hardware input is active whenever the drive is enabled through software.                                                                                                                                      |
| E49          | DriveHardFault (Safe-off HW Flt)                                                                                                                           | Safe torque-off function mismatch. Drive does not allow motion.                                                                       | • Loose wiring at STO connector. • Cable/header not seated properly in STO connector. • Safe torque-off circuit missing +24V DC.                                                                        | • Verify wire terminations, cable/header connections, and +24V. • Reset error and run proof test. • If error persists, return the drive to Rockwell Automation.                                                                                                                  |
| E50          | SercosFault (Sercos Same ADDR)  Duplicate node address detected on Sercos ring.                                                                            | SercosFault (Sercos Same ADDR)  Duplicate node address detected on Sercos ring.                                                       | SercosFault (Sercos Same ADDR)  Duplicate node address detected on Sercos ring.                                                                                                                         | Verify that each Sercos drive is assigned a unique node address.                                                                                                                                                                                                                 |
| E54          | Current feedback hardware fault detected. Replace the module.                                                                                              | Current feedback hardware fault detected. Replace the module.                                                                         | Current feedback hardware fault detected. Replace the module.                                                                                                                                           |                                                                                                                                                                                                                                                                                  |
| E55          | OverSpeedFault                                                                                                                                             | The velocity error limit has been exceeded.                                                                                           | Motor has exceeded velocity error limit Check the cables for noise.                                                                                                                                     |                                                                                                                                                                                                                                                                                  |

Table 102 - Seven-segment Status Indicator Error Codes (Continued)

| Error Code   | Fault Message - Logix Designer (HIM)                                       | Anomaly or Symptom Potential Cause Possible Resolution                                  |                                                                                                   |                                                                                                                                                                          |
|--------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E60          | DriveHardFault (Unknown Axis)                                              | Illegal ID bits detected Replace the module.                                            | Illegal ID bits detected Replace the module.                                                      |                                                                                                                                                                          |
| E61          | AuxFeedbackFault (Aux Fdbk AQB)                                            | Auxiliary Encoder State Error                                                           | The auxiliary encoder encountered an illegal transition.                                          | • Use shielded cables with twisted pair wires. • Route the feedback away from potential noise sources. • Check the system grounds. • Replace the motor/encoder.          |
| E62          | AuxFeedbackFault (Aux Fdbk Loss)                                           | The feedback wiring is open, shorted, or missing.                                       | The feedback wiring is open, shorted, or missing.                                                 | Check the motor feedback cable connectors/wiring to the IAM/AM module and servo motor.                                                                                   |
| E63          | AuxFeedbackNoise (Aux Fdbk Noise)                                          | Noise on auxiliary feedback cable.                                                      | Recommended grounding, per installation instructions, has not been followed.                      | • Verify grounding. • Route feedback cable away from noise sources. • Refer to System Design for Control of Electrical Noise Reference Manual, publication               |
| E64          | MotorFeedbackNoise (Mtr Fdbk Noise)                                        | Noise on motor feedback cable.                                                          | Recommended grounding, per installation instructions, has not been followed.                      | GMC-RM001 .                                                                                                                                                              |
| E65          | No Fault Message (condition indicated by on-screen message) (Hookup Fault) |                                                                                         | Hookup procedure failed Motor or feedback device malfunction.                                     | • Check motor power/feedback wiring. • Refer to on-screen message for resolution.                                                                                        |
| E66          | No Fault Message (condition indicated by on-screen message) (Atune Flt)    |                                                                                         | Autotune procedure failed Motor or feedback device malfunction.                                   | • Check motor power/feedback wiring. • Refer to on-screen message for resolution. • Perform Hookup in the Logix Designer application. • Consult application help screen. |
| E67          | DriveHardFault (Task init)                                                 | Operating system failed                                                                 | Software initialization fault detected due to hardware failure.                                   | • Cycle power. • If fault persists, replace module.                                                                                                                      |
| E68          | DriveHardFault (SCANport™ Comm)                                            |                                                                                         | DPI communication failed The DPI device or cable is faulty. Check DPI connections.                |                                                                                                                                                                          |
| E69          | DriveHardFault (Objects Init)                                              | Nonvolatile memory is corrupt due to control board hardware failure.                    | Nonvolatile memory is corrupt due to control board hardware failure.                              | Load default parameters, save to nonvolatile memory, and recycle power or reset the drive.                                                                               |
| E70          | DriveHardFault (NV Mem Init)                                               | Nonvolatile memory is corrupt due to control board software error.                      | Nonvolatile memory is corrupt due to control board software error.                                | Load default parameters, save to nonvolatile memory, and recycle power or reset the drive.                                                                               |
| E71          | DriveHardFault (Memory Init)                                               | RAM or nonvolatile memory validation failure                                            | RAM or nonvolatile memory validation failure                                                      | • Cycle power. • If fault persists, replace module.                                                                                                                      |
| E72          | DriveOvertemp Fault (Drive Overtemp)                                       | Inverter thermal switch tripped                                                         | The IAM or an AM module fan failed. Replace the failed module.                                    |                                                                                                                                                                          |
| E72          | DriveOvertemp Fault (Drive Overtemp)                                       | Inverter thermal switch tripped                                                         | The cabinet ambient temperature is above rating.                                                  | Check the cabinet temperature.                                                                                                                                           |
| E72          | DriveOvertemp Fault (Drive Overtemp)                                       | Inverter thermal switch tripped                                                         | The machine duty cycle requires an RMS current exceeding the continuous rating of the controller. | Change the command profile to reduce speed or increase time.                                                                                                             |
| E72          | DriveOvertemp Fault (Drive Overtemp)                                       | Inverter thermal switch tripped                                                         | The airflow access to the Kinetix 6000 system is limited or blocked.                              | Check airflow and re-route cables away from the Kinetix 6000 system.                                                                                                     |
| E73          | Communicate (Backplane Comm)                                               | Power rail CAN communication failed. Check module for proper mount.                     | Power rail CAN communication failed. Check module for proper mount.                               |                                                                                                                                                                          |
| E73          | Communicate (Backplane Comm)                                               | Power rail connection shorted or open. Check power rail and module for foreign objects. | Power rail connection shorted or open. Check power rail and module for foreign objects.           |                                                                                                                                                                          |
| E74          | DriveOvercurrent Fault (Bus OverCurrent)                                   | DC link current exceeds rating.                                                         | Motor or transmission malfunction.                                                                | • Check for proper motor sizing. • Check/replace transmission device. • Check/replace motor.                                                                             |
| E74          | DriveOvercurrent Fault (Bus OverCurrent)                                   | DC link current exceeds rating.                                                         | IAM module not sized properly.                                                                    | • Check for proper IAM module sizing. • Install larger kW rated IAM module.                                                                                              |
| E75          | DriveOvervoltage Fault (Shunt Time Out)                                    | The IAM/AM module, or shunt module has exceeded its shunt resistor continuous rating.   | The IAM/AM module, or shunt module has exceeded its shunt resistor continuous rating.             | • Use a properly sized shunt or modify duty cycle of the application. • System uses internal shunt and requires external shunt for additional capacity.                  |

## Table 102 - Seven-segment Status Indicator Error Codes (Continued)

| Error Code   | Fault Message - Logix Designer (HIM)      | Anomaly or Symptom Potential Cause Possible Resolution                                                                                    |                                                                                                                                           |                                                                                                                               |
|--------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| E76          | DriveHardFault (CAN Init)                 | DPI hardware initialization fault detected.                                                                                               | Control board hardware failure.                                                                                                           | • Reset System. • If fault persists, replace system module.                                                                   |
| E77          | DriveHardFault (Module Mismatch)          | Either 230V AM module is installed on power rail with 460V IAM module, or 460V AM module is installed on power rail with 230V IAM module. | Either 230V AM module is installed on power rail with 460V IAM module, or 460V AM module is installed on power rail with 230V IAM module. | Replace mismatched module.                                                                                                    |
| E78          | DriveHardFault (Sercos Init)              | Control hardware fault detected.                                                                                                          | Control hardware fault detected.                                                                                                          | • Cycle power. • If fault persists, replace module.                                                                           |
| E79          | DriveOvervoltage Fault (Shunt Module Flt) | Over-temperature fault indicator on Bulletin 2094 shunt module is steady red.                                                             | Over-temperature fault indicator on Bulletin 2094 shunt module is steady red.                                                             | Refer to Table 108 on page 140 .                                                                                              |
| E79          | DriveOvervoltage Fault (Shunt Module Flt) | Shunt-fault indicator on Bulletin 2094 shunt module is steady red. Refer to Table 109 on page 140                                         | Shunt-fault indicator on Bulletin 2094 shunt module is steady red. Refer to Table 109 on page 140                                         | .                                                                                                                             |
| E79          | DriveOvervoltage Fault (Shunt Module Flt) | Bulletin 2094 shunt module is missing from power rail.                                                                                    | Bulletin 2094 shunt module is missing from power rail.                                                                                    | • Install missing module on power rail. • Fill empty slot with slot-filler module.                                            |
| E80          | DriveHardFault (CPLD Flt)                 | Control hardware fault detected. Replace module.                                                                                          | Control hardware fault detected. Replace module.                                                                                          |                                                                                                                               |
| E81          | DriveHardFault (Common Bus Flt)           | Follower IAM module detected AC input power being applied.                                                                                | Follower IAM module detected AC input power being applied.                                                                                | Remove AC input power connections from follower IAM module.                                                                   |
| E90          | DriveHardFault (Precharge Timeout Flt)    | Precharge resistor power exceeds the resistor rating. Wait for resistor to cool.                                                          | Precharge resistor power exceeds the resistor rating. Wait for resistor to cool.                                                          |                                                                                                                               |
| E95          | IPIMFault (IPIM Module Flt)               | A fault has occurred in one or more IPIM modules on the power rail.                                                                       | A fault has occurred in one or more IPIM modules on the power rail.                                                                       | Refer to the troubleshooting chapter in the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 . |

## IAM/AM Module Status Indicators

Table 103 - Drive Status Indicator

| Drive Status Indicator Drive Status Possible Resolution                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------|
| Off Normal, no faults N/A                                                                                                           |
| Steady red Drive faulted  Refer to seven-segment error code and Kinetix 6000 Drive System Error Codes troubleshooting on page 134 . |

## Table 104 - Comm Status Indicator

| Comm Status Indicator Drive Status                          |                                                                                                                         | Potential Cause Possible Resolution                                                                                             |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Off  No communication (1)                                   |                                                                                                                         | Loose fiber-optic connection. Verify proper fiber-optic cable connections. Broken fiber-optic cable. Replace fiber-optic cable. |
| Flashing green Establishing communication                   | System is still in the process of establishing Sercos communication.  Node address setting on the drive module does not | Wait for steady green indicator.                                                                                                |
| Steady green Communication ready No faults or failures. N/A |                                                                                                                         |                                                                                                                                 |

## Table 105 - Bus Status Indicator

| Bus Status Indicator Bus Status Condition   |                                                 |                                                                                                                                                                                                                                                     |
|---------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off                                         | No power or DC bus is not present.              | • Normal when bus power is not applied. • Fault exists, refer to seven-segment error code and Kinetix 6000 Drive System Error Codes troubleshooting on page 134 . • Follower IAM module is not configured as CommonBus Follow in the Logix Designer |
| Flashing green                              | Bus power is present, axis disabled. No faults. | Normal when: • 24V is not applied to Hardware Enable Input (IOD-2). • MSO instruction is not commanded in the Logix Designer application.                                                                                                           |
| Steady green                                | Bus power is present, axis enabled. No faults.  | Normal when: • 24V is applied to Hardware Enable Input (IOD-2). • MSO instruction is commanded in the Logix Designer application.                                                                                                                   |

## Shunt Module Status Indicators

Each of the shunt module status indicators provide specific troubleshooting information.

Table 106 - General Shunt Module Troubleshooting

|       |                                       | Module Status Under These Conditions                                                                                                                                                                                                         |
|-------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shunt |                                       | Fault is latched. Until fault condition is corrected and cleared.                                                                                                                                                                            |
| Shunt | Fault is cleared.                     | • Using MASR, MAFR, MGSR instructions or the HIM (red stop button). • Only after the DC bus is discharged (bus status indicator is flashing). • Drive must be configured with 2094-BSP2 shunt module or Bulletin 1394 external shunt module. |
| Shunt | Disabled (for DC bus regulation).     | • When the 2094-BSP2 shunt module is used on a 230V system. • When either 230V or 460V system is configured with a Bulletin 1394 external shunt module. • When configured in Common-bus Follower mode.                                       |
| Shunt | Enabled to discharge the DC bus.      | IAM/AM Drive (IAM or leader IAM module) three-phase power is removed.                                                                                                                                                                        |
| Shunt | Disabled from discharging the DC bus. | When configured in Common-bus Follower mode.                                                                                                                                                                                                 |

## IMPORTANT

Under some fault conditions, two reset commands can be required to clear drive and shunt module faults.

Table 107 - Bus Status Indicator

|                                                                                                         | Bus Status Indicator Status Potential Cause Possible Resolution                                         |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Flashing Normal condition when control power is applied and bus voltage is less than 60V DC. N/A        | Flashing Normal condition when control power is applied and bus voltage is less than 60V DC. N/A        |
| Steady Green Normal condition when control power is applied and bus voltage is greater than 60V DC. N/A | Steady Green Normal condition when control power is applied and bus voltage is greater than 60V DC. N/A |
| Off Control power is not present. Internal power supply failure. Replace shunt module.                  |                                                                                                         |

## Table 108 - Temperature Fault Status Indicator

| Over-Temp Fault Indicator   |                                                                                |                                                | Status Potential Cause Possible Resolution                                                        |
|-----------------------------|--------------------------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------|
|                             | Off Normal condition. N/A                                                      | Off Normal condition. N/A                      |                                                                                                   |
| Steady Red                  | Shunt module internal temperature exceeds operating temperature specification. | Shunt module fan failed. Replace shunt module. |                                                                                                   |
| Steady Red                  | Shunt module internal temperature exceeds operating temperature specification. | Shunt module temperature exceeds rating.       | • Wait for shunt module to cool. • Reset faults. • Verify IAM module bus regulator configuration. |
| Steady Red                  | External over temperature condition.                                           | External temperature switch is open.           | • Wait for shunt module to cool. • Reset faults. • Verify IAM module bus regulator configuration. |
| Steady Red                  | External over temperature condition.                                           | TS jumper is not present. Install jumper.      |                                                                                                   |

## Table 109 - Shunt Fault Status Indicator

|                                              |                                                                                                    | Shunt Fault Indicator Status Potential Cause Possible Resolution                                 |
|----------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Off Normal condition N/A                     | Off Normal condition N/A                                                                           |                                                                                                  |
| Shorted internal or external shunt resistor. | Mis-wired shunt jumper or other short on RC connector.  Mis-wired (shorted) external shunt wiring. | Steady Red  • Correct mis-wire (shorted) condition. • If anomaly persists, replace shunt module. |

## Table 110 - All Shunt Module Status Indicators

| Shunt Module Status Indicator                |                                                   |                                | Status Potential Cause Possible Resolution                  |
|----------------------------------------------|---------------------------------------------------|--------------------------------|-------------------------------------------------------------|
| • Bus Status • Over-Temp Fault • Shunt Fault | All three status indicators flash simultaneously. | Shunt module hardware failure. | • Cycle power. • If anomaly persists, replace shunt module. |

## General System Anomalies

## Table 111 - General System Anomalies

|                             |                                                                                                                                                                     | Condition Potential Cause Possible Resolution                                                                                      |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Axis or system is unstable. | The position feedback device is incorrect or open. Check wiring.                                                                                                    |                                                                                                                                    |
| Axis or system is unstable. | Unintentionally in Torque mode.                                                                                                                                     | Check to see what primary operation mode was programmed.                                                                           |
| Axis or system is unstable. |                                                                                                                                                                     | Motor tuning limits are set too high. Run Tune in the Logix Designer application.                                                  |
| Axis or system is unstable. | Position loop gain or position controller acceleration or deceleration rate is improperly set.                                                                      | Run Tune in the Logix Designer application.                                                                                        |
| Axis or system is unstable. | Improper grounding or shielding techniques are causing noise to be transmitted into the position feedback or velocity command lines, causing erratic axis movement. | Check wiring and ground.                                                                                                           |
| Axis or system is unstable. | Motor Select limit is incorrectly set (servo motor is not matched to axis module).                                                                                  | • Check setups. • Run Tune in the Logix Designer application.                                                                      |
| Axis or system is unstable. | Mechanical resonance.                                                                                                                                               | Notch filter or output filter can be required (refer to Axis Properties dialog box, Output tab in the Logix Designer application). |

These anomalies do not always result in a fault code, but can require troubleshooting to improve performance.

Table 111 - General System Anomalies (Continued)

|                                                                      |                                                                                                                                                                                                                                                             | Condition Potential Cause Possible Resolution                                                                                               |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| You cannot obtain the motor acceleration/deceleration that you want. |                                                                                                                                                                                                                                                             | Torque Limit limits are set too low. Verify that current limits are set properly.                                                           |
| You cannot obtain the motor acceleration/deceleration that you want. | Incorrect motor selected in configuration.                                                                                                                                                                                                                  | Select the correct motor and run Tune in the Logix Designer application again.                                                              |
| You cannot obtain the motor acceleration/deceleration that you want. | The system inertia is excessive.                                                                                                                                                                                                                            | • Check motor size versus application need. • Review servo system sizing.                                                                   |
| You cannot obtain the motor acceleration/deceleration that you want. | The system friction torque is excessive.                                                                                                                                                                                                                    | Check motor size versus application need.                                                                                                   |
| You cannot obtain the motor acceleration/deceleration that you want. | Available current is insufficient to supply the correct acceleration or deceleration rate.                                                                                                                                                                  | • Check motor size versus application need. • Review servo system sizing.                                                                   |
| You cannot obtain the motor acceleration/deceleration that you want. |                                                                                                                                                                                                                                                             | Acceleration limit is incorrect. Verify limit settings and correct them, as necessary.                                                      |
| You cannot obtain the motor acceleration/deceleration that you want. |                                                                                                                                                                                                                                                             | Velocity Limit limits are incorrect. Verify limit settings and correct them, as necessary.                                                  |
| Motor does not respond to a velocity command.                        | The axis cannot be enabled for 1.5 seconds after disabling.                                                                                                                                                                                                 | Disable the axis, wait for 1.5 seconds, and enable the axis.                                                                                |
| Motor does not respond to a velocity command.                        | Enable signal has not been applied or the enable wiring is incorrect.                                                                                                                                                                                       | • Check the controller. • Check the wiring.                                                                                                 |
| Motor does not respond to a velocity command.                        | The motor wiring is open. Check the wiring.                                                                                                                                                                                                                 |                                                                                                                                             |
| Motor does not respond to a velocity command.                        | The motor thermal switch has tripped.                                                                                                                                                                                                                       | • Check for a fault. • Check the wiring.                                                                                                    |
| Motor does not respond to a velocity command.                        | The motor has malfunctioned.                                                                                                                                                                                                                                | Repair or replace the motor.                                                                                                                |
| Motor does not respond to a velocity command.                        | The coupling between motor and machine has broken (for example, the motor moves, but the load/machine does not).                                                                                                                                            | Check and correct the mechanics.                                                                                                            |
| Motor does not respond to a velocity command.                        | Primary operation mode is set incorrectly. Check and properly set the limit.                                                                                                                                                                                |                                                                                                                                             |
| Motor does not respond to a velocity command.                        | Velocity or current limits are set incorrectly. Check and properly set the limits.                                                                                                                                                                          |                                                                                                                                             |
| Presence of noise on command or motor feedback signal wires.         | Recommended grounding per installation instructions have not been followed.                                                                                                                                                                                 | • Verify grounding. • Route wire away from noise sources. • Refer to System Design for Control of Electrical Noise, publication GMC-RM001 . |
| Presence of noise on command or motor feedback signal wires.         | Line frequency present.                                                                                                                                                                                                                                     | • Verify grounding. • Route wire away from noise sources.                                                                                   |
| Presence of noise on command or motor feedback signal wires.         | Variable frequency can be velocity feedback ripple or a disturbance caused by gear teeth or ballscrew balls, for example. The frequency can be a multiple of the motor power transmission components or ballscrew speeds resulting in velocity disturbance. | • Decouple the motor for verification. • Check and improve mechanical performance, for example, the gearbox or ballscrew mechanism.         |
| No rotation                                                          | The motor connections are loose or open. Check motor wiring and connections.                                                                                                                                                                                |                                                                                                                                             |
| No rotation                                                          | Foreign matter is lodged in the motor. Remove foreign matter.                                                                                                                                                                                               |                                                                                                                                             |
| No rotation                                                          |                                                                                                                                                                                                                                                             | The motor load is excessive. Verify the servo system sizing.                                                                                |
| No rotation                                                          |                                                                                                                                                                                                                                                             | The bearings are worn. Return the motor for repair.                                                                                         |
| No rotation                                                          | The motor brake is engaged (if supplied).                                                                                                                                                                                                                   | • Check brake wiring and function. • Return the motor for repair.                                                                           |
| No rotation                                                          | The motor is not connect to the load. Check coupling.                                                                                                                                                                                                       |                                                                                                                                             |
| Motor overheating                                                    | The duty cycle is excessive.                                                                                                                                                                                                                                | Change the command profile to reduce acceleration or deceleration or increase time.                                                         |
| Motor overheating                                                    | The rotor is partially demagnetized causing excessive motor current. Return the motor for repair.                                                                                                                                                           |                                                                                                                                             |

Table 111 - General System Anomalies (Continued)

|                                                                                             | Condition Potential Cause Possible Resolution                                                                                           |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Abnormal noise                                                                              | Motor tuning limits are set too high. Run Tune in the Logix Designer application.                                                       |
| Abnormal noise                                                                              | Loose parts are present in the motor. • Remove the loose parts. • Return motor for repair. • Replace motor.                             |
| Abnormal noise                                                                              | Through bolts or coupling is loose. Tighten bolts.                                                                                      |
| Abnormal noise                                                                              | The bearings are worn. Return motor for repair.                                                                                         |
| Abnormal noise                                                                              | Mechanical resonance. Notch filter can be required (refer to Axis Properties dialog box, Output tab in the Logix Designer application). |
| Erratic operation - Motor locks into position, runs without control or with reduced torque. | Motor power phases U and V, U and W, or V and W reversed. Check and correct motor power wiring.                                         |
| Erratic operation - Motor locks into position, runs without control or with reduced torque. | Sine, Cosine or Rotor leads are reversed in the feedback cable connector. Check and correct motor feedback wiring.                      |

## Logix 5000/Drive Fault Behavior

These fault actions are configurable from the Axis Properties dialog box, Fault Actions tab in the Logix Designer application.

Table 112 - Drive Fault Action Definitions

| Drive Fault Action Definition   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shutdown                        | The drive disables the axis as defined in Logix 5000/Drive Fault Behavior ,  Table 113 . In addition, the axis in Logix Designer enters the Shutdown state, which disables any axes that are using this axis as a camming or gearing master. In addition, the AxisHomedStatus tag for the faulted axis is cleared. Shutdown is the most severe action to a fault and it is usually reserved for faults that could endanger the machine or operator if power is not removed as quickly as possible. |
|                                 | Disable Drive The drive disables the axis as defined in Logix 5000/Drive Fault Behavior ,  Table 113 .                                                                                                                                                                                                                                                                                                                                                                                             |
| Stop Motion                     | The axis decelerates at the maximum deceleration rate (set in the Logix Designer application>Axis Properties>Dynamics tab). Once the axis has come to a stop, the servo loops remain enabled but no further motion can be generated until the fault is reset. This is the gentlest stopping mechanism in response to a fault. It is usually used for less severe faults.                                                                                                                           |
| Status Only                     | The drive continues to operate. Status is provided by the seven-segment fault status indicator, drive status indicator, and DPI (if used). The application program must handle any motion faults. In general, use this setting in applications where the standard fault actions are not appropriate.                                                                                                                                                                                               |

Only selected faults are programmable. In the Logix 5000/Drive Fault Behavior table on page 143, the controlling attribute is given for programmable fault actions. All faults that are not configurable have a fault action of Shutdown.

Figure 84 - Axis Properties - Fault Actions Tab

Drive Fault Action/Attribute for Motor Overtemp fault (E04).

Table 113 - Logix 5000/Drive Fault Behavior

| Logix 5000 Fault Message (HIM Message)        | Error Code   | Description                                                                                                                                                                                                                                                                                                  | Drive Fault Action/ Attribute               | Logix Designer Programmable Fault Action?   |
|-----------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|
| BusUndervoltageFault (Blown fuse)             |              | E00 A blown fuse was detected in the inverter pcb.                                                                                                                                                                                                                                                           | Coast/Disable (open contactor enable relay) | No                                          |
| MotorOvertempFault (Motor Overtemp)           | E04 (1)      | The motor thermal switch was tripped. Firmware I 2 t protection does not generate a fault, rather it dynamically folds back current when 110% of motor rating is reached. Setting the Motor Thermal fault action to Status Only or Stop Motion bypasses the foldback behavior and allows the fault to occur. | N/A                                         | Yes Motor Thermal                           |
| DriveOvercurrentFault (Power Fault)           |              | E05 An instantaneous over-current was detected in the inverter power section.                                                                                                                                                                                                                                | Coast/Disable (open contactor enable relay) | No                                          |
| HardOvertravelFault (+/- Hard Overtravel)     | E06          | Axis moved beyond the physical travel limits in the positive/negative direction. This fault can be configured for status only.                                                                                                                                                                               | Decel/Disable                               | Yes Hard Overtravel                         |
| MotFeedbackFault (Motor Feedback Loss)        |              | E07 The feedback wiring is open, shorted or missing. Coast/Disable No                                                                                                                                                                                                                                        |                                             |                                             |
| BusUndervoltageFault (Bus Under Voltage)      | E09          | With 3-phase present, the DC bus voltage is below limits. The trip point is 275V and 137V DC for 460V/230V drives respectively.                                                                                                                                                                              | Coast/Disable (open contactor enable relay) | No                                          |
| BusUndervoltageFault (Bus Under Voltage)      | E09          | DC bus voltage is below limits when any axis on common-bus follower power rail was enabled.                                                                                                                                                                                                                  | Coast/Disable (open contactor enable relay) | No                                          |
| DriveOvervoltageFault (Bus Overvoltage)       | E10          | The DC bus voltage is above limits. The trip point is 820V and 410V DC for 460V/230V drives respectively.                                                                                                                                                                                                    | Coast/Disable (open contactor enable relay) | No                                          |
| MotFeedbackFault (Illegal Hall State)         |              | E11 State of Hall feedback inputs in incorrect. Coast/Disable No                                                                                                                                                                                                                                             |                                             |                                             |
| SoftovertravelFault (+/- Software Overtravel) | E16          | Axis position exceeded maximum software setting in the positive/negative direction. This fault can be configured for status only.                                                                                                                                                                            | Decel/Disable                               | Yes Soft Overtravel                         |
| OverSpeedFault (Overspeed Fault)              | E18          | Axis speed has reached 150% of the maximum rated setting. The 100% trip point is dictated by the lesser of the user velocity limits or the motor rated base speed.                                                                                                                                           | Coast/Disable No                            |                                             |
| PositionErrorFault (Follow Error)             | E19          | Axis position error limit has been exceeded. This fault can be configured for status only.                                                                                                                                                                                                                   | Decel/Disable                               | Yes Position Error                          |

<!-- image -->

Table 113 - Logix 5000/Drive Fault Behavior (Continued)

| Logix 5000 Fault Message (HIM Message)      | Error Code  Description                                                                                                                                                             | Drive Fault Action/ Attribute               | Logix Designer Programmable Fault Action?   |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|
| MotFeedbackFault (Mtr Fdbk AQB)             | E20 Motor encoder has encountered an illegal state transition. Coast/Disable No                                                                                                     |                                             |                                             |
| AuxFeedbackFault (Aux Feedback Comm)        | E21  Communication was not established with an intelligent (Stegmann) encoder on the Auxiliary feedback port.                                                                       | Decel/Disable No                            |                                             |
| MotFeedbackFault (Motor Feedback Comm)      | E30  Communication was not established with an intelligent (Stegmann) encoder on the Motor feedback port.                                                                           | Decel/Disable No                            |                                             |
| DriveHardFault                              | E31  Excessive motor shaft movement during power up, Sercos ring phase-up, or after a fault reset.                                                                                  | Coast/Disable No                            |                                             |
| GroundShortFault (Ground Fault)             | E34 Excessive ground current in the converter was detected.                                                                                                                         | Coast/Disable (open contactor enable relay) | No                                          |
| DriveUndervoltageFault (Precharge Fault)    | E35 The converter precharge cycle has failed.                                                                                                                                       | Coast/Disable (open contactor enable relay) | No                                          |
| DriveOvertempFault (System Overtemperature) | E36 (2)  Converter internal temperature limit exceeded.                                                                                                                             | Coast/Disable (open contactor enable relay) | No                                          |
| PowerPhaseLossFault (Phase Loss Flt)        | One or two phases of the input AC power are missing.                                                                                                                                | Coast/Disable (open contactor enable relay) | No                                          |
| PowerPhaseLossFault (Phase Loss Flt)        | • All phases of the input AC power are missing. • Axis was enabled when main (three-phase) power was removed. • Common-bus follower axis was enabled when DC bus power was removed. | Decel/Disable                               | No                                          |
| SercosFault (Sercos Ring Flt)               | E38 The Sercos ring is not active after being active and operational. Decel/Disable No                                                                                              |                                             |                                             |
| DriveHardFault (Self Sense Flt)             | E39 Self-sensing commutation fault detected. Coast/Disable No                                                                                                                       |                                             |                                             |
| DriveEnableInputFault (Drive Enable Flt)    | E43 Generated when Enable input switches off when drive is enabled. Decel/Disable                                                                                                   |                                             | Yes Drive Enable Input                      |
| DriveHardFault (Safe-Off HW Flt)            | E49 Safe torque-off function mismatch. Drive does not allow motion. Refer to the Kinetix Safe Torque-off Feature Safety Reference Manual, publication GMC RM002, for more information. Applies to 2094-xCxx-Mxx-S IAM and 2094- xMxx-S AM modules with safe torque-off feature.                                                                                                                                                                                     | Coast/Disable (open contactor enable relay) | No                                          |
| SercosFault (Sercos Same ADDR)              | E50 Duplicate node address detected on Sercos ring. Decel/Disable No                                                                                                                |                                             |                                             |
| DriveHardFault (Ifbk HW Fault)              | E54 Current feedback hardware fault detected.                                                                                                                                       | Coast/Disable (open contactor enable relay) | No                                          |
| OverSpeedFault                              | E55 The velocity error limit has been exceeded. Coast/Disable No                                                                                                                    |                                             |                                             |
| DriveHardFault (Unknown Axis)               | E60 Invalid module type identified by firmware when applying power.                                                                                                                 | Coast/Disable (open contactor enable relay) | No                                          |
| AuxFeedbackFault (Aux Fdbk AQB)             | E61 Auxiliary encoder has encountered an illegal state transition. Coast/Disable No                                                                                                 |                                             |                                             |
| AuxFeedbackFault (Aux Fdbk Loss)            | E62 The feedback wiring is open, shorted or missing. Coast/Disable No                                                                                                               |                                             |                                             |
| AuxFeedbackNoise (Aux Fdbk Noise)           | E63 Presence of noise on auxiliary feedback cable.                                                                                                                                  | Coast/Disable                               | Yes Feedback Noise                          |
| MotorFeedbackNoise (Mtr Fdbk Noise)         | E64 Presence of noise on motor feedback cable.                                                                                                                                      | Coast/Disable                               | Yes Feedback Noise                          |

Table 113 - Logix 5000/Drive Fault Behavior (Continued)

| Logix 5000 Fault Message (HIM Message)                                     | Error Code  Description                                                                                                                                                                                                                                                                                         | Drive Fault Action/ Attribute               | Logix Designer Programmable Fault Action?   |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|
| No Fault Message (condition indicated by on-screen message) (Hookup Fault) | E65 Hookup procedure failed. Coast/Disable No                                                                                                                                                                                                                                                                   |                                             |                                             |
| No Fault Message (condition indicated by on-screen message) (Atune Flt)    | E66 Autotune procedure failed. Coast/Disable No                                                                                                                                                                                                                                                                 |                                             |                                             |
| DriveHardFault (Task init)                                                 | E67 Operating system failed.                                                                                                                                                                                                                                                                                    | Coast/Disable (open contactor enable relay) | No                                          |
| DriveHardFault (SCANport Comm)                                             | E68 DPI communication failed. Decel/Disable No                                                                                                                                                                                                                                                                  |                                             |                                             |
| DriveHardFault (Objects Init)                                              | E69 Nonvolatile memory attribute out of range.                                                                                                                                                                                                                                                                  | Coast/Disable (open contactor enable relay) | No                                          |
| DriveHardFault (NV Mem Init)                                               | E70 Nonvolatile memory corrupted.                                                                                                                                                                                                                                                                               | Coast/Disable (open contactor enable relay) | No                                          |
| DriveHardFault (Memory Init)                                               | E71 RAM or nonvolatile memory validation failure.                                                                                                                                                                                                                                                               | Coast/Disable (open contactor enable relay) | No                                          |
| DriveOvertempFault (Drive Overtemp)                                        | E72 Inverter temperature limit exceeded. Firmware I 2 t protection does not generate a fault, rather it dynamically folds back current when 110% of drive rating is reached. Setting the Drive Thermal fault action to Status Only or Stop Motion bypasses the foldback behavior and allows the fault to occur. | N/A                                         | Yes Drive Thermal                           |
| Communicate (Backplane Comm)                                               | E73 Power rail backplane CAN communication failed. Decel/Disable No                                                                                                                                                                                                                                             |                                             |                                             |
| DriveOvercurrentFault (Bus OverCurrent)                                    | E74 The converter has exceeded its converter rating.                                                                                                                                                                                                                                                            | Coast/Disable (open contactor enable relay) | No                                          |
| DriveOvervoltageFault (Shunt Time Out)                                     | E75 The IAM/AM module or shunt module has exceeded its shunt resistor continuous rating. SHUTDOWN for IAM module, DISABLE for AM module. IAM module provides fault handling for shunt module.                                                                                                                   | Coast/Disable (open contactor enable relay) | No                                          |
| DriveHardFault (Can Init)                                                  | E76 Either DPI or backplane CAN initialization failure.                                                                                                                                                                                                                                                         | Coast/Disable (open contactor enable relay) | No                                          |
| DriveHardFault (Module Mismatch)                                           | E77  Generated by IAM module if the power rating of an AM module on the same power rail does not match with IAM module input power rating.                                                                                                                                                                      | Coast/Disable (open contactor enable relay) | No                                          |
| DriveHardFault Sercos Init                                                 | E78 Control hardware fault detected.                                                                                                                                                                                                                                                                            | Coast/Disable (open contactor enable relay) | No                                          |
| DriveOvervoltageFault (Shunt Module Flt)                                   | E79  Power rail mounted shunt module fault. Displayed on IAM module seven segment fault status indicator.                                                                                                                                                                                                                                                                                                                 | Coast/Disable (open contactor enable relay) | No                                          |
| HardwareFault (CPLD Flt)                                                   | E80 Control hardware fault detected.                                                                                                                                                                                                                                                                            | Coast/Disable (open contactor enable relay) | No                                          |

Table 113 - Logix 5000/Drive Fault Behavior (Continued)

| Logix 5000 Fault Message (HIM Message)   | Error Code   | Description                                                             | Drive Fault Action/ Attribute               | Logix Designer Programmable Fault Action?   |
|------------------------------------------|--------------|-------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------|
| HardwareFault (Common Bus Flt)           | E81          | Common-bus follower IAM module detected AC input power being applied.   | Coast/Disable (open contactor enable relay) | No                                          |
| HardwareFault (Precharge Timeout Flt)    | E90          | Precharge resistor power exceeds the resistor rating.                   | Coast/Disable (open contactor enable relay) | No                                          |
| IPIMFault (IPIM Module Flt)              |              | E95 A fault has occurred in one or more IPIM modules on the power rail. | Coast/Disable (open contactor enable relay) | No                                          |

## Before You Begin

## Remove Kinetix 6000 Drive Modules

<!-- image -->

## Remove and Replace the Kinetix 6000 Drive Modules

This chapter provides remove and replace procedures for your Kinetix® 6000 drive system components.

| Topic Page                             |
|----------------------------------------|
| Before You Begin 147                   |
| Remove Kinetix 6000 Drive Modules 147  |
| Replace Kinetix 6000 Drive Modules 148 |
| Remove the Power Rail 149              |
| Replace the Power Rail 150             |

<!-- image -->

ATTENTION: This drive contains electrostatic discharge (ESD) sensitive parts and assemblies. You are required to follow static-control precautions when you install, test, service, or repair this assembly. If you do not follow ESD control procedures, components can be damaged. If you are not familiar with static control procedures, refer to Guarding Against Electrostatic Damage, publication 8000-4.5.2, or any other applicable ESD awareness handbook.

These tools are required before you begin removal and replacement procedures:

- Screwdriver, 3.5 mm (0.14 in.)
- Voltmeter

Follow these steps to remove the IAM, AM, and IPIM modules from the Bulletin 2094 power rail.

1. Verify that all control and input power has been removed from the system.

<!-- image -->

ATTENTION: To avoid shock hazard or personal injury, assure that all power has been removed before proceeding. This system can have multiple sources of power. More than one disconnect switch can be required to de-energize the system.

<!-- image -->

## Replace Kinetix 6000 Drive Modules

2. Wait five minutes for the DC bus to discharge completely before proceeding.

<!-- image -->

ATTENTION: This product contains stored energy devices. To avoid hazard of electrical shock, verify that all voltage on capacitors has been discharged before attempting to service, repair, or remove this unit. Do not attempt the procedures in this document unless you are qualified to do so and are familiar with solid-state control equipment and the safety procedures in publication NFPA 70E.

3. Label and remove all connectors from the IAM/AM module you are removing.

To identify each connector, refer to Figure 23 on page 47 .

4. Remove the motor cable from the cable shield clamp, as shown in these examples.
5. Loosen the mounting screw (bottom center of each module).
6. Grasp the top and bottom of the module with both hands and gently pull the module away from the connectors enough to clear the guide pins (module pivots on top bracket).
7. Lift the bracket out of the power rail slot and remove the module from the power rail.

<!-- image -->

Power Rail (side view)

<!-- image -->

This procedure also applies to Bulletin 2094-BSP2 shunt module, 2094-PRF slot-filler module, and 2094-SEPM-B24-S IPIM module.

<!-- image -->

Follow these steps to replace drives from the Bulletin 2094 power rail.

## Remove the Power Rail

1. Determine your drive module replacement.
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

The IAM module can have two or three power rail connectors and guide pins, the AM module can have one or two, all other modules have only one connector and one guide pin.

5. Use 2.26 N·m (20 lb·in) torque to tighten the mounting screw.
6. Reconnect the module connectors.
7. Reapply power to the system.
8. Verify that the system is operating properly.

<!-- image -->

Because parameter settings reside in the Logix Designer application, you do not need to perform any tuning or set-up procedures.

This procedure assumes you have removed all modules from the power rail.

Follow these steps to remove the power rail.

1. Disconnect the braided grounding strap from the grounding stud on the right side of the power rail.
2. Loosen the mounting bolts (removing the bolts is not necessary).
3. Lift the power rail up and off of the mounting bolts.

<!-- image -->

## Replace the Power Rail

This procedure assumes you do not need to change the location of the power rail on the panel and you intend to reuse the mounting bolts of the power rail you just removed.

## IMPORTANT

If you need to change the location of the power rail, or if you are installing a power rail designed for additional or fewer modules than you removed, refer to Kinetix 6000 Power Rail Installation Instructions, publication 2094-IN003 .

<!-- image -->

ATTENTION: To avoid damage to the power rail during installation, do not remove the protective covers until the module for each slot is ready for mounting.

Follow these steps to replace the power rail.

1. Align the replacement power rail over the existing mounting bolts.

## IMPORTANT

To improve the bond between the power rail and subpanel, construct your subpanel out of zinc plated (paint-free) steel.

2. Tighten the mounting bolts.
3. Reattach the braided grounding strap to the power rail grounding stud (refer to page 149).

## Interconnect Diagrams

This appendix provides wiring examples and system block diagrams for your Kinetix® 6000 drive system components.

| Topic Page                                              |
|---------------------------------------------------------|
| Interconnect Diagram Notes 151                          |
| Power Wiring Examples 152                               |
| Axis Module/Rotary Motor Wiring Examples 160            |
| Axis Module/Linear Motor/Actuator Wiring Examples 169   |
| Kinetix 6000M Integrated Drive-Motor Wiring Example 175 |
| Brake Current Example 176                               |
| System Block Diagrams 176                               |

Interconnect Diagram Notes This appendix provides wiring examples to assist you in wiring the
iidihlhiil Kinetix 6000 drive system. These notes apply to the wiring examples on the following pages.

<!-- image -->

| Note Information                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 For power wiring specifications, refer to Power Wiring Requirements on page 77 .                                                                                                                                                                                                                                                                                                                                                                                            |
| 2 For input fuse and circuit breaker sizes, refer to Circuit Breaker/Fuse Options on page 23 .                                                                                                                                                                                                                                                                                                                                                                                |
| 3 Place AC (EMC) line filters as close to the drive as possible and do not route very dirty wires in wireway. If routing in wireway is unavoidable, use shielded cable with shields grounded to the drive chassis and filter case. For AC line filter specifications, refer to the Kinetix Rotary and Linear Motion Cable Specifications, publication KNX-TD004 .                                                                                                             |
| 4 Terminal block is required to make connections.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 5 2094-BCxx-Mxx - x  (460V) IAM modules require a step-down transformer for single-phase control power input. Source the 2094-ACxx-Mxx - x  (230V) IAM module control power from the three-phase input power (line-to-line) with neither leg bonded to ground or neutral potential. The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder. |
| 6 2094-ALxxS and 2094-BLxxS and 2094-XL75S-C2 LIM modules can supply input power for up to eight axes. 2094-XL75S-C1 LIM modules can supply input power for up to sixteen axes. For common-bus systems with more than sixteen axes, multiple LIM modules (or control power transformers) are required. For Kinetix 6000M systems, the control power current needs to be calculated and the LIM module needs to be sized.                                                      |
| 7 2094-ALxxS, 2094-BLxxS, and 2094-XL75S-Cx LIM modules are capable of connecting to two IAM modules, providing each IAM module has its own line filter and the maximum current specification is not exceeded.                                                                                                                                                                                                                                                                |
| 8 Contactor coil (M1) needs integrated surge suppressors for AC coil operation. Refer to the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications, publication KNX-TD003 .                                                                                                                                                                                                                                                                           |
| 9 Drive Enable input must be opened when main power is removed, or a drive fault occurs. A delay of at least 1.0 second must be observed before attempting to enable the drive after main power is restored.                                                                                                                                                                                                                                                                  |
| 10 Cable shield clamp must be used to meet CE and UK requirements. No external connection to ground is required.                                                                                                                                                                                                                                                                                                                                                              |
| 11 Default configuration for jumper is for grounded power at user site. Ungrounded sites must jumper the bleeder resistor to prevent high electrostatic buildup. Refer to Determine the Input Power Configuration on page 66 for more information.                                                                                                                                                                                                                            |
| 12 Leave jumper between PR2 and PR3 as shown to use the internal precharge resistor. Remove jumper when external precharge/circuit is required. For more information, refer to the 8720MC Regenerative Power Supply Installation Manual, publication 8720MC-RM001 .                                                                                                                                                                                                           |
| 13  ATTENTION: Implementation of safety circuits and risk assessment is the responsibility of the machine builder. Please reference international standards IEC 62061 and ISO 13849-1 estimation and safety performance categories.                                                                                                                                                                                                                                           |

<!-- image -->

<!-- image -->

| Note Information                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 14  ATTENTION: Wiring the contactor enable relay is required. Refer to Contactor Enable Relay on page 56, for more information. The recommended minimum wire size for wiring the three-phase power enable control circuit to the contactor enable connector is 1.5 mm 2  (16 AWG). |
| 15 The Bulletin 2094 axis module referenced is either an individual axis module (catalog number 2094-xMxx - x)  x) or the same axis module that resides within an integrated axis module (catalog number 2094-xCxx-Mxx - x ).                                                      |
| 16 For motor cable specifications, refer to the Kinetix Rotary and Linear Motion Cable Specifications, publication KNX-TD004 .                                                                                                                                                     |
| 17 Wire colors are for flying-lead cable and can vary from the premolded cable connectors.                                                                                                                                                                                         |
| 18 Motor power cables (2090-XXNPMF-xxSxx and 2090-CPBM6DF-16AAxx) have a drain wire that must be folded back under the cable shield clamp.                                                                                                                                         |
| 19 MPL-A/B15xx-H…MPL-A/B45xx-H, MPL-A15xx-V/E…MPL-A2xx-V/E, MPL-A3xx-S/M…MPL-A45xx-S/M, MPM-A115xx…MPM-A130xx, MPF-A3xx…MPF-A45xx, MPS Axxx, MPAR-Axxx, MPAS-Axxx (ballscrew), and MPAS-A/Bxxx (direct drive) encoders use the +5V DC supply.                                                                                                                                                                                                                                                                                    |
| 20 MPL-B15xx-V/E…MPL-B2xx-V/E, MPL-B3xx-S/M…MPL-B9xx-S/M, MPL-A5xx, MPM-Bxx, MPM-A165xx…MPM-A215xx, MPF-Bxx, MPF-A5xx, MPS-Bxxx, MPAR-Bxxx, and MPAS-Bxxx (ballscrew) encoders use the +9V DC supply.                                                                              |
| 21 Brake connector pins are labeled plus (+) and minus (-) or F and G respectively. Power connector pins are labeled U, V, W, and GND or A, B, C, and D respectively.                                                                                                              |

## Power Wiring Examples

These examples apply to power wiring configurations with and without the Bulletin 2094 line interface module (LIM), DC common bus wiring, and shunt module wiring.

Figure 85 - Single IAM Module with 2094-AL09 or 2094-BL02 LIM Module

<!-- image -->

Figure 86 - Multiple IAM Modules with LIM Module

<!-- image -->

Figure 87 - Multiple IAM Modules with LIM Module (continued)

<!-- image -->

This configuration does not include a LIM module. You must supply input power components. The single-phase and three-phase line filters are wired downstream of fusing and the M1 contactor.

<!-- image -->

ATTENTION: Wiring the contactor enable (CED) relay is required. To avoid injury or damage to the drive, wire the contactor enable relay into your control string.

Refer to Contactor Enable Relay on page 56 for more information.

Figure 88 - IAM Module (without LIM module)

<!-- image -->

## DC Common Bus Wiring Examples

Figure 89 - Leader IAM Module with Single Follower IAM Module

<!-- image -->

Figure 90 - Leader IAM Module with Multiple Follower IAM Modules

<!-- image -->

Figure 91 - Leader IAM Module with Multiple Follower IAM Modules (continued)

<!-- image -->

* Indicates User Supplied Component

Figure 92 - 8720MC-RPS Leader Drive with Single Follower IAM Module

<!-- image -->

## Shunt Module Wiring Examples

Refer to Kinetix Rotary and Linear Motion Cable Specifications, publication KNX-TD004 for the Bulletin 1394 external shunt module catalog numbers available for the Kinetix 6000 drive systems.

## Axis Module/Rotary Motor Wiring Examples

Figure 93 - Shunt Module Wired for Internal Operation (default configuration)

<!-- image -->

Refer to the Kinetix 6000 Shunt Module Installation Instructions, publication 2094-IN004, for additional installation information.

Figure 94 - Shunt Module with External Passive Shunt

<!-- image -->

## IMPORTANT

Only passive shunts with a thermal switch are wired to the TS connector on the Kinetix 6000 shunt module. If your external passive shunt does not have a thermal switch, leave the jumper (default configuration) in place on the TS connector.

Refer to the External Shunt Module Installation Instructions, publication 2090-IN004, for additional installation information.

These examples apply to Kinetix 6000 drives with Allen-Bradley® rotary motors.

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with bayonet connectors.

IMPORTANT

<!-- image -->

The Kinetix MPL motor wiring examples on this page apply to motors equipped with bayonet connectors.

<!-- image -->

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with circular DIN (threaded) connectors.

<!-- image -->

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with circular DIN (SpeedTec) connectors.

<!-- image -->

IMPORTANT

The Kinetix MPL motor wiring examples on this page apply to motors equipped with circular DIN (SpeedTec) connectors.

## Figure 99 - AM Module Wiring Example with Kinetix MPL-B and MPM-A/B Resolver Motors

<!-- image -->

Refer to Low Profile EnDat Feedback Module Installation Instructions, publication 2090-IN020, for connector kit specifications.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

(1) When wiring the thermal switch on 1326AB (resolver-based) motors requires the use of the 2090-K6CK-D15MF Low-profile connector kit and wire extension to the power connector. Pins 16, 17, and S are filtered to prevent noise transmission back to the drive. Refer to page 98 for wiring instructions and a diagram.

<!-- image -->

## Axis Module/Linear Motor/ Actuator Wiring Examples

2094-IN007, for connector kit specifications.

These examples apply to Kinetix 6000 drives with Allen-Bradley linear motors and actuators.

<!-- image -->

2094-IN007, for connector kit specifications.

<!-- image -->

<!-- image -->

efer to Low Profile Connector Kit Installation Instructions, publication 2094-IN007, for connector kit specifications.

Table 1 - Kinetix MPAR and MPAI Electric Cylinder Power and Feedback Cables

| Electric Cylinder Cat. No.   | Fram e   | Power Cable Cat. No.                                                    | Feedback Cable Cat. No.                                                 |
|------------------------------|----------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| MPAR-A/B1xxx (series A) (1)  | 32       | 2090-XXNPMF-16Sxx (standard) or 2090-CPxM4DF-16AFxx (continuous-flex)   | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-A/B2xxx (series A) 40   |          | 2090-XXNPMF-16Sxx (standard) or 2090-CPxM4DF-16AFxx (continuous-flex)   | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-A/B1xxx (series B) 32   |          | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-A/B2xxx (series B) 40   |          | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-A/B3xxx                 | 63       | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B2xxxx                | 64       | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B3xxxx                | 83       | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B4xxxx                | 110      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B5xxxx                  | 144      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A5xxxx                  | 144      | 2090-CPxM7DF-14AAxx (standard) or 2090-CPxM7DF-14AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |

<!-- image -->

Refer to Low Profile Connector Kit Installation Instructions, publication 2094-IN007, for connector kit specifications.

<!-- image -->

Figure 108 - AM Module with Kinetix LDC or Kinetix LDL Linear Motors (flying-lead cables)

<!-- image -->

## Kinetix 6000M Integrated Drive-Motor Wiring Example

<!-- image -->

This example applies to Kinetix 6000 drives with Kinetix 6000M integrated drive-motor (IDM) systems.

ATTENTION: When using the Kinetix 6000M IDM system, with Kinetix 6000 drives, the IPIM module only forwards the safetyfeedback monitoring signals to the adjacent (downstream) drive on the power rail. To avoid personal injury due to unexpected motion, make sure that the safety-feedback connections are fed through each drive on the power rail so that safety devices can recognize when the Kinetix 6000 drive opens the feedback contactor in the cascaded safety string.

<!-- image -->

## Brake Current Example

Table 3 - Coil Currents Rated at &lt;1.0 A

| Compatible Brake Motors/Actuators  (1)                         |               |
|----------------------------------------------------------------|---------------|
| MPL/MPF-x310, MPL/MPF-x320, MPL/MPF-x330                       | 0.45…0.55 A   |
| MPL-x420, MPL-x430, MPL-x4520, MPL-x4530, MPL-x4540, MPL-x4560 | 0.576…0.704 A |
| MPF-x430, MPF-x4530, MPF-x4540                                 | 0.576…0.704 A |
| MPS-x4540, MPM-x130, MDF-SB1153, MDF-SB1304                    | 0.576…0.704 A |

The relay output of the Kinetix 6000 (MBRK± BC-5 and BC-6) is suitable for directly controlling a motor brake, subject to the relay voltage limit of 30V DC, and the relay current limit as shown below.

Table 2 - Brake Relay Current Limit

| Kinetix 6000 IAM/AM Module                                                 | Brake Current Value, max   | Brake Current Value, max   |                                      |
|----------------------------------------------------------------------------|----------------------------|----------------------------|--------------------------------------|
|                                                                            |                            |                            | Series A Series B Series C and later |
| 2094-AC05-Mxx - x, 2094-AC09-M02-x , 2094-AMP5-x, 2094-AM01-x, 2094-AM02-x | 1.0 A                      | N/A                        | 3.0 A                                |
| 2094-BC01-Mxx - x, 2094-BC02-M02-x , 2094-BMP5-x, 2094-BM01-x, 2094-BM02-x | 1.0 A                      | 3.0 A                      | 3.0 A                                |
| 2094-AC16-M03-x, 2094-AC32-M05-x ,  2094-AM03-x, 2094-AM05-x               | 1.3 A N/A                  |                            | 3.0 A                                |
| 2094-BC04-M03-x, 2094-BC07-M05-x, x, 2094-BM03-x, 2094-BM05-x              |                            | 3.0 A 3.0 A                | 3.0 A                                |

Coil Current Compatible Brake Motors Coil Current

MPL-x1510, MPL-x1520, MPL-x1530 0.43…0.53 A TLY-A110T-H, TLY-A120T-H, and TLY-A130T-H 0.18…0.22 A

MPL-x210, MPL-x220, MPL-x230 0.46…0.56 A TLY-A220T-H and TLY-A230T-H 0.333…0.407 A

MPS-x330, MPM-x115, MDF-SB1003 1326AB-B4xxx

Table 4 - Coil Currents Rated at &gt;1.0 A and   1.3 A

| TLY-A2530P-H, TLY-A2540P-H, and TLY-A310M-H 0.351…0.429 A   |
|-------------------------------------------------------------|
| 0.88 A                                                      |
| F-4030, F-4050, and F-4075 0.69 A                           |

Coil Current Compatible Brake Motors Coil Current

MPF-x540, MPS-B560, MPM-x165 1326AB-B5xxx, and 1326AB-B7xxx

| Compatible Brake Motors  (1)             |             |
|------------------------------------------|-------------|
| MPL-xB520, MPL-xB540, MPL-x560, MPL-x580 | 1.05…1.28 A |

Table 5 - Coil Currents Rated at &gt;1.3 A and   3.0 A

| Compatible Brake Motors Coil Current     |
|------------------------------------------|
| MPL-B640, MPL-B660, MPL-B680 1.91…2.19 A |
| MPL-B860, MPL-B880 2.05…2.50 A           |
| MPM-x215 1.84…2.25 A                     |
| MPL-B960, MPL-B980 N/A                   |

IMPORTANT Because the coil current for MPL-B960 and MPL-B980 motors is rated 3.85…4.70 A, an external relay must be used.

This section provides block diagrams of the Kinetix 6000 drive modules. For block diagrams of the LIM module and RBM module, refer to Additional Resources on page 10. for the documentation available for those products.

## System Block Diagrams

| F-6100, F-6200, and F-6300 1.30 A   |
|-------------------------------------|
| 1.20 A                              |

Figure 110 - IAM/AM Module (inverter) Block Diagram

<!-- image -->

Figure 111 - IAM Module (converter) Block Diagram

<!-- image -->

Figure 112 - Shunt Module Block Diagram

<!-- image -->

## Notes:

## Upgrade Kinetix 6000M System Firmware

## Upgrade Drive Firmware with ControlFLASH Software

## Upgrade the Drive Firmware

This appendix provides procedures for upgrading Kinetix® 6000 drive firmware by using ControlFLASH™ or DriveExplorer™ software.

| Topic Page                                            |
|-------------------------------------------------------|
| Upgrade Kinetix 6000M System Firmware 181             |
| Upgrade Drive Firmware with ControlFLASH Software 181 |

Upgrading firmware for the Kinetix 6000M integrated drive-motor (IDM) system is done by using ControlFLASH software. The procedure for upgrading the IDM units uses the Sercos interface, similar to the axis modules. However, upgrading firmware on the IPIM module is accomplished over the EtherNet/ IP™ network.

IMPORTANT

DriveExplorer software does not apply to Kinetix 6000M firmware upgrades.

For the firmware upgrade procedure specific to the IDM system, refer to the Kinetix 6000M Integrated Drive-Motor System User Manual, publication 2094-UM003 .

Upgrading axis module firmware by using ControlFLASH software involves configuring your controller communication, selecting the drive to upgrade, and upgrading the firmware.

## Before You Begin

You need the following software and information before you begin.

| Description Cat. No.                                             | Firmware Revision or Software Version                            |                                                                  |
|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| RSLogix 5000®software or Studio 5000 Logix Designer®            | RSLogix 5000software 15.x or later                              |                                                                  |
| RSLogix 5000®software or Studio 5000 Logix Designer®            | Logix Designer application 21.x or later                         |                                                                  |
| ControlLogix® Sercos module                                      | 1756-MxxSE 15.32 or later                                        |                                                                  |
| ControlLogix® Sercos module                                      | 1756-L60M03SE 15.4 or later                                      |                                                                  |
| CompactLogix™ Sercos module 1768-M04SE 15.35 or later            |                                                                  |                                                                  |
| SoftLogix™ Sercos PCI card 1784-PM16SE 15.33 or later            |                                                                  |                                                                  |
| RSLinx® software 2.50 or later                                   | RSLinx® software 2.50 or later                                   |                                                                  |
| ControlFLASH software kit (1)                                    | 4.00.09 or later                                                 |                                                                  |
| Catalog number of the targeted IAM/AM module you want to upgrade | Catalog number of the targeted IAM/AM module you want to upgrade | Catalog number of the targeted IAM/AM module you want to upgrade |
| Network path to the targeted IAM/AM module.                      | Network path to the targeted IAM/AM module.                      | Network path to the targeted IAM/AM module.                      |

<!-- image -->

- (1) Download the ControlFLASH kit from http://support.rockwellautomation.com/controlflash. Contact Rockwell Automation Technical Support at (440) 646-5800 for assistance. For more ControlFLASH information (not drive specific), refer to the ControlFLASH Firmware Upgrade Kit User Manual, publication 1756-UM105 .

## IMPORTANT

Control power must be present at CPD-1 and CPD-2 prior to upgrading your target drive.

The seven-segment status indicator on the target IAM (inverter) module or AM module must be displaying a fixed 2, 3, or 4 before beginning this procedure.

ATTENTION: To avoid personal injury or damage to equipment during the firmware upgrade due to unpredictable motor activity, do not apply three-phase AC or common-bus DC input power to the drive.

<!-- image -->

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

7. Type the IP address of your Logix 5000 Ethernet module. The IP address shown is an example. Yours will be different.
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

3. Select your drive module. In this example, the 2094-BC01-MP5 IAM module is selected.
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

13. Acknowledge the warning and click OK.
2. The Progress dialog box opens and upgrading begins.

The drive module seven-segment status indicator changes from the fixed 2, 3, or 4 to F, which indicates that upgrading is in progress.

<!-- image -->

- After the upgrade information is sent to the drive, the drive resets and performs diagnostic checking.
14. Wait for the Progress dialog box to time out.
15. The Update Status dialog box opens and indicates success or failure as described below.

<!-- image -->

16. Click OK.

<!-- image -->

## Verify the Firmware Upgrade

Follow these steps to verify your firmware upgrade was successful.

<!-- image -->

Verifying the firmware upgrade is optional.

1. Open your RSLinx software.
2. From the Communications pull-down menu, choose RSWho.
3. Expand your Ethernet node, Logix 5000 backplane, and EtherNet/IP network module.
4. Right-click the drive module and choose Device Properties.

<!-- image -->

## The Device Properties dialog box opens.

<!-- image -->

5. Verify the new firmware revision level.
6. Click Close.

## Notes:

## Before You Begin

## Calculate Total Bus Capacitance

## DC Common-bus Applications

This appendix provides integration procedures specific to Kinetix® 6000 multi-axis drive systems configured for DC common bus. The procedure involves calculating capacitance values and setting the Additional Bus Capacitance parameter by using DriveExplorer® software.

| Topic Page                                       |
|--------------------------------------------------|
| Before You Begin 189                             |
| Calculate Total Bus Capacitance 189              |
| Calculate Additional Bus Capacitance 190         |
| Bulletin 2094 Drive Capacitance Values 190       |
| Common Bus Capacitance Example 191               |
| Set the Additional Bus Capacitance Parameter 192 |

To set the Additional Bus Capacitance parameter by using the Logix Designer application, refer to Appendix E beginning on page 211 .

Calculating capacitance, as it applies to the Bulletin 2094 shunt module and Kinetix 6000M IPIM module, is also included in this appendix.

These procedures assume you have mounted and wired your Kinetix 6000 DC common-bus system.

Before you set the Additional Bus Capacitance (Add Bus Cap) parameter in DriveExplorer software or the Logix Designer application, you need to calculate these values:

- Total bus capacitance
- Additional bus capacitance

Total bus capacitance is the sum of all capacitance values for your Bulletin 2094 common-bus modules. Specifically, this includes the capacitance values for each of these modules:

- Leader IAM (converter and inverter) module
- Each AM and shunt module (if present) on the leader IAM power rail
- Each IPIM module (if present) on the leader IAM power rail
- Each follower IAM (converter and inverter) module
- Each AM module on the follower IAM power rail
- Each IPIM module (if present) on the follower IAM power rail

<!-- image -->

## Calculate Additional Bus Capacitance

## Bulletin 2094 Drive Capacitance Values

Refer to Bulletin 2094 Drive Capacitance Values on page 190 for IAM, AM, IPIM, and shunt module capacitance values.

## IMPORTANT

If total bus capacitance of your system exceeds the leader IAM module precharge rating and input power is applied, the IAM module seven-segment status indicator displays error code E90 (precharge timeout fault).

To correct this condition, you must replace the leader IAM module with a larger module or decrease the total bus capacitance by removing AM modules or IPIM modules.

Table 6 - Maximum IAM Module Bus Capacitance

| Leader IAM (200V-class) Module   | Bus Capacitance, max µF   | Leader IAM (400V-class) Modules   | Bus Capacitance, max µF   |
|----------------------------------|---------------------------|-----------------------------------|---------------------------|
| 2094-AC05-MP5-x                  | 7145                      | 2094-BC01-MP5-x                   | 4585                      |
| 2094-AC05-M01-x                  | 7145                      | 2094-BC01-M01-x                   | 4585                      |
| 2094-AC09-M02-x                  |                           | 15,295 2094-BC02-M02-x            | 8955                      |
| 2094-AC16-M03-x                  |                           | 34,400 2094-BC04-M03-x            | 8955                      |
| 2094-AC32-M05-x                  |                           | 62,825 2094-BC07-M05-x            | 17,915                    |

## IMPORTANT

If your total bus capacitance value exceeds the value in the table above, you must increase the size of the leader IAM module or decrease the total bus capacitance by removing other modules on the power rail.

Additional bus capacitance is the sum of all follower IAM, AM, and IPIM module capacitance values for your Bulletin 2094 common-bus modules. Specifically, this includes the capacitance values for each of these modules:

- Each follower IAM (converter and inverter) module
- Each AM module on the follower IAM module power rail
- Each IPIM module on the follower IAM module power rail

Enter the additional bus capacitance value in Set the Additional Bus Capacitance Parameter beginning on page 193 .

Use these tables when calculating total bus capacitance and additional bus capacitance for your Bulletin 2094 common-bus application.

Table 7 - IAM/AM (200V-class) Modules

| IAM Converter (200V class)                 | Capacitance µF   | AM Inverter (200V-class)   |   Capacitance µF |
|-----------------|------------------|----------------------------|------------------|
| 2094-AC05-MP5-x | 270              | 2094-AMP5-x                |              390 |
| 2094-AC05-M01-x | 270              | 2094-AM01-x                |              660 |
| 2094-AC09-M02-x |                  | 540 2094-AM02-x            |              780 |
| 2094-AC16-M03-x |                  | 1320 2094-AM03-x           |             1320 |
| 2094-AC32-M05-x |                  | 1980 2094-AM05-x           |             2640 |

## Common Bus Capacitance Example

Table 8 - IAM/AM (400V-class) Modules

220 2094-BM02-x

940 2094-BM03-x

1410 2094-BM05-x

| IAM Converter (400V class)                 | Capacitance µF   |
|-----------------|------------------|
| 2094-BC01-MP5-x | 110              |
| 2094-BC02-M02-x |                  |
| 2094-BC04-M03-x |                  |
| 2094-BC07-M05-x |                  |

| AM Inverter (400V-class)   |   Capacitance µF |
|----------------------------|------------------|
| 2094-BMP5-x                |               75 |
| 2094-BM01-x                |              150 |
|                            |              270 |
|                            |              840 |
|                            |             1175 |

Table 9 - Shunt Module (200/400V-class)

| Shunt Module (200/400V-class)   | Capacitance µF   |
|---------------------------------|------------------|
| 2094-BSP2 470                   |                  |

Table 10 - IPIM Module (400V-class)

| IPIM Module (400V-class)   | Capacitance µF   |
|----------------------------|------------------|
| 2094-SEPM-B24-S 840        |                  |

In this example, the sum of the leader IAM power rail modules capacitance (6530 μF) and the follower IAM power rail modules capacitance (5280 μF) equals 11,810 μF total bus capacitance.

The sum of the follower IAM module power rail equals 5280 μF additional bus capacitance.

Figure 113 - Calculating Common Bus Capacitance

<!-- image -->

## Set the Additional Bus Capacitance Parameter

In this section you set the Add Bus Cap parameter by using DriveExplorer software.

<!-- image -->

You can also set the Add Bus Cap parameter by changing IDN parameter values. Refer to Appendix E on page 211 for more information.

<!-- image -->

You can use this procedure to change other parameters too, the Analog Output parameters, for example.

The following hardware and software tools are required to provide the necessary communication link between your personal computer and the Kinetix 6000 drive system running DriveExplorer software.

Table 11 - Kinetix 6000 System Requirements

| Description Cat. No. Version            |                                    |
|-----------------------------------------|------------------------------------|
| DriveExplorer software  (1) (2)         | 9306-4EXP02ENE 2.01 or later       |
| Serial to SCANport™ adapter  (2) (3)    | 1203-SSS (Series B) 3.004 or later |
| Studio 5000 Logix Designer® application | 9324-RLD300xxE 21.0 or later       |
| RSLogix 5000®software 15.0 or later    | 9324-RLD300xxE 21.0 or later       |

<!-- image -->

ATTENTION: To avoid personal injury or equipment damage, at least one end of a Sercos fiber-optic cable must be disconnected from the drive. This makes sure that motion does not occur while changes are being made to the Add Bus Cap parameter.

## Remove Sercos Communication

Follow these steps to remove (break) Sercos communication.

1. Remove three-phase and control power from the Kinetix 6000 drive system.
2. Remove one of the Sercos fiber-optic cables. Fiber-optic cable connections (Tx and Rx) are on the top of each IAM and AM module.
3. Re-apply three-phase and control power.

## Set the Additional Bus Capacitance Parameter

Follow these steps to set the Additional Bus Capacitance parameter.

1. Start your DriveExplorer software.
2. From the Explore menu, choose Connect&gt;Local or press CTRL+L. DriveExplorer software will read your system.
3. Observe the Linear List of parameters as grouped by Node, Port, and Axis hierarchy as shown below.
4. Choose Devices&gt;Node&gt;Product and navigate to the parameter x:x:x599 as shown below.
5. Double-click the x:x:x599 Add Bus Cap parameter.

<!-- image -->

<!-- image -->

The command dialog box for parameter x599 - Add Bus Cap opens.

<!-- image -->

6. Click the Value Edit tab and enter the Add Bus Cap Value (F).
7. Click OK.

The Add Bus Cap value is changed, but not saved in nonvolatile memory.

## Save the Add Bus Cap Parameter to Nonvolatile Memory

Follow these steps to save the Add Bus Cap parameter to nonvolatile memory.

1. From the Actions menu, choose Nonvolatile Memory.

This message dialog box opens.

<!-- image -->

2. Click Save.

The changes are saved to nonvolatile memory and this cautionary message dialog box opens.

<!-- image -->

3. Click Yes.

The save to nonvolatile memory is complete and this confirmation message dialog box opens.

<!-- image -->

4. Click OK.
5. Close the DriveExplorer software.

## Verify the Parameter Changes

Follow these steps to verify your parameter change was successful.

<!-- image -->

Verifying the parameter change is optional.

1. Open your DriveExplorer software.
2. Cycle the drive control power.
3. Reconnect the drive to your DriveExplorer software and read the Add Bus Cap value just like you did in Set the Additional Bus Capacitance Parameter on page 193 .
4. Verify the new parameter value. In this example, the new value is 1780 μF.
5. Close the DriveExplorer software.

<!-- image -->

## Reconnect Sercos Communication

Follow these steps to reconnect Sercos communication.

1. Remove three-phase and control power from the Kinetix 6000 drive system.
2. Replace the Sercos fiber-optic cable removed earlier. Fiber-optic cable connections (Tx and Rx) are on the top of each IAM and AM module.
3. Re-apply three-phase and control power.

## Notes:

## Benefits

## How it Works

<!-- image -->

## Configure the Load Observer Feature

The load observer feature is a control loop inside the Kinetix® 6000 drive (firmware revision 1.124 or later) that estimates the mechanical load on the motor and compensates for it, thereby forcing the motor to behave as if it is unloaded and relatively easy to control. As a result, load observer automatically compensates for disturbances and load dynamics, such as sudden inertia/ torque changes, compliance, backlash, and resonances.

| Topic Page                                   |
|----------------------------------------------|
| Benefits 197                                 |
| How it Works 197                             |
| Configuration 198                            |
| Set Gains with Sercos IDN Write Messages 208 |
| Compensate for High Frequency Resonances 209 |

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

Table 12 - Load Observer Modes

|                                      | Mode Value Description                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      | Disabled (default) 0 Load Observer is inactive                                          | Disabled (default) 0 Load Observer is inactive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Load Observer Only 1                 | Provides a Torque Estimate only                                                         | This setting is a filtered acceleration feedback with the addition of integral action in the acceleration forward path that is active below the observer bandwidth. This greatly increases the disturbance rejection properties (stiffness) over the acceleration feedback setting. However, it is also fairly aggressive and the observer bandwidth must be decreased for stable operation.                                                                                                                                                                                                                        |
| Load Observer with Velocity Estimate | 2 Standard Operation: Provides Torque and Velocity Estimates                            | This setting combines the best of the Load Observer Only and Velocity Estimate Only settings. Separately, load observer removes error, but increases phase lag and is fairly aggressive, whereas velocity estimate provides a smooth response and reduces phase lag, but creates error. Together, they remove error and provide a smooth response. Load observer performs well in situations that require adapting to changing inertia and velocity integrator anti-windup.                                                                                                                                         |
| Velocity Estimate Only 3             | Provides a Velocity Estimate only                                                       | This setting creates a filtered velocity feedback signal that is void of phase lag. Less phase lag (delay around the loop) allows for higher performance. However, the signal is modeled at frequencies above the observer bandwidth, producing error in velocity feedback. This generates a fictitiously lower velocity error since velocity error equals velocity command minus velocity feedback. Nevertheless, the steady state error disappears when used in position mode with either the position integrator or the observer integrator. This configuration is not desirable for Velocity mode applications. |
| Acceleration Feedback 4              | Provides acceleration feedback by disconnecting Acceleration Reference to load observer | This setting creates a filtered acceleration feedback signal. This setting is fairly aggressive and the observer bandwidth must be decreased significantly for stable operation. The Load Observer Only setting is similar, but without the additional phase lag (delay) created by necessary filtering.                                                                                                                                                                                                                                                                                                            |

The following figures illustrate the high-level operation of each observer mode.

Figure 114 - Load Observer and Control Loop Signals Relationship Block Diagram

<!-- image -->

Load observer also generates a Velocity Estimate signal that you can apply to the velocity loop. The Velocity Estimate has less delay than the Velocity Feedback signal derived from the actual feedback device. It also helps to reduce high frequency output noise caused by load observer's aggressive action on the acceleration reference. Together, load observer with the Velocity Estimate setting provides the best overall performance.

You can configure the load observer feature in a variety of ways by writing to a set of configuration IDN parameters. The overall behavior of load observer is controlled by Load Observer Configuration (IDN P-431). This parameter is used to select the load observer mode. It can be set to the following values.

<!-- image -->

<!-- image -->

You can configure the load observer feature in a variety of ways by writing to a set of configuration IDN parameters. The overall behavior of load observer is controlled by Load Observer Configuration (IDN P-431). This parameter is used to select the Load Observer mode. Use it to set the IDN values listed in Table 12 on page 198

## Remaining IDN Parameter Descriptions

Load observer gains that require user interaction are Load Observer Bandwidth (Kop) and Load Observer Integral Bandwidth (Koi). They are set by IDN P-432 and IDN P-433, respectively. Guidelines for setting these gains are provided in the following sections. In general, Kop acts like a velocity integrator without windup and Koi acts a like a position integrator without windup. Typically, Koi = 0.

Figure 120 - Load Observer Gains

<!-- image -->

Load observer gains that do not require user interaction are Load Observer Feedback Gain (Kof) and the Load Observer Input Gain (Kou). They are automatically set internally based on the Load Observer Configuration. However, when in Acceleration Feedback mode, Kof can also be set manually by IDN P-434 with typical values between zero and one.

Table 13 - Load Observer Gain Parameters

|                                                 |       |                     |    | IDN Name Units Format Value, min Value, max   |
|-------------------------------------------------|-------|---------------------|----|-----------------------------------------------|
| P:0:432 Load Observer Bandwidth (Kop) Rad/s     |       | 16 bit unsigned int |  0 | 12,500  (1) (2)                               |
| P:0:433  Load Observer Integral Bandwidth (Koi) | Rad/s | 16 bit unsigned int |  0 | 65,535                                        |
| P:0:434 Load Observer Feedback Gain (Kof) – 200 |       | 16 bit unsigned int |  0 |                                               |

## IMPORTANT

You must validate the input parameter to the message instruction when executing message instructions to the attributes in Table 13 . The value being sent is interpreted by the drive as an unsigned 16-bit integer. Attempting to write negative values results in the binaryequivalent positive value being used by the drive.

The Acceleration Estimate and Torque Estimate signals are read by using IDN-435 and P-436, respectively. Definitions for these IDN parameters are given in the following table.

Table 14 - Load Observer Output Signals

|                                              |              |                   |        | IDN Name Units Format Value, min Value, max   |
|----------------------------------------------|--------------|-------------------|--------|-----------------------------------------------|
| P:0:435  Load Observer Acceleration Estimate | Acceleration | 32bit signed int  | -2  31 | 2  31  -1                                     |
| P:0:436 Load Observer Torque Estimate Torque |              | 16 bit signed int | -2  15 | 2  15  -1                                     |

When load observer and the torque low-pass filter are both enabled, and the low-pass filter bandwidth is less than 5 times the load observer bandwidth, their interaction can interfere with each other, causing instability. The lowpass filter is always limited to a bandwidth under 389 Hz in drive firmware prior to revision 1.116. As a result, IDN P-065 was added in drive firmware revision 1.116 to override the torque low-pass filter bandwidth limiting. The filter is also bypassed if the override IDN P-065 is set to 1 and the torque lowpass filter bandwidth is set to zero.

Table 15 - Torque Low-pass Filter Bandwidth

| IDN P:0:065   | Bandwidth in the Logix Designer Application  Actual Bandwidth in Drive   |
|---------------|--------------------------------------------------------------------------|
| 0 (1)         | = 0 389 Hz                                                               |
| 0 (1)         | > 0 Limited to 389 Hz                                                  |
| 1 (2)         | = 0 Filter bypassed                                                      |
| 1 (2)         | > 0 Limited to 10,430 Hz                                               |

Refer to Appendix E on page 211 for more information on changing IDN parameter values with read/write messages in the Logix Designer application.

## Out-of-Box Gain Settings

This method of setting controller gains works for unknown loads or when an auto-tune is not performed. It produces a relatively high level of performance

in 90% of motion applications. Most of the time, there is no need to perform an auto-tune procedure or further optimize gain settings.

<!-- image -->

Try this method before executing Auto-tune.

Follow these steps to configure the drive for high performance right out of the box. This procedure uses load observer to automatically account for the unknown load. As a result, you must be familiar with creating an axis in the Logix Designer application and accessing drive IDN parameters.

1. Create a new axis with type AXIS\_SERVO\_DRIVE.

If you need more information to create a new axis, refer to Configure the Kinetix 6000 Drive Modules on page 117 .

2. Click the Drive/Motor tab in the Axis Properties dialog box and add a motor.

<!-- image -->

If you need more information to add a motor, refer to Configure Axis Properties on page 121 .

3. Click the Gains tab in the Axis Properties dialog box.

The current Velocity Proportional Gain (Initial Kvp) value is used to recalculate other gain values.

<!-- image -->

4. Make the following calculations:
- a. Load Observer Bandwidth: Kop = Velocity Proportional Gain x 2.56
- b. Velocity Loop Bandwidth: Kvp = Kop/4
- c. Position Loop Bandwidth: Kpp = Kvp/4
5. Configure these settings and values on the Gains tab.
- a. Position Proportional Gain = Kpp
- b. Velocity Proportional Gain = Kvp
- c. Velocity Feedforward Gain = 100%

<!-- image -->

- d. Integrator Hold = Disabled
6. Configure these IDN parameter values.
- a. IDN P-431 = 2 (load observer with velocity estimate)
- b. IDN P-432 = Kop
- c. IDN P-433 = 0
- d. IDN P-065 = 1
7. Click the Output tab in the Axis Properties dialog box and verify these settings.
- a. Load Inertia Ratio = 0
- b. Enable Low-pass Output Filter = Unchecked
8. If required, reduce the Maximum Acceleration and Maximum Deceleration values to meet application requirements and protect the drive and motor from overload.

<!-- image -->

<!-- image -->

<!-- image -->

Acceleration limits, by default, are set to their maximum value, providing the best performance for a Load Inertia Ratio of zero. However, your application loads the motor and it will not be able to accelerate as fast.

<!-- image -->

9. Refer to Compensate for High Frequency Resonances on page 209, to tune-out resonant frequencies.

## Auto-tune Gain Settings

This procedure explains how to configure the load observer feature after running Auto-tune. This method also works for any existing set of gains where the Load Inertia Ratio is known or manually calculated, for example, when the Load Inertia Ratio &gt; 0.

<!-- image -->

Try the out-of-box method before executing Auto-tune. Refer to Outof-Box Gain Settings on page 201 .

1. Click the Tune tab in the Axis Properties dialog box and perform Autotune.

For variable inertia loads, perform Auto-tune at the point of lowest mechanical inertia. If you manually calculate the Load Inertia Ratio, use the minimum load inertia.

2. Click the Output tab in the Axis Properties dialog box and verify that the Load Inertia Ratio &gt; 0.
3. Click the Gains tab in the Axis Properties dialog box.
3. The current Position and Velocity gain values are used to recalculate other gain values.
4. Determine if the mechanical load connected to the motor is rigid or compliant.
- Rigid systems typically involve high-performance load mechanics that are tightly coupled directly to the motor shaft and there is no lost motion.

<!-- image -->

<!-- image -->

Refer to Rigid Mechanical Loads on page 205, for rigid applications.

- Everything else is compliant, including systems with belts and pulleys, long shafts, short shafts with heavy loads, and couplings and gearboxes with backlash and/or lost motion.
- Refer to Compliant Mechanical Loads on page 205, for compliant applications.

## Rigid Mechanical Loads

Follow these steps if the load is rigid.

1. Calculate the Load Observer Bandwidth. Load Observer Bandwidth: Kop = Velocity Proportional Gain
2. Configure these IDN parameter values.
- a. IDN P-431 = 2 (Load Observer with Velocity Estimate)
- b. IDN P-432 = Kop
- c. IDN P-433 = 0
- d. IDN P-065 = 1
3. If the Low-pass Output Filter is enabled, verify that the Low-pass Output Filter Bandwidth is  the Velocity Proportional Gain x 2/(2pi). Sercos IDN P-065 has an impact on how the Low-pass Output Filter functions. Refer to Table 15 on page 201 for more information.
4. Refer to Compensate for High Frequency Resonances on page 209, to tune-out resonant frequencies.

<!-- image -->

<!-- image -->

## Compliant Mechanical Loads

The compliant setting reduces all of the gains by a factor of (Load Inertia Ratio +1) and then calculates the Load Observer Bandwidth. Typically, this reduction is too conservative, making the loop response sluggish and the error too large. However, it does assure stability.

Follow these steps if the load is compliant.

1. Make the following calculations to de-tune all gains by a factor of the (Load Inertia Ratio + 1):
- a. Position Loop Bandwidth:
3. Kpp = Position Proportional Gain/(Load Inertia Ratio + 1)
- b. Position Integral Bandwidth:
5. Kpi = Position Integral Gain/(Load Inertia Ratio + 1) 2
- c. Velocity Loop Bandwidth:
7. Kvp = Velocity Proportional Gain/(Load Inertia Ratio + 1)
- d. Velocity Integral Bandwidth:
9. Kvi = Velocity Integral Gain/(Load Inertia Ratio + 1) 2

- e. Load Observer Bandwidth: Kop = Kvp
2. Configure these settings and values on the Gains tab.
- a. Set the Position Proportional Gain = Kpp
- b. Position Integral gain = Kpi
- c. Velocity Proportional Gain = Kvp
- d. Velocity Integral Gain = Kvi

<!-- image -->

<!-- image -->

To manually increase the gains by some factor to optimize the response, refer to Manual Tuning for Further Optimization on page 207 .

3. Configure these IDN parameter values.
- a. IDN P-431 = 2 (Load Observer with Velocity Estimate)
- b. IDN P-432 = Kop
- c. IDN P-433 = 0
- d. IDN P-065 = 1
4. If the Low-pass Output Filter is enabled, verify that the Low-pass Output Filter Bandwidth  Velocity Proportional Gain x 5/(2pi).
7. Sercos IDN P-065 has an impact on how the Low-pass Output Filter functions. Refer to Table 15 on page 201 for more information.
5. Refer to Compensate for High Frequency Resonances on page 209, to tune-out resonant frequencies.

<!-- image -->

## Tuning Mode Summary

This table summarizes the primary difference between the two tuning modes.

Table 16 - Tuning Mode Comparison

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

## Set Gains with Sercos IDN Write Messages

4. Manually tune the position loop.
- a. Restore the Position and Feedforward Gains to the original values to re-enable the position loop.
- b. While Jogging the axis and monitoring the Torque Reference trend, incrementally increase the following gains simultaneously and stop when the Torque Reference begins to become oscillatory or unstable:
- Position Proportional Gain = Position Proportional Gain x N
- Position Integral Gain = Position Integral Gain x N 2
- c. Decrease the gains by using the previous equations with an N = 0.5. A typical range of values for the Position Integral Gain is given: 0  Position Integral Gain  Position Proportional Gain 2 /4000

Write the Load Observer Configuration attribute and the Load Observer gains each time the drive gets initialized after applying power.

The Sercos IDN write instruction is accomplished by using RSLogix 5000® software or the Logix Designer application. Refer to Appendix E on page 211 for more information on changing IDN parameter values by using this method.

1. Upon initialization of the drive, read the INT value of the configuration of the drive at Sercos IDN P:0:431.

<!-- image -->

## Compensate for High Frequency Resonances

2. If the value is not what you want, latch it and write the new value back to the drive at the same address, again as type INT.
3. Verify the change with another Sercos IDN Read Message from IDN P:0:431.

<!-- image -->

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
3. Click the Output tab in the Axis Properties dialog box.
- a. Check Enable Notch Filter Frequency and set the Notch Filter Frequency to the resonant frequency with the largest amplitude.
- b. If multiple resonances have nearly the same amplitude, set the Notch Filter Frequency to the lowest resonant frequency.
- c. If the problem persists, also check Enable Low-pass Output Filter and set the Low-pass Output Filter Frequency to the next largest resonant frequency.
- d. Click OK.

<!-- image -->

<!-- image -->

## Before You Begin

<!-- image -->

## Change Default IDN Parameter Values

This appendix provides a procedure, specific to the Kinetix® 6000 (Sercos) drive systems, for changing IDN parameter values to non-default values when your application does not match the default configuration. The procedure also applies when one or more Kinetix 6000M IDM systems are present.

| Topic Page                      |
|---------------------------------|
| Before You Begin 211            |
| Change IDN Parameter Values 212 |

The Logix 5000™ processor contains a motion planner that sends real-time and non real-time data to the drive. This drive communication is performed via a set of Sercos interface telegrams. Each telegram has an identification or Ident (IDN) number. All parametric data, such as scaling and loop gains, and realtime loop closure information is configured this way.

## Table 17 - IDN Instruction Format in the IEC Standard Document

| IDN Number   | Name                 | Name                                     | Name                     | Name                 |
|--------------|----------------------|------------------------------------------|--------------------------|----------------------|
| IDN Number   | Function/Description | Function/Description                     | Function/Description     | Function/Description |
| IDN Number   | Length in bytes      | Minimum input value/ Maximum input value | Scaling/resolution Units |                      |

There are default parameters in the Logix 5000-to-Kinetix 6000 drive product structure you can reconfigure when the default configuration does not match the Integrated Architecture™ machine configuration.

By using this procedure, you can change the Additional Bus Capacitance value in common-bus configurations.

<!-- image -->

You can also set the Additional Bus Capacitance parameter by using DriveExplorer™ software (refer to Appendix D), the Logix Designer application, or RSLogix 5000® software, version 20.00 or later, from I/O configuration&gt;Sercos module&gt;Drive module properties&gt;Power tab (refer to Chapter 6).

Use this flowchart to determine if changing your default configuration is required.

## Change IDN Parameter Values

Figure 121 - Configuration Flowchart

<!-- image -->

In this section you follow the Configuration Flowchart on page 212 to determine if you need to use the Sercos IDN Write instruction in the Logix Designer application to change the IDN parameter values.

## Read the Present IDN Parameter Value

Follow these steps to read the present IDN value.

1. Start your Logix Designer application program.
2. Configure a Message Configuration (MSG) instruction to read your present IDN parameter values.

In this example, the Message Configuration (MSG) instruction is set to read the additional bus capacitance of your leader IAM power module.

<!-- image -->

- a. From the Message Type pull-down menu, choose Sercos IDN Read.
- b. From the Identification Number pull-down menus, choose P-0-99.
3. Click New Tag.
4. The New Tag dialog box opens.
5. Type the name of your Destination tag.

<!-- image -->

In this example, the tag name is Read\_Value.

6. Click OK.

In this example, the MSG instruction reads the P-0-99 IDN value and places it in the destination as specified by the new tag.

7. Click the Communication tab.
8. Click Browse.
9. Select the Bulletin 2094 module to read the MSG instruction.
10. Click OK.

<!-- image -->

## Calculate the New IDN Value

Changing the additional bus capacitance value requires calculations. Determine the sum of all capacitance values for the follower IAM module, each AM module, and each IPIM module on the follower IAM power rail.

Refer to Calculate Additional Bus Capacitance on page 190 for more information.

## Write the New IDN Parameter Value

Follow these steps to write the new IDN parameter value.

1. Configure a Message Configuration (MSG) instruction to write the IDN parameter value required for your application.

In this example, the Message Configuration (MSG) instruction is set to write the additional bus capacitance of your leader IAM power module.

<!-- image -->

- a. From the Message Type pull-down menu, choose Sercos IDN Write.
- b. From the Identification Number pull-down menus, choose P-0-99.
2. Click New Tag.
3. The New Tag dialog box opens.
4. Type the name of your Source tag.

<!-- image -->

In this example, the tag name is Write\_Value.

5. Click OK.

In this example, the new tag creates a source value (that you entered) that

- the MSG instruction uses to overwrite the existing P-0-099 IDN value.
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

## Notes:

## Before You Begin

## Enhanced Peak Performance

This appendix provides procedures and information, specific to Kinetix® 6000 drive systems, for enabling the peak enhancement feature in each drive.

| Topic Page                     |
|--------------------------------|
| Before You Begin 217           |
| Enhanced Peak Example 218      |
| Change the Drive Parameter 222 |

The peak current ratings of the Kinetix 6000 460V drives are configured at the factory as 150% of continuous current. However, you can program 460V (series B and later) AM modules and the equivalent IAM (inverter) modules, for up to 250% of continuous inverter current.

To achieve the enhanced peak performance, you must determine the values of maximum acceleration, deceleration, and torque. This feature is present only in the Kinetix 6000 (series B and later) drives listed in Table 18 .

Table 18 - Kinetix 6000 Series Change

| IAM Module Cat. No.                   |                               |
|---------------------------------------|-------------------------------|
| Cat. No. Series A (inverter)          | Series B and later (inverter) |
| 2094-BC01-MP5-S 2094-BMP5-S 150% 250% |                               |
| 2094-BC01-M01-S 2094-BM01-S 150% 250% |                               |
| 2094-BC02-M02-S 2094-BM02-S 150% 250% |                               |
| 2094-BC04-M03-S 2094-BM03-S 150% 250% |                               |
| 2094-BC07-M05-S 2094-BM05-S 150% 200% |                               |

The default values that populate the AXIS\_SERVO\_DRIVE properties in the Logix Designer application are calculated for each motor and drive, but assume 150% peak torque in those calculations. For the drive to command more current, you must enter new values for some of those parameters, including the following:

- TorqueLimitBipolar
- TorqueLimitPositive
- TorqueLimitNegative
- MaximumAcceleration
- MaximumDeceleration
- AccelerationLimitBipolar
- AccelerationLimitPositive
- AccelerationLimitNegative

You can access these parameters offline in the Logix Designer application Axis Properties tabs or online as sent to the drive in an SSV instruction.

<!-- image -->

## Enhanced Peak Example

To calculate the new values, you also need to determine these values:

- Drive electrical data (Motion Analyzer solution page, under Drive tab)
- Motor electrical data (Motion Analyzer solution page, under Motor tab)
- TorqueScaling (the Logix Designer application, Axis Properties, Output tab)

Figure 122 - Drive and Motor Data in Motion Analyzer Software

<!-- image -->

## IMPORTANT

The default unit in Motion Analyzer software for drive and motor current is A (0-pk). Because the example formula is in A (RMS), you must change the units in the Drive and Motor tabs to A (RMS). Pause your mouse over A (0-pk) and use the pull-down menu to change the units to A (RMS). Refer to Figure 122 for an example.

In this example, the following motor and drive combination is used:

- Drive = 2094-BC02-M02-S
- Motor = MPL-B540K

Table 19 - Example Definitions

| Description Symbol IDN Example   |               |                   |
|----------------------------------|---------------|-------------------|
| Motor continuous current (A rms  | ) I mtr, cont | S:0:0111 14.49525 |
| Motor peak current (A rms        | ) I mtr, pk   | S:0:0109 42.42641 |
| Drive continuous current (A rms  | ) I dr, cont  | S:0:0112 10.3379  |
| Drive peak current (A rms        | ) I dr, pk    | 150%: 15.5069     |
| Drive peak current (A rms        | ) I dr, pk    | 250%: 25.8094     |

Default Peak Torque Limit Value

Default TorqueLimit Values

Figure 123 - Example Torque Formula

<!-- image -->

1. Navigate to Axis Properties and click the Limits tab.
2. Overwrite the existing Peak Torque Limit (TorqueLimitBipolar) value. In this example, the calculated value is 178.1.
3. Click Set Custom Limits.
4. Overwrite the existing TorqueLimitPositive and TorqueLimitNegative values.

<!-- image -->

<!-- image -->

In this example, the calculated values are 178.1 and -178.1 (respectively). The calculated value for Torque max is the maximum value for the following:

- TorqueLimitBipolar
- TorqueLimitPositive (+)
- TorqueLimitNegative (-)

If you want to limit the torque, adjust the calculated values to a value closer to zero. The values shown are the default values for 150% peak torque with this motor and drive pair.

<!-- image -->

For more information on system configuration with your Logix 5000 controller and the Logix Designer application, refer to page 107 .

5. Click the Output tab.

<!-- image -->

The TorqueScaling and LoadInertiaRatio values are populated after an autotune. If an autotune is not possible, model the system in Motion Analyzer software and enter that value for the LoadInertiaRatio. The default value for the LoadInertiaRatio is 0.0, however for this example, a ratio of 10.20:1 is used (load inertia = 0.015 Kg-m^2).

IMPORTANT

To obtain more accurate results, performing Autotune in the Logix Designer application is recommended.

To calculate the maximum acceleration and deceleration from Torque max , use this equation.

<!-- image -->

<!-- image -->

If autotune cannot be performed, enter the data for the LoadInertiaRatio, DriveResolution, and ConversionConstant as shown in step 5 through step 9 .

6. Change the Load Inertia Ratio value to 10.2.
7. Click Apply.

The TorqueScaling values update.

<!-- image -->

8. Click the Drive/Motor tab.

<!-- image -->

The values for DriveResolution and ConversionConstant start out populated with default values, but can be changed for your specific needs. If you plan to change those values, enter the new values into the dialog boxes. Otherwise, use the defaults.

9. Click the Conversion tab.

<!-- image -->

## Enhanced Peak Example Calculation

Based on the values shown, this is the sample calculation.

<!-- formula-not-decoded -->

To provide safe headroom, this value needs to be reduced by 15% before being written to the controller. This is the sample calculation.

MaximumAcceleration = 0.85 · 0.85 · = 283.98 PU/s2 MaximumDeceleration = Accelmax Accel max

Default Acceleration and Deceleration Values

Default AccelerationLimitBipolar Value

Default AccelerationLimitPositive and AccelerationLimitNegative Values

1. Click the Dynamics tab.
2. Overwrite the existing Maximum Acceleration and Maximum Deceleration values.

<!-- image -->

In this example, the calculated values are 283.98 for each.

3. Click Calculate for the Maximum Acceleration Jerk and Maximum Deceleration Jerk fields to automatically calculate new values.
4. Adjust the new jerk values for your specific application needs. Setting the values for AccelerationLimitBipolar, AccelerationLimitPositive, and AccelerationLimitNegative requires one more calculation by using this formula.

AccelerationLimitBipolar = -AccelerationLimitNegative AccelerationLimitPositive =

<!-- formula-not-decoded -->

0.85

5. Click the Limits tab.
6. Click Set Custom Limits.
7. Overwrite the existing AccelerationLimitBipolar value. In this example, the calculated value is 668.18.
8. Overwrite the existing AccelerationLimitPositive and AccelerationLimitNegative values.

<!-- image -->

In this example, the calculated values are +668.18 and -668.18 (respectively).

9. Repeat this process for each IAM and AM module in your system.

Change the Drive Parameter Before the drive is capable of accepting a command for the new peak current
id hdihidbdl ratings, you need to change a drive parameter. This needs to be done only once, and there are two methods to perform the task.

IMPORTANT

The Sercos IDN method that uses the Logix Designer application supports automatic drive replacement (ADR).

## Sercos IDN Write Instruction

The Sercos IDN write instruction is accomplished by using the Logix Designer application. Refer to Appendix on page 211 for more information on changing IDN parameter values by using this method.

1. On initialization of the drive, read the INT value of the configuration of the drive at Sercos IDN P:0:7.
2. If the value of bit zero is zero, latch it and write the new value back to the drive at the same address, again as type INT.
3. Verify change with another Sercos IDN Read Message from IDN P:0:7 and examine bit zero.

<!-- image -->

<!-- image -->

## Refer to this Logix Designer application example.

<!-- image -->

## DriveExplorer Software

To use DriveExplorer™ software to change IDN parameter values, you must also have the 1203-SSS Serial to SCANport™ adapter. Refer to Appendix on page 189 for more information on changing IDN parameter values by using this method.

1. Connect a 1203-SSS Serial to SCANport adapter to the drive by using DriveExplorer software.
2. Change parameter P507 [Drv Peak Rating] from 150% to 250% (or 200% if applicable).
3. Save device values to nonvolatile memory.

## Before You Begin

## RBM Module Wiring Examples

<!-- image -->

## RBM Module Interconnect Diagrams

This appendix provides Bulletin 2090 Resistive Brake Module (RBM) interconnect diagrams specific to Kinetix® 6000 multi-axis servo-drive systems with and without the safe torque-off feature.

| Topic Page                     |
|--------------------------------|
| Before You Begin 225           |
| RBM Module Wiring Examples 225 |

Kinetix 6000 drives with the safe torque-off feature have the -S designation at the end of the catalog number. For example, the 2094-AM01-S AM module includes safe torque-off and the 2094-AM01 AM module does not.

These procedures assume you have installed your RBM module with the Kinetix 6000 servo-drive system. For RBM module installation instructions, refer to the Resistive Brake Module Installation Instructions, publication 2090-IN009 .

IMPORTANT

Drive firmware revision 1.071 or later is required to use the RBM module with Kinetix 6000 drives.

<!-- image -->

ATTENTION: Use the interconnection diagrams as a general recommendation of how the control circuit can be implemented. Actual applications can vary due to requirements based on the machine builders risk assessment. The machine builder must perform a risk assessment and determine a category level of safety that must be applied to the machine.

For Kinetix 6000 drive systems, you can set the delay time for your RBM module in the Logix Designer application. Refer to Configure Axis Properties on page 121 .

This example diagram shows 2094-xCxx-Mxx-S and 2094-xMxx-S drives (with safe torque-off) and 2094-ALxxS, 2094-BLxxS, and 2094-XL75S LIM modules wired with the Bulletin 2090 RBM module.

<!-- image -->

<!-- image -->

This example diagram shows 2094-xCxx-Mxx and 2094-xMxx drives (without safe torque-off) and 2094-ALxxS, 2094-BLxxS, and 2094-XL75S LIM modules wired with the Bulletin 2090 RBM module.

Figure 126 - RBM Wiring Example, Category 2 Configuration per ISO 13849

<!-- image -->

<!-- image -->

This example diagram shows 2094-xCxx-Mxx and 2094-xMxx drives (without safe torque-off) and 2094-AL09 and 2094-BL02 LIM modules wired with the Bulletin 2090 RBM module.

<!-- image -->

Figure 129 - RBM Wiring Example, Category 2 Configuration per ISO 13849 (continued)

<!-- image -->

This example diagram shows 2094-xCxx-Mxx drives (without safe torque-off) and 2094-ALxxS, 2094-BLxxS, and 2094-XL75S LIM modules wired with the Bulletin 2090 RBM module. The example continues on page 233 .

<!-- image -->

Figure 131 - RBM Wiring Example, Category 3 Configuration per ISO 13849 (continued)

<!-- image -->

This example diagram shows 2094-xCxx-Mxx drives (without safe torque-off) and 2094-AL09 and 2094-BL02 LIM modules wired with the Bulletin 2090 RBM module.

<!-- image -->

Figure 133 - RBM Wiring Example, Category 3 Configuration per ISO 13849 (continued)

<!-- image -->

## Notes:

## History of Changes

This appendix contains the new or updated information for each revision of this publication. These lists include substantive updates only and are not intended to reflect all changes. Translated versions are not always available for each revision.

## 2094-UM001L-EN-P, August 2022

## Change

Added information for Series E Kinetix 6000 Servo Drives.

## 2094-UM001K-EN-P, August 2020

## Change

Updated IAM/AM Module Series Changes with changes for Series D drives.

Updated Determine the Input Power Configuration with changes in the use of AC line filters.

Added History of Changes appendix.

## 2094-UM001J-EN-P, July 2015

## Change

| Updated the internal solid-state motor short-circuit protection rating to include 200,000 A (fuses) and 65,000 A (circuit breakers).   |
|----------------------------------------------------------------------------------------------------------------------------------------|
| Added Mersen HSJ fuses for 2094-BCxx-Mxx-S integrated axis module DC-bus power.                                                        |
| Updated absolute position examples table.                                                                                              |
| Updated auxiliary feedback encoders table with Bulletin 847H and 847T catalog numbers.                                                 |
| Added IMPORTANT information for calculating the control power current load.                                                            |
| Added error code E31.                                                                                                                  |
| Added error code E55.                                                                                                                  |
| Added error code E31 fault behavior.                                                                                                   |
| Added error code E55 fault behavior.                                                                                                   |
| Updated notes 19 and 20 with new compatibility for Kinetix MPAS linear actuators.                                                      |
| Added IMPORTANT information regarding message instruction.                                                                             |

## 2094-UM001I-EN-P, July 2015

| Change                                                                                       |
|----------------------------------------------------------------------------------------------|
| Updated Circuit Breaker/Fuse Options section                                                 |
| Updated motor feedback connector pinout tables with 5V/9V footnote                           |
| Updated auxiliary feedback connector pinout tables with 5V/9V footnote                       |
| Updated Motor Brake Relay with additional motor brake control information                    |
| Updated absolute position limit specifications to include all compatible multi-turn encoders |
| Corrected AM, BM phase error parameter values                                                |

<!-- image -->

## 2094-UM001I-EN-P, July 2015 (Continued)

| Change                                                                                                                                                    |                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Updated the input power section for consistency with other drive-family user manuals and added the impedance-grounded power configuration                 | Updated the input power section for consistency with other drive-family user manuals and added the impedance-grounded power configuration                 |
| Added Kinetix MPS motors and MPAS linear stages to the SpeedTec DIN connector tables                                                                      | Added Kinetix MPS motors and MPAS linear stages to the SpeedTec DIN connector tables                                                                      |
| Updated the ControlLogix 1756-ENxT EtherNet/IP™ module line art with new design                                                                           | Updated the ControlLogix 1756-ENxT EtherNet/IP™ module line art with new design                                                                           |
| Updated sercos optical power DIP switch settings                                                                                                          | Updated sercos optical power DIP switch settings                                                                                                          |
| Updated error code E05 possible resolutions with ‘reduce deceleration rates’                                                                              | Updated error code E05 possible resolutions with ‘reduce deceleration rates’                                                                              |
| Updated resolver motor feedback pinout with correct wire color for TS+ signal                                                                             | Updated resolver motor feedback pinout with correct wire color for TS+ signal                                                                             |
| Updated Kinetix MPAS linear stage wiring diagram with SpeedTec DIN cable catalog numbers                                                                  | Updated Kinetix MPAS linear stage wiring diagram with SpeedTec DIN cable catalog numbers                                                                  |
| Updated linear motor wiring diagram with correct motor feedback pinout                                                                                    | Updated linear motor wiring diagram with correct motor feedback pinout                                                                                    |
| Added ATTENTION statement, corrected Kinetix 6000M IDM catalog number, and added (internal) jumper circuitry to pins 1…4 of the safe torque-off connector | Added ATTENTION statement, corrected Kinetix 6000M IDM catalog number, and added (internal) jumper circuitry to pins 1…4 of the safe torque-off connector |
| Updated the Configure the Load Observer Feature appendix with changes consistent with publication MOTION-AT005.                                           | Updated the Configure the Load Observer Feature appendix with changes consistent with publication MOTION-AT005.                                           |

## 2094-UM001H-EN-P, May 2012

## Change

Studio 5000™ Logix Designer application is the rebranding of RSLogix™ 5000 software. General references to RSLogix 5000 software have been replaced by the Logix Designer application. References to specific RSLogix 5000 software versions did not change.

Updated references to safe-off (SO) as safe torque-off (STO), per EN61800-5-2.

Updated references to series A and B drives. The 230V drive modules previously labeled as series A are now series A and C. The 460V drives previously labeled as series B are now series B and C.

Added Kinetix LDAT linear thrusters to system overview table.

Added Kinetix LDAT linear thrusters to typical system installation diagrams.

Updated System Mounting Requirements for enclosure rating from IP2x to IP54.

Added AC line filter selection table.

Updated safe torque-off (STO) connector pinout table with series C descriptions for safety enable inputs.

Updated motor/resistive brake circuitry diagram and text with changes for the new solid-state relay.

Added the Kinetix LDAT linear thruster interconnect diagram with Kinetix® 6000 drive.

Added the Configure the Load Observer Feature appendix.

## 2094-UM001G-EN-P, May 2012

## Change

Added acronyms for the Kinetix 6000M integrated drive-motor (IDM) system.

Added the IPIM module to About the Kinetix 6000 Drive System.

Added the Kinetix 6000M integrated drive-motor (IDM) to typical system installation diagrams and catalog number explanation.

Added the IPIM module to Minimum Clearance Requirements.

Added the IPIM module to Establishing Noise Zones.

Added the IPIM module to Determine Mounting Order.

Revised motor power, brake, and feedback cable compatibility tables to include the MPL-A/B15xxx -xx7xAA and MPL-A/B2xxx-xx7xAA low-inertia motors and MPAR-A/B1xxx and MPAR-A/B2xxx electric cylinders with SpeedTec (M7) connectors.

Added IPIM Module Connections with summary of installation connections and links to other diagrams and publications with additional information.

Added Kinetix 6000M Integrated Drive-Motor Sercos Connections

Added Ethernet Cable Connections

Updated the introduction with an overview of IDM system configuration.

Updated the introduction with an overview of the IDM system troubleshooting

Updated existing circular DIN (SpeedTec) interconnect diagram with Bulletin MPL-A/B15xxx -xx7xAA and MPL-A/B2xxx-xx7xAA low-inertia motors with SpeedTec (M7) connectors.

Updated the Kinetix MPAI electric cylinders interconnect diagram with frame 64 and 144 cable catalog numbers.

## 2094-UM001G-EN-P, May 2012 (Continued)

## Change

Updated the Kinetix MPAR electric cylinders interconnect diagram with cable catalog number changes for SpeedTec (M7) connector

Added Kinetix 6000M Integrated Drive-Motor Wiring Example.

Added Kinetix MDF catalog numbers to Controlling a Brake Example

Added an overview for IDM system firmware upgrades.

Updated the procedure and tables with IPIM module values.

## 2094-UM001F-EN-P, March 2011

## Change

Corrected formulas used to enable enhanced-peak performance.

## 2094-UM001E-EN-P, January 2011

## Change

Updated system configuration diagrams with power rail and cable clamp redesign features.

Updated communication diagrams with drive-to-drive double-wide configurations.

Updated mounting diagrams with power rail and cable clamp redesign features.

Updated IAM and AM module illustrations with cable clamp redesign features.

Updated power cable catalog numbers with standard (non-flex) SpeedTec DIN cables.

Updated brake cable catalog numbers with standard (non-flex) SpeedTec DIN cables.

Updated feedback cable catalog numbers with standard (non-flex) SpeedTec DIN cables.

Removed Bulletin 1336 external active shunt modules. Added reference to Rockwell Automation Encompass partner solutions.

Added tables to distinguish the dimensional differences between series A and series B drives. Updated dimension drawings with power rail and cable clamp redesign features.

Updated Axis Module/Rotary Motor Wiring Examples with standard (non-flex) SpeedTec DIN motor power and feedback cables.

Updated Axis Module/Linear Motor/Actuator Wiring Examples with standard (non-flex) SpeedTec DIN motor power and feedback cables.

This new appendix provides procedures and information for enabling the peak enhancement feature.

## 2094-UM001D-EN-P, May 2010

| Change                                                               |
|----------------------------------------------------------------------|
| IAM/AM Module Series Change                                          |
| Catalog Number Explanation                                           |
| Drive Component Compatibility                                        |
| Peak Enhancement Specifications                                      |
| Set the Ground Jumper                                                |
| Kinetix MPL Motor Connectors                                         |
| Motor Power Cable Compatibility                                      |
| Motor Brake Cable Compatibility                                      |
| Motor Feedback Cable Compatibility - Bayonet Connectors              |
| Motor Feedback Cable Compatibility - Circular DIN/Plastic Connectors |
| Configure Axis Properties                                            |
| IAM Module (460V) Power Specifications (series A and B)              |
| AM Module (inverter) 460V Power Specifications (series A and B)      |
| Product Dimensions                                                   |

## 2094-UM001C-EN-P, December 2009

| Change                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pinout for the 2090-K6CK-KENDAT feedback module.                                                                                                                                                |
| Linear scaling specifications for analog outputs.                                                                                                                                               |
| Input power-cycle capability specifications.                                                                                                                                                    |
| Heidenhain EnDat encoder specifications.                                                                                                                                                        |
| Auxiliary position feedback encoder catalog numbers.                                                                                                                                            |
| Motor power cable compatibility.                                                                                                                                                                |
| Wiring motor brake connections.                                                                                                                                                                 |
| Motor and feedback cable combinations.                                                                                                                                                          |
| Wiring the 2090-K6CK-KENDAT feedback module.                                                                                                                                                    |
| Installing the fiber-optic connector bracket kit.                                                                                                                                               |
| Maximum feedback cable length specifications for Kinetix MPM rotary motors and Kinetix MPAR electric cylinders; Kinetix RDB direct-drive servo motors; LDC-Series and LDL-Series linear motors. |
| Interconnect diagrams for Kinetix MPM rotary motors and Kinetix RDB direct-drive servo motors.                                                                                                  |
| Interconnect diagrams for Kinetix MPAR electric cylinders; Kinetix LDC and Kinetix LDL linear motors.                                                                                           |
| Coil current ratings for motor brake applications.                                                                                                                                              |
| Changing default IDN parameter values using Sercos Read and Write instructions.                                                                                                                 |
| Wiring examples for Kinetix 6000 drives with and without the safe-off feature.                                                                                                                  |

## Numerics

1756-MxxSE 114

1768-M04SE 114

1784-PM16SE 114

2090-K6CK-D15F 91 , 97 , 98

2090-K6CK-D15M 91 , 97 , 98 , 161

2090-K6CK-D15MF 87 , 91 , 97 , 99 , 168

2090-K6CK-D26M 91 , 97 , 99

2090-K6CK-KENDAT 51 , 62 , 91 , 97 , 98

2094 power rail 43

26-pin I/O connector 132

## A

## AC line filters

noise reduction 39

selection 22

## acceleration

feedback 200

reference 197

acronyms 9

k

actual position feedback actuators

LDAT 172

MPAI 171

MPAR 171

MPAS 170

## additional bus capacitance

calculating 190

example 191

additional resources 10

analog outputs 55

analog test points

DAC0 131

DAC1 131

applying power 124

atune fault 137

aux fdbk noise fault 137

aux feedback AQB 137

aux feedback loss 137

auxiliary encoder error 136

feedback pinouts 52

specifications 63

## auxiliary feedback encoders 64

## axis module

axis properties 121 , 123

catalog number 18

configuring 108

connector designators 48

mounting 45

remove from power rail 147

replacing on power rail 148

series change 11

status indicators 138

wiring requirements 78

axis unstable 140

197

## B

backplane comm 137

bandwidth 129

Kop 200

## base node address

example with double-wide modules 112

example with IDM system 113

example with two ControlLogix chassis 111

example with two power rails 110

base node address, sercos 108

baud rate 108

bayonet connector 84

block diagrams converter 178

inverter 177

shunt module 179

blown fuse

134

## bonding

EMI (electromagnetic interference) 27

examples 28

high-frequency energy 28

subpanels 28

braided strap 75

brake relay 57

building your own cables 66

## bus

overcurrent 137

overvoltage regulator

135

119

status indicator 126 , 139

undervoltage 135

## C

## cables

66

building your own cables categories 38 CE and UK requirements 20 fiber-optic cable length 102 noise zones 29 routing 22 shield clamp 90

shield, EMC 86 , 87

## CAN init 138

## capacitance values 190

## catalog number

axis module 18

integrated axis module

IPIM module 18

shunt module 18

slot-filler module 18

CB1, CB2, CB3 125

CE and UK compliance 20

## changing parameters

DriveExplorer

131

HIM 131

## circuit breaker

LIM 125

selection 23

clamp 90

18

## comm status indicator 126 , 138 common bus (refer to DC common bus) compatibility IDM system 19 network 19 compliant mechanical loads 205 configuration 198 configuring AM 108 axis properties 121 baud rate, IAM 108 delay times 123 drive modules 117 feedback only axis 119 IAM 108 optical power level 109 configuring sercos base node address 108 IDM system 107 sercos module 114 , 116 connecting Ethernet cables 105 external shunt resistor 99 feedback 91 I/O 91 IPIM module 100 motor shield clamp 90 panel-mounted breakout kit 96 premolded feedback cables 96 resistive brake module 101 sercos cables 102 connector designators axis module 48 integrated axis module 48 connector locations axis module 48 integrated axis module 47 contactor enable relay 56 control power input specifications 61 ControlFLASH firmware upgrade 181 software kit 181 troubleshooting 186 verify upgrade 186 , 195 controller properties 114 conventions used in this manual 9 conversion tab 122 converter 178 CPLD FLT 138 cycle time 116 D DAC0 131 DAC1 131 data

rate 116

type 118

date/time tab 115

## DC common bus

156 , 157 , 158 , 159

192

capacitance values 190 common bus flt 138 configuring 119 follower IAM 16 , 69 fuse requirements 70 interconnect diagram leader IAM 16 , 69 precharge 16 , 69 , 190 setting the add bus cap parameter total bus capacitance 16 typical installation 16 delay times 123 digital I/O not working correctly 134 digital inputs 54 DIN-style connector 84 dip switches 116 disable drive 142 download program 124 drive compatibility 19 enable fault 136 overcurrent 135 overtemp 136 , 137 status indicator 126 , 138 tab 121 undervoltage 136 DriveExplorer software 130 , 131 , 192 E earth ground 75 EMC cable shield 86 , 87 motor ground termination 83 EMI (electromagnetic interference) bonding 27 enable time synchronization 115 enclosure requirements 21 selection 24 encoder communication fault 136 encoders 64 erratic operation 142 error codes 134 establishing communication 138 EtherNet/IP connecting cables 105 PORT1 and PORT2 connectors 105 external shunt resistor 40 wiring 99 F fault action tab 122 fault action 143 programmable 143

## fault codes

IDM system 133

## feedback

91

119

motor feedback connector 48

cables and pinouts cables, CE and UK 20 feedback only axis gain (Kof) 200 power supply 64

tab 122

## fiber-optic

Rx and Tx connectors 102 55

signals

## fiber-optic cables

drive-to-drive 104

drive-to-IPIM 105

## firmware upgrade 181

verify upgrade 186 , 195

## follow

error 135

## follower

IAM 16 , 69

fuse selection 23

## G

gains 200

## ground

fault 136

jumper setting 70

grounded power configuration 67

grounding multiple subpanels 76

## H

## hardware

enable input 127 , 129

overtravel 135

## headers

motion allowed jumper 49

HF bonding 27

## high-frequency

energy

28

resonances 209

HIM 130

## hookup

fault 137

tab 127

## human interface module (HIM) 130

## I

## I/O

connections 91

I/O connector 132

pinouts, AM 50

50

54

pinouts, IAM specifications

## IDM fault codes 133

## IDM system

compatibility 19 configuring sercos firmware upgrade

107

181

interconnect diagram 175

system overview 15

## IDN

calculate value 213

change values 211 , 222

load observer 197

read value 212

read/write messages 208

write value 214

Ifbk HW fault 136

illegal hall state 135

## input

connector pinouts, IAM gain (Kou) 200

power source 125

## input power wiring

3-phase delta 68 determining input power 66 ground jumper setting 70 grounded power configuration high/low resistance 68

67

ungrounded power configuration 68

## installing drive accessories

AC line filters 39

external shunt resistor 40

low-profile connector kits motor brake 42

RBM 41

thermal switch 42

## installing your drive 21

bonding examples 28

bonding subpanels 28

cable categories 38

circuit breakers 23

clearance requirements 26

enclosure selection 24

fuse selection 23

HF bonding 27

line filter 22

noise zones 29

system mounting requirements 21

transformer 22

## integral bandwidth (Koi) 200 integrated axis module

axis properties 121 , 123

catalog number 18

configuring 108

connector designators 48

connector locations 47

interconnect diagram 152 , 153 , 155 , 156 , 157 ,

158 , 159

mounting 45

removing from power rail 147

replace on power rail 148

series change 11

status indicators 138

wiring BC connector r 88

wiring CED connector 81

wiring CPD connector 79

wiring IPD connector 80

wiring MP connector 83

wiring requirements 77 , 78

wiring STO connector 82

53

97

| interconnect diagrams                          | high-frequency resonances  209                           |
|------------------------------------------------|----------------------------------------------------------|
| 2094 with 1326AB  168                          | manual tuning  207                                       |
| 2094 with F-Series motor  169                  | out-of-box  201                                          |
| 2094 with LDAT  172                            | rigid mechanical loads  205                              |
| 2094 with LDC  173 ,  174                      | IDN read/write messages  208                             |
| 2094 with LDL  173 ,  174                      | input gain (Kou)  200                                    |
| 2094 with MPAI  171                            | integral bandwidth (Koi)  200                            |
| 2094 with MPAR  171                            | load inertia ratio  197                                  |
| 2094 with MPAS  170                            | mechanical load  197                                     |
| 2094 with MPL  161                             | no auto-tuning  207                                      |
| 2094 with MPL motor  162                       | torque estimate  197                                     |
| 2094 with MPL/MPM  165                         | velocity                                                 |
| 2094 with MPL/MPM/MPF  164                     | estimate  198                                            |
| 2094 with MPL/MPS  163                         | feedback  198                                            |
|                                                | logic power status indicator  125                        |
| 2094 with RDB  166                             |                                                          |
| 2094 with TLY  167 IDM system  175             | Logix Designer application  12 ,  114 ,  130 ,  181      |
| notes  151 225                                 | low profile connector kits                               |
| ,                                              | 97                                                       |
| power, DC common bus  156 ,  157 ,  158 ,  159 | wiring                                                   |
| power, IAM with LIM  152 ,  153 155            | M                                                        |
| power, IAM without LIM  RBM  225               |                                                          |
| shunt module                                   | manual tuning  207 197                                   |
| 2094  160 passive  160                         | mechanical load  memory init  137                        |
| interpreting status indicators  133            | module                                                   |
| inverter  177 IPIM module                      | mismatch  138                                            |
|                                                | mounting order  44 properties                            |
| catalog number  18 compatibility  19           |                                                          |
| fault  138                                     | drive modules  117 sercos module  116                    |
| mounting  45                                   | monitor system variables  131 10                         |
| removing from power rail  148 wiring  100      | Motion Analyzer                                          |
| IPM fault  135                                 | motion group properties                                  |
|                                                | 120 motion-allowed jumper  49                            |
|                                                | ,  82                                                    |
| ISO 13849  228                                 | motor                                                    |
| K                                              | encoder error  135 feedback loss  135                    |
| Kinetix 6000M system                           | jumps when first enabled  134 overtemp  134              |
| compatibility  19                              |                                                          |
|                                                | motors acceleration or deceleration anomalies  brake  42 |
| L                                              | cable length  20 ,  21 feedback pinouts  50 ,            |
| leader IAM  16 ,  69                           | feedback specifications  63                              |
| line filter selection                          | 93                                                       |
| 22                                             | ground termination  83                                   |
| line interface module                          | interconnect diagram                                     |
| circuit breakers  125                          | 1326AB  168                                              |
| interconnect diagram  152 ,  153 ,  155        | F-Series                                                 |
| three-phase power  125                         | 169 MPL  161 ,                                           |
| linear motors                                  | 162 MPL/MPM                                              |
| LDC  173 ,                                     | 165 MPL/MPM/MPF  MPL/MPS  163                            |
| 174 LDL  173 174                               | 164                                                      |
| ,                                              | RDB  166 TLY  167                                        |
| load inertia ratio  197                        |                                                          |
| load observer                                  |                                                          |
| acceleration                                   | motor and feedback tab  122 MPL connectors               |
| feedback                                       | bayonet  84                                              |
| 200 reference  197                             |                                                          |
| actual position feedback  197 207              | DIN-style  84 overheating  141                           |
| auto-tuning  200 198                           | power and brake pinouts  power wiring                    |
| bandwidth (Kop)  configuration                 | 53 86                                                    |
| feedback gain (Kof)                            | 3-phase and brake                                        |
| gains  200                                     | 86                                                       |
| 200 auto-tune  204                             | 3-phase only                                             |
| 205                                            |                                                          |
| compliant mechanical loads                     |                                                          |

3-phase, brake, thermal switch 87

shield clamp wiring 90

testing 126

tuning 126

velocity 141

mounting brackets 43

## mounting your drive 45

2094 power rail 43

axis module 45

IAM module 45

IPIM module 45

module mounting order 44

mounting brackets 43

shunt module 45

slot-filler module 45

## MPL connectors

84

84

bayonet DIN-style mtr fdbk noise fault 137

## N

## network

compatibility 19

node address 118

noise abnormal 142

feedback 141

reduction 39

zones 29

NV mem init 137

## O

objects init 137

optical power level 109

overspeed fault 135

## P

## panel

mounted breakout kit 96

requirements

21

## parameters

drive

IDN 222

peak enhancement 222

system variables 130

drive, IDN 211

load observer 197

peak enhancement 217

## peak enhancement

definition of terms 60

enable peak enhancement 217

example 218

example calculation 221

inverter overload curve 61

load duty cycle 60

peak current ratings 59

peak overload support 59

software/firmware 59

specifications 59

## pinouts

auxiliary feedback connector 52 I/O connector

## IAM/AM 50

input connector, IAM 53

motor and brake connector 53

motor feedback connector

50

safe torque-off connector

IAM/AM 49

planning your installation 21

PORT 1 status indicator 126

PORT 2 status indicator 126

## power

cables, CE and UK 20

cycling 58 dissipation phase loss

26

indicator not on 134

136

## power rail

connecting braided strap 75

removing 149

replacing 150

power supply, feedback k 64

power up 124

precharge 16 , 69 , 190

fault 136

timeout flt 138

premolded feedback cables 96

publications, related 10

## R

RBM 41

related publications 10

relay output 176

remove

modules from power rail 147

## replace

modules on power rail 148

## resistive brake module

interconnect diagrams 225 wiring 101

rigid mechanical loads 205

routing power and signal wiring 66

RSLinx software

181

RSLogix 5000 software 181 , 192

## S

## safe torque-off

HW fault 136

motion-allowed jumper 49 , 82

pinouts, AM 49

pinouts, IAM 49

wiring 82

## safety

lock status indicator 126

## SCANport

comm 137

SCANport/DPI adapter 130 , 192

selection

AC line filters 22

self sense fault 136

,

93

## sercos

```
connecting cables 102 connections 55 init 138 module 114 module properties 116 ring fault 136 same addr 136 series change 11 peak enhancement specifications 59 setting the add bus cap parameter 192 seven-segment status indicator 125 shield clamp 90 shunt module 179 bus status indicator 139 catalog number 18 fault 138 interconnect diagram 2094 160 passive 160 mounting 45 removing from power rail 148 shunt fault status indicator 140 temperature status indicator 140 time out 137 troubleshooting 139 wiring requirements 78 shutdown 142 slot-filler module catalog number 18 mounting 45 removing from power rail 148 software DriveExplorer 130 , 192 Logix Designer application 12 , 114 overtravel 135 specifications analog outputs 55 auxiliary feedback encoders 64 brake relay 57 contactor enable relay 56 control power input 61 digital inputs 54 feedback motor and auxiliary 63 power supply 64 peak enhancement 59 power cycling 58 dissipation 26 sercos connections 55 status indicators 126 , 133 , 138 bus status 139 comm status 138 drive status 138 logic power 125 sercos interface module 126 seven-segment 125 status only 142 stop motion 142 Studio 5000 Logix Designer 12 , 114 surge suppression 89 switches base node address 108 baud rate 108 optical power level 109
```

## system

```
components 12 ground 75 mounting requirements 21 system block diagrams converter 178 inverter 177 shunt module 179 system overview DC common bus 16 sercos 17 with LIM 13 without LIM 14 T task init 137 test axes hookup tab 127 thermal switch 42 torque estimate 197 total bus capacitance 16 calculating 189 example 191 transformer sizing 22 transmit power level 117 troubleshooting bus status indicator 139 comm status indicator 138 ControlFLASH 186 disable drive 142 drive status indicator 138 error codes 134 fault action 143 general atune fault 137 aux fdbk noise fault 137 aux feedback AQB 137 aux feedback loss 137 auxiliary encoder error 136 backplane comm 137 blown fuse 134 bus overcurrent 137 bus overvoltage 135 bus undervoltage 135 CAN init 138 common bus flt 138 CPLD FLT 138 digital I/O not working correctly 134 drive enable fault 136 drive overcurrent 135 drive overtemp 136 , 137 drive undervoltage 136 encoder communication fault 136 follow error 135 ground fault 136 hardware overtravel 135 hookup fault 137 Ifbk HW fault 136 illegal hall state 135 IPIM module flt 138 IPM fault 135 memory init 137 module mismatch 138 motor encoder error 135 motor feedback loss 135
```

## motor jumps when first enabled 134 motor overtemp 134 mtr fdbk noise fault 137 NV mem init 137 objects init 137 overspeed fault 135 power indicator not on 134 power phase loss 136 precharge fault 136 precharge timeout flt 138 safe torque-off HW fault 136 SCANport comm 137 self sense fault 136 sercos init 138 sercos ring fault 136 sercos same addr 136 shunt module fault 138 shunt time out 137 software overtravel 135 task init 137 unknown axis 137 general system anomalies 140 abnormal noise 142 axis unstable 140 erratic operation 142 feedback noise 141 motor acceleration or deceleration motor overheating 141 motor velocity 141 no rotation 141 Logix/drive fault behavior 142 programmable fault action 143 safety precautions 133 shunt module 139 bus status indicator 139 shunt fault status indicator 140 temperature status indicator 140 shutdown 142 status only 142 stop motion 142 tune axes bandwidth 129 tune tab 129 typical installation DC common bus 16 IDM system 15 sercos 17 with LIM 13 without LIM 14 U ungrounded power configuration 68 units tab 122 unknown axis 137 using analog test points 131 V

## velocity

estimate 198 feedback 198

```
141
```

## wiring

```
building your own cables 66 earth ground 75 Ethernet cables 105 external shunt resistor 99 ground jumper setting 70 grounded power configuration 67 I/O connections 91 IAM BC connector 88 CED connector 81 CPD connector 79 IPD connector 80 MP connector 83 STO connector 82 input power type 66 IPIM module 100 low profile connectors 97 motor cable shield clamp 90 motor power 86 , 87 requirements 65 IAM 77 IAM/AM 78 shunt module 78 resistive brake module 101 routing power and signal wiring 66 safe torque-off feature 82 sercos fiber optic cables 102 ungrounded power configuration 68 78
```

## wiring guidelines

## W

## Notes:

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

Allen-Bradley, CompactLogix, ControlFLASH, ControlLogix, DriveExplorer, expanding human possibility, Guardmaster, Integrated Architecture, Kinetix, Logix 5000, Rockwell Automation, RSLinx, RSLogix 5000, SCANport, SoftLogix, Studio 5000 Logix Designer, and Studio 5000 are trademarks of Rockwell Automation, Inc.

EtherNet/IP is a trademark of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan 12a,1831Diegem,Belgium,Tel:(32)26630600,Fax:(32)26630640 ASIA PACIFIC: RockwellAutomation, Level 14, Core F, Cyberport 3, 100 Cyberport Road, Hong Kong, Tel:(852)2887 4788,Fax:(852)2508 1846 UNITEDKINGD0M:Rockwell Automation Ltd.Pitfield,Kiln Farm MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800,Fax:(44)(1908)261-917