<!-- image -->

## MicroLogix 1500 Programmable Controllers

Bulletins 1764 Controllers and 1769 Expansion I/O

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

Preface

## Table of Contents

|                         | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9    |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                         | Purpose of this Manual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9     |
|                         | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                        |
|                         | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9      |
|                         | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9    |
|                         | Chapter 1                                                                                                                               |
| Hardware Overview       | Hardware Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11    |
|                         | Component Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |
|                         | Base Unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12    |
|                         | Processors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12     |
|                         | Memory Modules/Real-time Clock. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13                        |
|                         | Cables. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13  |
|                         | Programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 |
|                         | Communication Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14         |
|                         | Compact I/O Expansion Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                |
|                         | End Cap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15    |
|                         | Expansion Power Supply and Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                          |
|                         | System Requirements for Using Expansion Modules . . . . . . . . . . . . . . . . . . . . . . . . 15                                      |
|                         | Adding an I/O Bank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16           |
|                         | Address Expansion I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18              |
|                         | Expansion I/O Power Failure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                  |
|                         | Chapter 2                                                                                                                               |
| Install Your Controller | Installation Considerations . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21      |
|                         | Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21      |
|                         | Hazardous Location Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                         |
|                         | Disconnecting Main Power. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                  |
|                         | Safety Circuits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22       |
|                         | Power Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22           |
|                         | Periodic Tests of Master Control Relay Circuit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                             |
|                         | Power Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23       |
|                         | Isolation Transformers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23              |
|                         | Power Supply Inrush . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23            |
|                         | Loss of Power Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23              |
|                         | Input States on Power Down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                   |
|                         | Other Types of Line Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                   |
|                         | Help Prevent Excessive Heat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23           |
|                         | Master Control Relay. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24    |
|                         | Emergency Stop Switches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24                  |
|                         | Base Unit Mounting Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26              |
|                         | Controller and                                                                                                                          |
|                         | Expasion I/O Spacing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27     |
|                         | Mount the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27    |
|                         | DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28          |

|                           | Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           | Install Controller Components. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                                                                                                    |
|                           | Prevent Electrostatic Discharge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                                                                                                             |
|                           | Processor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                                                                                              |
|                           | Data Access Tool (DAT). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31                                                                                                       |
|                           | Memory Module/Real-time Clock. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32                                                                                                                |
|                           | Compact I/O Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                                                                                                      |
|                           | Chapter 3                                                                                                                                                                                                                        |
| Wire Your Controller      | Wiring Requirements . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   35                                                                                            |
|                           | Wiring Recommendation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                                                                                                           |
|                           | Wire without Spade Lugs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                                                                                                         |
|                           | Wire with Spade Lugs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                                                                                                      |
|                           | Use Surge Suppressors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                                                                                                 |
|                           | Recommended Surge Suppressors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38                                                                                                                    |
|                           | Ground the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38                                                                                              |
|                           | Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39                                                                                           |
|                           | Miswiring - 1764-28BXB Only . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39                                                                                                           |
|                           | Terminal Block Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                                                                                                        |
|                           | Terminal Groupings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                                                                                                      |
|                           | Sinking and Sourcing Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41                                                                                                            |
|                           | 1764-24AWA Wiring Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41                                                                                                             |
|                           | 1764-24BWA Wiring Diagram with Sinking Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . 42                                                                                                                           |
|                           | 1764-24BWA Wiring Diagram with Sourcing Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . 43                                                                                                                            |
|                           | 1764-28BXB Wiring Diagram with Sinking Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . 43                                                                                                                           |
|                           | 1764-28BXB Wiring Diagram with Sourcing Outputs . . . . . . . . . . . . . . . . . . . . . . . . . 44                                                                                                                             |
|                           | Controller I/O Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45                                                                                            |
|                           | Minimizing Electrical Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45                                                                                                         |
|                           | Transistor Output Transient Pulses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45                                                                                                                |
|                           | Chapter 4                                                                                                                                                                                                                        |
| Communication Connections | Default Communication Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47                                                                                                             |
|                           | Use the Communications Toggle Push Button . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47                                                                                                                   |
|                           | Connect to the RS-232 Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                                                                                                  |
|                           | DF1 Full-Duplex Communication Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                                                                                                                         |
|                           | Make a DF1 Point-to-Point Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                                                                                                                  |
|                           | Use a Modem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                                                                                                 |
|                           | Isolated Modem Connection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                                                                                            |
|                           | Connect to a DF1 Half-Duplex Network. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                                                                                                                   |
|                           | Connecting to a DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                                                                                                        |
|                           | DH-485 Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                                                                                                 |
|                           | Recommended Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                                                                                         |
|                           | DH-485 Communication Cable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                                                                                                               |
|                           | Ground and Terminate the DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                                                                                                                         |
|                           | Connect the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                                                                                            |
|                           | Cable Selection Guide. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                                                                                                      |
|                           | Recommended User-supplied Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60 Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61 |

|                           | Install and Attach the AIC+. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61              |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|                           | Power the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62        |
|                           | Connect to Ethernet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63     |
|                           | Ethernet Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63             |
|                           | RS-232 Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64            |
|                           | Chapter 5                                                                                                                              |
| Use Trimpots and the Data | Trimpot Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65   |
| Access Tool               | Trimpot Information Function File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                     |
|                           | Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66        |
|                           | Data Access Tool. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 |
|                           | DAT Keypad and Indicator Light Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                            |
|                           | Power-Up Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66            |
|                           | DAT Function File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67         |
|                           | Power Save Timeout (PST) Parameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                          |
|                           | Understanding the DAT Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                   |
|                           | Entering Bit Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68         |
|                           | Entering Integer Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68             |
|                           | Monitoring and Editing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69            |
|                           | F1 and F2 Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69           |
|                           | Working Screen Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69                |
|                           | Non-Existent Elements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70              |
|                           | Controller Faults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70       |
|                           | Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70        |
|                           | Chapter 6                                                                                                                              |
| Use Real-Time Clock and   | Real-Time Clock Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73         |
| Memory Modules            | Removal/Insertion Under Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73                     |
|                           | Real-Time Clock Function File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73                  |
|                           | Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73    |
|                           | Write Data to the Real-Time Clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                     |
|                           | RTC Battery Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74             |
|                           | Memory Module Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74         |
|                           | User Program and Data Back-Up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                       |
|                           | Program Compare. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74            |
|                           | Data File Download Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                   |
|                           | Memory Module Write Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                      |
|                           | Removal/Insertion Under Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                     |
|                           | Memory Module Information File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                     |
|                           | Appendix A                                                                                                                             |
| Specifications            | MicroLogix 1500 Controller Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77                  |
|                           | Choosing a Power Supply. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78                |
|                           | Controller Dimensions . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   83  |
|                           | Compact I/O Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83        |
|                           | Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83        |
|                           | End Cap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83   |

Appendix B

| Replacement Parts             | MicroLogix 1500 Replacement Kits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85                                                                                                                           |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                               | Lithium Battery (1747-BA) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85                                                                                                                    |
|                               | Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85                                                                                                               |
|                               | Battery Handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                                                                                                                     |
|                               | Storage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                                                                                                               |
|                               | Transportation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                                                                                                                    |
|                               | Disposal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87                                                                                                               |
|                               | Replacement Terminal Blocks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87                                                                                                                         |
|                               | Replacement Doors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88                                                                                                                  |
|                               | Appendix C                                                                                                                                                                                                                                          |
| Troubleshoot Your System      | Understand the Controller Status Indicators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                                                                                                                                 |
|                               | Normal Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90                                                                                                                       |
|                               | Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90                                                                                                                     |
|                               | Controller Error Recovery Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91                                                                                                                        |
|                               | Identifying Controller Faults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                                    |
|                               | Automatically Clearing Faults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                                              |
|                               | Manually Clearing Faults Using the Fault Routine . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                                                           |
|                               | Fault Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                                     |
|                               | Calling Rockwell Automation for Assistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                                                 |
|                               | Appendix D                                                                                                                                                                                                                                          |
| Upgrade Your Operating System | Prepare for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                                                        |
|                               | Install ControlFLASH Software. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                                                               |
|                               | Prepare the Controller for Firmware Update. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                                                                          |
|                               | Perform the Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                                                          |
|                               | Missing or Corrupt OS LED Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                                                          |
|                               | Appendix E                                                                                                                                                                                                                                          |
| Understand Communication      | RS-232 Communication Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                                                                                                                            |
| Protocols                     | DF1 Full-duplex Protocol. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                                                                                                                  |
|                               | DF1 Half-duplex Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                                                                                                                   |
|                               | DF1 Half-duplex Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                                                                                                            |
|                               | Considerations When Communicating as a DF1 Slave on a Multi-drop Link . . . . . 96                                                                                                                                                                  |
|                               | Use Modems with MicroLogix Programmable Controllers . . . . . . . . . . . . . . . . . . . . 96                                                                                                                                                      |
|                               | DH-485 Communication Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                                                                                                                            |
|                               | DH-485 Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                                                                    |
|                               | Devices that use the DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                                                                      |
|                               | Important DH-485 Network Planning Considerations. . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                                                                                  |
|                               | Modbus RTU Slave Communication Protocol. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101                                                                                                                                      |
|                               | ASCII Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                                                                                                            |
|                               | Appendix F                                                                                                                                                                                                                                          |
| System Loading and Heat       | System Loading Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                                                                                                                         |
| Dissipation                   | System Expansion Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 Select System Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 |

| Verify the System Loading. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                         |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| Calculating Heat Dissipation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                 |
| Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111       |
| Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . 115 |

## Notes:

## About This Publication

## Purpose of this Manual

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

## Additional Resources

## Additional Resources

|                                                                                                                       | Resource Description                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 | Provides information on the MicroLogix 1200 and MicroLogix 1500 controllers instruction set.           |
| AIC+ Advanced Interface Converter User Manual, publication 1761-UM004                                                 | Describes how to install and connect an AIC+. This manual also contains information on network wiring. |
| MicroLogix Ethernet Interface User Manual, publication 1761-UM006                                                     | Provides information on how to install, configure, and commission an EtherNet/IP™ Interface (ENI).     |
| DeviceNet Interface User Manual, publication 1761-UM005                                                               | Provides information on how to install, configure, and commission a DeviceNet® Interface (DNI).        |
| Compact I/O Modules Specifications Technical Data, publication 1769-TD006                                             | Provides information and specifications on Compact I/O modules.                                        |
| CompactLogix Communication Modules Specifications Technical Data, publication 1769-TD007                              | Provides information and specifications on CompactLogix™ and Compact I/O communication modules.        |
| CompactLogix Power Supplies Specifications Technical Data, publication 1769-TD008                                     | Provides information and specifications on CompactLogix and Compact I/O power supplies.                |
| Compact I/O Analog Modules User Manual, publication 1769-UM002                                                        | Provides detailed information on installing, configuring, and using Compact I/O analog modules.        |

Use this manual if you are responsible for designing, installing, programming, or troubleshooting control systems that use MicroLogix™ 1500 controllers.

You should have a basic understanding of electrical circuitry and familiarity with relay logic. If you do not, obtain the proper training before using this product.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This manual is a reference guide for MicroLogix 1500 controllers and 1769 expansion I/O. It describes the procedures that you use to install, wire, and troubleshoot your controller. This manual:

- Explains how to install and wire your controllers
- Gives you an overview of the MicroLogix 1500 controller system

See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for the MicroLogix 1200 and 1500 instruction set and for application examples to show the instruction set in use. See your programming software user documentation for more information on programming your MicroLogix 1500 controller.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic  Page                               |
|-------------------------------------------|
| Added Inclusive Language Acknowledgment 9 |
| Updated Environmental Specifications 77   |
| Updated Certifications 78                 |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

## Additional Resources (Continued)

|                                                                                                                    | Resource Description                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compact I/O Thermocouple/mV Input Module User Manual, publication 1769-UM004                                       | Provides detailed information on installing, configuring, and using 1769-IT6 Thermocouple/ mV Input modules.                                                                                                                                                                    |
| Compact I/O RTD/Resistance Input Module User Manual, publication 1769-UM005                                        | Provides detailed information on installing, configuring, and using 1769-IR6 RTD/Resistance Input modules.                                                                                                                                                                      |
| Compact High-speed Counter Module User Manual, publication 1769-UM006                                              | Provides detailed information on installing, configuring, and using 1769-HSC high-speed counter modules.                                                                                                                                                                        |
| 1769-SDN DeviceNet Scanner Module User Manual, publication 1769-UM009                                              | Provides detailed information on installing, configuring, and using a 1769-SDN DeviceNet scanner module.                                                                                                                                                                        |
| DF1 Protocol and Command Set Reference Manual, publication 1770-6.5.16                                             | Provides information about the DF1 open protocol.                                                                                                                                                                                                                               |
| Modbus Protocol Specifications, available from modbus.org                                                          | Provides information about the Modbus protocol.                                                                                                                                                                                                                                 |
| EtherNet/IP Network Devices User Manual, publication ENET-UM006                                                    | Describes how to configure and use EtherNet/IP devices to communicate on the EtherNet/IP network.                                                                                                                                                                               |
| Ethernet Reference Manual, publication ENET-RM002                                                                  | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                                                                      |
| System Security Design Guidelines Reference Manual, publication SECURE-RM001                                       | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                                                                   |
| UL Standards Listing for Industrial Control Products, publication CMPNTS-SR002                                     | Assists original equipment manufacturers (OEMs) with construction of panels, to help ensure that they conform to the requirements of Underwriters Laboratories.                                                                                                                 |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications                                                            | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

## Hardware Features

## Hardware Overview

The MicroLogix 1500 programmable controller is composed of a base unit, which contains a power supply, input and output circuits, and a processor. The controller is available with 24 or 28 points of embedded I/O. Additional I/O may be added using Compact I/O™ modules.

Figure 1 - Controller Hardware Features

<!-- image -->

## Controller Description

|                                                       | Description Description                         |
|-------------------------------------------------------|-------------------------------------------------|
| 1 Removable terminal blocks 7                         | Memory module/Real-time clock(1)                |
| 2 Interface to expansion I/O, removable ESD barrier 8 | Replacement battery(1)                          |
| 3 Input indicators 9 Battery                          |                                                 |
|                                                       | 4 Output indicators 10 Terminal doors and label |
| 5 Communication port 11                               | Data access tool(1)                             |
|                                                       | 6 Status indicators 12 Mode switch, trimpots    |

## Component Descriptions

<!-- image -->

A MicroLogix 1500 controller is composed of a processor (1764-LSP or enhanced 1764-LRP with RS-232 port) and a base unit. The FET transistor outputs are available on the 1764-28BXB base unit only.

## Base Unit

<!-- image -->

Figure 2 - Base Unit Hardware Features

| Catalog Number    |                        |                                 |                                                                                        | Line Power Inputs Outputs High Speed I/O   |
|-------------------|------------------------|---------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------|
|                   |                        |                                 | 1764-24AWA 120/240V AC 12 120V AC 12 relays, 2 isolated relays per unit Not applicable |                                            |
|                   | 1764-24BWA 120/240V AC | 8 standard 24V DC 4 fast 24V DC | 12 relays, 2 isolated relays per unit 4 20 kHz input                                   |                                            |
| 1764-28BXB 24V DC |                        | 8 standard 24V DC 8 fast 24V DC | 6 relays, 2 isolated relays per unit 4 standard 24V DC FET 2 fast 24V DC FET           | 8 20 kHz input 2 20 kHz output             |

## Processors

Figure 3 - Processor – 1764-LSP

<!-- image -->

Figure 5 - Data Access Tool – 1764-DAT

<!-- image -->

1764-DAT mounted on 1764-LSP processor

## Memory Modules/Real-time Clock

Figure 6 - Memory Module Mounted on the 1764-LSP Processor

Table 1 lists the available memory modules and real-time clock modules.

<!-- image -->

Table 1 - Memory Modules and Real-time Clocks

| Catalog Number Description Memory Size   |                                                  |
|------------------------------------------|--------------------------------------------------|
|                                          | 1764-RTC Real-time clock Not applicable          |
|                                          | 1764-MM1 Memory module 8K                        |
|                                          | 1764-MM1RTC Memory module and real-time clock 8K |
| 1764-MM2(1)                              | Memory module 16K                                |
| 1764-MM2RTC(1)                           | Memory module and real-time clock 16K            |
| 1764-MM3(2)                              | Memory module 16K                                |
| 1764-MM3RTC(2)                           | Memory module and real-time clock 16K            |

## Cables

Use only the communication cables that are listed in Table 2 in Class I Division 2 hazardous environment.

## Programming

Table 2 - Cables for Use in Class I Division 2 Hazardous Environment

| Catalog Number Catalog Number                                 |
|---------------------------------------------------------------|
| 1761-CBL-PM02, series C or later 2707-NC8, series B or later  |
| 1761-CBL-HM02, series C or later 2707-NC9, series B or later  |
| 1761-CBL-AM00, series C or later 2707-NC10, series B or later |
| 1761-CBL-AP00, series C or later 2707-NC11, series B or later |
| 1761-CBL-PH02, series A or later —                            |
| 1761-CBL-AH02, series A or later —                            |

Program the MicroLogix 1500 controller using RSLogix 500® software, version 4.00.00 or later. Certain features are only available when using the most current version of the software, as specified in System Requirements for Using Expansion Modules on page 15 .

Table 3 lists the firmware release numbers, feature and functionality enhancements, and the required version of RSLogix 500 Starter software.

Table 3 - Required Software Version by FRN Number

| Controller   | Firmware Release                | Available for Sale Date           | Catalog Number Series Catalog Number Revision   | OS FRN Number   | Feature and Functionality Changes                                                                                                                                                  | Required Version of RSLogix 500/ RSLogix 500 Starter Software   |
|--------------|---------------------------------|-----------------------------------|-------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 1764-LSP     |                                 | Initial Release February 1999 A B |                                                 |                 | 2 Initial Release                                                                                                                                                                  | 3.01.00                                                         |
| 1764-LSP     | Enhancement October 1999 A C    |                                   |                                                 |                 | 3 Power Supply and Expansion Cable Compatibility 3.01.00                                                                                                                           |                                                                 |
| 1764-LSP     | Series B Release March 2000 B A |                                   |                                                 | 4               | String Data File Type, ASCII Instruction Set, Modbus RTU Slave Protocol, Ramping (when using PWM outputs), Static Data File Protection, RTC Messaging                              | 4.00.00                                                         |
| 1764-LSP     |                                 | Enhancement October 2000 B B      |                                                 | 5               | PTO Controlled Stop, Memory Module Program Compare Bit Enhancement                                                                                                                 | 4.50.00                                                         |
| 1764-LSP     | Series C Release                | September 2001                    | C A                                             | 6               | Floating Point Data File Support, Programmable Limit Switch (PLS), Real Time Clock Adjust (Copy Word), Absolute Value, Gray Code, Recipe, Message Instruction Support for 1769-SDN | 5.10.00                                                         |
| 1764-LRP     | Initial Release March 2000 B A  |                                   |                                                 |                 | 4 Initial Release - Same Functionality as 1764-LSP                                                                                                                                 | 4.00.00                                                         |
| 1764-LRP     |                                 | Enhancement October 2000 B B      |                                                 | 5               | PTO Controlled Stop, Memory Module Program Compare Bit Enhancement                                                                                                                 | 4.50.00                                                         |
|              | Series C Release                | September 2001                    | C A                                             | 6               | Floating Point Data File Support, Programmable Limit Switch (PLS), Real Time Clock Adjust (Copy Word), Absolute Value, Gray Code, Recipe, Message Instruction Support for 1769-SDN | 5.10.00                                                         |

## Communication Options

The MicroLogix 1500 controller can be connected to a personal computer. It can also be connected to the DH-485 network with an Advanced Interface Converter (1761-NET-AIC), to an Ethernet network with an Ethernet Interface (1761-NET-ENI), or to a DeviceNet network with a DeviceNet Scanner module (1769-SDN). The controller can also be connected to Modbus SCADA networks as an RTU slave. See Communication Connections on page 47 for more information on connecting to the available communication options.

The 1764-LRP processor provides an additional communication port. Each of the communication ports can be independently configured for any supported communication protocol. Channel 0 is on the base unit and Channel 1 is on the 1764-LRP processor.

## Compact I/O Expansion Modules

Compact I/O expansion modules (Bulletin 1769) can be connected to the MicroLogix 1500 controller. A maximum of either 8 or 16 expansion I/O modules can be used, depending upon your system. See System Requirements for Using Expansion Modules on page 15 .

See System Loading and Heat Dissipation on page 103 for more information on system configurations.

## End Cap

An end cap terminator (1769-ECR or 1769-ECL) must be used at the end of the group of I/O modules attached to the MicroLogix 1500 controller. The end cap terminator is not provided with the base or processor units. It is required when using expansion I/O modules.

Figure 7 shows the right end cap (1769-ECR). The left end cap (1769-ECL) is shown in Figure 8 .

Figure 7 - Add an End Cap

<!-- image -->

## Expansion Power Supply and Cables

With Operating System Firmware Revision Number (FRN) 3 or later, you can connect an additional bank of I/O to your controller. Using an expansion power supply increases the system's capacity for adding expansion I/O modules. The additional I/O bank is connected to the controller with a specially designed cable. The additional I/O bank must include a power supply and an end cap.

<!-- image -->

Depending on the system configuration, each controller can support up to 16 expansion I/O modules. See the System Requirements for Using Expansion Modules below. Also see System Guidelines on page 16 for system limitations and illustrations of expansion I/O banks.

## System Requirements for Using Expansion Modules

To support a maximum of 8 I/O modules in an additional I/O bank, you must have the following:

Table 4 - Requirements to Support a Maximum of 8 I/O Modules

|                           | Product Catalog Number or Software Version                                                      | Product Catalog Number or Software Version                                                      |
|---------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| MicroLogix 1500 Processor | 1764-LSP, series A, revision C or later 1764-LSP, series B or later 1764-LRP, series B or later | 1764-LSP, series A, revision C or later 1764-LSP, series B or later 1764-LRP, series B or later |
| MicroLogix 1500 Base Unit | 1764-24AWA, series A or later 1764-24BWA, series A or later 1764-28BXB, series A or later       | 1764-24AWA, series A or later 1764-24BWA, series A or later 1764-28BXB, series A or later       |
| Operating System Version  | Firmware revision number (FRN) 3 or later(1)                                                    | Firmware revision number (FRN) 3 or later(1)                                                    |
| Programming Software      |                                                                                                 | 1764-LSP, series A RSLogix 500, version 3.01.09 or later                                        |
| Programming Software      | 1764-LSP, series B 1764-LRP, series B                                                           | RSLogix 500, version 4.00.00 or later                                                           |
| Programming Software      | 1764-LSP, series C 1764-LRP, series C                                                           | RSLogix 500, version 5.00.00 or later                                                           |

Table 4 - Requirements to Support a Maximum of 8 I/O Modules (Continued)

| Product Catalog Number or Software Version                       |
|------------------------------------------------------------------|
| 1 Power Supply (optional)  1769-PA2, 1769-PA4 1769-PB2, 1769-PB4 |
| 1 Cable (optional) 1769-CRL1, 1769-CRL3, 1769-CRR1, 1769-CRR3    |
| 1 End Cap (required) 1769-ECL, 1769-ECR                          |

To support a maximum of 16 I/O modules in an additional I/O bank, you must have the following:

Table 5 - Requirements to Support a Maximum of 16 I/O Modules

| Product Catalog Number or Software Version                                                                          |
|---------------------------------------------------------------------------------------------------------------------|
| MicroLogix 1500 Processor  1764-LSP, series C or later 1764-LRP, series C or later                                  |
| MicroLogix 1500 Base Unit 1764-24AWA, series B or later 1764-24BWA, series B or later 1764-28BXB, series B or later |
| Operating System Version  Firmware revision number (FRN) 6 or later(1)                                              |
| Programming Software RSLogix 500, version 5.10.00 or later                                                          |
| 1 Power Supply (optional) 1769-PA2, 1769-PA4, 1769-PB2, 1769-PB4                                                    |
| 1 Cable (optional) 1769-CRL1, 1769-CRL3, 1769-CRR1, 1769-CRR3                                                       |
| 1 End Cap (required) 1769-ECL, 1769-ECR                                                                             |

## IMPORTANT

If your processor is at an older revision, you must upgrade the operating system to FRN 3 or later to use an expansion cable and power supply (or to FRN 6 or later to allow up to 16 expansion modules). Go to rok.auto/pcdc to download the operating system upgrade.

MicroLogix 1500 base units are not field upgradeable from series A to series B.

## Adding an I/O Bank

System Guidelines

A maximum of one 1769 expansion cable can be used in a MicroLogix 1500 system, allowing for two banks of I/O modules (one connected directly to the controller and the other connected with the cable). Each I/O bank requires its own power supply (bank 1 uses the controller's embedded power supply).

<!-- image -->

## ATTENTION: LIMIT OF ONE EXPANSION POWER SUPPLY

The expansion power supply cannot be connected directly to the controller. It must be connected using an expansion cable. Only one power supply (embedded in the base unit or an expansion power supply) may be used on an I/O bank. Exceeding these limitations may damage the power supply and result in unexpected operation.

<!-- image -->

## ATTENTION: REMOVE POWER

Remove system power before making or breaking cable connections. When you remove or insert a cable connector with power applied, an electric arc may occur. An electric arc can cause personal injury or property damage by:

- Sending an erroneous signal to your system's field devices, causing unintended machine operation
- Causing an explosion in a hazardous environment

Electrical arcing causes excessive wear to contacts on both the module and its mating connector.

See your power supply and I/O module's documentation for instructions on how to set up your system.

## IMPORTANT

See the System Requirements for Using Expansion Modules on page 15 to determine the maximum number of expansion I/O modules you can use in your MicroLogix system.

Also see System Loading and Heat Dissipation on page 103 for more information on system configurations.

Figure 8 and Figure 9 show a MicroLogix 1500 controller with an expansion I/O bank.

Figure 8 - Vertical Orientation

<!-- image -->

- (1) The x in this catalog number can be either a 1 or a 3 representing the length of the cable: 1 = 1 ft. (0.305 m) and 3 = 3.28 ft. (1 m)

Figure 9 - Horizontal Orientation

<!-- image -->

- (1) The x in this catalog number can be either a 1 or a 3 representing the length of the cable: 1 = 1 ft. (0.305 m) and 3 = 3.28 ft. (1 m)

## Address Expansion I/O

The expansion I/O is addressed as slots 1…16 (the controller's embedded I/O is addressed as slot 0). Power supplies and cables are not counted as slots. Modules are counted from left to right on each bank as shown in Figure 10 and Figure 11. For more information on addressing, see the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

Figure 10 - Vertical Orientation

<!-- image -->

Figure 11 - Horizontal Orientation

<!-- image -->

## Expansion I/O Power Failure

Expansion I/O errors represent failures of the I/O bus or the modules themselves. The error codes are listed in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

## Notes:

## Installation Considerations

## Safety Considerations

## Install Your Controller

Most applications require installation in an industrial enclosure (Pollution Degree 2(a)) to reduce the effects of electrical interference (Over Voltage Category II (b) ) and environmental exposure. Locate your controller as far as possible from power lines, load lines, and other sources of electrical noise such as hard-contact switches, relays, and AC motor drives. For more information on proper grounding guidelines, see the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

<!-- image -->

<!-- image -->

ATTENTION: Vertical mounting of the controller is not recommended due to heat build-up considerations.

ATTENTION: Be careful of metal chips when drilling mounting holes for your controller or other equipmet within the enclosure or panel. Drilled fragments that fall into the base or processor unit could cause damage. Do not drill holes above a mounted controller if the protective debris strips are removed or the processor is installed.

Safety considerations are an important element of proper system installation. Actively thinking about the safety of yourself and others, as well as the condition of your equipment, is of primary importance. We recommend reviewing the following safety considerations.

## Hazardous Location Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D or non-hazardous locations only. The following WARNING statement applies to use in hazardous locations.

<!-- image -->

## ATTENTION: EXPLOSION HAZARD

- Substitution of components may impair suitability for Class I Division 2.
- Do not replace components or disconnect equipment unless power has been switched off.
- Do not connect or disconnect components unless power has been switched off, or the area is known to be non-hazardous.
- This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.
- All wiring must comply with N.E.C. article 501-4(b).
- The interior of the enclosure must be accessible only by the use of a tool.
- For applicable equipment (for example, relay modules), exposure to some chemicals may degrade the sealing properties of the materials used in these devices:
- Relays, epoxy

It is recommended that you periodically inspect these devices for any degradation of properties and replace the module if degradation is found.

(a) Pollution Degree 2 is an environment where normally only non-conductive pollution occurs except that occasionally temporary conductivity caused by condensation shall be expected.

(b) Overvoltage Category II is the load level section of the electrical distribution system. At this level transient voltages are controlled and do not exceed the impulse voltage capability of the products insulation.

<!-- image -->

<!-- image -->

ATTENTION: When installing any peripheral device (for example, push buttons, lamps) into a hazardous environment, ensure that they are Class I Division 2 certified, or determined to be safe for the environment.

Use only the communication cables that are listed in Table 6 in Class I Division 2 hazardous locations.

Table 6 - Communication Cables for Class I Division 2 Hazardous Location

| Catalog Number Catalog Number                                 |
|---------------------------------------------------------------|
| 1761-CBL-PM02, series C or later 2707-NC8, series A or later  |
| 1761-CBL-HM02, series C or later 2707-NC9, series B or later  |
| 1761-CBL-AM00, series C or later 2707-NC10, series B or later |
| 1761-CBL-AP00, series C or later 2707-NC11, series B or later |
| 1761-CBL-PH02, series A or later —                            |
| 1761-CBL-AH02, series A or later —                            |

## Disconnecting Main Power

<!-- image -->

## ATTENTION: EXPLOSION HAZARD

Do not replace components or disconnect equipment unless power has been switched off.

The main power disconnect switch should be located where operators and maintenance personnel have quick and easy access to it. In addition to disconnecting electrical power, all other sources of power (pneumatic and hydraulic) should be de-energized before working on a machine or process that is controlled by a controller.

## Safety Circuits

<!-- image -->

## ATTENTION: EXPLOSION HAZARD

Do not connect or disconnect connectors while circuit is live.

Circuits installed on the machine for safety reasons, like overtravel limit switches, stop push buttons, and interlocks, should always be hard-wired directly to the master control relay. These devices must be wired in series so that when any one device opens, the master control relay is de-energized, which removes power to the machine. Never alter these circuits to defeat their function. Serious injury or machine damage could result.

## Power Distribution

There are some points about power distribution that you should know:

- The master control relay must be able to inhibit all machine motion by removing power to the machine I/O devices when the relay is de-energized. It is recommended that the controller remain powered even when the master control relay is de-energized.
- If you are using a DC power supply, interrupt the load side rather than the AC line power. This avoids the additional delay of power supply turn-off. The DC power supply should be powered directly from the fused secondary of the transformer. Power to the DC input and output circuits should be connected through a set of master control relay contacts.

## Periodic Tests of Master Control Relay Circuit

Any part can fail, including the switches in a master control relay circuit. The failure of one of these switches would most likely cause an open circuit, which is a safe power-off failure. However, if one of these switches shorts out, it no longer provides any safety protection. These switches should be tested periodically to assure they will stop machine motion when needed.

## Power Considerations

## Help Prevent Excessive Heat

The following explains power considerations for the micro controllers.

## Isolation Transformers

Consider using an isolation transformer in the AC line to the controller. This type of transformer provides isolation from your power distribution system to reduce the electrical noise that enters the controller and is often used as a step-down transformer to reduce line voltage. Any transformer that is used with the controller must have a sufficient power rating for its load. The power rating is expressed in voltamperes (VA).

## Power Supply Inrush

During power-up, the MicroLogix 1500 power supply allows a brief inrush current to charge internal capacitors. Many power lines and control transformers can supply inrush current for a brief time. If the power source cannot supply this inrush current, the source voltage could sag momentarily.

The only effect of limited inrush current and voltage sag on the MicroLogix 1500 controller is that the power supply capacitors charge more slowly. However, consider the effect of a voltage sag on other equipment. For example, a deep voltage sag could reset a computer that is connected to the same power source. The following considerations determine whether the power source is required to supply high inrush current:

- The power-up sequence of devices in a system
- The amount of the power source voltage sag if the inrush current cannot be supplied
- The effect of voltage sag on other equipment in the system

If the entire system is powered-up simultaneously, a brief sag in the power source voltage typically does not affect any equipment.

## Loss of Power Source

The power supply is designed to withstand brief power losses without affecting the operation of the system. The time that the system is operational during power loss is called program scan hold-up time after loss of power. The duration of the power supply hold-up time depends on the type and state of the I/O, but is typically between 10 milliseconds and 3 seconds. When the duration of power loss reaches this limit, the power supply signals the processor that it can no longer provide adequate DC power to the system. This is referred to as a power supply shutdown. The processor then performs an orderly shutdown of the controller.

## Input States on Power Down

The power supply hold-up time that is described previously is longer than the turn-on and turn-off times of the inputs. Because of this, the input state change from On to Off that occurs when power is removed could be recorded by the processor before the power supply shuts down the system. Understanding this concept is important. The user program should be written to take this effect into account.

## Other Types of Line Conditions

Occasionally the power source to the system can be temporarily interrupted. It is also possible that the voltage level drops substantially below the normal line voltage range for a period of time. Both of these conditions are considered to be a loss of power for the system.

For most applications, normal convective cooling keeps the controller within the specified operating range. Confirm that the specified temperature range is maintained. Proper spacing of components within an enclosure is usually sufficient for heat dissipation.

## Master Control Relay

In some applications, a substantial amount of heat is produced by other equipment inside or outside the enclosure. In this case, place blower fans inside the enclosure to help with air circulation and to reduce hot spots near the controller.

Additional cooling provisions might be necessary when high ambient temperatures are encountered.

<!-- image -->

Do not bring in unfiltered outside air. Place the controller in an enclosure to protect it from a corrosive atmosphere. Harmful contaminants or dirt could cause improper operation or damage to components. In extreme cases, you can use air conditioning to protect against heat build-up within the enclosure.

A hard-wired master control relay (MCR) provides a reliable means for emergency machine shutdown. Since the master control relay allows the placement of several emergency stop switches in different locations, its installation is important from a safety standpoint. Overtravel limit switches or mushroom-head push buttons are wired in series so that when any of them opens, the master control relay is de-energized. This removes power to input and output device circuits. See Figure 12 and Figure 13 .

<!-- image -->

ATTENTION: Never alter these circuits to defeat their function since serious injury and/or machine damage could result.

<!-- image -->

If you are using an external DC power supply, interrupt the DC output side rather than the AC line side of the supply to avoid the additional delay of power supply turn-off.

The AC line of the DC output power supply should be fused.

Connect a set of master control relays in series with the DC power supplying the input and output circuits.

Place the main power disconnect switch where operators and maintenance personnel have quick and easy access to it. If you mount a disconnect switch inside the controller enclosure, place the switch operating handle on the outside of the enclosure, so that you can disconnect power without opening the enclosure.

Whenever any of the emergency stop switches are opened, power to input and output devices should be removed.

When you use the master control relay to remove power from the external I/O circuits, power continues to be provided to the controller's power supply so that diagnostic indicators on the processor can still be observed.

The master control relay is not a substitute for a disconnect to the controller. It is intended for any situation where the operator must quickly de-energize I/O devices only. When inspecting or installing terminal connections, replacing output fuses, or working on equipment within the enclosure, use the disconnect to shut off power to the rest of the system.

<!-- image -->

Do not control the master control relay with the controller. Provide the operator with the safety of a direct connection between an emergency stop switch and the master control relay.

## Emergency Stop Switches

When using emergency stop switches, adhere to the following points:

- Do not program emergency stop switches in the controller program. Any emergency stop switch should turn off all machine power by turning off the master control relay.
- Observe all applicable local codes concerning the placement and labeling of emergency stop switches.

- Install emergency stop switches and the master control relay in your system. Verify that relay contacts have a sufficient rating for your application. Emergency stop switches must be easy to reach.
- In the following illustration, input and output circuits are shown with MCR protection. However, in most applications, only output circuits require MCR protection.

Figure 12 and Figure 13 show the master control relay wired in a grounded system.

<!-- image -->

In most applications, input circuits do not require MCR protection; however, if you must remove power from all field devices, you must include MCR contacts in series with input power wiring.

Figure 12 - Schematic (Using IEC Symbols)

<!-- image -->

Figure 13 - Schematic (Using ANSI/CSA Symbols)

<!-- image -->

## Base Unit Mounting Dimensions

<!-- image -->

Figure 14 - Base Unit Dimensions

| Dimension(1)   |                                                                         | 1764-24AWA 1764-24BWA 1764-28BXB                                        |                                                                         |
|----------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Height (A)     | 118 mm (4.65 in.) – DIN latch closed 138 mm (5.43 in.) – DIN latch open | 118 mm (4.65 in.) – DIN latch closed 138 mm (5.43 in.) – DIN latch open | 118 mm (4.65 in.) – DIN latch closed 138 mm (5.43 in.) – DIN latch open |
|                | Width (B) 168 mm (6.62 in.)                                             | Width (B) 168 mm (6.62 in.)                                             | Width (B) 168 mm (6.62 in.)                                             |
|                | Depth (C) 87 mm (3.43 in.)                                              | Depth (C) 87 mm (3.43 in.)                                              | Depth (C) 87 mm (3.43 in.)                                              |

(1) See Controller Dimensions on page 83 for more dimensional information.

## Controller and Expasion I/O Spacing

## Mount the Controller

The base unit is designed to be mounted horizontally, with the Compact I/O expansion modules extending to the right of the base unit. Allow 50 mm (2 in.) minimum of space on all sides for adequate ventilation. Maintain spacing from enclosure walls, wireways, adjacent equipment, and so on, as shown in Figure 15 .

Figure 15 - Controller and Expansion I/O Spacing

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Do not remove protective debris strips until after the base and all other equipment in the panel near the base is mounted and wiring is complete. The debris strips are there to prevent drill fragments, wire strands and other dirt from getting into the controller. Once wiring is complete, remove protective debris strips and install processor unit. Failure to remove strips before operating can cause overheating.

<!-- image -->

ATTENTION: Be careful of metal chips when drilling mounting holes for your controller or other equipment within the enclosure or panel. Drilled fragments that fall into the controller could cause damage. Do not drill holes above a mounted controller if the protective debris strips have been removed.

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the base unit. Do not touch the connector pins or other sensitive areas.

<!-- image -->

If additional I/O modules are required for the application, remove the ESD barrier to install expansion I/O modules. A maximum of 16 I/O modules may be connected to the base (see System Requirements for Using Expansion Modules on page 15). The I/O module's current requirements and power consumption may further limit the number of modules connected to the base. See System Loading and Heat Dissipation on page 103. An end cap terminator (1769-ECR or 1769-ECL) is required at the end of the group of I/O modules attached to the base.

## DIN Rail Mounting

The base unit and expansion I/O DIN rail latches lock in the open position so that an entire system can be easily attached to or removed from the DIN rail. The maximum extension of the latch is 15 mm (0.67 in.) in the open position. A screwdriver is required for removal of the base unit. The base can be mounted to EN 50022 - 35 x 7.5 or EN 50022 - 35 x 15 DIN rails. DIN rail mounting dimensions are shown in Figure 16 .

<!-- image -->

Figure 16 - DIN Rail Mounting Dimensions

| Dimension Height   |                                                                            |
|--------------------|----------------------------------------------------------------------------|
| A                  | 118 mm (4.65 in.) – DIN latch closed 138 mm (5.43 in.) – DIN latch open    |
|                    | B 47.6 mm (1.875 in.)                                                      |
| C                  | 47.6 mm (1.875 in.) – DIN latch closed 54.7 mm (2.16 in.) – DIN latch open |

To install your base unit on the DIN rail, do as follows:

1. Mount your DIN rail. Make sure that the placement of the base unit on the DIN rail meets the recommended spacing requirements. See Controller and Expasion I/O Spacing on page 27 .
2. Hook the top slot over the DIN rail.
3. While pressing the base unit down against the top of the rail, snap the bottom of the base unit into position. Ensure DIN latches are in the up (secured) position.
4. Leave the protective debris strip attached until you are finished wiring the base unit and any other devices.

To remove your base unit from the DIN rail:

1. Place a flat-blade screwdriver in the DIN rail latch at the bottom of the base unit.
2. Holding the base unit, pry downward on the latch until the latch locks in the open position.
3. Repeat steps 1 and 2 for the second DIN rail latch. This releases the base unit from the DIN rail.
4. Unhook the top of the DIN rail slost from the rail.

Rockwell Automation Publication 1764-UM001D-EN-P - May 2024

<!-- image -->

## Install Controller Components

## Panel Mounting

Mount to panel using #8 or M4 screws. To install your base unit using mounting screws:

1. Secure the template to the mounting surface. Make sure that your base unit is spaced properly. See Controller and Expasion I/O Spacing on page 27 .
2. Drill holes through the template.
3. Remove the mounting template.
4. Mount the base unit.
5. Leave the protective debris strips attached until you are finished wiring the base unit and any other devices.

<!-- image -->

## Prevent Electrostatic Discharge

<!-- image -->

ATTENTION: Electrostatic discharge can damage integrated circuits or semiconductors if you touch bus connector pins. Follow these guidelines when you handle any module:

- Touch a grounded object to discharge static potential.
- Wear an approved wrist-strap grounding device.
- Do not touch the bus connector or connector pins.
- Do not touch circuit components inside the module.
- If available, use a static-safe work station.

When not in use, keep the module in its static-shield bag.

<!-- image -->

ATTENTION: Be sure the base unit is free of all metal fragments before removing protective debris strips and installing the processor unit. Failure to remove strips before operating can cause overheating.

## Processor

<!-- image -->

To install the processor, do as follows:

1. Make sure that the base unit power is off.
2. Slide the processor into the base unit using the guide rails for alignment.
3. Push until a click is heard. Be careful not to push on the connector when you install the 1764-LRP processor.

## IMPORTANT

It is critical that the processor is fully engaged and locked into place.

4. Make sure the actuator is pushed to the close position.
5. To remove the processor from the base unit, make sure base unit power is off. Push the actuator to the open position until the processor is ejected slightly. Once the processor has been ejected, it can be removed from the base unit.

<!-- image -->

<!-- image -->

## Data Access Tool (DAT)

To install the DAT, do as follows:

1. Remove the cover from the processor.
2. Hold the DAT in the proper orientation (as shown below) and place the DAT onto the processor. Align the DAT port on the processor with the plug on the DAT.
3. Firmly seat DAT on processor; make sure it seats into place.
4. To remove DAT, grasp using finger areas and pull upward.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Memory Module/Real-time Clock

To install the memory module or real-time clock, do as follows:

1. Remove the cover (or DAT if installed) from the processor.

<!-- image -->

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the base and processor units. Do not touch the connector pins or other sensitive areas.

<!-- image -->

2. Align connector on the memory module with the connector pins on the processor.
3. Firmly seat the memory module in the processor making sure the locking tabs click into place.
4. Replace the cover (or DAT if used).

<!-- image -->

<!-- image -->

<!-- image -->

## Compact I/O Module

Attach and Lock Module (Module-to-Controller or Module-to-Module)

A Compact I/O module can be attached to the controller or an adjacent I/O module before or after mounting to the panel or DIN rail. The module can be detached and replaced while the system is mounted to a panel or DIN rail.

<!-- image -->

<!-- image -->

ATTENTION: Remove power before removing or inserting an I/O module. When you remove or insert a module with power applied, an electrical arc may occur. An electrical arc can cause personal injury or property damage by:

- Sending an erroneous signal to your system's field devices, causing the controller to fault
- Causing an explosion in a hazardous environment

Electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance, reducing product reliability.

ATTENTION: When attaching I/O modules, it is very important that they are securely locked together to ensure proper electrical connection.

<!-- image -->

To attach and lock modules:

<!-- image -->

Remove the ESD barrier when attaching I/O modules to a MicroLogix 1500 base unit.

1. Disconnect power.
2. Check that the bus lever of the module to be installed is in the unlocked (fully right) position.
3. Use the upper and lower tongue-and-groove slots (1) to secure the modules together (or to a controller).
4. Move the module back along the tongue-and-groove slots until the bus connectors (2) line up with each other.
5. Push the bus lever back slightly to clear the positioning tab (3). Use your fingers or a small screw driver.
6. To allow communication between the controller and module, move the bus lever fully to the left (4) until it clicks. Ensure it is locked firmly in place.

<!-- image -->

ATTENTION: When attaching I/O modules, it is very important that the bus connectors are securely locked together to ensure proper electrical connection.

7. Attach an end cap terminator (5) to the last module in the system by using the tongueand-groove slots as before.

8. Lock the end cap bus terminator (6).

## IMPORTANT

A 1769-ECR right end cap (or a 1769-ECL left end cap if I/O bank is located below the controller) must be used to terminate the end of the serial communication bus.

See Controller Dimensions on page 83 for mounting dimensions.

## Wiring Requirements

## Wire Your Controller

## Wiring Recommendation

<!-- image -->

ATTENTION: Before you install and wire any device, disconnect power to the controller system.

<!-- image -->

ATTENTION: Calculate the maximum possible current in each power and common wire. Observe all electrical codes dictating the maximum current allowable for each wire size. Current above the maximum ratings may cause wiring to overheat, which can cause damage.

United States Only: If the controller is installed within a potentially hazardous environment, all wiring must comply with the requirements stated in the National Electrical Code 501-4 (b).

- Allow for at least 50 mm (2 in.) between I/O wiring ducts or terminal strips and the controller.
- Route incoming power to the controller by a path separate from the device wiring. Where paths must cross, their intersection should be perpendicular.

<!-- image -->

Do not run signal or communications wiring and power wiring in the same conduit. Wires with different signal characteristics should be routed by separate paths.

- Separate wiring by signal type. Bundle wiring with similar electrical characteristics together.
- Separate input wiring from output wiring.
- Label wiring to all devices in the system. Use tape, shrink-tubing, or other dependable means for labeling purposes. In addition to labeling, use colored insulation to identify wiring based on signal characteristics. For example, you may use blue for DC wiring and red for AC wiring.

## Table 7 - Wire Requirements

| Wire Type               | Wire Size(1)   | Wiring Torque             |
|-------------------------|----------------|---------------------------|
| Solid Cu-90 °C (194 °F) | 0.5…2.5 mm2  (14…20 AWG)                | 1.13 N•m (10 lb•in) rated |
|                         | 0.5…2.5 mm2  (14…20 AWG)                | 1.3 N•m (12 lb•in) maximum Stranded Cu-90 °C (194 °F) 0.5…2.5 mm2 (14…20 AWG)                           |

<!-- image -->

ATTENTION: Be careful when stripping wires. Wire fragments that fall into the controller could cause damage. Once wiring is complete, be sure the base unit is free of all metal fragments before removing protective debris strips and installing the processor unit. Failure to remove strips before operating can cause overheating.

<!-- image -->

## Use Surge Suppressors

## Wire without Spade Lugs

When wiring without spade lugs, we recommend that you keep the finger-safe covers in place. Loosen the terminal screw and route the wires through the opening in the finger-safe cover. Tighten the terminal screw making sure the pressure plate secures the wire.

<!-- image -->

## Wire with Spade Lugs

The diameter of the terminal screw head is 5.5 mm (0.220 in.). The input and output terminals of the MicroLogix 1500 base unit are designed for a 6.35 mm (0.25 in.) wide spade (standard for #6 screw for up to 14 AWG) or a 4 mm (metric #4) fork terminal.

When using spade lugs, use a small, flat-blade screwdriver to pry the finger-safe cover from the terminal blocks as shown below. Then loosen the terminal screw.

<!-- image -->

Because of the potentially high current surges that occur when switching inductive load devices, such as motor starters and solenoids, the use of some type of surge suppression to protect and extend the operating life of the controllers output contacts is required. Switching inductive loads without surge suppression can significantly reduce the life expectancy of relay contacts. By adding a suppression device directly across the coil of an inductive device, you prolong the life of the output or relay contacts. You also reduce the effects of voltage transients and electrical noise from radiating into adjacent systems.

Figure 17 shows an output with a suppression device. We recommend that you locate the suppression device as close as possible to the load device.

Figure 17 - Output with Suppression Device Example

<!-- image -->

If the outputs are DC, we recommend that you use an 1N4004 diode for surge suppression, as shown in Figure 18 .

Figure 18 - Relay or Solid-state DC Output with Suppression Device Example

<!-- image -->

Suitable surge suppression methods for inductive AC load devices include a varistor, an RC network, or an Allen-Bradley surge suppressor, all shown in Figure 19. These components must be appropriately rated to suppress the switching transient characteristic of the particular inductive device. See Table 8 for recommended suppressors.

Figure 19 - Surge Suppression for Inductive AC Load Devices

<!-- image -->

If you connect an expansion I/O Triac output to control an inductive load, we recommend that you use varistors to suppress noise. Choose a varistor that is appropriate for the application. The suppressors we recommend for Triac outputs when switching 120V AC inductive loads are a Harris MOV, part number V175 LA10A, or an Allen-Bradley MOV, catalog number 599-K04 or 599-KA04. Consult the varistor manufacturer's data sheet when selecting a varistor for your application

For inductive DC load devices, a diode is suitable. A 1N4004 diode is acceptable for most applications. A surge suppressor can also be used. See Table 8 for recommended suppressors.

As shown in Figure 20, these surge suppression circuits connect directly across the load device.

## Ground the Controller

Figure 20 - Surge Suppression for Inductive DC Load Devices

(A surge suppressor can also be used.)

<!-- image -->

## Recommended Surge Suppressors

Use the Allen-Bradley surge suppressors shown in Table 8 for use with relays, contactors, and starters.

Table 8 - Recommended Surge Suppressors

| Suppressor Device Coil Voltage Catalog Number                 |                         |                           |
|---------------------------------------------------------------|-------------------------|---------------------------|
| Bulletin 509 Motor Starter Bulletin 509 Motor Starter         | 120V AC 240V AC         | 599-K04(1) 599-KA04(1)    |
| Bulletin 100 Contactor Bulletin 100 Contactor                 | 120V AC 240V AC         | 199-FSMA1(2) 199-FSMA2(2) |
| Bulletin 709 Motor Starter 120V AC 1401-N10                   |                         |                           |
| Bulletin 700 Type R, RM Relays AC coil None required          |                         |                           |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 12V DC 12V DC           | 199-FSMA9                 |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 24V DC 24V DC           | 199-FSMA9                 |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 48V DC 48V DC           | 199-FSMA9                 |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 115…125V DC 115…125V DC | 199-FSMA10                |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 230…250V DC 230…250V DC | 199-FSMA11                |
| Bulletin 700 Type N, P, or PK Relay 150V max, AC or DC        |                         | 700-N24(2)                |
| Miscellaneous electromagnetic devices limited to 35 sealed VA | 150V max, AC or DC      | 700-N24(2)                |

In solid-state control systems, grounding and wire routing helps limit the effects of noise due to electromagnetic interference (EMI). Run the ground connection from the ground screw of the base unit to the electrical panel's ground bus prior to connecting any devices. Use 2.5 mm 2 (14 AWG) wire. This connection must be made for safety purposes.

This product is intended to be mounted to a well grounded mounting surface such as a metal panel. See the Industrial Automation Wiring and Grounding Guidelines , publication 1770-4.1, for additional information. Additional grounding connections from the mounting tabs or DIN rail, if used, are not required unless the mounting surface cannot be grounded. You must also provide an acceptable grounding path for each device in your application.

<!-- image -->

Use all four mounting positions for panel mounting installation.

## Wiring Diagrams

<!-- image -->

<!-- image -->

This symbol denotes a protective earth ground terminal which provides a low impedance path between electrical circuits and earth for safety purposes and provides noise immunity improvement. This connection must be made for safety purposes.

<!-- image -->

<!-- image -->

ATTENTION: Remove the protective debris strip before applying power to the controller. Failure to remove the strip may cause the controller to overheat.

This following illustrations show the wiring diagrams for the MicroLogix 1500 controllers. Controllers with DC inputs can be wired as either sinking or sourcing configuration. Sinking and sourcing does not apply to AC inputs. See Sinking and Sourcing Wiring Diagrams on page 41 .

<!-- image -->

This symbol denotes a protective earth ground terminal which provides a low impedance path between electrical circuits and earth for safety purposes and provides noise immunity improvement. This connection must be made for safety purposes.

<!-- image -->

## Miswiring - 1764-28BXB Only

The following table shows miswiring conditions and the consequences of improper wiring:

Table 9 - Consequences of Improper Wiring

| Condition Result                                                                                         |                                                                                              |                                                                                                 |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Operating with voltage less than 20.4V DC                                                                | This will not damage the base unit. The base unit may not power up.                          | This will not damage the base unit. The base unit may not power up.                             |
| Operating with voltage less than 20.4V DC                                                                | IMPORTANT                                                                                    | This is not recommended. You must verify that the line voltage remains within specified limits. |
| Reverse wiring of the line terminals (0…30V DC)                                                          | Reverse wiring will not damage the base unit. The base unit will not power up.               | Reverse wiring will not damage the base unit. The base unit will not power up.                  |
| Applied voltage level exceeds the published recommended value (For example, applying 120V AC to 240V AC) | Exceeding the published recommended voltage may result in permanent damage to the base unit. | Exceeding the published recommended voltage may result in permanent damage to the base unit.    |

## Terminal Block Layouts

The base unit terminal block layouts are shown in Figure 21. The shading on the labels indicates how the terminals are grouped. A detail of the groupings are shown in Table 10 and Table 11 .

Figure 21 - Base Unit Terminal Block Layout

+24V

DC

POWER

OUT

VAC

VDC 0

DC

COM 0

COM

Group 0 Group 1 Group 2

I / 1

I / 4

I / 6

I / 0

VAC

VDC 1

I / 3

I / 2

VAC

VDC 3

DC

COM 1

VAC

VDC 4

O / 3

VAC

VDC 2

I / 11

I / 9

DC

COM 2

I / 7

I / 8

O / 7 O / 8

VAC

VDC 5

I / 10

24BWA

O / 10

24BWA

I / 5

O / 5

O / 0 O / 2 O / 6 O / 9 O / 11 O / 1 O / 4 VAC
VDC 5
O / 3

Gr rou

Gro oup

p

up 0

p 0

NOT

Gro

Gr rou

up 1

oup

p

p 1

AC

USED

COM 0

NOT

USED

Gro

Gr rou

up 2

oup

p

p 2

Gro

Gr rou

up 3

oup

p

Gr rou

Gro oup

Gr rou

Gro up 4

oup p 3

p

p 4

up 5

p

p 5

Group 0 Group 1 Group 2

I / 1

I / 6

I / 4

I / 0

VAC

VAC

VDC 0

VAC

VDC 2

VDC 1

O / 0

O / 1

Gr rou

Gro oup

p

up 0

p 0

Gro

Gr rou

up 1

oup

p

p 1

I / 3

I / 2

VAC

VDC 3

AC

COM 1

VAC

VDC 4

I / 5

AC

COM 2

I / 9

I / 11

I / 7

I / 8

I / 10

O / 5

O / 7 O / 8 O / 10

O / 3

24AWA

24AWA

O / 2 O / 6 O / 9 O / 11 O / 4 VAC
VDC 5
O / 3

Gr

VAC

VDC 5

Gr rou

Gro

Gro oup

p

up 2

p 2

Gro

Gr rou

up 3

oup

p

p 3

rou up 4

oup

p

p 4

Gro

Gr rou

up 5

oup

p

p 5

<!-- image -->

## Terminal Groupings

Table 10 - Input Terminal Grouping

| Controller   | Inputs                                     | Inputs   | Inputs   |
|--------------|--------------------------------------------|----------|----------|
| Controller   | Input Group Common Terminal Input Terminal |          |          |
| 1764-24BWA   | Group 0 DC COM 0 I/0…I/3                   |          |          |
| 1764-24BWA   | Group 1  DC COM 1  I/4…I/7                 |          |          |
| 1764-24BWA   | Group 2 DC COM 2 I/8…I/11                  |          |          |
| 1764-24AWA   | Group 0 AC COM 0 I/0…I/3                   |          |          |
| 1764-24AWA   | Group 1  AC COM 1  I/4…I/7                 |          |          |
| 1764-24AWA   | Group 2 AC COM 2 I/8…I/11                  |          |          |
| 1764-28BXB   | Group 0 DC COM 0 I/0…I/3                   |          |          |
| 1764-28BXB   | Group 1  DC COM 1  I/4…I/7                 |          |          |
| 1764-28BXB   | Group 2 DC COM 2 I/8…I/15                  |          |          |

O / 4

Inputs

1764-24BWA

Outputs

Inputs

1764-24AWA

Outputs

85-265

VAC

L1

85-265

VAC

L1

L2

L2

## Sinking and Sourcing Wiring Diagrams

Table 11 - Output Terminal Grouping

| Controller   | Outputs   | Outputs                                       | Outputs                         |
|--------------|-----------|-----------------------------------------------|---------------------------------|
| Controller   |           | Output Group Voltage Terminal Output Terminal |                                 |
|              |           | Group 0 VAC/VDC 0 O/0                         |                                 |
|              | Group 1   | VAC/VDC 1                                     | O/1                             |
|              |           | Group 2 VAC/VDC 2 O/2                         |                                 |
|              | Group 3   | VAC/VDC 3                                     | O/3                             |
|              |           | Group 4 VAC/VDC 4 O/4…O/7                     |                                 |
|              | Group 5   | VAC/VDC 5                                     | O/8…O/11                        |
|              |           | Group 0 VAC/VDC 0 O/0                         |                                 |
|              | Group 1   | VAC/VDC 1                                     | O/1                             |
|              |           | Group 2 VAC/VDC 2 O/2                         |                                 |
|              | Group 3   | VAC/VDC 3                                     | O/3                             |
|              |           | Group 4 VAC/VDC 4 O/4…O/7                     |                                 |
|              | Group 5   | VAC/VDC 5                                     | O/8…O/11                        |
|              |           | Group 0 VAC/VDC 0 O/0                         |                                 |
|              | Group 1   | VAC/VDC 1                                     | O/1                             |
|              |           | Group 2 VDC 2, VDC COM 2 O/2…O/7              |                                 |
|              | Group 3   | VAC/VDC 3                                     | O/8 and O/9                     |
|              |           |                                               | Group 4 VAC/VDC 4 O/10 and O/11 |

Any of the MicroLogix 1500 controller DC embedded input groups can be configured as sinking or sourcing depending on how the DC COM is wired on the group.

|                                                    | Type Definition                                                                                                                                      |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sinking Input Connection of a PNP sourcing device  | The input energizes when high-level voltage is applied to the input terminal (active high). Connect the power supply VDC (-) to the DC COM terminal. |
| Sourcing Input Connection of an NPN sinking device | The input energizes when low-level voltage is applied to the input terminal (active low). Connect the power supply VDC (+) to the DC COM terminal.   |

## 1764-24AWA Wiring Diagram

Input Terminals

"NOT USED" terminals are not intended for use as connection points.

<!-- image -->

Output Terminals

<!-- image -->

## 1764-24BWA Wiring Diagram with Sinking Inputs

Input Terminals

<!-- image -->

Output Terminals

<!-- image -->

## 1764-24BWA Wiring Diagram with Sourcing Inputs

Input Terminals

<!-- image -->

## Output Terminals

<!-- image -->

## 1764-28BXB Wiring Diagram with Sinking Inputs

Input Terminals

<!-- image -->

"NOT USED" terminals are not intended for use as connection points.

## Output Terminals (FET Outputs Are Sourcing Only)

<!-- image -->

## 1764-28BXB Wiring Diagram with Sourcing Outputs

Input Terminals

<!-- image -->

"NOT USED" terminals are not intended for use as connection points.

Output Terminals (FET Outputs Are Sourcing Only)

<!-- image -->

## Controller I/O Wiring

## Minimizing Electrical Noise

Because of the variety of applications and environments where controllers are installed and operating, it is impossible to ensure that all environmental noise will be removed by input filters. To help reduce the effects of environmental noise, install the MicroLogix 1500 system in a properly rated (for example, NEMA) enclosure. Make sure that the MicroLogix 1500 system is properly grounded.

A system may malfunction due to a change in the operating environment after a period of time. We recommend periodically checking system operation, particularly when new machinery or other noise sources are installed near the Micrologix 1500 system.

## Transistor Output Transient Pulses

<!-- image -->

ATTENTION: A brief transient current pulse may flow through transistor outputs if the external supply voltage is suddenly applied at the VDC and VDC com terminals (for example, through the master control relay). It is a fast rateof-change of voltage at the terminals that causes the pulse. This condition is inherent in transistor outputs and is common to solid state devices. The transient pulses may occur regardless of whether the controller is powered or running.

The transient energy is dissipated in the load, and the pulse duration is longer for loads with high impedance. Figure 22 illustrates the relation between pulse duration and load current. Power-up transients will not exceed the times shown in the graph. For most applications the pulse energy is not sufficient to energize the load.

To reduce the possibility of inadvertent operation of devices connected to transistor outputs, consider adding an external resistor in parallel to the load to increase the on-state load current. The duration of the transient pulse is reduced when the on-state load current is increased or the load impedance is decreased.

Figure 22 - Transient Pulse Duration as a Function of Load Current

<!-- image -->

## Notes:

## Default Communication Configuration

## Use the Communications Toggle Push Button

## Communication Connections

The method you use and cabling required depend on your application. This chapter also describes how the controller establishes communication with the appropriate network.

<!-- image -->

ATTENTION: All devices communicating within a network must use the same protocol.

The MicroLogix 1500 controller has the following default communication configuration.

Table 12 - DF1 Full-duplex Default Configuration Parameters

| Parameter Default                         |
|-------------------------------------------|
| Baud Rate 19.2K                           |
| Parity None                               |
| Source ID (Node Address) 1                |
| Control Line No handshaking               |
| Error Detection CRC                       |
| Embedded Responses Auto detect            |
| Duplicate Packet (Message) Detect Enabled |
| ACK Timeout 50 counts                     |
| NAK retries 3 retries                     |
| ENQ retries 3 retries                     |
| Stop Bits 1                               |

<!-- image -->

The default configuration is present when:

- The controller is powered-up for the first time
- The Communications Toggle push button specifies default communications (the DCOMM LED is on)
- An OS upgrade is completed

See Understand Communication Protocols on page 95 for more information on communicating.

The Communications Toggle push button is located on the processor. You must remove the processor door or DAT to access the Communications Toggle push button.

Use the Communications Toggle push button to change from the user-defined communication configuration to the default communications configuration and back. The Default Communications (DCOMM) LED operates to show when the controller is in the default communications mode (settings are shown in page Table 12).

<!-- image -->

## Connect to the RS-232 Port

<!-- image -->

<!-- image -->

The Communications Toggle push button must be pressed and held for two seconds to activate.

The Communications Toggle push button only affects the communication configuration of Channel 0.

## DF1 Full-Duplex Communication Parameters

When a communication channel is configured for DF1 Full-duplex, the following parameters can be changed.

Table 13 - DF1 Full-duplex Configuration Parameters

| Parameter Options Default                                                 |
|---------------------------------------------------------------------------|
| Baud Rate 300, 600, 1200, 2400, 4800, 9600, 19.2K, 38.4K 19.2K            |
| Parity None, even None                                                    |
| Source ID (Node Address) 0 to 254 decimal 1                               |
| Control Line No handshaking, Full-duplex modem handshaking No handshaking |
| Error Detection CRC, BCC CRC                                              |
| Embedded Responses Auto-detect, enabled Auto detect                       |
| Duplicate Packet (Message) Detect  Enabled, disabled Enabled              |
| ACK Timeout 1…65535 counts (20 ms increments) 50 counts                   |
| NAK retries 0…255 3 retries                                               |
| ENQ retries 0…255 3 retries                                               |
| Stop Bits Not a setting, always 1 1                                       |

## Make a DF1 Point-to-Point Connection

You can connect the MicroLogix 1500 programmable controller to your computer using a serial cable from your computer's serial port to the controller, as shown in the following illustrations.

<!-- image -->

ATTENTION: Chassis ground, internal 24V ground, user 24V DC ground, and RS-232 ground are internally connected. You must connect the chassis ground terminal screw to ground prior to connecting any devices. It is important that you understand your personal computer's grounding system before connecting to the controller. An optical isolator, such as the 1761-NET-AIC, is recommended between the controller and your personal computer when using Channel 0. An isolator is not required when using Channel 1 (1764-LRP).

## Channel 0

We recommend using an Advanced Interface Converter (AIC+), catalog number 1761-NET-AIC, or similar optical isolator, as shown below. See Cable Selection Guide on page 58 for specific AIC+ cabling information.

Figure 23 - Channel 0 Point-to-Point Connection

<!-- image -->

Channel 1

Figure 24 - Channel 1 Point-to-Point Connection

<!-- image -->

## Use a Modem

You can use modems to connect a computer to one MicroLogix 1500 controller (using DF1 Fullduplex protocol), to multiple controllers (using DF1 Half-duplex protocol), or Modbus RTU slave protocol, as shown in Figure 25. Do not use DH-485 protocol through modems under any circumstance. (See Use Modems with MicroLogix Programmable Controllers on page 96 for information on types of modems you can use with the MicroLogix controllers.)

<!-- image -->

## Isolated Modem Connection

We recommend using an AIC+, catalog number 1761-NET-AIC, as your optical isolator for Channel 0. See Cable Selection Guide on page 58 for specific AIC+ cabling information. Using an AIC+ to isolate the modem is shown in Figure 26 .

Figure 26 - Isolated Modem Connection

<!-- image -->

## Constructing Your Own Modem Cable

If you construct your own modem cable, the maximum cable length is 15.24 m (50 ft.) with a 25-pin or 9-pin connector. See Figure 27 for constructing a straight-through cable.

Figure 27 - Typical Modem Cable Pinout

<!-- image -->

| or 1764-LRP Channel 1   | AIC+ optical isolator       |               | Modem              |
|-------------------------|-----------------------------|---------------|--------------------|
|                         |                             | 3 TXD TXD 2 3 | 9-pin 25-pin 9-pin |
|                         |                             |               | 2 RXD RXD 3 2      |
|                         |                             |               | 5 GND GND 7 5      |
|                         |                             | 1 CD CD 8 1   | 4 DTR DTR 20 4     |
|                         | Pins 4 and 6 are internally |               | 6 DSR DSR 6 6      |
|                         | 1764-LRP only.              |               | 8 CTS CTS 5 8      |
|                         |                             |               | 7 RTS RTS 4 7      |

## Constructing Your Own Null Modem Cable

If you construct your own null modem cable, the maximum cable length is 15.24 m (50 ft.) with a 25-pin or 9-pin connector. See Figure 28 .

Figure 28 - Typical Null Modem Cable Pinout

<!-- image -->

## Connect to a DF1 Half-Duplex Network

Table 14 shows available parameters for a communication port that is configured for DF1 Halfduplex slave.

Table 14 - DF1 Half-duplex Configuration Parameters

| Parameter Options                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                        | Baud Rate 300, 600, 1200, 2400, 4800, 9600, 19.2K, 38.4K                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                        | Parity None, even                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Source ID (Node Address) 0…254 decimal |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                        | Control Line No handshaking, handshaking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Error Detection CRC, BCC               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EOT Suppression                        | Enabled, disabled When EOT Suppression is enabled, the slave does not respond when polled if no message is queued. This saves modem transmission power and time when there is no message to transmit.                                                                                                                                                                                                                                                                                                                               |
| Duplicate Packet (Message) Detect      | Enabled, disabled Detects and eliminates duplicate responses to a message. Duplicate packets may be sent under noisy communication conditions if the sender’s Message Retries are not set to 0.                                                                                                                                                                                                                                                                                                                                     |
| Poll Timeout (x20 ms)                  | 0…65535 (can be set in 20 ms increments) Poll Timeout only applies when a slave device initiates a MSG instruction. It is the amount of time that the slave device waits for a poll from the master device. If the slave device does not receive a poll within the Poll Timeout, a MSG instruction error is generated, and the ladder program needs to requeue the MSG instruction. If you are using a MSG instruction, it is recommended that a Poll Timeout value of zero not be used. Poll Timeout is disabled when set to zero. |
| RTS Off Delay (x20 ms)                 | 0…65535 (can be set in 20 ms increments) Specifies the delay time between when the last serial character is sent to the modem and when RTS is deactivated. Gives the modem extra time to transmit the last character of a packet.                                                                                                                                                                                                                                                                                                   |
| RTS Send Delay (x20 ms)                | 0…65535 (can be set in 20 ms increments) Specifies the time delay between setting RTS until checking for the CTS response. For use with modems that are not ready to respond with CTS immediately upon receipt of RTS.                                                                                                                                                                                                                                                                                                              |
| Message Retries                        | 0…255 Specifies the number of times a slave device attempts to resend a message packet when it does not receive an ACK from the master device. For use in noisy environments where message packets may become corrupted in transmission.                                                                                                                                                                                                                                                                                            |
| Pre Transmit Delay (x1 ms)             | 0…65535 (can be set in 1 ms increments) When the Control Line is set to no handshaking, this is the delay time before transmission. Required for 1761-NET-AIC physical Half duplex networks. The 1761-NET-AIC needs delay time to change from transmit to receive mode. When the Control Line is set to DF1 Half-duplex Modem, this is the minimum time delay between receiving the last character of a packet and the RTS assertion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## DF1 Half-duplex Master/Slave Network

Use Figure 29 for DF1 Half-duplex master/slave protocol without hardware handshaking.

Figure 29 - DF1 Half-duplex Master/Slave Protocol

<!-- image -->

<!-- image -->

## DF1 Half-duplex Network (Using PC and Modems)

<!-- image -->

## Connecting to a DH-485 Network

processor (slave)

The following network diagrams provide examples of how to connect MicroLogix 1500 controllers to the DH-485 network using the Advanced Interface Converter (AIC+, catalog number 1761-NET-AIC). For more information on the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

DH-485 Network with a MicroLogix 1500 Controller

<!-- image -->

Typical 3-node Network (Channel 0 Connection)

<!-- image -->

Typical 3-node Network (Channel 1 Connection)

<!-- image -->

Networked Operator Interface Device and MicroLogix Controllers

<!-- image -->

## DH-485 Configuration Parameters

When MicroLogix communications are configured for DH-485, the following parameters can be changed:

Table 15 - DF1 Full-Duplex Configuration Parameters

| Parameter Options            |
|------------------------------|
| Baud Rate 9600, 19.2K        |
| Node Address 1 to 31 decimal |
| Token Hold Factor 1 to 4     |

See Software Considerations on page 99 for tips on setting the parameters listed Table 15 .

## Recommended Tools

To connect a DH-485 network, you need tools to strip and attach the shielded cable. We recommend the following equipment (or equivalent):

Table 16 - Working with Cable for DH-485 Network

| Description Part Number Manufacturer                   |
|--------------------------------------------------------|
| Shielded twisted pair cable #3106A or #9842 Belden     |
| Stripping tool Not applicable Not applicable           |
| 1/8” slotted screwdriver Not applicable Not applicable |

## DH-485 Communication Cable

The communication cable consists of a number of cable segments daisy-chained together. The total length of the cable segments cannot exceed 1219 m (4000 ft.). However, two segments can be used to extend the DH-485 network to 2438 m (8000 ft.). For additional information on connections using the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1764-UM004 .

## Communication Cable Connection to the DH-485 Connector

<!-- image -->

A daisy chained network is recommended. Do not make the incorrect connection that is shown in Figure 30 .

Figure 30 - Connect Communication Cable to DH-485 Connector

<!-- image -->

## Single Cable Connection

When connecting a single cable to the DH-485 connector, use Figure 31 .

Figure 31 - Single Cable Connection

<!-- image -->

## Multiple Cable Connection

When connecting multiple cables to the DH-485 connector, use Figure 32 .

Figure 32 - Multiple Cable Connection

<!-- image -->

## Connect the AIC+

Table 17 - Connections using Belden #3106A Cable

| For this Wire/Pair Connect this Wire To this Terminal   |                                                |
|---------------------------------------------------------|------------------------------------------------|
|                                                         | Shield/drain Non-jacketed Terminal 2 - Shield  |
|                                                         | Blue Blue Terminal 3 - (Common)                |
| White/orange                                            | White with orange stripe Terminal 4 - (Data B) |
| White/orange                                            | Orange with white stripe Terminal 5 - (Data A) |

Table 18 - Connections using Belden #9842 Cable

|              | For this Wire/Pair Connect this Wire To this Terminal   |
|--------------|---------------------------------------------------------|
|              | Shield/drain Non-jacketed Terminal 2 - Shield           |
| Blue/white   | White with blue stripe  Cut back - no connection(1)     |
| Blue/white   | Blue with white stripe Terminal 3 - (Common)            |
| White/orange | White with orange stripe Terminal 4 - (Data B)          |
| White/orange | Orange with white stripe Terminal 5 - (Data A)          |

## Ground and Terminate the DH-485 Network

Only one connector at the end of the link must have Terminals 1 and 2 jumpered together. This provides an earth ground connection for the shield of the communication cable.

Both ends of the network must have Terminals 5 and 6 jumpered together, as shown in Figure 33. This connects the termination impedance (of 120 Ω) that is built into each AIC+ as required by the DH-485 specification.

Figure 33 - End-of-Line Termination

<!-- image -->

The AIC+, catalog number 1761-NET-AIC, enables MicroLogix controllers to connect to a DH-485 network when they are configured for DH-485 protocol. The AIC+ has two isolated RS-232 ports and one RS-485 port. When two MicroLogix controllers are closely positioned, you can connect a controller to each of the RS-232 ports on the AIC+.

The AIC+ can also be used as an RS-232 isolator, providing an isolation barrier between the controllers communications port and any equipment connected to it (for example, a computer, modem, and so on).

Figure 34 shows the external wiring connections and specifications of the AIC+.

<!-- image -->

Figure 34 - AIC+ External Wiring Connections

| Item Description                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------|
| 1 Port 1 - DB-9 RS-232, DTE                                                                                            |
| 2 Port 3 - RS-485 Phoenix plug                                                                                         |
| 3 Port 2 - mini-DIN 8 RS-232 DTE                                                                                       |
| 4  DC Power source selector switch (Cable = Port 2 power source, External = External power source connected to item 5) |
| 5 Terminals for external 24V DC power supply and chassis ground                                                        |

For additional information on connecting the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

## Cable Selection Guide

<!-- image -->

|                                                 |                                              | Cable Length Connections from to AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | 1764-LRP processor, channel 1 Port 2 Yes External                           |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | SLC 5/03 or SLC 5/04 processors, channel 0 Port 2 Yes External              |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | MicroLogix 1000 or MicroLogix 1500 controller Port 1 Yes External           |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | PanelView 550 terminal through NULL modem adapter Port 2 Yes External       |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | DTAM™ Plus / DTAM™ Micro Port 2 Yes External                                |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | PC COM port Port 2 Yes External                                             |                                      |

<!-- image -->

|                                |                             | Cable Length Connections from to AIC+               | External Power Supply Required (1)   | Power Selection Switch Setting   |
|--------------------------------|-----------------------------|-----------------------------------------------------|--------------------------------------|----------------------------------|
| 1761-CBL-AM00(2)               | 45 cm (17.7 in.)            | MicroLogix 1000 or 1500 controllers Port 2 No Cable |                                      |                                  |
| 1761-CBL-HM02(2) 1761-CBL-AH02 | 2 m (6.5 ft.) 2 m (6.5 ft.) | To port 2 on another AIC+ Port 2 Yes External       |                                      |                                  |

(1) An external power supply is required unless the AIC+ is powered by the device that is connected to port 2, then the selection switch should be set to cable.

(2) Series C or later cables are required.

<!-- image -->

|                           |                                | Cable Length Connections from to AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|---------------------------|--------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | 1764-LRP processor, channel 1 Port 1 Yes External                           |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | SLC 5/03 or SLC 5/04 processor, channel 0 Port 1 Yes External               |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | PC COM port Port 1 Yes External                                             |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | PanelView 550 terminal through NULL modem adapter Port 1 Yes External       |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | DTAM Plus / DTAM Micro Port 1 Yes External                                  |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | Port 1 on another AIC+ Port 1 Yes External                                  |                                      |

<!-- image -->

| Cable Length Connections from to AIC+                                              | External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|------------------------------------------------------------------------------------|--------------------------------------|--------------------------------------|
| Straight 9-pin to 25-pin — Modem or other communication device Port 1 Yes External |                                      |                                      |

<!-- image -->

|                             |                                 | Cable Length Connections from to AIC+                       | External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-----------------------------|---------------------------------|-------------------------------------------------------------|--------------------------------------|--------------------------------------|
| 1761-CBL-AS03 1761-CBL-AS09 | 3 m (9.8 ft.) 9.5 m (31.17 ft.) | SLC™ 500 Fixed, SLC 5/01, SLC 5/02, and SLC 5/03 processors |                                      | Port 3 Yes External                  |
| 1761-CBL-AS03 1761-CBL-AS09 | 3 m (9.8 ft.) 9.5 m (31.17 ft.) | PanelView 550 terminal RJ45 port Port 3 Yes External        |                                      |                                      |

## 1761-CBL-PM02 (or equivalent) Cable Wiring Diagram

<!-- image -->

<!-- image -->

## Recommended User-supplied Components

The components in Table 19 can be purchased from your local electronics supplier.

Table 19 - User-supplied Components

| Component Recommended Model                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|
| External power supply and chassis ground Power supply rated for 20.4…28.8V DC                                     |
| NULL modem adapter Standard AT                                                                                    |
| Straight 9-pin to 25-pin RS-232 cable  See Figure 35 and Table 20 for port information if making your own cables. |

<!-- image -->

Table 20 - Cable Assignment

| Pin Port 1: DB-9 RS-232  Port 2(1): 8-pin mini-DIN Port 3: RS-485 Connector   |
|-------------------------------------------------------------------------------|
| 1 Received line signal detector (DCD) 24V DC Chassis ground                   |
| 2 Received data (RxD) Ground (GND) Cable shield                               |
| 3 Transmitted data (TxD) Request to send (RTS) Signal ground                  |
| 4  DTE ready (DTR)( )(2) Received data (RxD)(3) DH-485 data B                 |
| 5 Signal common (GND) Received line signal detector (DCD) DH-485 data A       |
| 6  DCE ready (DSR)(1)  Clear to send (CTS)(3)  Termination                    |
| 7 Request to send (RTS) Transmitted data (TxD) Not applicable                 |
| 8 Clear to send (CTS) Ground (GND) Not applicable                             |
| 9 Not applicable Not applicable Not applicable                                |

- (2) On port 1, pin 4 is electronically jumpered to pin 6. Whenever the AIC+ is powered on, pin 4 matches the state of pin 6.
- (3) In the 1761-CBL-PM02 cable, pins 4 and 6 are jumpered together within the DB-9 connector.

## Safety Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D or non-hazardous locations only.

<!-- image -->

## ATTENTION: EXPLOSION HAZARD

AIC+ must be operated from an external power source.

This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.

See Safety Considerations on page 21 for additional information.

## Install and Attach the AIC+

1. Take care when installing the AIC+ in an enclosure so that the cable connecting the MicroLogix controller to the AIC+ does not interfere with the enclosure door.
2. Carefully plug the terminal block into the RS-485 port on the AIC+ you are putting on the network. Allow enough cable slack to prevent stress on the plug.
3. Provide strain relief for the Belden cable after it is wired to the terminal block. This guards against breakage of the Belden cable wires.

## Power the AIC+

In normal operation with a MicroLogix programmable controller connected to port 2 of the AIC+, the controller powers the AIC+. Any AIC+ not connected to a MicroLogix controller requires a 24V DC power source. The AIC+ requires 120 mA at 24V DC.

If both the controller and external power are connected to the AIC+, the power selection switch determines what device powers the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if higher voltage is used.

Set the DC Power Source selector switch to EXTERNAL before connecting the power supply to the AIC+. Figure 36 shows where to connect external power for the AIC+.

Figure 36 - External Power for AIC+

<!-- image -->

<!-- image -->

ATTENTION: Always connect the CHS GND (chassis ground) terminal to the nearest earth ground. This connection must be made whether or not an external 24V DC supply is used.

Power Options

There are two options for powering the AIC+:

- Use the 24V DC user power supply built into the MicroLogix 1500 controller. The AIC+ is powered through a hard-wired connection using a communication cable (1761-CBL-HM02, or equivalent) connected to port 2.
- Use an external DC power supply with the following specifications:
- Operating voltage: 24V DC (-15%/+20%)
- Output current: 150 mA minimum
- Rated NEC Class 2

Make a hard-wired connection from the external supply to the screw terminals on the bottom of the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if miswired with the wrong power source.

## Connect to Ethernet

You can connect a MicroLogix 1500 controller to an Ethernet network via the Ethernet Interface (ENI), 1761-NET-ENI. For additional information on using the ENI, see the MicroLogix Ethernet Interface User Manual, publication 1761-UM006 . Figure 37 shows the external wiring connections of the ENI.

Figure 37 - ENI Wiring Connections

<!-- image -->

## Ethernet Connections

The Ethernet connector, port 1, is an RJ45, 10Base-T connector. The pin-out for the connector is shown in Table 21:

Table 21 - RJ45 Connector Pinout

| Pin Pin Name           |
|------------------------|
| 1 Tx+                  |
| 2 Tx                        |
| 3 Rx+                  |
| 4 Not used by 10Base-T |
| 5 Not used by 10Base-T |
| 6 Rx                        |
| 7 Not used by 10Base-T |
| 8 Not used by 10Base-T |

When to use straight-through and cross-over cable:

- ENI Ethernet port to 10Base-T Ethernet switch cables utilize a straight-through pin-out (1-1, 2-2, 3-3, 6-6).
- Direct point-to-point 10Base-T cables connecting the ENI Ethernet port directly to another ENI Ethernet port (or a computer 10Base-T port) require a cross-over pin-out (1-3, 2-6, 3-1, 6-2).

## RS-232 Connections

Port 2 of the ENI is an 8-pin mini-DIN RS-232 port that provides connection to DF1 compatible RS-232 devices. The connector pin assignments are shown in Figure 38 .

<!-- image -->

Figure 38 - 8-pin mini-DIN RS-232 Connector Pinout

| Pin Port 2             |
|------------------------|
| 1 24V DC               |
| 2 Ground (GND)         |
| 3 No connection        |
| 4 ENI input data, RxD  |
| 5 No connection        |
| 6 No connection        |
| 7 ENI output data, TxD |
| 8 Ground (GND)         |

Table 22 describes the RS-232 compatible cables.

Table 22 - Compatible RS-232 Cables

| ENI Connected to Catalog Number Use Cable   |                                           |                                                                   |
|---------------------------------------------|-------------------------------------------|-------------------------------------------------------------------|
| MicroLogix (all series)                     | 1761-CBL-AM00 1761-CBL-HM02 1761-CBL-AH02 | mini-DIN to mini-DIN 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) |
| SLC 5/03, SLC 5/04, or SLC 5/05 Channel 0   | 1761-CBL-AP00 1761-CBL-PM02 1761-CBL-PH02 | mini-DIN to D-shell 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.)  |
|                                             | PLC-5 1761-CBL-AP00 1761-CBL-PM02         | mini-DIN to D-shell 45 cm (17.7 in.) 2 m (6.5 ft.)                |

## Trimpot Operation

<!-- image -->

## Use Trimpots and the Data Access Tool

The processor has two trimming potentiometers (trimpots) which allow modification of data within the controller. Adjustments to the trimpots change the value in the corresponding Trimpot Information (TPI) register. The data value of each trimpot can be used throughout the control program as timer, counter, or analog presets depending upon the requirements of the application.

The trimpots are located below the mode switch under the left access door of the processor, as shown in Figure 39 .

Figure 39 - Location of Trimpots

<!-- image -->

Use a small flathead screwdriver to turn the trimpots. Adjusting their value causes data to change within a range of 0…250 (fully clockwise). The maximum rotation of each trimpot is three-quarters, as shown in Figure 40. Trimpot stability over time and temperature is typically ±2 counts.

Figure 40 - Maximum Rotation of Trimpot

<!-- image -->

Trimpot data is updated continuously whenever the controller is powered up.

## Trimpot Information Function File

The composition of the TPI Function file is described in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

## Data Access Tool

## Error Conditions

If the controller detects a problem/error with either trimpot, the last values read remain in the data location, and an error code is put in the error code byte of the TPI file for whichever trimpot had the problem. Once the problem/error is corrected, the error code is cleared. The error codes are described in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

The Data Access Tool (DAT) is a convenient and simple tool that provides an interface for editing and monitoring data. The DAT has five primary features:

- Provides direct access to 48 bit elements
- Provides direct access to 48 integer elements
- Provides two function keys
- Displays controller faults
- Allows Removal/Insertion Under Power

## DAT Keypad and Indicator Light Functions

The DAT has a digital display, 6 keys, an up/down key, and 7 indicator lights. Their functions are described in Table 23 .

<!-- image -->

Table 23 - DAT Keypad and Indicator Light Functions

| Feature Function                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Digital Display Displays the address elements, data values, faults, and errors                                                                    |
| Up/Down Key Selects the element numbers and change data values. The up/down key scrolls when held.                                                |
| F1 Key and Indicator Light Controls the F1 status bit. When the F1 key is pressed or latched, the F1 indicator LED is lit.                        |
| F2 Key and Indicator Light Controls the F2 status bit. When the F2 key is pressed or latched, the F2 indicator LED is lit.                        |
| ESC Key Cancels a current operation                                                                                                               |
| BIT Key and Indicator Light Pressing the BIT key puts the DAT in bit mode. The bit indicator light is on when the DAT is in bit mode.             |
| INT Key and Indicator Light Pressing the INT key puts the DAT in integer mode. The integer indicator light is on when the DAT is in integer mode. |
| ENTER Key Press to select the flashing element number or enter data value.                                                                        |
| PROTECTED Indicator Light Indicates that the element data cannot be changed using the DAT (element is read-only).                                 |

<!-- image -->

The F1, F2, ESC, BIT, INT, and ENTER keys do not repeat when held. Holding down any one of these keys results in only one key press. The Up/Down arrow key is the only key that repeats when held.

## Power-Up Operation

The DAT receives power when it is plugged into the controller. Upon power-up, the DAT performs a self-test.

If the test fails, the DAT displays an error code, all indicator lights are deactivated, and the DAT does not respond to any key presses. See Table 25 for a list of DAT error codes.

<!-- image -->

After a successful self-test, the DAT reads the DAT function file to determine its configuration.

## DAT Function File

DAT configuration is stored in the processor in a specialized configuration file called the DAT Function File. The DAT Function File, which is part of the user's control program, is described in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

Following a successful power-up sequence, the DAT enters the bit monitoring mode.

<!-- image -->

## Power Save Timeout (PST) Parameter

The power save timeout turns off the DAT display after keypad activity has stopped for a userdefined period of time. The power-save (DAT:0.PST) value is set in the DAT Function File. The valid range is 0…255 minutes. The power-save feature can be disabled by setting the PST value to 0, which keeps the display on continuously. The default value is 0.

In power-save mode, a dash flashes in the left-most segment of the display. Press any key (except F1 or F2) to return the DAT to its previous mode. If F1 or F2 is pressed, the DAT will change the value of the F1 or F2 status bits, but the display remains in power-save mode.

## Understanding the DAT Display

When the DAT enters either the bit or integer mode, the element number and its data are displayed. The element number is either the integer or bit location.

## Bit Mode Display Integer Mode Display

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

If the displayed element is defined in the controller's data file, and is not protected, the element number flashes, indicating that it can be modified. If the displayed element is protected, the PROTECTED indicator light illuminates, and the element number does not flash, indicating that the element cannot be modified.

If the element is undefined, the data field displays three dashes. The element number does not flash because the element does not exist.

<!-- image -->

## Entering Bit Mode

Bit mode allows you to view and modify up to 48 contiguous bit locations in the controller. The DAT enters the bit mode automatically following a successful power-up. The bit mode can also be selected by pressing the BIT key. If the bit mode was previously active, the DAT displays the last bit element monitored. If the integer mode was active, the DAT displays the first bit element in the data file. However, there may be a brief delay while the DAT requests information from the controller. During the delay, the working screen will display. See Working Screen Operation on page 69 .

## Entering Integer Mode

Integer mode allows you to view and modify up to 48 contiguous 16-bit integer data locations in the controller. To initiate integer mode, press the INT key. If the integer mode was previously active, the DAT displays the last integer element monitored. If the bit mode was active, the DAT displays the first integer element in the data file. However, there may be a brief delay while the DAT requests information from the controller. If there is a delay, the working screen is displayed. See Working Screen Operation on page 69 .

## Monitoring and Editing

1. Press the INT or BIT key to enter the desired mode. The element number flashes (if not protected).
2. Use the up/down key to scroll and select an element (to scroll rapidly, hold the up/down key).
3. Press ENTER to edit the element. The element number becomes steady and the data flashes if it is not protected.
4. Use the up/down key to change the data. Bit values toggle between "ON" and "OFF". Integer values increment or decrement. Holding down the up/down key causes the integer value to increment or decrement quickly.

<!-- image -->

If the data is protected or undefined, pressing the up/down key scrolls to the next element in the list.

5. Press ENTER to load the new data. Press ESC or INT/BIT to discard the new data.

## F1 and F2 Functions

The function keys, F1 and F2, correspond to bits and can be used throughout the control program as desired. They have no effect on bit or integer monitoring.

Each key has two corresponding bits in the DAT function file. The bits within the DAT function file are shown in Table 24 .

## Table 24 - DAT Function File Bits

|        | Key Bits Address Data Format Type User Program Access   |
|--------|---------------------------------------------------------|
| F1 Key | Pressed DAT:0/F1P Binary Status Read/Write              |
| F1 Key | Latched DAT:0/F1L Binary Status Read/Write              |
| F2 Key | Pressed DAT:0/F2P Binary Status Read/Write              |
| F2 Key | Latched DAT:0/F2L Binary Status Read/Write              |

## F1 or F2 Key Pressed

The pressed bits (DAT:0/F1P and DAT:0/F2P) function as push-buttons and provide the current state of either the F1 or F2 key on the keypad. When the F1 or F2 key is pressed, the DAT sets (1) the corresponding pressed key bit. When the F1 or F2 key is not pressed, the DAT clears (0) the corresponding pressed key bit.

## F1 or F2 Key Latched

The latched bits (DAT:0/F1L and DAT:0/F2L) function as latched push-buttons and provide latched/toggle key functionality. When the F1 or F2 key is pressed, the DAT sets (1) the corresponding latched key bit within the DAT Function File. When the F1 or F2 key is pressed a second time, the DAT clears (0) the corresponding latched key bit.

## Working Screen Operation

Because the DAT is a communications device, its performance is affected by the scan time of the controller. Depending on the user program, if a long scan time is encountered and the DAT waits for information from the controller, a working screen is displayed. The working screen consists of three dashes that move across the display from left to right. While the working screen is displayed, key presses are not recognized. Once the DAT receives data from the controller, it returns to its normal mode of operation.

If you encounter excessive working screen conditions, you can minimize the effect by adding an SVC instruction to the control program. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for information on the SVC instruction.

## Non-Existent Elements

When the DAT determines that an element number does not exist in the controller, the element value displays as three dashes.

If the protection bit for an element is undefined, the DAT will assume that the element is unprotected.

## Controller Faults

The DAT checks for controller faults every 10 seconds. When the DAT detects a controller fault, the display shows "FL" in the element number field and the value of the controller's major fault word (S2:6) is displayed in the value field, as shown below.

<!-- image -->

<!-- image -->

If an element value is being modified when the fault is detected, the fault is stored until the modification is accepted or discarded. Then, the fault will be displayed.

Pressing ESC while the fault is being displayed returns the DAT to its previous mode. The fault is not removed from the controller, just from the DAT display screen. The fault that was on screen will not display again and cannot be "recalled". If a new fault is detected, it will be displayed. If the initial fault is cleared and returns at a later time, the DAT will display the fault at that time.

## Error Conditions

When the DAT detects an error in its own operation, it displays the error screen. The error screen consists of "Err" and a two-digit error code, as shown below.

<!-- image -->

The DAT can experience two different types of errors, internal errors and communication errors.

## Internal DAT Errors

Internal DAT errors are non-recoverable. When the DAT experiences an internal error, it displays the error screen, and does not respond to any key presses. Remove and re-install the DAT. If this does not clear the error, the DAT must be replaced.

## Table 25 - DAT Error Codes

|                                               | Error Code Description Caused by Recommended Action                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
|                                               | 00 Interface time-out Communication traffic Add SVC instructions to ladder program.                                       |
| 01 …02 Power-up test failure Internal failure | Remove and reinsert the DAT. If failure persists, replace the unit.                                                       |
| 03…07 Internal error Internal failure         | Remove and reinsert the DAT. If failure persists, replace the unit.                                                       |
| 08  Processor owned(1)                        | Another device has ownership of the controller Release ownership by the other device.                                     |
|                                               | 09 Access denied Cannot access that file because another device has ownership Release file ownership by the other device. |
| 31…34 Internal error Internal failure         | Remove and reinsert the DAT. If failure persists, replace the unit.                                                       |

## Communication Errors

The DAT continually monitors the interface between the DAT and the controller to ensure a good communication path. If the DAT loses communication with the controller for more than three seconds, it generates an interface time-out error. The DAT automatically attempts to reestablish communications. The error screen displays until the DAT regains communications with the processor. All key presses are ignored until the display clears.

## DAT Error Codes

## Notes:

## Real-Time Clock Operation

<!-- image -->

## Use Real-Time Clock and Memory Modules

Five modules with different levels of functionality are available for use with the MicroLogix 1500 controller.

| Catalog Number Function Memory Size   |                                                  |
|---------------------------------------|--------------------------------------------------|
|                                       | 1764-RTC Real-time Clock Not applicable          |
|                                       | 1764-MM1 Memory Module 8K                        |
|                                       | 1764-MM1RTC Memory Module and Real-time Clock 8K |
| 1764-MM2(1)                           | Memory Module 16K                                |
| 1764-MM2RTC(1)                        | Memory Module and Real-time Clock 16K            |
| 1764-MM3(2)                           | Memory Module 16K                                |
| 1764-MM3RTC(2)                        | Memory Module and Real-time Clock 16K            |

## Removal/Insertion Under Power

The real-time clock module can be installed or removed at any time without risk of damage to either the module or the controller. If a module is installed while the MicroLogix 1500 controller is in an executing mode (Run or Remote Run), the module is not recognized until either a power cycle occurs, or until the controller is placed in a non-executing mode (program mode or fault condition).

Removal of the memory module is detected within one program scan. Removal of the real-time clock under power causes the controller to write zeros to the (RTC) Function File.

## Real-Time Clock Function File

The real-time clock provides year, month, day of month, day of week, hour, minute, and second information to the Real-Time Clock (RTC) Function File in the controller. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for information about the RTC function file.

## Accuracy

Table 26 indicates the accuracy of the real-time clock for various temperatures.

Table 26 - RTC Accuracy

| Ambient Temperature  Accuracy(1)       |
|----------------------------------------|
| 0°C (+32°F) +34…-70 seconds/month      |
| +25°C (+77°F) +36…-68 seconds/month    |
| +40°C (+104°F) +29…-75 seconds/month   |
| +55°C (+131°F) -133…-237 seconds/month |

## Memory Module Operation

## Write Data to the Real-Time Clock

When valid data is sent to the real-time clock from the programming device, the new values take effect immediately.

The real-time clock does not allow you to write invalid date or time data.

## RTC Battery Operation

The real-time clock has an internal battery that is not replaceable. The RTC Function File features a battery low indicator bit (RTC:0/BL), which shows the status of the RTC battery. When the battery is low, the indicator bit is set (1). This means that the battery may fail within 14 days and the real-time clock module needs to be replaced. When the battery low indicator bit is clear (0), the battery level is acceptable or a real-time clock is not attached.

If the RTC battery is low and the controller is powered, the RTC operates normally. If the controller power is removed and the RTC battery is low, RTC data may be lost.

Use the Disable Clock button in your programming device to disable the real-time clock before storing a module. This decreases the drain on the battery during storage.

Table 27 - RTC Battery Life Expectancy

|                               | Battery State Temperature Time Duration                                          |
|-------------------------------|----------------------------------------------------------------------------------|
| Operating 0…40 °C (32…104 °F) | 5 years(1)                                                                       |
| Storage                       | -40…+25 °C (-40…+77 °F) 5 years minimum +26…+60 °C (+79…+140 °F) 3 years minimum |

<!-- image -->

ATTENTION: Operating with a low battery indication for more than 14 days may result in invalid RTC data if controller power is lost.

The memory module supports program back-up as well as the following features:

- User Program and Data Back-Up
- Program Compare
- Data File Download Protection
- Memory Module Write Protection
- Removal/Insertion Under Power
- Memory Module Information File

## User Program and Data Back-Up

The memory module provides a simple and flexible program/data transport mechanism, allowing the user to transfer the program and data to the controller without the use of a personal computer and programming software.

The memory module can store one user program at a time.

During transfers to or from a memory module, the controller's RUN LED flashes.

## Program Compare

The memory module can also provide application security, allowing you to specify that if the program stored in the memory module does not match the program in the controller, the controller will not enter an executing (Run or Remote Run) mode. To enable this feature, set the S:2/9 bit in the system status file. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for more information.

## Data File Download Protection

The memory module allows the user to specify individual data files in the controller that are protected from the download procedure. This allows user data to be saved (not overwritten) during a download.

<!-- image -->

Data file download protection is only functional if the processor does not have a fault and if all protected data files in the memory module exactly match the protected data file structure within the controller. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for information on protecting data files during download.

## Memory Module Write Protection

The memory module supports write-once, read-many behavior. Write protection is enabled using your programming software.

## IMPORTANT

Once set, write protection cannot be removed. A change cannot be made to the control program stored in a write-protected memory module. If a change is required, use a different memory module.

## Removal/Insertion Under Power

The memory module can be installed or removed at any time without risk of damage to either the memory module or the controller, except during a data transaction. If the memory module is removed during a data transaction, data corruption can occur.

If a memory module is installed while the MicroLogix 1500 controller is executing, the memory module will not be recognized until either a power cycle occurs, or until the controller is placed in a non-executing mode (program mode or fault condition).

## Memory Module Information File

The controller has a Memory Module Information (MMI) File which provides status from the attached memory module. At power-up or on detection of a memory module being inserted, the catalog number, series, revision, and type (memory module and/or real-time clock) are identified and written to the MMI file. If a memory module and/or real-time clock is not attached, zeros are written to the MMI file. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for more information.

## Notes:

## MicroLogix 1500 Controller Specifications

## General Specifications

| Description 1764-24BWA 1764-24AWA 1764-28BXB                                                                                                                 |                                                                                                                                                              |                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of I/O  12 inputs 12 outputs                                                                                                                          | 12 inputs 12 outputs                                                                                                                                         | 16 inputs 12 outputs                                                                                                                                         |
| Line power 85…265V AC @ 47…63 Hz                                                                                                                             | 85…265V AC @ 47…63 Hz 20.4…30V DC                                                                                                                            |                                                                                                                                                              |
| Power supply usage 88VA 70VA                                                                                                                                 |                                                                                                                                                              | 30 W(1)                                                                                                                                                      |
| Power supply inrush  120V AC = 25 A for 8 ms 240V AC = 40 A for 4 ms                                                                                         | 120V AC = 25 A for 8 ms 240V AC = 40 A for 4 ms                                                                                                              | 24V DC = 4 A for 150 ms                                                                                                                                      |
| User power output 24V DC @ 400 mA, 400 µF max None None                                                                                                      |                                                                                                                                                              |                                                                                                                                                              |
| Input circuit type 24V DC, sinking/sourcing 120V AC 24V DC, sinking/sourcing                                                                                 |                                                                                                                                                              |                                                                                                                                                              |
| Output circuit type Relay Relay                                                                                                                              |                                                                                                                                                              | 6 relay, 6 FET transistor (24V DC sourcing)                                                                                                                  |
| Typical CPU hold-up time 10…3000 ms                                                                                                                          | Typical CPU hold-up time 10…3000 ms                                                                                                                          | Typical CPU hold-up time 10…3000 ms                                                                                                                          |
| 1.13 N•m (10 lb•in) rated 1.3 N•m (12 lb•in) maximum                                                                                                         | 1.13 N•m (10 lb•in) rated 1.3 N•m (12 lb•in) maximum                                                                                                         | 1.13 N•m (10 lb•in) rated 1.3 N•m (12 lb•in) maximum                                                                                                         |
| For 1764-LSP series A processors: RSLogix 500, version 3.01.09 or later For 1764-LSP and 1764-LRP series B processors: RSLogix 500, version 4.00.00 or later | For 1764-LSP series A processors: RSLogix 500, version 3.01.09 or later For 1764-LSP and 1764-LRP series B processors: RSLogix 500, version 4.00.00 or later | For 1764-LSP series A processors: RSLogix 500, version 3.01.09 or later For 1764-LSP and 1764-LRP series B processors: RSLogix 500, version 4.00.00 or later |

## Environmental Specifications

|                                         | Description 1764-24BWA, 1764-24AWA, 1764-28BXB                                     |
|-----------------------------------------|------------------------------------------------------------------------------------|
| Temperature, operating                  | IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock): °°°° pg  0 °C < Ta < +55 °C (+32 °F < Ta < +131 °F)                                                                                    |
| Temperature, ambient, max 55 °C         |                                                                                    |
| Temperature, surrounding air, max 55 °C |                                                                                    |
| Temperature, nonoperating               | IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock): °° -40…+85 °C (-40…+185 °F)                                                                                    |
| Relative humidty                        | IEC 60068-2-30 (Test Db, Unpackaged Damp Heat): 5…95% noncondensing                |
| Vibration                               | IEC 60068-2-6 (Test Fc, Operating): 5 g @ 10…500 Hz                                |
| Shock, operating                        | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30g panel mounted                      |
| Shock, nonoperating                     | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30g panel mounted 40g DIN rail mounted |
|                                         | Emissions IEC 61000-6-4                                                            |
| ESD immunity                            | IEC 61000-4-2: 4 kV contact discharges 8 kV air discharges                         |
| Radiated RF immunity                    | IEC 61000-4-3: 10V/m with 1 kHz sine-wave 80% AM from 80…6000 MHz                  |

## Specifications

<!-- image -->

## Environmental Specifications (Continued)

|                          | Description 1764-24BWA, 1764-24AWA, 1764-28BXB                                |
|--------------------------|-------------------------------------------------------------------------------|
| EFT/B immunity           | IEC 61000-4-4: ±2 kV @ 5 kHz                                                  |
| Surge transient immunity | IEC 61000-4-5: ±500V line-line(DM) and ±500V line-earth(CM) on DC power ports |
| Conducted RF immunity    | IEC 61000-4-6: 10V rms with 1 kHz sine-wave 80% AM from 150 kHz…80 MHz        |

## Certifications

| Certifications (when product is marked)(1)   | Value                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us                                      | UL Listed Industrial Control Equipment, certified for US and Canada. UL Listed for Class I Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada.                                                                                                                                             |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions European Union 2014/35/EU LVD, compliant with: EN 61131-2; Programmable Controllers (Clause 11) European Union 2011/65/EU RoHS, compliant with: EN IEC 63000; Technical documentation |
| RCM                                          | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                                                                                                                                           |
| Morocco                                      | Arrêté ministériel n° 6404-15 du 1 er muharram 1437 Arrêté ministériel n° 6404-15 du 29 ramadan 1436                                                                                                                                                                                                                |
| UKCA                                         | 2016 No. 1091 – Electromagnetic Compatibility Regulations 2016 No. 1101 – Electrical Equipment (Safety) Regulations 2012 No. 3032 – Restriction of the Use of Certain Hazardous Substances in Electrical and Electronic Equipment Regulations                                                                       |

## Choosing a Power Supply

This section contains information for selecting a power supply for applications using a 1764-28BXB base unit. Use the tables in Appendix F to calculate the total power (Watts) consumed by the system. With that information, use the graphs below to chose a power supply. You can use either current or power, depending on how the power supply is rated.

## Figure 41 - Input Current Required

<!-- image -->

Figure 42 - Input Power Required

<!-- image -->

Table 28 - Input Specifications

|                                                                     | Description 1764-24AWA                              | 1764-24BWA and 1764-28BXB                                | 1764-24BWA and 1764-28BXB                                |
|---------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                                                     |                                                     |                                                          | Inputs 0…7 Inputs 8 and Higher                           |
| On-state voltage range 79…132V AC                                   |                                                     | 14…30.0V DC @ 30 °C (86 °F) 14…26.4V DC @ 55 °C (131 °F) | 10…30.0V DC @ 30 °C (86 °F) 10…26.4V DC @ 55 °C (131 °F) |
| Off-state voltage range 0…20V AC 0…5V DC                            |                                                     |                                                          |                                                          |
| Operating frequency Not applicable 0…20 kHz                         |                                                     |                                                          | 0…500 Hz(1)                                              |
| On-state current: Min Nom Max                                       | 5.0 mA @ 79V AC 12.0 mA @ 120V AC 16.0 mA @ 132V AC | 2.5 mA @ 14V DC 7.3 mA @ 24V DC 12.0 mA @ 30V DC         | 2.0 mA @ 10V DC 8.9 mA @ 24V DC 12.0 mA @ 30V DC         |
| Off-state leakage current, min                                      |                                                     | 2.5 mA 1.5 mA                                            | 2.5 mA 1.5 mA                                            |
| Nominal impedance                                                   | 12 kΩ @ 50 Hz 10 kΩ @ 60 Hz                         | 3.3 kΩ                                                   | 2.7 kΩ                                                   |
| Inrush current, max 250 mA at 120V AC Not applicable Not applicable |                                                     |                                                          |                                                          |

(1) Scan-time dependent.

<!-- image -->

The 1764-24AWA input circuits (inputs 0…11) do not support adjustable filter settings. They have maximum turn-on and maximum turn-off times of 20 milliseconds.

Table 29 - Response Times for High-speed DC Inputs 0… 7 (1764-24BWA and 1764-28BXB)

| Filter Setting (ms) Maximum ON Delay (ms) Maximum OFF Delay (ms)   | Maximum High-speed Counter Frequency @ 50% Duty Cycle (kHz) Minimum ON Delay (ms) Minimum OFF Delay (ms)   |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
|                                                                    | 20.000 0.025 0.005 0.025 0.005 0.025                                                                       |
|                                                                    | 6.700 0.075 0.040 0.075 0.045 0.075                                                                        |
|                                                                    | 5.000 0.100 0.050 0.100 0.060 0.100                                                                        |
| 2.000 0.250 0.170 0.250 0.210 0.250                                |                                                                                                            |
| 1.000 0.500 0.370 0.500 0.330 0.500                                |                                                                                                            |
|                                                                    | 0.500 1.000 0.700 1.000 0.800 1.000                                                                        |
|                                                                    | 0.250 2.000 1.700 2.000 1.600 2.000                                                                        |
|                                                                    | 0.125 4.000 3.400 4.000 3.600 4.000                                                                        |
| 8.000(1)                                                           | 0.063  6.700 8.000 7.300 8.000                                                                             |
| 0.031 16.000 14.000 16.000 14.000 16.000                           |                                                                                                            |

(1) This is the default setting.

Table 30 - Response Times for Normal DC Inputs 8…11 (1764-24BWA) and 8…15 (1764-28BXB)

| Filter Setting (ms) Maximum ON Delay (ms) Maximum OFF Delay (ms)   | Maximum Frequency @ 50% Duty Cycle (kHz) Minimum ON Delay (ms) Minimum OFF Delay (ms)   |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| 1.000 0.500 0.090 0.500 0.020 0.500                                |                                                                                         |
|                                                                    | 0.500 1.000 0.500 1.000 0.400 1.000                                                     |
| 0.250 2.000 1.100 2.000 1.300 2.000                                |                                                                                         |
| 0.125 4.000 2.800 4.000 2.700 4.000                                |                                                                                         |
| 8.000(1)                                                           | 0.063  5.800 8.000 5.300 8.000                                                          |
| 0.031 16.000 11.000 16.000 10.000 16.000                           |                                                                                         |

(1) This is the default setting.

IMPORTANT

The relay current must stay within the limits defined in Table 31 and Table 32 .

Table 31 - Relay Contact Rating Table – 1764-24AWA, 1762-24BWA, 1762-28BXB

| Maximum Volts        | Amperes   | Amperes   | Voltamperes   | Voltamperes   |
|----------------------|-----------|-----------|---------------|---------------|
| Maximum Volts        |           | Amperes Continuous  p Make Break Make Break           |               |               |
| 240V AC 7.5 A 0.75 A |           |           | 2.5 A 1800VA  | 180VA(1)      |
| 120V AC 15 A 1.5 A   |           |           | 2.5 A 1800VA  | 180VA(1)      |
| 125V DC              | 0.22 A(2) | 0.22 A(2) | 1.0 A 28VA    | 1.0 A 28VA    |
| 24V DC               | 1.2 A(2)  | 1.2 A(2)  | 2.0 A 28VA    | 2.0 A 28VA    |

Table 32 - Output Specifications - Maximum Continuous Relay Current

| Specification 1764-24AWA, 1764-24BWA 1764-28BXB   |
|---------------------------------------------------|
| Current per common 8 A 8 A                        |
| Current per controller                            |
| Relay output                                      |
| Relay life - Electrical See Figure 43 .           |
| Relay life - Mechanical 20,000,000 cycles         |

<!-- image -->

ATTENTION: Do not exceed the “Current per common” specification.

Figure 43 - Relay Life Chart

<!-- image -->

Switching capacity(A)

Table 33 - Output Specifications – 1764-28BXB FET

| Specification                                   | General Operation (Outputs 2…7)                      | High-speed Operation (1) (Outputs 2 and 3 Only)        |
|-------------------------------------------------|------------------------------------------------------|--------------------------------------------------------|
| User supply voltage                             |                                                      | Min 20.4V DC 20.4V DC                                  |
| User supply voltage                             |                                                      | Max 26.4V DC 26.4V DC                                  |
| On-state voltage drop                           | @ max load current 1V DC Not applicable              |                                                        |
| On-state voltage drop                           | @ max surge current 2.5V DC Not applicable           |                                                        |
| Current rating per point                        | Max load  1 A @ 55 °C (131 °F) 1.5 A @ 30 °C (86 °F) | 100 mA                                                 |
| Current rating per point                        | Min load 1.0 mA 10 mA                                |                                                        |
| Current rating per point                        | Max leakage 1.0 mA 1.0 mA                            |                                                        |
| Surge current per point                         |                                                      | Peak current 4.0 A Not applicable                      |
| Surge current per point                         | Max surge duration 10 ms Not applicable              |                                                        |
| Surge current per point                         | Max rate of repetition °° p @ 30 °C (86 °F)                                                      | Once every second Not applicable                       |
| Surge current per point                         | Max rate of repetition °° p @ 55 °C (131 °F)                                                      | Once every 2 seconds Not applicable                    |
| Current per common Max total 6 A Not applicable |                                                      |                                                        |
|                                                 |                                                      | On-state current Min 2.5 mA @ 14V DC 2.0 mA @ 10V DC   |
| Off-state leakage current Max 1 mA 1 mA         |                                                      |                                                        |
| Turn-on time Max 0.1 ms 6 µs                    |                                                      |                                                        |
| Turn-off time Max 1.0 ms 18 µs                  |                                                      |                                                        |
| Repeatability Max Not applicable 2 µs           |                                                      |                                                        |
|                                                 |                                                      | Drift Max Not applicable 1 µs per 5 °C (1 µs per 9 °F) |

## Table 34 - Working Voltage – 1764-24AWA

| Specification 1764-24AWA                                                    |                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power supply input to backplane isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 151V AC for 1 second or 2145V DC for 1 second 132V Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Output group to backplane isolation                                         | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Output group to output group isolation                                      | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Table 35 - Working Voltage – 1764-24BWA

| Specification 1764-24BWA                                                    |                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power supply input to backplane isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Power supply user 24V output to backplane isolation                         | Verified by one of the following dielectric tests: 600V AC for 1 second or 848V DC for 1 second 50V Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 second or 1697V DC for 1 second 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                       |
| Output group to backplane isolation                                         | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Output group to output group isolation                                      | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Table 36 - Working Voltage – 1764-28BXB

| Specification 1764-28BXB                                                    |                                                                                                   |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 second or 1697V DC for 1 second |
| Input group to backplane isolation and input group to input group isolation | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                        |
| FET output group to backplane isolation and FET outputs group to group      | Verified by one of the following dielectric tests: 1200V AC for 1 second or 1697V DC for 1 second |
| FET output group to backplane isolation and FET outputs group to group      | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                        |
| Relay output group to backplane isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second |
| Relay output group to backplane isolation                                   | 265V Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Relay output group to relay and FET output group isolation                  | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second |
| Relay output group to relay and FET output group isolation                  | 265V Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation)  |

## Controller Dimensions

See Base Unit Mounting Dimensions on page 26 for more information.

<!-- image -->

## Compact I/O Dimensions

## Panel Mounting

<!-- image -->

## End Cap

This illustration shows the 1769-ECR right end cap. For the 1769-ECL left end cap, the drawing would be reversed.

<!-- image -->

## Notes:

## MicroLogix 1500 Replacement Kits

## Lithium Battery (1747-BA)

## Replacement Parts

Table 37 provides a list of replacement parts and their catalog number.

Table 37 - MicroLogix 1500 Controller Replacement Parts

| Description Catalog Number                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| Lithium battery 1747-BA                                                                                                                   |
| ESD barrier 1764-RPL-TRM1                                                                                                                 |
| Base terminal doors 1764-RPL-TDR1                                                                                                         |
| Processor access door 1764-RPL-CDR1                                                                                                       |
| Door combination kit, includes ESD barrier, terminal door, access door, base comms door, and trimpots/mode switch cover door  1764-RPL-DR |
| 17-point terminal block (for inputs on 1764-24AWA and 1764-24BWA bases) 1764-RPL-TB1                                                      |
| 21-point terminal block (for inputs of 1764-28BXB and outputs for all base units) 1764-RPL-TB2                                            |

## IMPORTANT

## Installation

IMPORTANT

Do not remove the permanent battery when installing a replacement battery.

Follow the procedure below to ensure proper replacement battery installation.

1. Insert battery into replacement battery pocket with wires facing up.
2. Insert replacement battery wire connector into connector port.
3. Secure battery wires under wire latch, as shown in Figure 44 .

Figure 44 - Install Replacement Battery

<!-- image -->

When the processor's Battery Low indicator is lit, install a backup battery immediately. After the indicator turns on, the battery lasts for at least:

- 14 days for the 1764-LSP
- 7 days for the 1764-LRP

<!-- image -->

## Battery Handling

Follow the procedure below to ensure proper battery operation and reduce personnel hazards.

- Use only for the intended operation.
- Do not ship or dispose of cells except according to recommended procedures.
- Do not ship on passenger aircraft.

<!-- image -->

## Storage

Store lithium batteries in a cool, dry environment, typically 20…25 °C (68…77 °F) and 40…60% humidity. Store the batteries and a copy of the battery instruction sheet in the original container, away from flammable materials.

## Transportation

One or Two Batteries

Each battery contains 0.23 g (0.008 oz.) of lithium. Therefore, up to two batteries can be shipped together within the United States without restriction. Regulations governing shipment to or within other countries may differ.

## Three or More Batteries

Procedures for the transportation of three or more batteries shipped together within the United States are specified by the Department of Transportation (DOT) in the Code of Federal Regulations, CFR49, "Transportation." An exemption to these regulations, DOT - E7052, covers the transport of certain hazardous materials classified as flammable solids. This exemption authorizes transport of lithium batteries by motor vehicle, rail freight, cargo vessel, and cargoonly aircraft, providing certain conditions are met. Transport by passenger aircraft is not permitted.

A special provision of DOT-E7052 (11 th Rev., October 21, 1982, par. 8-a) provides that:

"Persons that receive cell and batteries covered by this exemption may reship them pursuant to the provisions of 49 CFR 173.22a in any of these packages authorized in this exemption including those in which they were received."

The Code of Federal Regulations, 49 CFR 173.22a, relates to the use of packaging authorized under exemptions. In part, it requires that you must maintain a copy of the exemption at each facility where the packaging is being used in connection with shipment under the exemption.

Shipment of depleted batteries for disposal may be subject to specific regulation of the countries involved or to regulations endorsed by those countries, such as the IATA Articles Regulations of the International Air Transport Association, Geneva, Switzerland.

IMPORTANT

Regulations for transportation of lithium batteries are periodically revised. See www.dot.gov for the latest shipping information.

## ATTENTION:

- Do not charge the batteries. An explosion could result or the cells could overheat causing burns.
- Do not open, puncture, crush, or otherwise mutilate the batteries. A possibility of an explosion exists and/or toxic, corrosive, and flammable liquids would be exposed.
- Do not incinerate or expose the batteries to high temperatures. Do not attempt to solder batteries. An explosion could result.
- Do not short positive and negative terminals together. Excessive heat can build up and cause severe burns.

## Replacement Terminal Blocks

## Disposal

<!-- image -->

ATTENTION: Do not incinerate or dispose of lithium batteries in general trash collection. Explosion or violent rupture is possible. Batteries should be collected for disposal in a manner to prevent against short-circuiting, compacting, or destruction of case integrity and hermetic seal.

For disposal, batteries must be packaged and shipped in accordance with transportation regulations, to a proper disposal site. The U.S. Department of Transportation authorizes shipment of "Lithium batteries for disposal" by motor vehicle only in regulation 173.1015 of CFR 49 (effective January 5, 1983). For additional information contact:

U.S. Department of Transportation Research and Special Programs Administration 400 Seventh Street, S.W. Washington, D.C. 20590

Although the Environmental Protection Agency at this time has no regulations specific to lithium batteries, the material contained may be considered toxic, reactive, or corrosive. The person disposing of the material is responsible for any hazard created in doing so. State and local regulations may exist regarding the disposal of these materials.

For a lithium battery product safety data sheet, contact the manufacturer:

Sanyo Energy Corporation Tadarand U.S. Battery Division San Diego, CA 92173 Port Washington, NY 11050

2001 Sanyo Avenue 2 Seaview Blvd. (619) 661-4801 (516) 621-4980

This figure illustrates how to replace the MicroLogix 1500 terminal blocks.

## Catalog Numbers:

- 1764-RPL-TB1: 17-point terminal block
- 1764-RPL-TB2: 21-point terminal block

<!-- image -->

## Replacement Doors

The following figures illustrate the procedure for installing the MicroLogix 1500 replacement doors.

Base Terminal Door (1764-RPL-TDR1)

Processor Access Door (1764-RPL-CDR1)

Base Comms Door (included in 1764-RPL-DR)

Trimpots/Mode Switch Cover Door (included in 1764-RPL-DR)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Understand the Controller Status Indicators

## Troubleshoot Your System

The controller status indicators provide a mechanism to determine the current status of the controller if a programming device is not present or available.

Figure 45 - Controller Status Indicator Location

<!-- image -->

Table 38 - Controller Status Indicators

| Status Indicator Color Indicates   |                                                                                  |
|------------------------------------|----------------------------------------------------------------------------------|
| POWER                              | Off No input power or power error condition                                      |
| POWER                              | Steady green Power on                                                            |
| RUN                                | Off Controller is not in Run mode or REM Run                                     |
| RUN                                | Steady green Controller is in Run mode or REM Run                                |
| RUN                                | Flashing green System is not in Run mode; memory module transfer is in progress  |
| FAULT                              | Off No fault detected                                                            |
| FAULT                              | Flashing red Faulted user program                                                |
| FAULT                              | Steady red Processor hardware fault or critical fault                            |
| FORCE                              | Off No forces installed                                                          |
| FORCE                              | Steady amber Forces installed                                                    |
| BATTERY LOW                        | Off Battery OK                                                                   |
| BATTERY LOW                        | Steady red Battery needs replacement (See Lithium Battery (1747-BA) on page 85.) |
| COMM 0                             | Flashes when communications are active                                           |
| COMM 1 (1764-LRP only)             | Flashes when communications are active                                           |
| DCOMM(1)                           | Off User configured communications mode is active                                |
| DCOMM(1)                           | Steady green Default communications mode active                                  |
| INPUTS                             | Off Input is not energized                                                       |
| INPUTS                             | Steady amber Input is energized (logic status)                                   |
| OUTPUTS                            | Off Output is not energized                                                      |
| OUTPUTS                            | Steady amber Output is energized (logic status)                                  |

<!-- image -->

Table 39 - Status Indicator Error Conditions

|                                     | If the LEDS Indicate The Following Error Exists Probable Cause Recommended Action   |                                        |                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All LEDS off                        | No input power or power supply error                                                |                                        | No line power Verify proper line voltage and connections to the controller.                                                                                                                                                                                                                                                                                                        |
| All LEDS off                        | No input power or power supply error                                                | Power supply overloaded                | This problem can occur intermittently if power supply is overloaded when output loading and temperature varies.                                                                                                                                                                                                                                                                    |
| Power and FAULT LEDs on solid       | Hardware faulted                                                                    | Processor hardware error               | Cycle power. Contact your local Rockwell Automation representative if the error persists.                                                                                                                                                                                                                                                                                          |
| Power and FAULT LEDs on solid       | Hardware faulted                                                                    |                                        | Loose wiring Verify connections to the controller.                                                                                                                                                                                                                                                                                                                                 |
| Power LED on and FAULT LED flashing | Application fault                                                                   | Hardware/software major fault detected | 1. Monitor Status File Word S:6 for major error code. See Identifying Controller Faults on page 92 for more information. 2. Remove hardware/software condition causing fault. 3. Clear Major Error Halted flag, bit S2:1/13. 4. Attempt a controller Run mode entry. If unsuccessful, repeat recommended action steps above or contact your local Rockwell Automation distributor. |

## Normal Operation

The POWER and RUN status indicators are On. If a force condition is active, the FORCE status indicator turns on and remains on until all forces are removed.

## Error Conditions

If an error exists within the controller, the controller status indicators operate as described in Table 39 .

## Controller Error Recovery Model

Figure 46 helps you diagnose software and hardware problems in the micro controller. The model provides common questions you might ask to help troubleshoot your system. See the recommended pages within the model for further help.

Figure 46 - Controller Error Recovery Model

<!-- image -->

Identifying Controller Faults While a program is executing, a fault may occur within the operating system or your program.
fiiifi When a fault occurs, you have various options to determine what the fault is and how to correct it. This section describes how to clear faults and provides a list of possible advisory messages with recommended corrective actions.

## Automatically Clearing Faults

You can automatically clear a fault by cycling power to the controller when the Fault Override at Power-up bit (S:1/8) is set in the status file.

You can also configure the controller to clear faults and go to RUN every time the controller is power cycled. This is a feature that OEMs can build into their equipment to allow end users to reset the controller. If the controller faults, it can be reset by simply cycling power to the machine. To accomplish this, set the following bits in the status file:

- S2:1/8 - Fault Override at Power-up
- S2:1/12 - Mode Behavior

If the fault condition still exists after cycling power, the controller re-enters the fault mode. For more information on status bits, see MicroLogix 1200 and MicroLogix 1500 Programable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

<!-- image -->

You can declare your own application-specific major fault by writing your own unique value to S:6 and then setting bit S:1/13 to prevent reusing system defined codes. The recommended values for user defined faults are FF00 to FF0F.

## Manually Clearing Faults Using the Fault Routine

The occurrence of recoverable or non-recoverable user faults can cause the user fault subroutine to be executed. If the fault is recoverable, the subroutine can be used to correct the problem and clear the fault bit S:1/13. The controller then continues in the Run or test mode.

The subroutine does not execute for non-user faults. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for information on creating a user fault subroutine.

## Fault Messages

See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for the controller fault messages that can occur during operation of the MicroLogix 1500 programmable controllers. Each fault message includes the error code description, the probable cause, and the recommended corrective action.

If you need to contact Rockwell Automation or local distributor for assistance, it is helpful to obtain the following (prior to calling):

- Controller type, series letter, and revision letter of the base unit
- Series letter, revision letter, and firmware (FRN) number of the processor (on bottom side of processor unit)
- Controller indicator status
- Controller error codes (found in S2:6 of status file)

## Calling Rockwell Automation for Assistance

## Prepare for Firmware Update

## Perform the Firmware Update

## Missing or Corrupt OS LED Pattern

## Upgrade Your Operating System

The operating system (OS) can be upgraded through the communication port on the controller. To download a new operating system, you must have the ControlFLASH™ Upgrade Kit, which is described in the ControlFLASH User Manual, publication 1756-UM105 .

The newer OS firmware for the controller is prepared in DMK disk image format which requires ControlFLASH version 13.00 or later.

To download new OS firmware for a MicroLogix controller, go to the Rockwell Automation Product Compatibility and Download Center (PCDC) at rok.auto/pcdc .

Before upgrading the controller's operating system, you must:

- Install ControlFLASH software on your computer.
- Extract the DMK kit containing the latest firmware (for ControlFLASH version 13.00 or later only).
- Install the ControlFLASH software. Double-click the processor catalog number/firmware revision number to install the OS upgrade.
- Prepare the controller for updating.

## IMPORTANT

Installing a new operating system deletes the user program.

## Install ControlFLASH Software

To install ControlFLASH properly, see the Install ControlFLASH section in ControlFLASH User Manual, publication 1756-UM105 .

If a ControlFLASH directory does not exist, one is created in your Program Files directory.

## Prepare the Controller for Firmware Update

Controller Configuration

The controller must be configured for default communications (use Communications Toggle push button; DCOMM LED on) and be in the Program mode to allow the download of a new operating system.

The following steps occur during the upgrade process.

1. The controller mode and communications parameters are checked.
2. The download begins.
3. During the download, the Force, Battery, and Comms LEDs perform a walking bit pattern.
4. When the download is complete, the integrity of the new OS is checked. If the new OS is corrupt, the controller sends an error message to the computer and flashes the Missing or Corrupt OS LED pattern. See Missing or Corrupt OS LED Pattern on page 93 .
5. Following a successful transfer, the Power, Force, and Battery LEDs flash on and remain on for five seconds. Then the controller resets.

When an OS download is not successful or if the controller does not contain a valid OS, the controller flashes the Run, Force, and Fault LEDS on and off.

<!-- image -->

## Notes:

## RS-232 Communication Interface

## DF1 Full-duplex Protocol

## DF1 Half-duplex Protocol

<!-- image -->

## Understand Communication Protocols

Use the information in this appendix to understand the differences in communication protocols. The following protocols are supported from the RS-232 communication channel:

- DF1 Full-duplex
- DF1 Half-duplex slave
- DH-485
- Modbus RTU slave (1764-LSP and 1764-LRP series B processors only)
- ASCII (1764-LSP and 1764-LRP series B processors only)

See Communication Connections on page 47 for information about required network devices and accessories.

The communications port on the MicroLogix 1500 controller utilizes an RS-232 interface. RS-232 is an Electronics Industries Association (EIA) standard that specifies the electrical characteristics for serial binary communication. It provides you with a variety of system configuration possibilities. RS-232 defines electrical connection characteristics; not protocols.

One of the biggest benefits of an RS-232 interface is that it lets you integrate telephone and radio modems into your control system (using the appropriate DF1 protocol only, not DH-485 protocol), but it is for point-to-point connections only between two devices.

DF1 Full-duplex protocol provides a point-to-point connection between two devices. DF1 FullDuplex protocol combines data transparency (American National Standards Institute ANSI X3.28-1976 specification subcategory D1) and 2-way simultaneous transmission with embedded responses (subcategory F1).

MicroLogix 1500 controllers support the DF1 Full-duplex protocol via RS-232 connection to external devices such as computers, or other controllers that support DF1 Full-duplex.

DF1 is an open protocol. See the DF1 Protocol and Command Set Reference Manual, publication 1770-RM516, for more information.

DF1 Full-duplex protocol (also referred to as DF1 point-to-point protocol) is useful where RS-232 point-to-point communication is required. DF1 protocol controls message flow, detects and signals errors, and retries if errors are detected.

For information about required network connecting equipment and examples of DF1 Fullduplex connections, see Communication Connections on page 47 .

DF1 Half-duplex protocol is a multi-drop single master/multiple slave network. DF1 Half-duplex protocol supports data transparency (American National Standards Institute ANSI - X3.28-1976 specification subcategory D1). In contrast to DF1 Full-duplex, communication takes place in one direction at a time. With an active Half-duplex master, you can use the RS-232 port on the MicroLogix 1500 controller as a Half-duplex programming port and a Half-duplex peer-to-peer messaging port.

## DF1 Half-duplex Operation

A DF1 Half-duplex master device initiates all communication by polling each slave device. The slave device can only transmit when it is polled by the master. It is the master's responsibility to poll each slave on a regular and sequential basis to allow slave devices an opportunity to communicate.

An additional feature of the DF1 Half-duplex protocol is that it is possible for a slave device to enable a MSG write or read to/from another slave. When the initiating slave is polled, the MSG is sent to the master. The master recognizes that the message is not intended for it, but for another slave, so the master immediately forwards the message to the intended slave. The master does this automatically; you do not need to program the master to move data between slave nodes. This slave-to-slave transfer can also be used by programming software to allow slave-to-slave upload and download of programs to processors (including the master) on the DF1 Half-duplex link.

A MicroLogix 1500 controller can only act as a slave device. A device that can act as a master is required to run the network. Several other Allen-Bradley products support the DF1 Half-duplex master protocol. They include the SLC 5/03 and higher processors, enhanced PLC-5 processors, and RSLinx software version 2.x or later.

DF1 Half-duplex supports up to 255 devices (address 0…254) with address 255 reserved for master broadcasts. The MicroLogix 1500 controller supports broadcast reception.

## Considerations When Communicating as a DF1 Slave on a Multi-drop Link

When communication is between either your programming software and a MicroLogix Programmable Controller or between two MicroLogix 1500 controllers via slave-to-slave communication on a larger multi-drop link, the devices depend on a DF1 Half-duplex master to give each of them access in a timely manner. As the number of slave devices increase, the time between when slave devices are polled also increases. This increase in time may also be large if you are using low communication rates. As these time periods grow, consider increasing the poll timeout and reply timeout values for slave devices.

## IMPORTANT

If a program download is started when using DF1 Half-duplex, but then is interrupted due to electromagnetic interference or other events, discontinue communications to the controller for the ownership timeout period and then restart the program download. The ownership timeout period is 60 seconds. After the timeout, you can re-establish communications with the processor and try the program download again. The only other way to remove program ownership is to cycle power on the processor.

## Use Modems with MicroLogix Programmable Controllers

The types of modems that you can use with MicroLogix controllers include the following:

- Dial-up phone modems

A MicroLogix controller, on the receiving end of the dial-up connection, can be configured for DF1 Full-duplex protocol with or without handshaking. The modem connected to the MicroLogix controller should support auto-answer. The MicroLogix 1500 series B processors (1764-LSP and 1764-LRP) support ASCII out communications. Therefore, they can cause the modem to initiate or disconnect a phone call.

- Leased-line modems

Leased-line modems are used with dedicated phone lines that are typically leased from the local phone company. The dedicated lines can be in a point-to-point topology to support Full-duplex communications between two modems or in a multi-drop topology to support Half-duplex communications between three or more modems.

## DH-485 Communication Protocol

- Radio modems

Radio modems can be implemented in a point-to-point topology to support either Halfduplex or Full-duplex communications, or in a multi-drop topology to support Halfduplex communications between three or more modems.

- Line drivers

Line drivers, also called short-haul modems, do not actually modulate the serial data, but rather condition the electrical signals to operate reliably over long transmission distances (up to several miles). Line drivers are available in Full-duplex and Half-duplex models. Allen-Bradley's AIC+ Advanced Interface Converter is a Half-duplex line driver that converts an RS-232 electrical signal into an RS-485 electrical signal, increasing the signal transmission distance from 15…1219 meters (50…4000 feet) [2438 meters (8000 feet) when bridged].

For point-to-point Full-duplex modem connections that do not require any modem handshaking signals to operate, use DF1 Full-duplex protocol with no handshaking. For pointto-point Full-duplex modem connections that require RTS/CTS handshaking, use DF1 Fullduplex protocol with handshaking.

For multi-drop modem connections, or for point-to-point modem connections that require RTS/CTS handshaking, use DF1 Half-duplex slave protocol.

## IMPORTANT

Never attempt to use DH-485 protocol through modems under any circumstance.

<!-- image -->

All MicroLogix controllers support RTS/CTS modem handshaking when configured for DF1 Full-duplex protocol with the control line parameter set to Full-duplex Modem Handshaking or DF1 Half-duplex slave protocol with the control line parameter set to "Half-duplex Modem". No other modem handshaking lines (Data Set Ready, Carrier Detect, and Data Terminal Ready) are supported by any MicroLogix 1500 controllers. MicroLogix 1500 1764-LRP processors also support DCD (Data Carrier Detect)

The DH-485 protocol defines the communication between multiple devices that coexist on a single pair of wires. DH-485 protocol uses RS-485 Half-duplex as its physical interface. RS-485 is a definition of electrical connection characteristics; it is not a protocol. RS-485 uses devices that can coexist on a common data circuit, thus allowing data to be easily shared between devices.

The DH-485 network offers:

- Interconnection of 32 devices
- Multi-master (peer-to-peer) capability
- Token passing access control
- The ability to add or remove nodes without disrupting the network
- Maximum network segment of 1219 m (4000 ft.)

The DH-485 protocol supports two classes of devices: initiators and responders. All initiators on the network get a chance to initiate message transfers. To determine which initiator has the right to transmit, a token passing algorithm is used.

Control of message transfers on the DH-485 network is performed by rotating the token along the nodes on the network. A node holding the token can send a message onto the network. Each node is allowed a fixed number of transmissions (based on the Token Hold Factor) each time it receives the token. After a node sends a message, it passes the token to the next device.

The allowable range of node addresses is 1…31. There must be at least one initiator on the network (such as a MicroLogix controller, or an SLC 5/02 or later processor).

## DH-485 Configuration Parameters

When MicroLogix communications are configured for DH-485, the following parameters can be changed:

Table 40 - DF1 Full-duplex Configuration Parameters

| Parameter Options              |
|--------------------------------|
| Communication Rate 9600, 19.2K |
| Node Address 1…31 decimal      |
| Token Hold Factor 1…4          |

See Software Considerations on page 99 for tips on setting the parameters listed above.

## Devices that use the DH-485 Network

In addition to the MicroLogix controllers, the devices that are shown in Table 41 also support the DH-485 network.

Table 41 - Devices that Support a DH-485 Network

| Catalog Number Description Installation Function Publication                                                                       |                                                    |                                                                                                                                                                                                   |                                  |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
|                                                                                                                                    |                                                    | Bulletin 1762 MicroLogix 1200 Series A or later These controllers support DH-485 communications.                                                                                                  | 1762-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1763 MicroLogix 1100 Series A or later These controllers support DH-485 communications.                                                                                                  | 1763-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1766 MicroLogix 1400 Series A or later These controllers support DH-485 communications.                                                                                                  | 1766-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1747 Processors SLC 500 Processors SLC™ Chassis These processors support a variety of I/O requirements and functionality.                                                                | 1747-UM011                       |
|                                                                                                                                    | 1746-BAS BASIC Module SLC Chassis                  | Provides an interface for SLC 500 devices to foreign devices. Program in BASIC to interface the 3 channels (2 RS232 and 1 DH-485) to printers, modems, or the DH-485 network for data collection. | 1746-UM004 1746-PM001 1746-RM001 |
|                                                                                                                                    |                                                    | 1784-KTX, 1784-KTXD PC DH-485 IM PCI Computer Bus Provides DH-485 using RSLinx software                                                                                                           | 1784-UM522                       |
| 1784-PCMK PCMCIA IM                                                                                                                |                                                    | PCMCIA slot in computer  Provides DH-485 using RSLinx software                                                                                                                                    | 1784-UM519                       |
| 2711-K5A2, 2711-B5A2, 2711-K5A5, 2711-B5A5, 2711-K5A1, 2711-B5A1, 2711-K9A2, 2711-T9A2, 2711-K9A5, 2711-T9A5, 2711-K9A1, 2711-T9A1 | PanelView 550 and PanelView 900 Operator Terminals | Panel Mount Provides electronic operator interface for SLC 500 processors                                                                                                                         | 2711-UM014                       |

## Important DH-485 Network Planning Considerations

Carefully plan your network configuration before installing any hardware. Some of the factors that can affect system performance are:

- Amount of electrical noise, temperature, and humidity in the network environment
- Number of devices on the network
- Connection and grounding quality in installation
- Amount of communication traffic on the network
- Type of process being controlled
- Network configuration

The major hardware and software issues you must resolve before installing a network are discussed in the following sections.

## Hardware Considerations

You must decide the length of the communication cable, where you route it, and how to protect it from the environment where it will be installed.

When the communication cable is installed, you must know how many devices are to be connected during installation and how many devices can be added in the future. The following sections help you understand and plan the network.

## Number of Devices and Length of Communication Cable

The maximum length of the communication cable is 1219 m (4000 ft.). This is the total cable distance from the first node to the last node in a segment. However, two segments can be used to extend the DH-485 network to 2438 m (8000 ft.). for additional information on connections using the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

## Planning Cable Routes

Follow these guidelines to help protect the communication cable from electrical interference:

- Keep the communication cable at least 1.52 m (5 ft.) from any electric motors, transformers, rectifiers, generators, arc welders, induction furnaces, or sources of microwave radiation.
- If you must run the cable across power feed lines, run the cable at right angles to the lines.
- If you do not run the cable through a contiguous metallic wireway or conduit, keep the communication cable at least 0.15 m (6 in.) from AC power lines of less than 20 A, 0.30 m (1 ft.) from lines greater than 20 A, but only up to 100 kVA, and 0.60 m (2 ft.) from lines of 100 kVA or more.
- If you run the cable through a contiguous metallic wireway or conduit, keep the communication cable at least 0.08 m (3 in.) from AC power lines of less than 20 A, 0.15 m (6 in.) from lines greater than 20 A, but only up to 100 kVA, and 0.30 m (1 ft.) from lines of 100 kVA or more.

Run the communication cable through a conduit to provide extra protection from physical damage and electrical interference. If you route the cable through a conduit, follow these additional recommendations:

- Use ferromagnetic conduits near critical sources of electrical interference. You can use aluminum conduits in non-critical areas.
- Use plastic connectors to couple between aluminum and ferromagnetic conduit. Make an electrical connection around the plastic connector (use pipe clamps and the heavy gauge wire or wire braid) to hold both sections at the same potential.
- Ground the entire length of conduit by attaching it to the building earth ground.
- Do not let the conduit touch the plug on the cable.
- Arrange the cables loosely within the conduit. The conduit should contain only serial communication cables.
- Install the conduit so that it meets all applicable codes and environmental specifications.

For more information on planning cable routes, see Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

## Software Considerations

Software considerations include the configuration of the network and the parameters that can be set to the specific requirements of the network. The following are major configuration factors that have a significant effect on network performance:

- Number of nodes on the network
- Addresses of those nodes
- Communication rate

The following sections explain network considerations and describe ways to select parameters for optimum network performance (speed). See your programming software's user manual for more information.

## Number of Nodes

The number of nodes on the network directly affects the data transfer time between nodes. Unnecessary nodes (such as a second programming terminal that is not being used) slow the data transfer rate. The maximum number of nodes on the network is 32.

## Setting Node Addresses

The best network performance occurs when node addresses are assigned in sequential order. Assign initiators, such as computers, the lowest numbered addresses to minimize the time that is required to initialize the network. The valid range for the MicroLogix controllers is 1…31 (controllers cannot be node 0). The default setting is 1. The node address is stored in the controller Communications Status file (CS0:5/0 to CS0:5/7).

## Setting Controller Communication Rate

The best network performance occurs at the highest communication rate, which is 19,200. 19,200 is the default communication rate for a MicroLogix device on the DH-485 network. All devices must be at the same communication rate. This rate is stored in the controller Communications Status file (CS0:5/8 to CS0:5/15).

## Setting Maximum Node Address

Once you have an established network set up and are confident that you are not adding more devices, you can enhance performance by adjusting the maximum node address of your controllers. Set it to the highest node address being used.

## IMPORTANT Set all devices to the same maximum node address.

## MicroLogix Remote Packet Support

MicroLogix controllers can respond and initiate with device's communications (or commands) that do not originate on the local DH-485 network. This is useful in installations where communication is needed between the DH-485 and DH+™ networks.

The example below shows how to send messages from a device on the DH+ network to a MicroLogix controller on the DH-485 network. This method uses an SLC 5/04 processor as the bridge connection.

When using this method as shown in Figure 47:

- PLC-5 devices can send read and write commands to MicroLogix controllers.
- MicroLogix controllers can respond to MSG instructions received.
- MicroLogix controllers can initiate MSG instructions to devices on the DH+ network.
- The computer can send read and write commands to MicroLogix controllers.
- The computer can do remote programming of MicroLogix controllers.

Figure 47 - Communication Between DH-485 and DH+ Networks with MicroLogix Controllers

<!-- image -->

## Modbus RTU Slave Communication Protocol

Table 42 - Modbus to MicroLogix Memory Map

| Modbus Addressing Description                                                                 |                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------|
|                                                                                               | File Type Data File Number Address |
| 0001…4096 Read/write Modbus coil data space Bit (B) or Integer (N) 3…255 Bits 0…4095          |                                    |
| 10001…14096 Read-only Modbus contact data space Bit (B) or Integer (N) 3…255 Bits 0…4095      |                                    |
| 30001…30256 Read-only Modbus input register space Bit (B) or Integer (N) 3…255 Words 0…255    |                                    |
| 30501…30532 Modbus communication parameters Communication Status Files 2 Words 0…31           |                                    |
| 31501…31566 Read-only system status file space Status (S) 2 Words 32…65                       |                                    |
| 40001…40256 Read/write Modbus holding register space Bit (B) or Integer (N) 3…255 Words 0…255 |                                    |
| 41501…41566 Read/write system status file space Status (S) 2 Words 0…65                       |                                    |

For more information on how to configure your MicroLogix 1500 controller for Modbus RTU slave protocol, see the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001. For more information about the Modbus protocol, see the Modbus Protocol Specifications (available from www.modbus.org).

## IMPORTANT

This section applies to MicroLogix 1500, 1764-LSP and 1764-LRP, series B and later processors only.

Modbus RTU slave is a Half-duplex, master-slave communications protocol. The Modbus network master initiates and controls all communications on the network. Modbus protocol allows a single master to communicate with a maximum of 255 slave devices.

When a MicroLogix 1200 or MicroLogix 1500 Communications port is configured for Modbus RTU slave operation, you must define where Modbus data (coils, contacts, and registers) is mapped into the MicroLogix data space.

The Modbus address space is comprised of seven distinct memory ranges. Four of these ranges can be mapped into MicroLogix data files. Three Modbus ranges are fixed to MicroLogix file 2, the Status file. Table 42 illustrates the Modbus to MicroLogix mappings.

## ASCII Protocol

## IMPORTANT

This section applies to MicroLogix 1500, 1764-LSP and 1764-LRP, series B and later processors only.

ASCII protocol provides connection to other ASCII devices, such as bar code readers, weigh scales, serial printers, and other intelligent devices.

You can use ASCII protocol by configuring the RS-232 port, channel 0 for ASCII driver (For the 1764-LRP only, you can select either Channel 0 or Channel 1).

See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for detailed configuration information.

When the driver is set to ASCII, the parameters described in Table 43 can be changed.

Table 43 - ASCII Channel Configuration Parameters

|                         | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Programming Software Default   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
|                         | Baud Rate Toggles between the communication rate of 300, 600, 1200, 2400, 4800, 9600, 19.2K, and 38.4K 1200                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                |
|                         | Parity Toggles between None, Odd, and Even None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                |
| Termination 1           | Specifies the first termination character. The termination character defines the one or two character sequence used to specify the end of an ASCII line received. Setting the first ASCII termination character to undefined (\ff) indicates no ASCII receiver line termination is used.                                                                                                                                                                                                                                                                                                                                                                                                                  | \d                             |
| Termination 2           | Specifies the second termination character. The termination character defines the one or two character sequence used to specify the end of an ASCII line received. Setting the second ASCII Termination character to undefined (\ff) and the first ASCII Termination character to a defined value (\d) indicates a single character termination sequence.                                                                                                                                                                                                                                                                                                                                                 | \ff                            |
|                         | Control Line Toggles between No Handshaking, Half-duplex Modem, and Full-duplex Modem No Handshaking                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                |
| Delete Mode             | The Delete Mode allows you to select the mode of the “delete” character. Toggles between Ignore, CRT, and Printer. Delete Mode affects the characters echoed back to the remote device. When Delete Mode is enabled, the previous character is removed from the receive buffer. • In CRT mode, when a delete character is encountered, the controller echos three characters to the device: backspace, space, and backspace. This erases the previous character on the terminal. • In Printer Mode, when a delete character is encountered, the controller echos the slash character, then the deleted character. Enable the Echo parameter to use Delete Mode.                                           | Ignore                         |
| Echo                    | When Echo Mode is enabled, all of the characters received are echoed back to the remote device. This allows you to view characters on a terminal connected to the controller. Toggles between Enabled and Disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Disabled                       |
| XON/XOFF                | Allows you to Enable or Disable XON/ XOFF software handshaking. XON/XOFF software handshaking involves the XON and XOFF control characters in the ASCII character set. When the receiver receives the XOFF character, the transmitter stops transmitting until the receiver receives the XON character. If the receiver does not receive an XON character after 60 seconds, the transmitter automatically resumes sending characters. Also, when the receive buffer is more than 80% full, an XOFF character is sent to the remote device to pause the transmission. Then, when the receive buffer drops to less than 80% full, an XON character is sent to the remote device to resume the transmission. | Disabled                       |
| RTS Off Delay (x20 ms)  | Allows you to select the delay between when a transmission is ended and when RTS is dropped. Specify the RTS Off Delay value in increments of 20 ms. Valid range is 0…65535.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0                              |
| RTS Send Delay (x20 ms) | Allows you to select the delay between when RTS is raised and the transmission is initiated. Specify the RTS Send Delay value in increments of 20 ms. Valid range is 0…65535.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 0                              |

## System Loading Calculations

## System Expansion Calculations

<!-- image -->

## System Loading and Heat Dissipation

When you connect MicroLogix accessories and expansion I/O, an electrical load is placed on the base unit power supply. This section shows how to calculate the load and validate that the system will not exceed the capacity of the base unit power supply or expansion power supply.

The following example is provided to illustrate system loading calculation. The system validation procedure accounts for the amount of 5V DC and 24V DC current consumed by controller, expansion I/O, and user supplied equipment.

Current consumed by the base units, memory modules, real-time clock modules, and the end cap terminators (for systems utilizing Compact I/O expansion) has already been factored into the calculations. A system is valid if the current and power requirements are satisfied.

<!-- image -->

An end cap terminator (1769-ECR or 1769-ECL) is needed for any system using Compact I/O expansion module.

## IMPORTANT

In a MicroLogix 1500 system, a maximum of one 1769 expansion cable can be used, allowing for two banks of I/O modules. One bank is connected directly to the controller and the other is connected with the expansion cable. The bank connected to the controller uses the controller's embedded power supply. The bank connected with the cable requires its own power supply.

## Select System Devices

1. Use Table 44 to select the processor and optional communications or display devices. Enter a 1 in the Select Devices column.
2. Enter the current draw values in the Calculated Current for System columns. If an external power supply will be used to power communication devices, do not include their current draw values in this calculation. Add up the current draw values to determine the SUBTOTAL1 values.
3. Use Table 45 to select the I/O modules. Enter the number of modules in either the Base Unit Expansion or the Bank 1 column.

Table 44 - Selecting Hardware: Base Unit and Communications/Display Devices

| Catalog Number Select Devices                              | Bus Current Draw Specification Calculated Current for System   | Bus Current Draw Specification Calculated Current for System   |                                                            |                                                            |                                                            |
|------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
|                                                            |                                                                | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA)          |                                                            |                                                            |                                                            |
| Choose a processor, LSP or LRP                             | Choose a processor, LSP or LRP                                 | Choose a processor, LSP or LRP                                 | Choose a processor, LSP or LRP                             | Choose a processor, LSP or LRP                             | Choose a processor, LSP or LRP                             |
| 1764-LSP 300 0                                             |                                                                |                                                                |                                                            |                                                            |                                                            |
| 1764-LRP 380 0                                             |                                                                |                                                                |                                                            |                                                            |                                                            |
| 1764-DAT(1) optional                                       | 350 0                                                          |                                                                |                                                            |                                                            |                                                            |
| Communications/Display Devices, optional, one only maximum | Communications/Display Devices, optional, one only maximum     | Communications/Display Devices, optional, one only maximum     | Communications/Display Devices, optional, one only maximum | Communications/Display Devices, optional, one only maximum | Communications/Display Devices, optional, one only maximum |
| 1761-NET-AIC(1)                                            | 0                                                              | 120(2)                                                         |                                                            |                                                            |                                                            |
| 1761-NET-ENI(1)                                            | 0                                                              | 100(2)                                                         |                                                            |                                                            |                                                            |
| 2707-MVH232 or 2707-MVP232(1)                              | 0                                                              | 80(2)                                                          |                                                            |                                                            |                                                            |
| SUBTOTAL1 (A1) (B1)                                        | SUBTOTAL1 (A1) (B1)                                            | SUBTOTAL1 (A1) (B1)                                            | SUBTOTAL1 (A1) (B1)                                        |                                                            |                                                            |

Table 45 - Selecting Hardware: Expansion I/O

| Select I/O Modules for Each Bank    | Select I/O Modules for Each Bank            | Calculate Current Draw                             | Calculate Current Draw                              | Calculate Current Draw                              | Calculate Current Draw   |
|-------------------------------------|---------------------------------------------|----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|--------------------------|
| Expansion I/O Modules               | Bus Current Draw Specification (mA)         | Calculated Current for Base Unit Expansion (mA)    | Calculated Current for Bank 1 Power Supply (mA) (3) | Calculated Current for Bank 1 Power Supply (mA) (3) |                          |
| Expansion I/O Modules               |                                             | 2250 mA max 400 mA max                             | n1 n2 X Y n1 x X n1 x Y n2 x X n2 x Y               |                                                     |                          |
| Catalog Number Number of Modules(4) |                                             | @ 5V DC @ 24V DC @ 5V DC @ 24V DC @ 5V DC @ 24V DC |                                                     |                                                     |                          |
| 1769-HSC(5)                         | 425 0                                       |                                                    |                                                     |                                                     |                          |
| 1769-IA16 115 0                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IA8I 90 0                      |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IF4 (series A) 120 150         |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IF4 (series B) 120 60          |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IF4XOF2 120 160                |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IM12 100 0                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IQ16 115 0                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IQ6XOW4 105 50                 |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IR6 100 45                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-IT6 100 40                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OA8 145 0                      |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OA16 225 0                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OB16 200 0                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OB16P 160 0                    |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OF2 (series A) 120 200         |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OF2 (series B) 120 120         |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OV16 200 0                     |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OW8 125 100                    |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OW8I 125 100                   |                                             |                                                    |                                                     |                                                     |                          |
| 1769-OW16 205 180                   |                                             |                                                    |                                                     |                                                     |                          |
| 1769-SDN 440 0                      |                                             |                                                    |                                                     |                                                     |                          |
|                                     | TOTAL MODULES: SUBTOTAL2: (A2) (B2) (C) (D) | TOTAL MODULES: SUBTOTAL2: (A2) (B2) (C) (D)        |                                                     |                                                     |                          |

## IMPORTANT

When planning the system layout, keep in mind that each module has a Power Supply Distance Rating. This is the maximum distance an I/O module may be located from the power supply. For most modules, the rating is 8. For the 1769-HSC and 1769-SDN, the rating is 4.

Depending on its configuration, the 1769-SDN may transfer large amounts of data into and out of the controller I/O image tables. Care should be taken when using more than three of these modules to verify that they are optimally configured. This helps to ensure that the maximum available 4K data table size is not exceeded. For more details, see See the Compact I/O 1769-SDN DeviceNet Scanner Module User Manual, publication 1769-UM009 for more details.

4. Enter the current draw values in the "Calculated Current" columns. Add up the current draw values to determine the "SUBTOTAL2" values.
5. Verify that the total number of modules does not exceed the system limits using the maximum values for the base unit and Table 48 for the expansion power supply, if used.

## Verify the System Loading

To have a valid system, both current and power requirements must be satisfied.

## Verify the Base Unit Loading

1. Enter the SUBTOTAL values from Table 44 and Table 45. Add the total current draw for the Base Unit. Verify the values are within the maximum limits.

Table 46 - Base Unit Power Supply Loading - Verify the Current Limits

| Current From                                                         | Calculated Current for System                   | Calculated Current for System   |
|----------------------------------------------------------------------|-------------------------------------------------|---------------------------------|
|                                                                      | @ 5V DC (mA) @ 24V DC (mA)                      |                                 |
| For 1764-24BWA only, enter the sum of any User 24V DC Sensor Current | (E)                                             | (E)                             |
|                                                                      | MAXIMUM LIMIT Not applicable 400 mA User 24V DC |                                 |
| Values from SUBTOTAL1 (Table 44)                                     | (A1) (B1)                                       |                                 |
| Values from SUBTOTAL2 (Table 45) (A2) (B2)                           |                                                 |                                 |
| TOTAL BASE UNIT CURRENT LOADING (F) (G)                              |                                                 |                                 |
|                                                                      | MAXIMUM LIMIT 2250 mA @ 5V DC 400 mA @ 24V DC   |                                 |

Table 47 - Base Unit Power Supply Loading - Verify the Required Power

| Catalog Number 1764-24AWA, 1764-28BXB Base Units 1764-24BWA Base Unit   | Catalog Number 1764-24AWA, 1764-28BXB Base Units 1764-24BWA Base Unit   | Catalog Number 1764-24AWA, 1764-28BXB Base Units 1764-24BWA Base Unit   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 5V Power Calculation (F) x 5V = W (F) x 5V = W                          |                                                                         |                                                                         |
| 24V Power Calculation (G) x 24V = W (G) x 24V = W                       |                                                                         |                                                                         |
|                                                                         | (E) x 24V = W                                                           |                                                                         |
| Add up Total Watts W W                                                  |                                                                         |                                                                         |
| MAXIMUM POWER LIMIT 16 W 22 W                                           |                                                                         |                                                                         |

## Verify the Expansion Power Supply Loading

Use the values from SUBTOTAL2 to verify that the system loading and I/O distribution are within the limits shown in Table 48. Consider future expansion when selecting a power supply.

Table 48 - Bank 1 Power Supply Loading - Verify the Current Limits

| Specification Catalog Number                                                                                                                                                 | Calculated Current for System            | 24V DC User Output Capacity   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|-------------------------------|
| Specification Catalog Number                                                                                                                                                 | @ 5V DC (mA) @ 24V DC (mA)               |                               |
| Values from SUBTOTAL2 (Table 45) (C) (D)                                                                                                                                     | Values from SUBTOTAL2 (Table 45) (C) (D) |                               |
| MAXIMUM CURRENT LIMIT                                                                                                                                                        |                                          | 1769-PA2 2000 800 250 mA      |
|                                                                                                                                                                              | 1769-PA4 4000 2000                       | Not applicable                |
|                                                                                                                                                                              | 1769-PB2 2000 800                        | Not applicable                |
|                                                                                                                                                                              | 1769-PB4 4000 2000                       | Not applicable                |
| I/O Distribution - Distribute I/O modules such that the current consumed from either the left side or the right side of the power supply never exceeds the following values: |                                          | 1769-PA2 2000 800 250 mA      |
| I/O Distribution - Distribute I/O modules such that the current consumed from either the left side or the right side of the power supply never exceeds the following values: | 1769-PA4 2000 1000                       | Not applicable                |
| I/O Distribution - Distribute I/O modules such that the current consumed from either the left side or the right side of the power supply never exceeds the following values: | 1769-PB2 2000 800                        | Not applicable                |
| I/O Distribution - Distribute I/O modules such that the current consumed from either the left side or the right side of the power supply never exceeds the following values: | 1769-PB4 2000 1000                       | Not applicable                |

## System Using a 1769-PA2

To validate your system, the total 5V DC current and 24V DC current consumed must be considered. The I/O modules must be distributed, such that the current consumed from the left or right side of the power supply never exceeds 2 A at 5V DC and 1.0 A at 24V DC. Use Figure 48 , Figure 49, and Figure 50 to determine if the power supply loading in your system is within the allowable range.

Figure 48 - 1769-PA2 Current with +24V DC User Load = 0 A

<!-- image -->

Figure 49 - 1769-PA2 Current with +24V DC User Load = 0.2 A

<!-- image -->

Figure 50 - 1769-PA2 Current with +24V DC User Load = 0.25 A

<!-- image -->

## System Using a 1769-PB2

To validate your system, the total 5V DC current and 24V DC current consumed must be considered. The I/O modules must be distributed, such that the current consumed from the left or right side of the power supply never exceeds 2 A at 5V DC and 1.0 A at 24V DC. Use Figure 51 to determine if the power supply loading in your system is within the allowable range.

Figure 51 - 1769-PB2 Current

<!-- image -->

## System Using a 1769-PA4

To validate your system, the total 5V DC current and 24V DC current consumed must be considered. The I/O modules must be distributed, such that the current consumed from the left and right side of the power supply never exceeds 2 A at 5V and 0.8 A at 24V DC with an
°° gpppy 
ambient temperature of 0…55 °C (32…131 °F). Use Figure 52 to determine if the power supply loading in your system is:

- Within the allowable range for special load conditions
- Above 55…60 °C (131…140 °F)

## Figure 52 - 1769-PA4 5V and 24V DC Current

<!-- image -->

## System Using a 1769-PB4

To validate your system, the total 5V DC current and 24V DC current consumed must be considered. The I/O modules must be distributed, such that the current consumed from the left and right side of the power supply never exceeds 2 A at 5V and 0.8 A at 24V DC with an
°° gy 
ambient temperature of 0…55 °C (32…131 °F). Use Figure 53 to determine if the power supply loading in your system is:

- Within the allowable range for special load conditions
- Above 55…60 °C (131…140 °F)

Figure 53 - 1769-PB4 5V and 24V DC Current

<!-- image -->

## Calculating Heat Dissipation Use Table 49 when you need to determine the heat dissipation for installation in an enclosure.

## Table 49 - Heat Dissipation

| Catalog Number                                                              | Equation or Constant Calculation Subtotal                         |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------|
| 1764-24AWA 18 W + (0.3 x System Loading) 18 W + (0.3 x ______ W) ______ W   |                                                                   |
| 1764-24BWA 20 W + (0.3 x System Loading) 20 W + (0.3 x ______ W) ______ W   |                                                                   |
| 1764-28BXB 20 W + (0.3 x System Loading) 20 W + (0.3 x ______ W) ______ W   |                                                                   |
| 1764-DAT 1.75 W                                                             | ______ W                                                          |
|                                                                             | 1769-HSC 6.21 W x number of modules 6.21 W x __________ ______ W  |
|                                                                             | 1769-IA16 3.30 W x number of modules 3.30 W x __________ ______ W |
|                                                                             | 1769-IA8I 1.81 W x number of modules 1.81 W x __________ ______ W |
| 1769-IF4 (series A) 3.99 W x number of modules 3.99 W x __________ ______ W |                                                                   |
| 1769-IF4 (series B) 2.63 W x number of modules 2.63 W x __________ ______ W |                                                                   |
| 1769-IF4XOF2 3.03 W x number of modules 3.03 W x __________ ______ W        |                                                                   |
| 1769-IM12 3.65 W x number of modules 3.65 W x __________ ______ W           |                                                                   |
|                                                                             | 1769-IQ16 3.55 W x number of modules 3.55 W x __________ ______ W |
| 1769-IQ6XOW4 2.75 W x number of modules 2.75 W x __________ ______ W        |                                                                   |
|                                                                             | 1769-IR6 1.50 W x number of modules 1.50 W x __________ ______ W  |
|                                                                             | 1769-IT6 1.50 W x number of modules 1.50 W x __________ ______ W  |
| 1764-LSP 1.5 W                                                              | ______ W                                                          |
| 1764-LRP 1.9 W                                                              | ______ W                                                          |
| 1764-MM1, -RTC, -MM1RTC, 1764-MM2, 1764-MM2RTC, 1764-MM3, 1764-MM3RTC 0     |                                                                   |
|                                                                             | 1769-OA8 2.12 W x number of modules 2.12 W x __________ ______ W  |
|                                                                             | 1769-OA16 4.9 W x number of modules 4.9 W x __________ ______ W   |
|                                                                             | 1769-OB16 2.11 W x number of modules 2.11 W x __________ ______ W |
| 1769-OB16P 2.69 W x number of modules 2.69 W x __________ ______ W          |                                                                   |
| 1769-OF2 (series A) 4.77 W x number of modules 4.77 W x __________ ______ W |                                                                   |
| 1769-OF2 (series B) 2.52 W x number of modules 2.52 W x __________ ______ W |                                                                   |
|                                                                             | 1769-OV16 2.06 W x number of modules 2.06 W x __________ ______ W |
|                                                                             | 1769-OW8 2.83 W x number of modules 2.83 W x __________ ______ W  |
| 1769-OW8I 2.83 W x number of modules 2.83 W x __________ ______ W           |                                                                   |
|                                                                             | 1769-OW16 4.75 W x number of modules 4.75 W x __________ ______ W |
|                                                                             | 1769-SDN 3.8 W x number of modules 3.8W x __________ ______ W     |
| Add Subtotals to determine Heat Dissipation                                 | ______ W                                                          |

## Notes:

The following terms and abbreviations are used throughout this manual.

address

A character string that uniquely identifies a memory location. For example, I:1/0 is the memory address for data located in Input file word 1, bit 0.

AIC+ Advanced Interface Converter

A device (1761-NET-AIC) that provides RS-232 isolation to an RS-485 Half-duplex communication link.

- application 1) A machine or process monitored and controlled by a controller.

2) The use of computer- or processor-based routines for specific purposes.

baud rate

The speed of communication between devices. Baud rate is typically displayed in K baud. For example, 19.2K baud = 19,200 bits per second.

bit The smallest unit of memory used in discrete or binary logic, where the value 1 represents ON and 0 represents OFF.

block diagrams A method used to illustrate logic components or a sequence of events.

Boolean operators

Logical operators such as AND, OR, NAND, NOR, NOT, and Exclusive-OR that can be used singularly or in combination to form logic statements or circuits. Can have an output response of T or F.

branch A parallel logic path within a rung of a ladder program. Its primary use is to build OR logic.

communication scan

A part of the controller’s operating cycle. Communication with devices, such as other controllers and operator interface devices, takes place during this period.

control program

User logic (the application) that defines the controller’s operation.

controller

A device, such as a programmable controller, used to control output devices.

controller overhead

A portion of the operating cycle used for housekeeping purposes, such as memory checks, tests, communications, and so on.

counter

A device that counts the occurrence of an event.

CPU (Central Processing Unit) The decision-making and data storage section of a programmable controller.

data table

The part of processor memory that contains I/O status and files where user data, such as bit, integer, timers, and counters) is monitored, manipulated, and changed for control purposes.

DIN rail Manufactured according to Deutsche Industrie Normenausshus (DIN) standards, a metal railing designed to ease installation and mounting of your devices.

download

The transfer of program or data files to a device.

DCD

Data Carrier Detect. A signal generated by a modem that represents traffic (activity) on a communications network.

DTE (Data Terminal Equipment)

Equipment that is attached to a network to send or receive data, or both.

EMI

Electromagnetic interference.

embedded I/O

Embedded I/O is the controller’s on-board I/O. For MicroLogix controllers, embedded I/O is all I/O residing at slot 0.

<!-- image -->

expansion I/O

Expansion I/O is I/O that is connected to the controller via a bus or cable. MicroLogix 1500 controllers use Bulletin 1769 expansion I/O. For MicroLogix controllers, expansion I/O is all I/O residing at slot 1 and higher.

encoder

A device that detects position, and transmits a signal representing that position.

executing mode Any run, remote run, or test mode.

false The status of an instruction that does not provide a continuous logical path on a ladder rung.

FIFO (First-In-First-Out) The order that data is stored and retrieved from a file.

file A collection of data or logic organized into groups.

full-duplex A mode of communication where data may be transmitted and received simultaneously (contrast with half-duplex).

half-duplex A mode of communication where data transmission is limited to one direction at a time.

hard disk A storage device in a personal computer.

high byte

Bits 8…15 of a word.

housekeeping

The portion of the scan when the controller performs internal checks and services communications.

input device A device, such as a push button or a switch, that supplies an electrical signal to the controller.

input scan The controller reads all input devices connected to the input terminals.

inrush current

The temporary surge of current produced when a device or circuit is initially energized.

instruction

A mnemonic defining an operation to be performed by the processor. A rung in a program consists of a set of input and output instructions. The input instructions are evaluated by the controller as being true or false. In turn, the controller sets the output instructions to true or false.

instruction set

The set of general purpose instructions available within a controller.

I/O (Inputs and Outputs)

Consists of input and output devices that provide and/or receive data from the controller.

jump

Change in normal sequence of program execution, by executing an instruction that alters the program counter (sometimes called a branch). In ladder programs a JUMP (JMP) instruction causes execution to jump to a specific rung in the user program.

ladder logic A graphical programming format resembling a ladder-like diagram. program is used by a programmable controller to control devices.

least significant bit (LSB) The element (or bit) in a binary word that carries the smallest value of weight.

LED (Light Emitting Diode)

Used as status indicator for processor functions and inputs and outputs.

LIFO (Last-In-First-Out)

The order that data is stored and retrieved from a file.

low byte

Bits 0…7 of a word.

logic A process of solving complex problems through the repeated use of simple functions that can be either true or false. General term for digital circuits and programmed instructions to perform required decision making and computational functions.

Master Control Relay (MCR) A mandatory hard-wired relay that can be de-energized by any series-connected emergency stop switch. Whenever the MCR is de-energized, its contacts open to de-energize all application I/O devices.

mnemonic

A simple and easy to remember term that is used to represent a complex or lengthy set of information.

Modbus RTU Slave

A serial communication protocol.

modem

Modulator/demodulator. Equipment that connects data terminal equipment to a communication line.

modes

Selected methods of operation. Example: run, test, or program.

negative logic The use of binary logic in such a way that “0” represents the desired voltage level.

network

A series of stations (nodes) connected by some type of communication medium. A network may be made up of a single link or multiple links.

nominal input current

The current at nominal input voltage.

normally closed

Contacts on a relay or switch that are closed when the relay is de-energized or deactivated. They are open when the relay is energized or the switch is activated.

normally open

Contacts on a relay or switch that are open when the relay is de-energized or the switch is deactivated. They are closed when the relay is energized or the switch is activated.

off-delay time

The OFF delay time is a measure of the time required for the controller logic to recognize that a signal has been removed from the input terminal of the controller. The time is determined by circuit component delays and by any applied filter.

offline

When a device is not scanning/controlling or when a programming device is not communicating with the controller.

offset

A continuous deviation of a controlled variable from a fixed point.

off-state leakage current When a mechanical switch is opened (off-state), no current flows through the switch. Semiconductor switches and transient suppression components which are sometimes used to protect switches, have a small current flow when they are in the off state. This current is referred to as the off-state leakage current. To ensure reliable operation, the off-state leakage current rating must be less than the minimum operating current rating of the device that is connected.

on-delay time

The ON delay time is a measure of the time required for the controller logic to recognize that a signal has been presented at the input terminal of the controller.

one shot

A programming technique that sets a bit for only one program scan.

online

When a device is scanning/controlling or when a programming device is communicating with the controller.

operating voltage

For inputs, the voltage range needed for the input to be in the On state. For outputs, the allowable range of user-supplied voltage.

output device A device, such as a pilot light or a motor starter coil, that is controlled by the controller.

output scan

The controller turns on, off, or modifies the devices connected to the output terminals.

PCCC

Programmable Controller Communications Commands

processor

A Central Processing Unit. See CPU (Central Processing Unit) on page 111 .

processor files

The set of program and data files resident in the controller.

program file Areas within a processor that contain the logic programs. MicroLogix controllers support multiple program files.

program mode

When the controller is not scanning the control program.

program scan

A part of the controller’s operating cycle. During the program scan, the logic program is processed and the Output Image is updated.

programming device

Executable programming package used to develop ladder diagrams.

protocol

The rules of data exchange via communications.

read To acquire data. For example, the processor reads information from other devices with a read message.

relay An electrically operated device that mechanically switches electrical circuits.

relay logic A representation of binary or discrete logic.

restore To transfer a program from a device to a controller.

reserved bit A location reserved for internal use.

retentive data Information (data) that is preserved through power cycles.

RS-232 An EIA standard that specifies electrical, mechanical, and functional characteristics for serial binary communication circuits.

run mode An executing mode during which the controller scans or executes the logic program.

rung Ladder logic is comprised of a set of rungs. A rung contains input and output instructions. During Run mode, the inputs on a rung are evaluated to be true or false. If a path of true logic exists, the outputs are made true. If all paths are false, the outputs are made false.

RTU Remote Terminal Unit

save To save a program to a computer hard disk.

scan

The scan is made up of four elements: input scan, program scan, output scan, and housekeeping.

scan time The time required for the controller to complete one scan.

sinking

A term used to describe current flow between two devices. A sinking device provides a direct path to ground.

sourcing A term used to describe current flow between two devices. A sourcing device or circuit provides a power.

status The condition of a circuit or system.

terminal A point on an I/O module that external devices, such as a push button or pilot light, are wired to.

throughput The time between when an input turns on and a corresponding output turns on or off. Throughput consists of input delays, program scan, output delays, and overhead.

true The status of an instruction that provides a continuous logical path on a ladder rung.

upload Data is transferred from the controller to a programming or storage device.

watchdog timer A timer that monitors a cyclical process and is cleared at the conclusion of each cycle. If the watchdog runs past its programmed time period, it causes a fault.

write

To send data to another device. For example, the processor writes data to another device with a message write instruction.

Cables 63

## Numerics

## 1764-24AWA

features 11

1764-24AWA wiring diagram 41

1764-24BWA

features 11

1764-24BWA sinking wiring diagram 42

1764-24BWA sourcing wiring diagram 43

1764-28BXB

features 11

1764-28BXB sinking wiring diagram 43

1764-28BXB sourcing wiring diagram 44

1764-LRP processor 12

1764-LSP processor 12

## A

address 111

AIC+

applying power to 62

attaching to the network connecting 57

isolated modem 50

installing 61

recommended user supplied components 60

selecting cable 59

AIC+ Advanced Interface Converter 111

## Allen-Bradley

contacting for assistance 92

application 111

ASCII protocol 102

attach and lock module 33

## B

base comms door 88

base terminal door 88

base unit panel mounting 29

## base units

hardware overview 12

## battery

processor battery life expectancy 85

processor replacement battery

RTC battery life expectancy 74

baud rate 111

bit 111

bit key 66

Bit Mode 68

block diagrams 111

Boolean operators 111

branch 111

## C

85

61

## cables

hardware overview 13 planning routes for DH485 connections 99 selection guide for the AIC+ 59

calling Allen-Bradley for assistance 92

## channel configuration

DF1 full-duplex 95

clearing faults 92

## communication

DeviceNet 63

## communication protocols

DF1 fullduplex 95

DF1 halfduplex 95

DH485 97

Modbus 101

communication scan 111

## compact I/O

attach and lock module 33

installing

33

## component descriptions 11

accessories cables 13

programming 14 base units 12 data access tool 13 end cap 15 expansion I/O 15 memory modules/real-time clock processor 12

## components

installing 29

## connecting the system

AIC+ 57

DeviceNet network 63

DF1 fullduplex protocol 48

DH485 network 53

## contactors (bulletin 100), surge suppressors

for 38

control program 111

## ControlFlash

missing/corrupt OS LED pattern 93

sequence of operation 93

using 93

## controller

definition 111

determining faults 89

fault messages 92

features 11

grounding 38

mounting 27

overhead 111

preventing excessive heat 23

troubleshooting 89

controller error recovery model 91

controller faults 89

controller LED status 89

controller operation normal

90

counters definition 111

CPU (central processing unit), definition 111

13

## D

```
DAT Communication Errors 71 configuration 67 Controller Faults Displayed 70 display 67 Error Conditions 70 Internal Errors 70 keypad 66 power-up operation 66 DAT Function File 67 data access tool hardware overview 13 installing 31 data table 111 DCD, definition 111 DeviceNet Communications 63 DeviceNet network connecting 63 DF1 fullduplex protocol configuration parameters 95 connecting 48 description 95 using a modem 49 , 96 DF1 halfduplex protocol description 95 DH485 communication protocol configuration parameters 55 , 98 DH485 network configuration parameters 99 connecting 53 description 97 devices that use the network 98 installation 55 planning considerations 98 protocol 97 token rotation 97 DIN rail 111 mounting 28 removing your base unit 28 disconnecting main power 22 download 111 DTE, definition 111 E Electronics Industries Association (EIA) ) 95 electrostatic discharge preventing 29 emergency-stop switches 24 EMI 111 encoder definition 112 end cap hardware overview 15 ENTER key 66 error recovery model 91 errors controller 90 hardware 90 identifying 92 ESC key 66 executing mode 112
```

## expansion I/O

hardware overview 15

```
F F1 Functions 69 F1 key 66 F2 Functions 69 F2 key 66 false 112 fault recovery procedure 92 fault routine 92 faults automatically clearing 92 identifying 92 manually clearing using the fault routine 92 FET output specifications 1764-28BXB 81 FIFO (First-In-First-Out) ) 112 file 112 full-duplex 112 G grounding the controller 38 H half-duplex 112 hard disk 112 hardware features 11 hardware overview 11 hazardous location 21 heat protection 23 high byte 112 housekeeping 112 I I/O 112 identifying controller faults 92 input device 112 input scan 112 input specifications 79 input states on power down 23 inrush current 112 installing ControlFlash software 93 installing controller components compact I/O 33 data access tool 31 memory module/real-time clock 32 processor 29 installing your base unit on DIN rail 28 using mounting screws 29 installion 29 instruction 112 instruction set definition 112
```

integer key 66 Integer Mode 68 isolated link coupler installing 56 isolation transformers power considerations 23 J jump 112 K keypad 66 L ladder logic 112 least significant bit (LSB) ) 112 LED (light emitting diode) 112 LEDs error with controller 90 normal controller operation 89 status 89 LIFO (Last-In-First-Out) 112 lithium battery (1747-BA) disposing 87 handling 86 installing 85 storing 86 transporting 86 logic 112 low byte 112 M master control relay 24 master control relay (MCR) ) 112 master control relay circuit periodic tests 22 memory module data file protection 75 program compare 74 program/data backup 74 removal/installation under power 73 , 75 Memory Module Information File 75 memory module/real-time clock installing 32 mnemonic 113 Modbus communication protocol 101 Modbus definition 113 modem 113 modem cable constructing your own 50 modems dialup phone 96 leasedline 96 line drivers 97 radio 97 using with MicroLogix controllers 96 modes 113 monitoring controller operation

fault recovery procedure 92

motor starters (bulletin 509) surge suppressors 38 motor starters (bulletin 709) surge suppressors 38 mounting dimensions 26 the controller 27 using DIN rail 28 N negative logic 113 network 113 nominal input current 113 normally closed 113 normally open 113 null modem cable 51 O offline 113 offset 113 off-state leakage current 113 one shot 113 online 113 operating voltage 113 output device 113 output scan 113 output specifications 80 1764-28BXB FET 81 P panel mounting base unit 29 PCCC 113 planning considerations for a network power considerations input states on power down 23 isolation transformers 23 loss of power source 23 other line conditions 23 overview 23 power supply inrush 23 power distribution 22 Power Save Timeout 67 power source loss of 23 power supply inrush power considerations 23 preparing for upgrade 93 preventing excessive heat 23 proceessor hardware overview 12 processor 113 installing 29 processor access door 88 processor files 113 program faults determining 89

98

```
program file definition 113 program mode 114 program scan definition 114 programming device 114 programming the controller required software 14 PROTECTED indicator light 66 , 68 protocol 114 R read 114 real time clock battery low indicator bit 74 disabling 74 Real Time Clock Function File 73 relay 114 relay contact rating table 80 relay logic 114 relays surge suppressors for 38 remote packet support 100 replacement battery 85 disposing 87 handling 86 installing 85 storing 86 transporting 86 replacement doors 88 base comms door 88 base terminal door 88 processor access door 88 trimpots/mode switch cover door 88 replacement kits 85 replacement parts 85 base comms door 88 base terminal door 88 processor access door 88 terminal blocks 87 trimpots/mode switch cover door 88 replacement terminal blocks 87 reserved bit 114 response times for high-speed dc inputs 79 response times for normal dc inputs 80 restore 114 retentive data 114 RS-232 communication interface 95 RS-232, definition 114 RTU, definition 114 run mode 114 rung 114 S safety circuits 22 safety considerations disconnecting main power 22 periodic tests of master control relay circuit 22 power distribution 22 safety circuits 22
```

```
save 114 scan 114 scan time 114 sinking 114 sinking and sourcing circuits 41 sinking wiring diagram 1764-28BXB 43 sourcing 114 sourcing wiring diagram 1764-28BXB 44 spade lug wiring 36 specifications input 79 output 80 relay contact rating table 80 response times for high-speed dc inputs 79 response times for normal dc inputs 80 working voltage (1764-24AWA) ) 82 working voltage (1764-24BWA) ) 82 working voltage (1764-28BXB) ) 82 status 114 surge suppressors for contactor 38 for motor starters 38 for relays 38 recommended 38 using 36 T terminal 114 throughput 114 Trimpot Information Function File 65 trimpots adjustment 65 error conditions 66 location 65 trimpots/mode switch cover door 88 troubleshooting automatically clearing faults 92 contacting Allen-Bradley for assistance 92 controller error recovery model 91 determining controller faults 89 identifying controller faults 92 manually clearing faults 92 understanding the controller LED status 89 using the fault routine 92 true 114 U upload 114 W wire requirements 35 wiring spade lug 36 wiring diagrams 39 wiring recommendation 35 wiring your controller 35 Working Screen Operation 69
```

## working voltage (1764-24AWA)

specifications 82

working voltage (1764-24BWA)

specifications 82

## working voltage (1764-28BXB)

specifications 82

write

114

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

Allen-Bradley, Compact I/O, CompactLogix, ControlFLASH, DH+, DTAM Micro, DTAM Plus, expanding human possibility, FactoryTalk, MicroLogix, PanelView, PLC-5, Rockwell Automation, RSLinx, RSLogix 500, SLC, SLC 5/03, SLC 500, and TechConnect are trademarks of Rockwell Automation, Inc.

DeviceNet and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility?

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIA PACIFIC:Rockwell Automation SEA Pte Ltd, 2 Corporation Road, #04-05, Main Lobby,Corporation Place,Singapore 618494,Tel:(65)6510 6608