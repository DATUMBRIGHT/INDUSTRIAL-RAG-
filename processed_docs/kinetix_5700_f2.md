<!-- image -->

This manual links to Kinetix 5500 Servo Drive Fault Codes Reference Data, publication 2198-RD005 for fault codes. Download the spreadsheet now for offline access.

<!-- image -->

## Kinetix 5500 Servo Drive

Catalog Numbers 2198-H003-ERS, 2198-H008-ERS,2198-H015-ERS, 2198-H025-ERS, 2198-H040-ERS,2198-H070-ERS, 2198-H003-ERS2, 2198-H008-ERS2,2198-H015-ERS2, 2198-H025-ERS2,

2198-H040-ERS2,2198-H070-ERS2, 2198-CAPMOD-1300

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

## IMPORTANT

Identifies information that is critical for successful application and understanding of the product.

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

Start

## Plan the Kinetix 5500 Drive System Installation

## Table of Contents

| Preface                                                                                                                                 | Preface   |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Download Firmware, and Other Associated Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                          |           |
| Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11       |           |
| Access Fault Codes List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11      |           |
| Conventions Used in This Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11              |           |
| Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12     |           |
| Chapter 1                                                                                                                               |           |
| About the Kinetix 5500                                                                                                                  |           |
| Servo Drive System. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . 15 |           |
| Drive Hardware and Input Power Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                          |           |
| Standalone Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                  |           |
| Shared AC/DC Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                    |           |
| Shared DC Common-bus Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                              |           |
| Shared AC/DC Hybrid Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                        |           |
| Motor Feedback and Feedback-only Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                              |           |
| Typical Communication Configurations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                    |           |
| Linear Topology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23         |           |
| Ring Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24        |           |
| Star Topology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25       |           |
| Safe Torque Off Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26             |           |
| Hardwired Safety Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26                     |           |
| Integrated Safety Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                     |           |
| Catalog Number Explanation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29            |           |
| Agency Compliance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30      |           |
| Chapter 2                                                                                                                               |           |
| System Design Guidelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31         |           |
| AC Line Filter Selection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32            |           |
| Transformer Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33              |           |
| Circuit Breaker/Fuse Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                   |           |
| 24V Control Power Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                   |           |
| Contactor Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36            |           |
| Passive Shunt Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37                    |           |
| Enclosure Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38            |           |
| Minimum Clearance Requirements. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 39                        |           |
| Electrical Noise Reduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40        |           |
| Bonding Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40          |           |
| Bonding Multiple Subpanels.  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   42               |           |
| Establishing Noise Zones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43               |           |
| Cable Categories for Kinetix 5500 Systems. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44                             |           |
| Noise Reduction Guidelines for Drive Accessories . . . . . . . . . . . . . . . . . . . . . . . . . . 44                                 |           |

Chapter 3

| Mount the Kinetix 5500 Drive   | Determine Mounting Order. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                                                                                                               |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System                         | Zero-stack Tab and Cutout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                                                                                                                       |
|                                | Shared-bus Connection System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                                                                                                                            |
|                                | Single-axis Configurations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                                                                                                     |
|                                | Multi-axis Configurations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                                                                                                    |
|                                | Drill-hole Patterns. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                                                                                                      |
|                                | Mount Your Kinetix 5500 Drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                                                                                                                 |
|                                | Chapter 4                                                                                                                                                                                                                                    |
| Connector Data and Feature     | Kinetix 5500 Connector Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60                                                                                                                 |
| Descriptions                   | Module Status Connector Pinout . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 61                                                                                                                        |
|                                | Safe Torque Off Connector Pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                                                                                                                            |
|                                | Input Power Connector Pinouts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                                                                                                                          |
|                                | DC Bus and Shunt Resistor Connector Pinouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62                                                                                                                                     |
|                                | Digital Inputs Connector Pinouts . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 62                                                                                                                        |
|                                | Ethernet Communication Connector Pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                                                                                                                                     |
|                                | Motor Power, Brake, and Feedback Connector Pinouts . . . . . . . . . . . . . . . . . . . . . . 63                                                                                                                                            |
|                                | Motor Feedback Connector Pinout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                                                                                                                             |
|                                | Understand Control Signal Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                                                                                                                        |
|                                | Digital Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                                                                                                          |
|                                | Ethernet Communication Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                                                                                                                                 |
|                                | Motor Brake Circuit. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                                                                                                                |
|                                | Control Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                                                                                                             |
|                                | Feedback Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                                                                                                             |
|                                | Absolute Position Feature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                                                                                                                     |
|                                | Safe Torque Off Safety Features. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   68                                                                                                               |
|                                | Servo Drives with Hardwired Safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68                                                                                                                            |
|                                | Servo Drives with Integrated Safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68                                                                                                                           |
|                                | Chapter 5                                                                                                                                                                                                                                    |
| Connect the Kinetix 5500 Drive | Basic Wiring Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70                                                                                                               |
| System                         | Routing the Power and Signal Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70                                                                                                                             |
|                                | Determine the Input Power Configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                                                                                                                          |
|                                | Grounded Power Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                                                                                                                           |
|                                | Ungrounded Power Configurations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73                                                                                                                              |
|                                | Ground Screw Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                                                                                                            |
|                                | Remove the Ground Screws in Select Power Configurations . . . . . . . . . . . . . . . . . . . . . 75                                                                                                                                         |
|                                | Ground the Drive System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                                                                                                             |
|                                | Ground the System Subpanel. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                                                                                                                         |
|                                | Ground Multiple Subpanels. . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . 77                                                                                                                    |
|                                | Wiring Requirements . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   78                                                                                                        |
|                                | Wiring Guidelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                                                                                                       |
|                                | Wire the Power Connectors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80                                                                                                                  |
|                                | Wire the 24V Control Power Input Connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80                                                                                                                                      |
|                                | Wire the Input Power Connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81                                                                                                                          |
|                                | Wire the Digital Input Connectors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 Wire the Safe Torque Off Connector. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 |
|                                | Wire the Digital Inputs Connector. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                                                                                                                          |
|                                | Wire Kinetix VP Motors and Actuators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                                                                                                                      |

## Configure and Start the Kinetix 5500 Drive System

| Maximum Cable Lengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83                 |
|----------------------------------------------------------------------------------------------------------------------------------------|
| Motor Power Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83                 |
| Motor Brake Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84                |
| Motor Feedback Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85                    |
| Apply the Single Motor-cable Shield Clamp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                           |
| Wire Other Motors and Actuators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88             |
| Install the Kinetix 5500 Add-On Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88                       |
| Motor Power and Brake Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                         |
| Motor Power/Brake Cable Series Change. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90                            |
| Maximum Cable Lengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91                 |
| Motor Power/Brake Cable Preparation.  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 91                        |
| Apply the Motor Power/brake Shield Clamp. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                             |
| Motor Feedback Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                    |
| Motor Feedback Cable Preparation. .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 96                     |
| Capacitor Module Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98            |
| External Passive-shunt Resistor Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                       |
| Ethernet Cable Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100           |
| Chapter 6                                                                                                                              |
| Understand the Kinetix 5500 Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                |
| Menu Screens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103         |
| Setup Screens . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104        |
| Startup Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106           |
| Configure the Drive. . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 107 |
| Set the Network Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                   |
| Studio 5000 Logix Designer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107           |
| Version History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107        |
| Install the Kinetix 5500 Add-On Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                        |
| Configure the Logix 5000 Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                |
| Configure the Kinetix 5500 Drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112                     |
| Configure the Motion Group. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120                  |
| Configure Feedback-only Axis Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121                    |
| Configure Induction-motor Frequency-control Axis Properties . . . . . . . . . . . . . . . . . . 122                                    |
| General and Motor Categories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122                   |
| Basic Volts/Hertz Method. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123                |
| Sensorless Vector Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124                 |
| Fan/Pump Volts/Hertz Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126                      |
| Configure SPM Motor Closed-loop Control Axis Properties . . . . . . . . . . . . . . . . . . . . . . 127                                |
| Download the Program. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                |
| Apply Power to the Kinetix 5500 Drive. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132                 |
| Applying Power after Changing Input Voltage Range . . . . . . . . . . . . . . . . . . . . . . . 132                                    |
| Understand Bus-sharing Group Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133                         |
| Bus-sharing Group Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134                    |
| Configure Bus-sharing Groups . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 134                   |
| Test and Tune the Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136       |
| Test the Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136      |

Chapter 7

| Troubleshoot the Kinetix 5500   | Safety Precautions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143                                                                                                                           |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Drive System                    | Interpret Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144                                                                                                                                |
|                                 | Display Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144                                                                                                                                 |
|                                 | Fault Code Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144                                                                                                                                    |
|                                 | Fault Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145                                                                                                                              |
|                                 | Kinetix 5500 Drive Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146                                                                                                                                               |
|                                 | Kinetix 5500 Capacitor Module Status Indicators. . . . . . . . . . . . . . . . . . . . . . . . . . 147                                                                                                                                                         |
|                                 | General Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147                                                                                                                                |
|                                 | Logix 5000 Controller and Drive Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149                                                                                                                                           |
|                                 | Chapter 8                                                                                                                                                                                                                                                      |
| Remove and Replace Servo        | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153                                                                                                                           |
| Drives                          | Remove and Replace Kinetix 5500 Servo Drives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154                                                                                                                                                   |
|                                 | Remove Power and All Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154                                                                                                                                                 |
|                                 | Remove the Servo Drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155                                                                                                                                       |
|                                 | Replace the Servo Drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155                                                                                                                                      |
|                                 | Start and Configure the Drive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156                                                                                                                                  |
|                                 | Chapter 9                                                                                                                                                                                                                                                      |
| Kinetix 5500 Safe Torque Off -  | Certification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157                                                                                                                      |
| Hardwired Safety                | Important Safety Considerations . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 157                                                                                                                                            |
|                                 | Category 3 Requirements According to ISO 13849-1 . . . . . . . . . . . . . . . . . . . . . . . . 158                                                                                                                                                           |
|                                 | Stop Category Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158                                                                                                                                       |
|                                 | Performance Level (PL) and Safety Integrity Level (SIL) . . . . . . . . . . . . . . . . . . . . 158                                                                                                                                                            |
|                                 | Description of Operation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   159                                                                                                                            |
|                                 | Fault Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160                                                                                                                              |
|                                 | Probability of Dangerous Failure Per Hour . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161                                                                                                                                            |
|                                 | Safe Torque Off Connector Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161                                                                                                                                      |
|                                 | Wire the Safe Torque Off Circuit. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162                                                                                                                                    |
|                                 | Safe Torque Off Wiring Requirements  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 162                                                                                                                                                |
|                                 | Safe Torque Off Feature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163                                                                                                                                |
|                                 | Safe Torque Off Feature Bypass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163                                                                                                                                             |
|                                 | Cascade the Safe Torque-off Signal. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164                                                                                                                                                |
|                                 | Safe Torque Off Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 164                                                                                                                                   |
|                                 | Chapter 10                                                                                                                                                                                                                                                     |
| Kinetix 5500 Safe Torque Off -  | Certification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165                                                                                                                      |
| Integrated Safety               | Important Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165                                                                                                                                              |
|                                 | Safety Application Requirements . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 165                                                                                                                                            |
|                                 | Category 3 Requirements According to ISO 13849 . . . . . . . . . . . . . . . . . . . . . . . . . 166                                                                                                                                                           |
|                                 | Stop Category Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166                                                                                                                                       |
|                                 | Performance Level (PL) and Safety Integrity Level (SIL) . . . . . . . . . . . . . . . . . . . . 167                                                                                                                                                            |
|                                 | Description of Operation  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  167                                                                                                                             |
|                                 | STO State Reset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167                                                                                                                                 |
|                                 | Fault Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168                                                                                                                              |
|                                 | Probability of Dangerous Failure Per Hour . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168                                                                                                                                            |
|                                 | Safe Torque Off Feature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169                                                                                                                                |
|                                 | Out-of-Box State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169 Out-of-Box State Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169 |

|                               | Understand Integrated Safety Drive Replacement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171                         |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|                               | Replace an Integrated Safety Drive in a GuardLogix System . . . . . . . . . . . . . . . . . . . . 171                                |
|                               | Configure Only When No Safety Signature Exists . . . . . . . . . . . . . . . . . . . . . . . . . . 172                               |
|                               | Configure Always. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172        |
|                               | Motion Direct Commands in Motion Control Systems. . . . . . . . . . . . . . . . . . . . . . . . . . . 173                            |
|                               | Understand STO Bypass When Using Motion Direct Commands . . . . . . . . . . . . . . 173                                              |
|                               | Logix Designer Application Warning Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174                              |
|                               | Torque Permitted in a Multi-workstation Environment . . . . . . . . . . . . . . . . . . . . . 176                                    |
|                               | Warning Icon and Text in Axis Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176                         |
|                               | Functional Safety Considerations . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 177                 |
|                               | Safe Torque Off Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177         |
|                               | Appendix A                                                                                                                           |
| Interconnect Diagrams         | Interconnect Diagram Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179         |
|                               | Power Wiring Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179      |
|                               | Single-axis Drive Wiring Examples . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 180                  |
|                               | Bus-sharing Wiring Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182                  |
|                               | Shunt Resistor Wiring Example. . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . 184         |
|                               | Kinetix 5500 Servo Drive and Rotary Motor Wiring Examples . . . . . . . . . . . . . . . . . . . . 185                                |
|                               | Kinetix 5500 Drive and Linear Actuator Wiring Examples . . . . . . . . . . . . . . . . . . . . . . . 187                             |
|                               | System Block Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191      |
|                               | Appendix B                                                                                                                           |
| Update the Drive Firmware     | Before You Begin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193 |
|                               | Configure Logix 5000 Controller Communication. . . . . . . . . . . . . . . . . . . . . . . . . . 193                                 |
|                               | Inhibit Feedback Only Axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 195             |
|                               | Update Firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196  |
|                               | Verify the Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199         |
|                               | Appendix C                                                                                                                           |
| Size Multi-axis Shared-bus    | Shared-bus Configurations . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   201     |
| Configurations                | Shared AC Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201               |
|                               | Shared DC Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202               |
|                               | Shared AC/DC Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204                    |
|                               | Shared AC/DC Hybrid Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205                       |
|                               | Power-sharing Sizing Examples .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  206            |
|                               | Shared DC Example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206             |
|                               | Shared AC/DC Hybrid Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207                    |
|                               | Shared AC/DC Example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208                |
|                               | Control Power Current Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208               |
|                               | Kinetix 5500 System Current Demand Example . . . . . . . . . . . . . . . . . . . . . . . . . . . 209                                 |
|                               | Energy Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209  |
|                               | Appendix D                                                                                                                           |
| Motor Control Feature Support | Frequency Control Methods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212         |
|                               | Basic Volts/Hertz . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213        |
|                               | Basic Volts/Hertz for Fan/Pump Applications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214                             |
|                               | Sensorless Vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215        |
|                               | Current Limiting for Frequency Control.   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . 216             |
|                               | The Effects of Current Limiting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216                 |

History of Changes

| Enable the Current Limiting Feature .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . 218                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Set the CurrentVectorLimit Attribute Value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218                                     |
| Stability Control for Frequency Control  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   219                      |
| Enable the Stability Control Feature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                              |
| Skip Speeds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221       |
| Multiple Skip Speeds. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222                     |
| Flux Up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223   |
| Flux Up Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224                  |
| Configure the Flux Up Attributes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225                             |
| Current Regulator Loop Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225                      |
| Motor Category . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226          |
| Motor Tests and Autotune Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228                                  |
| Motor Analyzer Category Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229                                     |
| Selection of Motor Thermal Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231                         |
| Generic Motors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231                  |
| Thermally Characterized Motors . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . . . . . 231                            |
| Speed Limited Adjustable Torque (SLAT) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232                            |
| Motion Polarity Setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232                     |
| SLAT Min Speed/Torque . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233                         |
| SLAT Max Speed/Torque. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234                          |
| SLAT Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234                 |
| Configure the Axis for SLAT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235                         |
| Motor Overload Retention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238                  |
| Phase Loss Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239               |
| Phase-loss Detection Configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240                                   |
| Phase Loss Detection Current Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241                                    |
| Closed Loop Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241                     |
| Frequency Control. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242                    |
| Velocity Droop Attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242                      |
| Velocity Droop Configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242                           |
| Commutation Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243              |
| Adaptive Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243           |
| Appendix E                                                                                                                                      |
| 2198-UM001M-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245              |
| 2198-UM001L-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245              |
| 2198-UM001K-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245              |
| 2198-UM001J-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245              |
| 2198-UM001I-EN-P. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246             |
| 2198-UM001H-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246              |
| 2198-UM001G-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247              |
| 2198-UM001F-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247              |
| 2198-UM001E-EN-P . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  247            |
| 2198-UM001D-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248              |
| 2198-UM001C-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249              |
| 2198-UM001B-EN-P . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249              |
| Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . .251 |

## Download Firmware, and Other Associated Files

## Summary of Changes

## Access Fault Codes List

## Conventions Used in This Manual

This manual provides detailed installation instructions for mounting, wiring, and troubleshooting the Kinetix® 5500 servo drives, and system integration for your drive and motor/actuator combination with a Logix 5000® controller.

This manual is intended for engineers or technicians who are directly involved in the installation and wiring of the Kinetix 5500 drives, and programmers who are directly involved in the operation, field maintenance, and integration of these drives with the EtherNet/IP™ communication module or controller.

If you do not have a basic understanding of Kinetix 5500 servo drives, contact your local Rockwell Automation sales representative for information on available training courses.

Use the Product Compatibility and Download Center at rok.auto/pcdc for the following:

- Download firmware and associated files such as Add-on Profile (AOP), Electronic Data Sheet (EDS), and Device Type Manager (DTM)
- Access product release notes

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic                                                                               | Page       |
|-------------------------------------------------------------------------------------|------------|
| Updated template.                                                                   | Throughout |
| Added attention statement to Figure 57 and Figure 99 related to 9V and 5V encoders. | 95, 186    |

<!-- image -->

This manual links to Kinetix 5500 Servo Drive Fault Codes Reference Data, publication 2198-RD005, for fault codes. Download the spreadsheet now for offline access.

These conventions are used throughout this manual:

- Bulleted lists such as this one provide information, not procedural steps.
- Numbered lists provide sequential steps or hierarchical information.
- Catalog number string 2198-Hxxx-ERSx is used when there's no need to distinguish between -ERS or -ERS2 servo drives.

| Kinetix 5500 Drive Cat. No.   | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| 2198-Hxxx-ERS                 | Kinetix 5500 drive with hardwired Safe Torque Off functionality  |
| 2198-Hxxx-ERS2                | Kinetix 5500 drive with integrated Safe Torque Off functionality |

## Additional Resources

## Table 1 - Additional Resources

| Resource                                                                                                                                                               | Description                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001                                                                                             | Product specifications for Kinetix VPL, VPC, VPF, VPH, and VPS; Kinetix MPL, MPM, MPF, and MPS; Kinetix TLY and TL; Kinetix HPK; and Kinetix MMA rotary motors.                                                                |
| Kinetix Linear Motion Specifications Technical Data, publication KNX-TD002                                                                                             | Product specifications for Kinetix MPAS and MPMA linear stages, Kinetix MPAR and MPAI electric cylinders, and Kinetix LDC and LDL linear motors.                                                                               |
| Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications Technical Data, publication KNX-TD003                                                                   | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP network and EtherNet/IP networking servo drive families.                                                                                    |
| Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNX-TD004                                                                            | Product specifications for Kinetix 2090 motor and interface cables.                                                                                                                                                            |
| Kinetix Servo Drive Performance Specifications per Ecodesign Regulation (EU) 2019/1781 Technical Data, publication KNX-TD006                                           | Provides energy efficiency performance data for Rockwell Automation Kinetix Servo drives. This data supports IE2 compliance of Kinetix Servo drives per EU 2019/1781.                                                          |
| Kinetix 5500 Servo Drive Fault Codes Reference Data, publication 2198-RD005                                                                                            | Provides the fault codes for Kinetix 5500 servo drives.                                                                                                                                                                        |
| AC Line Filter Installation Instructions, publication 2198-IN003                                                                                                       | Provides information on how to install AC line filters designed for Kinetix 5500 and Kinetix 5700 servo drive systems.                                                                                                         |
| Shunt Resistor Installation Instructions, publication 2097-IN002                                                                                                       | Provides information on how to install and wire Bulletin 2097 shunt resistors.                                                                                                                                                 |
| System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001                                                                                  | Information, examples, and techniques that are designed to minimize system failures caused by electrical noise.                                                                                                                |
| Servo Drive Installation Best Practices Application Technique, publication MOTION-AT004                                                                                | Best practice examples to help reduce the number of potential noise or electromagnetic interference (EMI) sources in your system and to make sure that the noise sensitive components are not affected by the remaining noise. |
| Kinetix Motion Control Selection Guide, publication KNX-SG001                                                                                                          | Overview of Kinetix servo drives, motors, actuators, and motion accessories that are designed to help make initial decisions for the motion control products best suited for your system requirements.                         |
| Kinetix 5500 Drive Systems Design Guide, publication KNX-RM009                                                                                                         | System design guide to select the required (drive specific) drive module, power accessory, feedback connector kit, and motor cable catalog numbers for your Kinetix 5500 drive system.                                         |
| Kinetix Halogen-free PUR and PVC Single Motor Cables Quick Reference, publication 2090-QR002                                                                           | Provides product specifications comparing 2090-CSBM1xx-xxLFxx (Halogen-free PUR) and 2090- CSxM1xx-xxVAxx (PVC) single motor cables.                                                                                           |
| Rockwell Automation Product Selection website rok.auto/ systemtools                                                                                                    | Online product selection and system configuration tools, including AutoCAD (DXF) drawings.                                                                                                                                     |
| FactoryTalk Motion Analyzer System Sizing and Selection Tool website rok.auto/motion-analyzer                                                                          | Comprehensive motion application sizing tool used for analysis, optimization, selection, and validation of your Kinetix Motion Control system.                                                                                 |
| Vertical Load and Holding Brake Management Application Technique, publication MOTION-AT003                                                                             | Provides information on vertical loads and how the servo motor holding-brake option can be used to help keep a load from falling.                                                                                              |
| Integrated Motion on the EtherNet/IP Network Reference Manual, publication MOTION-RM003                                                                                | Information on the AXIS_CIP_DRIVE attributes and the configuration software control modes and methods.                                                                                                                         |
| Integrated Motion on the EtherNet/IP Network Configuration and Startup User Manual, publication MOTION-UM003                                                           | Information on how to configure and troubleshoot your ControlLogix® and CompactLogix™ EtherNet/ IP™ network modules.                                                                                                           |
|                                                                                                                                                                        | GuardLogix 5570 Controllers User Manual, publication 1756-UM022 Provides information on how to install, configure, program, and use ControlLogix controllers and                                                               |
| Compact GuardLogix 5370 Controllers User Manual, publication                                                                                                           |                                                                                                                                                                                                                                |
| 1769-UM022                                                                                                                                                             | Provides information on how to install, configure, program, and use CompactLogix and Compact                                                                                                                                   |
| Compact GuardLogix 5380 Contro  GuardLogix controllers. llers User Manual, publication 5069-UM001                                                                      |                                                                                                                                                                                                                                |
| GuardLogix 5570 and Compact GuardLogix 5370 Controller Systems Safety Reference Manual, publication 1756-RM099  GuardLogix 5580 and Compact GuardLogix 5380 Controller | Provides information on how to achieve and maintain Safety Integrity Level (SIL) and Performance Level (PL) safety application requirements for GuardLogix and Compact GuardLogix controllers.                                 |
| ControlFLASH User Manual, publication 1756-UM105                                                                                                                       | Provides guidance on how to use ControlFLASH™ or ControlFLASH Plus™ software to update drive firmware. See the release notes for your product to determine whether it supports firmware updates                                |
| firmware See the release notes for your product to de by using ControlFLASH or ControlFLASH Plus software. ControlFLASH Plus Quick Start Guide, publication CFP-QS001                                                                                                                                                                        |                                                                                                                                                                                                                                |
| EtherNet/IP Network Devices User Manual, ENET-UM006                                                                                                                    | Describes how to configure and use EtherNet/IP devices to communicate on the EtherNet/IP network.                                                                                                                              |
| Ethernet Reference Manual, ENET-RM002                                                                                                                                  | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                     |
| System Security Design Guidelines Reference Manual, SECURE RM001                                                                                                                                                                        | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                  |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002                                                     | Provides a quick reference tool for Allen-Bradley® industrial automation controls and assemblies.                                                                                                                              |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

Table 1 - Additional Resources (Continued)

| Resource                                                                                                         | Description                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1 | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                      | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
|                                                                                                                  | Product Certifications website, rok.auto/certifications. Provides declarations of conformity, certificates, and other certification details.                                                                                                                                    |

## Notes:

## About the Kinetix 5500 Servo Drive System

Table 2 - Kinetix 5500 Drive System Overview

| Drive System Component          |                                                      | Cat. No. Description                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix 5500 Servo Drives       | 2198-Hxxx-ERS                                        | 200V-class (single-phase or three-phase) and 400V-class (three-phase) drives operate in standalone and multi-axis shared AC, shared DC, shared AC/DC, and shared AC/DC hybrid configurations. Modules are zero-stacked from drive-to-drive and use the shared-bus connection system to extend power in multi-axis configurations. Safe Torque Off via hardwired (STO) connector. |
| Kinetix 5500 Servo Drives       | 2198-Hxxx-ERS2                                       | Same power structures as 2198-Hxxx-ERS servo drives with standalone and multi-axis bus-sharing capability. Safe Torque Off via the EtherNet/IP™ network.                                                                                                                                                                                                                         |
| Kinetix 5500 Capacitor Module   | 2198-CAPMOD-1300                                     | Use for energy storage and/or to improve performance in applications producing regenerative energy and requiring shorter duty cycles (1360 µf). Modules are zero-stacked side by side with servo drives and use the shared-bus connection system to extend power.                                                                                                                |
| Shared-bus Connector Kits       | 2198-H040-x-x                                        | Input wiring connectors and DC bus T-connector for frame 1 and 2 servo drives.                                                                                                                                                                                                                                                                                                   |
| Shared-bus Connector Kits       | 2198-H070-x-x                                        | Input wiring connectors and DC bus T-connector for frame 3 servo drives.                                                                                                                                                                                                                                                                                                         |
| Feedback Connector Kit          |                                                      | 2198-KITCON-DSL Replacement feedback connector kit with 2-pin connector plug and grounding plate inside the connector housing.                                                                                                                                                                                                                                                   |
| Hiperface-to-DSL Converter Kit  | 2198-H2DCK (series B or later)                       | Use the 2198-H2DCK Hiperface-to-DSL feedback converter kit with Kinetix MPL, MPM, MPF, and MPS rotary motors, Kinetix MPAS ballscrew, MPAR, MPAI linear actuators, and Kinetix LDAT linear thrusters.                                                                                                                                                                            |
| I/O Connector Kits              |                                                      | 2198-KITCON-IOSP Replacement I/O connector kit (spring clamp) for I/O (IOD) connector.                                                                                                                                                                                                                                                                                           |
|                                 |                                                      | 2198-KITCON-IOSC Replacement I/O connector kit (screw terminal) for I/O (IOD) connector.                                                                                                                                                                                                                                                                                         |
| Connector Sets                  |                                                      | 2198-KITCON-PWR40 Replacement connector set, 40 A, for frame 1 and frame 2 drives.                                                                                                                                                                                                                                                                                               |
| Connector Sets                  |                                                      | 2198-KITCON-PWR70 Replacement connector set, 70 A, for frame 3 drives.                                                                                                                                                                                                                                                                                                           |
| Connector Sets                  |                                                      | 2198-KITCON-CAP1300 Replacement connector set, 40 A, for capacitor module.                                                                                                                                                                                                                                                                                                       |
| Encoder Output Module           | 2198-ABQE                                            | The Allen-Bradley® encoder output module is a DIN rail mounted EtherNet/IP™ network-based standalone module capable of outputting encoder pulses to a customer-supplied peripheral device (cameras, for example, used in line-scan vision systems).                                                                                                                              |
| Logix 5000® Controller Platform | Bulletin 1769 Bulletin 5069                          | Integrated Motion on the EtherNet/IP network in CompactLogix™ 5370, CompactLogix 5380, and CompactLogix 5480 controllers and Integrated Safety in Compact GuardLogix® 5370 controllers. Linear, Device Level Ring (DLR), and star topology is supported.                                                                                                                         |
| Logix 5000® Controller Platform | 1756-EN2T module 1756-EN2TR module 1756-EN3TR module | EtherNet/IP network communication modules for use with ControlLogix® 5570, ControlLogix 5580, and GuardLogix 5570 controllers. Linear, Device Level Ring (DLR), and star topology is supported.                                                                                                                                                                                  |
| Studio 5000® Environment        | —                                                    | Studio 5000 Logix Designer® application, version 21.00 or later, supports programming, commissioning, and maintaining the CompactLogix and ControlLogix controller families. Version 24.00 or later is required for 2198-Hxxx-ERS2 servo drives.                                                                                                                                 |
| Rotary Servo Motors             | Kinetix VP                                           | Compatible rotary motors include 200V and 400V-class Kinetix VPL, VPF, VPH, and VPS.                                                                                                                                                                                                                                                                                             |
| Rotary Servo Motors             | Kinetix MP                                           | Compatible rotary motors include 200V and 400V-class Kinetix MPL, MPM, MPF, and MPS when used with the Hiperface-to DSL feedback converter kit.                                                                                                                                                                                                                                                                                                                                                                                  |

## Start

Use this chapter to become familiar with the Kinetix® 5500 drive system and obtain an overview of the installation configurations.

| Topic                                           |   Page |
|-------------------------------------------------|--------|
| About the Kinetix 5500 Servo Drive System       |     15 |
| Drive Hardware and Input Power Configurations   |     17 |
| Motor Feedback and Feedback-only Configurations |     22 |
| Typical Communication Configurations            |     23 |
| Safe Torque Off Configurations                  |     26 |
| Catalog Number Explanation                      |     29 |
| Agency Compliance                               |     30 |

The Kinetix 5500 servo drives are designed to provide a Kinetix Integrated Motion solution for your drive and motor/actuator application.

1

## Table 2 - Kinetix 5500 Drive System Overview (Continued)

| Drive System Component   |                                        | Cat. No. Description                                                                                                                                                                                                                                                                                 |
|--------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Linear Actuators         | Kinetix VPAR Kinetix MP Kinetix LDAT   | Compatible linear actuators include 200V and 400V-class Kinetix VPAR, Kinetix MPAS ballscrew, MPAR, and MPAI, and Kinetix LDAT when used with the Hiperface-to-DSL feedback converter kit.                                                                                                           |
| Induction Motors —       |                                        | Induction motors with open loop frequency control are also supported.                                                                                                                                                                                                                                |
| Cables                   | 2090-CSxM1DF-xxxxxx                    | Kinetix 2090 flying-lead single-cable for motor power, feedback, and optional 24V DC brake power with Kinetix VP motors. Designed specifically for Kinetix 5500 servo drives.                                                                                                                        |
| Cables                   | 2090-CSxM1DG-xxxxxx                    | Kinetix 2090 flying-lead single cable for motor power, feedback, and optional 24V DC brake power with Kinetix VP motors and actuators. Designed with longer leads than 2090-CSxM1DF cables to accommodate Kinetix 5700 drive families.                                                               |
| Cables                   | 2090-CFBM7DF-CEAxxx                    | Kinetix 2090 motor feedback cables for Kinetix MP motors and actuators.                                                                                                                                                                                                                              |
| Cables                   | 2090-CPxM7DF-xxAxxx                    | Kinetix 2090 motor power/brake cables for Kinetix MP motors and actuators.                                                                                                                                                                                                                           |
| Cables                   | 1585J-M8CBJM-x                         | Ethernet cables are available in standard lengths. Shielded cable is recommended.                                                                                                                                                                                                                    |
| AC Line Filters          | 2198-DB08-F 2198-DB20-F 2198-DB42-F    | Bulletin 2198 three-phase AC line filters are required to meet CE and available for use in all Kinetix 5500 drive systems. Use 2198-DBxx-F filters as field replacements in existing installations. Select 2198-DBRxx-F filters for all new systems and do not remove the servo drive ground screws. |
| AC Line Filters          | 2198-DBR20-F 2198-DBR40-F 2198-DBR90-F | Bulletin 2198 three-phase AC line filters are required to meet CE and available for use with all Kinetix 5500 drive systems. Select 2198-DBRxx-F filters for all new systems and do not remove the servo drive ground screws.                                                                        |
| 24V DC Power Supply      | 1606-XLxxx                             | Bulletin 1606 24V DC power supply for control circuitry, digital inputs, safety, and motor brake.                                                                                                                                                                                                    |
| External Shunt Resistors |                                        | 2097-R6 and 2097-R7 Bulletin 2097 external passive shunt resistors for when the internal shunt capability of the drive is exceeded.                                                                                                                                                                  |

## Drive Hardware and Input Power Configurations

Typical Kinetix 5500 systems include single-phase and three-phase standalone configurations, three-phase shared AC, shared AC/DC, shared DC, and shared AC/DC hybrid configurations.

## Standalone Configurations

In these examples, a single standalone drive is shown with and without the Bulletin 2198 capacitor module.

Figure 1 - Typical Kinetix 5500 Standalone Installation

<!-- image -->

In this example, three-phase AC power and 24V control power is shared in a multi-axis configuration. All drives must have the same power rating (catalog number).

Figure 2 - Typical Shared AC Installations

<!-- image -->

IMPORTANT

In shared AC configurations, all drives must have the same power rating. Shared AC configurations do not support Bulletin 2198 capacitor modules.

## Shared AC/DC Configurations

In this example, three-phase AC input power, 24V control power, and DC-bus power are shared in a multi-axis configuration. All drives must be the same power rating (catalog number).

Figure 3 - Typical Shared AC/DC Installations

<!-- image -->

IMPORTANT

In shared AC/DC configurations, all drives must have the same power rating (catalog number).

## Shared DC Common-bus Configurations

In this multi-axis example, the common-bus leader (sourcing) drive receives three-phase AC input power and supplies DC power to common-bus follower (sinking) drives. The common-bus leader-drive power rating is greater than or equal to the power rating of each follower drive.

Figure 4 - Typical Shared DC Common-bus Installations

<!-- image -->

(

IMPORTANT

In shared DC common-bus configurations, the leader drive power rating must be greater than or equal to the power rating of the follower drives.

## Shared AC/DC Hybrid Configuration

In this multi-axis example, three-phase AC input power is supplied to two converter drives. The converter drive ratings must be the same, and greater than or equal to the power ratings of the inverter drives. This parallel converter configuration increases the DC-bus power supplied to the inverter drives.

Figure 5 - Typical Shared AC/DC Bus Hybrid Installations

<!-- image -->

IMPORTANT

In shared AC/DC hybrid configuration, the converter drives must have the same power rating and must be greater than or equal to the power ratings of the inverter drives.

## Motor Feedback and Feedback-only Configurations

Feedback connections are made at the 2-pin motor feedback (MF) connector. These examples illustrate how you can use the Bulletin 2198 connector kits for making these connections. To see motor power and brake connections, refer to Chapter 5 beginning on page 69 .

Figure 6 - Feedback Configuration Examples

<!-- image -->

## IMPORTANT

In 2198-H2DCK converter kit applications, you can replace the 2090-CPxM7DF power/brake cable with a 2090-CSxM1DF/DG single motor cable, and reuse the 2090-CFBM7DF feedback cable. This increases the maximum cable length for 18 AWG and 14 AWG single cables to 50 m (164 ft). 2090-CSBM1DF-10AFxx and 2090-CSBM1DG-10xxxx (10 AWG) cables do not support this 50 m (164 ft) option.

## Typical Communication Configurations

The Kinetix 5500 drives support any Ethernet topology including linear, ring, and star by using ControlLogix, GuardLogix, or CompactLogix controllers.

These examples feature the CompactLogix 5370 programmable automation controllers (Bulletin 1769) with support for Integrated Motion over the EtherNet/IP network.

See CompactLogix Controllers Specifications Technical Data, publication 1769-TD005, for more information on CompactLogix 5370 L1, L2, and L3 controllers.

## Linear Topology

In this example, all devices are connected in linear topology. The Kinetix 5500 drives include dual-port connectivity, however, if any device becomes disconnected, all devices downstream of that device lose communication. Devices without dual ports must include the 1783-ETAP module or be connected at the end of the line.

Figure 7 - Kinetix 5500 Linear Communication Installation

<!-- image -->

## Ring Topology

In this example, the devices are connected by using ring topology. If only one device in the ring is disconnected, the rest of the devices continue to communicate. For ring topology to work correctly, a Device Level Ring (DLR) supervisor is required (for example, the Bulletin 1783 ETAP device). DLR is an ODVA standard. For more information, see the EtherNet/IP Embedded Switch Technology Application Guide, publication ENET-AP005 .

Devices without dual ports, for example the display terminal, require a 1783-ETAP module to complete the network ring.

Figure 8 - Kinetix 5500 Ring Communication Installation

<!-- image -->

## Star Topology

In this example, the devices are connected by using star topology. Each device is connected directly to the switch.

Kinetix 5500 drives have dual ports, so linear topology is maintained from drive-to-drive, but Kinetix 5500 drives and other devices operate independently. The loss of one device does not impact the operation of other devices.

Figure 9 - Kinetix 5500 Star Communication Installation

<!-- image -->

You can use the 842E-CM integrated motion encoder for applications requiring an external encoder for gearing or camming to the Kinetix 5500 drive. By providing auxiliary feedback directly through the EtherNet/IP network, the 842E-CM encoder helps eliminate the need for point-to-point wiring while letting customers use the encoder in a variety of network topologies. For more information, see the 842E-CM Integrated Motion on EtherNet/IP Product Profile, publication 842ECM-PP001 .

## Safe Torque Off Configurations

Kinetix 5500 servo drives are available with Safe Torque Off via hardwired connections or integrated over the EtherNet/IP network. These examples illustrate the Safe Torque Off configuration options.

## Hardwired Safety Configuration

The 2198-Hxxx-ERS drives use the Safe Torque Off (STO) connector for wiring external safety devices and cascading hardwired safety connections from one drive to another.

Figure 10 - Safe Torque Off (hardwired) Configuration

<!-- image -->

## Integrated Safety Configurations

The GuardLogix 5570 or Compact GuardLogix 5370 safety controller issues the Safe Torque Off (STO) command over the EtherNet/IP network and the

2198-Hxxx-ERS2 integrated safety drive executes the command.

In this example, a single GuardLogix safety controller makes a Motion and Safety connection with the 2198-Hxxx-ERS2 integrated safety drives.

## IMPORTANT

If only one controller is used in an application with Motion and Safety connections, the controller must be one of the following:

- A GuardLogix 5570 controller or GuardLogix 5580 safety controller
- A Compact GuardLogix 5370 controller of Compact GuardLogix 5380 safety controller

## Figure 11 - Motion and Safety Configuration (single controller)

<!-- image -->

In this example, a non-safety controller makes the Motion-only connection and a separate GuardLogix safety controller makes the Safety-only connection with 2198-Hxxx-ERS2 integrated safety drives.

## IMPORTANT

If two controllers are used in an application with Motion-only and Safety-only connections, the controllers must be any of the following:

- The Safety-only connection must be a GuardLogix 5570 controller, GuardLogix 5580 safety controller, Compact GuardLogix 5370 controller, or Compact GuardLogix 5380 safety controller
- The Motion-only connection must be a ControlLogix 5570 controller, ControlLogix 5580 safety controller, CompactLogix 5370 controller, or CompactLogix 5380 safety controller.

Figure 12 - Motion and Safety Configuration (multi-controller)

<!-- image -->

## Catalog Number Explanation

Kinetix 5500 drive catalog numbers and performance specifications.

Table 3 - Kinetix 5500 Servo Drive Catalog Numbers

| Drive Cat. No. (integrated STO)   | Frame Size Input Voltage   |                                                                                | Continuous Output Power kW   | Output Current                | Output Current   |
|-----------------------------------|----------------------------|--------------------------------------------------------------------------------|------------------------------|-------------------------------|------------------|
| Drive Cat. No. (integrated STO)   | Frame Size Input Voltage   |                                                                                | Continuous Output Power kW   | Continuous A 0-pk Peak A 0-pk |                  |
| 2198-H003-ERS 2198-H003-ERS2      | 1                          | 195…264V rms, single-phase 195…264V rms, three-phase 324…528V rms, three-phase | 0.2 kW 0.3 kW 0.6 kW         | 1.4 3.5                       |                  |
| 2198-H008-ERS 2198-H008-ERS2      | 1                          | 195…264V rms, single-phase 195…264V rms, three-phase 324…528V rms, three-phase | 0.5 kW 0.8 kW 1.6 kW         | 3.5 8.8                       |                  |
| 2198-H015-ERS 2198-H015-ERS2      | 2                          | 195…264V rms, single-phase 195…264V rms, three-phase 324…528V rms, three-phase | 1.0 kW 1.5 KW 3.2 kW         | 7.1 17.7                      |                  |
| 2198-H025-ERS 2198-H025-ERS2      | 2                          | 195…264V rms, three-phase 324…528V rms, three-phase                            | 2.4 kW 5.1 kW                | 11.3 28.3                     |                  |
| 2198-H040-ERS 2198-H040-ERS2      | 2                          | 195…264V rms, three-phase 324…528V rms, three-phase                            | 4.0 kW 8.3 kW                | 18.4 45.9                     |                  |
| 2198-H070-ERS 2198-H070-ERS2 3    |                            | 195…264V rms, three-phase 324…528V rms, three-phase                            | 7.0 kW 14.6 kW               | 32.5 81.3                     |                  |

Table 4 - Capacitor Module Catalog Number

| Capacitor Module Cat. No.       | Frame Size Rated Voltage Capacitance   |              |
|---------------------------------|----------------------------------------|--------------|
| 2198-CAPMOD-1300 2 650V DC, nom |                                        | 1360 µF, min |

Table 5 - Shared-bus Connector Kit Catalog Numbers

| Kit Cat. No.                  | Frame Size                                                                                                                | Application                       | Description                                                                            |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------|
| 2198-H040-ADP-IN Frame 1 or 2 |                                                                                                                           | First drive                       | • Mains AC input wiring connector • 24V DC input wiring connector • DC bus T-connector |
| 2198-H040-A-T                 | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | AC sharing only                   | AC bus T-connector                                                                     |
| 2198-H040-D-T                 | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | DC sharing only                   | DC bus T-connector                                                                     |
| 2198-H040-P-T                 | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | Control power sharing only        | Control power T-connector                                                              |
| 2198-H040-AD-T                | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | AC and DC-bus sharing             | AC and DC bus T-connectors                                                             |
| 2198-H040-AP-T                | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | AC and control power sharing      | AC and control power T-connectors                                                      |
| 2198-H040-DP-T                | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | DC and control power sharing      | DC and control power T-connectors                                                      |
| 2198-H040-ADP-T               | Next drive is… Frame 1 drives: 2198-H003-ERSx 2198-H008-ERSx Frame 2 drives: 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | AC, DC, and control power sharing | AC, DC, and control power T-connectors                                                 |
| 2198-H070-ADP-IN              | Frame 3 drive: 2198-H070-ERSx                                                                                             | First drive                       | • Mains AC input wiring connector • 24V DC input wiring connector • DC bus T-connector |
| 2198-H070-A-T                 | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | AC sharing only                   | AC bus T-connector                                                                     |
| 2198-H070-D-T                 | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | DC sharing only                   | DC bus T-connector                                                                     |
| 2198-H070-P-T                 | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | Control power sharing only        | Control power T-connector                                                              |
| 2198-H070-AD-T                | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | AC and DC-bus sharing             | AC and DC bus T-connectors                                                             |
| 2198-H070-AP-T                | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | AC and control power sharing      | AC and control power T-connectors                                                      |
| 2198-H070-DP-T                | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | DC and control power sharing      | DC and control power T-connectors                                                      |
| 2198-H070-ADP-T               | Next drive is… Frame 3 drives: 2198-H070-ERSx                                                                             | AC, DC, and control power sharing | AC, DC, and control power T-connectors                                                 |

## Agency Compliance

Table 6 - Drive-to-Motor Maximum Cable Length

|                                              | Kinetix VP Servo Motors m (ft)                                                                                    | Kinetix VP Servo Motors m (ft)                                                                                    | Other Compatible Rotary Motors/Linear Actuators (1)                 |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Kinetix 5500 Servo Drive Cat. No.            | Standard (non-flex) Cables Cat. No. 2090-CSxM1DF-xxAAxx Cat. No. 2090-CSxM1DG-xxxAxx Cat. No. 2090-CSxM1E1-xxVAxx | Continuous-flex Cables (2) Cat. No. 2090-CSBM1DF-xxAFxx Cat. No. 2090-CSBM1DG-xxxFxx Cat. No. 2090-CSBM1E1-xxxFxx | Kinetix 2090 Motor/Actuator Cables (3) Cat. No. 2090-CxxM7DF m (ft) |
| 2198-H003-ERSx 2198-H008-ERSx                | 50 (164)                                                                                                          | 30 (98.4)                                                                                                         | 20 (65.6)                                                           |
| 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | 50 (164)                                                                                                          | 30 (98.4)                                                                                                         | 20 (65.6)                                                           |
| 2198-H070-ERSx                               | 50 (164)                                                                                                          | 30 (98.4)                                                                                                         | 20 (65.6)                                                           |

- Install the Kinetix 5500 system inside an approved enclosure. Run input power wiring in conduit (grounded to the enclosure) outside of the enclosure. Separate signal and power cables.
- Separate input power wiring from control wiring and motor cables.

See Appendix A on page 179 for input power wiring and drive/motor interconnect diagrams.

If this product is installed within the European Union and has the CE mark, or within the United Kingdom and has the UKCA mark, the following regulations apply.

<!-- image -->

ATTENTION: Meeting CE and UK requires a grounded system and the method of grounding the AC line filter and drive must match. Failure to do this renders the filter ineffective and can damage the filter. For grounding examples, refer to Grounded Power Configurations on page 71 .

For more information on electrical noise reduction, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

To meet CE and UK requirements, these requirements apply:

- Install an AC line filter (catalog number 2198-DBxxF or 2198-DBRxx-F). For specific pairing information for input power as close to the Kinetix 5500 drive as possible, see Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications, publication KNX-TD003 .
- Bond drive, capacitor module, and line filter grounding screws by using a braided ground strap as shown in Figure 43 on page 76 .
- Use Kinetix 2090 single motor cables with Kinetix VP servo motors and actuators. Use Kinetix 2090 motor power/brake and feedback cables for other compatible AllenBradley® motors and actuators.
- Combined motor cable length for all axes on the same DC bus must not exceed 250 m (820 ft). Drive-to-motor cables must not exceed 50 m (164 ft); however, use of continuous-flex cable and 2198-H2DCK converter kit limits the maximum length.

## System Design Guidelines

<!-- image -->

## Plan the Kinetix 5500 Drive System Installation

This chapter describes system installation guidelines that are used in preparation for mounting your Kinetix® 5500 drive components.

| Topic                      |   Page |
|----------------------------|--------|
| System Design Guidelines   |     31 |
| Electrical Noise Reduction |     40 |

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry and result in damage to the components.

Use the information in this section when designing your enclosure and planning to mount your system components on the panel.

For online product selection and system configuration tools, including AutoCAD (DXF) drawings of the product, refer to https://www.rockwellautomation.com/en-us/support/product/product-selectionconfiguration.html .

## System Mounting Requirements

- To comply with UL, CE, and UK requirements, the Kinetix 5500 drive systems must be enclosed in a grounded conductive enclosure offering protection as defined in standard IEC 60529 to IP20 such that they are not accessible to an operator or unskilled person. A NEMA 4X enclosure exceeds these requirements providing protection to IP66.

To maintain the functional safety rating of the Kinetix 5500 drive system, this enclosure must be appropriate for the environmental conditions of the industrial location and provide a protection class of IP54 or higher.

- The panel that you install inside the enclosure for mounting your system components must be on a flat, rigid, vertical surface that is not subjected to shock, vibration, moisture, oil mist, dust, or corrosive vapors in accordance with pollution degree 2 (IEC 61800-5-1). These conditions are required because the product is rated to protection class IP20 (IEC 60529).
- Size the drive enclosure so as not to exceed the maximum ambient temperature rating. Consider heat dissipation specifications for all drive components.
- Combined motor power cable length for all axes on the same DC bus must not exceed 250 m (820 ft). Drive-to-motor cables must not exceed 50 m (164 ft), however use of continuous-flex cable and 2198-H2DCK converter kit limits the maximum length. See Table 6 on page 30 for specifications by frame size.

## IMPORTANT

System performance was tested at these cable length specifications. These limitations also apply when meeting CE and UK requirements.

- Use high-frequency (HF) bonding techniques to connect the modules, enclosure, machine frame, and motor housing, and to provide a low-impedance return path for high-frequency (HF) energy and reduce electrical noise.

Bond drive, capacitor module, and line filter grounding screws by using a braided ground strap as shown in Figure 43 on page 76 .

See the System Design for Control of Electrical Noise Reference Manual, publication GMCRM001, to better understand the concept of electrical noise reduction.

## AC Line Filter Selection

An AC line filter is required to meet CE and UK requirements. Install an AC line filter for input power as close to the 2198-Hxxx-ERSx drive as possible.

## IMPORTANT

AC line filters are only recommended with grounded wye power configurations. For facility power configuration examples, see Determine the Input Power Configuration on page 71 .

Table 7 - AC Line Filter Selection

| Kinetix Drive Module Cat. No.                | AC Line Filter Cat. No.         |
|----------------------------------------------|---------------------------------|
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx | 2198-DB08-F                     |
| 2198-H025-ERSx 2198-H040-ERSx                | • 2198-DBR20-F or • 2198-DB20-F |
| 2198-H070-ERSx                               | • 2198-DBR40-F or • 2198-DB42-F |

## IMPORTANT

Use 2198-DBxx-F line filters only as field replacements in existing installations. Select 2198-DBRxx-F line filters for all new systems or to replace existing 2198-DBxx-F line filters. This does not apply to 2198-DB08-F line filters.

Table 8 - AC Line Filter Selection for Shared AC, Shared AC/DC, and Hybrid Multi-axis Systems

| Kinetix 5500 Drives   | Drive Voltage (three-phase),   |                                      | AC Line Filter Cat. No.                          |
|-----------------------|--------------------------------|--------------------------------------|--------------------------------------------------|
| Cat. No.              | Nom                            |                                      | 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes |
| 2198-H003-ERSx        | 240/480V 2198-DBR20-F          |                                      |                                                  |
| 2198-H008-ERSx        | 240/480V 2198-DBR20-F          |                                      |                                                  |
| 2198-H015-ERSx        | 240/480V 2198-DBR20-F —        |                                      |                                                  |
| 2198-H025-ERSx        | 240/480V 2198-DBR40-F —        |                                      |                                                  |
| 2198-H040-ERSx        |                                | 240/480V 2198-DBR40-F 2198-DBR90-F — | 240/480V 2198-DBR40-F 2198-DBR90-F —             |
| 2198-H070-ERSx        | 240/480V 2198-DBR90-F —        |                                      |                                                  |

## Transformer Selection

The servo drive does not require an isolation transformer for three-phase input power. However, a transformer can be required to match the voltage requirements of the drive to the available service.

To size a transformer for the main AC power inputs, refer to the Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications Technical Data, publication KNX-TD003 .

| IMPORTANT   | When using an autotransformer, make sure that the phase to neutral/ ground voltage does not exceed the input voltage ratings of the drive.                                                                                             |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Use a form factor of 1.5 for three-phase power (where form factor is used to compensate for transformer, drive module, and motor losses, and to account for utilization in the intermittent operating area of the torque speed curve). |
| IMPORTANT   | A line reactor must be used if the source transformer is greater than 150 KVA, maximum and 3% impedance, minimum                                                                                                                       |
| EXAMPLE     | Sizing a transformer to the voltage requirements of this drive: 2198-H040-ERSx = 8.4 kW = 12.6 KVA transformer.                                                                                                                        |

## Circuit Breaker/Fuse Selection

The Kinetix 5500 drives use internal solid-state motor short-circuit protection and, when protected by suitable branch circuit protection, are rated for use on a circuit capable of delivering up to 200,000 A (fuses) and 65,000 A (circuit breakers).

For the wiring diagram, refer to Power Wiring Examples on page 179 .

<!-- image -->

ATTENTION: Do not use circuit protection devices on the output of an AC drive as an isolating disconnect switch or motor overload device. These devices are designed to operate on sine wave voltage and the drive's PWM waveform does not allow it to operate properly. As a result, damage to the device occurs.

Standalone Drive Systems

Table 9 - Standalone Drive System Specifications for UL and IEC (non-UL) Applications

| Kinetix 5500 Drives   | Kinetix 5500 Drives   | UL Applications                             | UL Applications                                                                                    |
|-----------------------|-----------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------|
| Drive Cat. No.        | Drive Voltage, Nom    | Phase  Bussmann Fuses Cat. No.              | Molded Case CB Cat. No.  DIN gG Fuses Amps (max)  Molded Case CB Cat. No.                          |
| 2198-H003-ERSx        |                       |                                             | 240V Single-phase KTK-R-2 140U-D6D2-B10 and 140UT-D7D2-B10 2 140U-D6D2-B10 and 140UT-D7D2-B10      |
| 2198-H003-ERSx        |                       |                                             | 240/480V Three-phase KTK-R-3 140U-D6D3-B20 and 140UT-D7D3-B20 4 140U-D6D3-B20 and 140UT-D7D3-B20   |
| 2198-H008-ERSx        |                       |                                             | 240V Single-phase KTK-R-5 140U-D6D2-B20 and 140UT-D7D2-B20 6 140U-D6D2-B20 and 140UT-D7D2-B20      |
| 2198-H008-ERSx        |                       |                                             | 240/480V Three-phase KTK-R-7 140U-D6D3-B60 and 140UT-D7D3-B60 6 140U-D6D3-B60 and 140UT-D7D3-B60   |
| 2198-H015-ERSx        |                       |                                             | 240V Single-phase KTK-R-10 140U-D6D2-B80 and 140UT-D7D2-B80 10 140U-D6D2-B80 and 140UT-D7D2-B80    |
| 2198-H015-ERSx        |                       |                                             | 240/480V Three-phase KTK-R-15 140U-D6D3-C12 and 140UT-D7D3-C12 16 140U-D6D3-C12 and 140UT-D7D3-C12 |
| 2198-H025-ERSx        |                       |                                             | 240/480V Three-phase KTK-R-20 140U-D6D3-C20 and 140UT-D7D3-C20 20 140U-D6D3-C20 and 140UT-D7D3-C20 |
| 2198-H040-ERSx        |                       |                                             | 240/480V Three-phase KTK-R-25 140U-D6D3-C25 and 140UT-D7D3-C25 25 140U-D6D3-C25 and 140UT-D7D3-C25 |
| 2198-H070-ERSx        |                       | 240/480V Three-phase LPJ-35SP 140G-G6C3-C40 | 35 140G-G6C3-C40                                                                                   |

## Shared DC (common-bus) Drive Systems

Table 10 - Shared DC Drive System Specifications for UL and IEC (non-UL) Applications

| Kinetix 5500 Drives   | UL Applications         | UL Applications                                                                        |                                                                                        |
|-----------------------|-------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Drive Cat. No.        | Bussmann Fuses Cat. No. | Drive Voltage (three-phase), Nom Molded Case CB Cat. No.  Amps (max)                   | DIN gG Fuses Molded Case CB Cat. No.                                                   |
| 2198-H003-ERSx        |                         | 240/480V KTK-R-10 140U-D6D3-C15 and 140UT-D7D3-C15 10                                  | 140U-D6D3-C15 and 140UT-D7D3-C15                                                       |
| 2198-H008-ERSx        |                         | 240/480V KTK-R-10 140U-D6D3-C15 and 140UT-D7D3-C15 10                                  | 140U-D6D3-C15 and 140UT-D7D3-C15                                                       |
| 2198-H015-ERSx        |                         | 240/480V KTK-R-15 140U-D6D3-C15 and 140UT-D7D3-C15 16                                  | 140U-D6D3-C15 and 140UT-D7D3-C15                                                       |
| 2198-H025-ERSx        |                         |                                                                                        | 240/480V KTK-R-20 140U-D6D3-C20 and 140UT-D7D3-C20 20 140U-D6D3-C20 and 140UT-D7D3-C20 |
| 2198-H040-ERSx        |                         | 240/480V KTK-R-25 140U-D6D3-C25 and 140UT-D7D3-C25 25 140U-D6D3-C25 and 140UT-D7D3-C25 |                                                                                        |
| 2198-H070-ERSx        |                         | 240/480V LPJ-35SP 140G-G6C3-C40                                                        | 35 140G-G6C3-C40                                                                       |

## Shared AC Drive Systems

Table 11 - Input Power UL Circuit-protection Specifications

| Kinetix 5500 Drives   | Kinetix 5500 Drives              |                                                         | Molded Case CB Cat. No.          | Molded Case CB Cat. No.          | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|-----------------------|----------------------------------|---------------------------------------------------------|----------------------------------|----------------------------------|---------------------------|---------------------------|
| Drive Cat. No.        | Drive Voltage (three-phase), Nom | 2 Axes 3 Axes 4 Axes 5 Axes 2 Axes 3 Axes 4 Axes 5 Axes |                                  |                                  |                           |                           |
| 2198-H003-ERSx        | 240/480V KTK-R-15                |                                                         | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 |                           |                           |
| 2198-H008-ERSx        | 240/480V KTK-R-15                |                                                         | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 |                           |                           |
| 2198-H015-ERSx        | 240/480V KTK-R-20 KTK-R-25 —     |                                                         | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C20 and 140UT-D7D3-C20 | —                         |                           |
| 2198-H025-ERSx        | 240/480V KTK-R-30                | —                                                       | 140U-D6D3-C25 and 140UT-D7D3-C25 | 140U-D6D3-C30 and 140UT-D7D3-C30 | —                         |                           |
| 2198-H040-ERSx        | 240/480V LPJ-35SP LPJ-45SP —     |                                                         |                                  | 140G-G6C3-C40 140G-G6C3-C50 —    |                           |                           |
| 2198-H070-ERSx        | 240/480V LPJ-60SP —              |                                                         | 140G-G6C3-C60 —                  |                                  |                           |                           |

Table 12 - Input Power IEC (non-UL) Circuit-protection Specifications

| Kinetix 5500 Drives   | Kinetix 5500 Drives              |                                    |    | Molded Case CB Cat. No.          | Molded Case CB Cat. No.          | Molded Case CB Cat. No.          | Molded Case CB Cat. No.          |
|-----------------------|----------------------------------|------------------------------------|----|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Drive Cat. No.        | Drive Voltage (three-phase), Nom | 2 Axes 3 Axes 4 Axes 5 Axes 2 Axes |    |                                  |                                  | 3 Axes 4 Axes 5 Axes             |                                  |
| 2198-H003-ERSx        | 240/480V 16                      |                                    |    | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 |
| 2198-H008-ERSx        | 240/480V 16                      |                                    |    | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C15 and 140UT-D7D3-C15 |
| 2198-H015-ERSx        | 240/480V 20 25 —                 |                                    |    | 140U-D6D3-C15 and 140UT-D7D3-C15 | 140U-D6D3-C20 and 140UT-D7D3-C20 | —                                | —                                |
| 2198-H025-ERSx        | 240/480V 32                      |                                    | —  | 140U-D6D3-C25 and 140UT-D7D3-C25 | 140U-D6D3-C30 and 140UT-D7D3-C30 | —                                | —                                |
| 2198-H040-ERSx        | 240/480V 35 50                   |                                    |    |                                  | 140G-G6C3-C40 140G-G6C3-C50 —    |                                  |                                  |
| 2198-H070-ERSx        | 240/480V 63 —                    |                                    |    | 140G-G6C3-C60 —                  |                                  |                                  |                                  |

Shared AC/DC and Hybrid Systems

Table 13 - Input Power UL Circuit-protection Specifications

| Kinetix 5500 Drives   | Kinetix 5500 Drives              | Bussmann Fuse Cat. No.                                      | Bussmann Fuse Cat. No.                                                                            | Bussmann Fuse Cat. No.                                      | Molded Case CB Cat. No.                                     | Molded Case CB Cat. No.                                     | Molded Case CB Cat. No.   | Molded Case CB Cat. No.          | Molded Case CB Cat. No.          | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|-----------------------|----------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|---------------------------|----------------------------------|----------------------------------|---------------------------|---------------------------|
| Drive Cat. No.        | Drive Voltage (three-phase), Nom |                                                             | 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes |                                                             |                                                             |                                                             |                           |                                  |                                  |                           |                           |
| 2198-H003-ERSx        |                                  | 240/480V KTK-R-10 KTK-R-15 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V KTK-R-10 KTK-R-15 140U-D6D3-C15 and 140UT-D7D3-C15                                       | 240/480V KTK-R-10 KTK-R-15 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V KTK-R-10 KTK-R-15 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V KTK-R-10 KTK-R-15 140U-D6D3-C15 and 140UT-D7D3-C15 |                           |                                  |                                  |                           |                           |
| 2198-H008-ERSx        |                                  | 240/480V KTK-R-15 KTK-R-20 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V KTK-R-15 KTK-R-20 140U-D6D3-C15 and 140UT-D7D3-C15                                       | 240/480V KTK-R-15 KTK-R-20 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V KTK-R-15 KTK-R-20 140U-D6D3-C15 and 140UT-D7D3-C15 |                                                             |                           | 140U-D6D3-C20 and 140UT-D7D3-C20 | 140U-D6D3-C20 and 140UT-D7D3-C20 |                           |                           |
| 2198-H015-ERSx        |                                  | 240/480V KTK-R-20                                           | 240/480V KTK-R-20                                                                                 | —                                                           | 140U-D6D3-C15 and 140UT-D7D3-C15                            | 140U-D6D3-C20 and 140UT-D7D3-C20                            | —                         | —                                | —                                | —                         |                           |

Table 13 - Input Power UL Circuit-protection Specifications (Continued)

| Kinetix 5500 Drives   | Kinetix 5500 Drives              | Bussmann Fuse Cat. No.                | Molded Case CB Cat. No.             | Molded Case CB Cat. No.          | Molded Case CB Cat. No.   | Molded Case CB Cat. No.                                                                           | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|-----------------------|----------------------------------|---------------------------------------|-------------------------------------|----------------------------------|---------------------------|---------------------------------------------------------------------------------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Drive Cat. No.        | Drive Voltage (three-phase), Nom |                                       |                                     |                                  |                           | 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes |                           |                           |                           |                           |
| 2198-H025-ERSx        |                                  | 240/480V KTK-R-30 —                   | 140U-D6D3-C20 and 140UT-D7D3-C20    | 140U-D6D3-C30 and 140UT-D7D3-C30 | —                         |                                                                                                   |                           |                           |                           |                           |
| 2198-H040-ERSx        |                                  | 240/480V KTK-R-30 LPJ-45SP LPJ-50SP — | 140U-D6D3-C30 and 140UT-D7D3-C30    | 140G-G6C3-C50                    | —                         |                                                                                                   |                           |                           |                           |                           |
| 2198-H070-ERSx        |                                  |                                       | 240/480V LPJ-50SP — 140G-G6C3-C50 — |                                  |                           |                                                                                                   |                           |                           |                           |                           |

## Table 14 - Input Power IEC (non-UL) Circuit-protection Specifications

| Kinetix 5500 Drives   | Kinetix 5500 Drives              |    | Molded Case CB Cat. No.                         | Molded Case CB Cat. No.                         | Molded Case CB Cat. No.                                                                           | Molded Case CB Cat. No.                         | Molded Case CB Cat. No.          | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   | Molded Case CB Cat. No.   |
|-----------------------|----------------------------------|----|-------------------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------|----------------------------------|---------------------------|---------------------------|---------------------------|
| Drives Cat. No.       | Drive Voltage (three-phase), Nom |    |                                                 |                                                 | 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes 2 Axes 3 Axes 4 Axes 5 Axes 6 Axes 7 Axes 8 Axes |                                                 |                                  |                           |                           |                           |
| 2198-H003-ERSx        |                                  |    | 240/480V 10 16 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V 10 16 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V 10 16 140U-D6D3-C15 and 140UT-D7D3-C15                                                   | 240/480V 10 16 140U-D6D3-C15 and 140UT-D7D3-C15 |                                  |                           |                           |                           |
| 2198-H008-ERSx        |                                  |    | 240/480V 16 20 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V 16 20 140U-D6D3-C15 and 140UT-D7D3-C15 | 240/480V 16 20 140U-D6D3-C15 and 140UT-D7D3-C15                                                   | 140U-D6D3-C20 and 140UT-D7D3-C20                | 140U-D6D3-C20 and 140UT-D7D3-C20 |                           |                           |                           |
| 2198-H015-ERSx        | 240/480V 20                      | –  | 140U-D6D3-C15 and 140UT-D7D3-C15                | 140U-D6D3-C20 and 140UT-D7D3-C20                | –                                                                                                 |                                                 |                                  |                           |                           |                           |
| 2198-H025-ERSx        | 240/480V 32                      | —  | 140U-D6D3-C20 and 140UT-D7D3-C20                | 140U-D6D3-C30 and 140UT-D7D3-C30                | —                                                                                                 |                                                 |                                  |                           |                           |                           |
| 2198-H040-ERSx        | 240/480V 32 50                   | —  | 140U-D6D3-C30 and 140UT-D7D3-C30                | 140G-G6C3-C50 —                                 | 140G-G6C3-C50 —                                                                                   |                                                 |                                  |                           |                           |                           |
| 2198-H070-ERSx        | 240/480V 50 —                    |    | 140G-G6C3-C50 —                                 |                                                 |                                                                                                   |                                                 |                                  |                           |                           |                           |

## 24V Control Power Evaluation

The Kinetix 5500 drive system requires 24V DC input for its control circuitry. Due to the 24V shared-bus connection system and the 24V current requirements of the Kinetix 5500 drives, a thorough evaluation of control power is required before implementation. Consider the following when sizing such a system:

- Verify that the 24V DC power supply is capable of supplying the 24V current requirements of your Kinetix 5500 drive system. See Control Power Current Calculations on page 208 to determine the 24V current requirements.

For systems with a high 24V current demand, consider installing a separate 24V power supply for each bus group or change the bus group configuration to more evenly divide the 24V current demand.

- Verify that the wiring being used is capable of supplying the Kinetix 5500 drive system with a voltage within the 24V input-voltage range; 24V ±10% (21.6…26.4V DC). Consider the following:
- Mount the 24V power supply as close to the Kinetix 5500 drive system as possible to minimize input voltage drop.
- Install larger gauge wire, up to 2.5 mm 2 (14 AWG) for 24V control power when using the CP connectors included with the module; or use the 24V shared-bus connection

## IMPORTANT

The 24V current demand, wire gauge, and wire length all impact the voltage drop across the wiring being used.

## Contactor Selection

You can use an AC three-phase contactor to supply AC input power to the Kinetix 5500 drive. Follow these guidelines when selecting a contactor for your drive system.

- Make sure that the contactor is capable of supporting a higher amp rating than the input fuse/circuit breaker you selected from the tables in Circuit Breaker/Fuse Selection on page 33
- Select a contactor with a voltage rating and SCCR rating appropriate for your drive installation
- Do not cycle power to the contactor more than once per minute to help prevent damage to the Kinetix 5500 drive

## Passive Shunt Considerations

The Kinetix 5500 drives all include an internal shunt that is wired to the shunt resistor (RC) connector at the factory. Bulletin 2097-Rx external passive shunts are available to provide additional shunt capacity for applications where the internal shunt capacity is exceeded.

IMPORTANT

Keep the internal shunt wires connected unless you have an external passive shunt to connect.

## Table 15 - Bulletin 2097 Passive Shunt Options

| Kinetix 5500 Drives Cat. No.   | Internal Shunt Specifications   | Internal Shunt Specifications   | External Shunt Resistor (1) Compatibility Cat. No.   | External Shunt Resistor (1) Compatibility Cat. No.   |
|--------------------------------|---------------------------------|---------------------------------|------------------------------------------------------|------------------------------------------------------|
| Kinetix 5500 Drives Cat. No.   |                                 | Ω W                             | 2097-R7 2097-R6                                      |                                                      |
| 2198-H003-ERSx                 | 100                             | 30                              | X —                                                  |                                                      |
| 2198-H008-ERSx                 | 100                             | 30                              | X —                                                  |                                                      |
| 2198-H015-ERSx                 | 60                              | 50                              | X —                                                  |                                                      |
| 2198-H025-ERSx                 | 60                              | 50                              | X —                                                  |                                                      |
| 2198-H040-ERSx                 | 60                              | 50                              | — X                                                  |                                                      |
| 2198-H070-ERSx                 | 40                              | 75                              | —  X                                                 |                                                      |

(1) Shunt resistor selection is based on the needs of your actual hardware configuration.

Catalog numbers 2097-R6 and 2097-R7 are shunt resistors without an enclosure.

Figure 13 - External Passive Shunts

<!-- image -->

Table 16 - External Shunt Module Specifications

| Shunt Module Cat. No.   | Resistance Ω   | Continuous Power W   | Weight, Approx kg (lb)   |
|-------------------------|----------------|----------------------|--------------------------|
|                         |                |                      | 2097-R6 75 150 0.3 (0.7) |
|                         |                |                      | 2097-R7 150 80 0.2 (0.4) |

How the Bulletin 2097-Rx shunts connect to Kinetix 5500 drives is explained in External Passive-shunt Resistor Connections on page 99 and illustrated with interconnect diagrams in Shunt Resistor Wiring Example on page 184 .

Table 17 - Power Dissipation Specifications

| Kinetix 5500 Drive Cat. No.    | Frame Size   | Usage as Percentage of Rated Power Output (watts)   | Usage as Percentage of Rated Power Output (watts)   | Usage as Percentage of Rated Power Output (watts)   | Usage as Percentage of Rated Power Output (watts)   | Usage as Percentage of Rated Power Output (watts)   |
|--------------------------------|--------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
|                                |              |                                                     | 20% 40% 60% 80% 100%                                |                                                     |                                                     |                                                     |
| 2198-H003-ERSx  2198-H008-ERSx |              |                                                     | 1 12 25 37 50 62                                    |                                                     |                                                     |                                                     |
| 2198-H015-ERSx 2198-H025-ERSx  |              |                                                     | 2 40 80 120 160 200                                 |                                                     |                                                     |                                                     |
| 2198-H070-ERSx                 |              |                                                     | 3 64 128 192 256 320                                |                                                     |                                                     |                                                     |

## Enclosure Selection

This example is provided to assist you in sizing an enclosure for your Kinetix 5500 drive system. You need heat dissipation data from all components that are planned for your enclosure to calculate the enclosure size (refer to Table 17 on page 38).

With no active method of heat dissipation (such as fans or air conditioning), either of the following approximate equations can be used.

| Metric                                                    | Standard English                                          |
|-----------------------------------------------------------|-----------------------------------------------------------|
| Where T is the temperature difference between inside ° p air and outside ambient (°C), Q is the heat that is generated in the enclosure (Watts), and A is enclosure surface area (m 2 an enclosure is calculated as follows: A =  0.38Q 1.8T - 1.1                                                           | A =  4.08Q T - 1.1                                        |
| ). The exterior surface of all six sides of               | Where T is the temperature difference between inside ° p air and outside ambient (°F), Q is the heat that is generated in enclosure (Watts), and A is enclosure surface area (ft2). The exterior surface of all six sides of an enclosure is calculated as follows:                                                           |
| A = 2dw + 2dh + 2wh                                       | A = (2dw + 2dh + 2wh) /144                                |
| Where d (depth), w (width), and h (height) are in meters. | Where d (depth), w (width), and h (height) are in meters. |

If the maximum ambient rating of the Kinetix 5500 drive system is 50 °C (122 °F) and if the
°° g y
maximum environmental temperature is 20 °C (68 °F), then T=30. In this example, the total heat dissipation is 416 W (sum of all components in enclosure). So, in the equation below, T=30 and Q=416.

<!-- formula-not-decoded -->

In this example, the enclosure must have an exterior surface of at least 2.99 m 2 . If any portion of the enclosure is not able to transfer heat, do not include that value in the calculation.

Because the minimum cabinet depth to house the Kinetix 5500 system (selected for this example) is 300 mm (11.8 in.), the cabinet must have approximately the following dimensions (height x width x depth):

1500 x 700 x 300 mm (59.0 x 27.6 x 11.8 in.).

<!-- formula-not-decoded -->

Because this cabinet size is considerably larger than what is necessary to house the system components, it can be more efficient to provide a means of cooling in a smaller cabinet. Contact your cabinet manufacturer for options available to cool your cabinet.

## Minimum Clearance Requirements

This section provides information to assist you in sizing your cabinet and positioning your Kinetix 5500 drive:

- Additional clearance is required for cables and wires or the shared-bus connection system that is connected to the top of the drive.
- Additional clearance is required if other devices are installed above and/or below the drive and have clearance requirements of their own.
- Additional clearance left and right of the drive is required when mounted next to noise sensitive equipment or clean wireways.
- The recommended minimum cabinet depth is 300 mm (11.81 in.).

Figure 14 - Minimum Clearance Requirements

40 mm (1.57 in.) clearance above drive for airflow and installation.

<!-- image -->

## IMPORTANT

Mount the drive in an upright position as shown. Do not mount the drive on its side.

In multi-axis shared-bus configurations, drives must be spaced by aligning the zero-stack tab and cutout.

Figure 15 - Multi-axis Shared-bus Clearance Requirements

<!-- image -->

Shared-bus connection system for bus-sharing configurations is not shown for clarity.

## Electrical Noise Reduction

This section outlines best practices that minimize the possibility of noise-related failures as they apply specifically to Kinetix 5500 system installations. For more information on the concept of high-frequency (HF) bonding, the Ground Plane principle, and electrical noise reduction, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## Bonding Modules

Bonding is the practice of connecting metal chassis, assemblies, frames, shields, and enclosures to reduce the effects of electromagnetic interference (EMI).

Unless specified, most paints are not conductive and act as insulators. To achieve a good bond between power rail and the subpanel, surfaces must be paint-free or plated. Bonding metal surfaces creates a low-impedance return path for high-frequency energy.

## IMPORTANT

To improve the bond between the power rail and subpanel, construct your subpanel out of zinc-plated (paint-free) steel.

Improper bonding of metal surfaces blocks the direct return path and allows high-frequency energy to travel elsewhere in the cabinet. Excessive high-frequency energy can affect the operation of other microprocessor-controlled equipment.

Figure 16 on page 41 shows recommended bonding practices for painted panels, enclosures, and mounting brackets.

<!-- image -->

## Bonding Multiple Subpanels

Bonding multiple subpanels creates a common low impedance exit path for the high frequency energy inside the cabinet. Subpanels that are not bonded together do not necessarily share a common low impedance path. This difference in impedance can affect networks and other devices that span multiple panels:

- Bond the top and bottom of each subpanel to the cabinet by using 25.4 mm (1.0 in.) by 6.35 mm (0.25 in.) wire braid. As a rule, the wider and shorter the braid is, the better the bond.
- Scrape the paint from around each fastener to maximize metal-to-metal contact.

Figure 17 - Multiple Subpanels and Cabinet Recommendations

<!-- image -->

## Establishing Noise Zones

Observe these guidelines when routing cables used in the Kinetix 5500 system:

- The clean zone (C) is right of the drive system and includes the digital inputs wiring and Ethernet cable (gray wireway).
- The dirty zone (D) is above and below the drive system (black wireways) and includes the circuit breakers, 24V DC power supply, safety, and motor cables.
- The very dirty zone (VD) is limited to where the AC line (EMC) filter VAC output jumpers over to the drive (or first drive in multi-axis systems). Shielded cable is required only if the very dirty cables enter a wireway.
- (1) When space to the right of the drive does not permit 150 mm (6.0 in.) separation, use a grounded steel shield instead. For examples, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (2) When the 2198-H2DCK converter kit is used, feedback cable routes in the clean wireway.

Figure 18 - Noise Zones

<!-- image -->

Table 18 - Kinetix 5500 Drive

|                                                           | Connector                                                 | Zone                              | Zone                              | Zone                              |                                   |                                   |
|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| Wire/Cable                                                | Connector                                                 | Very Dirty Dirty Clean            | Ferrite Sleeve  Shielded Cable    |                                   |                                   |                                   |
| L1, L2, L3 (shielded cable)                               | IPD                                                       |                                   | —X —— X                           |                                   |                                   |                                   |
| L1, L2, L3 (unshielded cable)                             | IPD                                                       | X — — — —                         |                                   |                                   |                                   |                                   |
| DC-/DC+ (DC bus)                                          | DC                                                        | Busbar only, no wiring connector. | Busbar only, no wiring connector. | Busbar only, no wiring connector. | Busbar only, no wiring connector. | Busbar only, no wiring connector. |
| DC+/SH (shunt)                                            | RC                                                        |                                   | — X — — —                         |                                   |                                   |                                   |
| U, V, W (motor power)                                     | MP X                                                      | —                                 | X                                 |                                   |                                   |                                   |
| Motor feedback                                            | MF  X                                                     | —                                 | — — X                             |                                   |                                   |                                   |
| Motor brake                                               | BC  X                                                     | —                                 | X                                 |                                   |                                   |                                   |
| U, V, W (motor power)                                     | MP X —                                                    | —                                 | X                                 |                                   |                                   |                                   |
| Motor feedback (1)                                        | MF  — X                                                   | —                                 | — X                               |                                   |                                   |                                   |
| Motor brake                                               | BC  X —                                                   | —                                 | X                                 |                                   |                                   |                                   |
| 24V DC                                                    | CP                                                        |                                   | — X — — —                         |                                   |                                   |                                   |
| Safety enable for Safe Torque Off (hardwired)  (2)        | STO — X — — —                                             |                                   |                                   |                                   |                                   |                                   |
| Registration input                                        | IOD                                                       |                                   | ——X — X                           |                                   |                                   |                                   |
| Dedicated digital inputs (other than registration inputs) | Dedicated digital inputs (other than registration inputs) |                                   | — X — — —                         |                                   |                                   |                                   |
| Ethernet                                                  | PORT1 PORT2                                               |                                   | ——X — X                           |                                   |                                   |                                   |

(1) When the 2198-H2DCK converter kit is used, the feedback cable routes in the clean wireway.

(2) STO connector applies to only 2198-Hxxx-ERS (hardwired) servo drives.

## Table 19 - Capacitor Module

|                     |           | Zone                              | Method                            | Method                            |                                   |                                   |
|---------------------|-----------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| Wire/Cable          | Connector | Very Dirty Dirty Clean            | Ferrite Sleeve                    | Shielded Cable                    |                                   |                                   |
| DC-/DC+ (DC bus) DC |           | Busbar only, no wiring connector. | Busbar only, no wiring connector. | Busbar only, no wiring connector. | Busbar only, no wiring connector. | Busbar only, no wiring connector. |
| 24V DC              | CP        |                                   | — X — — —                         |                                   |                                   |                                   |
| Module status       | MS        |                                   | — X — — —                         |                                   |                                   |                                   |

## Noise Reduction Guidelines for Drive Accessories

See this section when mounting an AC (EMC) line filter or external passive-shunt resistor for guidelines that are designed to reduce system failures caused by excessive electrical noise.

## AC Line Filters

Observe these guidelines when mounting your AC (EMC) line filter (refer to the figure on page 43 for an example):

- Mount the AC line filter on the same panel as the Kinetix 5500 drive and as close to the drive as possible.
- Good HF bonding to the panel is critical. For painted panels, refer to the examples on page 41 .
- Separate input and output wiring as far as possible.

## IMPORTANT

CE and UK test certification applies to only the AC line filter used with a single drive or the line filter used in multi-axis drive configurations. Sharing a line filter with more than one multi-axis drive configuration can perform satisfactorily, but the customer takes legal responsibility.

## Cable Categories for Kinetix 5500 Systems

These tables indicate the zoning requirements of cables connecting to the Kinetix 5500 drive components.

## External Passive Shunt Resistor

Observe these guidelines when mounting your Bulletin 2097 external passive-shunt resistor outside of the enclosure:

- Mount shunt resistor and wiring in the very dirty zone or in an external shielded enclosure.
- Mount resistors in a shielded and ventilated enclosure outside of the cabinet.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.

Figure 19 - External Shunt Resistor Outside the Enclosure

<!-- image -->

When mounting your Bulletin 2097 passive-shunt resistor inside the enclosure, follow these additional guidelines:

- Mount metal-clad modules anywhere in the dirty zone, but as close to the Kinetix 5500 drive as possible.
- Route shunt power wires with other very dirty wires.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.
- Separate shunt power cables from other sensitive, low voltage signal cables.

Figure 20 - External Shunt Resistor Inside the Enclosure

<!-- image -->

<!-- image -->

## Mount the Kinetix 5500 Drive System

This chapter provides the system installation procedures for mounting your Kinetix® 5500 drives to the system panel.

| Topic                         |   Page |
|-------------------------------|--------|
| Determine Mounting Order      |     48 |
| Drill-hole Patterns           |     51 |
| Mount Your Kinetix 5500 Drive |     58 |

This procedure assumes you have prepared your panel and understand how to bond your system. For installation instructions regarding equipment and accessories that are not included here, refer to the instructions that came with those products.

<!-- image -->

SHOCK HAZARD: To avoid a hazard of electrical shock, perform all mounting and wiring of the Kinetix 5500 drives before applying power. Once power is applied, connector terminals can have voltage present even when not in use.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry and result in damage to the components.

## Determine Mounting Order

Mount drives in order (left to right) according to power rating (highest to lowest) starting with the highest power rating. If power rating is unknown, position drives (highest to lowest) from left to right based on amp rating.

## Zero-stack Tab and Cutout

Engaging the zero-stack tab and cutout from drive-to-drive makes efficient use of panel space for installations with multiple drives.

## IMPORTANT

Engaging the zero-stack tab and cutout from drive-to-drive is required for shared-bus multi-axis drive systems. This is done to make sure that the drive connectors are spaced properly to accept the shared-bus connection system.

Figure 21 - Zero-stack Tab and Cutout Example

<!-- image -->

For the zero-stack feature to engage properly when multiple frame sizes exist in the drive system, the following conditions must be met:

- Frame 3 drives must mount to the left of frame 1 or 2 drives.
- Frame 2 drives must mount to the left of frame 1 drives.

Capacitor modules can mount to the right of any frame size, but are always rightmost in any drive configuration.

## IMPORTANT

Mount drives in descending order, left to right, according to frame size with capacitor modules always mounted on the far right.

<!-- image -->

## Shared-bus Connection System

The shared-bus connection system is used to extend the mains AC input, 24V control input, and the DC bus power from drive-to-drive in shared-bus multi-axis configurations.

## IMPORTANT

When the shared-bus connection system is used, the zero-stack tab and cutout must be engaged between adjacent drives.

The connection system is composed of three components:

- Input wiring connectors that plug into the leftmost drive and receive input wiring for mains AC and 24V DC.
- AC bus, DC bus, and 24V DC T-connectors that plug into the drives downstream from the first where AC, DC, and/or 24V control power is shared. DC bus T-connectors also plug into the first drive where DC bus power is shared.
- Busbars that connect between drives to extend the mains AC bus, DC bus, and 24V DC control power from drive-to-drive.

Figure 23 - Connection System Example

<!-- image -->

The three components assemble from left to right across the drive system.

1. Attach wiring to input wiring connectors.
2. Insert input wiring connectors and T-connectors into the appropriate drive connectors.
3. Insert busbars to connect between wiring connectors and T-connectors.

## Single-axis Configurations

The following restrictions exist for standalone (single-axis) configurations:

- Standalone (single-axis) drives can be mounted to the panel individually or by using the zero-stack tab and cutout (refer to Figure 23 on page 49)
- The shared-bus connection system does not apply and must not be used

For a single-axis example configuration, refer to Standalone Configurations on page 17 .

## Multi-axis Configurations

Each multi-axis configuration has restrictions that apply:

- The shared-bus connection system must be used. Do not attach discrete wires from drive-to-drive.
- The maximum number of drives in Shared AC bus power-sharing groups cannot exceed 5.
- The maximum number of drives in any other bus power-sharing group cannot exceed 8.

For a multi-axis example configuration, refer to Shared AC/DC Hybrid Configuration on page 21 .

## Drill-hole Patterns

Hole patterns for drives that are mounted in zero-stack or shared-bus configuration are provided for mounting your drives to the panel. Drives with the highest power rating are always mounted to the left of any drive with a lower power rating in shared-bus configurations:

- Frame 1 drives can be followed by only another frame 1 drive.
- Frame 2 drives can be followed by frame 1 drives or another frame 2 drive.
- Frame 3 drives can be followed by frame 1, frame 2, or another frame 3 drive.
- Mount Bulletin 2198 capacitor modules in the rightmost position.
- Capacitor modules have the same hole pattern as frame 2 drives.
- Only Shared DC, Shared AC/DC, and Shared AC/DC, hybrid configurations are compatible with Bulletin 2198 capacitor modules.

Table 20 - Hole Pattern Overview

|                                              |         | Drive Cat. No. Frame Size Frame Size Patterns                                                    | Page   |
|----------------------------------------------|---------|--------------------------------------------------------------------------------------------------|--------|
| 2198-H003-ERSx 2198-H008-ERSx                |         | Frame 1 As many as eight frame 1 drives                                                          | 53     |
| 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | Frame 2 | As many as eight frame 2 drives One frame 2 drive followed by as many as seven frame 1 drives 54 |        |
| 2198-H070-ERSx                               | Frame 3 | As many as eight frame 3 drives                                                                  | 55     |
| 2198-H070-ERSx                               | Frame 3 | One frame 3 drive followed by as many as seven frame 1 drives 56                                 |        |
| 2198-H070-ERSx                               | Frame 3 | One frame 3 drive followed by as many as seven frame 2 drives 57                                 |        |

Table 21 - Capacitor Module Support

|                |    | Frame Size StandaloneSingle-phaseOperation                                            | Three-phase Operation                      | Three-phase Operation                      | Three-phase Operation                      | Three-phase Operation                      |
|----------------|----|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| Drive Cat. No. |    |                                            |                                            | Standalone Shared DC Shared AC/DC          | Shared AC/DC Hybrid                        |                                            |
|                |    | Number of Capacitor Modules Connected, Max | Number of Capacitor Modules Connected, Max | Number of Capacitor Modules Connected, Max | Number of Capacitor Modules Connected, Max | Number of Capacitor Modules Connected, Max |
| 2198-H003-ERSx (1)                | 1  | 0                                          | 0                                          | 0                                          | 0                                          | 0                                          |
| 2198-H008-ERSx (1)                | 1  | 0                                          |                                            | 2                                          | 2                                          |                                            |
| 2198-H015-ERSx (1)                |    | 0                                          | 1                                          | 1                                          |                                            |                                            |
| 2198-H025-ERSx |    | —                                          | 2 4 3                                      | 2 4 3                                      |                                            |                                            |
| 2198-H040-ERSx |    | —                                          |                                            |                                            |                                            |                                            |
| 2198-H070-ERSx |    | —                                          | 3 4                                        | 3 4                                        |                                            |                                            |

These hole patterns apply to standalone drives.

Figure 24 - Frame 1, Frame 2, and Frame 3 Standalone Hole Patterns

<!-- image -->

These hole patterns apply when all drives in the system are frame 1 or frame 2. There is 50 mm (1.97 in.) between mounting holes (A-to-A and B-to-B).

Figure 25 - Frame 1 and Frame 2 Hole Patterns

<!-- image -->

This hole pattern applies when transitioning from frame 2 drives to frame 1 drives. To mount additional frame 1 drives to the right of Axis 2 in this figure, refer to the frame 1 hole pattern in Figure 25 .

Figure 26 - Frame 2 to Frame 1 Hole Pattern

<!-- image -->

This hole pattern applies when all drives in the system are frame 3 drives. There is 85.20 mm (3.35 in.) between mounting holes, as shown.

Figure 27 - Frame 3 Hole Pattern

<!-- image -->

This hole pattern applies when transitioning from frame 3 drives to frame 1 drives. To mount additional frame 1 drives to the right of Axis 2 in this figure, refer to the frame 1 hole pattern in Figure 25 .

Figure 28 - Frame 3 to Frame 1 Hole Pattern

<!-- image -->

This hole pattern applies when transitioning from frame 3 drives to frame 2 drives. To mount additional frame 2 drives to the right of Axis 2 in this figure, refer to the frame 2 hole pattern in Figure 25 .

Figure 29 - Frame 3 to Frame 2 Hole Pattern

<!-- image -->

## Mount Your Kinetix 5500 Drive

This procedure assumes you have prepared your panel and understand how to bond your system. For installation instructions regarding other equipment and accessories, refer to the instructions that came with those products.

Follow these steps to mount your Kinetix 5500 drives to the panel.

1. Lay out the hole pattern for each Kinetix 5500 drive in the enclosure.

See Establishing Noise Zones on page 43 for panel layout recommendations.

## IMPORTANT

To improve the bond between the Kinetix 5500 drive and subpanel, construct your subpanel out of zinc-plated (paint-free) steel.

2. Drill holes in the panel for mounting your drive system. Hole patterns, by frame size, are shown in Drill-hole Patterns beginning on page 51 .
3. Loosely attach the mounting hardware to the panel. The recommended mounting hardware is M4 (#8-32) steel bolts. Observe bonding techniques as described in Bonding Modules on page 40 .
4. Attach the leftmost drive to the cabinet panel.
5. Attach additional drives (if any) just to the right of the previous drive by using the same method, but also making sure that the zero-stack tabs and cutouts are engaged. Zero-stack mounting is required based on configuration, refer to the Zero-stack Tab and Cutout Example on page 48 .
6. Tighten all mounting fasteners.

<!-- image -->

Apply 2.0 N·m (17.7 lb·in) maximum torque to each fastener.

<!-- image -->

## Connector Data and Feature Descriptions

This chapter illustrates drive connectors and indicators, including connector pinouts, and provides descriptions for Kinetix® 5500 drive features.

| Topic                                    |   Page |
|------------------------------------------|--------|
| Kinetix 5500 Connector Data              |     60 |
| Understand Control Signal Specifications |     64 |
| Feedback Specifications                  |     67 |
| Safe Torque Off Safety Features          |     68 |

## Kinetix 5500 Connector Data

Use these illustrations to identify the connectors and indicators for the Kinetix 5500 drive modules.

Figure 30 - Kinetix 5500 Drive Features and Indicators

<!-- image -->

5 Ethernet (PORT1) RJ45 connector 12 Link speed status indicators

6 Ethernet (PORT2) RJ45 connector 13 Link/Activity status indicators

| Item Description                                  |
|---------------------------------------------------|
| 1 Motor cable shield clamp                        |
| 2  Converter kit mounting hole  (1) (under cover) |
| 3 Motor feedback (MF) connector                   |
| 4 Digital inputs (IOD) connector                  |
| 7 Zero-stack mounting tab/cutout                  |

| Item Description              |
|-------------------------------|
| 8 Module status indicator     |
| 9 Network status indicator    |
| 10 LCD display                |
| 11 Navigation pushbuttons     |
| 14 Motor power (MP) connector |

| Item Description                                                                   |
|------------------------------------------------------------------------------------|
| 15 Motor brake (BC) connector                                                      |
| 16 Ground terminal                                                                 |
| 17 Shunt resistor (RC) connector                                                   |
| 18 AC mains input power (IPD) connector                                            |
| 19  DC bus (DC) connector (under cover) (2)                                        |
| 20 24V control input power (CP) connector                                          |
| 21  Safe Torque Off (STO) connector  (3) (does not apply to 2198-Hxxx-ERS2 drives) |

- (2) DC bus connector ships with protective knock-out cover that can be removed for use in shared-bus configurations.
- (3) Protective knock-out cover is removed on 2198-Hxxx-ERS (hardwired STO) drives.

Figure 31 - Capacitor Module Features and Indicators

<!-- image -->

| Item Description                              |
|-----------------------------------------------|
| 1 Ground screw (green)                        |
| 2 Module status (MS) connector (relay output) |
| 3 Module status indicator                     |
| 4  DC bus (DC) connector (under cover) (1) (2)                                               |
| 5  24V control input power (CP) connector (2) |

## Module Status Connector Pinout

| MS Pin   | Description   | Signal   |
|----------|---------------|----------|
| 1        | Module status output odue saus oupu 2 MS               | MS       |
|          | Module status output odue saus oupu 2 MS               |          |

## Safe Torque Off Connector Pinout

For the hardwired Safe Torque Off (STO) connector pinouts, feature descriptions, and wiring information, see Chapter 9 beginning on page 157 .

## Input Power Connector Pinouts

Table 22 - Mains Input Power Connector

| IPD Pin   | Description             | Signal   |
|-----------|-------------------------|----------|
|           | Chassis ground          |          |
| L3        | Three-phase input power | L3       |
| L2        | Three-phase input power | L2       |
| L1        | Three-phase input power | L1       |

## Table 23 - 24V Input Power Connector

|   CP Pin | Description                         | Signal   |
|----------|-------------------------------------|----------|
|        1 | 24V power supply, customer supplied | 24V+     |
|        2 | 24V common                          | 24V          |

## DC Bus and Shunt Resistor Connector Pinouts

Table 24 - DC Bus Power Connector

| DC Pin   | Description   | Signal   |
|----------|---------------|----------|
| 1        | DC bus connections  C bus coecos  2 DC+               | DC          |
|          | DC bus connections  C bus coecos  2 DC+               |          |

## Table 25 - Shunt Resistor Connector

| RC Pin   | Description   | Signal   |
|----------|---------------|----------|
| 1        | Shunt connections (frames 2 and 3)  Sucoecos (aes ad 3)  2 SH               | DC+      |
| 1        | Shunt connections (frame 1)  Sucoecos (ae )  2 DC+               | SH       |
|          | Shunt connections (frame 1)  Sucoecos (ae )  2 DC+               |          |

## Digital Inputs Connector Pinouts

The Kinetix 5500 drive has two configurable digital inputs and five configurable functions to choose from in the Logix Designer application. Digital input 1 can be configured as a dualfunction (home/registration) input.

## Table 26 - Digital Inputs Connector

| IOD Pin Description                                                 | Signal   |
|---------------------------------------------------------------------|----------|
| 1 24V current-sinking fast input #1. This is a dual-function input. | IN1 (1)  |
| 2 I/O common for customer-supplied 24V supply.                      | COM      |
| 3 24V current-sinking fast input #2.                                | IN2      |
| 4 I/O cable shield termination point.                               | SHLD     |

## Table 27 - Configurable Functions

| Default Configuration  (1)                                          | Description         |
|---------------------------------------------------------------------|---------------------|
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Unassigned          |
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Home                |
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Registration 1      |
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Registration 2      |
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Positive overtravel |
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Negative overtravel |
| Digital input1= Home/Registration 1 Digital input2 = Registration 2 | Home/Registration 1 |

Figure 32 - Pin Orientation for Digital Inputs (IOD) Connector

<!-- image -->

## Ethernet Communication Connector Pinout

| Pin Description   | Signal   |
|-------------------|----------|
| 1 Transmit+       | TD+      |
| 2 Transmit-       | TD          |
| 3 Receive+        | RD+      |
| 4 Reserved        | —        |
| 5 Reserved        | —        |
| 6 Receive-        | RD          |
| 7 Reserved        | —        |
| 8 Reserved        | —        |

## Motor Power, Brake, and Feedback Connector Pinouts

## Table 28 - Motor Power Connector

|    | MP Pin Description                                 | Signal Color   |         |
|----|----------------------------------------------------|----------------|---------|
| U  | Three-phase motor power Three-phase motor powerV V |                | U Brown |
|    | Three-phase motor power Three-phase motor powerV V |                | Black   |
|    | Three-phase motor power Three-phase motor powerV V | W W            | Blue    |
|    | Chassis ground                                     |                | Green   |

<!-- image -->

ATTENTION: To avoid damage to the Kinetix 5500 drive, make sure that the moSeer power signals are wired correctly. See Figure 50 on page 83 for motor power connector wiring examples.

## IMPORTANT

Drive-to-motor power cables must not exceed 50 m (164 ft), depending on overall system design.

System performance was tested at this cable length. These limitations also apply when meeting CE and UK requirements.

## Table 29 - Motor Brake Connector

| BC Pin Description   | Signal   |
|----------------------|----------|
| 1 Motor brake connections oobae coecos 2 MBRK                      | MBRK+    |
| 1 Motor brake connections oobae coecos 2 MBRK                      |           |

## Motor Feedback Connector Pinout

Figure 33 - Pin Orientation for Motor Feedback (MF) Connector

|        | MF Pin Description                                                                                                                                                                     | Signal   |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 1      | Bidirectional data and power for digital encoder interface  pg 2 D                                                                                                                                                                                        | D+       |
|        | Bidirectional data and power for digital encoder interface  pg 2 D                                                                                                                                                                                        |           |
| SHIELD | Cable shield and grounding plate (internal to 2198-KITCON-DSL connector kit) termination point  Cable shield and shield clamp (internal to 2198-H2DCK converter kit) termination point | SHIELD   |

Pin 1 Pin 2

<!-- image -->

<!-- image -->

## Understand Control Signal Specifications

Table 30 - Understand Digital Input Functions

| Function                                | Description                                                                                                                                                                                      | Default Behavior                                                                   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Home/Reg1                               | An active state indicates to a homing sequence that the referencing sensor has been seen. Typically, a transition of this signal is used to establish a reference position for the machine axis. | The function is always inactive. You can enable in the Logix Designer application. |
|                                         | Registration 1 An inactive-to-active transition (also known as a positive transition) or active-to-inactive transition (also known as a negative transition) is used to                          | The function is always inactive. You can enable in the Logix Designer application. |
|                                         | aceoace ao(ao oaa ega latch position values for use in registration moves. Registration 2                                                                                                                                                                                                  | The function is always inactive. You can enable in the Logix Designer application. |
| Positive overtravel Negative overtravel | The positive/negative limit switch (normally closed contact) inputs for each axis require 24V DC (nominal).                                                                                      | The function is always inactive. You can enable in the Logix Designer application. |

Table 31 - Digital Input Specifications

| Attribute                                                    | Value                                                                          |
|--------------------------------------------------------------|--------------------------------------------------------------------------------|
| Type                                                         | Active high, single-ended, current sinking (EN 61131-2 Type 1)                 |
| Dedicated functions                                          | Registration 1, Home, Registration 2, Positive overtravel, Negative overtravel |
| Input current (with 24V applied)                             | 12 mA, typical                                                                 |
| On-state input voltage                                       | 15…30V @ 15 mA, max                                                            |
| Off-state input voltage                                      | -1.0…5.0V                                                                      |
| Pulse reject filtering (registration functions)              | 12.0 µs                                                                        |
| Pulse reject filtering (home input function) debounce filter | 20 ms, nom                                                                     |
| Propagation delay (registration functions)                   | 0 (delay compensated)                                                          |
| Registration accuracy                                        | ±3 µs                                                                          |
| Registration repeatability                                   | 700 ns                                                                         |
| Windowed registration invalid-to-valid event delay           | 125 µs, min                                                                    |

## Figure 34 - Digital Input Circuitry

<!-- image -->

This section provides a description of the Kinetix 5500 digital inputs, Ethernet communication, power and relay specifications, encoder feedback specifications, and Safe Torque Off features.

## Digital Inputs

Two digital inputs are available for the machine interface on the IOD connector. Digital inputs require a 24V DC @ 15 mA supply. These are sinking inputs that require a sourcing device. A common and cable shield connection is provided on the IOD connector for digital inputs.

The Registration 1 input is capable of dual functionality. You can also use this as the Home input. Configuration for dual functionality is not needed.

## IMPORTANT

To improve registration input EMC performance, refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## Ethernet Communication Specifications

The PORT1 and PORT2 (RJ45) Ethernet connectors are provided for communication with the Logix 5000® controller.

| Attribute                                     | Value                                                                                                                          |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Communication                                 | The drive auto-negotiates speed and duplex modes. These modes can be forced through the Logix Designer application. 100BASE-TX, full duplex is recommended for maximum performance.                                                                                                                                |
| Cyclic update period                          | 1.0 ms, min                                                                                                                    |
| Embedded switch features                      | Three-port, cut-through, time correction on IEEE-1588 packets, limited filtering, quality of service with four priority levels |
| Auto MDI/MDIX crossover detection/ correction | Yes                                                                                                                            |
| Port-to-port time synchronization variation   | 100 ns, max                                                                                                                    |
| Cabling                                       | CAT5e shielded, 100 m (328 ft) max                                                                                             |

## Motor Brake Circuit

The brake option is a spring-set holding brake that releases when voltage is applied to the brake coil in the motor. The customer-supplied 24V power supply drives the brake output through a solid-state relay. The solid-state brake driver circuit provides the following:

- Brake current-overload protection
- Brake overvoltage protection

Two connections (BC-1 and BC-2) are required for the motor brake output. Connections are rated for 2.0 A @ +24V (refer to Figure 35).

Figure 35 - Motor Brake Circuit

<!-- image -->

## IMPORTANT

Motor parking-brake switching frequency must not exceed 10 cycles/min.

Control of the solid-state relay to release the motor brake is configurable in the Logix Designer application (refer to Configure SPM Motor Closed-loop Control Axis Properties on page 127). An active signal releases the motor brake. Turn-on and turn-off delays are specified by the MechanicalBrakeEngageDelay and MechanicalBrakeReleaseDelay settings.

## IMPORTANT

Holding brakes that are available on Allen-Bradley® rotary motors are designed to hold a motor shaft at 0 rpm for up to the rated brakeholding torque, not to stop the rotation of the motor shaft, or be used as a safety device.

You must command the servo drive to 0 rpm and engage the brake only after verifying that the motor shaft is at 0 rpm.

These steps provide one method that you can use to control a brake.

1. Wire the mechanical brake according to the appropriate interconnect diagram in Appendix 2 beginning on page 179 .
2. Enter the MechanicalBrakeEngageDelay and MechanicalBrakeReleaseDelay times in the Logix Designer application.

See Axis Properties &gt; Parameter List. The delay times must be from the appropriate motor family brake specifications table in the Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001 .

3. Use the drive stop-action default setting (Current Decel &amp; Disable).

See Axis Properties &gt; Actions &gt; Stop Action in the Logix Designer application.

4. To decelerate the servo motor to 0 rpm, use the motion instruction Motion Axis Stop (MAS).
5. To engage the brake and disable the drive, use the motion instruction Motion Servo Off (MSF).

## Control Power

The Kinetix 5500 drive requires 24V DC input power for control circuitry.

## IMPORTANT

SELV and PELV rated power supplies must be used to energize external safety devices that are connected to the Kinetix 5500 safety inputs.

The National Electrical Code and local electrical codes take precedence over the values and methods provided. Implementation of these codes is the responsibility of the machine builder.

Table 32 - Control Power Input Power Specifications

| Attribute                                                    | Frame 1       |              | Frame 2 Frame 3   |
|--------------------------------------------------------------|---------------|--------------|-------------------|
| Input voltage                                                | 21.6…26.4V DC |              |                   |
| Control power AC input current Nom @ 24V DC  (1) Inrush, max | 400 mA 2.0 A  | 800 mA 3.0 A | 1.3 A 3.0 A       |

## Feedback Specifications

Table 34 - Absolute Position Retention Limits

| Encoder Type                             | Cat. No.   |                                                             | Motor Cat. No. Actuator Cat. No.                                                     | Retention Limits           | Retention Limits   |
|------------------------------------------|------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------|--------------------|
| Encoder Type                             | Designator |                                                             |                                                                                      | Turns (rotary) mm (linear) |                    |
| Hiperface (DSL)                          | -P         | VPL-A/Bxxxxx-P VPF-A/Bxxxxx-P VPS-Bxxxxx-P                  | VPAR-A/Bxxxxx-P                                                                      | 4096 (±2048) —             |                    |
|                                          | -W         | VPL-A/Bxxxxx-W, VPF-A/Bxxxxx-W VPH-A/Bxxxxx-W               | VPAR-Bxxxxx-W                                                                        | 4096 (±2048) —             |                    |
|                                          | -Q         | VPL-A/Bxxxxx-Q VPF-A/Bxxxxx-Q VPH-A/Bxxxxx-Q                | VPAR-Bxxxxx-Q                                                                        | 512 (±256) —               |                    |
| Hiperface                                | -M         | MPL-A/Bxxxxx-M MPM-A/Bxxxxx-M MPF-A/Bxxxxx-M MPS-A/Bxxxxx-M | MPAR-A/B3xxxx-M MPAI-A/BxxxxxM                                                       | 2048 (±1024) —             |                    |
|                                          | -V         | MPL-A/Bxxxxx-V                                              | MPAS-A/Bxxxx1-V05, MPAS-A/Bxxxx2-V20 MPAR-A/B1xxxx-V, MPAR-A/B2xxxx-V MPAI-A/BxxxxxV | 4096 (±2048) —             |                    |
| Stegmann Hiperface (magnetic scale) -xDx |            |                                                             | — LDAT-Sxxxxxx-xDx                                                                   | — 960 (37 . 8)             |                    |

Figure 36 - Absolute Position Limits (measured in turns)

4096 Turns

<!-- image -->

The Kinetix 5500 drive accepts motor feedback signals from Stegmann Hiperface digitalservo-link (DSL) encoders on the motor feedback (MF) connector.

<!-- image -->

Auto configuration in the Logix Designer application of intelligent absolute, highresolution encoders is possible with only Allen-Bradley motors.

The Kinetix 5500 drives support Kinetix VP motors with Stegmann Hiperface digital-servo-link (DSL) encoders by using the 2-pin (MF) feedback connector. You can also use the MF connector for feedback-only applications.

Other Allen-Bradley motors and actuators with Stegmann Hiperface single-turn or multi-turn high-resolution absolute encoders are also accepted, but only when using drive firmware revision 2.002 or later, and the 2198-H2DCK Hiperface-to-DSL (series B or later) feedback converter kit.

Table 33 - Stegmann Hiperface DSL Specifications

| Attribute                                  | Value                                    |
|--------------------------------------------|------------------------------------------|
| Protocol                                   | Hiperface DSL                            |
| Memory support                             | Programmed with Allen-Bradley motor data |
| Hiperface data communication 9.375 Mbits/s |                                          |

## Absolute Position Feature

The absolute position feature of the drive tracks the position of the motor, within the multiturn retention limits, while the drive is powered off. The absolute position feature is available with only multi-turn encoders.

## Safe Torque Off Safety Features

Kinetix 5500 servo drives have Safe Torque Off (STO) capability and can safely turn off the inverter power transistors in response to the removal of the STO digital inputs, resulting in Stop Category 0 behavior.

## Servo Drives with Hardwired Safety

2198-Hxxx-ERS (hardwired) servo drives support parallel input terminals for cascading to adjacent drives over duplex wiring. For applications that do not require the STO safety function, you must install jumper wires to bypass the Safe Torque Off feature.

See Chapter 9 beginning on page 157. for the STO connector pinout, installation, and wiring information.

## Servo Drives with Integrated Safety

For 2198-Hxxx-ERS2 (integrated safety) servo drives, the GuardLogix® 5570 or Compact GuardLogix 5570 safety controller issues the STO command via the EtherNet/IP™ network and the 2198-Hxxx-ERS2 servo drives execute the command.

See Chapter 10 beginning on page 165. for integrated safety drive specifications, configuring motion and safety connections, motion direct commands, and the STO bypass feature.

<!-- image -->

## Connect the Kinetix 5500 Drive System

This chapter provides procedures for wiring your Kinetix® 5500 system components and making cable connections.

| Topic                                                   |   Page |
|---------------------------------------------------------|--------|
| Basic Wiring Requirements                               |     70 |
| Determine the Input Power Configuration                 |     71 |
| Ground Screw Settings                                   |     74 |
| Remove the Ground Screws in Select Power Configurations |     75 |
| Ground the Drive System                                 |     76 |
| Wiring Requirements                                     |     78 |
| Wiring Guidelines                                       |     79 |
| Wire the Power Connectors                               |     80 |
| Wire the Digital Input Connectors                       |     82 |
| Wire Kinetix VP Motors and Actuators                    |     82 |
| Wire Other Motors and Actuators                         |     88 |
| Capacitor Module Connections                            |     98 |
| External Passive-shunt Resistor Connections             |     99 |
| Ethernet Cable Connections                              |    100 |

## Basic Wiring Requirements

This section contains basic wiring information for the Kinetix 5500 drives.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can perform all cutting, drilling, tapping, and welding with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry and result in damage to components.

<!-- image -->

IMPORTANT

SHOCK HAZARD: To avoid a hazard of electrical shock, perform all mounting and wiring of the Bulletin 2198 drive modules before applying power. Once power is applied, connector terminals can have voltage present even when not in use.

This section contains common PWM servo system wiring configurations, size, and practices that can be used in most applications. National Electrical Code, local electrical codes, special operating temperatures, duty cycles, or system configurations take precedence over the values and methods provided.

## Routing the Power and Signal Cables

When you route power and signal wiring on a machine or system, radiated noise from nearby relays, transformers, and other electronic devices can be induced into I/O communication, or other sensitive low voltage signals. This can cause system faults and communication anomalies.

The Kinetix 2090 single motor cable contains the power, brake, and feedback wires, but is properly shielded to protect the noise-sensitive feedback signals.

See Electrical Noise Reduction on page 40 for examples of routing high and low voltage cables in wireways. Refer to the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, for more information.

## Determine the Input Power Configuration

Before wiring input power See your Kinetix 5500 system, you must determine the type of input power within your facility. The drive is designed to operate in both grounded and ungrounded environments.

<!-- image -->

ATTENTION: Ungrounded, corner-grounded, and impedance-grounded input power configurations are permitted, but you must remove the ground screws. See Ground Screw Settings on page 74 for a ground screw summary.

## Grounded Power Configurations

The grounded (wye) power configuration lets you ground your three-phase power at a neutral point. This type of grounded power configuration is preferred.

Figure 37 - Grounded Power Configuration (wye Secondary)

<!-- image -->

- (1) When using a 2198-DBxx-F line filter, the AC ground jumper is installed and the DC ground jumper is installed. When using a 2198-DBRxx-F line filter, the AC ground jumper is installed and the DC ground jumper is installed.

The Kinetix 5500 drive has factory-installed ground screws for grounded (wye) power distribution.

See Power Wiring Examples beginning on page 179 for input power interconnect diagrams.

Figure 38 - Impedance-grounded Power Configuration (wye Secondary)

<!-- image -->

- (1) The AC ground jumper is removed and the DC ground jumper is removed. See Figure 42 on page 75 for access to ground screws.
- (1) The AC ground jumper is removed and the DC ground jumper is removed. See Figure 42 on page 75 for access to ground screws.

Figure 39 - Corner-grounded Power Configuration (Delta Secondary)

<!-- image -->

See Power Wiring Examples beginning on page 179 for input power interconnect diagrams.

Figure 40 - Grounded Power Configuration (Single-phase Input)

<!-- image -->

- (1) When using a 2198-DBxx-F line filter, the AC ground jumper is installed and the DC ground jumper is installed. When using a 2198-DBRxx-F line filter, the AC ground jumper is installed and the DC ground jumper is installed.

## IMPORTANT

To reduce leakage current in single-phase AC input operation, remove the AC ground screw (refer to Figure 42 on page 75). Install the AC ground screw only if higher EMC performance is required.

See Power Wiring Examples beginning on page 179 for input power interconnect diagrams.

## Ungrounded Power Configurations

The ungrounded power configuration (Figure 41), corner-grounded (Figure 39), and impedance-grounded (Figure 38) power configurations do not provide a neutral ground point.

## IMPORTANT

If you determine that you have ungrounded, corner-grounded, or impedance-grounded power distribution in your facility, you must remove the ground screws in each of your drives that receive input power.

See Remove the Ground Screws in Select Power Configurations on page 75 for more information.

## Ground Screw Settings

Figure 41 - Ungrounded Power Configuration

<!-- image -->

- (1) The AC ground jumper is removed and the DC ground jumper is removed. See Figure 42 on page 75 for access to ground screws.

<!-- image -->

ATTENTION: Ungrounded systems do not reference each phase potential to a power distribution ground. This can result in an unknown potential to earth ground.

See Power Wiring Examples beginning on page 179 for input power interconnect diagrams.

Determine the ground screw setting for your Kinetix 5500 servo drives.

Table 35 - Ground Screw Settings

|                                                            |                                                                | Ground Configuration Example Diagram Ground Screw Setting   |
|------------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------|
| Grounded (wye)                                             | Figure 37 on page 71                                           | Both screws installed (default setting)                     |
| • AC fed ungrounded • Corner grounded • Impedance grounded | Figure 41 on page 74 Figure 39 on page 72 Figure 38 on page 72 | Both screws removed                                         |
| Single-phase input power                                   | Figure 40 on page 73                                           | AC screw removed (1)                                        |

<!-- image -->

ATTENTION: To help prevent damage to the servo drive, you must set the ground screws according to the example diagrams that are summarized in Table 35 .

## Remove the Ground Screws in Select Power Configurations

Removing the ground screws involves gaining access, opening the sliding door, and removing the screws.

## IMPORTANT

If you have grounded-wye power distribution, you do not need to remove the ground screws. Go to Ground the Drive System on page 76 .

Removing the ground screws in multi-axis configurations is best done when each drive is removed from the panel and placed on its side on a solid surface.

<!-- image -->

ATTENTION: Because the unit no longer maintains line-to-neutral voltage protection, the risk of equipment damage exists when you remove the ground screws.

<!-- image -->

ATTENTION: To avoid personal injury, the ground screws access door must be kept closed when power is applied. If power was present and then removed, wait at least 5 minutes for the DC-bus voltage to dissipate and verify that no DC-bus voltage exists before accessing the ground screws.

Figure 42 - Remove the Ground Screws

<!-- image -->

<!-- image -->

- Remove only the AC screw for single-phase operation

ATTENTION: Risk of equipment damage exists. The drive ground configuration must be accurately determined. Leave the ground screws installed for grounded power configurations (default). Remove the screws for ungrounded, corner-grounded, and impedance-grounded power configurations.

## Ground the Drive System

All equipment and components of a machine or process system must have a common earth ground point that is connected to the chassis. A grounded system provides a ground path for protection against electrical shock. Grounding your drives and panels minimize the shock hazard to personnel and damage to equipment caused by short circuits, transient overvoltages, and accidental connection of energized conductors to the equipment chassis.

<!-- image -->

ATTENTION: The National Electrical Code contains grounding requirements, conventions, and definitions. Follow all applicable local codes and regulations to ground your system safely. For CE and UK grounding requirements, refer to Agency Compliance on page 30 .

## Ground the System Subpanel

Ground Kinetix 5500 drives and 2198-CAPMOD-1300 capacitor modules to a bonded cabinet
22 ground-bus with a braided ground strap of at least 10 mm 2 (0.0155 in 2 ) in cross-sectional area. Keep the braided ground strap as short as possible for optimum bonding.

Figure 43 - Connecting the Ground Terminal

<!-- image -->

Make braided ground straps with at least 10 mm

2

(0.0155 in

2

)

cross-sectional area.

Keep straps as short as possible.

| Item Description                                 |
|--------------------------------------------------|
| 1 Ground screw (green) 2.0 N•m (17.7 lb•in), max |
| 2 Braided ground strap (customer supplied)       |
| 3 Ground grid or power distribution ground       |
| 4 Bonded cabinet ground bus (customer supplied)  |

See the System Design for Control of Electrical Noise Reference Manual, publication GMCRM001, for more information.

Kinetix 5500

Servo Drives

(shared-bus)

## Ground Multiple Subpanels

In this figure, the chassis ground is extended to multiple subpanels.

Figure 44 - Subpanels Connected to a Single Ground Point

<!-- image -->

High-frequency (HF) bonding is not illustrated. For HF bonding information, see Bonding Multiple Subpanels on page 42 .

## Wiring Requirements

Table 36 - Power and I/O Wiring Requirements

| Kinetix 5500 Drive Cat. No.                                                | Description                                         | Connects to Terminals         | Connects to Terminals   | Wire Size 2                                                                 | Strip Length   | Torque Value N•m (lb•in)   |
|----------------------------------------------------------------------------|-----------------------------------------------------|-------------------------------|-------------------------|-----------------------------------------------------------------------------|----------------|----------------------------|
|                                                                            |                                                     |                               | Pin Signal              | mm  (AWG)                                                                   | mm (in.)       |                            |
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | Mains input power  (1) (single-axis IPD connector)  | L3 L2 L1                      | L3 L2 L1                | 1.5…4 (16…12)                                                               | 8.0 (0.31)     | 0.5…0.6 (4.4…5.3)          |
| 2198-H070-ERSx                                                             | Mains input power  (1) (single-axis IPD connector)  | L3 L2 L1                      | L3 L2 L1                | 1.5…6 (16…10)                                                               | 10.0 (0.39)    | 0.5…0.6 (4.4…5.3)          |
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | Motor power                                         | U V W                         | U V W                   | Motor power cable depends on motor/ drive combination. 0.75…2.5 (2) (18…14) | 7.0 (0.28)     | 0.5…0.6 (4.4…5.3)          |
| 2198-H070-ERSx                                                             | Motor power                                         | U V W                         | U V W                   | 2.5…6 (2) (14…10)                                                           | 10.0 (0.39)    | 0.5…0.8 (4.4…7.1)          |
| 2198-xxxx-ERSx                                                             | PELV/SELV 24V power  (1) (single-axis CP connector) | CP-1 CP-2                     | 24V+ 24V                         | 0.5…2.5 (20…14)                                                             | 7.0 (0.28)     | 0.22…0.25 (1.9…2.2)        |
| 2198-xxxx-ERSx                                                             | Brake power                                         | BC-1 BC-2                     | MBRK+ MBRK-             | —  (3)                                                                      | 7.0 (0.28)     | 0.22…0.25 (1.9…2.2)        |
| 2198-xxxx-ERSx                                                             | DC Bus power                                        | DC-1 DC-2                     | DC DC+                         | —  (4)                                                                      | —  (4)         | —  (4)                     |
| 2198-xxxx-ERSx                                                             | Shunt resistor (frame 2 and 3)                      | RC-1 RC-2                     | DC+ SH                  | 0.5…4.0 (20…12)                                                             | 8.0 (0.31)     | 0.5…0.6                    |
| 2198-xxxx-ERSx                                                             | (20…12) 8.0 (0.31) (4.4…5.3) Shunt resistor RC-1SH (frame 1)                                                     | RC-1 RC-2                     | SH DC+                  | 0.2…1.5                                                                     | 8.0 (0.31)     | 0.5…0.6                    |
| 2198-xxxx-ERSx                                                             | Safety  (5)                                         | ST0-1 ST0-2 ST0-3 ST0-4 ST0-5 | SB+ SB S1 SC S2                         | (24…16)                                                                     | 10.0 (0.39)    | —  (6)                     |
| 2198-xxxx-ERSx                                                             | Digital inputs                                      | IOD-1 IOD-2 IOD-3 IOD-4       | IN1 (7) COM IN2 SHLD    | 0.2…1.5 (24…16)                                                             | 10.0 (0.39)    | —  (6)                     |

<!-- image -->

ATTENTION: To avoid personal injury and/or equipment damage, observe the following:

- Make sure that the installation complies with specifications regarding wire types, conductor sizes, branch circuit protection, and disconnect devices. The National Electrical Code (NEC) and local codes outline provisions for safely installing electrical equipment.
- Use motor power connectors for connection purposes only. Do not use them to turn the unit on and off.
- Ground shielded power cables to help prevent potentially high voltages on the shield.

Wires must be copper with 75 °C (167 °F) minimum rating. Phasing of main AC power is arbitrary and earth ground connection is required for safe and proper operation.

See Power Wiring Examples on page 179 for interconnect diagrams.

IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

## Wiring Guidelines

Use these guidelines as a reference when wiring the power connectors on your Kinetix 5500 drive.

## IMPORTANT

## IMPORTANT

For connector locations of the Kinetix 5500 drives, refer to Kinetix 5500 Connector Data on page 60 .

When removing insulation from wires and tightening screws to secure the wires, refer to Table 36 on page 78 for strip lengths and torque values.

To improve system performance, run wires and cables in the wireways as established in Establishing Noise Zones on page 43 .

Follow these steps when wiring the connectors for your Kinetix 5500 drive.

1. Prepare the wires for attachment to each connector plug by removing insulation equal to the recommended strip length.

## IMPORTANT

Use caution not to nick, cut, or otherwise damage strands as you remove the insulation.

2. Route the cable/wires to your Kinetix 5500 drive.
3. Insert wires into connector plugs. .

See connector pinout tables in Chapter 4 or the interconnect diagrams in Appendix A

4. Tighten the connector screws.
5. Gently pull on each wire to make sure it does not come out of its terminal; reinsert and tighten any loose wires.
6. Insert the connector plug into the drive connector.

## Wire the Power Connectors

This section provides examples and guidelines to assist you in making connections to the input power connectors.

See Power Wiring Examples on page 179 for an interconnect diagram.

## Wire the 24V Control Power Input Connector

The 24V power (CP) connector requires 24V DC input for the control circuitry. The single-axis connector plug is included with the drive, shared-bus connector kits are purchased separately.

<!-- image -->

Table 37 - Single-axis CP Connector Wiring Specifications

| Drive Module Cat. No.           | CP Pin Signal        | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|---------------------------------|----------------------|-------------------------------------|-------------------------|----------------------------|
| 2198-Hxxx-ERSx 2198-CAPMOD-1300 | CP-1 24V+  CP-2 24V- | 0.5…2.5 (20…14)                     | 7.0 (0.28)              | 0.22…0.25 (1.9…2.2)        |

Figure 46 - CP Connector Wiring - Shared Bus

<!-- image -->

Table 38 - Shared-bus CP Connector Wiring Specifications

| Drive Cat. No.                  | CP Pin Signal        | Input Current, Max A rms   | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|---------------------------------|----------------------|----------------------------|-------------------------------------|-------------------------|----------------------------|
| 2198-Hxxx-ERSx 2198-CAPMOD-1300 | CP-1 24V+  CP-2 24V- |                            |                                     | 40 10 (6) 11.0 (0.43)   | 1.7…1.8 (15.0…15.9)        |

## Wire the Input Power Connector

The input power (IPD) connector requires 195…528V AC (single-phase or three-phase) for mains input power. The single-axis connector plug is included with the drive, shared-bus connector kits are purchased separately.

<!-- image -->

ATTENTION: Make sure that the input power connections are correct when wiring the IPD connector plug or input wiring connector and that the plug/ connector is fully engaged in the drive connector. Incorrect wiring/polarity or loose wiring can damage equipment or cause an explosion.

Figure 47 - IPD Connector Wiring - Single Axis

<!-- image -->

| Kinetix 5500 Drive Cat. No.                                                |          | Pin Signal   | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|----------------------------------------------------------------------------|----------|--------------|-------------------------------------|-------------------------|----------------------------|
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | L3 L2 L1 | L3 L2 L1     | 1.5…4 (16…12)                       | 8.0 (0.31)              | 0.5…0.6 (4.4…5.3)          |
| 2198-H070-ERSx                                                             | L3 L2 L1 | L3 L2 L1     | 1.5…6 (16…10)                       | 10.0 (0.39)             | 0.5…0.6 (4.4…5.3)          |

Table 39 - Single-axis IPD Connector Wiring Specifications

<!-- image -->

Table 40 - Shared Bus IPD Connector Wiring Specifications

| Kinetix 5500 Drive Cat. No.                                                |          | Pin Signal   | Input Current, Max A rms   | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|----------------------------------------------------------------------------|----------|--------------|----------------------------|-------------------------------------|-------------------------|----------------------------|
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | L3 L2 L1 | L3 L2 L1     | 52                         | 13.3…3.3 (6…12)                     | 11.0 (0.43)             | 1.7…1.8 (15.0…15.9)        |
| 2198-H070-ERSx                                                             |          |              |                            | 13.3 (6)                            |                         |                            |

## Wire the Digital Input Connectors

## Wire Kinetix VP Motors and Actuators

This section provides guidelines to assist you in making digital input connections.

## Wire the Safe Torque Off Connector

For the hardwired Safe Torque Off (STO) connector pinouts, feature descriptions, and wiring information, see Chapter 9 beginning on page 157 .

## Wire the Digital Inputs Connector

The digital inputs (IOD) connector uses spring tension to hold wires in place.

Figure 49 - IOD Connector Wiring

<!-- image -->

Table 41 - Digital Inputs (IOD) Connector Specifications

| Drive Cat. No. DC Pin Signal   |                         |                      | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|--------------------------------|-------------------------|----------------------|-------------------------------------|-------------------------|----------------------------|
| 2198-Hxxx-ERSx                 | IOD-1 IOD-2 IOD-3 IOD-4 | IN1 (1) COM IN2 SHLD | 0.2…1.5 (24…16)                     | 10.0 (0.39)             | —  (2)                     |

- (1) This signal has dual-functionality. You can use IN1 (IOD-1) as registration or Home input.

(2) This connector uses spring tension to hold wires in place.

Kinetix 5500 drives and Kinetix VP motor/actuator combinations use single motor-cable technology with motor power, feedback, and brake wires (when specified) housed in a single cable. Feedback wires are shielded separately and provide a shield braid for grounding in the connector kit.

## IMPORTANT

Due to the unique characteristics of single cable technology, which is designed for and tested with Kinetix 5500 drives and Kinetix VP motors, you cannot build your own cables or use third-party cables.

See the Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNXTD004, for cable specifications.

Table 42 - Single Cable Catalog Numbers

| Motor Cat. No.                                 | Feedback Kit Cat. No.          | Motor Cable Cat. No. (with brake wires)                                            | Motor Cable Cat. No. (without brake wires)   | Feedback Connections                                                                                                                             |
|------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| VPL-A/Bxxxx VPF-A/Bxxxx VPH-A/Bxxxx VPS-Bxxxxx | 2198-KITCON-DSL (included with | 2090-CSBM1DF-xxAAxx (standard) cables 2090-CSBM1DF-xxAFxx (continuous-flex) cables | 2090-CSWM1DF-xxAAxx (standard) cables        | Flying lead feedback conductors. Cables are designed specifically for Kinetix 5500 drives.                                                       |
| VPAR-A/Bxxxx                                   | each servo drive)              | 2090-CSBM1DG-xxxAxx (standard) cables 2090-CSBM1DG-xxxFxx (continuous-flex) cables | 2090-CSWM1DG-xxxAxx (standard) cables        | Flying lead feedback conductors. Leads are longer to accommodate Kinetix 5700 drives. Extra service loops are required with Kinetix 5500 drives. |

## Maximum Cable Lengths

Combined motor cable length for all axes on the same DC bus must not exceed 250 m (820 ft). The maximum drive-to-motor cable length for Kinetix 5500 drives and motor/actuator combinations with 2090-CSxM1Dx cables is 50 m (164 ft) for most drives with standard (nonflex) cables. For additional cable length details, see Agency Compliance on page 30 .

## Motor Power Connections

See Kinetix 5500 Servo Drive and Rotary Motor Wiring Examples on page 185 for an interconnect diagram.

Figure 50 - MP Connector Wiring

<!-- image -->

<!-- image -->

WARNING: Make sure that the motor power connections are correct when wiring the MP connector plug and that the plug is fully engaged in the module connector. Incorrect wiring/polarity or loose wiring can cause an explosion or damage equipment.

Table 43 - Motor Power (MP) Connector Specifications

| Drive Cat. No.                                                             | Pin   | Signal/Wire Color                   | Recommended Wire Size (1) mm 2  (AWG)                                       | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|----------------------------------------------------------------------------|-------|-------------------------------------|-----------------------------------------------------------------------------|-------------------------|----------------------------|
| 2198-H003-ERSx 2198-H008-ERSx 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | U V W | Brown Black Blue Green/Yellow U V W | Motor power cable depends on motor/ drive combination. 0.75…2.5 (18…14) max | 8.0 (0.31)              | 0.5…0.6 (4.4…5.3)          |
| 2198-H070-ERSx                                                             |       |                                     | 2.5…6 (14…10) max                                                           | 10.0 (0.39)             | 0.5…0.8 (4.4…7.1)          |

## Motor Brake Connections

Figure 51 - BC Connector Wiring

<!-- image -->

Table 44 - Motor Brake (BC) Connector Specifications

| Drive Cat. No. Pin   | Signal/ Wire Color   | Recommended Wire Size(1) (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|----------------------|----------------------|----------------------------------|-------------------------|----------------------------|
| 2198-Hxxx-ERSx       | BC-1 MBRK+/Black  — 7.0 (0.28)  (1.9…2.2) BC-2 MBRK-/White                      | —                                | 7.0 (0.28)              | 0.22…0.25                  |

(1) Motor brake wires are part of the 2090-CSBM1DF/DG motor cable.

## Motor Feedback Connections

Single motor-cable feedback connections are made by using the 2198-KITCON-DSL feedback connector kit (included with each servo drive).

- 2090-CSxM1DF cables have flying lead conductors that are designed specifically for Kinetix 5500 servo drives.
- 2090-CSxM1DG cables also have flying lead feedback conductors. Leads are longer than 2090-CSxM1DF cables to accommodate Kinetix 5700 servo drives. However, because the leads are longer, extra service loops are required with Kinetix 5500 drives.

## IMPORTANT

When using the 2198-KITCON-DSL feedback connector kit, the ambient
°° g 
temperature for the Kinetix 5500 drive enclosure is 0…50 °C (32…122 °F).

Figure 52 - MF Connector Wiring Example

<!-- image -->

## IMPORTANT

Cable preparation and positioning that provides a high-frequency bond between the shield braid and grounding plate is required to optimize system performance.

Table 45 - Motor Feedback (MF) Connector Specifications

| Drive Cat. No. Pin   | Signal/ Wire Color               | Wire Size AWG   | Strip Length mm (in.)    | Cover Screw Torque Value N•m (lb•in)   |
|----------------------|----------------------------------|-----------------|--------------------------|----------------------------------------|
| 2198-Hxxx-ERSx       | MF-1 D+/Blue  MF-2 D-/White/Blue |                 | 22 10.0 (0.39) 0.4 (3.5) |                                        |
| 2198-Hxxx-ERSx       |                                  |                 | 22 10.0 (0.39) 0.4 (3.5) |                                        |

## IMPORTANT

The feedback bundle in 2090-CSxM1DF-18Axxx motor cables (typically used with frame 1 drives) route around the shield clamp (as shown in Figure 52). The feedback bundle in2090-CSxM1DG-18, 2090-CSxM1xx-14, and 2090-CSBM1xx-10 motor cables (typically used with frame 2 and 3 drives) route with the power and brake wires inside the cable shield.

## Apply the Single Motor-cable Shield Clamp

Factory-supplied Kinetix 2090 single motor cables are shielded, and the braided cable shield must terminate at the drive during installation. A small portion of the cable jacket has been removed to expose the shield braid. The exposed area must be clamped (with the clamp provided) at the bottom front of the drive.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, make sure that shielded power cables are grounded according to recommendations.

<!-- image -->

Cables for Kinetix VP motors (catalog numbers 2090-CBxM1DF-18Axxx) do not route the feedback bundle under the shield clamp. The 2090-CSxM1DG-18, 2090-CSxM1xx-14, and 2090-CSBM1xx-10 motor cables have the feedback bundle within the cable shield braid.

This procedure assumes you have completed wiring your motor power, brake, and feedback connectors and are ready to apply the cable shield clamp.

Follow these steps to apply the motor cable shield clamp.

1. Loosen the left-side (retention) clamp screw and remove the right-side screw.

## 18 AWG Cable Installation

<!-- image -->

When the drive/motor combination calls for 18 AWG cable, the feedback cable routes around the motor cable shield clamp.

## 14 AWG and 10 AWG Cable Installation Example

<!-- image -->

When the drive/motor combination calls for 14 AWG or 10 AWG cable, the feedback cable routes along with the power and brake wiring.

2. Position the exposed portion of the cable shield directly in line with the clamp.

## IMPORTANT

Loosen the retention screw, if needed, until you can start threading both clamp screws with the cable shield under the clamp.

3. Tighten each screw a few turns at a time until the maximum torque value of 2.0 N·m (17.7 lb·in) is achieved.
4. Repeat step 1 through step 3 for each drive in multi-axis configurations.

## Wire Other Motors and Actuators

Kinetix 5500 drives are also compatible with many other motors and actuators, however the 2198-H2DCK Hiperface-to-DSL feedback converter kit is required for converting the 15-pin Hiperface feedback signals to 2-pin DSL feedback signals.

Follow these guidelines when 2090-CPxM7DF (power/brake) cables and 2090-CFBM7DF (feedback) cables are used in a new installation or reused in an existing installation with Kinetix 5500 servo drives. Kinetix MP servo motors and actuators have separate connectors for 2090-CPxM7DF power/brake cables and 2090-CFBM7DF feedback cables.

## IMPORTANT

To configure these additional motors and actuators (see Table 47 , Current Motor Power Cable Compatibility on page 89) with your Kinetix 5500 servo drive, you must have drive firmware 2.002 or later. See Table 46 to determine if you must install the Kinetix 5500 Add-on Profile.

Table 46 - Add-on Profile (AOP) Installation Requirement

|                | Drive Firmware Revision Logix Designer Application Version Kinetix 5500 AOP Needed?   |
|----------------|---------------------------------------------------------------------------------------|
| 2.002 or later | 21.00 Yes 21.03 or later (1) No                                                       |
| 2.002 or later |                                                                                       |

## Install the Kinetix 5500 Add-On Profile

Add-On profiles are available for download at the Custom Downloads Add-On Profiles website: https://download.rockwellautomation.com/esd/download.aspx?downloadid=addonprofiles

Follow these steps to download the Kinetix 5500 AOP.

1. Log in to the Custom Download Add-On Profiles website.

The Custom Download Files dialog box opens.

<!-- image -->

2. Check the box for the AOP for 2198-Hxxx CIP Motion Kinetix5500.
3. Click Download Now and accept the user license agreement. If you are prompted to install the Download Manager, allow the installation.
4. Click the Add-On Profile icon and follow the download instructions.
5. Extract the AOP zip file and run Setup.

To access AOP downloads by using the Product Compatibility Download Center (PCDC), see Install the Kinetix 5500 Add-On Profile on page 108 .

## Motor Power and Brake Connections

The motors and actuators in Table 47 have separate power/brake and feedback cables. The motor power/brake cable attaches to the cable clamp on the drive and the power/brake conductors attach to the MP and BC connectors, respectively.

Table 47 - Current Motor Power Cable Compatibility

| Motor/Actuator Cat. No. (1)                                                                                                                        | Motor Power Cat. No. (2) (with brake wires)                             | Motor Power Cat. No. (2) (without brake wires)                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| MPL-A/B15xxx - xx7xAA, MPL-A/B2xxx-xx7xAA, MPL-A/B3xxx - xx7xAA, MPL-A/B4xxx-xx7xAA, MPL-A/B45xxx - xx7xAA, MPL-A/B5xxx-xx7xAA, MPL-B6xxx - xx7xAA | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| MPM-A/Bxxxx, MPF-A/Bxxxx, MPS-A/Bxxxx                                                                                                              | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| MPAS-A/Bxxxx1-V05SxA, MPAS-A/Bxxxx2-V20SxA, MPAI-A/Bxxxx, MPAR-A/B3xxx, MPAR-A/B1xxx, and MPAR-A/B2xxx (series B)                                  | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |
| LDAT-Sxxxxxx-xDx                                                                                                                                   | —                                                                       | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF-xxAFxx (continuous-flex) |

See Motor Power Connections on page 83 and Motor Brake Connections on page 84 for the MP and BC connector specifications.

Table 48 - Legacy Motor Power Cables

| Motor Cable     | Description  Motor Power Cat. No.                                                  |
|-----------------|------------------------------------------------------------------------------------|
| Standard        | Power/brake, threaded 2090-XXNPMF-xxSxx Power-only, bayonet 2090-XXNPMP-xxSxx      |
| Continuous-flex | Power/brake, threaded 2090-CPBM4DF-xxAFxx Power-only, threaded 2090-CPWM4DF-xxAFxx |
| Continuous-flex | Power-only, bayonet 2090-XXTPMP-xxSxx                                              |
| Continuous-flex |                                                                                    |

Table 49 - Induction Motor Power Cable Specifications

| Cable Manufacturer Cable Series   |              |      | Voltage Rating Temperature Rating   |
|-----------------------------------|--------------|------|-------------------------------------|
| Belden                            | 29500…29507  | 600V | 90 °C (194 °F)                      |
| Lapp Group                        | ÖLFEX VFD XL | 600V | 90 °C (194 °F)                      |
| SAB                               | VFD XLPE TR  | 600V | 90 °C (194 °F)                      |

## Motor Power/Brake Cable Series Change

Motor power and brake conductors on 2090-CPBM7DF (series A) cables have the following dimensions from the factory. If your cable is reused from an existing application, the actual conductor lengths could be slightly different.

Figure 53 - 2090-CPBM7DF (series A) Power/brake Cable Dimensions

<!-- image -->

To reuse your existing (series A) Kinetix 2090 cables with Kinetix 5500 drives, some preparation is necessary so that the cable shield, conductor, and strip lengths are correct. Follow these cable preparation guidelines:

- Trim the shield flush so that no strands can short to adjacent terminals.
- Measure the conductor lengths and include a service loop.
- Remove just enough insulation to provide the proper strip length.

Motor power and brake conductors on 2090-CPBM7DF (series B) 12 AWG and 10 AWG standard (non-flex) cables provide drive-end shield braid and conductor preparation that is modified for compatibility with multiple Kinetix servo drive families, including Kinetix 5500 drives.

Figure 54 - 2090-CPBM7DF (series B, 10 AWG or 12 AWG) Power/brake Cable Dimensions

<!-- image -->

## Maximum Cable Lengths

Combined motor cable length for all axes on the same DC bus must not exceed 250 m (820 ft). The maximum drive-to-motor cable length for Kinetix 5500 drives and motor/actuator combinations with 2090-CxxM7DF cables is 20 m (65.6 ft); however, you can replace the existing motor power/brake cable with a 2090-CSBM1DF or 2090-CSBM1DG single motor cable to extend the length up to 50 m (164 ft).

## IMPORTANT

The option to replace 2090-CPBM7DF power/brake cables with 2090-CSBM1DF/DG single cables applies to only 18 AWG and 14 AWG single cables. 2090-CSBM1Dx-10xxxx (10 AWG/M40 connector) single cables are not compatible with 2090-CPBM7DF-10Axxx (10 AWG/M40 connector) power/brake cables.

When replacing your existing motor power/brake cable with a 2090-CSBM1DF/DG single motor cable, only the motor power and brake conductors are used. Cut off the feedback conductors in the single motor cable and reuse the existing Kinetix 2090 feedback cable.

## Motor Power/Brake Cable Preparation

2090-CPBM7DF (series B) cables are available with 12 AWG and 10 AWG motor-power conductor sizes. So, 14 AWG cables that are used on frame 3 drives, which are physically taller, require preparation.

Cable Preparation for Frame 1 and Frame 2 Drives

For frame 1 and frame 2 drives, the 2090-CPBM7DF (16 AWG and 14 AWG) power conductor length, 102 mm (4.0 in.), is sufficiently long to reach the MP connector plug and provide adequate stress relief.

The brake conductor length, 635 mm (25 in.), is much longer than necessary. We recommend that you measure 163 mm (6.4 in.) from the edge of the cable jacket (that is covered by heat shrink) and trim off the rest.

See Figure 56 and on page 94 for a typical installation example. For strip lengths and torque values, refer to Table 43 on page 83 .

Cable Preparation for Frame 3 Drives

2090-CPBM7DF (series B) 12 AWG and 10 AWG cables are designed for use with Kinetix 5500 drives and do not require any modifications.

For frame 3 drives, 2090-CPBM7DF (14 AWG) cables, and 12 AWG and 10 AWG (series A) cables, the overall length of the cable preparation area must be increased for the motor power conductors to reach the MP connector and also provide a proper service loop.

Follow these steps to prepare your existing 14 AWG cables, and 12 AWG and 10 AWG (series A) cables.

1. Remove a total of 325 mm (12.8 in.) of cable jacket from your existing cable. This exposes additional cable shield.
2. Remove all but 63.5 mm (2.5 in.) of the shield.
3. Cover 12.5 mm (0.5 in.) of the shield ends and an equal length of the conductors with 25 mm (1.0 in.) of electrical tape or heat shrink.
4. Do the same on the other side of the cable shield. This keeps the shield ends from fraying and holds the conductors together.
4. Cut the brake conductors back to 163 mm (6.4 in.) and trim the shield braid at the base of the jacket.
6. The shield braid covering the brake conductors is not needed.
5. Remove the specified length of insulation from the end of each wire.

This example applies to existing 2090-CPBM7DF (14 AWG) cables, and 12 AWG and 10 AWG (series A) cables. If you are using a 2090-CSBM1DF/DG single motor cable, you can remove the shield braid covering the brake conductors.

Figure 55 - Power/brake Cable (14 AWG, 12 AWG, and 10 AWG)

<!-- image -->

- (1) The overall shield braid covering the brake conductors can be removed.

See Figure 56 and on page 94 for a typical installation example. For strip lengths and torque values, refer to Table 43 on page 83 .

## Apply the Motor Power/brake Shield Clamp

The power/brake cable shield attaches to the drive cable clamp. A clamp spacer is included with the 2198-H2DCK feedback converter kit for cable diameters that are too small for a tight fit within the drive clamp alone.

<!-- image -->

SHOCK HAZARD: To avoid a hazard of electrical shock, make sure that shielded power cables are grounded according to recommendations.

Follow these steps to apply the motor power/brake shield clamp.

1. To provide stress relief to the motor power and brake conductors, route the conductors with service loops.
2. Make sure that the cable clamp tightens around the cable shield and provides a good bond between the cable shield and the drive chassis.

## IMPORTANT

Loosen the retention screw, if needed, until you can start threading both clamp screws with the cable shield under the clamp.

3. Tighten each screw, a few turns at a time, until the maximum torque value of 2.0 N·m (17.7 lb·in) is achieved.

## IMPORTANT

If the power/brake cable shield has a loose fit inside the shield clamp, insert the clamp spacer between the shield clamp and the drive to reduce the clamp diameter. When the clamp screws are tight, 2.0 N·m (17.7 lb·in), the result must be a high-frequency bond between the cable shield and the drive chassis.

See Figure 56 on page 94 for a cable-clamp attachment illustration.

Figure 56 - Cable Clamp Attachment

<!-- image -->

- (1) The clamp spacer is included with the Hiperface-to-DSL feedback converter kit, catalog number 2198-H2DCK.

## Motor Feedback Connections

The feedback cable attaches to the 2198-H2DCK converter kit and is wired to the 10-pin connector. Kinetix 2090 feedback cables require preparation to make sure that the shield clamp attaches properly and conductors route smoothly to the 10-pin connector terminals.

## IMPORTANT

When using the 2198-H2DCK feedback connector kit and Kinetix 2090 feedback cables that are listed in Table 50 or Table 51, the ambient temperature for the Kinetix 5500 drive enclosure is derated to
°° p
0…40 °C (32…104 °F).

All current and legacy feedback cables that are listed below are compatible with the 2198H2DCK (series B or later) converter kit.

## IMPORTANT

Only Allen-Bradley motors and actuators with single-turn or multi-turn high-resolution absolute encoders are compatible.

Table 50 - Motor Feedback Cable Compatibility

| Motor/Actuator Family                              | Motor/Actuator (1) Cat. No.                                                                             | Feedback Cable Cat. No.                                                                                                                                 |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix MPL low-inertia motors                     | MPL-A/B15xxx-V/Ex7xAA MPL-A/B2xxx-V/Ex7xAA                                                              | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MPL low-inertia motors                     | MPL-A/B3xxx-S/Mx7xAA MPL-A/B4xxx-S/Mx7xAA MPL-A/B45xxx-S/Mx7xAA MPL-A/B5xxx-S/Mx7xAA MPL-B6xxx-S/Mx7xAA | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MPM medium-inertia motors MPM-A/Bxxxx-S/M  |                                                                                                         | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MPF food-grade motors MPF-A/Bxxxx-S/M      |                                                                                                         | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MP stainless-steel motors MPS-A/Bxxxxx-S/M |                                                                                                         | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MPAS integrated linear stages              | MPAS-A/Bxxxx1-V05SxA MPAS-A/Bxxxx2-V20SxA                                                               | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MPAR electric cylinders                    | MPAR-A/B1xxxx-V and MPAR-A/B2xxxx-V (series B) MPAR-A/B3xxxx-M                                          | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix MPAI heavy-duty electric cylinders         | MPAI-A/BxxxxxM3                                                                                         | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |
| Kinetix LDAT linear thrusters LDAT-Sxxxxxx-xDx     |                                                                                                         | 2090-CFBM7DF-CEAAxx 2090-CFBM7DD-CEAAxx 2090-CFBM7DF-CERAxx (standard) or 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx 2090-CFBM7DF-CDAFxx (continuous-flex) |

Table 51 - Legacy Motor Feedback Cables

| Motor Cable     | Description                                    | Feedback Cable Cat. No.          |
|-----------------|------------------------------------------------|----------------------------------|
| Standard        | Encoder feedback, threaded                     | 2090-XXNFMF-Sxx 2090-UXNFBMF-Sxx |
| Standard        | Encoder feedback, bayonet                      | 2090-UXNFBMP-Sxx                 |
| Standard        | Encoder feedback, bayonet                      | 2090-XXNFMP-Sxx                  |
| Continuous-flex | Encoder feedback, bayonet 2090-XXTFMP-Sxx      |                                  |
| Continuous-flex | Encoder feedback, threaded 2090-CFBM4DF-CDAFxx |                                  |

Figure 57 - 2198-H2DCK Converter Kit Pinout

<!-- image -->

| Terminal Signal Wire Color   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|------------------------------|-------------------------|----------------------------|
| 1 SIN+ Black                 | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 2 SIN– White/Black           | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 3 COS+ Red                   | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 4 COS– White/Red             | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 5 DATA+ Green                | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 6  ECOM (1) White/Gray       | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 7  EPWR_9V (2) Orange        | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 10 DATA– White/Green         | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 11 TS White/Orange           | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |
| 14  EPWR_5V (2)  Gray        | 5.0 (0.2)               | 0.22…0.25 (1.9…2.2)        |

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect either the 5V or the 9V supply, but not both.

## Motor Feedback Cable Preparation

Follow these steps to prepare feedback cables.

1. Remove 115 mm (4.5 in.) of cable jacket and 103 mm (4.0 in.) of cable shield.

## IMPORTANT

This length of wire is required to provide a service loop for the longest wires terminated at the 10-pin connector. However, most wires must be trimmed shorter, depending on the terminal they are assigned to.

2. Determine the length for each of the 10 wires and trim as necessary.
3. Remove 5.0 mm (0.2 in.) of insulation from the end of each wire.

<!-- image -->

Apply the Converter Kit Shield Clamp

Follow these steps to apply the converter kit shield clamp.

1. Apply the shield clamp to the 12 mm (0.5 in.) of exposed cable shield to achieve a highfrequency bond between the shield braid and clamp.

## IMPORTANT

Cable preparation and positioning that provides a highfrequency bond between the shield braid and clamp is required to optimize system performance.

Also, make sure that the cable is positioned where the cover clamps onto the jacket for added stress relief.

Apply 0.30 N·m (2.6 lb·in) torque to each screw.

<!-- image -->

2. Route and insert each wire to its assigned terminal.

Include a service loop, as shown in Figure 58, and refer to the connector pinout in Figure 57 .

3. Tighten each terminal screw.

Apply 0.22…0.25 N·m (1.9…2.2 lb·in) torque to each screw.

4. Gently pull on each wire to make sure it does not come out of its terminal; reinsert and tighten any loose wires.
5. Attach the tie wrap for added stress relief.

Table 53 - 2090-CFBM7DF-CEAxxx Feedback Cables

| Rotary Motors    | MPL-B15xxx…MPL-B2xxx-V/Ex4/7xAA MPL-B3xxx…MPL-B6xxx-M/Sx7xAA MPL-A5xxx-M/Sx7xAA MPM-A165xxx…MPM-A215xxx   | MPL-A15xxx…MPL-A2xxx-V/Ex4/7xAA MPL-A3xxx-M/Sx7xAA MPL-A4xxx-M/Sx7xAA MPL-A45xxx-M/Sx7xAA MPM-A115xxx…MPM-A130xxx-M/S MPF/MPS-A3xx-M/S MPF/MPS-A4xx-M/S MPF/MPS-A45xx-M/S MPS-A5xxx-M/S   | 2198-H2DCK Converter Kit Pin   |
|------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
|                  | MPM-Bxxxxx-M/S MPF-Bxxx-M/S MPF-A5xxx-M/S MPS-Bxxx-M/S                                                    |                                                                                                                                                                                           | 2198-H2DCK Converter Kit Pin   |
| Linear Actuators | MPAS-Bxxxxx-VxxSxA MPAR-Bxxxx, MPAI-Bxxxx LDAT-Sxxxxxx-xDx                                                | MPAS-Axxxxx-VxxSxA MPAR-Axxxx, MPAI-Axxxx                                                                                                                                                 |                                |
| 1                |                                                                                                           | Sin+ Sin+ 1                                                                                                                                                                               |                                |
| 2                |                                                                                                           | Sin- Sin- 2                                                                                                                                                                               |                                |
| 3                | Cos+                                                                                                      | Cos+                                                                                                                                                                                      | 3                              |
| 4                | Cos-                                                                                                      | Cos-                                                                                                                                                                                      | 4                              |
| 5                | Data+                                                                                                     | Data+                                                                                                                                                                                     | 5                              |
| 6                | Data-                                                                                                     | Data-                                                                                                                                                                                     | 10                             |
|                  | 9 Reserved                                                                                                | EPWR _ 5V                                                                                                                                                                                 | 14                             |
| 10               | ECOM                                                                                                      | ECOM                                                                                                                                                                                      | 6 (1)                          |
| 11               | EPWR_9V                                                                                                   | Reserved                                                                                                                                                                                  | 7                              |
| 12               | ECOM                                                                                                      | ECOM                                                                                                                                                                                      | 6                              |
| 13               | TS                                                                                                        | TS                                                                                                                                                                                        | 11                             |

(1) The ECOM and TS- connections are tied together and connect to the cable shield.

A mounting bracket is included with the 2198-H2DCK converter kit to secure the kit to the drive. Install the mounting bracket in the mounting position specific to the frame size of your drive.

Figure 58 - Wire the 2198-H2DCK Feedback Converter Kit

<!-- image -->

## Capacitor Module Connections

Follow these guidelines when wiring the 2198-CAPMOD-1300 capacitor module:

- Wire output (MS) connections to the Logix 5000® controller (optional).
- See Kinetix 5500 Capacitor Module wiring example on page 181 .
- See Kinetix 5500 Capacitor Module Status Indicators on page 147 for troubleshooting the module status indicator and relay output.
- See the installation instructions provided with your Bulletin 2198 capacitor module, publication 2198-IN004 .

## IMPORTANT

To improve system performance, run wires and cables in the wireways as established in Chapter 2 starting on page 31. Connections to the DCbus must be made with the shared-bus connection system.

Figure 59 - MS Connector Wiring

<!-- image -->

Table 54 - Capacitor Module Connector Specifications

| Connector Description      |           | Pin Signal   | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|----------------------------|-----------|--------------|-------------------------------------|-------------------------|----------------------------|
| Module Status              | MS-1 MS-2 | MS MS        | 0.14…1.5 (28…16)                    | 7.0 (0.28)              | 0.22…0.25 (1.9…2.2)        |
| PELV/SELV 24V power (plug) | CP-1 CP-2 | 24V+ 24V              | 0.5…2.5 (20…14)                     | 7.0 (0.28)              | 0.22…0.25 (1.9…2.2)        |
| DC-bus power Busbar        |           | DC DC+              | —  (1)                              | —  (1)                  | —  (1)                     |

## External Passive-shunt Resistor Connections

Follow these guidelines when wiring your 2097-Rx shunt resistor:

- See External Passive Shunt Resistor on page 45 for noise zone considerations.
- See Shunt Resistor Wiring Example on page 184 .
- See the installation instructions provided with your Bulletin 2097 shunt resistor, publication 2097-IN002 .

## IMPORTANT

To improve system performance, run wires and cables in the wireways as established in Chapter 2 .

Figure 60 - RC Connector Wiring

<!-- image -->

Table 55 - Shunt Resistor (RC) Connector Specifications

| Drive Cat. No. Pin                                          |           | Signal   | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------------------------------------------------|-----------|----------|-------------------------------------|-------------------------|----------------------------|
| 2198-H003-ERSx 2198-H008-ERSx                               | RC-1 RC-2 | SH DC+   | 0.5…4.0 (20…12)                     | 8.0 (0.31)              | 0.5…0.6 (4.4…5.3)          |
| 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx 2198-H070-ERSx | RC-1 RC-2 | DC+ SH   | 0.5…4.0 (20…12)                     | 8.0 (0.31)              | 0.5…0.6 (4.4…5.3)          |

## IMPORTANT

You must disconnect the internal shunt wires at the RC connector before connecting the Bulletin 2097 shunt resistor wires.

## Ethernet Cable Connections

This procedure assumes you have your Logix 5000 controller and Kinetix 5500 drive modules mounted and are ready to connect the network cables.

The EtherNet/IP™ network is connected by using the PORT 1 and PORT 2 connectors. See Figure 30 on page 60 to locate the Ethernet connectors on your Kinetix 5500 drive. See Figure 61 to locate the connectors on your Logix 5000 controller.

Shielded Ethernet cable is required and available in several standard lengths. Ethernet cable lengths connecting drive-to-drive, drive-to-controller, or drive-to-switch must not exceed 100 m (328 ft). See the Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNX-TD004, for more information.

Figure 61 - ControlLogix and CompactLogix Ethernet Port Locations

<!-- image -->

These Logix 5000 controllers accept linear, ring (DLR), and star network configurations. See Typical Communication Configurations on page 23 for linear, ring, and star configuration examples.

## IMPORTANT

When using an external Ethernet switch for routing traffic between the controller and the drive, switches with IEEE-1588 time synchronization capabilities (boundary or transparent clock) must be used to make sure that switch delays are compensated.

<!-- image -->

## Configure and Start the Kinetix 5500 Drive System

This chapter provides procedures for configuring your Kinetix® 5500 drive system with a Logix 5000® controller.

| Topic                                                       |   Page |
|-------------------------------------------------------------|--------|
| Understand the Kinetix 5500 Display                         |    102 |
| Configure the Drive                                         |    107 |
| Studio 5000 Logix Designer                                  |    107 |
| Configure the Logix 5000 Controller                         |    109 |
| Configure Feedback-only Axis Properties                     |    121 |
| Configure Induction-motor Frequency-control Axis Properties |    122 |
| Configure SPM Motor Closed-loop Control Axis Properties     |    127 |
| Download the Program                                        |    131 |
| Apply Power to the Kinetix 5500 Drive                       |    132 |
| Understand Bus-sharing Group Configuration                  |    133 |
| Test and Tune the Axes                                      |    136 |

<!-- image -->

Before you begin, make sure you know the catalog number for each drive component, the Logix module and /or controller, and the servo motor used in your motion control application.

## Understand the Kinetix 5500 Display

Each soft menu item is executed by pressing the navigation button directly below the item, as shown in this example.

<!-- image -->

The Kinetix 5500 drive has two status indicators and an LCD status display. The indicators and display are used to monitor the system status, set network parameters, and troubleshoot faults. Four navigation buttons are directly below the display and are used to select items from a soft menu.

Figure 62 - Kinetix 5500 Drive LCD Display and Status Indicators

<!-- image -->

This is the Home screen. The setup selections are tied to the two Setup (left-side) buttons and the menu selections are tied to the two Menu (right-side) buttons.

The soft menu provides a changing selection that corresponds to the current screen. Use the navigation buttons to perform the following.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

|    | Press to go back. Pressing enough times results in the Home  screen.                                                                                                                                         |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | Pressing either arrow moves the selection to the next (or previous) item. When changing values, pressing the up arrow increments the highlighted value. Values roll over after reaching the end of the list. |
|    | Press to select values to change, moving from right to left. Values roll over when reaching the end of the list.                                                                                             |
|    | Press to select a menu item.                                                                                                                                                                                 |
|    | Press to return to the Home screen.                                                                                                                                                                          |
| ?  | Press to display the fault help (possible solutions in troubleshooting tables).  (1)                                                                                                                         |

## Menu Screens

The menu screens provide information about the drives, motors, diagnostics, and the fault log. Parameters cannot be updated in the menu screens. Press one of the menu buttons to access the menu.

You can use the soft menu items and navigation buttons to view the information.

<!-- image -->

| Menu/Sub Menu Selections       |                               | Attributes Description Example Values                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                            |                                                                                                                  |
|--------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Drive Info                     | Catalog number 2198-Hxxx-ERSx | Catalog number 2198-Hxxx-ERSx                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                            |                                                                                                                  |
| Drive Info                     | Firmware revision             | Firmware revision                                                                                                                                                                                                                                                                                          | FW REV: 1.1.450167                                                                                                                                                                                                                                                                                         | FW REV: 1.1.450167                                                                                               |
| Drive Info                     | Hardware revision             | Hardware revision                                                                                                                                                                                                                                                                                          | HW REV: 1.1                                                                                                                                                                                                                                                                                                | HW REV: 1.1                                                                                                      |
| Drive Info                     | Serial number                 | Serial number                                                                                                                                                                                                                                                                                              | SERIAL#: xxxxxxxxxxx                                                                                                                                                                                                                                                                                       | SERIAL#: xxxxxxxxxxx                                                                                             |
| Drive Info                     | Model number                  | Model number                                                                                                                                                                                                                                                                                               | MODEL: VPL-B1306F                                                                                                                                                                                                                                                                                          | MODEL: VPL-B1306F                                                                                                |
| Drive Info                     | Serial number                 | Serial number                                                                                                                                                                                                                                                                                              | SERIAL#: xxxxxxxxxxx                                                                                                                                                                                                                                                                                       | SERIAL#: xxxxxxxxxxx                                                                                             |
| Drive Info                     | Bus diagnostics               | Bus diagnostics                                                                                                                                                                                                                                                                                            | BUS VOLT: 0.0V BUS CUR: 0.0A                                                                                                                                                                                                                                                                               | BUS VOLT: 0.0V BUS CUR: 0.0A                                                                                     |
| Drive Info                     | Converter diagnostics         | Converter diagnostics                                                                                                                                                                                                                                                                                      | CONV UTIL: 0.7%                                                                                                                                                                                                                                                                                            | CONV UTIL: 0.7%                                                                                                  |
| Drive Info                     |                               |                                                                                                                                                                                                                                                                                                            | CONV TEMP: 31.7C                                                                                                                                                                                                                                                                                           | CONV TEMP: 31.7C                                                                                                 |
| Drive Info                     | Inverter diagnostics          | Inverter diagnostics                                                                                                                                                                                                                                                                                       | INV UTIL: 0.0%                                                                                                                                                                                                                                                                                             | INV UTIL: 0.0%                                                                                                   |
| Diagnostics> Motor Diagnostics | Motor speed                   | Motor speed                                                                                                                                                                                                                                                                                                | SPEED:0.0 RPM                                                                                                                                                                                                                                                                                              | SPEED:0.0 RPM                                                                                                    |
|                                | Motor current                 | Motor current                                                                                                                                                                                                                                                                                              | MTR CUR:0.0A RMS                                                                                                                                                                                                                                                                                           | MTR CUR:0.0A RMS                                                                                                 |
|                                | Motor utilization             | Motor utilization                                                                                                                                                                                                                                                                                          | MTR UTIL:0.0%                                                                                                                                                                                                                                                                                              | MTR UTIL:0.0%                                                                                                    |
|                                | Motor temperature             | Motor temperature                                                                                                                                                                                                                                                                                          | MTR TEMP:0.00C                                                                                                                                                                                                                                                                                             | MTR TEMP:0.00C                                                                                                   |
|                                | Serial number                 | Serial number                                                                                                                                                                                                                                                                                              | SERIAL#xxxxxxxxxxx                                                                                                                                                                                                                                                                                         | SERIAL#xxxxxxxxxxx                                                                                               |
|                                | Resolution                    | Resolution                                                                                                                                                                                                                                                                                                 | RESOLUTION: 262144                                                                                                                                                                                                                                                                                         | RESOLUTION: 262144                                                                                               |
|                                | Number of turns               | Number of turns                                                                                                                                                                                                                                                                                            | NO OF TURNS: 1                                                                                                                                                                                                                                                                                             | NO OF TURNS: 1                                                                                                   |
|                                | Encoder temperature           | Encoder temperature                                                                                                                                                                                                                                                                                        | ENC TEMP:33.7C                                                                                                                                                                                                                                                                                             | ENC TEMP:33.7C                                                                                                   |
|                                | Supply voltage                | Supply voltage                                                                                                                                                                                                                                                                                             | SUPP VOLT:11.3V                                                                                                                                                                                                                                                                                            | SUPP VOLT:11.3V                                                                                                  |
|                                | Link quality                  | Link quality                                                                                                                                                                                                                                                                                               | LINK QUAL: 100.0%                                                                                                                                                                                                                                                                                          | LINK QUAL: 100.0%                                                                                                |
|                                | Remote signal                 | The link quality attribute indicates how noisy a communication link is and also indicates if there is a communication link that is already established at the drive end. The LINK QUAL value must always be 100%. If the value is persistently below 100%, it indicates a poor feedback ground connection. | The link quality attribute indicates how noisy a communication link is and also indicates if there is a communication link that is already established at the drive end. The LINK QUAL value must always be 100%. If the value is persistently below 100%, it indicates a poor feedback ground connection. |                                                                                                                  |
|                                | strength indicator            | Similar to Link Quality, RSSI reports the quality of link as seen at the motor end by the encoder. Maintain the RSSI value in the range of 80…100%. If the value is persistently below 80%, it indicates a poor feedback ground connection.                                                                | Similar to Link Quality, RSSI reports the quality of link as seen at the motor end by the encoder. Maintain the RSSI value in the range of 80…100%. If the value is persistently below 80%, it indicates a poor feedback ground connection.                                                                | RSSI: 100.0%                                                                                                     |
|                                | Accumulated position errors   | This is an aggregated number of errors in the primary position feedback channel of DSL feedback. POS ERRORS: 1                                                                                                                                                                                             | This is an aggregated number of errors in the primary position feedback channel of DSL feedback. POS ERRORS: 1                                                                                                                                                                                             |                                                                                                                  |
|                                | Channel position errors       | This is an aggregated number of errors on a secondary communication channel of the DSL feedback. CHNL ERRORS: 5                                                                                                                                                                                            | This is an aggregated number of errors on a secondary communication channel of the DSL feedback. CHNL ERRORS: 5                                                                                                                                                                                            |                                                                                                                  |
| Fault Log                      | Fault text                    | Fault code as listed in the Kinetix 5500 Fault Codes.xlsx file.(1)                                                                                                                                                                                                                                         | FLT S20 - CONV OVERLOAD FL                                                                                                                                                                                                                                                                                 | FLT S20 - CONV OVERLOAD FL                                                                                       |
| Fault Log                      | Fault details                 | The problem as reported in the Kinetix 5500 Fault Codes.xlsx file.(1)                                                                                                                                                                                                                                      | The converter thermal model indicates that the temperature has exceeded the factory set capacity rating of 110%.                                                                                                                                                                                           | The converter thermal model indicates that the temperature has exceeded the factory set capacity rating of 110%. |
| Fault Log                      | Fault help                    | The possible solution as reported in the Kinetix 5500 Fault Codes.xlsx file.(1)                                                                                                                                                                                                                            | • Reduce the number of drives in the same bus group • Reduce duty-cycle of commanded motion                                                                                                                                                                                                                | • Reduce the number of drives in the same bus group • Reduce duty-cycle of commanded motion                      |

## Setup Screens

The setup screens provide the means of changing drive settings, for example, the IP address. Press one of the setup buttons to access the setup screens.

You can use the soft menu items and navigation buttons to view the information and make changes.

Press to validate your changes:

- If the change is invalid, the value doesn't change.
- If the change is valid, an asterisk appears next to the changed attribute.

## IMPORTANT

<!-- image -->

<!-- image -->

You must cycle control power to make network configuration changes persistent. In this example, the IP address was changed. The change takes effect and the asterisk disappears after control power is cycled.

Display configuration changes take effect immediately.

Table 56 - Navigating the Settings Menu

| Settings Menu Selections Sub Menu Selections Attributes Default Description   |                               |                                                                    |              |                                                                                                                 |
|-------------------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| Protected Mode                                                                | Reset                         | ENABLED DISABLED                                                   | ENABLED      | When Enabled (default), identity object or safety resets are not possible when a controller connection is open. |
| Protected Mode                                                                | Network Config                | ENABLED DISABLED                                                   | ENABLED      | When Enabled (default), network configuration changes are not possible when a controller connection is open.    |
| Protected Mode                                                                | Flash Update                  | ENABLED DISABLED                                                   | ENABLED      | When Enabled (default), firmware updates are not possible when a controller connection is open.                 |
| Protected Mode                                                                | Device Config                 | ENABLED DISABLED                                                   | ENABLED      | When Enabled (default), only attribute writes are possible when a controller connection is open.                |
| Network                                                                       | ->Static IP (1)               | IP address                                                         |              | 192.168.1.1 Indicates current IP address                                                                        |
| Network                                                                       | ->Static IP (1)               | Subnet mask                                                        |              | 255.255.255.000 Indicates current subnet mask                                                                   |
| Network                                                                       | ->Static IP (1)               | Gateway                                                            |              | 192.168.001.001 Indicates current gateway                                                                       |
| Network                                                                       | DHCP                          | On                                                                 | On           | Turns on DHCP                                                                                                   |
| Network                                                                       | DHCP                          | Off                                                                | Off          | Turns off DHCP                                                                                                  |
| Display                                                                       | Backlight Timeout             | 30 sec…NEVER (NEVER=no timeout period, the backlight is always on) | -> 3 min (1) | Sets backlight timeout period of the display                                                                    |
| Display                                                                       | Cyclic Data Select  (2)       | ->DC BUS (1)                                                       | ->DC BUS (1) | DC bus voltage                                                                                                  |
| Display                                                                       | Cyclic Data Select  (2)       | CONV UTIL                                                          | CONV UTIL    | Converter utilization in percent                                                                                |
| Display                                                                       | Cyclic Data Select  (2)       | CONV TEMP                                                          | CONV TEMP    | Converter temperature in °C                                                                                     |
| Display                                                                       | Cyclic Data Select  (2)       | SHUNT UTIL                                                         | SHUNT UTIL   | Shunt utilization in percent                                                                                    |
| Display                                                                       | Cyclic Data Select  (2)       | INV UTIL                                                           | INV UTIL     | Inverter utilization in percent                                                                                 |
| Display                                                                       | Cyclic Data Select  (2)       | INV TEMP                                                           | INV TEMP     | Inverter temperature in °C                                                                                      |
| Display                                                                       | Cyclic Data Select  (2)       | MOTOR UTIL                                                         | MOTOR UTIL   | Motor utilization in percent                                                                                    |
| Display                                                                       | Cyclic Data Select  (2)       | SPEED                                                              | SPEED        | RPM                                                                                                             |
| Display                                                                       | Cyclic Data Select  (2)       | OUT PWR                                                            | OUT PWR      | Output power in watts                                                                                           |
| Display                                                                       | Cyclic Data Select  (2)       | OUT FREQ                                                           | OUT FREQ     | Output frequency in hertz                                                                                       |
| Display                                                                       | Cyclic Data Select  (2)       | OUT CUR                                                            | OUT CUR      | Output current in amps                                                                                          |
| Display                                                                       | Contrast                      | -10…+10                                                            | 0            | Contrast setting of the display                                                                                 |
| Safety  (3)                                                                   | Reset Ownership Are you sure? |                                                                    |              | Resets safety ownership (reset fails after 30 seconds)                                                          |
| Web                                                                           | Enabled                       | Enabled                                                            | Enabled      | Enables the web server                                                                                          |
| Web                                                                           | ->Disabled                    | ->Disabled                                                         | ->Disabled   | Disables the web server                                                                                         |

## Startup Sequence

On initial powerup, the drive performs a self test. Upon successful completion, the drive firmware revision is displayed.

<!-- image -->

Next, the axis state, the IP address, and the default cyclic data attribute (in this example DC bus voltage) appears. In addition, the setup and menu soft keys are displayed. This is the Home screen.

<!-- image -->

In this example PRECHARGE is the axis state attribute. Table 57 lists the other axis states and their descriptions.

Table 57 - Axis States on the Home Screen

| Axis State Description                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STANDBY The drive is waiting to receive configuration information from the controller.                                                                                                             |
| CONNECTING The drive is trying to establish communication with the EtherNet/IP™ controller.                                                                                                        |
| CONFIGURING The drive is receiving configuration information from the controller.                                                                                                                  |
| SYNCING The drive is waiting for a successful Group Sync service.                                                                                                                                  |
| STOPPED The drive is fully configured, but the control loops are not enabled.                                                                                                                      |
| PRECHARGE The drive is ready for mains input power.                                                                                                                                                |
| STARTING  The drive is enabled and checking various conditions before entering the RUNNING or TESTING state. For example, the drive checks the Brake Release delay time during the STARTING state. |
| RUNNING • The drive is enabled, configured with an active control mode, and actively tracking a command. • The drive is configured for No Control and is fully operational.                        |
| TESTING The drive is actively executing a test procedure, for example, a hookup test.                                                                                                              |
| STOPPING The drive is decelerating to a stop as the result of a disable.                                                                                                                           |
| ABORTING The drive is decelerating to a stop as the result of a fault or an abort request.                                                                                                         |
| MAJOR FAULTED The drive is faulted due to an existing or past fault condition.                                                                                                                     |
| START INHIBITED The drive has an active condition that inhibits it from being enabled.                                                                                                             |
| SHUTDOWN The drive has been shut down.                                                                                                                                                             |

## Configure the Drive

## Studio 5000 Logix Designer

You can include the drive in your Studio 5000 Logix Designer® application by adding it to a configured EtherNet/IP module or controller under the I/O configuration tree. After setting network parameters, you can view the drive status information in Studio 5000® environment and use it in your Logix Designer application.

## Set the Network Parameters

You must program network parameters by using the LCD display.

1. From the LCD display, select SETUP&gt;NETWORK and choose between STATIC IP and DHCP.

The default setting is STATIC IP.

2. If STATIC IP, then press to configure the following parameters:
- IP address
- Gateway
- Subnet mask

Settings are stored in nonvolatile memory. IP addressing can also be changed through the Module Configuration dialog box in RSLinx® software. Changes to the IP addressing take effect after power is cycled. The drive is factory programmed to static IP address of 192.168.1.1.

See Setup Screens on page 104 for help with setting the network parameters.

For help with using the Studio 5000 Logix Designer application as it applies to configuring the ControlLogix® or CompactLogix™ controllers, refer to Additional Resources on page 12 .

## Version History

Each release of the Studio 5000 Logix Designer application makes possible the configuration of additional Allen-Bradley® motors, actuators, and drive features not available in previous versions.

| IMPORTANT   | To configure these additional drive features with your Kinetix 5500 servo drive, you must have drive firmware 4.001 or later. See Table 58 to determine if you must install the Kinetix 5500/5700 Add-on Profile.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 58 - AOP Installation Requirement

|                    | Drive Firmware Revision Logix Designer Application Version Kinetix 5500/5700 AOP Needed?   |     |
|--------------------|--------------------------------------------------------------------------------------------|-----|
| 4.001              | 26.00 or 27.00                                                                             | Yes |
| 4.001              | 28.00 or later                                                                             | No  |
| 5.001              | 26.00, 27.00, or 28.00                                                                     | Yes |
| 5.001              | 29.00 or later                                                                             | No  |
| 7.001 or later (1) | 29.00 or later                                                                             | No  |

## Install the Kinetix 5500 Add-On Profile

Download Add-On profiles (AOP) from the Product Compatibility Download Center (PCDC) website: rok.auto/pcdc .

Follow these steps to download the Kinetix 5500 Add-On profile.

1. Go to the Product Compatibility Download Center. The Compatibility &amp; Downloads webpage appears.
2. Click Download.
3. Enter Kinetix 5500 in the Search PCDC window.
4. Click the appropriate firmware revision and follow prompts to download.
5. Extract the AOP zip file and run Setup.

<!-- image -->

## Configure the Logix 5000 Controller

These procedures assume that you have wired your Kinetix 5500 drive system. In this example, the GuardLogix® 5580 safety controller, and CompactLogix 5380 controller dialog boxes are shown.

Follow these steps to configure the controller.

1. Apply power to your controller and open your Logix Designer application.
2. From the Create menu, choose New Project.

<!-- image -->

The New Project dialog box appears.

<!-- image -->

<!-- image -->

IMPORTANT

If you are configuring a 2198-Hxxx-ERS2 (integrated) servo drive in a safety application, you must use a GuardLogix safety controller.

In this example, the typical dialog boxes for ControlLogix and GuardLogix 5380 controllers and CompactLogix 5380 controllers with embedded Ethernet are shown.

Follow these steps to configure your Logix 5000 controller.

1. Expand the Logix 5000 controller family and select your controller.
2. Type the file Name.
3. Click Next.

The New Project dialog box appears.

<!-- image -->

<!-- image -->

4. From the Revision dropdown menu, choose your software revision.
5. Click Finish.

The new controller appears in the Controller Organizer under the I/O Configuration folder.

Controller Organizer with CompactLogix 5380 controller.

Controller Organizer with GuardLogix 5580 controller.

6. In this example, a GuardLogix 5580 controller with 1756-EN2T communication module is used.

<!-- image -->

7. From the Edit menu, choose Controller Properties. The Controller Properties dialog box appears.
8. Click the Date/Time tab.
9. Check Enable Time Synchronization.

<!-- image -->

The motion modules set their clocks to the module that you assign as the Grandmaster.

## IMPORTANT

Check Enable Time Synchronization for all controllers that participate in CIP Sync™. The overall CIP Sync network automatically promotes a Grandmaster clock, unless the priority is set in the Advanced tab.

10. Click OK.

## Configure the Kinetix 5500 Drive

## IMPORTANT

To configure 2198-Hxxx-ERS (hardwired safety) drives, you must be using the Logix Designer application, version 21.00 or later.

To configure 2198-Hxxx-ERS2 (integrated safety) drives, you must be using the Logix Designer application, version 24.00 or later.

Use this table to determine where to begin your drive configuration.

| Drive Cat. No.   | Start Here                                         |   Page |
|------------------|----------------------------------------------------|--------|
| 2198-Hxxx-ERS    | Configure Drive with Hardwired Safety Connections  |    112 |
| 2198-Hxxx-ERS2   | Configure Drive with Integrated Safety Connections |    114 |

Configure Drive with Hardwired Safety Connections

Follow these steps to configure Kinetix 5500 drives with hardwired safety.

1. Below the controller you created, right-click Ethernet and choose New Module.

The Select Module Type dialog box appears.

<!-- image -->

2. By using the filters, check Motion and Allen-Bradley, and select your 2198-Hxxx-ERS servo drive as appropriate for your actual hardware configuration.
3. Click Create.

The New Module dialog box appears.

<!-- image -->

4. Configure the new drive.
- a. Type the drive Name.
- b. Select an Ethernet Address option.

In this example, the Private Network address is selected.

- c. Enter the address of your 2198-Hxxx-ERS drive.

In this example, the last octet of the address is 1.

- d. Under Module Definition click Change.

Depending on the Module Definition revision selection, alternate product features can be selected.

5. To close the New Module dialog box, click OK.

Your 2198-Hxxx-ERS servo drive appears in the Controller Organizer under the Ethernet controller in the

I/O Configuration folder.

6. Click Close to close the Select Module Type dialog box.
7. Jump to Continue Drive Configuration on page 117 to continue with your drive configuration.

<!-- image -->

## Configure Drive with Integrated Safety Connections

Follow these steps to configure Kinetix 5500 drives with integrated safety.

1. Below the controller you created, right-click Ethernet and choose New Module.

The Select Module Type dialog box appears.

<!-- image -->

2. By using the filters, check Motion and Allen-Bradley, and select your 2198-Hxxx-ERS2 servo drive as appropriate for your actual hardware configuration.
3. Click Create.

The New Module dialog box appears.

<!-- image -->

4. Configure the new drive.
- a. Type the drive Name.
- b. Select an Ethernet Address option.

In this example, the Private Network address is selected.

- c. Enter the address of your 2198-Hxxx-ERS2 servo drive.

In this example, the last octet of the address is 2.

- d. Under Module Definition click Change.

The Module Definition dialog box appears.

<!-- image -->

- e. From the Connection dropdown menu, choose the Connection mode for your motion application.

|                   | Connection Mode Controller Needed                                                                                          | Description Cat. No. 2198-Hxxx-ERS                       | Description Cat. No. 2198-Hxxx-ERS2                                                                                           |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Motion only       | ControlLogix 5570 or 5580 Guardlogix 5570 or 5580 as well CompactLogix 5370 or 5380 or 5480 CompactGuardLogix 5370 or 5380 | Only hardwired Safe Torque Off connections are possible. | Motion is managed by this controller. Safety is managed by another controller that has a Safety-only connection to the drive. |
| Motion and Safety | Guardlogix 5570 or 5580 CompactGuardLogix 5370 or 5380                                                                     |                                                          | — Motion and Safety are managed by this controller.                                                                           |
| Safety only       | GuardLogix 5570 or 5580 or Compact GuardLogix 5370 or 5380                                                                 | —                                                        | Safety is managed by this controller. Motion is managed by another controller that has a Motion-only connection to the drive. |

<!-- image -->

When 'Safety' appears in the Connection mode, integrated safety is implied.

The Safety Network Number (SNN) field populates automatically when the Connection mode includes an integrated Motion and Safety or Safety-only connection. For a detailed explanation of the safety network number, refer to the GuardLogix Controller Systems Safety Reference Manual, publication 1756-RM099 .

5. To close the Module Definition dialog box, click OK.
6. To close the New Module dialog box, click OK.

Your 2198-Hxxx-ERS2 servo drive appears in the Controller Organizer under the Ethernet controller in the I/O Configuration folder.

Right-click the drive you created in the Controller Organizer and choose Properties.

The Module Properties dialog box appears.

7. Click the Drive Safety tab.
8. From the Restart Type dropdown menu, choose Manual or Automatic depending on your specific application.
- Manual restart indicates a transition from 0 to 1 on the SO.Reset tag is required to allow torque after the SO.SafeTorqueOff tag has transitioned from 0 to 1.

<!-- image -->

<!-- image -->

- Automatic restart indicates that torque will be allowed only by transitioning the SO.SafeTorqueOff tag from 0 to 1. The SO.Reset tag is used only for resetting safety faults.
9. Click Apply.
10. Click the Safety tab.

<!-- image -->

The connection between the owner and the 2198-Hxxx-ERS2 servo drive is based on the following:

- Servo drive catalog number must be 2198-Hxxx-ERS2 (integrated)
- Servo drive safety network number
- GuardLogix slot number
- GuardLogix safety network number
- Path from the GuardLogix controller to the 2198-Hxxx-ERS2 drive
- Configuration signature

If any differences are detected, the connection between the GuardLogix controller and the 2198-Hxxx-ERS2 drive is lost, and the yellow yield icon appears in the controller project tree after you download the program.

11. Click Advanced.

The Advanced Connection Reaction Time Limit Configuration dialog box appears.

<!-- image -->

Analyze each safety channel to determine the appropriate settings. The smallest Input RPI allowed is 6 ms. Selecting small RPI values consumes network bandwidth and can cause nuisance trips because other devices cannot get access to the network.

12. Click OK.

For more information about the Advanced Connection Reaction Time Limit Configuration, refer to the GuardLogix 5570 Controllers User Manual, publication 1756-UM022 .

## Continue Drive Configuration

After you've established your Kinetix 5500 drive in the Logix Designer application, the remaining configuration steps are the same regardless of the drive catalog number.

1. Right-click the 2198-Hxxx-ERSx servo drive you created and choose Properties. The Module Properties dialog box appears.
2. Click the Associated Axes tab.
3. Click New Axis.

<!-- image -->

The New Tag dialog box appears.

<!-- image -->

4. Type the axis Name.
2. AXIS\_CIP\_DRIVE is the default Data Type.
5. Click Create.

The axis (Axis\_1 in this example) appears in the Controller Organizer under Motion Groups &gt; Ungrouped Axes and is assigned as Axis 1.

<!-- image -->

<!-- image -->

<!-- image -->

You can configure an axis as Feedback Only. See Configure Feedbackonly Axis Properties on page 121 for more information.

6. Click Apply.
7. Click the Digital Input tab.
8. From the Axis dropdown menu, choose an axis to configure.
9. From the Digital Input dropdown menus, choose a digital input assignment appropriate for your application. For more information, see Table 30 on page 64 and Table 31 on page 64 .
10. Click Apply.
11. Click the Power tab.

<!-- image -->

<!-- image -->

IMPORTANT Single-phase operation is possible only when Module Properties &gt; Power tab &gt; Bus Configuration is configured as Standalone.

## IMPORTANT

The Logix Designer application enforces shared-bus configuration rules for Kinetix 5500 drives, except for shared AC configurations.

12. From the dropdown menus, choose the power options appropriate for your actual hardware configuration.

<!-- image -->

ATTENTION: To avoid damage to equipment, make sure the AC input voltage that is configured in the Logix Designer application matches the actual hardware being configured.

| Attribute                     | Menu                         | Description                                                                                                                              |
|-------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Voltage                       |                              | 400-480 VAC 324…528 AC rms input voltage                                                                                                 |
| Voltage                       |                              | 200-240 VAC 195…264 AC rms input voltage                                                                                                 |
| AC Input Phasing              | • Three Phase • Single Phase | Input power phasing. Kinetix 5500 drives with single-phase operation is limited to 2198-H003- ERSx, 2198-H008-ERSx, and 2198-H015-ERSx . |
| Bus Configuration  (1)(2)     | Standalone                   | Applies to single-axis drives and drives with Shared AC input configurations.                                                            |
| Bus Configuration  (1)(2)     | Shared AC/DC                 | Applies to converter drives with Shared AC/DC and Shared AC/DC Hybrid input configurations.                                              |
| Bus Configuration  (1)(2)     | Shared DC                    | Applies to inverter drives with Shared DC input (common-bus) configurations.                                                             |
| Bus Sharing Group  (3)(2)     |                              | Standalone Applies to standalone bus configurations.                                                                                     |
| Bus Sharing Group  (3)(2)     | • Group1 • Group2 • Group3…  | Applies to any bus-sharing configuration. (4)                                                                                            |
| Shunt Regulator Action        | Disabled                     | Disables the internal shunt resistor and external shunt option.                                                                          |
| Shunt Regulator Action        |                              | Shunt Regulator Enables the internal and external shunt options.                                                                         |
| Shunt Regulator Resistor Type | Internal                     | Enables the internal shunt (external shunt option is disabled).                                                                          |
| Shunt Regulator Resistor Type | External                     | Enables the external shunt (internal shunt option is disabled).                                                                          |
| External Shunt (5)            | • None • 2097-R6 • 2097-R7   | Selects external shunt option. Only the shunt model that is intended for the drive model is shown.                                       |

## 13. Click OK.

14. Repeat step 1 through step 13 for each 2198-Hxxx-ERSx servo drive.

## Configure the Motion Group

Follow these steps to configure the motion group.

1. In the Controller Organizer, right-click Motion Groups and choose New Motion Group. The New Tag dialog box appears.
2. Type the new motion group Name.
3. Click Create.

<!-- image -->

Your new motion group appears in the Controller Organizer under the Motion Groups folder.

4. Right-click the new motion group and choose Properties.

The Motion Group Properties dialog box appears.

<!-- image -->

5. Click the Axis Assignment tab and move your axes (created earlier) from Unassigned to Assigned.
6. Click the Attribute tab and edit the default values as appropriate for your application.
7. Click OK.

Your axis moves to the new motion group.

<!-- image -->

<!-- image -->

## Configure Feedback-only Axis Properties

Follow these steps to configure feedback-only axis properties.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the General category.

The General dialog box appears.

<!-- image -->

3. From the Axis Configuration dropdown menu, choose Feedback Only.
4. From the Feedback Configuration dropdown menu, choose Master Feedback.
5. From the Module dropdown menu, choose the drive to associate with your Feedback Only axis.
4. The Module Type and Power Structure fields populate with the chosen drive catalog number.
6. Click Apply.
7. Select the Master Feedback Category.
7. The Master Feedback Device Specification appears.
8. From the Type dropdown menu, choose a feedback device type.
9. Review other categories in the Controller Organizer and make changes as needed for your application.
10. Click OK.

<!-- image -->

## Configure Induction-motor Frequency-control Axis Properties

Follow these steps to configure induction-motor axis properties for various frequency control methods.

## General and Motor Categories

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the General category.

The General dialog box appears.

<!-- image -->

3. From the Axis Configuration dropdown menu, choose Frequency Control.
4. From the Feedback Configuration dropdown menu, choose No Feedback.
5. From the Module dropdown menu, choose the drive to associate with your Frequency Control (induction motor) axis.
4. The Module Type and Power Structure fields populate with the chosen drive catalog number.
6. Click Apply.
7. Select the Motor category.

<!-- image -->

8. From the Data Source dropdown menu, choose Nameplate Datasheet. This is the default setting.
9. From the Motor Type dropdown menu, choose Rotary Induction.
10. From the motor nameplate or datasheet, enter the phase-to-phase values for your motor.
4. See Motor Category on page 226 for a motor performance datasheet example.
11. Click Apply.

## Basic Volts/Hertz Method

1. Configure the General tab and Motor tab as shown in General and Motor Categories on page 122 .
2. Select the Frequency Control category.
3. From the Frequency Control Method dropdown menu, select Basic Volts/Hertz.
4. Enter the Basic Volts/Hertz attribute values appropriate for your application. Default values are shown.
5. Click Apply.
6. Select the Parameter List category.
7. The Motion Axis Parameters dialog box appears.

<!-- image -->

<!-- image -->

7. From the Parameter Group dropdown menu, choose Frequency Control.
8. Set the FluxUp, SkipSpeed, VelocityDroop, and CurrentVectorLimit attributes appropriate for your application.
3. See the corresponding section in Appendix 5 for information and configuration examples regarding all of these topics.
9. Click OK.

## Sensorless Vector Method

1. Configure the General tab and Motor tab as shown in General and Motor Categories on page 122 .
2. Select the Frequency Control category.
3. From the Frequency Control Method dropdown menu, select Sensorless Vector.
4. Enter the Basic Volts/Hertz attribute values appropriate for your application. Default values are shown.
5. Click Apply.
6. Select the Parameter List category.
7. The Motion Axis Parameters dialog box appears.
8. From the Parameter Group dropdown menu, choose Frequency Control.
9. Set the FluxUp, SkipSpeed, VelocityDroop, MaximumFrequency, MaximumVoltage, and CurrentVectorLimit attributes appropriate for your application.

<!-- image -->

<!-- image -->

See the corresponding section in Appendix 5 for information and configuration examples regarding all of these topics.

10. Click Apply.
11. Select the Motor &gt; Model category.

Motor model attributes are automatically estimated from the Nameplate/Datasheet

- parameters. For improved performance, motor tests can be run.
12. Select the Motor &gt; Analyzer category.
13. The Analyze Motor to Determine Motor Model dialog box opens.
14. Click one of the motor test tabs.

<!-- image -->

In this example, Calculate Model is chosen. See Motor Tests and Autotune Procedure on page 228 for information about each of the tests.

15. Click Start.
16. Click Accept Test Results.
17. Click OK.

## Fan/Pump Volts/Hertz Method

1. Configure the General tab and Motor tab as shown in General and Motor Categories on page 122 .
2. Select the Frequency Control category.
3. From the Frequency Control Method dropdown menu, select Fan/Pump Volts/Hertz.
4. Enter the Basic Volts/Hertz attribute values appropriate for your application. Default values are shown.
5. Click Apply.
6. Select the Parameter List category. The Motion Axis Parameters dialog box appears.
7. From the Parameter Group dropdown menu, choose Frequency Control.
8. Set the FluxUp, SkipSpeed, VelocityDroop, RunBoost, MaximumFrequency, MaximumVoltage, and CurrentVectorLimit attributes appropriate for your application. See the corresponding section in Appendix 5 for information and configuration examples regarding all of these topics.
9. Click OK.

<!-- image -->

<!-- image -->

## Configure SPM Motor Closed-loop Control Axis Properties

Table 59 - Motor Feedback Compatibility

| Feedback Type   |    | Description                                                                                                                                                                                                              | Feedback Connector        |
|-----------------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Hiperface       | High-resolution single turn and multi-turn, absolute    | Applies to Kinetix MPL, MPM, MPF, MPS (-M/S or -V/E) rotary motors and Kinetix MPAS (ballscrew), MPAR, MPAI linear actuators, and Kinetix LDAT (-xDx) linear thrusters, which are wired to the 2198-H2DCK converter kit. | 2-pin motor feedback (MF) |
| Hiperface DSL   |    | Applies to Kinetix VPL, VPF, VPH, and VPS rotary motors wired to the 2198-KITCON-DSL connector kit.                                                                                                                      | 2-pin motor feedback (MF) |

## IMPORTANT

Unprogrammed Smart feedback devices (Hiperface Sin/Cos and Hiperface DSL) are not supported. Unprogrammed as load or feedbackonly feedback types are supported. Contact your local distributor or Rockwell Automation sales representative for support options.

Follow these steps to configure surface permanent-magnet (SPM) motor closed-loop axis properties.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the General category.
3. The General and Associated Module dialog box appears.
3. From the General dropdown menus, change configuration settings as needed for your application.

<!-- image -->

## IMPORTANT

Frequency Control is not supported for permanent magnet motors.

4. From the Associated Module &gt; Module dropdown menu, choose your Kinetix 5500 drive. The drive catalog number populates the Module Type and Power Structure fields.
5. Click Apply.
6. Select the Motor category.

Kinetix 5500 drives accept Hiperface and Hiperface DSL feedback from surface permanent magnet (SPM) motors when the appropriate feedback connector kit is used. Table 59 lists the compatible Allen-Bradley motors and actuators.

The Motor Device Specification dialog box appears.

<!-- image -->

7. From the Data Source dropdown menu, choose Catalog Number.
8. Click Change Catalog.

The Change Catalog Number dialog box appears.

<!-- image -->

9. Select the motor catalog number appropriate for your application. To verify the motor catalog number, refer to the motor nameplate.
10. To close the Change Catalog Number dialog box, click OK.
11. Click Apply.

Motor data specific to your motor appears in the Nameplate / Datasheet - Phase to Phase parameters field.

12. Select the Scaling category and edit the default values as appropriate for your application.
13. Click Apply, if you make changes.
14. Select the Load category and edit the default values as appropriate for your application.
15. Click Apply, if you make changes.
16. Select the Actions category.

<!-- image -->

<!-- image -->

The Actions to Take Upon Conditions dialog box appears.

<!-- image -->

From this dialog box, you can program actions for the drive module to take. See Logix 5000 Controller and Drive Behavior on page 149 for more information.

17. Select the Exceptions category.

The Action to Take Upon Exception Condition dialog box appears.

<!-- image -->

From this dialog box, you can change the action for exceptions (faults). See Logix 5000 Controller and Drive Behavior on page 149 for more information.

<!-- image -->

In the Logix Designer application, version 32.00 and later, Disable replaced StopDrive as the default Action.

18. Select the Parameter List category.

The Motion Axis Parameters dialog box appears.

<!-- image -->

From this dialog box, you can set brake engage and release delay times for servo motors. For recommended motor brake delay times, refer to the Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001 .

19. Click OK.
20. Repeat step 1 through step 19 for each servo motor axis.

## Download the Program

After completing the Logix Designer application and saving the file, you must download your program to the Logix 5000 processor.

## Apply Power to the Kinetix 5500 Drive

This procedure assumes that you have wired and configured your Kinetix 5500 system and your Logix 5000 controller.

<!-- image -->

SHOCK HAZARD: To avoid hazard of electrical shock, perform all mounting and wiring of the Bulletin 2198 servo drives before applying power. Once power is applied, connector terminals can have voltage present even when not in use.

Follow these steps to apply power to the Kinetix 5500 system.

1. Disconnect the load to the motor.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, disconnect the load to the motor. Make sure that each motor is free of all linkages when initially applying power to the system.

2. Apply 24V DC control power.

The LCD display begins the startup sequence. See Startup Sequence on page 106. If the startup sequence does not begin, check the 24V control power connections.

3. When the startup sequence completes, verify that the two status indicators are steady green and the axis state is PRECHARGE.

If the axis state does not reach PRECHARGE and the two status indicators are not steady green, refer to Kinetix 5500 Drive Status Indicators on page 146 .

## IMPORTANT

Apply control power before applying three-phase AC power. This makes sure that the shunt is enabled, which can help prevent nuisance faults or Bus Overvoltage faults.

4. Apply mains input power and monitor the DC BUS voltage on the LCD display.

If the DC BUS does not reach the expected voltage level, check the three-phase input power connections. Also, it can take as many as 1.8 seconds after input power is applied

- before the drive can accept motion commands.
5. Verify that the axis state changes to STOPPED.

If the axis state does not change to STOPPED, refer to Fault Code Overview on page 144 .

## Applying Power after Changing Input Voltage Range

This step applies to any drive or multi-axis drive configuration.

<!-- image -->

ATTENTION: To avoid damage to equipment when the configured input voltage range of the drive or drives changes from 230V AC to 460V AC or from 460V AC to 230V AC, the bus voltage must bleed down below 50V DC before the new configured input voltage is applied.

## Understand Bus-sharing Group Configuration

When configuring Module Properties &gt; Power tab for each Kinetix 5500 servo drive, you can breakout drives from one or more servo systems into multiple bus-sharing (power) groups.

A drive that faults in Group 1 does not affect the operation of Group 2, even though all drives in Groups 1 and 2 are in the same Motion group in the Logix Designer application.

Figure 63 - 25 Bus-sharing Groups Are Possible

<!-- image -->

## IMPORTANT

Bus-sharing groups do not apply to drives with a Bus Configuration of Standalone. When Standalone is configured as the Bus Configuration, Standalone (dimmed) is also configured as the Bus Sharing Group.

Figure 64 - Standalone Bus Configuration

<!-- image -->

## Bus-sharing Group Example

In this example, 12 axes are needed to support the motion application. All 12 axes are configured in the same Motion group in the Logix Designer application.

However, the 12 axes of motion are also configured as two bus-sharing groups and one standalone drive in Module Properties &gt; Power tab. By creating two bus-sharing groups, a converter drive that faults in Group 1 only disables Group 1 drives, and has no effect on the drive operation of Group 2 or the Standalone drive.

Figure 65 - Bus-sharing Group Example

<!-- image -->

## Configure Bus-sharing Groups

Group 1 is a shared AC/DC hybrid configuration. The Bus Configuration for the first two converter drives is Shared AC/DC. The Bus Configuration for the inverter drives is Shared DC.

<!-- image -->

ATTENTION: To avoid damage to equipment, all modules that are physically connected to the same shared-bus connection system must be part of the same Bus Sharing Group in the Logix Designer application.

Figure 66 - Group 1 Converter Drives Configuration

<!-- image -->

Figure 67 - Group 1 Inverter Drives Configuration

<!-- image -->

Group 2 is a shared DC (common-bus) configuration. The Bus Configuration for the leader drive is Shared AC/DC. The Bus Configuration for the follower drives is Shared DC.

Figure 68 - Group 2 Leader Drive Configuration

<!-- image -->

## Test and Tune the Axes

Figure 69 - Group 2 Follower Drives Configuration

<!-- image -->

Figure 70 - Standalone Drive Configuration

<!-- image -->

This procedure assumes that you have configured your Kinetix 5500 drive, your Logix 5000 controller, and applied power to the system.

## IMPORTANT

Before proceeding with testing and tuning your axes, verify that the MOD and NET status indicators are operating as described in Kinetix 5500 Drive Status Indicators on page 146 .

For help with using the Logix Designer application as it applies to testing and tuning your axes with a Logix 5000 controller, refer to Additional Resources on page 12 .

## Test the Axes

Follow these steps to test the axes.

1. Verify that the load was removed from each axis.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, you must remove the load from each axis as uncontrolled motion can occur when an axis with an integral motor brake is released during the test.

2. In your Motion Group folder, right-click an axis and choose Properties. The Axis Properties dialog box appears.

3. Click the Hookup Tests category.
4. In the Test Distance field, enter the desired test distance.
3. The Position Units are defined in the Axis Properties &gt; Scaling tab.
5. To verify connections, click the appropriate test from the following.

<!-- image -->

<!-- image -->

| Hookup Test Definitions   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Marker                    | Verifies marker detection capability as you manually rotate the motor shaft. The test completes when the drive either detects the marker or when the motor moves the distance that is specified in the Test Distance field. If the marker remains undetected and the test completes successfully, it means that the motor moved the full test distance. If the marker remains undetected and the test fails, the motor did not move the full test distance. Run this test after running the Motor Feedback and Motor and Feedback tests. |
| Commutation               | Verifies the commutation offset and commutation polarity of the motor. For Kinetix 5500 drives, this test applies to only third-party motors. See Commutation Test on page 243 .                                                                                                                                                                                                                                                                                                                                                         |
| Motor Feedback            | Verifies that feedback connections are wired correctly as you manually rotate the motor shaft. The test completes when the drive determines that the motor moved the full distance that is specified in the Test Distance field. Run this test before the Motor and Feedback Test to verify that the feedback can be read properly.                                                                                                                                                                                                      |
| Motor and Feedback        | Verifies that motor power and feedback connections are wired correctly as the drive commands the motor to rotate. Because the drive is rotating the motor, this test requires full bus power to run. Run the Motor Feedback test before running this test to verify that the feedback is being read correctly.                                                                                                                                                                                                                           |

## 6. Click Start.

The Logix Designer - Motor and Feedback Test dialog box appears. The Test State is Executing. TESTING appears on the drive LCD display.

<!-- image -->

When the test completes successfully, the Test State changes from Executing to Passed.

<!-- image -->

7. Click OK.

This dialog box appears asking if the direction was correct.

8. Click Yes.
9. Click Accept Test Results.
10. If the test fails, this dialog box appears.
- a. Click OK.
- b. Verify the DC bus voltage.
- c. Verify unit values entered in the Scaling category.
- d. Verify the motor power and feedback wiring.
- e. Return to step 6 and run the test again.

## Tune the Axes

Choose the tuning procedure best suited for your motor type.

<!-- image -->

| Motor Type            | Go Directly To                    |
|-----------------------|-----------------------------------|
| Permanent magnet (PM) | Tune Permanent Magnet Motors      |
| Induction             | Tune Induction Motors on page 140 |

Tune Permanent Magnet Motors

The load observer feature provides high-performance motion control without having to manually tune your axis. Using load observer with a default set of gains can yield highperformance right out of the box. Most of the time, there is no need to perform an autotune procedure or further optimize gain settings.

Follow these steps to configure the drive for high performance by using the load observer feature.

1. Verify that the load is connected.

Reattach the load if it was disconnected for the Hookup Test.

<!-- image -->

ATTENTION: If the drive has not been enabled before (new installation), verify that you have safeguards in place to safely remove power from the drive if there is an unstable situation where the drive can produce undesired motion.

2. Click the Autotune tab in the Axis Properties dialog box.
- a. From the dropdown menus for Application Type, Loop Response, and Load Coupling, choose Custom, Medium, and Rigid settings, respectively.

<!-- image -->

<!-- image -->

- b. Verify that only the Velocity Feedforward box is checked.

<!-- image -->

Uncheck Torque Low Pass Filter (that is checked by default).

3. Click the Load category in the Axis Properties dialog box.
- a. Check Use Load Ratio.
- b. Set the Load Ratio = 0.
4. Click the Observer category in the Axis Properties dialog box.
- a. From the Configuration dropdown menu, choose Load Observer with Velocity Estimate if the axis is configured for Position Loop control.

<!-- image -->

Choose Load Observer Only if the axis is configured for Velocity Loop control. Load Observer is not available for Torque Loop control.

<!-- image -->

- b. Click Apply and click Yes to update all dependent attributes.
2. The Load Observer Bandwidth and other gains are set automatically.

<!-- image -->

5. Click the Compliance category in the Axis Properties dialog box.
- a. From the Adaptive Tuning Configuration dropdown menu, choose Tracking Notch.
- b. Click Apply.
6. Enable the drive for a few seconds with an MSO instruction or motion direct command, followed by an MSF instruction or motion direct command, to make sure that no audible squealing noise is present.

<!-- image -->

## IMPORTANT

If an audible squealing noise is heard, go to Axis Properties&gt;Load&gt; Compliance category and set the Torque Notch Filter Frequency field (Hz) to remove the noise. See Motion System Tuning Application Techniques, publication MOTION-AT005 (Compensating for High Frequency Resonances), for information on how to set the Torque Notch Filter Frequency field.

7. Repeat Test and Tune the Axes for each axis.

Tune Induction Motors

IMPORTANT

The Automatic FluxUpControl setting is recommended for best Autotune results.

Follow these steps to tune the induction motor axes.

1. Verify that the load is removed from the axis being tuned.

<!-- image -->

ATTENTION: To reduce the possibility of unpredictable motor response, tune your motor with the load removed first, then reattach the load and perform the tuning procedure again to provide an accurate operational response.

2. Select the Autotune category.
3. Type values for Travel Limit and Speed.
3. In this example, Travel Limit = 50.0 and Speed = 2.0. The actual values of programmed units depend on your application.
4. From the Direction dropdown menu, choose a setting appropriate for your application. Forward Uni-directional is default.
5. Edit other fields as appropriate for your application.
6. Click Start.

<!-- image -->

The Logix Designer - Autotune dialog box appears. When the test completes, the Test State changes from Executing to Success.

<!-- image -->

Tuned values populate the Loop and Load parameter tables. Actual bandwidth values (Hz) depend on your application and can require adjustment once motor and load are connected.

7. Click Accept Tuned Values.

8. To close the Logix Designer - Autotune dialog box, click OK.
9. To close the Axis Properties dialog box, click OK.
10. If the test fails, this dialog box appears.
- a. Click OK.
- b. Adjust motor velocity.
- c. See the controller user manual for more information.
- d. Return to step 6 and run the test again.
11. Repeat Test and Tune the Axes for each axis.

<!-- image -->

## Safety Precautions

<!-- image -->

## Troubleshoot the Kinetix 5500 Drive System

This chapter provides troubleshooting tables and related information for your Kinetix® 5500 servo drives.

| Topic                                    |   Page |
|------------------------------------------|--------|
| Safety Precautions                       |    143 |
| Interpret Status Indicators              |    144 |
| General Troubleshooting                  |    147 |
| Logix 5000 Controller and Drive Behavior |    149 |

Observe the following safety precautions when troubleshooting your Kinetix 5500 servo drive.

<!-- image -->

ATTENTION: Capacitors on the DC bus can retain hazardous voltages after input power has been removed. Before working on the drive, measure the DC bus voltage to verify that it has reached a safe level or wait the full-time interval as indicated in the warning on the front of the drive. Failure to observe this precaution could result in severe bodily injury or loss of life.

<!-- image -->

<!-- image -->

ATTENTION: Do not attempt to defeat or override the drive fault circuits. You must determine the cause of a fault and correct it before you attempt to operate the system. Failure to correct the fault could result in personal injury and/or damage to equipment as a result of uncontrolled machine operation.

ATTENTION: Provide an earth ground for test equipment (oscilloscope) used in troubleshooting. Failure to ground the test equipment could result in personal injury.

## Interpret Status Indicators

This section contains troubleshooting tables that can be used to identify faults, potential causes of faults, and the appropriate actions to resolve a fault. If the fault persists after attempting to troubleshoot the system, contact your Rockwell Automation sales representative for further assistance.

## Display Interface

The LCD display provides fault messages and troubleshooting information by using the soft menu items and navigation buttons.

Under the Main Menu, select FAULT LOG by using the up/down arrows.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

|    | Press to display the list of active fault codes.                                  |
|----|-----------------------------------------------------------------------------------|
|    | Press again to display the fault details (the problem in troubleshooting tables). |
| ?  | Press to display the fault help (possible solutions in troubleshooting tables).   |

See Understand the Kinetix 5500 Display on page 102 for more information on navigating the LCD display menu.

## Fault Code Overview

The fault code tables are designed to help you determine the source of the fault or exception. When a fault condition is detected, the drive performs the appropriate fault action, the fault is displayed, and the fault is added to a persistent fault log (along with diagnostics data). The earlier faults have priority to be displayed.

The drive removes the fault text from the display when a Fault Reset service is sent from the controller and the fault is no longer active. If a fault is still active following a Fault Reset service, the fault is again posted to the display and written to the fault log.

However, there is a delay before the fault is posted again. In a Studio 5000 Logix Designer® application, this delay results as the AxisFault tag on the drive axis being cleared until the fault is posted again. During this delay, the AxisState tag continues to indicate that the axis is faulted. Use the AxisState tag on the axis object and only to determine if an axis is faulted.

Although software overtravel fault codes do not exist, software overtravel detection for the AXIS\_CIP\_DRIVE axis type is determined in the Logix 5000® controller. For more information, see Integrated Motion on the EtherNet/IP™ Network Reference Manual, publication MOTIONRM003 .

The drive maintains a log of the last 128 faults with time stamps and is stored in persistent memory. However, the fault log cannot be cleared on the drive.

## Table 60 - Fault Code Summary

| Fault Code Type  (1)(2)    | Description                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| FLT Sxx                    | Standard runtime axis exceptions. The exception can apply to an individual axis or to all axes.                                                     |
| FLT Mxx                    | Manufacturer-specific runtime axis exception. The exception can apply to an individual axis or to all axes.                                         |
| INIT FLT Sxx  INIT FLT Mxx | Exceptions that prevent normal operation and occur during the initialization process.                                                               |
| NODE FLTxx                 | Exceptions that can prevent normal operation of the drive module and apply to the entire module and affect all axes.                                |
| NODE ALARM xx              | Exceptions that can prevent normal operation of the drive module, but do not result in any action other than reporting the alarm to the controller. |
| INHIBIT Sxx                | Conditions that prevent normal operation and indicate that the drive module is prevented from being enabled. INHIBIT Mxx                            |
|                            | Conditions that prevent normal operation and indicate that the drive module is prevented from being enabled. INHIBIT Mxx                            |

## Table 60 - Fault Code Summary (Continued)

| Fault Code Type  (1)(2)   | Description                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ALARM Sxx                 | An underlying exception condition that does not result in any action other than reporting the alarm to the controller. ALARM Mxx |
| SAFE FLTxx                | Exception that is generated by a fault condition that is detected in the safety function.                                        |

(2) Mxx refers to Manufacturer-specific exceptions.

<!-- image -->

## Fault Codes

<!-- image -->

Fault codes that are triggered by conditions that fall outside factory-set limits are identified by FL at the end of the display message. For example, FLT S07 – MTR OVERLOAD FL.

Fault codes that are triggered by conditions that fall outside user-set limits are identified by UL at the end of the display message. For example,

FLT S08 – MTR OVERLOAD UL.

This manual links to Kinetix 5500 Servo Drive Fault Codes Reference Data, publication 2198-RD005, for fault codes. Download the spreadsheet now for offline access.

## Kinetix 5500 Servo Drive

<!-- image -->

## Ethernet RJ45 Connectors

<!-- image -->

## Kinetix 5500 Drive Status Indicators

The module status and network status indicators are just above the LCD status display.

| IMPORTANT   | Status indicators are not reliable for safety functions. Use them only for general diagnostics during commissioning or troubleshooting. Do not attempt to use status indicators to determine operational status.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 61 - Module Status Indicator

| Condition      | Status                                                                                                                    |
|----------------|---------------------------------------------------------------------------------------------------------------------------|
| Steady Off     | No power is being applied to the drive.                                                                                   |
| Steady Green   | Drive is operational. No faults or failures.                                                                              |
| Flashing Green | Standby (drive not configured).                                                                                           |
| Flashing Red   | Major recoverable fault. The drive detected a recoverable fault, for example, an incorrect or inconsistent configuration. |
| Steady Red     | Major fault. The drive detected a nonrecoverable fault.                                                                   |
|                | Flashing Green/Red Self-test. The drive performs self-test during powerup.                                                |

## Table 62 - Network Status Indicator

| Condition      | Status                                                                                                 |
|----------------|--------------------------------------------------------------------------------------------------------|
| Steady Off     | No power applied to the drive or IP address is not configured.                                         |
| Flashing Green | Drive connection is not established, but has obtained an IP address.                                   |
| Steady Green   | Drive connection is established. Normal operation.                                                     |
| Flashing Red   | Connection timeout. One or more of the connections, for which this drive is the target, has timed out. |
| Steady Red     | Duplicate IP address. IP address specified is already in use.                                          |
|                | Flashing Green/Red Self-test. The drive performs self-test during powerup.                             |

Table 63 - Ethernet Link Speed Status Indicator

| Condition   | Status   |
|-------------|----------|
| Steady Off  | 10 Mbit  |
| Steady On   | 100 Mbit |

Table 64 - Ethernet Link/Activity Status Indicator

| Condition   | Status           |
|-------------|------------------|
| Steady Off  | No link          |
| Steady On   | Link established |
| Blinking    | Network activity |

<!-- image -->

## General Troubleshooting

## Kinetix 5500 Capacitor Module Status Indicators

The capacitor module status indicator and module status (MS) connector are on the front of the module. The module status connector is a relay output suitable for wiring to the Logix 5000 controller.

Table 65 - Module Status Indicator and Relay Output

| Module Status Indicator Relay Output  (1)   | Status                                                          | Resolution                                                                                                       |
|---------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
|                                             | Steady Green Closed Bus is fully charged and no faults exist. — |                                                                                                                  |
| Flashing Green Open                         | Control power is present and the bus is waiting to charge up.   | —                                                                                                                |
| Flashing Red Open                           | Recoverable fault (precharge or overvoltage fault).             | • Cycle control and bus power • Verify that AC input meets specifications                                        |
| Steady Red Open                             | Internal, nonrecoverable fault condition inside the module.     | • Cycle control and bus power • Verify that AC input meets specifications • Replace the module if fault persists |

(1) Wiring the module status relay output to the Logix 5000 controller is optional.

These conditions do not always result in a fault code, but can require troubleshooting to improve performance.

| Condition                                                            | Potential Cause                                                                                                                                                     | Possible Resolution                                                                                                                                                                                                               |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Axis or system is unstable.                                          | The position feedback device is incorrect or open.                                                                                                                  | Check wiring.                                                                                                                                                                                                                     |
| Axis or system is unstable.                                          | Unintentionally in Torque mode.                                                                                                                                     | Check to see what primary operation mode was programmed.                                                                                                                                                                          |
| Axis or system is unstable.                                          | Motor tuning limits are set too high.                                                                                                                               | Run Tune in the Logix Designer application.                                                                                                                                                                                       |
| Axis or system is unstable.                                          | Position loop gain or position controller accel/decel rate is improperly set.                                                                                       | Run Tune in the Logix Designer application.                                                                                                                                                                                       |
| Axis or system is unstable.                                          | Improper grounding or shielding techniques are causing noise to be transmitted into the position feedback or velocity command lines, causing erratic axis movement. | Check wiring and ground.                                                                                                                                                                                                          |
| Axis or system is unstable.                                          | Motor Select limit is incorrectly set (servo motor is not matched to axis module).                                                                                  | • Check setups. • Run Tune in the Logix Designer application.                                                                                                                                                                     |
| Axis or system is unstable.                                          | Mechanical resonance.                                                                                                                                               | • Notch filter or output filter can be required (refer to Axis Properties dialog box, Output tab in the Logix Designer application). • Enable adaptive tuning. See Adaptive Tuning on page 243 for more notch filter information. |
| You cannot obtain the motor acceleration/deceleration that you want. | Torque Limit limits are set too low.                                                                                                                                | Verify that torque limits are set properly.                                                                                                                                                                                       |
| You cannot obtain the motor acceleration/deceleration that you want. | Incorrect motor selected in configuration.                                                                                                                          | Select the correct motor and run Tune in the Logix Designer application again.                                                                                                                                                    |
| You cannot obtain the motor acceleration/deceleration that you want. | The system inertia is excessive.                                                                                                                                    | • Check motor size versus application need. • Review servo system sizing.                                                                                                                                                         |
| You cannot obtain the motor acceleration/deceleration that you want. | The system friction torque is excessive.                                                                                                                            | Check motor size versus application need.                                                                                                                                                                                         |
| You cannot obtain the motor acceleration/deceleration that you want. | Available current is insufficient to supply the correct accel/decel rate.                                                                                           | • Check motor size versus application need. • Review servo system sizing.                                                                                                                                                         |
| You cannot obtain the motor acceleration/deceleration that you want. | Acceleration limit is incorrect.                                                                                                                                    | Verify limit settings and correct them, as necessary.                                                                                                                                                                             |
| You cannot obtain the motor acceleration/deceleration that you want. | Velocity Limit limits are incorrect.                                                                                                                                | Verify limit settings and correct them, as necessary.                                                                                                                                                                             |
| You cannot obtain the motor acceleration/deceleration that you want. | The motor is operating in the field-weakening range of operation. Reduce the commanded acceleration or deceleration.                                                |                                                                                                                                                                                                                                   |

| Condition                                                                                   | Potential Cause                                                                                                                                                                                                                                                | Possible Resolution                                                                                                                    |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Motor does not respond to a command.                                                        | The axis cannot be enabled until stopping time has expired. Disable the axis, wait for 1.5 seconds, and enable the axis.                                                                                                                                       |                                                                                                                                        |
| Motor does not respond to a command.                                                        | The motor wiring is open.                                                                                                                                                                                                                                      | Check the wiring.                                                                                                                      |
| Motor does not respond to a command.                                                        | The motor cable shield connection is improper.                                                                                                                                                                                                                 | • Check feedback connections. • Check cable shield connections.                                                                        |
| Motor does not respond to a command.                                                        | The motor has malfunctioned.                                                                                                                                                                                                                                   | Repair or replace the motor.                                                                                                           |
| Motor does not respond to a command.                                                        | The coupling between motor and machine has broken (for example, the motor moves, but the load/machine does not).                                                                                                                                               | Check and correct the mechanics.                                                                                                       |
| Motor does not respond to a command.                                                        | Primary operation mode is set incorrectly.                                                                                                                                                                                                                     | Check and properly set the limit.                                                                                                      |
| Motor does not respond to a command.                                                        | Velocity or torque limits are set incorrectly.                                                                                                                                                                                                                 | Check and properly set the limits.                                                                                                     |
| Motor does not respond to a command.                                                        | Brake connector not wired                                                                                                                                                                                                                                      | Check brake wiring                                                                                                                     |
| Presence of noise on command or motor feedback signal wires.                                | Recommended grounding per installation instructions have not been followed.                                                                                                                                                                                    | • Verify grounding. • Route wire away from noise sources. • See System Design for Control of Electrical Noise, publication GMC-RM001 . |
| Presence of noise on command or motor feedback signal wires.                                | Line frequency can be present.                                                                                                                                                                                                                                 | • Verify grounding. • Route wire away from noise sources.                                                                              |
| Presence of noise on command or motor feedback signal wires.                                | Variable frequency can be velocity feedback ripple or a disturbance that is caused by gear teeth or ballscrew, and so forth. The frequency can be a multiple of the motor power transmission components or ballscrew speeds resulting in velocity disturbance. | • Decouple the motor for verification. • Check and improve mechanical performance, for example, the gearbox or ballscrew mechanism.    |
| No rotation                                                                                 | The motor connections are loose or open. Check motor wiring and connections.                                                                                                                                                                                   |                                                                                                                                        |
| No rotation                                                                                 | Foreign matter is lodged in the motor.                                                                                                                                                                                                                         | Remove foreign matter.                                                                                                                 |
| No rotation                                                                                 | The motor load is excessive.                                                                                                                                                                                                                                   | Verify the servo system sizing.                                                                                                        |
| No rotation                                                                                 | The bearings are worn.                                                                                                                                                                                                                                         | Return the motor for repair.                                                                                                           |
| No rotation                                                                                 | The motor brake is engaged (if supplied).                                                                                                                                                                                                                      | • Check brake wiring and function. • Return the motor for repair.                                                                      |
| No rotation                                                                                 | The motor is not connected to the load.                                                                                                                                                                                                                        | Check coupling.                                                                                                                        |
| Motor overheating                                                                           | The duty cycle is excessive.                                                                                                                                                                                                                                   | Change the command profile to reduce accel/decel or increase time.                                                                     |
| Motor overheating                                                                           | The rotor is partially demagnetized causing excessive motor current. Return the motor for repair.                                                                                                                                                              |                                                                                                                                        |
|                                                                                             | Motor tuning limits are set too high.                                                                                                                                                                                                                          | Run Tune in the Logix Designer application.                                                                                            |
|                                                                                             | Loose parts are present in the motor.                                                                                                                                                                                                                          | • Remove the loose parts. • Return motor for repair. • Replace motor.                                                                  |
| Abnormal noise                                                                              | The through bolts or coupling is loose.                                                                                                                                                                                                                        | Tighten bolts.                                                                                                                         |
|                                                                                             | The bearings are worn.                                                                                                                                                                                                                                         | Return motor for repair.                                                                                                               |
|                                                                                             | Mechanical resonance.                                                                                                                                                                                                                                          | Notch filter can be required (refer to Axis Properties dialog box, Output tab in the Logix Designer application).                      |
| Erratic operation - Motor locks into position, runs without control or with reduced torque. | Motor power phases U and V, U and W, or V and W reversed. Check and correct motor power wiring.                                                                                                                                                                |                                                                                                                                        |

## Logix 5000 Controller and Drive Behavior

By using the Logix Designer application, you can configure how the Kinetix 5500 drives respond when a drive fault/exception occurs.

<!-- image -->

The INIT FLT xxx faults are always generated after powerup, but before the drive is enabled, so the stopping behavior does not apply. NODE ALARM xxx faults do not apply because they do not trigger stopping behavior.

The drive supports fault actions for Ignore, Alarm, Minor Fault, and Major Fault as defined in Table 66. The drive also supports three configurable stopping actions as defined in Table 68 .

See the drive behavior tables beginning on page 151 to see how the fault and stopping actions apply to each of the exception fault codes.

Table 66 - Kinetix 5500 Drive Exception Action Definitions

| Exception Action Definition   |                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ignore                        | The drive completely ignores the exception condition. For some exceptions that are fundamental to the operation of the planner, Ignore is not an available option.                                                                                                                                                                  |
| Alarm                         | The drive sets the associated bit in the Motion Alarm Status word, but does not otherwise affect axis behavior. Like Ignore, if the exception is so fundamental to the drive, Alarm is not an available option. When an exception action is set to Alarm, the Alarm goes away by itself when the exceptional condition has cleared. |
| Minor Fault                   | The drive latches the exception condition but the drive does not execute any exception action.                                                                                                                                                                                                                                      |
|                               | Major Fault The drive latches the exception condition and executes the configured exception action.                                                                                                                                                                                                                                 |

You can configure exception behavior in the Logix Designer application from the Axis Properties dialog box, Actions category. These controller exception actions are mapped to the drive exception actions.

Table 67 - Logix Designer Exception Action Definitions

| Exception Action Definition                                       |                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ignore                                                            | The controller completely ignores the exception condition. For some exceptions that are fundamental to the operation of the planner, Ignore is not an available option.                                                                                                                                                                                                                                        |
| Alarm                                                             | The controller sets the associated bit in the Motion Alarm Status word, but does not otherwise affect axis behavior. Like Ignore, if the exception is so fundamental to the drive, Alarm is not an available option. When an exception action is set to Alarm, the Alarm goes away by itself when the exceptional condition has cleared.                                                                       |
| Fault Status Only                                                 | Like Alarm, Fault Status Only instructs the controller to set the associated bit in the Motion Fault Status word, but does not otherwise affect axis behavior. However, unlike Alarm, an explicit Fault Reset is required to clear the fault once the exceptional condition has cleared. Like Ignore and Alarm, if the exception is so fundamental to the drive, Fault Status Only is not an available option. |
| Stop Planner                                                      | The controller sets the associated bit in the Motion Fault Status word and instructs the Motion Planner to perform a controlled stop of all planned motion at the configured maximum deceleration rate. An explicit Fault Reset is required to clear the fault once the exceptional condition has cleared. If the exception is so fundamental to the drive, Stop Planner is not an available option.           |
| StopDrive (version 31 and earlier) Disable (version 32 and later) | When the exception occurs, the associated bit in the Fault Status word is set and the axis comes to a stop by using the stopping action that is defined by the drive for the particular exception that occurred. There is no controller-based configuration to specify what the stopping action is; the stopping action is device-dependent.                                                                   |
| Shutdown                                                          | When the exception occurs, the drive brings the motor to a stop by using the stopping action defined by the drive (as in Stop Drive) and the power module is disabled. An explicit Shutdown Reset is required to restore the drive to operation.                                                                                                                                                               |

For Kinetix 5500 drives, only selected exceptions are configurable. In the drive behavior tables, the controlling attribute is given for programmable fault actions.

Table 68 - Configurable Stopping Actions

<!-- image -->

| Stopping Action Description        |                                                                                                                                                      |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Decel and hold Most control        | The best available stopping action is the one that maintains the most control over the motor. However, not all faults support every stopping action. |
| Decel and disable (1) Less control | The best available stopping action is the one that maintains the most control over the motor. However, not all faults support every stopping action. |
| Disable and coast Least control    | The best available stopping action is the one that maintains the most control over the motor. However, not all faults support every stopping action. |

(1) When configured for Frequency Control (induction motors only), select Decel and disable only when the Current Limiting feature is enabled. For more information on this feature, see Current Limiting for Frequency Control on page 216 .

When configured for Frequency Control (IM motors only), Decel and disable should only be selected when the Current Limiting feature has been enabled. For more information on this feature, refer to Appendix 5 .

Only selected drive exceptions are configurable. In the drive behavior tables, the controlling attribute is given for programmable fault actions.

<!-- image -->

In the Logix Designer application, version 32.00 and later, Disable replaced StopDrive as the default Action.

Figure 71 - Logix Designer Axis Properties - Actions Category

<!-- image -->

This dialog box applies to Kinetix 5500 (EtherNet/IP network) servo drives.

Table 69 - Drive Behavior, FLT Sxx Fault Codes

|                                                           |                                                           |                        | Induction Motor   | Fault Action                  | Best Available Stopping Action (applies to major faults)   | Fault Action   | Fault Action   |
|-----------------------------------------------------------|-----------------------------------------------------------|------------------------|-------------------|-------------------------------|------------------------------------------------------------|----------------|----------------|
| Exception Fault Code Exception Text                       |                                                           | Permanent Magnet Motor |                   | Ignore Minor FaultMajor Fault | Alarm                                                      |                |                |
| FLT S02 – MTR COMMUTATION Motor Commutation Fault X       |                                                           |                        | —                 |                               | — — — X Disable/Coast                                      |                |                |
| FLT S03 – MTR OVERSPEED FL                                | Motor Overspeed Factory Limit Fault                       |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S04 – MTR OVERSPEED UL                                | Motor Overspeed User Limit Fault                          | X                      | X                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S05 – MTR OVERTEMP FL                                 | Motor Overtemperature Factory Limit Fault                 |                        |                   |                               | X — — — — X Disable/Coast                                  |                |                |
| FLT S07 – MTR OVERLOAD FL                                 | Motor Thermal Overload Factory Limit Fault                |                        |                   |                               | X X — — — X Decel/Disable                                  |                |                |
| FLT S08 – MTR OVERLOAD UL                                 | Motor Thermal OverLoad User Limit Fault                   | X                      | X                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S10 – INV OVERCURRENT Inverter Overcurrent Fault X    |                                                           |                        | X                 |                               | — — — X Disable/Coast                                      |                |                |
| FLT S11 – INV OVERTEMP FL                                 | Inverter Overtemperature Factory Limit Fault              |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S13 – INV OVERLOAD FL                                 | Inverter Thermal Overload Factory Limit Fault             |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S14 – INV OVERLOAD UL                                 | Inverter Thermal Overload User Limit Fault                | X                      | X                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S15 – CONV OVERCURRENT Converter Overcurrent Fault X  |                                                           |                        | X                 |                               | — — — X Disable/Coast                                      |                |                |
| FLT S16 – GROUND CURRENT                                  | Ground Current Factory Limit Fault                        |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S18 – CONV OVERTEMP FL                                | Converter OverTemp Factory Limit Fault                    |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S20 – CONV OVERLOAD FL                                | Converter Thermal OverLoad Factory Limit Fault            |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S21 – CONV OVERLOAD UL                                | Converter Thermal Overload User Limit Fault               | X                      | X                 |                               | X X X X Decel/Hold                                         |                |                |
|                                                           | FLT S23 – AC PHASE LOSS AC Single Phase Loss Fault X      |                        | X                 |                               | X X X X Decel/Disable                                      |                |                |
| FLT S25 – PRECHARGE FAILURE Pre-charge Failure Fault X    |                                                           |                        | X                 |                               | — — — X Disable/Coast                                      |                |                |
| FLT S29 – BUS OVERLOAD FL                                 | Bus Regulator Thermal OverLoad Factory Limit Fault        |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S30 – BUS OVERLOAD UL                                 | Bus Regulator Thermal Overload User Limit Fault           | X                      | X                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S31 – BUS REG FAILURE Bus Regulator Failure X         |                                                           |                        | X                 |                               | — — — X Disable/Coast                                      |                |                |
| FLT S33 – BUS UNDERVOLT FL                                | Bus Undervoltage Factory Limit Fault                      |                        |                   |                               | X X — — — X Decel/Disable                                  |                |                |
| FLT S34 – BUS UNDERVOLT UL                                | Bus Undervoltage User Limit Fault                         | X                      | X                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S35 – BUS OVERVOLT FL                                 | Bus Overvoltage Factory Limit Fault                       |                        |                   |                               | X X — — — X Disable/Coast                                  |                |                |
| FLT S39 – BUS POWER LEAKAGE Bus Power Leakage Fault X     |                                                           |                        | X                 |                               | — — — X Decel/Disable                                      |                |                |
| FLT S45 – FDBK COMM FL (1)                                | Motor Feedback Data Loss Factory Limit Fault              |                        |                   |                               | X — — — — X Disable/Coast                                  |                |                |
| FLT S47 – FDBK DEVICE FAILURE Feedback Device Failure X   |                                                           |                        | —                 |                               | — — — X Disable/Coast                                      |                |                |
| FLT S49 – BRAKE SLIP FLT Brake Slip Exception X           |                                                           |                        | —                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S50 – POS HW OTRAVEL Hardware Overtravel - Positive X |                                                           |                        | X                 | X X X X Decel/Hold            | X X X X Decel/Hold                                         |                |                |
|                                                           | FLT S51 – NEG HW OTRAVEL Hardware Overtravel - Negative X |                        | X                 |                               |                                                            |                |                |
| FLT S54 – POSN ERROR (1)                                  | Excessive Position Error Fault X                          |                        | —                 |                               | X X X X Disable/Coast                                      |                |                |
| FLT S55 – VEL ERROR (1)                                   | Excessive Velocity Error Fault X                          |                        | —                 |                               | X X X X Disable/Coast                                      |                |                |
| FLT S56 – OVERTORQUE LIMIT  (1)                           | Overtorque Limit Fault X                                  |                        | —                 |                               | X X X X Decel/Hold                                         |                |                |
| FLT S57 – UNDERTORQUE LIMIT  (1)                          | Undertorque Limit Fault X                                 |                        | —                 |                               | X X X X Decel/Hold                                         |                |                |

## Table 70 - Drive Behavior, FLT Mxx Fault Codes

|                                                                                      |                        |                 | Fault Action   | Fault Action                                                                          | Fault Action   | Fault Action   |
|--------------------------------------------------------------------------------------|------------------------|-----------------|----------------|---------------------------------------------------------------------------------------|----------------|----------------|
| Exception Fault Code Exception Text                                                  | Permanent Magnet Motor | Induction Motor | Ignore         | Best Available Stopping Action (applies to major faults) Alarm Minor FaultMajor Fault |                |                |
| FLT M02 – MOTOR VOLTAGE Motor Voltage Mismatch Fault X                               |                        | X               |                | X X X X Disable/Coast                                                                 |                |                |
| FLT M25 – COMMON BUS DC Common Bus Fault X                                           |                        | X               |                | — — — X Decel/Disable                                                                 |                |                |
| FLT M26 – RUNTIME ERROR Runtime Error                                                | X                      | X               |                | — — — X Disable/Coast                                                                 |                |                |
| FLT M28 – SAFETY COMM (2198-Hxxx-ERS2 drives only) Safety Module Communication Error |                        |                 |                | X X — — — X Disable/Coast                                                             |                |                |

## Table 71 - Drive Behavior, NODE FLT Fault Codes

|                                                        |                                  |                        | Induction   | Fault Action   | Best Available Stopping Action                         | Fault Action   | Fault Action   |
|--------------------------------------------------------|----------------------------------|------------------------|-------------|----------------|--------------------------------------------------------|----------------|----------------|
| Exception Fault Code Exception Text                    |                                  | Permanent Magnet Motor | Motor       | Ignore         | (applies to major faults) Alarm Minor FaultMajor Fault |                |                |
| NODE FLT 01 – LATE CTRL UPDATE                         | Control Connection Update Fault  |                        |             |                | X X — — — X Decel/Disable                              |                |                |
| NODE FLT 02 – PROC WATCHDOG Processor Watchdog Fault X |                                  |                        | X           |                | — — — X Disable/Coast                                  |                |                |
| NODE FLT 03 – HARDWARE Hardware Fault                  |                                  | X                      | X           |                | — — — X Disable/Coast                                  |                |                |
| NODE FLT 05 – CLOCK SKEW FLT Clock Skew Fault          |                                  | X                      | X           |                | — — — X Disable/Coast                                  |                |                |
| NODE FLT 06 – LOST CTRL CONN                           | Lost Controller Connection Fault |                        |             |                | X X ———X Decel/Disable                                 |                |                |
| NODE FLT 07 – CLOCK SYNC Clock Sync Fault              |                                  | X                      | X           |                | — — — X Disable/Coast                                  |                |                |
| NODE FLT 09 – DUPLICATE IP ADDRESS                     | Duplicate IP Address Fault X     |                        | X           |                | — — — X Disable/Coast                                  |                |                |

## Before You Begin

<!-- image -->

## Remove and Replace Servo Drives

This chapter provides remove and replace procedures for Kinetix® 5500 drives.

| Topic                                        |   Page |
|----------------------------------------------|--------|
| Before You Begin                             |    153 |
| Remove and Replace Kinetix 5500 Servo Drives |    154 |
| Start and Configure the Drive                |    156 |

<!-- image -->

ATTENTION: This drive contains electrostatic discharge (ESD) sensitive parts and assemblies. You are required to follow static-control precautions when you install, test, service, or repair this assembly. If you do not follow ESD control procedures, components can be damaged. If you are not familiar with static control procedures, refer to Guarding Against Electrostatic Damage, publication 8000-4.5.2, or any other applicable ESD awareness handbook.

When each drive is installed, network settings are configured from the setup screens. Before removing the drive, revisit the Network menu and make note of the static IP or DHCP settings. See Configure the Drive on page 107 to access those settings.

| IMPORTANT   | If you intend to use the same Logix Designer application after replacing your drive, the new drive must be the same catalog number as the old drive.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|

You also need these tools available before you begin removal and replacement procedures:

- Screwdrivers (to loosen/remove screws)
- Voltmeter (to make sure that no voltage exists on drive connectors)
- Non-conductive probe for removing DC bus T-connectors

## Remove and Replace Kinetix 5500 Servo Drives

Follow these steps to remove and replace servo drives from the panel.

## Remove Power and All Connections

1. Verify that all control and input power has been removed from the system.

<!-- image -->

ATTENTION: To avoid shock hazard or personal injury, make sure that all power has been removed before proceeding. This system can have multiple sources of power. Multiple disconnect switches can be required to de-energize the system.

2. Wait five minutes for the DC bus to discharge completely before proceeding.

<!-- image -->

SHOCK HAZARD: This product contains stored energy devices. To avoid the hazard of electrical shock, verify that the voltage on the capacitors has been discharged before attempting to service, repair, or remove this unit. Do not attempt the procedures in this document unless you are qualified to do so and are familiar with solid-state control equipment and the safety procedures in publication NFPA 70E.

3. Label and remove all wiring connectors from the drive that you are removing. To identify each connector, refer to Kinetix 5500 Connector Data on page 60 .

<!-- image -->

You do not need to remove the shunt (RC) connector, unless there is an external shunt that is wired to it.

4. Remove the shared-bus input wiring connectors, T-connectors, and busbars from the drive you are removing.

## IMPORTANT

DC bus T-connectors latch on both sides when inserted into the drive. To remove the DC bus T-connector, at least one latch must be pried away with a non-conductive probe.

See Shared-bus Connection System on page 49 .

5. Use a screwdriver to loosen the two cable clamp screws, removing the screw on the right.
6. Remove the single motor cable from the cable shield clamp.
7. Remove the ground screw and braided ground strap. See Ground the System Subpanel on page 76 .

<!-- image -->

## Remove the Servo Drive

You can remove single-axis drives from the panel or any single drive from a multi-axis configuration by using the same procedure.

IMPORTANT This procedure applies to any 2198-Hxxx-ERSx drive in any configuration.

Follow these steps to remove Kinetix 5500 servo drives from the panel.

1. Loosen the top and bottom screws of the drive to remove. Frame 1 and 2 drives have one top and bottom screw. Frame 3 drives have two top and bottom screws.
2. Grasp the top and bottom of the drive with both hands and pull the drive straight out and away from the panel, clearing the zero-stack mounting tabs and cutouts.

<!-- image -->

## Replace the Servo Drive

To replace the servo drive, reverse the steps in the Remove the Servo Drive procedure or refer to Mount Your Kinetix 5500 Drive on page 58:

- Torque mounting, shield clamp, and ground screws to 2.0 N·m (17.7 lb·in), max
- Reconnect the feedback connector kit and torque the mounting screws to 0.4 N·m (3.5 lb·in), max

## Start and Configure the Drive

Follow these steps to configure the replacement drive.

## IMPORTANT

If you intend to use the same Logix Designer application after replacing your drive, the new drive must be the same catalog number as the old drive.

## IMPORTANT

If a 2198-Hxxx-ERS2 drive was previously configured by a safety controller, reset the drive to the Out of Box state. See Out-of-Box State on page 169 .

1. Reapply power to the drive/system.

See Apply Power to the Kinetix 5500 Drive on page 132 for the procedure.

2. Configure the network settings for the drive.
- a. If your old drive was configured as Static IP, you must set the IP address, gateway, and subnet mask in the new drive identical to the old drive. See Configure the Drive on page 107 to access those settings.
- b. If you replaced a 2198-Hxxx-ERS2 servo drive in an integrated safety application, review Understand Integrated Safety Drive Replacement on page 171 and follow the appropriate procedure in Replace an Integrated Safety Drive in a GuardLogix System on page 171 to properly set the safety network number for the new drive.
3. Download the Logix Designer application to the controller.
4. Verify the drive/system is working properly.

## Certification

<!-- image -->

## Kinetix 5500 Safe Torque Off - Hardwired Safety

The 2198-Hxxx-ERS servo drives are equipped for hardwired Safe Torque Off (STO). The hardwired STO function meets the requirements of Performance Level d (PLd) and safety category 3 (CAT 3) per ISO 13849-1, and SIL 2 per IEC 61508, IEC 61800-5-2, and IEC 62061.

| Topic                                     |   Page |
|-------------------------------------------|--------|
| Certification                             |    157 |
| Description of Operation                  |    159 |
| Probability of Dangerous Failure Per Hour |    161 |
| Safe Torque Off Connector Data            |    161 |
| Wire the Safe Torque Off Circuit          |    162 |
| Safe Torque Off Feature                   |    163 |
| Safe Torque Off Specifications            |    164 |

A ControlLogix® 5570, ControlLogix 5580, CompactLogix™ 5370, or CompactLogix 5380 controller is required for hardwired safety control of the Kinetix® 5500 Safe Torque Off function. The 2198-Hxxx-ERS servo drives use the STO connector for wiring external safety devices and cascading hardwired safety connections from one drive to another.

The TÜV Rheinland group has approved 2198-Hxxx-ERS servo drives with hardwired Safe Torque Off for use in safety-related applications up to ISO 13849-1, Performance Level d (PLd) and Category 3, SIL CL 2 per IEC 61508, IEC 61800-5-2, and IEC 62061, in which removing the motion producing power is considered to be the safe state.

For product certifications currently available from Rockwell Automation, go to website rok.auto/certifications .

## Important Safety Considerations

You, the system user, are responsible for the following:

- Validation of any sensors or actuators that are connected to the system
- Completing a machine-level risk assessment
- Certification of the machine to the desired ISO 13849-1 Performance Level or IEC 62061 SIL level
- Project management and proof testing in accordance with ISO 13849

## Category 3 Requirements According to ISO 13849-1

Safety-related parts are designed with these attributes:

- A single fault in any of these parts does not lead to the loss of the safety function.
- A single fault is detected whenever reasonably practicable.
- Accumulation of undetected faults can lead to the loss of the safety function and a failure to remove motion producing power from the motor.

## Stop Category Definition

Stop Category 0 as defined in IEC 60204 or Safe Torque Off as defined by IEC 61800-5-2 is achieved with immediate removal of motion producing power to the actuator.

## IMPORTANT

If there is a malfunction, the most likely stop category is Stop Category 0. When designing the machine application, timing and distance must be considered for a coast-to-stop. For more information regarding stop categories, refer to IEC 60204-1.

## Performance Level (PL) and Safety Integrity Level (SIL)

For safety-related control systems, Performance Level (PL), according to ISO 13849-1, and SIL levels, according to IEC 61508 and IEC 62061, include a rating of the systems ability to perform its safety functions. All safety-related components of the control system must be included in both a risk assessment and the determination of the achieved levels.

See the ISO 13849-1, IEC 61508, and IEC 62061 standards for complete information on requirements for PL and SIL determination.

## Description of Operation

The Safe Torque Off feature provides a method, with sufficiently low probability of failure, to force the power-transistor control signals to a disabled state. When disabled, or any time power is removed from the safety enable inputs, all drive output-power transistors are released from the ON-state. This results in a condition where the drive performs a Category 0 Stop. Disabling the power transistor output does not provide mechanical isolation of the electrical output that is required for some applications.

Under normal operation, the Safe Torque Off inputs are energized. If either of the safety enable inputs are de-energized, then all output power transistors turn off. The Safe Torque Off response time is less than 12 ms.

<!-- image -->

ATTENTION: If there are two simultaneous faults in the IGBT circuit, permanent magnet motors can result in a rotation of up to 180 electrical degrees.

<!-- image -->

ATTENTION: If any of the safety enable inputs de-energize, the Start Inhibit field indicates SafeTorqueOffInhibit and GuardStopRequestStatus bit of AxisGuardStatus tag set to 1. Both inputs must be de-energized within 1 second and re-energized within 1 second to avoid GuardStopInputFault conditions.

Figure 72 - System Operation when Inputs are Meeting Timing Requirements

<!-- image -->

|    | Event Description                                                                                                                                                                                                                                                                                                                            |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    | 1 At least one input is switched-off. GuardStopRequestStatus bit is set to 1.                                                                                                                                                                                                                                                                |
| 2  | Second input is switched-off within 1 second. This event must always occur before event 3 to prevent GuardStopInputFault.                                                                                                                                                                                                                    |
|    | 3 First input is switched-on.                                                                                                                                                                                                                                                                                                                |
|    | 4 Second input is switched-on within 1 second of event 3.                                                                                                                                                                                                                                                                                    |
| 5  | Both inputs are in OFF state simultaneously within 1 second. As a result, GuardStopInputFault is not posted.                                                                                                                                                                                                                                 |
| 6  | The GuardStopRequestStatus bit sets back to 0 if event 4 occurs within a 100 ms interval after event 3. If event 4 is outside of the 100 ms interval, but within the 1 second interval after event 3, then the GuardStop RequestStatus bit sets back to 0 after the 1 second interval following event 3 (not immediately following event 4). |

## Fault Codes

<!-- image -->

This manual links to Kinetix 5500 Servo Drive Fault Codes Reference Data, publication 2198-RD005, for fault codes. Download the spreadsheet now for offline access.

Figure 73 demonstrates when the Safe Torque Off mismatch is detected and a GuardStopInputFault is posted.

Figure 73 - System Operation in the Event that the Safety Enable Inputs Mismatch

<!-- image -->

| SS_IN_CH0            | 24V DC     |
|----------------------|------------|
| SS_IN_CH1            |            |
| GuardStopInputFault  | 0 1 Second |
| SafeTorqueOffInhibit |            |

When one safety input is turned off, the second input must also be turned off, otherwise a fault is asserted (see Figure 74). The fault is asserted even if the first safety input is turned on again, without the second input transitioning to the ON state.

Figure 74 - System Operation in the Event that the Safety Enable Inputs Mismatch Momentarily

<!-- image -->

| SS_IN_CH0            | 24V DC   |
|----------------------|----------|
| SS_IN_CH1            | 24V DC   |
| GuardStopInputFault  | 1        |
| SafeTorqueOffInhibit | 1 0      |

<!-- image -->

ATTENTION: The Safe Torque Off fault is detected upon demand of the Safe Torque Off function. After troubleshooting the STO function or performing maintenance that might affect the STO function, the STO function must be executed to verify correct operation.

## IMPORTANT

The GuardStopInputFault can be reset only if both inputs are in the OFFstate for more than 1 second. After the fault reset requirement is satisfied, an MAFR command in the Logix Designer application must be issued to reset the GuardStopInputFault.

## Probability of Dangerous Failure Per Hour

## Safe Torque Off Connector Data

Safety-related systems are classified as operating in a High-demand/continuous mode. The SIL value for a High-demand/continuous mode safety-related system is directly related to the probability of a dangerous failure occurring per hour (PFH).

PFH calculation is based on the equations from IEC 61508 and shows worst-case values. Table 72 provides data for a 20-year proof test interval and demonstrates the worst-case effect of various configuration changes on the data.

| IMPORTANT   | Determination of safety parameters is based on the assumptions that the system operates in High-demand mode and that the safety function is requested at least once every three months.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

l

Table 72 - PFH for 20-year Proof Test Interval

| Attribute          |   Value |
|--------------------|---------|
| PFH (1e-9)         |    0.35 |
| Proof test (years) |   20    |

The 10-pin connector consists of two parallel 5-pin rows for cascading safety connections from drive-to-drive in multi-axis configurations.

Figure 75 - Pin Orientation for 10-pin Safe Torque Off (STO) Connector

<!-- image -->

Table 73 - Safe Torque Off (STO) Connector Pinouts

| STO Pin Description                                                                      | Signal   |
|------------------------------------------------------------------------------------------|----------|
| 1  Safety bypass plus signal. Connect to both safety inputs to disable the STO function. | SB+      |
| 2  Safety bypass minus signal. Connect to safety common to disable the STO function.     | SB          |
| 3 STO input 1 (SS_IN_CH0).                                                               | S1       |
| 4 STO input common (SCOM).                                                               | SC       |
| 5 STO input 2 (SS_IN_CH1).                                                               | S2       |

## Wire the Safe Torque Off Circuit

This section provides guidelines for wiring your Kinetix 5500 Safe Torque Off drive connections.

## IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

## IMPORTANT

## IMPORTANT

To improve system performance, run wires and cables in the wireways as established in Establishing Noise Zones beginning on page 43 .

Pins ST0-1 and ST0-2 (SB+ and SB-) are used to disable the Safe Torque Off function. When wiring to the STO connector, use an external 24V supply for the external safety device that triggers the Safe Torque Off request. To avoid jeopardizing system performance, do not use pin ST0-1 (SB+) as a power supply for the external safety device.

## Safe Torque Off Wiring Requirements

The Safe Torque Off (STO) connector uses spring tension to secure the wire. Depress the tab, along side each pin, to insert or release the wire. Two rows of pins are provided for drive-to- 
°° g ppp
drive connections. Wire must be copper with 75 °C (167 °F) minimum rating.

## IMPORTANT

Stranded wires must terminate with ferrules to help prevent short circuits, per table D7 of ISO 13849-1.

Figure 76 - Safe Torque Off (STO) Terminal Plug

<!-- image -->

Table 74 - Safe Torque Off (STO) Terminal Plug Wiring

| Safe Torque Off (STO) Connector   | Safe Torque Off (STO) Connector   | Recommended Wire Size mm 2  (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-----------------------------------|-----------------------------------|-------------------------------------|-------------------------|----------------------------|
|                                   | Pin Signal                        |                                     |                         |                            |
| STO-1 STO-2 STO-3 STO-4 STO-5     | SB+ SB S1 SC S2                                   | 0.2…1.5 (24…16)                     | 10 (0.39)               | —  (1)                     |

(1) This connector uses spring tension to hold the wires in place.

## Safe Torque Off Feature

The Safe Torque Off circuit, when used with suitable safety components, provides protection according to ISO 13849-1 (PLd), Category 3 or according to IEC 61508, IEC 61800-5-2, and IEC 62061 (SIL CL 2). All components in the system must be chosen and applied correctly to achieve the desired level of operator safeguarding.

The Safe Torque Off circuit is designed to safely turn off all output-power transistors. You can use the Safe Torque Off circuit in combination with other safety devices to achieve Stop Category 0 and protection-against-restart as specified in IEC 60204-1.

<!-- image -->

ATTENTION: This option is suitable only for performing mechanical work on the drive system or affected area of a machine. It does not provide electrical safety.

<!-- image -->

<!-- image -->

SHOCK HAZARD: In Safe Torque Off mode, hazardous voltages can still be present at the drive. To avoid an electric shock hazard, disconnect power to the system and verify that the voltage is zero before performing any work on the drive.

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

## Safe Torque Off Feature Bypass

The 2198-Hxxx-ERS drives do not operate without a safety circuit or safety bypass wiring. For applications that do not require the Safe Torque Off feature, you must install jumper wires to bypass the Safe Torque Off circuitry.

Each 2198-Hxxx-ERS drive includes one 10-pin wiring plug for wiring to safety devices. To bypass the safety function, wire these signals as shown in Figure 77. With the jumper wires installed, the Safe Torque Off feature is not used.

<!-- image -->

## Cascade the Safe Torque-off Signal

The total number of drives in a single cascaded safety circuit is limited by the current carrying capacity of the cascaded safety wiring. See Table 75 for current rating per channel, per drive.

Figure 78 - Cascaded Safe Torque Off Wiring

<!-- image -->

## Safe Torque Off Specifications

To maintain safety rating, Kinetix 5500 drives must be installed inside protected control panels or cabinets appropriate for the environmental conditions of the industrial location. The protection class of the panel or cabinet must be IP54 or higher.

Table 75 - Safe Torque Off Signal Specifications

| Attribute                   | Attribute                               | Value                                            |
|-----------------------------|-----------------------------------------|--------------------------------------------------|
| Safety inputs (per channel) | Input current                           | < 10 mA                                          |
| Safety inputs (per channel) | Input ON voltage range 18…26.4V DC      |                                                  |
| Safety inputs (per channel) | Input OFF voltage, max 5V DC            |                                                  |
| Safety inputs (per channel) | Input ON current, per input, max        | 10 mA, each drive (1)                            |
| Safety inputs (per channel) | Input OFF current, max (@ V in < 5V DC) | 2 mA                                             |
| Safety inputs (per channel) | Pulse rejection width 700 s            |                                                  |
| Safety inputs (per channel) | External power supply SELV/PELV         |                                                  |
| Safety inputs (per channel) | Input type                              | Optically isolated and reverse voltage protected |

For additional information regarding Allen-Bradley® safety products, including safety relays, light curtain, and gate interlock applications, refer to https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/safetyproducts.html .

## Certification

<!-- image -->

## Kinetix 5500 Safe Torque Off - Integrated Safety

The 2198-Hxxx-ERS2 servo drives are equipped for integrated Safe Torque Off (STO). The integrated STO function meets the requirements of Performance Level e (PLe) and safety category 3 (CAT 3) per ISO 13849-1, and SIL 3 per IEC 61508, IEC 61800-5-2, and IEC 62061.

With integrated safety, the GuardLogix® 5570 or Compact GuardLogix 5570 safety controller issues the Safe Torque Off (STO) command over the

EtherNet/IP™ network and the 2198-Hxxx-ERS2 servo drive executes the STO command.

| Topic                                                     |   Page |
|-----------------------------------------------------------|--------|
| Certification                                             |    165 |
| Description of Operation                                  |    167 |
| Probability of Dangerous Failure Per Hour                 |    168 |
| Safe Torque Off Feature                                   |    169 |
| Out-of-Box State                                          |    169 |
| Understand Integrated Safety Drive Replacement            |    171 |
| Replace an Integrated Safety Drive in a GuardLogix System |    171 |
| Motion Direct Commands in Motion Control Systems          |    173 |
| Safe Torque Off Specifications                            |    177 |
| Safe Torque Off Specifications                            |    177 |

The TÜV Rheinland group has approved 2198-Hxxx-ERS2 servo drives with integrated Safe Torque Off for use in safety-related applications up to ISO 13849-1, Performance Level e (PLe) and Category 3, SIL CL 3 per IEC 61508, IEC 61800-5-2, and IEC 62061, in which removing the motion producing power is considered to be the safe state.

For product certifications currently available from Rockwell Automation, go to website rok.auto/certifications .

## Important Safety Considerations

You, the system user, are responsible for the following:

- Validation of any sensors or actuators that are connected to the system
- Completing a machine-level risk assessment
- Certification of the machine to the desired ISO 13849-1 Performance Level or IEC 62061 SIL level
- Project management and proof testing performed in accordance with ISO 13849

## Safety Application Requirements

Safety application requirements include evaluating probability of failure rates (PFH), system reaction time settings, and functional verification tests that fulfill SIL 3 criteria. See Probability of Dangerous Failure Per Hour on page 168 for more PFH information.

Creating, recording, and verifying the safety signature is also a required part of the safety application development process. Safety signatures are created by the safety controller. The safety signature consists of an identification number, date, and time that uniquely identifies the safety portion of a project. This includes all safety logic, data, and safety I/O configuration.

For safety system requirements, including information on the safety network number (SNN), verifying the safety signature, and functional verification tests refer to the GuardLogix 5570 Controller Systems Safety Reference Manual, publication 1756-RM099 .

## IMPORTANT

You must read, understand, and fulfill the requirements that are detailed in publication 1756-RM099 before operating a safety system that uses a GuardLogix controller and 2198-Hxxx-ERS2 servo drive.

## Category 3 Requirements According to ISO 13849

Safety-related parts are designed with these attributes:

- A single fault in any of these parts does not lead to the loss of the safety function.
- A single fault is detected whenever reasonably practicable.
- Accumulation of undetected faults can lead to the loss of the safety function and a failure to remove motion producing power from the motor.

## Stop Category Definition

Stop Category 0 as defined in IEC 60204 or Safe Torque Off as defined by IEC 61800-5-2 is achieved with immediate removal of motion producing power to the actuator.

## IMPORTANT

If there is a malfunction, the most likely stop category is Stop Category 0. When designing the machine application, timing and distance must be considered for a coast-to-stop. For more information regarding stop categories, refer to IEC 60204-1.

## Description of Operation

## Performance Level (PL) and Safety Integrity Level (SIL)

For safety-related control systems, Performance Level (PL), according to ISO 13849-1, and SIL levels, according to IEC 61508 and IEC 62061, include a rating of the systems ability to perform its safety functions. All safety-related components of the control system must be included in both a risk assessment and the determination of the achieved levels.

See the ISO 13849-1, IEC 61508, and IEC 62061 standards for complete information on requirements for PL and SIL determination.

The Safe Torque Off (STO) feature provides a method, with sufficiently low probability of failure, to force the power-transistor control signals to a disabled state. When the command to execute the STO function is received from the GuardLogix controller, all drive output-power transistors are released from the ON-state. This results in a condition where the drive is coasting. Disabling the power transistor output does not provide mechanical isolation of the electrical output that is required for some applications.

The 2198-Hxxx-ERS2 drive STO function response time is less than 10 ms. Response time is the delay between the time when the drive STO function receives the integrated safety packet with an STO request and the time when motion producing power is removed from the motor.

## STO State Reset

The 2198-Hxxx-ERS2 servo drives support both manual and automatic restart types for exiting the STO state.

- Manual restart indicates a transition from 0 to 1 on the SO.Reset tag is required to allow torque after the SO.SafeTorqueOff tag has transitioned from 0 to 1.
- Automatic restart indicates that torque will be allowed only by transitioning the SO.SafeTorqueOff tag from 0 to 1. The SO.Reset tag is used only for resetting safety faults.

## IMPORTANT

2198-Hxxx-ERS2 servo drives enter the STO state if any STO function fault is detected.

See Figure 79 for an understanding of the 2198-Hxxx-ERS2 STO-state manual restart functionality.

<!-- image -->

| Figure 79 - Kinetix 5500 STO Timing Diagram - Manual Restart   | Figure 79 - Kinetix 5500 STO Timing Diagram - Manual Restart   |
|----------------------------------------------------------------|----------------------------------------------------------------|
| Drv:SO.SafeTorqueOff                                           |                                                                |
| Drv:SO.Reset                                                   |                                                                |
| Drv:SI.ResetRequired                                           |                                                                |
| Drv:SI.TorqueDisabled                                          |                                                                |
| Axis.SafeTorqueOffActiveInhibit                                |                                                                |
| Axis.SafeTorqueOffActiveStatus                                 |                                                                |
| Axis.SafeTorqueDisabledStatus                                  |                                                                |
| Axis.SafetyResetRequestStatus                                  |                                                                |
| Safe Torque-off Request Axis.SafetyResetRequiredStatus         | Reset Request                                                  |

## Probability of Dangerous Failure Per Hour

## Fault Codes

<!-- image -->

This manual links to Kinetix 5500 Servo Drive Fault Codes Reference Data, publication 2198-RD005, for fault codes. Download the spreadsheet now for offline access.

Safety-related systems are classified as operating in a High-demand/continuous mode. The SIL value for a High-demand/continuous mode safety-related system is directly related to the probability of a dangerous failure occurring per hour (PFH).

PFH calculation is based on the equations from IEC 61508 and shows worst-case values. Table 76 provides data for a 20-year proof test interval and demonstrates the worst-case effect of various configuration changes on the data.

| IMPORTANT   | Determination of safety parameters is based on the assumptions that the system operates in High-demand mode and that the safety function is requested at least once every three months.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Table 76 - PFH for 20-year Proof Test Interval

| Attribute          |   Value |
|--------------------|---------|
| PFH (1e-9)         |    1.54 |
| Proof test (years) |   20    |

## Safe Torque Off Feature

## Out-of-Box State

The Safe Torque Off feature, when used with suitable safety components, provides protection according to ISO 13849-1 (PLe), Category 3 or according to IEC 61508, IEC 61800-5-2, and IEC 62061 (SIL CL 3). All components in the system must be chosen and applied correctly to achieve the desired level of operator safeguarding.

The Safe Torque Off feature is designed to safely turn off all output power transistors. You can use the Safe Torque Off feature in combination with other safety devices to achieve Stop Category 0 and protection-against-restart as specified in IEC 60204-1.

<!-- image -->

ATTENTION: This option is designed to restrict motion producing power on the drive system or affected area of a machine. It does not provide electrical safety.

<!-- image -->

<!-- image -->

SHOCK HAZARD: In Safe Torque Off mode, hazardous voltages can still be present at the drive. To avoid an electric shock hazard, disconnect power to the system and verify that the voltage is zero before performing any work on the drive.

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

The 2198-H xxx-ERS2 servo drives ship in the out-of-box state.

<!-- image -->

ATTENTION: In the out-of-box state, motion producing power is allowed by the Safe Torque Off (STO) function unless an integrated safety connection configuration has been applied to the drive at least once.

In the out-of-box state, you can configure 2198-Hxxx-ERS2 servo drives as follows:

- Without a GuardLogix 5570 safety controller for a non-safety application.
- With a GuardLogix 5570 safety controller when the Safe Torque Off (STO) function is not required.

## Out-of-Box State Support

After the integrated safety connection configuration is applied to the 2198-Hxxx-ERS2 servo drive at least once, you can restore the drive to the out-of-box state.

Follow these steps to restore your 2198-Hxxx-ERS2 servo drive to the out-of-box state.

1. Right-click the 2198-Hxxx-ERS2 servo drive that you created and choose Properties.

<!-- image -->

2. Click the Connection tab.

The Connection tab appears.

<!-- image -->

3. Check Inhibit Module.
4. Click Apply and click the Safety tab.

The Safety tab appears.

<!-- image -->

5. In the Configuration Ownership field, click Reset Ownership.

IMPORTANT

Only authorized personnel should attempt Reset Ownership.

If any active connection is detected, the reset is rejected.

6. Cycle drive power.

The drive is in the out-of-box state.

| IMPORTANT   | If power to the drive is not cycled after step 5, the drive does not transition to the out-of-box state and maintains STO function.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | When the drive returns to the out-of-box state, STO safety integrity is lost.                                                         |

## Understand Integrated Safety Drive Replacement

## Replace an Integrated Safety Drive in a GuardLogix System

GuardLogix controllers retain the I/O device configuration onboard and are able to download the configuration to the replacement device.

IMPORTANT

If a 2198-Hxxx-ERS2 servo drive was used previously, clear the existing configuration before installing it on a safety network by resetting the drive to its out-of-box condition. To see how this is done, refer to Out-of-Box State Support on page 169 .

Replacing a 2198-Hxxx-ERS2 servo drive that sits on an integrated safety network is more complicated than replacing standard devices because of the safety network number (SNN).

The device number and SNN compose the safety device's DeviceID. Safety devices require this more complex identifier to make sure that duplicate device numbers do not compromise communication between the correct safety devices. The SNN is also used to provide integrity on the initial download to the 2198-Hxxx-ERS2 servo drive.

When the Logix Designer application is online, the Safety tab of the Module Properties dialog box displays the current configuration ownership. When the opened project owns the configuration, Local is displayed.

<!-- image -->

Communication error is displayed if the module read fails. See Replace an Integrated Safety Drive in a GuardLogix System for integrated safety drive replacement information.

When you replace an integrated safety drive, the replacement device must be configured properly and the replacement drives operation be user-verified.

<!-- image -->

ATTENTION: During drive replacement or functional test, the safety of the system must not rely on any portion of the affected drive.

Two options for safety drive replacement are available on the Safety tab of the Controller Properties dialog box in the Logix Designer application:

- Configure Only When No Safety Signature Exists
- Configure Always

Figure 80 - Safety Drive Replacement Options

<!-- image -->

## Configure Only When No Safety Signature Exists

This setting instructs the GuardLogix controller to automatically configure a safety drive only under the following conditions:

- The safety task does not have a safety task signature.
- The replacement drive is in an out-of-box condition, meaning that a safety network number does not exist in the safety drive.

If the safety task has a safety task signature, the GuardLogix controller automatically configures the replacement CIP Safety™ I/O device only if the following is true:

- The device already has the correct safety network number.
- The device electronic keying is correct.
- The node or IP address is correct.

For detailed information, see the GuardLogix 5570 Controllers User Manual, publication 1756UM022 or Compact GuardLogix 5370 Controllers User Manual, publication 1769-UM022 .

## Configure Always

When the Configure Always feature is enabled, the controller automatically checks for and connects to a replacement drive that meets the following requirements:

- The controller has configuration data for a compatible drive at that network address
- The drive is in Hardwired STO mode or has an SNN that matches the configuration

<!-- image -->

<!-- image -->

ATTENTION: Enable the Configure Always feature only if the entire integrated safety control system is not being relied on to maintain SIL 3 behavior during the replacement and functional testing of a Kinetix 5500 drive. Do not place drives that are in Hardwired STO mode on an integrated safety network when the Configure Always feature is enabled. If other parts of the integrated safety control system are being relied upon to maintain SIL 3, make sure that the controller's Configure Always feature is disabled.

It is your responsibility to implement a process to make sure that proper safety functionality is maintained during device replacement.

ATTENTION: Do not place any devices in the out-of-box condition on any integrated safety network when the Configure Always feature is enabled, except while following the device replacement procedure in the GuardLogix user manual appropriate for your Logix 5000® controller:

- GuardLogix 5570 Controllers User Manual, publication 1756-UM022
- Compact GuardLogix 5370 Controllers User Manual, publication 1769-UM022 .

## Motion Direct Commands in Motion Control Systems

You can use the Motion Direct Command (MDC) feature to initiate motion while the controller is in Program mode, independent of application code that is executed in Run mode. These commands let you perform various functions, for example, move an axis, jog an axis, or home an axis.

Some typical uses might involve the following:

- a machine integrator testing different parts of the motion system while the machine is being commissioned
- a maintenance engineer, under certain restricted scenarios in accordance with safe machine operating procedures, wanting to move an axis (like a conveyor) to clear a jam before resuming normal operation

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, follow these rules regarding Run mode and Program mode.

- Only authorized, trained personnel with knowledge of safe machine operation should be allowed to use Motion Direct Commands
- Additional supervisory methods, like removing the controller keyswitch, should be used to maintain the safety integrity of the system after returning the safety controller to RUN mode

## Understand STO Bypass When Using Motion Direct Commands

If a Safety-only connection between the GuardLogix safety controller and the 2198-Hxxx-ERS2 servo drive was established at least once after the drive was received from the factory, the drive does not allow motion while the safety controller is in Program mode by default.

This is because the safety task is not executed while the GuardLogix safety controller is in Program mode. This applies to applications running in a single-safety controller (with Motion and Safety connections). When an integrated safety drive has a Motion connection to a standard controller and a separate Safety connection to a dual-safety controller, the standard controller can transition to Program mode while the safety controller stays in Run mode and continues to execute the safety task.

However, 2198-Hxxx-ERS2 drive systems are designed with a bypass feature for the STO function in single-safety controller configurations. You can use the MDC feature to allow motion while following all necessary and prescribed steps per machine safety operating procedures.

<!-- image -->

ATTENTION: Consider the consequences of allowing motion by using MDC when the controller is in Program mode. You must acknowledge warning messages in the Logix Designer application that warn of the drive bypassing the STO function and unintended motion can occur. The integrated safety drive does not respond to the request of STO function if MDC mode is entered.

ATTENTION: It is your responsibility to maintain machine safety integrity while executing motion direct commands. One alternative is to provide ladder logic for Machine Maintenance mode that leaves the controller in Run mode with safety functions executing.

## Logix Designer Application Warning Messages

When the controller is in Run mode, executing safety functions, the 2198-Hxxx-ERS2 drive follows the commands that it receives from the safety controller. Safety state = Running, Axis state = Stopped/Running, as shown in Figure 81 .

Figure 81 - Safety State Indications When Controller is in Run Mode (safety task executing)

<!-- image -->

When the controller transitions to Program mode, the integrated safety drive is in the safe state (torque not permitted). Safety state = Not Running, Axis state = Start Inhibited, as shown in Figure 82).

Figure 82 - Safety State Indications After Controller Transitions to Program Mode

<!-- image -->

When you issue a motion direct command to an axis to produce torque in Program mode, for example MSO or MDS, with the safety connection present to the drive, a warning message is presented before the motion direct command is executed, as shown in Figure 83 .

Figure 83 - STO Bypass Prompt When the Safety Controller is in Program Mode

<!-- image -->

The warning in Figure 83 is displayed the first time a motion direct command is issued.

After you acknowledge the warning message by clicking Yes, torque is permitted by the drive and a warning message is indicated in the software as shown in Figure 84. Safety state = Not Running (torque permitted), Axis state = Stopped/Running, Persistent Warning = Safe Torque Off Bypassed.

IMPORTANT

Switch the controller to Run mode to exit Motion Direct Command mode with STO function bypassed.

Figure 84 - Safety State Indications After Controller Transitions to Program Mode (MDC executing)

<!-- image -->

## IMPORTANT

The persistent warning message text 'Safe Torque Off bypassed' appears when a motion direct command is executed.

Warning message persists even after the dialog is closed and reopened as long as the integrated safety drive is in STO Bypass mode.

The persistent warning message is removed only after the integrated safety drive is restored to the Safe state.

## Torque Permitted in a Multi-workstation Environment

The warning in Figure 85 is displayed to notify a second user working in a multi-workstation environment that the first user has placed the integrated safety drive in the STO state and that the current action is about to bypass the STO state and permit torque.

Figure 85 - STO Bypass Prompt When MDC is Issued in Multi-workstation Environment

<!-- image -->

## Warning Icon and Text in Axis Properties

In addition to the other warnings that require your acknowledgment, the Logix Designer application also provides warning icons and persistent warning messages in other Axis Properties dialog boxes when the integrated safety drive is in STO Bypass mode.

Figure 86 - Axis and Safe State Indications on the Hookup Services Dialog Box

<!-- image -->

Figure 87 - Axis and Safe State Indications on Motion Direct Commands Dialog Box

<!-- image -->

## Safe Torque Off Specifications

Figure 88 - Axis and Safe State Indications on the Motion Console Dialog Box

<!-- image -->

## Functional Safety Considerations

<!-- image -->

ATTENTION: Before maintenance work can be performed in Program mode, the developer of the application must consider the implications of allowing motion through motion direct commands and should consider developing logic for runtime maintenance operations to meet the requirements of machine safety operating procedures.

<!-- image -->

<!-- image -->

ATTENTION: Motion is allowed when motion direct commands are used in Program mode and STO function is not available.

Motion direct commands issued when the controller is in Program mode causes the drive to bypass the STO Active condition.

It is your responsibility to implement additional preventive measures to maintain safety integrity of the machinery during execution of motion direct commands in Program mode.

ATTENTION: To avoid personal injury and damage to equipment if there is unauthorized access or unexpected motion during authorized access, return the controller to RUN mode and remove the key before leaving the machine unattended.

To maintain safety rating, Kinetix 5500 drives must be installed inside protected control panels or cabinets appropriate for the environmental conditions of the industrial location. The protection class of the panel or cabinet must be IP54 or higher.

Table 77 - Safe Torque Off Network Specifications

| Attribute                                                           | Value   | Logix Designer Tag Name   |
|---------------------------------------------------------------------|---------|---------------------------|
| Safety connection RPI, min                                          | 6 ms    | —                         |
| Input assembly connections                                          | 3       | —                         |
| Output assembly connections                                         | 1       | —                         |
| Integrated safety open request support Type 1 and Type 2 requests — |         |                           |

Table 77 - Safe Torque Off Network Specifications (Continued)

| Attribute          | Value  Logix Designer Tag Name                                 |
|--------------------|----------------------------------------------------------------|
| Axis safety status | Bit 0: Safety fault Axis.SafetyFaultStatus                     |
| Axis safety status | Bit 1: Safety reset request Axis.SafetyResetRequestStatus      |
| Axis safety status | Bit 2: Safety Reset Required  Axis.SafetyResetRequiredStatus   |
| Axis safety status | Bit 3: Safe Torque Off active Axis.SafeTorqueOffActiveStatus   |
| Axis safety status | Bit 4: Safe Torque Off disabled  Axis.SafeTorqueDisabledStatus |
| Axis safety status | Bit 5…31: Undefined (0) —                                      |
| Axis safety faults | Bit 1: Safety core fault Axis.SafetyCoreFault                  |
| Axis safety faults | Bit 3: Safe Torque Off fault Axis.SafeTorqueOffFault           |
| Axis safety faults | All others: Undefined (0) —                                    |

Table 78 - Safe Torque Off Assembly Specifications

|                        | Attribute Instance Attribute Value Logix Designer Tag Name   |                                                    |
|------------------------|--------------------------------------------------------------|----------------------------------------------------|
| Safety input assembly  | 0X1A0                                                        | Bit 0: Torque disabled Drv:SI.TorqueDisabled       |
| Safety input assembly  | 0X1A0                                                        | Bit 6: Safety fault Drv:SI.SafetyFault             |
| Safety input assembly  | 0X1A0                                                        | Bit 7: Reset required Drv:SI.ResetRequired         |
| Safety output assembly | 0X180                                                        | Bit 0: Safe Torque Off output Drv:SO.SafeTorqueOff |
| Safety output assembly | 0X180                                                        | Bit 7: Reset request Drv:SO.Reset                  |

## Interconnect Diagram Notes

Table 79 - Interconnect Diagram Notes

<!-- image -->

|    | Note Information                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | For power wiring specifications, refer to Wiring Requirements on page 78 .                                                                                                                                                                                                                                                                                                                                                                     |
|  2 | For input fuse and circuit breaker sizes, refer to Circuit Breaker/Fuse Selection on page 33 .                                                                                                                                                                                                                                                                                                                                                 |
|  3 | AC (EMC) line filter is required for EMC compliance. Place the line filter as close to the drive as possible and do not route dirty wires in the wireway. If routing in the wireway is unavoidable, use shielded cable with shields that are grounded to the drive chassis and filter case. For AC line filter specifications, refer to Kinetix 5700, 5500, 5300, and 5100 Servo Drives Specifications Technical Data, publication KNX-TD003 . |
|  4 | Terminal block is required to make connections.                                                                                                                                                                                                                                                                                                                                                                                                |
|  5 | Cable shield clamp must be used to meet CE and UK requirements.                                                                                                                                                                                                                                                                                                                                                                                |
|  6 | PE ground connection bonded to the panel must be used to meet CE and UK requirements.                                                                                                                                                                                                                                                                                                                                                          |
|  7 | DC connector that is covered with protective knockout is the default configuration. Remove the knockout to insert DC bus T-connector and busbars. Do not attach discrete wiring to the DC bus terminals is.                                                                                                                                                                                                                                    |
|  8 | Internal shunt wired to the RC connector is the default configuration. Remove internal shunt wires to attach external shunt wires.                                                                                                                                                                                                                                                                                                             |
|  9 | Default configuration for ground screws is for grounded power at user site. For ungrounded or corner-grounded power, remove the screws. See Determine the Input Power Configuration on page 71 for more information.                                                                                                                                                                                                                           |
| 10 | ATTENTION: Implementation of control circuits and risk assessment is the responsibility of the machine builder. Reference international standards IEC 62061 and ISO 13849-1 estimation and safety performance categories.                                                                                                                                                                                                                      |
| 11 | For motor cable specifications, refer to Kinetix Rotary and Linear Motion Cable Specification Technical Data, publication KNX-TD004 .                                                                                                                                                                                                                                                                                                          |
| 12 | Kinetix motor catalog numbers: MPL-A15xx…MPL-A45xx, MPM-A115xx…MPM-A130xx, MPF-A3xx…MPF-A45xx, MPS-Axxx, MPAR-Axxx, MPAS-Axxx, and LDAT-Sxx-xBx encoders use the +5V DC supply.                                                                                                                                                                                                                                                                |
| 13 | Kinetix motor catalog numbers: MPL-Bxx, MPL-A5xx, MPM-Bxx, MPM-A165xx…MPM-A215xx, MPF-Bxx, MPF-A5xx, MPS-Bxxx, MPAR-Bxxx, MPAS-Bxxx, and LDAT-Sxx-xDx encoders use the +9V DC supply.                                                                                                                                                                                                                                                          |
| 14 | Brake connector pins are labeled plus (+) and minus (-) or F and G respectively. Power connector pins are labeled U, V, W, and  (GND) or A, B, C, and (D) respectively.                                                                                                                                                                                                                                                                        |
| 15 | Kinetix LDAT linear thrusters do not have a brake option, so only the 2090-CPWM7DF-xxAAxx or 2090-CPWM7DF-xxAFxx motor power cables apply.                                                                                                                                                                                                                                                                                                     |

## Power Wiring Examples

You must supply input power components. The single-phase and three-phase line filters are wired downstream of the circuit protection.

## Interconnect Diagrams

This appendix provides wiring examples and system block diagrams for your Kinetix® 5500 system components.

| Topic                                                     |   Page |
|-----------------------------------------------------------|--------|
| Interconnect Diagram Notes                                |    179 |
| Power Wiring Examples                                     |    179 |
| Bus-sharing Wiring Examples                               |    182 |
| Shunt Resistor Wiring Example                             |    184 |
| Kinetix 5500 Servo Drive and Rotary Motor Wiring Examples |    185 |
| Kinetix 5500 Drive and Linear Actuator Wiring Examples    |    187 |
| System Block Diagrams                                     |    191 |

This appendix provides wiring examples to assist you in wiring the Kinetix 5500 drive system. These notes apply to the wiring examples on the pages that follow.

<!-- image -->

## Single-axis Drive Wiring Examples

## Figure 89 - Kinetix 5500 Drives Power Wiring (three-phase operation)

<!-- image -->

<!-- image -->

Circuit Protection *

Note 2

* Indicates User Supplied Component

## Bus-sharing Wiring Examples

For bus-sharing configurations, use the 2198-H0x0-xx-x shared-bus connection system to extend power from drive to drive.

Figure 92 - Kinetix 5500 Drives with Shared AC Bus

<!-- image -->

Figure 93 - Kinetix 5500 Drives with Shared AC/DC Bus

See table on page 179 for note information.

Bonded Cabinet Ground Bus *

Chassis

Note 4

Customer Supplied

+24V DC

Power Supply *

195…264V AC rms or

324…528V AC rms

Three-phase Input

Notes 1, 2

2198-Hxxx-ERSx

Kinetix 5500 Drive

PE Ground

Note 6

24V\_COM

+24V

L3

L2

L1

DC+

DC-

2198-Hxxx-ERSx

Kinetix 5500 Drive

PE Ground

Note 6

24V\_COM

+24V

L3

L2

L1

DC+

DC-

2198-DBxx-F

Three-phase

AC Line Filter

Note 3

2

1

4

3

2

1

2198-H0x0-ADP-IN

Busbar Connectors

2198-H0x0-ADP-T

Busbar Connectors

2198-Hxxx-ERSx

Kinetix 5500 Drive

PE Ground

Note 6

24V\_COM

+24V

L3

L2

L1

DC+

DC-

Control Power

(CP) Connectors

Three-phase Input

(IPD) Connectors

DC Bus

(DC) Connectors

2198-H0x0-ADP-T

Busbar Connectors

Note 4

See table on page 179 for note information.

Bonded Cabinet Ground Bus *

Chassis

Customer Supplied

+24V DC

Power Supply *

195…264V AC rms or

324…528V AC rms

Three-phase Input

Notes 1, 2

Circuit Protection *

Note 2

* Indicates User Supplied Component

Three-phase Input

(IPD) Connector

2198-H0x0-ADP-IN

Busbar Connectors

2198-H0x0-DP-T

Busbar Connectors

Figure 95 - Kinetix 5500 Drives with Shared AC/DC Hybrid Bus

2198-Hxxx-ERSx

Kinetix 5500 Drive

PE Ground

Note 6

24V\_COM

+24V

L3

L2

L1

DC+

DC-

Control Power

(CP) Connectors

DC Bus

(DC) Connectors

2198-H0x0-DP-T

Busbar Connectors

Figure 94 - Kinetix 5500 Drives with Shared DC (common bus)

<!-- image -->

2198-Hxxx-ERSx

Kinetix 5500 Drive

PE Ground

Note 6

24V\_COM

+24V

L3

L2

L1

DC+

DC-

2198-Hxxx-ERSx

Kinetix 5500 Drive

PE Ground

Note 6

24V\_COM

+24V

L3

L2

L1

DC+

DC-

2198-DBxx-F

Three-phase

AC Line Filter

Note 3

2

1

4

3

2

1

## Shunt Resistor Wiring Example

See the External Passive-shunt Resistor Connections on page 99 for the Bulletin 2097 external shunt resistor catalog numbers available for Kinetix 5500 servo drives.

## IMPORTANT

Before wiring the Bulletin 2097 external shunt to the RC connector, remove the wires from the servo drive internal shunt. Do not connect internal and external shunt resistors to the drive.

Figure 96 - Shunt Resistor Wiring Example

<!-- image -->

See the Kinetix 300 Shunt Resistor Installation Instructions, publication 2097-IN002, for shunt resistor installation instructions.

## Kinetix 5500 Servo Drive and Rotary Motor Wiring Examples

These compatible Kinetix VP rotary motors use single cable technology. The motor power, brake, and feedback wires are all packaged in a single cable.

Figure 97 - Kinetix 5500 Drives with Kinetix VPL, VPF, VPH, and VPS Motors

<!-- image -->

2090-CSxM1DF single cables have flying lead conductors that are designed specifically for Kinetix 5500 servo drives. 2090-CSxM1DG cables have flying leads that are longer than 2090CSxM1DF cables to accommodate Kinetix 5700 servo drives.

Figure 98 - Grounding Technique for Feedback Cable Shield

<!-- image -->

These compatible Kinetix MP rotary motors have separate connectors and cables for power/ brake and feedback connections.

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect either the 5V or the 9V supply, but not both. See Notes 12 and 13.

Figure 99 - Kinetix 5500 with Kinetix MP Rotary Motors

<!-- image -->

## Kinetix 5500 Drive and Linear Actuator Wiring Examples

These Kinetix VPAR linear actuators use single cable technology. The motor power, brake, and feedback wires are all packaged in a single cable.

Figure 100 - Kinetix 5500 Drives with Kinetix VPAR Electric Cylinders

<!-- image -->

2090-CSxM1DF single cables have flying lead conductors that are designed specifically for Kinetix 5500 servo drives. 2090-CSxM1DG cables have flying leads that are longer than 2090CSxM1DF cables to accommodate Kinetix 5700 servo drives.

See the cable-shield grounding technique for single cables on page 185 .

under clamp.

These compatible linear actuators have separate connectors and cables for power/brake and feedback connections.

Figure 101 - Kinetix 5500 with Kinetix LDAT Linear Thrusters

<!-- image -->

Figure 102 - Kinetix 5500 with Kinetix MPAS Linear Stages

<!-- image -->

Figure 103 - Kinetix 5500 with Kinetix MPAR and MPAI Electric Cylinders

<!-- image -->

Table 80 - Kinetix MPAR and MPAI Electric Cylinder Power and Feedback Cables

| Electric Cylinder Cat. No.       | Frame   | Power Cable Cat. No.                                                    | Feedback Cable Cat. No.                                                 |
|----------------------------------|---------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| MPAR-A/B1xxx (series A and B) 32 |         | 2090-XXNPMF-16Sxx (standard) or 2090-CPxM4DF-16AFxx (continuous-flex)   | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-A/B2xxx (series A and B) 40 |         | 2090-XXNPMF-16Sxx (standard) or 2090-CPxM4DF-16AFxx (continuous-flex)   | 2090-XXNFMF-Sxx (standard) or 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-A/B1xxx (series B and C) 32 |         | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-A/B2xxx (series B and C) 40 |         | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-A/B3xxx                     | 63      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B2xxxx                    | 64      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B3xxxx                    | 83      | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B4xxxx                    | 110     | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B5xxxx                      | 144     | 2090-CPxM7DF-16AAxx (standard) or 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A5xxxx                      | 144     | 2090-CPxM7DF-14AAxx (standard) or 2090-CPxM7DF-14AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) or 2090-CFBM7DF-CEAFxx (continuous-flex) |

## System Block Diagrams

This section provides block diagrams of the Kinetix 5500 drive modules.

Figure 104 - Kinetix 5500 Drive Block Diagram

<!-- image -->

Figure 105 - Kinetix 5500 Capacitor Module Block Diagram

<!-- image -->

## Before You Begin

## Update the Drive Firmware

This appendix provides procedures for updating your Kinetix® 5500 drive firmware.

| Topic                      |   Page |
|----------------------------|--------|
| Before You Begin           |    193 |
| Update Firmware            |    196 |
| Verify the Firmware Update |    199 |

You can update your Kinetix 5500 drive firmware by using ControlFLASH™ software.

To update the drive firmware, you must configure a path to your drive, select the drive module to update, and complete the firmware update procedure.

## IMPORTANT

If the drive firmware contains updated safety firmware, you must deenergize the safety inputs first or the update fails.

To update the drive firmware in Feedback Only mode, you must inhibit the axis first. See Inhibit Feedback Only Axis on page 195 for more information.

The following table shows the minimum firmware revisions and software versions that are required for updating drive firmware.

Table 81 - Kinetix 5500 System Requirements

| Description                             | Firmware Revision   |
|-----------------------------------------|---------------------|
| Studio 5000 Logix Designer® application | 21.00 or later      |
| RSLinx® software (1)                    | 3.60.00 or later    |
| ControlFLASH software kit (2)           | 12.01.00 or later   |

## IMPORTANT

Control power must be present at CP-1 (24V+) and CP-2 (24V-) before updating your target drive.

## IMPORTANT

## IMPORTANT

<!-- image -->

The axis state on the LCD display must be STANDBY, CONFIGURING, or PRECHARGE before beginning this procedure.

The axis state on the LCD display must be STANDBY, when Protected mode is enabled. See Table 57 on page 106 for more information.

ATTENTION: To avoid personal injury or damage to equipment during the firmware update due to unpredictable motor activity, do not apply threephase AC or common-bus DC input power to the drive.

## Configure Logix 5000 Controller Communication

This procedure assumes that your communication method to the Logix 5000® controller is the Ethernet network. It also assumes that your Logix 5000 Ethernet module or controller has already been configured.

<!-- image -->

For more controller information, see Additional Resources on page 12 .

Follow these steps to configure Logix 5000 controller communication.

1. Open your RSLinx® Classic software.
2. From the Communications menu, choose Configure Drivers.

The Configure Drivers dialog box appears.

<!-- image -->

3. From the Available Driver Types dropdown menu, choose Ethernet devices.
4. Click Add New.

The Add New RSLinx Classic Driver dialog box appears.

5. Type the new driver name.
6. Click OK.

<!-- image -->

The Configure driver dialog box appears.

<!-- image -->

7. Type the IP address of your Kinetix 5500 servo drive.
8. Click OK.

The new Ethernet driver appears under Configured Drivers.

<!-- image -->

9. Click Close.
10. Minimize the RSLinx application dialog box.

## Inhibit Feedback Only Axis

If an axis is configured as Feedback Only, you must inhibit the axis before performing the firmware update. Follow these steps to inhibit an axis.

1. Open your Logix Designer application.
2. Right-click the 2198-Hxxx-ERSx servo drive that you configured as Feedback Only and choose Properties.
3. The Module Properties dialog box appears.
3. Click the Connection tab.
4. Check Inhibit Module.
5. Click OK.
6. Save your file and download the program to the controller.

<!-- image -->

<!-- image -->

## Update Firmware

Follow these steps to select the drive module to update.

1. In the Logix Designer application, from the Tools menu, choose ControlFLASH.

<!-- image -->

You can also open the ControlFLASH software by choosing Start &gt; Programs &gt; FLASH Programming Tools &gt; ControlFLASH.

The Welcome to ControlFLASH dialog box appears.

<!-- image -->

## 2. Click Next.

The Catalog Number dialog box appears.

<!-- image -->

3. Select your drive module.

In this example, the 2198-H003-ERS servo drive is selected.

4. Click Next.

The Select Device to Update dialog box appears.

<!-- image -->

5. Expand your Ethernet node, Logix backplane, and EtherNet/IP™ network module.

6. Select the servo drive to update.
7. Click OK.

The Firmware Revision dialog box appears.

<!-- image -->

8. Select the firmware revision to update.
9. Click Next.

The Summary dialog box appears.

<!-- image -->

10. Confirm the drive catalog number and firmware revision.
11. Click Finish.

This ControlFLASH warning dialog box appears.

<!-- image -->

12. Click Yes (only if you are ready).

This ControlFLASH warning dialog box appears.

<!-- image -->

13. Acknowledge the warning and click OK.

The Progress dialog box appears and updating begins.

The axis state on the LCD display changes from CONFIGURING, STOPPED, or PRECHARGE

to FIRMWARE UPDATE, which indicates that the update is in progress.

After the update information is sent to the drive, the drive resets and performs diagnostic checking.Wait for the Progress dialog box to time out.

It is normal for this process to take several minutes.

## IMPORTANT

<!-- image -->

<!-- image -->

Do not cycle power to the drive during this process or the firmware update does not complete successfully.

14. Verify that the Update Status dialog box appears and indicates success or failure and take the appropriate action as described in the following table.

15. Click OK.

| Update Status Display   |                                                                   | Action                                                                                       |
|-------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Success                 | The Update complete message appears in a green Status dialog box. | Go to step 15 .                                                                              |
| Failure                 | The Update failure message appears in a red Status dialog box.    | See the ControlFLASH User Manual, publication 1756-UM105 ,  for troubleshooting information. |

<!-- image -->

## IMPORTANT

If you are updating a feedback-only axis and you checked Inhibit Module on the Connection tab in Module Properties, you must clear the Inhibit Module checkbox before resuming normal operation.

## Verify the Firmware Update

Follow these steps to verify that your firmware update was successful.

<!-- image -->

Verifying the firmware update is optional.

1. Open your RSLinx software.
2. From the Communications menu, choose RSWho.
3. Expand your Ethernet node, Logix backplane, and EtherNet/IP network module.
4. Right-click the drive module and choose Device Properties.

<!-- image -->

The Device Properties dialog box appears.

<!-- image -->

5. Verify the new firmware revision level.
6. Click Close.

## Notes:

## Shared-bus Configurations

<!-- image -->

## Size Multi-axis Shared-bus Configurations

This appendix provides information and examples for sizing your Kinetix® 5500 drive sharedbus configurations.

| Topic                              |   Page |
|------------------------------------|--------|
| Shared-bus Configurations          |    201 |
| Power-sharing Sizing Examples      |    206 |
| Control Power Current Calculations |    208 |
| Energy Calculations                |    209 |

Shared-bus configurations include the following types:

- Shared AC
- Shared DC (common bus)
- Shared AC/DC
- Shared AC/DC Hybrid

These restrictions apply to all shared-bus configurations:

- Shared-bus configurations must use the shared-bus connection system.
- Single-phase drive operation is not supported.
- Shared AC/DC and shared AC/DC hybrid configurations result in a derating of 30% of the total converter power available.
- The zero-stack tabs and cutouts must be engaged from drive-to-drive. Systems cannot start in one cabinet and end in another.
- Program drives for the same converter AC input voltage.

```
IMPORTANT Do not make drive-to-drive connections with discrete wires.
```

Shared AC configurations are configured as Standalone in the project file and do not share these restrictions that apply to multi-axis shared-bus configurations:

- All drives in a bus-sharing group must be configured with the same bus power-sharing group number in the Logix Designer application.
- The maximum number of drives in any bus power-sharing group cannot exceed eight.

## Shared AC Configurations

In shared AC configurations, the first (leftmost) drive receives AC input voltage. The sharedbus connection system extends the AC bus to all downstream drives:

- All drives are configured in the project file as Standalone drives.
- Drives must be of the same power rating (catalog number).
- Shared AC configurations do not support Bulletin 2198 capacitor modules.
- The maximum number of drives in Shared AC configurations is restricted as described in Table 82 .

Table 83 - Shared DC Panel Layout

| Frame Size Combination Leader Drive Cat. No.   |                | Follower Drives, Max (1)   | Follower Cat. No.    | Number of Capacitor Modules, Max   |
|------------------------------------------------|----------------|----------------------------|----------------------|------------------------------------|
|                                                | 2198-H003-ERSx |                            | 4 2198 - H003 - ERSx | 0                                  |
| 1                                              | 2198-H008-ERSx | 4                          | 2198-H003-ERSx       | 1                                  |
|                                                | 2198-H008-ERSx | 4                          | 2198-H008-ERSx       | 1                                  |
| 2 and 1                                        | 2198-H015-ERSx | 6                          | 2198-H003-ERSx       | 1                                  |
| 2 and 1                                        | 2198-H015-ERSx | 6                          | 2198-H008-ERSx       | 1                                  |
| 2                                              | 2198-H015-ERSx | 6                          | 2198-H015-ERSx       | 1                                  |
| 2 and 1                                        | 2198-H025-ERSx | 6                          | 2198-H003-ERSx       | 3                                  |
| 2 and 1                                        | 2198-H025-ERSx | 6                          | 2198-H008-ERSx       | 3                                  |
| 2                                              | 2198-H025-ERSx | 6                          | 2198-H015-ERSx       | 3                                  |
| 2                                              | 2198-H025-ERSx | 6                          | 2198-H025-ERSx       | 3                                  |
| 2 and 1                                        | 2198-H040-ERSx | 6                          | 2198-H003-ERSx       | 3                                  |
| 2 and 1                                        | 2198-H040-ERSx | 6                          | 2198-H008-ERSx       | 3                                  |
| 2                                              |                |                            | 2198-H015-ERSx       |                                    |
| 2                                              |                |                            | 2198-H025-ERSx       |                                    |
| 2                                              |                |                            | 2198-H040-ERSx       |                                    |

Table 82 - Shared AC Panel Layout

| Drive Cat. No. Frame Size   | Number of Drives Configured as Shared AC, Max   |
|-----------------------------|-------------------------------------------------|
| 2198-H003-ERSx              | 1 5                                             |
| 2198-H008-ERSx              | 1 5                                             |
| 2198-H015-ERSx              | 2 3                                             |
| 2198-H040-ERSx              | 2 3                                             |
| 2198-H070-ERSx              | 3 2                                             |

Figure 106 - Typical Shared AC Configuration

<!-- image -->

For an example shared AC installation with additional details, see Figure 2 on page 18 .

## Shared DC Configurations

In a Shared DC (DC common bus) configuration, the first (leftmost) drive is the leader drive and is the only drive that receives the AC input voltage. All drives to the right of the leader drives are follower drives. They receive the DC bus voltage extended from the leader drive through the shared-bus connection system:

- For DC common-bus installations, the power rating of the leader drive must be greater than or equal to the power rating of the follower drives.
- The leader drive is configured in the project file as Shared AC/DC.
- The follower drives are configured in the project file as Shared DC.
- Shared DC configurations support Bulletin 2198 capacitor modules.

Table 83 - Shared DC Panel Layout

| Frame Size Combination Leader Drive Cat. No.   |                |   Follower Drives, Max (1) | Follower Cat. No.   |   Number of Capacitor Modules, Max |
|------------------------------------------------|----------------|----------------------------|---------------------|------------------------------------|
| 3 and 1                                        | 2198-H070-ERSx |                          7 | 2198-H003-ERSx      |                                  4 |
| 3 and 1                                        | 2198-H070-ERSx |                          7 | 2198-H008-ERSx      |                                  4 |
| 3 and 1                                        | 2198-H070-ERSx |                          7 | 2198-H015-ERSx      |                                  4 |
| 3 and 1                                        | 2198-H070-ERSx |                          7 | 2198-H040-ERSx      |                                  4 |
| 3                                              | 2198-H070-ERSx |                          7 | 2198-H070-ERSx      |                                  4 |

Figure 107 - Typical DC Common Bus Configuration

<!-- image -->

## IMPORTANT

The total number of drives in a Kinetix 5500 drive system must not exceed eight.

For an example shared DC installation with additional details, see Figure 4 on page 20 .

## Shared AC/DC Configurations

In a shared AC/DC configuration, the first (leftmost) drive receives AC input voltage. The shared-bus connection system extends the AC and DC bus to all downstream drives:

- All drives are configured in the project file as Shared AC/DC drives.
- Drives must be of the same power rating (catalog number).
- Shared AC/DC configurations support Bulletin 2198 capacitor modules
- Total available converter power is derated by 30%.
- The maximum number of drives configured as Shared AC/DC is described in Table 84 .

## Table 84 - Shared AC/DC Panel Layout

| Drive Cat. No. Frame Size   | Drives Configured as Shared AC/DC, Max  (1)   | Number of Capacitor Modules, Max   |
|-----------------------------|-----------------------------------------------|------------------------------------|
| 2198-H003-ERSx              | 1 8                                           | 0                                  |
| 2198-H008-ERSx              | 1 8                                           | 1                                  |
| 2198-H015-ERSx              | 24 4                                          |                                    |
| 2198-H040-ERSx              | 24 4                                          |                                    |
| 2198-H070-ERSx              |                                               | 32 4                               |

Figure 108 - Typical Shared AC/DC Configuration

<!-- image -->

For an example shared AC/DC installation with additional details, see Figure 3 on page 19 .

## Shared AC/DC Hybrid Configurations

In shared AC/DC hybrid configurations, three-phase AC input power is supplied to two or more (leader) drives that act as converters. This parallel converter configuration increases the DC power that is supplied to the inverter (follower) drives:

- The leftmost drives in a hybrid configuration act as parallel converter drives and must be of the same power rating (catalog number).
- Shared DC (inverter) drives mounted to the right of the shared AC/DC (converter) drives must have the same or lower power rating (catalog number) than the shared AC/DC drives.
- The total motoring load must not exceed the rated load for the drives sourcing the DC power. Each follower drive must be sized for the motor load that is connected to it.
- Total available converter power is derated by 30%.
- The maximum number of drives configured in the project file as Shared AC/DC is restricted according to Table 84 on page 204 .
- The maximum number of drives configured in the project file as Shared DC is restricted according to Table 83 on page 202 .
- Shared AC/DC hybrid configurations support Bulletin 2198 capacitor modules.
- (1) For Bulletin 2198 capacitor module maximum values, refer to the Kinetix 5500 Capacitor Module Installation Instructions, publication 2198-IN004 .

Figure 109 - Typical Shared AC/DC Hybrid Configuration

<!-- image -->

For an example shared AC/DC hybrid installation with additional details, see Figure 5 on page 21 .

## Power-sharing Sizing Examples

For best results, size motors based on load torque requirements by using Motion Analyzer Online. Select drives based on continuous or peak torque requirements. Based on the load profile, use Motion Analyzer Online to estimate the net converter and inverter power and bus regulator capacity.

Table 85 - Converter and Bus Regulator Capacity

| Configuration Available Converter Capacity                                                                                         | Available Regenerative Capacity                                 |
|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Shared AC Converter power rating of each drive Internal shunt of each drive                                                        |                                                                 |
| Common bus Converter power rating of leader drive Shared AC/DC  Sum of converter power ratings times 0.7 (70%) Shared AC/DC hybrid | Sum of all internal shunts from each drive in bus-sharing group |

## Shared DC Example

In this example, four 2198-H040-ERS drives are used in a common-bus configuration.

<!-- image -->

Each 2198-H040-ERS drive is rated at 8.4 kW continuous output power to the bus. However, only the leader drive acts as the converter, so the available converter power to the system is 8.4 kW. In this example, total motoring load must not exceed 8.4 kW.

## Shared AC/DC Hybrid Example

If the required motoring power exceeds the available converter power that is sourced by the shared DC configuration, then connect a second converter drive to make a shared AC/DC hybrid configuration. This increases the available converter power.

In this example, the same four 2198-H040-ERS drives are used, however, two are connected as parallel converter (leader) drives and the other two as common-bus (follower) drives. The total converter power is derated by 30%.

Figure 111 - Shared AC/DC Hybrid Configuration

<!-- image -->

The available converter power to the system is (8.4 · 2) · 0.7 = 11.76 kW. In this example, the total motoring load must not exceed 11.76 kW. The available converter power was increased by 40% over the same drives in shared DC configuration.

## Control Power Current Calculations

## Shared AC/DC Example

If the required motoring power exceeds the available converter power that is sourced by two leader drives, then connect all four drives as parallel converter drives. This further increases the available converter power.

In this example, the same four 2198-H040-ERS drives are used, however, all four are connected as parallel converter (leader) drives. The total converter power is derated by 30%.

<!-- image -->

The available converter power to the system is (8.4 · 4) · 0.7 = 23.52 kW. In this example, total motoring load must not exceed 23.52 kW. The available converter power was increased by 180% over the same drives in shared DC configuration.

Kinetix 5500 servo drives and the Bulletin 2198 capacitor module have different 24V DC power consumption. Factors to consider when calculating the combined current demand from your 24V DC power supply includes the following:

- The catalog number for each drive in the system
- Whether the motor or actuator includes the holding brake option
- Whether the system includes Bulletin 2198 capacitor modules (1...4 modules are possible)

## Table 86 - Control Power Current Demand

| Cat. No.                                     | 24V Current (non-brake motor) A DC   | 24V Current (2 A brake motor) A DC   | 24V Inrush Current (1) A   |
|----------------------------------------------|--------------------------------------|--------------------------------------|----------------------------|
| 2198-H003-ERSx  2198-H008-ERSx               |                                      | 0.4 2.4 2.0                          |                            |
| 2198-H015-ERSx 2198-H025-ERSx 2198-H040-ERSx | 0.8                                  | 2.8                                  | 3.0                        |
| 2198-H070-ERSx                               | 1.3                                  | 3.3                                  | 2.0                        |
| 2198-CAPMOD-1300 0.3                         |                                      | —                                    |                            |

(1) Inrush current duration is less than 30 ms.

## Energy Calculations

Table 88 - Energy Absorbing Potential

| Kinetix 5500 Drive Cat. No.   |   Internal Shunt (1) J |   External Shunt kJ | Capacitor Module  (1) J   | Capacitor Module, Max  (2) J   |
|-------------------------------|------------------------|---------------------|---------------------------|--------------------------------|
| 2198-H003-ERSx                |                427.09  |              12.51  |                           | — —                            |
| 2198-H008-ERSx                |                427.09  |              12.51  | 554.4                     | 554.4                          |
| 2198-H015-ERSx                |                549.01  |              12.521 | 676.32                    | 676.32                         |
| 2198-H025-ERSx                |                575.223 |              12.549 | 702.53                    | 957.162                        |
| 2198-H040-ERSx                |                601.434 |              22.647 | 728.74                    | 983.373                        |
| 2198-H070-ERSx                |               1827.01  |              27.218 | 1954.3                    | 2208.95                        |

See Motion Analyzer Online, version 7.0 or later, for custom shunt sizing.

## Kinetix 5500 System Current Demand Example

In this example, the Kinetix 5500 drive system includes two 2198-H040-ERS drives, four 2198H008-ERS drives, and one capacitor module.

Figure 113 - Shared AC/DC Hybrid Configuration

<!-- image -->

Table 87 - Kinetix 5500 System Current Demand Calculations

| Kinetix 5500 Module Cat. No.  Qty   | 24V Current (non-brake motors) A DC     | 24V Current (2 A brake motors) A DC     | 24V Inrush Current (1) A   |
|-------------------------------------|-----------------------------------------|-----------------------------------------|----------------------------|
| 2198-H008-ERSx                      |                                         | 4 0.4 x 4 = 1.6 2.4 x 4 = 9.6 2 x 4 = 8 |                            |
| 2198-H040-ERSx                      | 2 0.8 x 2 = 1.6 2.8 x 2 = 5.6 3 x 2 = 6 |                                         |                            |
| 2198-CAPMOD-1300 1 0.3 x 1 = 0.3 —  |                                         |                                         | 2 x 1 = 2                  |
| Total current demand                | 3.5                                     | 15.2                                    | 16                         |

The Kinetix 5500 servo drives have internal shunt resistors for dissipating excessive energy. In addition, Bulletin 2097 external shunt resistors and Bulletin 2198 capacitor modules are available to increase the shared DC bus capacitance.

Use this table to calculate the total energy absorbing potential (joules) and determine if a capacitor module or external shunt resistor is needed.

## Notes:

## Motor Control Feature Support

This appendix provides feature descriptions for the induction motors and permanent-magnet motors that are supported by Kinetix® 5500 servo drives.

| Topic                                   |   Page |
|-----------------------------------------|--------|
| Frequency Control Methods               |    212 |
| Current Limiting for Frequency Control  |    216 |
| Stability Control for Frequency Control |    219 |
| Skip Speeds                             |    221 |
| Flux Up                                 |    223 |
| Current Regulator Loop Settings         |    225 |
| Motor Category                          |    226 |
| Selection of Motor Thermal Models       |    231 |
| Speed Limited Adjustable Torque (SLAT)  |    232 |
| Motor Overload Retention                |    238 |
| Phase Loss Detection                    |    239 |
| Velocity Droop                          |    241 |
| Commutation Test                        |    243 |
| Adaptive Tuning                         |    243 |

<!-- image -->

## Frequency Control Methods

The Kinetix 5500 servo drives support three open-loop frequency control methods. The choices are the following:

- Basic Volts/Hertz - This method is used in single asynchronous-motor applications
- Basic Volts/Hertz - Fan Pump - This method is similar to Basic Volts/Hertz, but is tailored for fan/pump applications
- Sensorless Vector with Slip Compensation - This method is used for most constant torque applications. Provides excellent starting, acceleration, and running torque

To configure your induction motor in the Logix Designer application, refer to Configure Induction-motor Frequency-control Axis Properties on page 122 .

Open-loop frequency control is suitable in applications such as conveyors, pumps, and fans. Features include the following:

- Start Boost and Run Boost
- Electronic motor thermal-overload protection per Class 10 requirements
- Two skip frequencies, in which the drive does not operate
- All three-phase induction motors, suitable for variable speed drive (VFD) operation, are supported

Table 89 - Motor Specifications

| Attribute               | Value             |
|-------------------------|-------------------|
| Output frequency, max   | 590 Hz            |
| Pole pairs, max         | 50                |
| Motor cable length, max | 50 m (164 ft) (1) |

## Basic Volts/Hertz

Volts/hertz operation creates a fixed relationship between output voltage and output frequency. Voltage is applied to the motor, which is based on the operating frequency command at a fixed volts/hertz ratio. The ratio is calculated from the motor nameplate data and entered into the Logix Designer application &gt; Axis Properties &gt; Frequency Control category.

The Basic Volts/Hertz method provides various patterns. The default configuration is a straight line from zero to rated voltage and frequency. As seen in Figure 114, you can change the volts/hertz ratio to provide increased torque performance when required by programming five distinct points on the curve.

Table 90 - Basic Volts/Hertz Definitions

| Curve Feature                      | Definition                                                                                                                                                                                                                                                                                                                      |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start boost                        | Used to create additional torque for breakaway from zero speed and acceleration of heavy loads at lower speeds.                                                                                                                                                                                                                 |
| Run boost                          | Used to create additional running torque at low speeds. The value is typically less than the required acceleration torque. The drive lowers the boost voltage to this level when running at low speeds (not accelerating). This reduces excess motor heating that could result if the higher start/accel boost level were used. |
| Break voltage/frequency            | Used to increase the slope of the lower portion of the Volts/Hertz curve, providing additional torque.                                                                                                                                                                                                                          |
| Motor nameplate voltage/ frequency | Sets the upper portion of the curve to match the motor design. Marks the beginning of the constant power region.                                                                                                                                                                                                                |
|                                    | Maximum voltage/frequency Slopes the portion of the curve that is used above base speed.                                                                                                                                                                                                                                        |

## Figure 114 - Basic Volts/Hertz Method

<!-- image -->

## Basic Volts/Hertz for Fan/Pump Applications

The Basic Volts/Hertz Fan/Pump (fan/pump) method is based on the Basic Volts/Hertz (VHz) method, but is tailored for fan/pump applications.

## Figure 115 - Output Voltage Equation

$$V 2 x = f x f n V n – V boost + Vboost$$

Where:

V x = Output voltage

f x = Output frequency

V n = Rated voltage

F n = Rated frequency

V boost = Run boost voltage

For maximum system efficiency, fan/pump loads use variable-frequency drives that are equipped with a specific VHz curve where the voltage is proportional to the square of the frequency.

Figure 116 - Basic Volts/Hertz Fan/Pump Method

<!-- image -->

<!-- image -->

The Fan/Pump control method supports the run-boost attribute, but does not support break-voltage, break-frequency, or start-boost.

## Sensorless Vector

The Sensorless Vector method uses a volts/hertz core that is enhanced by a current resolver, slip estimator, and a voltage-boost compensator based on the operating conditions of the motor.

<!-- image -->

The algorithms operate on the knowledge of the relationship between the rated slip and torque of the motor. The drive uses applied voltages and measured currents to estimate operating slip-frequency. You can enter values to identify the motor resistance value or you can run a motor test to identify the motor resistance value (see Motor Tests and Autotune Procedure on page 228). Motor nameplate data and test results are ways to accurately estimate the required boost voltage.

The sensorless vector method offers better torque production and speed regulation over a wider speed range than basic volts/hertz.

Dynamic boost is applied internally to compensate voltage drop and improve starting torque.

<!-- image -->

## Current Limiting for Frequency Control

The current limiting module prevents the OutputCurrent value from exceeding the OperativeCurrentLimit value when the drive is configured in Frequency Control mode.

<!-- image -->

In Frequency Control mode, OperativeCurrentLimit is the minimum value of the motor-thermal current limit, inverter-thermal current limit, motor-peak current limit, drive-peak current limit, and the CurrentVectorLimit value.

## The Effects of Current Limiting

Indirect current limiting is available for induction motors that are configured for frequency control. You can use this feature to help prevent overcurrent faults due to aggressive acceleration/deceleration profiles or impact loads. The Current Limiting attribute uses a PI regulator to control the OutputCurrent by adjusting the velocity reference.

## IMPORTANT

When configured for Frequency Control (induction motors only), select the Decel and disable stopping action only when the Current Limiting feature is enabled.

Figure 120 - Effects of Current Limiting on an Aggressive Acceleration

Aggressive Acceleration, No Current Limiting

<!-- image -->

<!-- image -->

<!-- image -->

Current limiting for frequency control is not enabled by default. You can enable via messaging by using the following device-specific attributes.

<!-- image -->

We recommend you leave the Kp, Ki, Kd gains at the default values.

Table 91 - Enable Current Limiting via Messaging

| Attribute Offset   | Type Attribute Name           | Conditional Implementation             | Description                                                                                                                                                                                                                                                                                           |
|--------------------|-------------------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3022 SINT          | Current Limiting Enable       | Frequency Control Induction Motor only | When enabled, limits the rate of change to the velocity reference during high-current situations for improved current limiting. This feature is only active when executing an MDS command and when configured for Frequency Control. 0 = Current Limiting is disabled 1 = Current Limiting is enabled |
|                    | 3023 REAL Current Limiting Kd | Frequency Control Induction Motor only | Derivative gain for the current limiting function. Only functional when configured for Frequency Control and when executing an MDS command. Units of seconds.                                                                                                                                         |
|                    | 3024 REAL Current Limiting Ki | Frequency Control Induction Motor only | Integral gain for the current limiting function. Only functional when configured for Frequency Control and when executing an MDS command. Units of feedback counts / (Amp, inst. Seconds).                                                                                                            |
|                    | 3025 REAL Current Limiting Kp | Frequency Control Induction Motor only | Proportional gain for the current limiting function. Only functional when configured for Frequency Control and when executing an MDS command. Units of feedback counts / Amp, inst.                                                                                                                   |

IMPORTANT

For induction motors greater than 5 Hp, we recommend that you enable the Stability Control feature when Current Limiting is enabled.

## Enable the Current Limiting Feature

In this example, a Message Configuration (MSG) instruction is configured to enable the CurrentLimitingEnable attribute for axis 1. The Instance field is used to direct the message to the proper axis.

<!-- image -->

## Set the CurrentVectorLimit Attribute Value

For current limiting, the CurrentVectorLimit attribute is used to help determine the OperativeCurrentLimit of the drive. Set the CurrentVectorLimit value to artificially lower OperativeCurrentLimit below the drive or motor peak current limits.

1. Select the Parameter List category and scroll to CurrentVectorLimit.
2. Set the CurrentVectorLimit value appropriate for your application.

| CoastingTimeLimit   | 0.0 S                                |
|---------------------|--------------------------------------|
| ConversionConstant  | 1000000.0 MotionCounts/PositionUnits |
| CurrentVectorLimit  | 100.0 %MotorRated                    |
| FluxUpControl       | NoDelay                              |
| FluxUpTime          | 0.0s                                 |

## IMPORTANT

The CurrentVectorLimit attribute appears in the Parameter List of the Logix Designer application, version 29.00 and later. If you are using a previous version, the CurrentVectorLimit attribute must be set via a Message Configuration (MSG) instruction.

## Stability Control for Frequency Control

Table 92 - Enable Current Limiting via Messaging

| Attribute Offset   | Type Attribute Name            | Conditional Implementation             | Description                                                                                                                                                                                              |
|--------------------|--------------------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3026 SINT          | Stability Control Enable       | Frequency Control Induction Motor only | Enables stability control when configured for frequency control. 0 = Stability Control is disabled 1 = Stability Control is enabled                                                                      |
| 3027 REAL          | Stability Filter Bandwidth     | Frequency Control Induction Motor only | Sets the bandwidth of the low-pass filter that is applied to the current feedback signal. This bandwidth is common to both the angle and voltage stability control algorithms. Units of radians/ second. |
| 3028 REAL          | Stability Voltage Gain         | Frequency Control Induction Motor only | The gain of the voltage stability control function. Only active when configured for frequency control. Units of Volt (inst, p-n)/Amp (inst).                                                             |
|                    | 3029 REAL Stability Angle Gain | Frequency Control Induction Motor only | The gain of the electrical angle stability control function. Only active when configured for frequency control. Units of radians/Amp (inst).                                                             |

## IMPORTANT

Because the stability control feature works by manipulating the OutputVoltage and OutputFrequency signals, these signals may appear 'noisy' when the feature is enabled.

Stability control is available for induction motors that are configured for frequency control. This feature can be used to help remove resonances that are sometimes seen on larger motors. The stability control feature adjusts the OutputFrequency and OutputVoltage commands to stabilize the OutputCurrent.

Figure 122 - Effects of Stability Control

<!-- image -->

Id Feedback, Iq Feedback versus Commanded Speed with Stability Control Enabled

<!-- image -->

Stability control for frequency control is not enabled by default. You can enable via messaging by using the following device-specific attributes.

<!-- image -->

We recommend you leave the angle, voltage gains, and filter bandwidth at the default values.

## Enable the Stability Control Feature

In this example, a Message Configuration (MSG) instruction is configured to enable the StabilityControl attribute for axis 1. The Instance field is used to direct the message to the proper axis.

<!-- image -->

## Skip Speeds

Some machines have a resonant operating frequency (vibration speed) that is undesirable or could cause equipment damage. To guard against continuous operation at one or more resonant points, you can configure the skip-speed attributes in the Logix Designer application &gt; Axis Properties &gt; Parameter List category.

The value that is programmed into the SkipSpeed1 or SkipSpeed2 attribute sets the central speed of a skip-speed band within which the drive does not operate. The width of the band is determined by the SkipSpeedBand attribute. The range is split, half above and half below the SkipSpeedx attribute. Any command setpoint within this band is adjusted by the skip-speed feature to fall at either the upper or lower skip-speed band boundary value. The skip-speed feature contains hysteresis (25% of the SkipSpeedBand value) to prevent frequent switching of VelocityReference.

Figure 123 - Single Skip Speed Example

<!-- image -->

A SkipSpeedBand value of 0 disables the skip-speed feature.

| IMPORTANT   | If you want there to be only one SkipSpeed value, the SkipSpeed1 and SkipSpeed2 settings must be the same.                                         |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Acceleration and deceleration are affected by the skip-speed feature. Too large of a SkipSpeedBand value can result in an overcurrent drive fault. |
| IMPORTANT   | The MaximumFrequency attribute is always enforced. Skip-speed band boundary values beyond the MaximumFrequency value do not apply.                 |

## Multiple Skip Speeds

The Kinetix 5500 drives feature two independent skip-speed attributes (SkipSpeed1 and SkipSpeed2) that use the same SkipSpeedBand.

Figure 124 - Multiple Skip Speed Example

<!-- image -->

When the skip-speed band boundaries of SkipSpeed1 and SkipSpeed2 overlap, the skip-speed hysteresis is calculated using the effective skip band.

In Figure 125, SkipSpeed1 is set to 0 and SkipSpeed2 is set to 15 Hz. The skip band is 10 Hz wide.

At point A, the axis is enabled, and the motor begins to rotate at -5 Hz even though the command is 0 Hz. As the command reaches hysteresis point the output frequency begins to follow the command. During deceleration, when the command decreases to 0 Hz, the output frequency continues at 5 Hz until the axis is disabled (point B), or the command is changed outside of the skip band.

Figure 125 - Zero-speed Skip Frequency

<!-- image -->

## Flux Up

AC induction motors require that flux builds in the motor stator before controlled torque can develop. To build flux, voltage is applied. There are two methods to flux the motor and three configurable FluxUpControl settings.

With the No Delay setting (normal start), flux is established when the output voltage and frequency are applied to the motor. While flux is building, the unpredictable nature of the developed torque can cause the rotor to oscillate even though acceleration of the load can occur. In the motor, the acceleration profile does not follow the commanded acceleration profile due to the lack of developed torque.

Figure 126 - Acceleration Profile during Normal Start - No Flux Up

<!-- image -->

With the Automatic setting (default), DC current is applied to the motor so that flux builds before rotation. The flux-up time period is based on the level of flux-up current and the rotor time constant of the motor. The flux-up current is not adjustable.

In the Manual setting, DC current is applied to the motor so that flux builds before rotation. The flux-up time period is determined by the FluxUpTime attribute. The flux-up current is not adjustable.

Figure 127 - Flux Up Current Versus Flux Up Time

<!-- image -->

Once rated flux is reached in the motor, normal operation can begin and the desired acceleration profile achieved.

<!-- image -->

## Flux Up Attributes

| ID Access Attribute       | Conditional Implementation                                              |
|---------------------------|-------------------------------------------------------------------------|
| 558 Set Flux Up Control   | Ind Motor only 0 = No Delay 1 = Manual Delay 2 = Automatic Delay        |
| 559 Set  Flux Up Time (1) | Ind Motor only Units: Seconds Default: 0.0000 Min/Max: 0.0000 / 1000.00 |

## FluxUpControl Attribute

When the motion axis is enabled, DC current is applied to an induction motor to build stator flux before transitioning to the Running state. This attribute controls how an induction motor is to be fluxed in the Starting state before transitioning to the Running state.

Table 93 - FluxUp Control Delay Methods

| Delay Method Description   |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                            | No delay The axis transitions immediately to the Running state while the motor flux is building.                                        |
| Manual delay               | The axis remains in the Starting state while the motor stator flux is building according to the Flux Up Time attribute.                 |
| Automatic delay            | The drive determines the amount of delay time to fully flux the motor, based on the motor configuration attribute data or measurements. |

## FluxUpTime Attribute

When FluxUpControl is configured for Manual Delay, this attribute sets the length of delay time to fully flux the motor before transitioning to the Running state.

## Current Regulator Loop Settings

## Configure the Flux Up Attributes

Follow these steps to configure the flux-up attributes.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the Parameter List category and scroll to FluxUpControl.
3. From the FluxUpControl dropdown menu, choose the proper delay value appropriate for your application.
4. If you chose Manual Delay in step 3, enter a value in the FluxUpTime attribute appropriate for your application.

<!-- image -->

<!-- image -->

If you chose No Delay or Automatic Delay in step 3, the FluxUpTime attribute does not apply.

Current loop bandwidth is set differently based on the selected motor type.

Table 94 - Current Regulator Loop Settings

<!-- image -->

| Motor Type                       |   Default Torque/Current Loop Bandwidth Hz |
|----------------------------------|--------------------------------------------|
| Rotary permanent magnet          |                                       1000 |
| Rotary interior permanent magnet |                                       1000 |
| Linear permanent magnet          |                                       1000 |

## IMPORTANT

The Logix Designer application does not perform calculations when the Torque/Current Loop Bandwidth attribute is updated. This bandwidth affects many other gains and limits. Changing (lowering) the torque loop bandwidth without updating all dependent attributes can result in drive/motor instability.

## Motor Category

From the Motor category, you can enter motor nameplate or datasheet values (phase-to-phase parameters) for rotary induction motors.

In this example, the Motor category &gt; Nameplate / Datasheet parameters, were taken from a typical motor performance datasheet. Max Speed and Peak Current values are typically application-dependent.

Figure 129 - Motor Nameplate / Datasheet Example

<!-- image -->

See Figure 130 for an example of a motor manufacturer performance data sheet.

Figure 130 - Motor Manufacturer Performance Data Sheet Example

C E R T I FI C AT I ON DAT A SHE E T

T Y PI C AL MOT OR PE R FOR MANC E DAT A

<!-- image -->

PH H z V OL TS FL AMPS STAR T TY PE

30/ 460

DUTY INSL S.F. AMB°C EL EV ATION

3 60 230/ 3/ 1.5 460

INV E R TE R ONL Y C ONTINUOUS F 3 1.0 40

F UL L L O AD E F F : 84 3/4 L O AD E F F : 82.5 1/2 L O AD E F F : 78.5

3300

G TD. EFF ELEC. TY PE NO LOAD AMPS

F UL L L O AD PF : 75 3/4 L O AD PF : 65.5 1/2 L O AD PF : 51 81.5 S Q C AGE INV DUTY 2 / 1

| F.L. TOR QUE   | LOCK ED R OTOR AMPS   | L.R . TOR QUE      | B.D. TOR QUE F.L . R ISE°C   |    |
|----------------|-----------------------|--------------------|------------------------------|----|
| 3 L B -F T     | 30 / 15               | 10.8 L B -F T 360% | 15 L B -F T 500%             | 65 |

| SOUND PR ESSUR E @ 3 F T .   |                                        | SO UND PO W E R R O T O R W K ^2 MA X . W K ^2 SA F E ST A L L T I ME   | STAR TS / HOUR   | APPROX. MOTOR WGT   |
|------------------------------|----------------------------------------|-------------------------------------------------------------------------|------------------|---------------------|
| 62 dB A                      | 72 dB A 0.11 L B -F T ^2 0 L B -F T ^2 | 0 S E C .                                                               |                  | 0 42 L B S .        |

## E QUI V AL E NT W Y E C K T .PAR AME T E R S (OHMS PE R PHASE )

|   R 1 |    R 2 |     X 1 |    X 2 |     X M |
|-------|--------|---------|--------|---------|
| 8.378 | 5.6232 | 10.7068 | 9.9116 | 278.036 |

|     R M |   ZR EF |   X R |    T D |   TD0 |
|---------|---------|-------|--------|-------|
| 11132.8 |     284 |   1.7 | 0.0071 | 0.136 |

## Motor &gt; Model Category

From the Motor &gt; Model category, you can enter additional motor nameplate or datasheet values (phase-to-neutral parameters) for induction motors.

The Motor &gt; Model parameters are used in closed-loop induction-motor control mode, sensorless vector control mode, and when FluxUp is enabled. The Logix Designer application automatically estimates the Motor &gt; Model parameters based on the motor nameplate data. You can also enter these parameter values directly from the motor nameplate/datasheet or indirectly by running a Motor &gt; Analyzer test.

Figure 131 - Phase-to-Neutral Parameters

<!-- image -->

IMPORTANT

If you do not know the Stator Leakage, Rotor Leakage, Stator Resistance, Rated Flux Current, and system inertia, you can run the static motor test and Autotune procedure to determine the parameter values.

## Motor &gt; Analyzer Category

From the Motor &gt; Analyzer category, you can perform three types of tests to identify motor parameters.

In this example, the Calculate Model test was run. If the Motor &gt; Analyzer test executes successfully, and you accept the test values, they populate the Model Parameter attributes.

Figure 132 - Motor Analyzer Category

<!-- image -->

Table 95 - Motor Tests and Autotune Matrix

| Control Mode                        | Description Calculate Static                                          |              | Dynamic Autotune (inertia test)                     |
|-------------------------------------|-----------------------------------------------------------------------|--------------|-----------------------------------------------------|
| Induction motor - Frequency control | Basic volts/hertz Not required Not required Not required Not required |              |                                                     |
| Induction motor - Frequency control | Basic volts/hertz for Fan/Pump                                        |              | Not required Not required Not required Not required |
| Induction motor - Frequency control | Sensorless vector                                                     | Required (1) | Preferred Not required Not required                 |

For motor/system autotune procedure, see Tune Induction Motors on page 140 for more information.

The Motor &gt; Analyzer category offers three choices for calculating or measuring electrical motor data.

Follow these steps to run motor tests and identify motor parameters.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the Motor &gt; Analyzer category.

Nameplate data was entered on page 226. The nameplate data must be entered before running the Calculate test.

<!-- image -->

3. To run the test, click Start.
4. To save the values, click Accept Test Results.
5. Click OK.

## Motor Tests and Autotune Procedure

You can perform three types of tests to identify motor parameters and one test for motor/ system inertia. These parameters are used by sensorless-vector frequency-control and induction motor closed-loop modes. Table 95 recommends which test to use based on the control mode and application.

## Motor Analyzer Category Troubleshooting

## Calculate Model

When a Calculate test is run, the drive uses motor nameplate data to estimate the motor's Rated Flux Current, Stator Resistance (Rs), Stator Leakage Reactance (X1), and Rotor Leakage Reactance (X2). The drive also calculates the rated slip speed, based on rated speed and rated frequency. No measurements are taken when using the Calculate test.

## Static Motor Test

Use the Static test if the motor shaft cannot rotate or if it is already coupled to the load. Only tests that do not create motor movement are run. During this test, the Stator Resistance (Rs), Stator Leakage Reactance (X1), and Rotor Leakage Reactance (X2) values are measured during a series of static tests. The Rated Flux Current is estimated, since measurement of this value requires motor movement. The drive also calculates the rated slip speed, based on rated speed and rated frequency.

The Static test requires that you enter initial estimates for Rated Flux Current, Rated Slip Speed, Stator Resistance (Rs), Stator Leakage Reactance (X1), and Rotor Leakage Reactance (X2) into the Motor Model fields. The method of entering initial estimates depends on the version of the Logix Designer application:

- For the Logix Designer application, version 29.00 or later, initial estimates are populated by the controller.
- For the Logix Designer application, version 28.00 or earlier, initial estimates can be entered by running and accepting the results of a Calculate test, or by entering the values directly into the Logix Designer application.

## Dynamic Motor Test

Dynamic tests are run with the motor disconnected from the load because the motor shaft turns and there are no travel limits. This is often the most accurate test method. During this test, the Stator Resistance (Rs), Stator Leakage Reactance (X1), and Rotor Leakage Reactance (X2) values are measured in a series of static tests. The Rated Flux Current is measured during a rotational test, in which the drive commands 75% of the motor rated speed.

The rated slip speed is measured during a second rotational test. In this test, the drive commands a speed (default of 100% of the motor rated speed) and sets a torque limit (default of 50% of the motor rated torque). This test quickly accelerates the motor to rated speed and then decelerates back to zero speed.

## IMPORTANT

The Dynamic test does not support travel limits.

The Dynamic test also requires that you enter initial estimates for Rated Flux Current, Rated Slip Speed, Stator Resistance (Rs), Stator Leakage Reactance (X1), and Rotor Leakage Reactance (X2) into the Motor Model fields. The method of entering initial estimates depends on the version of the Logix Designer application:

- For the Logix Designer application, version 29.00 or later, initial estimates are automatically populated by the controller.
- For the Logix Designer application, version 28.00 or earlier, initial estimates can be entered by running and accepting the results of a Calculate test, or by entering the values directly into the Logix Designer application.

The Dynamic test uses the Ramp Acceleration and Ramp Deceleration attributes to set the rotational test ramp-up and ramp-down times. If the resulting acceleration/deceleration times are less than 10 seconds, 10 seconds is used. If these attributes are not supported, 10 seconds is also used.

Table 96 - Slip Test via Messaging

| Attribute Offset   | Type Attribute Name                     | Conditional Implementation       | Description                                                                                                                                                                        |
|--------------------|-----------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                    | 3095 REAL IM Slip Test Torque Limit     | Closed loop induction motor only | Sets positive and negative torque limits for the slip test within the Dynamic motor test (similar to the torque limits in the inertia test). Units are in percent of rated torque. |
|                    | 3096 REAL IM Slip Test Velocity Command | Closed loop induction motor only | Sets the velocity command for the slip test within the Dynamic motor test (similar to the velocity command in the inertia test). Units are in percent of motor rated speed.        |

The Dynamic test requires that the Positive and Negative Torque Limits for the axis are not over-written while the test is in progress. This requirement can be satisfied by making sure that (1) these cyclic attributes are not checked as writable within the Drive Parameters tab of the axis properties and (2) these parameters are not being messaged via an MSG instruction.

When configured for closed-loop control, the Dynamic test requires that an accurate system inertia is set in the Logix Designer application.

- For the Logix Designer application, version 29.00 or later, a default value is automatically populated by the controller.
- For the Logix Designer application, version 28.00 or earlier, the system inertia can be set by running and accepting the results of an Autotune test, or by entering the motor inertia value directly into the Logix Designer application.

When configured for closed-loop control, the Dynamic test uses the velocity regulator tuning as entered into the Logix Designer application. If the motor is coupled to a load, the velocity regulator tuning may need to be adjusted to make sure that the velocity response is well controlled. The Dynamic test fails if the steady-state velocity feedback is not within a ±30% tolerance of the commanded velocity.

## IMPORTANT The Dynamic test is not supported in closed-loop Torque Control.

If using the Dynamic test in Frequency Control mode, uncouple the motor from any load or results may not be valid. In closed-loop control, either a coupled or uncoupled load produces valid results.

The Dynamic test also uses the IM Slip Test Velocity Command (percent of rated speed) and IM Slip Test Torque Limit (percent of rated torque) attributes to define the motion profile for the slip measurement. The default values are 100.0 and 50.0 respectively. The speed command dictates the speed that the motor spins up to and the torque dictates how quickly the motor reaches that speed. In general, A higher speed and lower torque results in a longer acceleration and a more accurate rated slip speed. However, the dynamic test does not return expected results if the torque limit is set below 30.0.

## Selection of Motor Thermal Models

The Kinetix 5500 drives contain two motor thermal-overload protection algorithms that you can use to help prevent the motor from overheating.

## Generic Motors

The default thermal model is a generic I 2 T Class 10 overload protection algorithm. This model is active if the MotorWindingToAmbientResistance or the MotorWindingToAmbientCapacitance values are 0.0. The purpose of this algorithm is to limit the time that a motor is operating with excessive levels of current. The relationship between Motor Overload Factory Limit trip-time and motor output current is shown in Figure 133 .

Figure 133 - Motor Overload Curve

<!-- image -->

You can use the MotorOverloadLimit attribute (default of 100%, max of 200%) to increase the motor overload trip-time by artificially increasing the motor rated current (for thermal protection only). MotorOverloadLimit should only be increased above 100% if cooling options are applied. Increasing MotorOverloadLimit causes MotorCapacity to increase more slowly.

The generic motor thermal model also derates the motor rated current (for thermal protection only) when operating at low speeds. The derating factor is 30% at 0 Hz and 0% at 20 Hz, with linear interpolation between. Operating at output frequencies less than 20 Hz causes MotorCapacity to increase more quickly.

When the generic motor thermal-model is active, the MotorCapacity attribute increases only if the motor output current is greater than the effective motor rated current (taking into account the MotorOverloadLimit and low speed derating factor). The default MotorThermalOverloadFactoryLimit and MotorThermalOverloadUserLimit values for this thermal model are both 100%.

IMPORTANT

The generic motor-thermal model does not support Current Foldback as a Motor Overload Action.

## Thermally Characterized Motors

If the MotorWindingToAmbientResistance and MotorWindingToAmbientCapacitance attribute values are both nonzero, the motor is considered thermally characterized and an alternate motor thermal model is run. The purpose of this algorithm is to limit the time that a motor is operating with excessive levels of current. This thermal model uses the first-order time constant that is determined from the MotorWindingToAmbientResistance and MotorWindingToAmbientCapacitance values to estimate the motor thermal capacity based on the motor output current.

The MotorOverloadLimit attribute (default of 100%, max of 200%) can be used to increase the motor overload trip-time by increasing the MotorThermalOverloadFactoryLimit value. The MotorOverloadLimit should be increased above 100% only if cooling options are applied. Increasing MotorOverloadLimit does not change the behavior of MotorCapacity.

## Speed Limited Adjustable Torque (SLAT)

This thermal model supports setting the MotorOverloadAction attribute as Current Foldback. Selecting the Current Foldback action results in a reduction in the current reference via the MotorThermalCurrentLimit attribute value that is reduced in proportion the percentage difference between the MotorCapacity and the MotorOverloadLimit values.

When this thermal model is active, the MotorCapacity attribute is nonzero if the motor output current is nonzero. The default MotorThermalOverloadFactoryLimit and MotorThermalOverloadUserLimit values for this thermal model are both 110%.

| IMPORTANT   | This thermal model does not derate the motor-rated current when operating at low speeds. Operating at low output frequencies does not cause the MotorCapacity behavior to change.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Speed limited adjustable torque (SLAT) is a special mode of operation that is used primarily in web handling applications. While configured for SLAT, the drive typically operates as a torque regulator. The drive can automatically enter velocity regulation, based on conditions within the velocity regulator and the magnitude of the velocity regulator's output, relative to the applied TorqueTrim attribute.

A torque regulated application can be described as any process that requires tension control. For example, a winder or unwinder with material being drawn or pulled with a specific tension required. The process also requires that another element set the speed.

When operating as a torque regulator, the motor current is adjusted to achieve the desired torque. If the material that is being wound or unwound breaks, the load decreases dramatically and the motor can potentially go into a runaway condition.

The SLAT feature is used to support applications that require a robust transition from torque regulation to velocity regulation (and vice versa). The SLAT feature can be configured via the SLATConfiguration attribute as:

Table 97 - SLAT Configuration Descriptions

| Name                  | Description                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       | SLAT Disable SLAT function is disabled. Normal Velocity Loop operation.                                                                                                                   |
| SLAT Min Speed/Torque | Drive automatically switches from Torque regulation to Velocity regulation if VelocityError < 0 and switches back to Torque regulation if VelocityError > SLATSetPoint for SLATTimeDelay. |
| SLAT Max Speed/Torque | Drive automatically switches from Torque regulation to Velocity regulation if VelocityError > 0 and switches back to Torque regulation if VelocityError < SLATSetPoint for SLATTimeDelay. |

Direction of the applied torque and direction of the material movement determine whether SLAT minimum or SLAT maximum mode should be used.

## Motion Polarity Setting

The Motion Polarity setting in the Logix Designer application &gt; Axis Properties &gt; Polarity does not affect SLAT behavior. However, you may require clarification on whether to use the SLAT Min Speed/Torque or SLAT Max Speed/Torque configuration when Motion Polarity is set to Inverted. In this case, the velocity error that is displayed in the Logix Designer application is inverted compared to what is actually used by the axis to control the SLAT function. So, if the SLAT configuration is set to Min and then Motion Polarity is switched to Inverted, change the SLAT configuration to Max.

Table 98 - SLAT Operation When Motion Polarity Is Inverted

| Velocity Command            | Motion Polarity   | SLAT Configuration   |
|-----------------------------|-------------------|----------------------|
| Positive (clockwise)        | Normal            | Min                  |
| Positive (clockwise)        | Inverted          | Max                  |
| Negative (counterclockwise) | Normal            | Min Max              |
| Negative (counterclockwise) | Inverted          |                      |

## SLAT Min Speed/Torque

SLAT Min Speed/Torque is a special mode of operation that is primarily used in web handling applications. If the TorqueTrim attribute is less than the torque output due to the velocity regulator's control effort, then the drive typically operates as a torque regulator. The drive can automatically enter velocity regulation, based on conditions within the velocity regulator and the magnitude of the velocity regulator's output relative to the torque reference.

When used for SLAT control, an application-dependent VelocityCommand value is applied to the drive via an MAJ instruction. An application-dependent TorqueTrim value is also applied via cyclic write. Under normal operation, VelocityCommand is set to a level that results in the velocity regulator's control effort becoming saturated when the motor's speed is mechanically limited. The TorqueReference value equals the TorqueTrim value, resulting in a positive VelocityError value.

If the mechanical speed limitation is removed (example: web break), the motor accelerates and VelocityError becomes negative. At this time, a forced transition to velocity regulation occurs, and the motor's speed is regulated to the VelocityCommand attribute.

The axis remains in velocity regulation until VelocityError exceeds SLATSetPoint for a period of time that is specified by SLATTimeDelay. At this point, the axis returns to operating as a torque regulator.

Figure 134 - SLAT Min Speed/Torque

<!-- image -->

See the Integrated Motion on the EtherNet/IP™ Network Reference Manual, publication MOTION-RM003, for more information on SLAT attributes.

## SLAT Max Speed/Torque

SLAT Max Speed/Torque is a special mode of operation that is primarily used in web handling applications. If the TorqueTrim attribute is greater than the torque output due to the velocity regulator's control effort, then the drive typically operates as a torque regulator. The drive can automatically enter velocity regulation, based on conditions within the velocity regulator and the magnitude of the velocity regulator's output relative to the torque reference.

When used for SLAT control, an application-dependent VelocityCommand value is applied to the drive via an MAJ instruction. An application-dependent TorqueTrim value is also applied via cyclic write. Under normal operation, VelocityCommand is set to a level that results in the velocity regulator's control effort becoming saturated when the motor's speed is mechanically limited. The TorqueReference value equals the TorqueTrim value, resulting in a negative VelocityError value.

If the mechanical speed limitation is removed (example: web break), the motor accelerates and VelocityError becomes positive. At this time, a forced transition to velocity regulation occurs, and the motor's speed is regulated to the VelocityCommand attribute.

The axis remains in velocity regulation until VelocityError is less than SLATSetPoint for a time specified by SLATTimeDelay. At this point, the axis returns to operating as a torque regulator.

Figure 135 - SLAT Max Speed/Torque

<!-- image -->

See the Integrated Motion on the EtherNet/IP Network Reference Manual, publication MOTIONRM003, for more information on SLAT attributes.

## SLAT Attributes

| ID Access Attribute        | Conditional Implementation                                               |
|----------------------------|--------------------------------------------------------------------------|
| 833 Set SLAT Configuration | 0 = SLAT Disable (1) 1 = SLAT Min Speed/Torque 2 = SLAT Max Speed/Torque |
| 834 Set SLAT Set Point     | Velocity Units                                                           |
| 835 Set SLAT Time Delay    | Seconds                                                                  |

(1) SLAT Disable, when viewed in version 28.00 (and earlier) of the Logix Designer application, reads Torque Only.

## Configure the Axis for SLAT

Follow these steps to configure the SLAT attributes.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the General category.
3. The General dialog box appears.
3. From the Axis Configuration dropdown menu, choose Velocity Loop. The Velocity Loop dialog box appears.
4. Enter values for the Velocity Loop attributes appropriate for your application.
5. Click Apply.
6. Select the Parameters List category.

<!-- image -->

<!-- image -->

The Motion Axis Parameters dialog box appears.

<!-- image -->

7. From the SLATConfiguration dropdown menu, choose the SLAT configuration appropriate for your application.

IMPORTANT

SLAT parameters are configurable only when Velocity Loop is chosen from the General category, Axis Configuration dropdown menu.

8. Click Apply.
9. Enter values for SLATSetPoint and SLATTimeDelay attributes appropriate for your application.
10. Click OK.
11. Select the Drive Parameters category.

<!-- image -->

The Drive Parameters to Controller Mapping dialog box appears.

<!-- image -->

When using SLAT with Kinetix 5500 drives, the velocity command is sent to the drive via an MAJ instruction. The torque command is sent via the cyclic write TorqueTrim attribute. See the Integrated Motion on the EtherNet/IP Network Reference Manual, publication MOTION-RM003 , for more information on cyclic read and cyclic write.

## For MAJ instructions:

- When using SLAT, start the axis with the MSO instruction.
- The VelocityCommand is sent via the MAJ instruction.
- The TorqueCommand is sent to AxisTag.TorqueTrim.
- To make changes to the VelocityCommand, you must retrigger the MAJ with the Speed value or use an MCD (motion change dynamics) instruction.
- To stop the axis, use an MAS instruction.
- The axis accelerates and decelerates at the MAJ instruction programmed Acceleration and Deceleration rates.
- You can also change the rates using the MCD instruction.

## Motor Overload Retention

The motor overload retention feature protects the motor if there is a drive power-cycle, in which the motor thermal state is lost.

With motor overload retention, upon drive power-up, the MotorCapacity attribute initially reads:

- 20% if the motor is configured to use an integral thermal switch or an integral motor winding temperature is available
- 50% if the motor is not configured to use an integral thermal switch or an integral motor winding temperature is not available

If you have a separate monitoring algorithm within your Logix 5000® controller, you can use the InitialMotorCapacity attribute (3075)10 or (C03)16 to change the initial MotorCapacity value that the motor overload retention feature populates.

- You can write to the InitialMotorCapacity attribute only in the Stopped state after power-up
- You cannot write to the InitialMotorCapacity attribute after the first time the axis is enabled following a power cycle.

Use a message instruction to write to the InitialMotorCapacity value.

In this example, the source element tag motorcapacity is a REAL data type.

<!-- image -->

## Phase Loss Detection

The phase-loss detection feature is designed to determine if motor power wiring is electrically connected to a motor and that reasonable current control exists. This attribute enables the operation of the drive's torque proving functions that work in conjunction with mechanical brake control.

When the ProvingConfiguration attribute is enabled, the drive performs a torque prove test of the motor current while in the Starting state to prove that current is properly flowing through each of the motor phases before releasing the brake. If the Torque Prove test fails, the motor brake stays engaged and an FLT-S09 Motor Phase Loss exception (fault) is generated.

## IMPORTANT

The mechanical brake must be set as soon as the drive is disabled. When the brake is under the control of the axis state machine, this is automatic. But, when controlled externally, failure to set the brake when the drive is disabled can cause a free-fall condition on a vertical application.

## Table 99 - Phase-loss Detection Startup Sequence

| Startup Phase Description   |                                                                                                                                                                      |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Phase 1                     | When the drive receives an enable request, the Starting state begins execution and torque proving starts.                                                            |
| Phase 2                     | The torque proving feature ramps current to the motor-phase output connector and verifies that the current feedback circuitry detects current on each of the phases. |
| Phase 3                     | Once motor-current feedback has been verified in each motor phase, the drive attempts to enable the current control loop at a user-specified current level, and verifies that the current loop error tolerance is within range.                                                                                                                                                                      |

Torque proving is available for all motoring configurations including closed-loop servo control and induction motors.

For permanent magnet (PM) motors, the drive attempts to apply current to the motor phases such that all current through the motor is flux current. However, due to the electrical angle of the motor at the time of the MSO instruction, it may not be possible to verify the motor phase wiring with only flux current. Therefore, with a PM motor it is possible that the motor shaft can move slightly during torque proving if no motor brake exists to hold the load.

## Phase-loss Detection Attributes

|                              | ID Access Attribute Conditional Implementation             |
|------------------------------|------------------------------------------------------------|
| 590 SSV ProvingConfiguration | 0 = Disabled 1 = Enabled                                   |
| 591 SSV TorqueProveCurrent   | % Motor Rated Units: Amps Default: 0.000 Min/Max: 0/10,000 |

## Phase-loss Detection Configuration

Follow these steps to configure the phase-loss detection attributes.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the Parameter List category and scroll to ProvingConfiguration.
3. From the ProvingConfiguration dropdown menu, choose Enabled to enable the torque proving feature.
4. Enter a value in the TorqueProveCurrent attribute appropriate for your application.
5. Click OK.

<!-- image -->

<!-- image -->

The TorqueProveCurrent attribute is active only if ProvingConfiguration is set to Enabled. TorqueProveCurrent lets you specify the amount of current that is used during the torque proving test and calculated as a percentage of motor rating. The higher the TorqueProveCurrent value the more current the drive delivers to the motor to verify that the motor phase wiring is available and capable of that current level. High current levels conversely cause more thermal stress and (potentially) can cause more torque to be driven against the motor brake during the test. If the TorqueProveCurrent level selected is too small, the drive cannot distinguish the proving current from noise, and in this case the drive posts an INHIBIT M04 torque proving configuration fault code. The minimum amount of torque proving current depends on the catalog number of the drive.

## Velocity Droop

## Phase Loss Detection Current Example

In this example, a 2198-H040-ERSx servo drive is paired with a

VPL-B1003T-C motor with 9.58 A rms rated current. Use the phase-loss detection equation and table to calculate the initial minimum torque proving current as a percentage of motor rated current. Depending on the unique characteristics of your application, the required torque proving current value can be larger than the initial recommended value.

## Figure 136 - Phase-loss Detection Equation

<!-- formula-not-decoded -->

Table 100 - Recommended Phase-loss Detection Current

| Drive Cat. No.   |   Phase-loss Detection Current, Min A, rms |
|------------------|--------------------------------------------|
| 2198-H003-ERSx   |                                     0.2514 |
| 2198-H008-ERSx   |                                     0.6285 |
| 2198-H015-ERSx   |                                     1.257  |
| 2198-H025-ERSx   |                                     2.011  |
| 2198-H040-ERSx   |                                     3.268  |
| 2198-H070-ERSx   |                                     5.782  |

The velocity droop function can be useful when some level of compliance is required due to rigid mechanical coupling between two motors. The feature is supported when the axis is configured for Frequency Control, Velocity Control, or Position Control.

## Closed Loop Control

The closed-loop velocity droop function is supported when configured for either Velocity or Position control. The velocity error input to the integral term is reduced by a fraction of the velocity regulator's output, as controlled by the VelocityDroop attribute. Therefore, as torque loading on the motor increases, actual motor speed is reduced in proportion to the droop gain. This is helpful when some level of compliance is required due to rigid mechanical coupling between two motors.

| IMPORTANT   | The closed-loop velocity droop function acts to reduce the velocity error input to the integral term, but never changes the polarity of the velocity error.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | When configured for closed-loop control, the units of the VelocityDroop attribute are Velocity Control Units / Sec / % Rated Torque.                          |

## Frequency Control

The velocity droop function is also supported when configured for Frequency Control. As the estimated Iq current within the motor increases, the velocity reference is reduced in proportion to the VelocityDroop attribute. Therefore, as torque loading on the motor increases, actual motor speed is reduced in proportion to the droop gain. This is helpful when some level of compliance is required due to rigid mechanical coupling between two motors.

IMPORTANT

The frequency-control velocity droop function acts to reduce the velocity reference, but never changes the direction of the velocity reference.

IMPORTANT

When configured for frequency control, the units of the VelocityDroop attribute are Velocity Control Units / Sec / % Rated Iq Current.

## Velocity Droop Attribute

| ID Access Attribute        | Conditional Implementation     |
|----------------------------|--------------------------------|
| 464/321 SSV Velocity Droop | Velocity Units / Sec / % Rated |

## Velocity Droop Configuration

Follow these steps to configure the velocity droop attribute.

1. In the Controller Organizer, right-click an axis and choose Properties.
2. Select the Parameter List category and scroll to VelocityDroop.
3. Enter a value in the Velocity Droop attribute appropriate for your application.
4. Click OK.

<!-- image -->

## Commutation Test

## Adaptive Tuning

The commutation test determines an unknown commutation offset and can also be used to determine the unknown polarity of the start-up commutation wiring. You can also use the commutation test to verify a known commutation offset and the polarity start-up commutation wiring.

IMPORTANT For Kinetix 5500 drives, this test applies to only third-party motors.

IMPORTANT

When motors have an unknown commutation offset and are not listed in the Motion Database by catalog number, you cannot enable the axis.

## Figure 137 - Hookup Tests - Commutation Tab

<!-- image -->

To run the commutation test, see Test the Axes on page 136 .

The adaptive tuning feature is an algorithm inside the Kinetix 5500 servo drives. The algorithm continuously monitors and, if necessary, adjusts or adapts various filter parameters and, in some cases, control-loop gains to compensate for unknown and changing load conditions while the drive is running. Its primary function is to:

- Automatically adjust torque-loop notch and low-pass filter parameters to suppress resonances
- Automatically adjust control-loop gains to avoid instability when detected

See Motion System Tuning Application Techniques, publication MOTION-AT005, for more information on the AdaptiveTuningConfiguration attribute.

## Notes:

## 2198-UM001M-EN-P

## 2198-UM001L-EN-P

## 2198-UM001K-EN-P

## 2198-UM001J-EN-P

## History of Changes

This appendix contains the new or updated information for each revision of this publication. These lists include substantive updates only and are not intended to reflect all changes. Translated versions are not always available for each revision.

## 2198-UM001M-EN-P, November 2022

| Change                                                                       |
|------------------------------------------------------------------------------|
| Added UK (or UKCA) certification.                                            |
| Changed the drive-to-motor maximum cable lengths for continuous flex cables. |

## 2198-UM001L-EN-P, February 2022

| Change                                                                                     |                                                                                            |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Updated guidance for downloading fault code and parameter spreadsheets.                    | Updated guidance for downloading fault code and parameter spreadsheets.                    |
| Replaced LDAT-Series with Kinetix LDAT.                                                    | Replaced LDAT-Series with Kinetix LDAT.                                                    |
| Replaced Bulletin 2090 and 2090-Series with Kinetix 2090.                                  | Replaced Bulletin 2090 and 2090-Series with Kinetix 2090.                                  |
| Added Download Firmware, AOP, EDS, and Other Files section to Preface.                     | Added Download Firmware, AOP, EDS, and Other Files section to Preface.                     |
| Added Access Fault Codes section to Preface.                                               | Added Access Fault Codes section to Preface.                                               |
| Added publication 2198-RD005 to Additional Resources table.                                | Added publication 2198-RD005 to Additional Resources table.                                |
| Updated phase-loss detection equation in the Phase Loss Detection Current Example section. | Updated phase-loss detection equation in the Phase Loss Detection Current Example section. |

## 2198-UM001K-EN-P, November 2021

| Change                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------|
| Added publication month and year to page footers.                                                                                    |
| Added GuardLogix 5580 and Compact GuardLogix 5380 controller numbers to the Important table content.                                 |
| Added GuardLogix 5580, Compact GuardLogix 5380, ControlLogix 5580, and CompactLogix 5380 controllers to the Important table content. |
| Added 140UT- catalog numbers to the various Drive Systems tables, and to the two Shared AC/DC and Hybrid Systems tables.             |

## 2198-UM001J-EN-P, November 2019

## Change

Added reference to Knowledgebase article for fault codes and descriptions.

Added Kinetix 5700 drive compatibility with 2090-CSxM1xx -xxVAxx (PVC) and 2090-CSBM1xx-xxLFxx (Halogen-free PUR) single motor-cables.

<!-- image -->

## 2198-UM001I-EN-P

## 2198-UM001H-EN-P

## 2198-UM001I-EN-P, May 2019

| Change                                                                                                                                                                                                                      |                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added Access the Attachments that explains how the fault code tables (FLT Sxx, FLT Mxx, and INIT FLT for example), previously in Troubleshoot the Kinetix 5500 Drive System (chapter 7), moved to the attached spreadsheet. | Added Access the Attachments that explains how the fault code tables (FLT Sxx, FLT Mxx, and INIT FLT for example), previously in Troubleshoot the Kinetix 5500 Drive System (chapter 7), moved to the attached spreadsheet. |
| Added Kinetix VPH hygienic stainless-steel servo motors as another rotary motor compatible with Kinetix 5500 servo drives.                                                                                                  | Added Kinetix VPH hygienic stainless-steel servo motors as another rotary motor compatible with Kinetix 5500 servo drives.                                                                                                  |
| Added Kinetix VPAR electric cylinders as another linear actuator compatible with Kinetix 5500 servo drives.                                                                                                                 | Added Kinetix VPAR electric cylinders as another linear actuator compatible with Kinetix 5500 servo drives.                                                                                                                 |
| Added 2198-DBRxx-F AC line filters.                                                                                                                                                                                         | Added 2198-DBRxx-F AC line filters.                                                                                                                                                                                         |
| Added 24V Control Power Evaluation with information to help evaluate 24V control power current requirements.                                                                                                                | Added 24V Control Power Evaluation with information to help evaluate 24V control power current requirements.                                                                                                                |
| Added Contactor Selection with information to help evaluate AC input power system requirements.                                                                                                                             | Added Contactor Selection with information to help evaluate AC input power system requirements.                                                                                                                             |
| Added Passive Shunt Considerations with information to help evaluate when an external shunt resistor is required.                                                                                                           |                                                                                                                                                                                                                             |
| Added the 2198-CAPMOD-1300 capacitor module power dissipation specifications to the table.                                                                                                                                  | Added the 2198-CAPMOD-1300 capacitor module power dissipation specifications to the table.                                                                                                                                  |
| Moved Capacitor Module Features and Indicators (previously in Chapter 5) to Chapter 4.                                                                                                                                      | Moved Capacitor Module Features and Indicators (previously in Chapter 5) to Chapter 4.                                                                                                                                      |
| Added Module Status Connector Pinout.                                                                                                                                                                                       | Added Module Status Connector Pinout.                                                                                                                                                                                       |
| Added new information regarding the use of 2198-DBRxx-F AC line filters and servo drive ground screw settings.                                                                                                              | Added new information regarding the use of 2198-DBRxx-F AC line filters and servo drive ground screw settings.                                                                                                              |
| Updated the maximum input current rating (40 A) for the 24V input power shared-bus connection system.                                                                                                                       | Updated the maximum input current rating (40 A) for the 24V input power shared-bus connection system.                                                                                                                       |
| Updated Install the Kinetix 5500 Add-On Profile with instructions for accessing downloads on the Product Compatibility Download Center (PCDC).                                                                              | Updated Install the Kinetix 5500 Add-On Profile with instructions for accessing downloads on the Product Compatibility Download Center (PCDC).                                                                              |
| Added step 5 to the Tune the Axes procedure.                                                                                                                                                                                | Added step 5 to the Tune the Axes procedure.                                                                                                                                                                                |
| Updated Motor Analyzer Category Troubleshooting with rated slip-speed information.                                                                                                                                          | Updated Motor Analyzer Category Troubleshooting with rated slip-speed information.                                                                                                                                          |
| Added links to the Product Certifications website to Chapter 9 and Chapter 10 replacing the Certifications appendix.                                                                                                        | Added links to the Product Certifications website to Chapter 9 and Chapter 10 replacing the Certifications appendix.                                                                                                        |

## 2198-UM001H-EN-P, November 2016

| Change                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added the CompactLogix™ 5380 controller to safe torque-off configurations.                                                                                                      |
| Updated drive system pollution degree 2 and IP20 specifications.                                                                                                                |
| Updated circuit breaker/fuse specifications with additional circuit-breaker solutions.                                                                                          |
| Added Registration Accuracy value to digital input specifications table.                                                                                                        |
| Updated Absolute Position table and figure with Kinetix VPL and Kinetix VPF multi-turn encoder motors and made corrections to other motor/actuator specifications where needed. |
| Added the CompactLogix 5380 controller to safe torque-off configurations.                                                                                                       |
| Added Protected Mode menu settings to LCD display navigation tables.                                                                                                            |
| Updated Kinetix 5500 Add-on Profile information for drive firmware 7.001                                                                                                        |
| Updated dialog boxes with active attributes for drive firmware 7.001, removed work-around procedures, and added CurrentVectorLimit parameter to steps.                          |
| Added software overtravel fault-code information to Fault Codes introductory text.                                                                                              |
| Added fault code FLT S02 and other drive firmware 7.001 changes.                                                                                                                |
| Updated FLT S47 FDBK DEVICE FAILURE with Hiperface Feedback sub-codes.                                                                                                          |
| Added fault code INHIBIT S04 COMMUTATION NOT CONFIGURED.                                                                                                                        |
| Updated General Troubleshooting with Adaptive Tuning attributes.                                                                                                                |
| Updated Configurable Stopping Actions table with footnote for Current Limiting feature.                                                                                         |
| Added fault-code FLT S02 drive behavior and updated drive behavior for several other fault codes.                                                                               |
| Added references to publications 1756-UM022 and 1769-UM022 .                                                                                                                    |
| Updated system requirements with important axis-state information for drives and Protected Mode.                                                                                |
| Updated Current Limiting for Frequency Control with changes in drive firmware 7.001.                                                                                            |
| Updated Motor > Model Category text with changes in drive firmware 7.001.                                                                                                       |
| Updated Motor Tests and Autotune Matrix table with changes in drive firmware 7.001.                                                                                             |
| Updated Motor Analyzer Category Troubleshooting with changes in drive firmware 7.001.                                                                                           |
| Added Motion Polarity Setting with changes in drive firmware 7.001.                                                                                                             |
| Updated Motor Overload Retention with changes in drive firmware 7.001.                                                                                                          |

## 2198-UM001G-EN-P

## 2198-UM001F-EN-P

## 2198-UM001E-EN-P

## 2198-UM001G-EN-P, March 2016

| Change                                                                                   |                                                                                          |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Updated Drive-to-Motor Maximum Cable Length table with the 2090-CSBM1E1 cable.           | Updated Drive-to-Motor Maximum Cable Length table with the 2090-CSBM1E1 cable.           |
| Updated Transformer Selection with line reactor requirements.                            | Updated Transformer Selection with line reactor requirements.                            |
| Updated IEC (non-UL) Circuit Breaker/Fuse Selection table with DIN gG fuses.             | Updated IEC (non-UL) Circuit Breaker/Fuse Selection table with DIN gG fuses.             |
| Updated Kinetix 5500/5700 Add-On Profile with changes for revision 5.001.                | Updated Kinetix 5500/5700 Add-On Profile with changes for revision 5.001.                |
| Updated the Revision field with firmware revision 5.001 and added step 4d.               | Updated the Revision field with firmware revision 5.001 and added step 4d.               |
| Added Current Limiting for Frequency Control (new feature with drive firmware 5.001).    | Added Current Limiting for Frequency Control (new feature with drive firmware 5.001).    |
| Added Stability Control for Frequency Control (new feature with drive firmware 5.001).   | Added Stability Control for Frequency Control (new feature with drive firmware 5.001).   |
| Revised the Motor Analyzer Category Troubleshooting content to increase understanding.   | Revised the Motor Analyzer Category Troubleshooting content to increase understanding.   |
| Added Commutation Test to Hookup Tests category (new feature with drive firmware 5.001). | Added Commutation Test to Hookup Tests category (new feature with drive firmware 5.001). |

## 2198-UM001F-EN-P, December 2015

| Change                                                                                                                                                                                   |                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Updated references to compatible Logix 5000™ PAC controllers. Added compatibility with ControlLogix® 5580 controllers.                                                                   | Updated references to compatible Logix 5000™ PAC controllers. Added compatibility with ControlLogix® 5580 controllers.                                                                   |
| Added support for using 2090-CSxM1DG cables with Kinetix 5500 servo drives.                                                                                                              | Added support for using 2090-CSxM1DG cables with Kinetix 5500 servo drives.                                                                                                              |
| Added ControlLogix 5580 controller to Ethernet Cable Connections.                                                                                                                        | Added ControlLogix 5580 controller to Ethernet Cable Connections.                                                                                                                        |
| Added link and installation information for the Kinetix 5500/5700 Add-on Profile available with drive firmware 4.001.                                                                    | Added link and installation information for the Kinetix 5500/5700 Add-on Profile available with drive firmware 4.001.                                                                    |
| Added Configure Feedback-only Axis Properties.                                                                                                                                           | Added Configure Feedback-only Axis Properties.                                                                                                                                           |
| Added Configure Induction-motor Frequency-control Axis Properties with support for Basic Volts/Hz, Sensorless Vector, and Fan/Pump Volts/Hz methods available with drive firmware 4.001. | Added Configure Induction-motor Frequency-control Axis Properties with support for Basic Volts/Hz, Sensorless Vector, and Fan/Pump Volts/Hz methods available with drive firmware 4.001. |
| Added Tune Induction Motors.                                                                                                                                                             | Added Tune Induction Motors.                                                                                                                                                             |
| Updated fault memory description to reflect 128 fault log.                                                                                                                               | Updated fault memory description to reflect 128 fault log.                                                                                                                               |
| Updated Appendix D with support information for new features available with drive firmware 4.001.                                                                                        | Updated Appendix D with support information for new features available with drive firmware 4.001.                                                                                        |

## 2198-UM001E-EN-P, September 2015

| Change                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added table to Conventions to better define -ERS and -ERS2 catalog number strings.                                                                         |
| Added Motor Feedback and Feedback-only Configurations to better describe how feedback connector kits and cables are used.                                  |
| Updated drive-to-drive Ethernet cables with 0.15 mm (6.0 in.) catalog number.                                                                              |
| Updated cable length table with limitations for 2090-CSxM1DF 10 AWG cables.                                                                                |
| Updated panel requirements with protection class IP20 and pollution degree 2 specifications. Updated Ethernet cable bullet to say cables must be shielded. |
| Updated Circuit Breaker/Fuse Selection tables with replacement circuit breaker catalog numbers.                                                            |
| Updated Digital Inputs Connector Pinouts with configurable I/O content.                                                                                    |
| Added ATTENTION statement to Motor Power connector pinouts.                                                                                                |
| Updated Digital Input tables with new configurable features.                                                                                               |
| Updated Motor Brake Circuit with additional motor brake control information.                                                                               |
| Updated the input power section for consistency with other drive-family user manuals. Added an impedance grounded power configuration, single-phase grounded configuration, and leakage current information.                                                                                                                                                            |
| Updated the shield clamp procedure with additional retention screw details.                                                                                |
| Added Induction Motor specifications table.                                                                                                                |
| Updated IMPORTANT statement with limitations for 2090-CSxM1DF 10 AWG cables.                                                                               |
| Updated the shield clamp procedure with additional retention screw details.                                                                                |
| Updated drive configuration dialog boxes with changes for Studio 5000 Logix Designer® application, version 27, throughout Chapter 6.                       |
| Updated Tune the Axes with load observer information.                                                                                                      |
| Added ATTENTION statement regarding bus-sharing groups.                                                                                                    |

## 2198-UM001D-EN-P

## 2198-UM001E-EN-P, September 2015 (Continued)

| Change                                                                                  |
|-----------------------------------------------------------------------------------------|
| Added Kinetix 5500 Drive Exception Action Definitions table.                            |
| Updated stopping actions in Drive Behavior table.                                       |
| Updated STO State Reset for new safe torque-off functionality.                          |
| Updated Appendix E with new safety certificate and declaration of conformity documents. |
| Updated Appendix F with Summary of Changes from publication 2198-UM001D-EN-P.           |
| Updated Fault Codes summary table and fault code tables                                 |
| Added Kinetix 5500 Drive Exception Action Definitions table                             |
| Updated stopping actions in Drive Behavior table                                        |
| Updated STO State Reset for new safe torque-off functionality                           |
| Updated Appendix E with new safety certificate and declaration of conformity documents  |
| Updated Appendix F with Summary of Changes from publication 2198-UM001D-EN-P            |

## 2198-UM001D-EN-P, May 2014

| Change                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Replaced catalog number string 2198-Hxxx-ERS with 2198-Hxxx-ERSx when there’s no need to distinguish between -ERS or -ERS2.                      |
| Added footnotes and other text to note that STO connector does not apply to 2198-Hxxx-ERS2 drives.                                               |
| Added references to the Hiperface-to-DSL (series B) feedback converter kit as needed.                                                            |
| Added Kinetix VPF food-grade motors as compatible with Kinetix 5500 drives throughout the manual.                                                |
| Added Kinetix LDAT integrated linear thrusters as compatible with Kinetix 5500 drives throughout the manual.                                     |
| Added 2198-Hxxx-ERS2 catalog numbers throughout the manual.                                                                                      |
| Added Safe Torque-off Configurations.                                                                                                            |
| Corrected the short-circuit current rating from 150,000 to 200,000 A.                                                                            |
| Updated the Absolute Position Feature section with multi-turn catalog number strings for compatible motors and actuators.                        |
| Updated Ethernet Cable Connections with ControlLogix EtherNet/IP communication modules.                                                          |
| Updated controller configuration by adding GuardLogix controller and ControlLogix EtherNet/IP communication module configuration.                |
| Broke out Configure the Kinetix 5500 Drive with separate procedures for 2198-Hxxx-ERS and 2198-Hxxx-ERS2 servo drives.                           |
| Updated Tune the Axes with a reference to the load observer feature.                                                                             |
| Added FLT-S04 - MTR OVERSPEED UL fault code. Added FLT S09 – MTR PHASE LOSS fault code. Added FLT S49 – BRAKE SLIP FLT fault code.               |
| Added FLT-M28 - SAFETY COMM fault code.                                                                                                          |
| Added INIT FLT-M14 - SAFETY FIRMWARE fault code.                                                                                                 |
| Updated NODE FLT fault codes. Added NODE FLT 03 – HARDWARE 04 fault code.                                                                        |
| Added NODE ALARM 04 – CLOCK SKEW ALARM.                                                                                                          |
| Updated the configurable stopping action definitions.                                                                                            |
| Added FLT-S04 - MTR OVERSPEED UL fault behavior. Added FLT S15 – CONV OVERCURRENT fault behavior. Added FLT S49 – BRAKE SLIP FLT fault behavior. |
| Added FLT-M28 - SAFETY COMM fault behavior.                                                                                                      |
| Added NODE FLT 05 – CLOCK SKEW FLT fault behavior                                                                                                |
| Updated System Operation timing diagram with 100 ms.                                                                                             |
| Added Chapter 10, Kinetix 5500 Safe Torque-off - Integrated Safety.                                                                              |

## 2198-UM001C-EN-P

## 2198-UM001B-EN-P

## 2198-UM001C-EN-P, February 2014

| Change                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------|
| Added Hiperface-to-DSL feedback converter kit throughout the manual, as needed.                                                       |
| Added Kinetix VPS stainless-steel servo motors as another rotary motor compatible with Kinetix 5500 servo drives.                     |
| Updated Configure Feedback Only Axis Properties to include the Bulletin 842E-CM integrated motion encoder on the EtherNet/IP network. |
| Added History of Changes appendix.                                                                                                    |

## 2198-UM001B-EN-P, September 2013

| Change                                                                                                                                                            |                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added capacitor module shared-bus replacement kit to System Overview table.                                                                                       | Added capacitor module shared-bus replacement kit to System Overview table.                                                                                       |
| Added Drive-to-Motor Maximum Cable Lengths table to CE requirements.                                                                                              | Added Drive-to-Motor Maximum Cable Lengths table to CE requirements.                                                                                              |
| Added IMPORTANT advisory regarding non-UL Listed circuit breakers.                                                                                                | Added IMPORTANT advisory regarding non-UL Listed circuit breakers.                                                                                                |
| Updated Circuit Breaker Selection tables with Allen-Bradley catalog numbers.                                                                                      | Updated Circuit Breaker Selection tables with Allen-Bradley catalog numbers.                                                                                      |
| Updated Connection System Example diagram with DC bus T-connector removal instructions.                                                                           | Updated Connection System Example diagram with DC bus T-connector removal instructions.                                                                           |
| Updated Wire the Motor Power, Brake, and Feedback Connectors with continuous-flex cable catalog numbers and IMPORTANT advisory regarding single-cable technology. | Updated Wire the Motor Power, Brake, and Feedback Connectors with continuous-flex cable catalog numbers and IMPORTANT advisory regarding single-cable technology. |
| Updated NODE FLT 03 HARDWARE 01 and added sub-codes HARDWARE 02 and HARDWARE 03.                                                                                  | Updated NODE FLT 03 HARDWARE 01 and added sub-codes HARDWARE 02 and HARDWARE 03.                                                                                  |
| Added IMPORTANT advisory regarding DC bus T-connector removal.                                                                                                    | Added IMPORTANT advisory regarding DC bus T-connector removal.                                                                                                    |
| Updated Energy Absorbing Potential table with External Shunt values.                                                                                              | Updated Energy Absorbing Potential table with External Shunt values.                                                                                              |

## Notes:

## Numerics

2090-CSBM1DF 16 , 83

2090-CSBM1DG 16 , 83

2198-CAPMOD-1300 29

2198-DBRxx-F 16

2198-DBxx-F 16

2198-H2DCK 15 , 22 , 67 , 88 , 97

2198-KITCON-DSL 15 , 22 , 85

## 24V input power connector

evaluation 36 pinouts 62 wiring 80

## A

about this publication 11

absolute position feature 67

AC line filters

2198-DBRxx-F 16

2198-DBxx-F 16

noise reduction 44

actions category 130

adaptive tuning 243

Add-on Profile 88 , 108

alarm 149

application requirements 165

applying power

132

associated axes tab 117

audience for this manual 11

axis properties

121

,

122

,

127

axis unstable 147

## B

basic volts/hertz

BC connector pinouts 63 wiring 84 , 89

Beldon

89

## block diagrams

capacitor module 192 191

power

## bonding

EMI (electromagnetic interference) ) 40 examples 41 high frequency energy 42 42

subpanels brake relay 65

## Bulletin

MPAI electric cylinders 22 MPAR electric cylinders 22 MPAS linear stages 22

## bus

123 , 213

configuration 119

regulator 119

## bus-sharing

group 119 group example 134 groups 133

## C

## cables

83 , 89 , 95

100

86 , 93 , 96

catalog numbers categories 44 Ethernet cable length induction motors 89 shield clamp calculate model 229

capacitor module 192

catalog number 29 description 15 interconnect diagram status indicator 147 support 51 wiring 98

## catalog numbers

29

motor cables 83 , 89 , 95

capacitor module servo drives hardwired 29 integrated 29

shared-bus connection system 29

## category 3

requirements 158 , 166

stop category definitions 158 , 166

## CE

compliance 30

## certification

application requirements 165 PL and SIL 158 , 167 TÜV Rheinland 157 , 165 user responsibilities 157 , 165 website 157 , 165

circuit breaker selection 33

clamp

86

,

93

,

96

commutation offset 137 , 243

## CompactLogix

Ethernet connections 100

## compatibility

motor feedback 127

181

## configuring

## basic volts/hertz 123 controller 109 fan/pump volts/hertz 126 feedback-only axis 118 , 121 flux up 225 frequency control category 123 , 124 , 126 general category 121 , 122 hardwired 112 home screen 102 hookup test 137 induction motor tuning 141 induction-motor frequency-control axis 122 integrated safety 114 IP address 107 Logix 5000 communication 193 master feedback 121 menu screens 103 module properties 113 , 114 , 116 , 117 , 118 inhibit module 195 motion group 120 motor category 226 test 136 motor category 122 motor feedback 127 motor&gt;analyzer category 125 network parameters 107 parameter list category 123 , 124 , 126 power tab bus-sharing group example 134 bus-sharing groups 133 sensorless vector 124 servo motor axis actions category 130 delay times 131 general category 127 load category 129 motor category 128 parameter list category 131 scaling category 129 setup screens 104 SLAT 235 SPM motor closed-loop axis properties 127 startup sequence 106 torque proving 240 velocity droop 242 connecting CompactLogix 100 ControlLogix 100 converter kit shield clamp 96 Ethernet cables 100 motor shield clamp 86 , 93 connector kit 2198-H2DCK 88 2198-KITCON-DSL 85 connector locations servo drives 60 control power input specifications 66 pinouts 62 system calculations 208 wiring 80 ControlFLASH firmware update 193 firmware upgrade 193 198

troubleshooting

## controller

and drive behavior 149

CompactLogix 109

## configure 109 ControlLogix 109 properties date/time tab 111 enable time synchronization ControlLogix Ethernet connections 100 conventions used in this manual 11 converter kit 2198-H2DCK 88 cable lengths, max 83 , 91 cable preparation motor feedback 96 motor power/brake 91 description 15 Kinetix 5500 AOP 88 CP connector pinouts 62 wiring 80 current limiting 216 current regulator loop 225 D date/time tab 111 DC bus connector pinouts 62 delay times 131 digital inputs 64 pinouts 62 wiring 82 disable 149 display 102 download program 131 drilling hole patterns 51 drive replacement integrated safety 171 dynamic motor test 229 E earth ground 76 EMC motor ground termination 86 EMI (electromagnetic interference) bonding 40 enable time synchronization 111 enclosure power dissipation 38 requirements 31 sizing 38 encoder support DSL 67 energy calculations 209 erratic operation 148 Ethernet connector pinouts 63 EtherNet/IP

connecting cables 100 connections 65 PORT1 and PORT2 connectors 100

111

## external shunt resistor 45 , 46

62

pinouts wiring 99

## F

fan/pump 214

fan/pump volts/hertz 126

## fault

code summary 144 codes 144 status only 149

## feedback

configurations 22 feedback-only axis 118 grounding technique 185

feedback-only axis 121

firmware update 193

verify update 199

firmware upgrade

ControlFLASH software 193 system requirements 193

flux up 223

attributes 224

frequency control category 123 , 124 , 126

fuse selection 33

## G

## general

category 121 , 122 , 127 tab 113 , 114

grounded power configuration 71

## grounding

multiple subpanels 77 screws 75

## H

hardwired connections 112

hardwired STO 26

HF bonding 40

high frequency energy 42

Hiperface-to-DSL feedback converter kit 88

hole patterns 51

home screen soft menu 102

hookup test 137 , 243

## I

## I/O

digital inputs specifications 64

IEC 61508 158 , 167

IEC 62061 158 , 167

ignore

149

## induction motor control 89

configure flux up 225 control methods basic volts/hertz 213 fan/pump 214 sensorless vector 215 flux up 223

## attributes 224 frequency-control axis 122 motor analyzer category 227 and inertia tests 228 data sheet 226 model category 227 multiple skip speed 222 open-loop frequency control 212 , 216 , 219 skip speed 221 SLAT 234 inhibit module 195 input power wiring 24V control 80 3-phase delta 72 determine input power 71 grounded power configuration 71 grounding screws 75 mains 81 remove grounding screws 75 ungrounded power configuration 73 installing drive accessories AC line filters 44 external shunt resistor 45 , 46 installing your drive 31 bonding examples 41 bonding subpanels 42 cable categories 44 circuit breakers 33 clearance requirements 39 fuse selection 33 HF bonding 40 passive shunts 37 system mounting requirements 31 transformer 33 integrated safety connections 114 drive replacement 171 out-of-box state 169 protocol 173 STO state reset 167 integrated STO 27 , 28 interconnect diagrams 2198 drive with LDAT 188 2198 drive with MPAR/MPAI 190 2198 drive with MPAS 189 2198 drive with MPL/MPM/MPF/MPS 186 2198 drive with VPAR 187 2198 drive with VPL/VPF/VPH/VPS 185 bus-sharing drives shared AC 182 shared AC/DC 182 shared AC/DC hybrid 183 shared DC 183 capacitor module 181 feedback grounding technique 185 notes 179 shunt resistor 184 single-axis drive single-phase 181 three-phase 180 IOD connector pinouts 62 wiring 82 IP address 107 IPD connector pinouts 61 81

wiring

## ISO 13849-1 CAT 3

requirements

158 , 166

stop category definitions 158 , 166

## K

Kinetix 5500 15

Kinetix LDAT linear thruster 22

Kinetix VP electric cylinders 22

## L

Lapp 89

LCD display 102

messages 144

## LDAT linear thruster

Kinetix 22

## linear actuators

interconnect diagram

LDAT 188

MPAR/MPAI 190

MPAS 189

link/activity status indicator 146

speed status indicator 146

load category 129

load observer 138

Logix 5000 communication 193

Logix Designer 107

Logix Designer application 109

## M

## mains input power connector

pinouts 61

wiring 81

major fault 149

master feedback 121

menu screens

103

MF connector pinouts 63

wiring 85 , 94

minor fault 149

module definition 113 , 114

## module properties

associated axes tab 117

general tab 113 , 114

module definition 113 , 114

new tag 117

power tab 118

safety tab 116

## module status connector

pinouts 61

module status indicator 146

Motion Analyzer website 12

motion direct commands

STO bypas 173

warning messages 174

motion group 120

## link

## motor

analyzer category 125 , 227 category 122 data sheet 226 feedback compatibility 127 model category 227

motor and inertia tests 228

overload retention 238

thermal models 231

## motors

accel/decel problems 147

brake connector pinouts 63

wiring 84 , 89

cable catalog numbers 83 , 89 , 95

cable length 30 , 31 , 83 , 91

category 128

feedback connector pinouts 63

wiring 85 , 94

ground termination 86

induction 89

interconnect diagram

MPL/MPM/MPF/MPS 186

VPL/VPF/VPH/VPS 185

overheating 148

power connector pinouts 63

wiring 83 , 89

shield clamp wiring 86 , 93 , 96

testing 136

tuning 136

velocity 148

## mounting your capacitor module

mounting order 48

## mounting your drive

attaching to the panel drilling hole patterns mounting order 48 single-axis 50

58

51

shared-bus connection system 49

zero-stack tab and cutout 48

## MP connector

pinouts

63

wiring 83 , 89

MPAI electric cylinders 22

MPAR electric cylinders 22

MPAS linear stages 22

MS connector pinouts 61

multiple skip speed 222

## N

navigation buttons 102

network parameters 107 status indicator 146

## new tag

data type 117

## noise

abnormal 148

feedback 148

reduction 44

## O

open-loop frequency control 212 out-of-box state 169

## P

panel requirements 31

parameter list category 123 , 124 , 126 , 131

passive shunt use cases 37

PFH definition 161 , 168

## pinouts

24V input power connector 62

DC bus connector 62

digital inputs connector 62

Ethernet connector 63

mains input power connector 61

module status connector 61

motor brake connector 63

motor feedback connector 63

motor power connector 63

safe torque-off 161

shunt connector 62

## planning your installation 31

power dissipation 38

power tab bus configuration 119

bus regulator 119

bus-sharing group 119

group example 134

groups 133

power structure 118

power up 132

product selection website 12

## R

rated slip speed 229

regenerative energy 209

remove grounding screws 75

## remove/replace drive

remove drive 155

remove power 154

replace drive 155 startup and configure

156

## routing power and signal wiring 70

## S

## SAB 89

## safe torque-off 162

bypass wiring 163

cascaded wiring 164

hardwired 26

27 , 28

159 , 167

68 , 164 , 177

configurations integrated operation PFH 161 , 168 pinouts 161 specifications

## safety

tab 116

scaling category 129

| sensorless vector  124 ,  215                                              |
|----------------------------------------------------------------------------|
| setup screens  104                                                         |
| shared AC                                                                  |
| configurations  201 interconnect diagram  182                              |
| shared AC/DC                                                               |
| configurations  204                                                        |
| interconnect diagram  182                                                  |
| power sharing example  208                                                 |
| shared AC/DC hybrid                                                        |
| configurations  205                                                        |
| interconnect diagram  183                                                  |
| power sharing example  207                                                 |
| shared DC                                                                  |
| configurations  202 183                                                    |
| interconnect diagram                                                       |
| power sharing example  206                                                 |
| shared-bus                                                                 |
| configurations  201                                                        |
| connection system                                                          |
| 49 catalog numbers  29                                                     |
| guidelines  201 86 ,  93 ,  96                                             |
| shield clamp                                                               |
| shunt connector                                                            |
| pinouts  62 99                                                             |
| wiring                                                                     |
| shunt resistor                                                             |
| interconnect diagram  184                                                  |
| shunts passive  37                                                         |
| 149                                                                        |
| shutdown  sizing                                                           |
| control power  208 energy calculations                                     |
| 209 power sharing examples shared AC/DC  208                               |
| shared DC  206                                                             |
| shared AC/DC hybrid  207 shared-bus configurations  201                    |
| shared AC  201 shared AC/DC  204                                           |
| shared AC/DC hybrid  205 shared DC  202                                    |
| 201                                                                        |
| shared-bus guidelines  221                                                 |
| skip speed  232                                                            |
| SLAT  attributes  234 configuring  235                                     |
| slip test messaging  230                                                   |
| soft menu                                                                  |
| home screen  102                                                           |
| software                                                                   |
| Logix Designer application  109 specifications                             |
| brake relay  65 control power input                                        |
| 66 digital inputs  64                                                      |
| motor feedback                                                             |
| EtherNet/IP connections  absolute position                                 |
| 65 67 67                                                                   |
| Stegmann DSL  safe torque-off  68 ,  164 ,                                 |
| 177                                                                        |
| speed limited adjustable torque  232 SPM motor closed-loop axis properties |
| 219                                                                        |
| stability control                                                          |
| 127                                                                        |

startup sequence 106

static motor test 229

status indicators capacitor module 147 link speed status 146 link/activity status 146 module status 146 network status 146 STO bypass 173 connector pinouts 161 connector wiring 162 state reset 167 stop drive 149 planner 149 Studio 5000 Logix Designer 107 system block diagrams capacitor module 192 power 191 components 15 ground 76 mounting requirements 31 overview EtherNet/IP 23 , 24 , 25 shared AC 18 shared AC/DC 19 shared AC/DC hybrid 21 shared DC 20 standalone 17 T testing axes hookup test 137 time synchronization 111 torque proving 238 attributes 238 configuring 240 training 11 transformer sizing 33 troubleshooting alarm 149 capacitor module status 147 ControlFLASH 198 controller/drive fault behavior 149 disable 149 fault code summary 144 codes 144 status only 149 general system problems 147 abnormal noise 148 axis unstable 147

erratic operation 148

feedback noise 148

motor accel/decel 147

motor overheating 148

motor velocity 148

## UK

compliance 30

ungrounded power configuration 73

use cases passive shunt 37

user responsibilities 165

## V

## velocity droop 241

attribute 242

configure 242

verify update 199

voltage drop

24V input power 36

## W

## website

certifications 157 , 165 Motion Analyzer 12 product selection 12

no rotation 148

ignore 149

LCD display messages 144

link speed status indicator 146

link/activity status indicator 146

major fault 149

minor fault 149

module status indicator 146

network status indicator 146

safety precautions 143

shutdown 149

status indicators stop

drive 149

planner 149

## tuning

induction motor 141

PM motor 138

## tuning axes

load observer 138

## typical installation

EtherNet/IP 23 , 24 , 25

shared AC 18

shared AC/DC 19

shared AC/DC hybrid 21

shared DC 20

standalone 17

## U

146

## wiring

BC connector 84 89

96

grounded power configuration 71

86 , 93

75

routing power and signal wiring 70

163

, capacitor module 98 converter kit shield clamp CP connector 80 earth ground 76 Ethernet cables 100 external shunt resistor 99 grounding screws 75 guidelines 79 input power type 71 IOD connector 82 IPD connector 81 MF connector 85 , 94 motor cable shield clamp MP connector 83 , 89 RC connector 99 remove grounding screws requirements 70 , 78 safe torque-off bypass safe torque-off cascaded 164

STO connector 162

ungrounded power configuration 73

## Z

zero-stack tab and cutout 48

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

Allen-Bradley, CompactGuardLogix, CompactLogix, ControlFLASH, ControlLogix, expanding human possibility, GuardLogix, Kinetix, Logix 5000, PanelView Plus, POINT Guard I/O, POINT I/O, Rockwell Automation, RSLinx, Stratix, Studio 5000, and Studio 5000 Logix Designer are trademarks of Rockwell Automation, Inc.

CIP Safety, CIP Sync, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## rockwellautomation.com

expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:（1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIAPACIFIC:RockwellAutomationSEAPteLtd,2CorporationRoad,#04-05,MainLobby,CorporationPlace,Singapore618494,Tel:(65)65106608 UNITEDKINGD0M:RockwellAutomationLtd.,Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)（1908)838-800