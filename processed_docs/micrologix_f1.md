<!-- image -->

## MicroLogix 1100 Programmable Controllers

Bulletin 1763 Controllers and 1762 Expansion I/O

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

|                         | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9    |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                         | Purpose of this Manual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9     |
|                         | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                        |
|                         | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9      |
|                         | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9    |
|                         | Chapter 1                                                                                                                               |
| Hardware Overview       | Hardware Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11    |
|                         | Component Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12         |
|                         | MicroLogix 1100 Memory Module and Built-in Real-time Clock . . . . . . . . . . . . . . . . 12                                           |
|                         | 1762 Expansion I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12                  |
|                         | Communication Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13         |
|                         | Programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13 |
|                         | Communication Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14         |
|                         | Chapter 2                                                                                                                               |
| Install Your Controller | Installation Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15        |
|                         | Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15      |
|                         | Hazardous Location Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                         |
|                         | Disconnecting Main Power. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16                  |
|                         | Safety Circuits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16       |
|                         | Power Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17           |
|                         | Periodic Tests of Master Control Relay Circuit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17                             |
|                         | Power Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17       |
|                         | Isolation Transformers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17              |
|                         | Power Supply Inrush . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17            |
|                         | Loss of Power Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17              |
|                         | Input States on Power Down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                   |
|                         | Other Types of Line Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                   |
|                         | Help Prevent Excessive Heat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18           |
|                         | Master Control Relay. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18    |
|                         | Emergency Stop Switches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                  |
|                         | Install a Memory Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22       |
|                         | Using the Battery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22  |
|                         | Connecting the Battery Wire Connector. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                           |
|                         | Controller Mounting Dimensions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23              |
|                         | Controller and                                                                                                                          |
|                         | Expansion I/O Spacing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24      |
|                         | Mount the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24    |
|                         | DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25          |
|                         | Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26         |
|                         | 1762 Expansion I/O Module Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26                   |
|                         | Mount 1762 Expansion I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27         |
|                         | DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27          |
|                         | Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27         |

## Table of Contents

|                           | Connect Expansion I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28             |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|                           | Chapter 3                                                                                                                              |
| Wire Your Controller      | Wiring Requirements . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   29  |
|                           | Wiring Recommendation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                 |
|                           | Wiring the Terminal Block . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29               |
|                           | Use Surge Suppressors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30       |
|                           | Recommended Surge Suppressors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32                          |
|                           | Ground the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32    |
|                           | Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 |
|                           | Terminal Block Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33              |
|                           | Terminal Groupings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34            |
|                           | Sinking and Sourcing Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                  |
|                           | 1763-L16AWA, 1763-L16BWA, 1763-L16BBB, and 1763-L16DWD Wiring Diagrams . . . 35                                                        |
|                           | Controller I/O Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37  |
|                           | Minimizing Electrical Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37               |
|                           | Wire Your Analog Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37         |
|                           | Analog Channel Wiring Guidelines. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37                     |
|                           | Minimize Electrical Noise on Analog Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38                              |
|                           | Ground Your Analog Cable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38                |
|                           | Expansion I/O Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39    |
|                           | Digital Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39             |
|                           | Analog Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45      |
|                           | Chapter 4                                                                                                                              |
| Communication Connections | Supported Communication Protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                   |
|                           | Default Communication Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51                   |
|                           | Use the Communications Toggle Functionality. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52                        |
|                           | Change Communication Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52                            |
|                           | Connect to the RS-232 Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55        |
|                           | Make a DF1 Point-to-point Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                        |
|                           | Use a Modem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56       |
|                           | Connect to a DF1 Half-duplex Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                        |
|                           | Connecting to a DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59              |
|                           | DH-485 Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                       |
|                           | Recommended Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61               |
|                           | DH-485 Communication Cable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                     |
|                           | Connecting the Communication Cable to the DH-485 Connector . . . . . . . . . . . . . . 61                                              |
|                           | Ground and Terminate the DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                               |
|                           | Connect the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63  |
|                           | Cable Selection Guide. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64            |
|                           | Recommended User-supplied Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                                  |
|                           | Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67             |
|                           | Install and Attach the AIC+. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67              |
|                           | Power the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67        |
|                           | Connecting to Ethernet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68      |
|                           | Ethernet Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68             |

## Chapter 5

| Use the LCD and Keypad   | Operating Principles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72                                                                                                           |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          | Startup Screen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72                                                                                                               |
|                          | Main Menu and Default Screen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73                                                                                                                            |
|                          | Operating Buttons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                                                                                                                 |
|                          | Select Between Menu Items. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                                                                                                                          |
|                          | Cursor Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                                                                                                              |
|                          | Setting Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                                                                                                              |
|                          | I/O Status. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76                                                                                                   |
|                          | View I/O Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77                                                                                                               |
|                          | Monitor Bit File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77                                                                                                      |
|                          | Target Bit File Number (TBF) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77                                                                                                                        |
|                          | Monitor a Bit File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                                                                                                              |
|                          | Monitor Integer File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                                                                                                          |
|                          | Target Integer File Number (TIF). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                                                                                                                           |
|                          | Monitor an Integer File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83                                                                                                                   |
|                          | Use the Mode Switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88                                                                                                             |
|                          | Controller Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88                                                                                                                |
|                          | Change Mode Switch Position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                                                                                                                           |
|                          | Use a User-defined LCD Screen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90                                                                                                                     |
|                          | User-defined LCD Screen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91                                                                                                                        |
|                          | Configure Advanced Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                                   |
|                          | Change Key In Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                            |
|                          | Key In Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                                                                                                              |
|                          | Change Key In Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                                                                                    |
|                          | Communications Toggle Functionality. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                                                                                                                          |
|                          | Ethernet Port Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                                                                                                                 |
|                          | Trimpots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                                                                                    |
|                          | Trimpot Operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                                                                                                  |
|                          | Changing Data Value of a Trimpot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                                                                                                                              |
|                          | Trimpot Configuration in LCD Function File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                                                                   |
|                          | Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                                                |
|                          | View System Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                                                                                                                |
|                          | View Fault Code. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                                                                                                        |
|                          | Chapter 6                                                                                                                                                                                                                                      |
| Memory Modules           | Write Data to the Real-time Clock. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101                                                                                                                             |
|                          | RTC Battery Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101                                                                                                                      |
|                          | Memory Module Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                                                                                                                  |
|                          | User Program, User Data, and Recipe Back-up. . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                                                                                                                                         |
|                          | Program Compare. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                                                                                                                     |
|                          | Data File Download Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                                                                                                                            |
|                          | Memory Module Write Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                                                                                                                               |
|                          | Removal/Insertion Under Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                                                                                                                              |
|                          | Memory Module Information File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                                                                                                                              |
|                          | Program/Data Download . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 Program/Data Upload. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103 |

|                          | Chapter 7                                                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Online Editing           | Overview of Online Editing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                                |
|                          | Online Editing Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                                     |
|                          | Effects of Online Editing On Your System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                           |
|                          | System Impacts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                  |
|                          | Data Table File Size. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                  |
|                          | Online Edit Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                |
|                          | Directions and Cautions for MicroLogix 1100 Online Edit User . . . . . . . . . . . . . . . . . . . 107                                                         |
|                          | Change the RSLinx “Configure CIP Option” (OS Series A FRN 1, 2, and 3 only). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107 |
|                          | A Download is Required Before Starting Online Editing . . . . . . . . . . . . . . . . . . . . . 107                                                            |
|                          | Types of Online Editing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                              |
|                          | Edit Functions in Runtime Online Editing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                                                  |
|                          | Edit Functions in Program Online Editing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                                                   |
|                          | Appendix A                                                                                                                                                     |
| Specifications           | MicroLogix 1100 Controller Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                                        |
|                          | 1762 Expansion I/O Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118                                      |
|                          | Digital I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118                                  |
|                          | Analog I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122                                   |
|                          | Appendix B                                                                                                                                                     |
| Replacement Parts        | MicroLogix 1100 Replacement Kits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129                                       |
|                          | Lithium Battery (1763-BA) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129                                |
|                          | Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129                             |
|                          | Battery Handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130                                 |
|                          | Storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130                            |
|                          | Transportation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130                                 |
|                          | Disposal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                           |
|                          | Appendix C                                                                                                                                                     |
| Troubleshoot Your System | Understand the Controller Status Indicators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133                                             |
|                          | Controller Status Indicators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133                                        |
|                          | Status Indicators on the LCD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134                                         |
|                          | I/O Status Indicators on the LCD. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134                                            |
|                          | Normal Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135                                   |
|                          | Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135                                 |
|                          | Controller Error Recovery Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136                                    |
|                          | Analog Expansion I/O Diagnostics and Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . 137                                                       |
|                          | Module Operation and Channel Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137                                                     |
|                          | Power-up Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137                                       |
|                          | Critical and Non-critical Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137                                         |
|                          | Module Error Definition Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137                                          |
|                          | Error Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138                              |
|                          | Calling Rockwell Automation for Assistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139                                             |

Appendix D

| Use ControlFLASH to Upgrade   | Prepare for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Your Operating System         | Install ControlFLASH Software. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141                            |
|                               | Use DMK Extraction Tool for Firmware Upgrade . . . . . . . . . . . . . . . . . . . . . . . . . . . 141                                          |
|                               | Prepare the Controller for Firmware Update. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143                                       |
|                               | Sequence of Operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143                |
|                               | Missing or Corrupt OS LED Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144                       |
|                               | Appendix E                                                                                                                                      |
| Connect to Networks via RS                               | RS-232 Communication Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145                         |
| 232/RS-485 Interface          | RS-485 Communication Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145                          |
|                               | DF1 Full-duplex Protocol. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145               |
|                               | DF1 Half-duplex Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146                |
|                               | DF1 Half-duplex Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146                         |
|                               | Considerations When Communicating as a DF1 Slave on a Multi-drop Link . . . . 147                                                               |
|                               | Use Modems with MicroLogix Programmable Controllers . . . . . . . . . . . . . . . . . . . 147                                                   |
|                               | DH-485 Communication Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148                         |
|                               | DH-485 Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149                                 |
|                               | Devices that use the DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149                                   |
|                               | Important DH-485 Network Planning Considerations. . . . . . . . . . . . . . . . . . . . . . . 149                                               |
|                               | Example DH-485 Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152                              |
|                               | Modbus Communication Protocol. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154                          |
|                               | ASCII . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154 |
|                               | Appendix F                                                                                                                                      |
| Connect to Networks via       | MicroLogix 1100 Controllers and Ethernet Communication . . . . . . . . . . . . . . . . . . . . . . 155                                          |
| Ethernet Interface            | MicroLogix 1100 Performance Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155                                  |
|                               | MicroLogix 1100 and Computer Connections to the Ethernet Network . . . . . . . . . . . . 156                                                    |
|                               | Connect an Ethernet switch on the Ethernet Network. . . . . . . . . . . . . . . . . . . . . . 156                                               |
|                               | Cables. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157           |
|                               | Ethernet Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158               |
|                               | Duplicate IP address Detection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159                     |
|                               | Configure the Ethernet Channel on the MicroLogix 1100 Controller . . . . . . . . . . . . . . . 159                                              |
|                               | Configure Using RSLogix 500 Programming Software. . . . . . . . . . . . . . . . . . . . . . . . . . 160                                         |
|                               | Configure Using BOOTP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160                 |
|                               | Using the Rockwell Automation BOOTP/DHCP Utility . . . . . . . . . . . . . . . . . . . . . . . 161                                              |
|                               | Use a DHCP Server To Configure Your Processor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162                                   |
|                               | Subnet Masks and Gateways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162                     |
|                               | Manually Configuring Channel 1 for Controllers on Subnets . . . . . . . . . . . . . . . . . 163                                                 |
|                               | MicroLogix 1100 Embedded Web Server Capability. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163                                     |
|                               | Appendix G                                                                                                                                      |
| System Loading and Heat       | System Loading Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165                     |
| Dissipation                   | System Loading Example Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165                                     |
|                               | System Loading Worksheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166                    |
|                               | Current Loading. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166                  |
|                               | Calculating Heat Dissipation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167                  |

| Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169   |        |
|------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . .173 |

## About This Publication

## Purpose of this Manual

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

## Additional Resources

## Additional Resources

|                                                                                                                    | Resource Description                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001                  | Information on the MicroLogix 1100 controllers instruction set.                                                                                                                               |
| AIC+ Advanced Interface Converter User Manual, publication 1761-UM004                                              | A description on how to install and connect an AIC+. This manual also contains information on network wiring.                                                                                 |
| DeviceNet Interface User Manual, publication 1761-UM005                                                            | Information on how to install, configure, and commission a DeviceNet® Interface (DNI).                                                                                                        |
| DF1 Protocol and Command Set Reference Manual, publication 1770-RM516                                              | Information on DF1 open protocol.                                                                                                                                                             |
| Modbus Protocol Specifications, available from www.modbus.org                                                      | Information about the Modbus protocol.                                                                                                                                                        |
| System Security Design Guidelines Reference Manual, publication SECURE-RM001                                       | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment. |
| UL Standards Listing for Industrial Control Products, publication CMPNTS-SR002                                     | Assists original equipment manufacturers (OEMs) with construction of panels, to help ensure that they conform to the requirements of Underwriters Laboratories.                               |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                              |

Use this manual if you are responsible for designing, installing, programming, or troubleshooting control systems that use MicroLogix™ 1100 controllers.

You should have a basic understanding of electrical circuitry and familiarity with relay logic. If you do not, obtain the proper training before using this product.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This manual is a reference guide for MicroLogix 1100 controllers and 1762 expansion I/O. It describes the procedures that you use to install, wire, and troubleshoot your controller. This manual:

- Explains how to install and wire your controllers
- Gives you an overview of the MicroLogix 1100 controller system

See the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001, for the MicroLogix 1100 instruction set and for application examples to show the instruction set in use. See your RSLogix 500® programming software user documentation for more information on programming your MicroLogix 1100 controller.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic  Page                                   |
|-----------------------------------------------|
| Updated template throughout                   |
| Added inclusive language acknowledgment 9     |
| Updated General Specifications 111            |
| Updated Environmental Specifications 121, 126 |
| Updated Certifications 122, 127               |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

## Additional Resources (Continued)

|                                                                                                                  | Resource Description                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1 | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                      | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications                                                          | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

## Hardware Features

## Hardware Overview

The MicroLogix 1100 programmable controller contains a power supply, input and output circuits, a processor, an isolated combination RS-232/RS-485 communication port, and an Ethernet port. Each controller supports 18 I/O points (10 digital inputs, 2 analog inputs, and 6 discrete outputs).

The hardware features of the controller are shown in Figure 1 .

Figure 1 - Controller Hardware Features

<!-- image -->

## Controller Description

|                                              | Description Description                                                          |
|----------------------------------------------|----------------------------------------------------------------------------------|
|                                              | 1 Output terminal block 7 LCD keypad (ESC, OK, Up, Down, Left, Right)            |
| 2 Battery connector 8 Status indicators      |                                                                                  |
| 3 Bus connector interface to expansion I/O 9 | Memory module port cover(1) or memory module(2)                                  |
|                                              | 4 Battery 10 DIN rail latches                                                    |
|                                              | 5 Input terminal block 11 RS-232/RS-485 communication port (Channel 0, isolated) |
|                                              | 6 LCD display 12 Ethernet port (Channel 1)                                       |

Table 1 - Controller Input Power and Embedded I/O

| Catalog Number  Description        |                                      |                            | Input Power Digital Inputs Analog Inputs Digital Outputs   |
|------------------------------------|--------------------------------------|----------------------------|------------------------------------------------------------|
| 1763-L16AWA 120/240V AC 10 120V AC |                                      | 2 voltage input 0...10V DC | 6 relays All individually isolated                         |
| 1763-L16BWA 120/240V AC            | 6 24V DC 4 high-speed 24V DC (1)     | 2 voltage input 0...10V DC | 6 relays All individually isolated                         |
| 1763-L16BBB 24V DC                 | 6 24V DC 4 high-speed 24V DC (1)     | 2 voltage input 0...10V DC | 2 relays (isolated) 2 24V DC FET 2 high-speed 24V DC FET   |
| 1763-L16DWD 12...24V DC            | 6 12...24V DC 4 high-speed 12/24V DC | 2 voltage input 0...10V DC | 6 relays All individually isolated                         |

<!-- image -->

<!-- image -->

## Component Descriptions

## MicroLogix 1100 Memory Module and Built-in Real-time Clock

The controller has a built-in real-time clock to provide a reference for applications that need time-based control.

The controller is shipped with a memory module port cover in place. You can order a memory module, 1763-MM1, as an accessory. The memory module provides an optional backup of your user program and data, and is a means to transport your programs between controllers.

The program and data in your MicroLogix 1100 controller is nonvolatile and is stored when the power is lost to the controller. The memory module provides additional backup that can be stored separately. The memory module does not increase the available memory of the controller.

Figure 2 - 1763-MM1 Memory Module

<!-- image -->

## 1762 Expansion I/O Modules

1762 expansion I/O modules can be connected to the MicroLogix 1100 controller, as shown in Figure 3 .

<!-- image -->

A maximum of four I/O modules, in any combination, can be connected to a controller. See System Loading and Heat Dissipation on page 165 to determine how much heat a certain combination generates.

Figure 3 - 1762 Expansion I/O Modules

1762 expansion I/O module 1762 expansion I/O modules connected to a MicroLogix 1100 controller

<!-- image -->

<!-- image -->

## Communication Cables

## Programming

## Expansion I/O Modules

| Catalog Number Description                                                              |
|-----------------------------------------------------------------------------------------|
| 1762-IA8 8-point 120V AC input module                                                   |
| 1762-IQ8 8-point sinking/sourcing 24V DC input module                                   |
| 1762-IQ16 16-point sinking/sourcing 24V DC input module                                 |
| 1762-IQ32T 32-point sinking/sourcing 24V DC input module                                |
| 1762-OA8 8-point 120/240V AC Triac output module                                        |
| 1762-OB8 8-point sourcing 24V DC output module                                          |
| 1762-OB16 16-point sourcing 24V DC output module                                        |
| 1762-OB32T 32-point sourcing 24V DC output module                                       |
| 1762-OV32T 32-point sinking 24V DC output module                                        |
| 1762-OW8 8-point AC/DC relay output module                                              |
| 1762-OW16 16-point AC/DC relay output module                                            |
| 1762-OX6I 6-point isolated AC/DC relay output module                                    |
| 1762-IQ8OW6 8-point sinking/sourcing 24V DC input and 6-point AC/DC relay output module |
| 1762-IF4 4-channel voltage/current analog input module                                  |
| 1762-OF4 4-channel voltage/current analog output module                                 |
| 1762-IF2OF2 Combination 2-channel input 2-channel output voltage/current analog module  |
| 1762-IR4 4-channel RTD/resistance input module                                          |
| 1762-IT4 4-channel thermocouple/mV input module                                         |

Use only the following communication cables with the MicroLogix 1100 controllers. These cables are required for Class I Division 2 applications.

- 1761-CBL-AM00, series C or later
- 1761-CBL-AP00, series C or later
- 1761-CBL-PM02, series C or later
- 1761-CBL-HM02, series C or later
- 1761-CBL-PH02, series A or later
- 1761-CBL-AH02, series A or later
- 2707-NC9, series C or later
- 1763-NC01, series A or later

<!-- image -->

## ATTENTION: UNSUPPORTED CONNECTION

Do not connect a MicroLogix 1100 controller to another MicroLogix family controller such as MicroLogix 1000, MicroLogix 1200, MicroLogix 1500, or the network port of a 1747-DPS1 port splitter with a 1761- CBL-AM00 (8-pin mini-DIN to 8-pin mini-DIN) cable or equivalent.

This type of connection damages the RS-232/RS-485 communication port (Channel 0) of the MicroLogix 1100 and/or the controller itself. The communication pins that are used for RS-485 communications on the MicroLogix 1100 controller are alternately used for 24V power on the other MicroLogix controllers and the network port of the 1747-DPS1 port splitter.

Program the MicroLogix 1100 controller using RSLogix 500 software, version 7.00.00 or later. To use the latest features, you must use RSLogix 500 software, version 7.20.00 or later. Communication cables for programming are available separately from the controller and software.

## Communication Options

MicroLogix 1100 controllers provide two communications ports: an isolated combination RS-232/RS-485 communication port (Channel 0) and an Ethernet port (Channel 1).

You can connect the isolated Channel 0 port on the MicroLogix 1100 controller to the following:

- Operator interfaces, personal computers, and so on, using DF1 Full-duplex point-to-point
- A DH-485 network
- A DF1 Radio Modem network
- A DF1 Half-duplex network as an RTU master or RTU slave
- A Modbus network as an RTU master or RTU slave
- An ASCII network
- An Ethernet network using the Ethernet Interface module (1761-NET-ENI or 1761-NET-ENIW)

When connecting to a DH-485 network, DF1 Half-duplex network (a) ) or a Modbus network, the MicroLogix 1100 controller can be connected directly to Channel 0 (without an Advanced Interface Converter, 1761-NET-AIC). The Channel 0 combo port provides both RS-232 and RS-485 isolated connections. The appropriate electrical interface is selected through your choice of communication cable. The existing MicroLogix 1761 communication cables provide an interface to the RS-232 drivers. The 1763-NC01 cable provides an interface to the RS-485 drivers (for DH-485, Modbus RTU Master, RTU slave networks, DF1 Half-duplex master (a) , and DF1 Half-duplex slave (a) ).

The controller may also be connected to serial devices, such as barcode readers, weigh scales, serial printers, and other intelligent devices, using ASCII. See Default Communication Configuration on page 51 for the configuration settings for Channel 0. MicroLogix 1100 controllers can be connected directly to the RS-485 network via channel 0, using ASCII (a) .

The MicroLogix 1100 controller supports EtherNet/IP™ communication via the Ethernet communication Channel 1. You can connect your controller to a local area network that provides communication between various devices at 10 Mbps or 100 Mbps. This port supports CIP™ explicit messaging (message exchange) only. The controller cannot be used for CIP implicit messaging (real-time I/O messaging). The controller also includes an embedded web server, which allows viewing of not only module information, TCP/IP configuration, and diagnostic information, but also includes the data table memory map and data table monitor screen using a standard web browser.

See Communication Connections on page 51 for more information on connecting to the available communication options.

## Installation Considerations

## Safety Considerations

## Install Your Controller

Most applications require installation in an industrial enclosure (Pollution Degree 2(a)) to reduce the effects of electrical interference (Over Voltage Category II (b) ) and environmental exposure. Locate your controller as far as possible from power lines, load lines, and other sources of electrical noise such as hard-contact switches, relays, and AC motor drives. For more information on proper grounding guidelines, see the Industrial Automation Wiring and Grounding Guidelines publication 1770-4.1 .

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Vertical mounting of the controller is not supported due to heat build-up considerations.

ATTENTION: Be careful of metal chips when drilling mounting holes for your controller or other equipment within the enclosure or panel. Drilled fragments that fall into the controller or I/O modules could cause damage. Do not drill holes above a mounted controller if the protective debris shields are removed or the processor is installed.

ATTENTION: Do not place the MicroLogix 1100 programmable controller in direct sunlight. Prolonged exposure to direct sunlight could degrade the LCD display and have adverse effects on the controller. The controller is not designed for outdoor use.

Safety considerations are an important element of proper system installation. Actively considering the safety of yourself and others, and the condition of your equipment, is of primary importance. We recommend reviewing the following safety considerations.

## Hazardous Location Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D, or non-hazardous locations only. The following WARNING statement applies to use in hazardous locations.

(a) Pollution Degree 2 is an environment where normally only non-conductive pollution occurs except that occasionally temporary conductivity that is caused by condensation shall be expected.

(b) Overvoltage Category II is the load-level section of the electrical distribution system. At this level, transient voltages are controlled and do not exceed the impulse voltage capability of the product's insulation.

<!-- image -->

<!-- image -->

## WARNING: EXPLOSION HAZARD

- Substitution of components may impair suitability for Class I Division 2.
- Do not replace components or disconnect equipment unless power has been switched off.
- Do not connect or disconnect components unless power has been switched off.
- This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.
- All wiring must comply with N.E.C. article 501-10(b).
- The interior of the enclosure must be accessible only by the use of a tool.
- For applicable equipment (for example, relay modules), exposure to some chemicals may degrade the sealing properties of the materials that are used in these devices:
- Relays, epoxy

It is recommended that you periodically inspect these devices for any degradation of properties and replace the module if degradation is found.

Use only the communication cables that are listed in Table 2 in Class I Division 2 hazardous locations.

Table 2 - Communication Cables for Class I Division 2 Hazardous Locations

| Catalog Number Catalog Number                                 |
|---------------------------------------------------------------|
| 1761-CBL-PM02, series C or later 2707-NC9, series C or later  |
| 1761-CBL-HM02, series C or later 1763-NC01, series A or later |
| 1761-CBL-AM00, series C or later —                            |
| 1761-CBL-AP00, series C or later —                            |
| 1761-CBL-PH02, series A or later —                            |
| 1761-CBL-AH02, series A or later —                            |

## Disconnecting Main Power

<!-- image -->

## WARNING: EXPLOSION HAZARD

Do not replace components, connect equipment, or disconnect equipment unless power has been switched off.

The main power disconnect switch should be located where operators and maintenance personnel have quick and easy access to it. In addition to disconnecting electrical power, all other sources of power (pneumatic and hydraulic) should be de-energized before working on a machine or process that is controlled by a controller.

## Safety Circuits

<!-- image -->

## WARNING: EXPLOSION HAZARD

Do not connect or disconnect connectors while the circuit is live.

Circuits installed on the machine for safety reasons, like overtravel limit switches, stop push buttons, and interlocks, should always be hard-wired directly to the master control relay. These devices must be wired in series so that when any one device opens, the master control relay is de-energized, which removes power to the machine. Never alter these circuits to defeat their function. Serious injury or machine damage could result.

## Power Considerations

## Power Distribution

There are some points about power distribution that you should know:

- The master control relay must be able to inhibit all machine motion by removing power to the machine I/O devices when the relay is de-energized. It is recommended that the controller remains powered even when the master control relay is de-energized.
- If you are using a DC power supply, interrupt the load side rather than the AC line power. This avoids the additional delay of power supply turn-off. The DC power supply should be powered directly from the fused secondary of the transformer. Power to the DC input and output circuits should be connected through a set of master control relay contacts.

## Periodic Tests of Master Control Relay Circuit

Any part can fail, including the switches in a master control relay circuit. The failure of one of these switches would most likely cause an open circuit, which is a safe power-off failure. However, if one of these switches shorts out, it no longer provides any safety protection. These switches should be tested periodically to help verify that they stop machine motion when needed.

The following explains the power considerations for the micro controllers.

## Isolation Transformers

Consider using an isolation transformer in the AC line to the controller. This type of transformer provides isolation from your power distribution system to reduce the electrical noise that enters the controller and is often used as a step-down transformer to reduce line voltage. Any transformer that is used with the controller must have a sufficient power rating for its load. The power rating is expressed in voltamperes (VA).

## Power Supply Inrush

During power-up, the MicroLogix 1100 power supply allows a brief inrush current to charge internal capacitors. Many power lines and control transformers can supply inrush current for a brief time. If the power source cannot supply this inrush current, the source voltage could sag momentarily.

The only effect of limited inrush current and voltage sag on the MicroLogix 1100 controller is that the power supply capacitors charge more slowly. However, consider the effect of a voltage sag on other equipment. For example, a deep voltage sag could reset a computer that is connected to the same power source. The following considerations determine whether the power source is required to supply high inrush current:

- The power-up sequence of devices in a system
- The amount of the power source voltage sag if the inrush current cannot be supplied
- The effect of voltage sag on other equipment in the system

If the entire system is powered-up simultaneously, a brief sag in the power source voltage typically does not affect any equipment.

## Loss of Power Source

The power supply is designed to withstand brief power losses without affecting the operation of the system. The time that the system is operational during power loss is called program scan hold-up time after loss of power. The duration of the power supply hold-up time depends on the type and state of the I/O, but is typically between 10 milliseconds and 3 seconds. When the duration of power loss reaches this limit, the power supply signals the processor that it can no longer provide adequate DC power to the system. This is referred to as a power supply shutdown. The processor then performs an orderly shutdown of the controller.

## Help Prevent Excessive Heat

## Master Control Relay

## Input States on Power Down

The power supply hold-up time that is described previously is longer than the turn-on and turn-off times of the inputs. Because of this, the input state change from On to Off that occurs when power is removed could be recorded by the processor before the power supply shuts down the system. Understanding this concept is important. The user program should be written to take this effect into account.

## Other Types of Line Conditions

Occasionally the power source to the system can be temporarily interrupted. It is also possible that the voltage level drops substantially below the normal line voltage range for a period of time. Both of these conditions are considered to be a loss of power for the system.

For most applications, normal convective cooling keeps the controller within the specified operating range. Confirm that the specified temperature range is maintained. Proper spacing of components within an enclosure is sufficient for heat dissipation.

In some applications, a substantial amount of heat is produced by other equipment inside or outside the enclosure. In this case, place blower fans inside the enclosure to help with air circulation and to reduce hot spots near the controller.

Additional cooling provisions might be necessary when high ambient temperatures are encountered.

<!-- image -->

Do not bring in unfiltered outside air. Place the controller in an enclosure to protect it from a corrosive atmosphere. Harmful contaminants or dirt could cause improper operation or damage to components. In extreme cases, you can use air conditioning to protect against heat build-up within the enclosure.

A hard-wired master control relay (MCR) provides a reliable means for emergency machine shutdown. Since the master control relay allows the placement of several emergency stop switches in different locations, its installation is important from a safety standpoint. Overtravel limit switches or mushroom-head push buttons are wired in series so that when any of them opens, the master control relay is de-energized. This removes power to input and output device circuits. See Figure 4 and Figure 5 .

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

Figure 4 and Figure 5, show the master control relay that is wired in a grounded system.

<!-- image -->

In most applications, input circuits do not require MCR protection; however, if you must remove power from all field devices, you must include MCR contacts in series with input power wiring.

Figure 4 - Schematic (Using IEC Symbols)

<!-- image -->

Figure 5 - Schematic (Using ANSI/CSA Symbols)

<!-- image -->

## Install a Memory Module

## Using the Battery

To install a memory module, do as follows:

1. Remove the memory module port cover.
2. Align the connector on the memory module with the connector pins on the controller.
3. Firmly seat the memory module into the controller.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

The MicroLogix 1100 controller is equipped with a replaceable battery (1747-BA). The Battery Low indicator on the LCD display of the controller shows the status of the replaceable battery. When the battery is low, the indicator is set (displayed as a solid rectangle). This means that either the battery wire connector is disconnected, or the battery fails within 2 weeks if it is connected. When the battery level is acceptable, the indicator is clear (displayed as an empty rectangle).

## IMPORTANT

The MicroLogix 1100 controller ships with the battery wire connector connected. Ensure that the battery wire connector is inserted into the connector port if your application needs battery power. For example, when using a real-time clock (RTC), or to store the program in the controller's memory for an extended time while the power is removed.

See Guidelines for Handling Lithium Batteries Installation Instructions, publication 1747-IN515, for more information on installation, handling, usage, storage, and disposal of the battery.

See RTC Battery Operation on page 101, for more information on the use of the battery in relation with RTC.

## Controller Mounting Dimensions

## IMPORTANT

When the controller's Battery Low indicator is set (displayed as a solid rectangle) with the battery wire connector connected, we recommend strongly to install a new battery immediately.

## Connecting the Battery Wire Connector

To connect the battery wire connector to the battery connector, do as follows:

1. Insert the replaceable battery wire connector into the controller's battery connector.
2. Secure the battery connector wires along the wire guide.

<!-- image -->

Figure 6 - Controller Dimensions

<!-- image -->

1763-L16AWA, 1763-L16BWA, 1763-L16BBB, 1763-L16DWD

|    |                   | Dimension 1763-L16AWA 1763-L16BWA 1763-L16BBB 1763-L16DWD   |                   |                   |
|----|-------------------|-------------------------------------------------------------|-------------------|-------------------|
| A  | 90 mm (3.5 in.)   | 90 mm (3.5 in.)                                             | 90 mm (3.5 in.)   | 90 mm (3.5 in.)   |
| B  | 110 mm (4.33 in.) | 110 mm (4.33 in.)                                           | 110 mm (4.33 in.) | 110 mm (4.33 in.) |
| C  | 87 mm (3.43 in.)  | 87 mm (3.43 in.)                                            | 87 mm (3.43 in.)  | 87 mm (3.43 in.)  |

## Controller and Expansion I/O Spacing

## Mount the Controller

The controller mounts horizontally, with the expansion I/O extending to the right of the controller. Allow 50 mm (2 in.) of space on all sides of the controller system for adequate ventilation. Maintain spacing from enclosure walls, wireways, adjacent equipment, and so on, as shown in Figure 7 .

Figure 7 - Controller and Expansion I/O Spacing

<!-- image -->

MicroLogix 1100 controllers are suitable for use in an industrial environment when installed in accordance with these instructions. Specifically, this equipment is intended for use in clean, dry environments (Pollution degree 2 (a) ) and to circuits not exceeding Over Voltage Category II(b) (IEC 60664-1).(c)

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Do not remove the protective debris shield until after the controller and all other equipment in the panel near the controller are mounted and wiring is complete. Once the wiring is complete, remove the protective debris shield. Failure to remove the shield before operating can cause overheating.

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

For environments with greater vibration and shock concerns, use the panel mounting method that is described in Panel Mounting on page 26, rather than DIN rail mounting.

(a) Pollution Degree 2 is an environment where, normally, only non-conductive pollution occurs except that occasionally a temporary conductivity that is caused by condensation shall be expected.

(b) Over Voltage Category II is the load-level section of the electrical distribution system. At this level transient voltages are controlled and do not exceed the impulse voltage capability of the product's insulation.

(c) Pollution Degree 2 and Over Voltage Category II are International Electrotechnical Commission (IEC) designations.

## DIN Rail Mounting

The maximum extension of the latch is 14 mm (0.55 in.) in the open position. A flat-blade screwdriver is required to remove the controller. The controller can be mounted to EN 50022 35 x 7.5 or EN 50022 - 35 x 15 DIN rails. DIN rail mounting dimensions are shown in Figure 8 .

Figure 8 - DIN Rail Mounting Dimensions

<!-- image -->

To install your controller on the DIN rail, do as follows:

1. Mount your DIN rail. Make sure that the placement of the controller on the DIN rail meets the recommended spacing requirements. See Controller and Expansion I/O Spacing on page 24 .
2. Close the DIN latch, if it is open.
3. Hook the top slot over the DIN rail.
4. While pressing the controller down against the top of the rail, snap the bottom of the controller into position.
5. Leave the protective debris shield attached until you are finished wiring the controller and any other devices.

## To remove your controller from the DIN rail:

1. Place a flat-blade screwdriver in the DIN rail latch at the bottom of the controller.
2. Holding the controller, pry downward on the latch until the latch locks in the open position.
3. Repeat steps 1 and 2 for the second DIN rail latch.
4. Unhook the top of the DIN rail slot from the rail.

<!-- image -->

<!-- image -->

## 1762 Expansion I/O Module Dimensions

## Panel Mounting

Mount to panel using #8 or M4 screws. To install your controller using mounting screws:

1. Secure the template to the mounting surface. Make sure that your controller is spaced properly. See Controller and Expansion I/O Spacing on page 24 .
2. Drill holes through the template.
3. Remove the mounting template.
4. Mount the controller.
5. Leave the protective debris shield in place until you are finished wiring the controller and any other devices.

<!-- image -->

Figure 9 - 1762 Expansion I/O Module Dimensions

<!-- image -->

| Dimension Expansion I/O Module   |
|----------------------------------|
| A 90 mm (3.5 in.)                |
| B 40 mm (1.57 in.)               |
| C 87 mm (3.43 in.)               |

## Mount 1762 Expansion I/O

<!-- image -->

ATTENTION: During panel or DIN rail mounting of all devices, be sure that all debris such as metal chips and wire stands, is kept from falling into the module. Debris that falls into the module could cause damage when the module is under power.

## DIN Rail Mounting

The module can be mounted using the following DIN rails:

- 35 x 7.5 mm (EN 50022 - 35 x 7.5)
- 35 x 15 mm (EN 50022 - 35 x 15)

Before mounting the module on a DIN rail, close the DIN rail latch. Press the DIN rail mounting area of the module against the DIN rail. The latch momentarily opens and locks into place.

Use DIN rail end anchors (Allen-Bradley part number 1492-EA35 or 1492-EAH35) for vibration or shock environments. Figure 10 shows the location of the end anchors.

Figure 10 - End Anchor Location

<!-- image -->

<!-- image -->

1762 expansion I/O must be mounted horizontally as illustrated.

<!-- image -->

For environments with greater vibration and shock concerns, use the panel mounting method described below, instead of DIN rail mounting.

## Panel Mounting

Use the dimensional template shown in Figure 11 to mount the module. The preferred mounting method is to use two M4 or #8 panhead screws per module. Mounting screws are required on every module.

## Figure 11 - Dimensional Template

For more than 2 modules: (number of modules - 1) x 40 mm (1.59 in.)

A = 95 mm (3.74 in.) 1763-L16AWA, 1763-L16BWA, 1763-L16BBB, 1763-L16DWD

All dimensions are in mm (inches). Hole spacing tolerance: ±0.4 mm (0.016 in.)

<!-- image -->

## Connect Expansion I/O Modules

The expansion I/O module is attached to the controller or another I/O module by means of a flat ribbon cable after mounting, as shown in Figure 12 .

Figure 12 - Attach Expansion I/O Module

<!-- image -->

<!-- image -->

Use the pull loop on the connector to disconnect modules. Do not pull on the ribbon cable.

<!-- image -->

You can connect up to four expansion I/O modules to a controller.

<!-- image -->

<!-- image -->

ATTENTION: Remove power before removing or inserting an I/O module. When you remove or insert a module with power applied, an electric arc may occur. An electric arc can cause personal injury or property damage by:

- Sending an erroneous signal to your system's field devices, causing the controller to fault
- Causing an explosion in a hazardous environment

Electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance, reducing product reliability.

## WARNING: EXPLOSION HAZARD

In Class I Division 2 applications, the bus connector must be fully seated and the bus connector cover must be snapped in place.

In Class I Division 2 applications, all modules must be mounted in direct contact with each other as shown in Connect Expansion I/O Modules on page 28. If DIN rail mounting is used, an end emergency stop must be installed ahead of the controller and after the last 1762 I/O module.

## Wiring Requirements

## Wire Your Controller

## Wiring Recommendation

<!-- image -->

ATTENTION: Before you install and wire any device, disconnect power to the controller system.

<!-- image -->

ATTENTION: Calculate the maximum possible current in each power and common wire. Observe all electrical codes dictating the maximum current allowable for each wire size. Current above the maximum rating may cause wiring to overheat, which can cause damage.

United States Only: If the controller is installed within a potentially hazardous environment, all wiring must comply with the requirements stated in the National Electrical Code 501-10 (b).

- Allow for at least 50 mm (2 in.) between I/O wiring ducts or terminal strips and the controller.
- Route incoming power to the controller by a path separate from the device wiring. Where paths must cross, their intersection should be perpendicular.

<!-- image -->

Do not run signal or communications wiring and power wiring in the same conduit. Wires with different signal characteristics should be routed by separate paths.

- Separate wiring by signal type. Bundle wiring with similar electrical characteristics together.
- Separate input wiring from output wiring.
- Label wiring to all devices in the system. Use tape, shrink-tubing, or other dependable means for labeling purposes. In addition to labeling, use colored insulation to identify wiring based on signal characteristics. For example, you may use blue for DC wiring and red for AC wiring.

Table 3 - Wire Requirements

| Wire Type                  | Wire Size (2 wire maximum per terminal screw) (1)   | Wire Size (2 wire maximum per terminal screw) (1)   |
|----------------------------|-----------------------------------------------------|-----------------------------------------------------|
|                            |                                                     | 1 wire per terminal 2 wires per terminal            |
| Solid Cu 90 °C (194 °F)    | 0.5…4.0 mm2  (12…20 AWG) 0.5…1.5 mm2 (16…20 AWG)                                                     |                                                     |
| Stranded Cu 90 °C (194 °F) |                                                     | 0.5…2.5 mm2  (14…20 AWG) 0.5…0.75 mm2 (18…20 AWG)                                                     |

## Wiring the Terminal Block

The MicroLogix 1100 controllers have screw-cage clamps on the input and output terminal blocks. With screw-cage clamp terminal blocks, there is no need to attach additional hardware such as a spade lug to the wire, or use a fingersafe cover.

## To wire the terminal block:

1. Strip the end of the wire. The recommended length for the stripped end of the wire is 11.0 mm (0.44 in.).
2. Insert it into an open clamp.

<!-- image -->

## Use Surge Suppressors

3. Using a small screwdriver, tighten the terminal screw. To ensure that the wire conductor is secured inside the clamp, tighten it to the rated torque, 0.56 N·m (5.0 lb·in).

The diameter of the terminal screw head is 5.5 mm (0.22 in.).

<!-- image -->

Because of the potentially high current surges that occur when switching inductive load devices, such as motor starters and solenoids, the use of some type of surge suppression to protect and extend the operating life of the controllers output contacts is required. Switching inductive loads without surge suppression can significantly reduce the life expectancy of relay contacts. By adding a suppression device directly across the coil of an inductive device, you prolong the life of the output or relay contacts. You also reduce the effects of voltage transients and electrical noise from radiating into adjacent systems.

Figure 13 shows an output with a suppression device. We recommend that you locate the suppression device as close as possible to the load device.

Figure 13 - Output with Suppression Device Example

AC or DC

outputs

<!-- image -->

If the outputs are DC, we recommend that you use an 1N4004 diode for surge suppression, as shown in Figure 14. For inductive DC load devices, a diode is suitable. A 1N4004 diode is acceptable for most applications. A surge suppressor can also be used. See Table 4 for recommended suppressors. As shown in Figure 14, these surge suppression circuits connect directly across the load device.

Figure 14 - Relay or Solid-state DC Output with Suppression Device Example

<!-- image -->

Suitable surge suppression methods for inductive AC load devices include a varistor, an RC network, or an Allen-Bradley surge suppressor, all shown in Figure 15. These components must be appropriately rated to suppress the switching transient characteristic of the particular inductive device. See the table on 32 for recommended suppressors.

Figure 15 - Surge Suppression for Inductive AC Load Devices

<!-- image -->

## Ground the Controller

## Recommended Surge Suppressors

Use the Allen-Bradley surge suppressors shown in Table 4 for use with relays, contactors, and starters.

Table 4 - Recommended Surge Suppressors

|                                                               |                         | Device Coil Voltage Suppressor Catalog Number   |
|---------------------------------------------------------------|-------------------------|-------------------------------------------------|
| Bulletin 509 Motor Starter Bulletin 509 Motor Starter         | 120V AC 240V AC         | 599-K04(1) 599-KA04(1)                          |
| Bulletin 100 Contactor Bulletin 100 Contactor                 | 120V AC 240V AC         | 199-FSMA1(2) 199-FSMA2(2)                       |
| Bulletin 709 Motor Starter 120V AC                            |                         | 1401-N10(2)                                     |
| Bulletin 700 Type R, RM Relays AC coil None required          |                         |                                                 |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 12V DC 12V DC           | 199-FSMA9                                       |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 24V DC 24V DC           | 199-FSMA9                                       |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 48V DC 48V DC           | 199-FSMA9                                       |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 115…125V DC 115…125V DC | 199-FSMA10                                      |
| Bulletin 700 Type R Relay Bulletin 700 Type RM Relay          | 230…250V DC 230…250V DC | 199-FSMA11                                      |
| Bulletin 700 Type N, P, or PK Relay 150V max, AC or DC        |                         | 700-N24(2)                                      |
| Miscellaneous electromagnetic devices limited to 35 sealed VA | 150V max, AC or DC      | 700-N24(2)                                      |

In solid-state control systems, grounding and wire routing helps limit the effects of noise due to electromagnetic interference (EMI). Run the ground connection from the ground screw of the controller to the ground bus prior connecting any devices. Use 2.5 mm 2 (14 AWG) wire. For AC-powered controllers, this connection must be made for safety purposes.

<!-- image -->

ATTENTION: All devices connected to the RS-232/RS-485 communication port must be referenced to controller ground, or be floating (not referenced to a potential other than ground). Failure to follow this procedure may result in property damage or personal injury.

- For 1763-L16BWA controllers, the COM of the sensor supply is also connected to chassis ground internally. The 24V DC sensor power source should not be used to power output circuits. It should only be used to power input devices.
- For 1763-L16BBB and 1763-L16DWD controllers, the VDC NEUT or common terminal of the power supply is also connected to chassis ground internally.

This product is intended to be mounted to a well grounded mounting surface such as a metal panel. See the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional information. Additional grounding connections from the mounting tab or DIN rail, if used, are not required unless the mounting surface cannot be grounded.

<!-- image -->

Use all four mounting positions for panel mounting installation.

## Wiring Diagrams

<!-- image -->

<!-- image -->

ATTENTION: Remove the protective debris strip before applying power to the controller. Failure to remove the strip may cause the controller to overheat.

The following illustrations show the wiring diagrams for the MicroLogix 1100 controllers. Controllers with DC inputs can be wired as either sinking or sourcing inputs. Sinking and sourcing does not apply to AC inputs. See Sinking and Sourcing Wiring Diagrams on page 35 .

The controller terminal block layouts are shown in Terminal Block Layouts on page 33. The shading on the labels indicates how the terminals are grouped. A detail of the groupings is shown in the table following the terminal block layouts.

<!-- image -->

This symbol denotes a protective earth ground terminal, which provides a low impedance path between electrical circuits and earth for safety purposes and provides noise immunity improvement. This connection must be made for safety purposes on AC-powered controllers.

<!-- image -->

<!-- image -->

This symbol denotes a functional earth ground terminal, which provides a low impedance path between electrical circuits and earth for non-safety purposes, such as noise immunity improvement.

## Terminal Block Layouts

Figure 16 - 1763-L16AWA

<!-- image -->

Figure 17 - 1763-L16BWA

<!-- image -->

<!-- image -->

ATTENTION: The 24V DC sensor supply of the 1763-L16BWA should not be used to power output circuits. It should only be used to power input devices (for example, sensors, switches). See Master Control Relay on page 18 for information on MCR wiring in output circuits.

Figure 18 - 1763-L16BBB

<!-- image -->

Figure 19 - 1763-L16DWD

<!-- image -->

## Terminal Groupings

Table 5 - Input Terminal Grouping

| Controller   | Inputs   | Inputs                                     | Inputs   |
|--------------|----------|--------------------------------------------|----------|
| Controller   |          | Input Group Common Terminal Input Terminal |          |
| 1763-L16AWA  |          | Group 0 AC COM 0 I/0 through I/3           |          |
| 1763-L16AWA  |          | Group 1 AC COM 1 I/4 through I/9           |          |
| 1763-L16AWA  |          | Group 2 IA COM IV1(+) and IV2(+)           |          |
| 1763-L16BWA  |          | Group 0 DC COM 0 I/0 through I/3           |          |
| 1763-L16BWA  |          | Group 1 DC COM 1 I/4 through I/9           |          |
| 1763-L16BWA  |          | Group 2 IA COM IV1(+) and IV2(+)           |          |

## Sinking and Sourcing Wiring Diagrams

Table 5 - Input Terminal Grouping (Continued)

| Controller              | Inputs   | Inputs                                     | Inputs   |
|-------------------------|----------|--------------------------------------------|----------|
| Controller              |          | Input Group Common Terminal Input Terminal |          |
| 1763-L16BBB 1763-L16DWD |          | Group 0 DC COM 0 I/0 through I/3           |          |
| 1763-L16BBB 1763-L16DWD |          | Group 1 DC COM 1 I/4 through I/9           |          |
| 1763-L16BBB 1763-L16DWD |          | Group 2 IA COM IV1(+) and IV2(+)           |          |

Table 6 - Output Terminal Grouping

| Controller                          | Outputs   | Outputs                                                   | Outputs         | Outputs                                   |
|-------------------------------------|-----------|-----------------------------------------------------------|-----------------|-------------------------------------------|
| Controller                          |           | Output Group Voltage Terminal Output Terminal Description |                 |                                           |
| 1763-L16AWA 1763-L16BWA 1763-L16DWD | Group 0   | VAC/VDC                                                   | O/0             | Isolated Relay output                     |
| 1763-L16AWA 1763-L16BWA 1763-L16DWD |           |                                                           |                 | Group 1 VAC/VDC O/1 Isolated Relay output |
| 1763-L16AWA 1763-L16BWA 1763-L16DWD | Group 2   | VAC/VDC                                                   | O/2             | Isolated Relay output                     |
| 1763-L16AWA 1763-L16BWA 1763-L16DWD |           |                                                           |                 | Group 3 VAC/VDC O/3 Isolated Relay output |
| 1763-L16AWA 1763-L16BWA 1763-L16DWD | Group 4   | VAC/VDC                                                   | O/4             | Isolated Relay output                     |
| 1763-L16AWA 1763-L16BWA 1763-L16DWD |           |                                                           |                 | Group 5 VAC/VDC O/5 Isolated Relay output |
| 1763-L16BBB                         | Group 0   | VAC/VDC                                                   | O/0             | Isolated Relay output                     |
| 1763-L16BBB                         |           |                                                           |                 | Group 1 VAC/VDC O/1 Isolated Relay output |
| 1763-L16BBB                         | Group 2   | DC +24V, DC -24V                                          | O/2 through O/5 | FET output                                |

Any of the MicroLogix 1100 controller DC embedded input groups can be configured as sinking or sourcing depending on how the DC COM is wired on the group.

|                | Type Definition                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sinking Input  | The input energizes when a high-level voltage is applied to the input terminal (active high). Connect the power supply VDC (-) to the input group’s COM terminal. |
| Sourcing Input | The input energizes when a low-level voltage is applied to the input terminal (active low). Connect the power supply VDC (+) to the input group’s COM terminal.   |

<!-- image -->

ATTENTION: The 24V DC sensor power source must not be used to power output circuits. It should only be used to power input devices (for example, sensors, switches). See Master Control Relay on page 16 for information on MCR wiring in output circuits.

## 1763-L16AWA, 1763-L16BWA, 1763-L16BBB, and 1763-L16DWD Wiring Diagrams

<!-- image -->

In Figure 20 to Figure 27, lower case alphabetic subscripts are appended to common-terminal connections to indicate that different power sources may be used for different isolated groups, if desired.

Figure 20 - 1763-L16AWA Input Wiring Diagram (1)

<!-- image -->

(1) "NOT USED" terminals are not intended for use as connection points.

Figure 21 - 1763-L16BWA Sinking Input Wiring Diagram

<!-- image -->

Figure 22 - 1763-L16BWA Sourcing Input Wiring Diagram

<!-- image -->

Figure 23 - 1763-L16BBB and 1763-L16DWD Sinking Input Wiring Diagram

<!-- image -->

Figure 24 - 1763-L16BBB and 1763-L16DWD Sourcing Input Wiring Diagram

<!-- image -->

Figure 25 - 1763-L16AWA and 1763-L16BWA Output Wiring Diagram

<!-- image -->

Figure 26 - 1763-L16BBB Output Wiring Diagram

<!-- image -->

Figure 27 - 1763-L16DWD Output Wiring Diagram

<!-- image -->

## Controller I/O Wiring

## Wire Your Analog Channels

## Minimizing Electrical Noise

Because of the variety of applications and environments where controllers are installed and operating, it is impossible to ensure that all environmental noise will be removed by input filters. To help reduce the effects of environmental noise, install the MicroLogix 1100 system in a properly rated (for example, NEMA) enclosure. Make sure that the MicroLogix 1100 system is properly grounded.

A system may malfunction due to a change in the operating environment after a period of time. We recommend periodically checking system operation, particularly when new machinery or other noise sources are installed near the MicroLogix 1100 system.

Analog input circuits can monitor voltage signals and convert them to serial digital data.

<!-- image -->

## Analog Channel Wiring Guidelines

Consider the following when wiring your analog channels:

- The analog common (COM) is connected to earth ground inside the module. These terminals are not electrically isolated from the system. They are connected to chassis ground.
- Analog channels are not isolated from each other.

- Use Belden 8761, or equivalent, shielded wire.
- Under normal conditions, the drain wire (shield) should be connected to the metal mounting panel (earth ground). Keep the shield connection to earth ground as short as possible.
- To ensure optimum accuracy for voltage-type inputs, limit overall cable impedance by keeping all analog cables as short as possible. Locate the I/O system as close to your voltage-type sensors or actuators as possible.
- The controller does not provide loop power for analog inputs. Use a power supply that matches the transmitter specifications as shown in Figure 28 .

Figure 28 - Sensor/Transmitter Types

<!-- image -->

## Minimize Electrical Noise on Analog Channels

Inputs on analog channels employ digital high-frequency filters that significantly reduce the effects of electrical noise on input signals. However, because of the variety of applications and environments where analog controllers are installed and operated, it is impossible to ensure that all environmental noise will be removed by the input filters.

Several specific steps can be taken to help reduce the effects of environmental noise on analog signals:

- Install the MicroLogix 1100 system in a properly rated (for example, NEMA) enclosure. Make sure that the MicroLogix 1100 system is properly grounded.
- Use Belden cable #8761 for wiring the analog channels, making sure that the drain wire and foil shield are properly earth grounded.
- Route the Belden cable separately from any AC wiring. Additional noise immunity can be obtained by routing the cables in a grounded conduit.

## Ground Your Analog Cable

Use a shielded communication cable (Belden #8761). The Belden cable has two signal wires (black and clear), one drain wire, and a foil shield. The drain wire and foil shield must be grounded at one end of the cable.

## Expansion I/O Wiring

<!-- image -->

IMPORTANT

Do not ground the drain wire and foil shield at both ends of the cable.

## Digital Wiring Diagrams

Figure 29 to Figure 41 show the digital expansion I/O wiring diagrams.

Figure 29 - 1762-IA8 Wiring Diagram

L1

100/120V AC

L2

Figure 30 - 1762-IQ8 Wiring Diagram

<!-- image -->

IN 1

IN 3

IN 5

IN 7

AC

COM

AC

COM

IN 0

IN 2

IN 4

IN 6

Commons are connected internally.

Figure 31 - 1762-IQ16 Wiring Diagram

<!-- image -->

Figure 32 - 1762-IQ32T Wiring Diagram

<!-- image -->

Figure 33 - 1762-OA8 Wiring Diagram

<!-- image -->

Figure 34 - 1762-OB8 Wiring Diagram

<!-- image -->

Figure 35 - 1762-OB16 Wiring Diagram

<!-- image -->

Figure 36 - 1762-OB32T Wiring Diagram

<!-- image -->

<!-- image -->

Figure 37 - 1762-OV32T Wiring Diagram

<!-- image -->

<!-- image -->

Figure 38 - 1762-OW8 Wiring Diagram

<!-- image -->

Figure 39 - 1762-OW16 Wiring Diagram

<!-- image -->

Figure 40 - 1762-OX6I Wiring Diagram

<!-- image -->

Figure 41 - 1762-IQ8OW6 Wiring Diagram

<!-- image -->

## Analog Wiring

Consider the following when wiring your analog modules:

- The analog common (COM) is not connected to earth ground inside the module. All terminals are electrically isolated from the system.
- Channels are not isolated from each other.
- Use Belden 8761, or equivalent, shielded wire.
- Under normal conditions, the drain wire (shield) should be connected to the metal mounting panel (earth ground). Keep the shield connection to earth ground as short as possible.
- To ensure optimum accuracy for voltage-type inputs, limit overall cable impedance by keeping all analog cables as short as possible. Locate the I/O system as close to your voltage-type sensors or actuators as possible.
- The module does not provide loop power for analog inputs. Use a power supply that matches the input transmitter specifications.

## 1762-IF2OF2 Input Type Selection

Select the input type, current or voltage, using the switches on the module's circuit board and the input type/range selection bits in the Configuration Data File. See the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001. You can access the switches through the ventilation slots on the top of the module. Switch 1 controls channel 0; switch 2 controls channel 1. The factory default setting for both switch 1 and switch 2 is Current. Switch positions are shown in Figure 42 .

Figure 42 - Select Input Type with the Switches

1762-IF2OF2 Output Type Selection

<!-- image -->

The output type selection, current or voltage, is made by wiring to the appropriate terminals, Iout or Vout, and by the type/range selection bits in the Configuration Data File. See the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

<!-- image -->

ATTENTION: Analog outputs may fluctuate for less than a second when power is applied or removed. This characteristic is common to most analog outputs. While the majority of loads will not recognize this short signal, it is recommended that preventive measures be taken to ensure that connected equipment is not affected.

<!-- image -->

## 1762-IF2OF2 Wiring

Figure 43 shows the 1762-IF2OF2 analog expansion I/O terminal block.

Figure 43 - 1762-IF2OF2 Terminal Block Layout

<!-- image -->

Figure 44 - Differential Sensor Transmitter Types

<!-- image -->

Figure 45 - Single-ended Sensor/Transmitter Types

<!-- image -->

(1) All power supplies rated N.E.C. Class 2

## 1762-IF4 Input Type Selection

Select the input type, current or voltage, using the switches on the module's circuit board and the input type/range selection bits in the Configuration Data File. See the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001. You can access the switches through the ventilation slots on the top of the module.

Figure 46 - 1762-IF4 Switch Positions

<!-- image -->

Figure 47 - 1762-IF4 Terminal Block Layout

<!-- image -->

Figure 48 - Differential Sensor Transmitter Types

<!-- image -->

<!-- image -->

Grounding the cable shield at the module end only usually provides sufficient noise immunity. However, for best cable shield performance, earth ground the shield at both ends, using a 0.01 µF capacitor at one end to block AC power ground currents, if necessary.

Figure 49 - Sensor/Transmitter Types

<!-- image -->

(1) All power supplies rated N.E.C. Class 2

## 1762-OF4 Output Type Selection

The output type selection, current or voltage, is made by wiring to the appropriate terminals, Iout or Vout, and by the type/range selection bits in the Configuration Data File.

Figure 50 - 1762-OF4 Terminal Block Layout

<!-- image -->

Figure 51 - 1762-OF4 Wiring

<!-- image -->

## Notes:

## Supported Communication Protocols

## Default Communication Configuration

## Communication Connections

The method that you use and cabling that is required to connect your controller depends on what type of system you are employing. This chapter also describes how the controller establishes communication with the appropriate network.

The MicroLogix 1100 controllers provide two communication channels, an isolated RS-232/RS-485 communication port (Channel 0) and an Ethernet port (Channel 1).

MicroLogix 1100 controllers support the following communication protocols from the primary RS-232/RS-485 communication channel, Channel 0:

- DH-485
- DF1 Full-duplex
- DF1 Half-duplex master and slave
- DF1 Radio modem
- Modbus RTU master and slave
- ASCII

The Ethernet communication channel, Channel 1, allows your controller to be connected to a local area network for various devices providing 10 Mbps/100 Mbps transfer rate. MicroLogix 1100 controllers support CIP explicit messaging (message exchange). MicroLogix 1100 controllers do not support Ethernet I/O master capability through CIP implicit messaging (real-time I/O messaging).

For more information on MicroLogix 1100 communications, see the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

The MicroLogix 1100 communication Channel 0 has the following default communication configuration.

<!-- image -->

For Channel 0, the default configuration is present when:

- The controller is powered-up for the first time.
- The Communications Toggle functionality specifies default communications (Specified using the LCD Display. The DCOMM indicator on the LCD Display is On, that is, lit in solid rectangle.).
- An OS upgrade is completed.

See Use the LCD and Keypad on page 71 for more information about using the LCD Display.

See Connect to Networks via Ethernet Interface on page 155 for more information on communicating.

| Parameter Default                         |
|-------------------------------------------|
| Baud Rate 19.2 KBps                       |
| Parity None                               |
| Source ID (Node Address) 1                |
| Control Line No handshaking               |
| Error Detection CRC                       |
| Embedded Responses Auto detect            |
| Duplicate Packet (Message) Detect Enabled |
| ACK Timeout 50 counts                     |

Table 7 - DF1 Full-duplex Default Configuration Parameters

<!-- image -->

## Use the Communications Toggle Functionality

Table 7 - DF1 Full-duplex Default Configuration Parameters (Continued)

| Parameter Default     |
|-----------------------|
| NAK retries 3 retries |
| ENQ retries 3 retries |
| Stop Bits 1           |
| Data Bits 8           |

The Communications Toggle functionality can be operated using the LCD display on the controller, as shown in Figure 52 .

Use the Communications Toggle functionality to change from the user-defined communication configuration to the default communications mode and back on Channel 0. The Default Communications (DCOMM) indicator on the LCD display operates to show when the controller is in the default communications mode (settings are shown in Table 7).

Figure 52 - DCOMM Indicator on LCD Display

<!-- image -->

<!-- image -->

The Communications Toggle functionality only affects the communication configuration of Channel 0.

## Change Communication Configuration

Follow this procedure to change from the user-defined communication configuration to the default communications mode and back. In this example, we start from the Main Menu screen of the LCD display. If necessary, press ESC repeatedly until you return to the Main Menu screen.

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items are not displayed on the Main Menu screen, scroll down the screen by pressing the Down key.

<!-- image -->

2. Press OK on the LCD keypad. The Advanced Settings Menu screen is displayed.
3. Select DCOMM Cfg using the Up and Down keys, then press OK.
4. The DCOMM Configuration screen displays. The current status, Disable in this example, is selected by default.

<!-- image -->

<!-- image -->

The DCOMM status indicator, which is the third of the five indicators at the top left of the LED display, is displayed as an empty rectangle. It means that the communication configuration is set to a user-defined communication mode.

<!-- image -->

5. Use the up arrow to change the indicator position so that it points to Enable. Press OK to change to the default communication mode.

<!-- image -->

The DCOMM Mode Change Notification screen displays. It indicates that the communication configuration is changed to the default communication mode. The DCOMM status indicator displays as a solid rectangle.

<!-- image -->

If you change to the user-defined configuration from the default configuration mode by selecting Disable and pressing OK, the DCOMM Mode Change Notification displays.

<!-- image -->

6. Press ESC to return to the Advanced Settings Menu screen, as shown in step 3 .

## Connect to the RS-232 Port

There are two ways to connect the MicroLogix 1100 programmable controller to your computer using the DF1 protocol: using a point-to-point connection or using a modem. Descriptions of these methods follow.

<!-- image -->

ATTENTION: All devices connected to the RS-232/RS-485 communication port must be referenced to controller ground, or be floating (not referenced to a potential other than ground). Failure to follow this procedure may result in property damage or personal injury.

- For 1763-L16BWA controllers, the COM of the sensor supply is also connected to chassis ground internally. The 24V DC sensor power source should not be used to power output circuits. It should only be used to power input devices.
- For 1763-L16BBB and 1763-L16DWD controllers, the VDC NEUT or common terminal of the power supply is also connected to chassis ground internally.

## Table 8 - Available Communication Cables

| Communication Cables Length                                                                          |
|------------------------------------------------------------------------------------------------------|
| 1761-CBL-AM00, series C or later cables are required for Class I Div 2 applications 45 cm (17.7 in.) |
| 1761-CBL-AP00, series C or later cables are required for Class I Div 2 applications 45 cm (17.7 in.) |
| 1761-CBL-PM02, series C or later cables are required for Class I Div 2 applications 2 m (6.5 ft.)    |
| 1761-CBL-HM02, series C or later cables are required for Class I Div 2 applications 2 m (6.5 ft.)    |
| 1761-CBL-PH02, series A or later cables are required for Class I Div 2 applications 2 m (6.5 ft.)    |
| 1761-CBL-AH02, series A or later cables are required for Class I Div 2 applications 2 m (6.5 ft.)    |
| 2707-NC9, series C or later cables are required for Class I Div 2 applications 15 m (49.2 ft.)       |
| 1763-NC01, series A or later 30 cm (11.8 in.)                                                        |

<!-- image -->

## ATTENTION: UNSUPPORTED CONNECTION

Do not connect a MicroLogix 1100 controller to another MicroLogix family controller such as MicroLogix 1000, MicroLogix 1200, MicroLogix 1500, or to the 1747-DPS1 network port using a 1761-CBL-AM00 (8-pin mini-DIN to 8-pin miniDIN) cable or equivalent.

This type of connection causes damage to the RS-232/RS-485 communication port (Channel 0) of the MicroLogix 1100 controller and/or the controller itself. Communication pins that are used for RS-485 communications are alternately used for 24V power on the other MicroLogix controllers and the 1747-DPS1 network port.

## Make a DF1 Point-to-point Connection

You can connect the MicroLogix 1100 programmable controller to your computer using a serial cable (1761-CBL-PM02) from your computer's serial port to the controller's Channel 0. The recommended protocol for this configuration is DF1 Full-duplex.

You can connect a MicroLogix 1100 controller to your computer directly without using an external optical isolator, such as Advanced Interface Converter (AIC+), catalog number 1761-NET-AIC, as shown in Figure 53, because Channel 0 is isolated within the controller.

Figure 53 - Point-to-point Connection

<!-- image -->

(1) Series C or later cables are required for Class I Division 2 applications.

## Use a Modem

You can use modems to connect a computer to one MicroLogix 1100 controller (using DF1 Fullduplex protocol), to multiple controllers (using DF1 Half-duplex protocol), or Modbus RTU slave protocol via Channel 0, as shown in Figure 54. See Connect to Networks via RS-232/RS-485 Interface on page 145 for information on the types of modems that you can use with the micro controllers.

## IMPORTANT

Do not attempt to use the DH-485 protocol through modems under any circumstance. The communication timing using the DH-485 protocol is not supported by modem communications.

<!-- image -->

(1) Series C or later cables are required for Class I Division 2 applications.

You can connect a MicroLogix 1100 controller to your modem directly without using an external optical isolator, such as AIC+, catalog number 1761-NET-AIC, as shown in Figure 54, because Channel 0 is isolated within the controller.

## MicroLogix 1100 Channel 0 to Modem Cable Pinout

When connecting the MicroLogix 1100 controller Channel 0 to a modem using an RS-232 cable, the maximum that the cable length may be extended is 15.24 m (50 ft.).

| DTE Device (MicroLogix 1100 controller Channel 0)   | DCE Device (Modem, PanelView™, and so on)   | DCE Device (Modem, PanelView™, and so on)   |
|-----------------------------------------------------|---------------------------------------------|---------------------------------------------|
|                                                     | 8-pin 25-pin 9-pin                          |                                             |
|                                                     | 7 TXD TXD 2 3                               |                                             |
|                                                     | 4 RXD RXD 3 2                               |                                             |
|                                                     | 2 GND GND 7 5                               |                                             |
|                                                     | 1 B(+) DCD 8 1                              |                                             |
|                                                     | 8 A(-) DTR 20 4                             |                                             |
|                                                     | 5 N.C. DSR 6 6                              |                                             |
|                                                     | 6 CTS CTS 5 8                               |                                             |
|                                                     | 3 RTS RTS 4 7                               |                                             |

<!-- image -->

ATTENTION: Do not connect pin 1, 8, and 5. This connection causes damage to the RS-232/RS-485 communication port (channel 0) of the MicroLogix 1100 controller and/or the controller itself.

## Connect to a DF1 Half-duplex Network

Table 9 shows available parameters for a communication port that is configured for DF1 Halfduplex slave.

Table 9 - DF1 Half-duplex Configuration Parameters

| Parameter Options                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Baud Rate 300, 600, 1200, 2400, 4800, 9600, 19.2 Kbps, 38.4 Kbps                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                   | Parity None, even                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                   | Node Address 0...254 decimal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                   | Control Line No handshaking, half-duplex modem (RTS/CTS handshaking, no handshaking (485 network)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Error Detection CRC, BCC          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| EOT Suppression                   | Enabled, disabled When EOT Suppression is enabled, the slave does not respond when polled if no message is queued. This saves modem transmission power and time when there is no message to transmit.                                                                                                                                                                                                                                                                                                                              |
| Duplicate Packet (Message) Detect | Enabled, disabled Detects and eliminates duplicate responses to a message. Duplicate packets may be sent under noisy communication conditions if the sender’s Message Retries are not set to 0.                                                                                                                                                                                                                                                                                                                                    |
| Poll Timeout (x20 ms)             | 0...65,535 (can be set in 20 ms increments) Poll Timeout only applies when a slave device initiates a MSG instruction. It is the amount of time that the slave device waits for a poll from the master device. If the slave device does not receive a poll within the Poll Timeout, a MSG instruction error is generated, and the ladder program must requeue the MSG instruction. If you are using a MSG instruction, it is recommended that a Poll Timeout value of zero not be used. Poll Timeout is disabled when set to zero. |
| RTS Off Delay (x20 ms)            | 0...65,535 (can be set in 20 ms increments) Specifies the delay time between when the last serial character is sent to the modem and when RTS is deactivated. Gives the modem extra time to transmit the last character of a packet.                                                                                                                                                                                                                                                                                               |
| RTS Send Delay (x20 ms)           | 0...65,535 (can be set in 20 ms increments) Specifies the time delay between setting RTS until checking for the CTS response. For use with modems that are not ready to respond with CTS immediately upon receipt of RTS.                                                                                                                                                                                                                                                                                                          |
| Message Retries                   | 0...255 Specifies the number of times a slave device attempts to resend a message packet when it does not receive an ACK from the master device. For use in noisy environments where message packets may become corrupted in transmission.                                                                                                                                                                                                                                                                                         |
| Pre Transmit Delay (x1 ms)        | 0...65,535 (can be set in 1 ms increments) When the Control Line is set to no handshaking, this is the delay time before transmission. Required for 1761-NET-AIC physical half duplex networks. The 1761-NET-AIC needs a delay time to change from transmit to receive mode. When the Control Line is set to DF1 Half-duplex Modem, this is the minimum time delay between receiving the last character of a packet and the RTS assertion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## DF1 Half-duplex Master/Slave Network

Use Figure 55 for DF1 Half-duplex master/slave protocol without hardware handshaking.

Figure 55 - DF1 Half-duplex Master/Slave Protocol

<!-- image -->

- (1) DB-9 RS-232 port
- (2) mini-DIN 8 RS-232 port
- (3) RS-485 port
- (4) Series C or later cables are required for Class I Division 2 applications.

DF1 Half-duplex Network (Using PC and Modems)

Figure 56 - DF1 Half-duplex Protocol

<!-- image -->

## Connecting to a DH-485 Network

The network diagrams on the next pages provide examples of how to connect MicroLogix 1100 controllers to the DH-485 network.

You can connect a MicroLogix 1100 controller to your DH-485 network directly without using an external optical isolator, such as MicroLogix and SLC Communication Adapter (1761-NET-AIC), as shown in Figure 58, because Channel 0 is isolated within the controller.

<!-- image -->

Use a 1763-NC01 series A or later (8-pin mini-DIN to 6-pin DH-485 connector) cable or equivalent to connect a MicroLogix 1100 controller to a DH-485 network.

Figure 57 - 1761-NC01 MicroLogix Cable

<!-- image -->

We recommend that you use a 1747-UIC USB interface to connect your computer to a DH-485 network. For more information on the 1747-UIC, see the Universal Serial Bus (USB) to DH-485 Interface Converter Installation Instructions, publication 1747-IN063 .

## DH-485 Configuration Parameters

When MicroLogix communications are configured for DH-485, the following parameters can be changed:

Table 10 - DH-485 Configuration Parameters

| Parameter Options           |
|-----------------------------|
| Baud Rate 9600, 19.2 KBps   |
| Node Address 1...31 decimal |
| Token Hold Factor 1...4     |

See Software Considerations on page 150 for tips on setting the parameters listed in Table 10 .

DH-485 Network with a MicroLogix 1100 Controller

Figure 58 - Connect to a DH-485 Network

<!-- image -->

## Typical 3-node Network (Channel 0 Connection)

<!-- image -->

## Recommended Tools

To connect a DH-485 network to additional devices, you need tools to strip the shielded cable and to attach the cable to the AIC+ Advanced Interface Converter. We recommend the following equipment (or equivalent):

Table 11 - Working with Cables for DH-485 Network

| Description Part Number Manufacturer                   |
|--------------------------------------------------------|
| Shielded twisted-pair cable #3106A or #9842 Belden     |
| Stripping tool Not applicable Not applicable           |
| 1/8” slotted screwdriver Not applicable Not applicable |

## DH-485 Communication Cable

The suggested DH-485 communication cable is either Belden #3106A or #9842. The cable is jacketed and shielded with one or two twisted-wire pairs and a drain wire.

One pair provides a balanced signal line and one additional wire is used for a common reference line between all nodes on the network. The shield reduces the effect of electrostatic noise from the industrial environment on network communication.

The communication cable consists of a number of cable segments daisy chained together. The total length of the cable segments cannot exceed 1219 m (4000 ft.). However, two segments can be used to extend the DH-485 network to 2438 m (8000 ft.). For additional information on connections using the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

When cutting cable segments, make them long enough to route them from one AIC+ to the next, with sufficient slack to help prevent strain on the connector. Allow enough extra cable to help prevent chafing and kinking in the cable.

Use these instructions for wiring the Belden #3106A or #9842 cable. See Cable Selection Guide on page 64 if you are using standard Allen-Bradley cables.)

## Connecting the Communication Cable to the DH-485 Connector

<!-- image -->

A daisy chained network is recommended. Do not make the incorrect connection that is shown in Figure 59 .

Figure 59 - Connect Communication Cable to DH-485 Connector

<!-- image -->

Single Cable Connection

When connecting a single cable to the DH-485 connector, use Figure 60 .

Figure 60 - Single Cable Connection

<!-- image -->

Multiple Cable Connections

When connecting multiple cables to the DH-485 connector, use Figure 61 .

Figure 61 - Multiple Cable Connections

<!-- image -->

Table 12 - Connections using Belden #3106A Cable

| For this Wire/Pair Connect this Wire To this Terminal   |                                                |
|---------------------------------------------------------|------------------------------------------------|
|                                                         | Shield/drain Non-jacketed Terminal 2 - Shield  |
|                                                         | Blue Blue Terminal 3 - (Common)                |
| White/orange                                            | White with orange stripe Terminal 4 - (Data B) |
| White/orange                                            | Orange with white stripe Terminal 5 - (Data A) |

Table 13 - Connections using Belden #9842 Cable

|              | For this Wire/Pair Connect this Wire To this Terminal   |
|--------------|---------------------------------------------------------|
|              | Shield/drain Non-jacketed Terminal 2 - Shield           |
| Blue/white   | White with blue stripe  Cut back - no connection(1)     |
| Blue/white   | Blue with white stripe Terminal 3 - (Common)            |
| White/orange | White with orange stripe Terminal 4 - (Data B)          |
| White/orange | Orange with white stripe Terminal 5 - (Data A)          |

## Connect the AIC+

## Ground and Terminate the DH-485 Network

Only one connector at the end of the link must have Terminals 1 and 2 jumpered together. This provides an earth ground connection for the shield of the communication cable.

Both ends of the network must have Terminals 5 and 6 jumpered together, as shown in Figure 62. This connects the termination impedance (of 120 Ω) that is built into each AIC+ or the 1763-NC01 cable as required by the DH-485 specification.

Figure 62 - End-of-Line Termination

<!-- image -->

MicroLogix 1100 Channel 0 to DH-485 Communication Cable Pinout

When connecting the MicroLogix 1100 controller Channel 0 to a DH-485 communication cable pinout using an RS-232 cable, the maximum that the cable length may be extended is 15.24 m (50 ft.). See Figure 63 .

Figure 63 - DH-485 Communications Cable Pinout

<!-- image -->

You can connect a MicroLogix 1100 controller to a DH-485 network via Channel 0 directly without using an optical isolator, such as AIC+, catalog number 1761-NET-AIC, because Channel 0 is isolated. However, you must use an AIC+ to connect your computer or other MicroLogix family products, such as MicroLogix 1200 controllers, to a DH-485 network.

Figure 64 shows the external wiring connections and specifications of the AIC+.

<!-- image -->

Figure 64 - AIC+ External Wiring Connections

| Item Description                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------|
| 1 Port 1 - DB-9 RS-232, DTE                                                                                            |
| 2 Port 3 - RS-485 Phoenix plug                                                                                         |
| 3 Port 2 - mini-DIN 8 RS-232 DTE                                                                                       |
| 4  DC Power source selector switch (Cable = Port 2 power source, External = External power source connected to item 5) |
| 5 Terminals for external 24V DC power supply and chassis ground                                                        |

For additional information on connecting the AIC+, see the AIC+ Advanced Interface Converter User Manual , publication 1761-UM004 .

## Cable Selection Guide

<!-- image -->

|                                                 |                                              | Cable Length Connections from to AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | SLC 5/03 or SLC 5/04 processors, ch 0 Port 2 Yes External                   |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | MicroLogix 1000, 1200, or 1500 controllers, ch 0 Port 1 Yes External        |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | MicroLogix 1100 controller, ch 0 Port 1 Yes External                        |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | PanelView 550 terminal through NULL modem adapter Port 2 Yes External       |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | DTAM™ Plus / DTAM™ Micro Port 2 Yes External                                |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | PC COM port Port 2 Yes External                                             |                                      |

<!-- image -->

|                                                 |                                              | Cable Length Connections from to AIC+                            | External Power Supply Required (1)   | Power Selection Switch Setting   |
|-------------------------------------------------|----------------------------------------------|------------------------------------------------------------------|--------------------------------------|----------------------------------|
| 1761-CBL-AM00(2) 1761-CBL-HM02(2) 1761-CBL-AH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | MicroLogix 1000, 1200, or 1500 controllers, ch 0 Port 2 No Cable |                                      |                                  |
| 1761-CBL-AM00(2) 1761-CBL-HM02(2) 1761-CBL-AH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | MicroLogix 1100 controller, ch 0 Port 2 Yes External             |                                      |                                  |
| 1761-CBL-AM00(2) 1761-CBL-HM02(2) 1761-CBL-AH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | To port 2 on another AIC+ Port 2 Yes External                    |                                      |                                  |

(1) An external power supply is required unless the AIC+ is powered by the device that is connected to port 2, then the selection switch should be set to cable.

(2) Series C or later cables are required.

<!-- image -->

|                           |                                | Cable Length Connections from to AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|---------------------------|--------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | SLC 5/03 or SLC 5/04 processor, ch 0 Port 1 Yes External                    |                                      |
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

## 1761-CBL-PM02 Series C (or equivalent) Cable Wiring Diagram

<!-- image -->

<!-- image -->

## Recommended User-supplied Components

These components can be purchased from your local electronics supplier.

Table 14 - User-supplied Components

| Component Recommended Model                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|
| External power supply and chassis ground Power supply rated for 20.4...28.8V DC                                   |
| NULL modem adapter Standard AT                                                                                    |
| Straight 9-pin to 25-pin RS-232 cable  See Figure 65 and Table 15 for port information if making your own cables. |

## Figure 65 - Port Pinout

<!-- image -->

Table 15 - Cable Assignment

| Pin Port 1: DB-9 RS-232  Port 2(1): 1761-CBL-PM02 cable Port 3: RS-485 Connector   |
|------------------------------------------------------------------------------------|
| 1 Received line signal detector (DCD) 24V DC Chassis ground                        |
| 2 Received data (RxD) Ground (GND) Cable shield                                    |
| 3 Transmitted data (TxD) Request to send (RTS) Signal ground                       |
| 4  DTE ready (DTR) (2) Received data (RxD)(3) DH-485 data B                        |
| 5 Signal common (GND) Received line signal detector (DCD) DH-485 data A            |
| 6  DCE ready (DSR)(2)  Clear to send (CTS)(3)  Termination                         |
| 7 Request to send (RTS) Transmitted data (TxD) Not applicable                      |
| 8 Clear to send (CTS) Ground (GND) Not applicable                                  |
| 9 Not applicable Not applicable Not applicable                                     |

(1) An 8-pin mini-DIN connector is used for making connections to port 2. This connector is not commercially available. If you are making a cable to connect to port 2, you must configure your cable to connect to the Allen-Bradley cable shown in Figure 65 .

(2) On port 1, pin 4 is electronically jumpered to pin 6. Whenever the AIC+ is powered on, pin 4 matches the state of pin 6. (3) In the 1761-CBL-PM02 cable, pins 4 and 6 are jumpered together within the DB-9 connector.

<!-- image -->

<!-- image -->

## Safety Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D, or non-hazardous locations only.

<!-- image -->

## ATTENTION: EXPLOSION HAZARD

AIC+ must be operated from an external power source.

This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.

See Safety Considerations on page 15 for additional information.

## Install and Attach the AIC+

1. Take care when installing the AIC+ in an enclosure so that the cable connecting the MicroLogix controller to the AIC+ does not interfere with the enclosure door.
2. Carefully plug the terminal block into the RS-485 port on the AIC+ you are putting on the network. Allow enough cable slack to help prevent stress on the plug.
3. Provide strain relief for the Belden cable after it is wired to the terminal block. This guards against breakage of the Belden cable wires.

## Power the AIC+

MicroLogix 1000, MicroLogix 1200, and MicroLogix 1500 programmable controllers support 24V DC communication power on Channel 0. When connected to the 8-pin mini-DIN connector on the 1761-NET-AIC, 1761-NET-ENI, and the 1761-NET-ENIW, these controllers provide the power for the interface converter modules.

The MicroLogix 1100 controller does not provide 24V DC communication power. Instead these pins are used to provide RS-485 communications directly. Any AIC+, ENI, or ENIW not connected to a MicroLogix 1000, MicroLogix 1200, or MicroLogix 1500 controller requires a 24V DC power supply.

If both the controller and external power are connected to the AIC+, the power selection switch determines what device powers the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if a higher voltage supply is used.

Set the DC Power Source selector switch to EXTERNAL before connecting the power supply to the AIC+. Figure 66 shows where to connect external power for the AIC+.

Figure 66 - External Power for AIC+

<!-- image -->

## Connecting to Ethernet

<!-- image -->

ATTENTION: Always connect the CHS GND (chassis ground) terminal to the nearest earth ground. This connection must be made whether or not an external 24V DC supply is used.

Power Options

There are two options for powering the AIC+:

- Use the 24V DC user power supply built into the MicroLogix 1000, MicroLogix 1200, or MicroLogix 1500 controller. The AIC+ is powered through a hard-wired connection using a communication cable (1761-CBL-HM02, or equivalent) connected to port 2.
- Use an external DC power supply with the following specifications:
- Operating voltage: 24V DC (-15%/+20%)
- Output current: 150 mA minimum
- Rated NEC Class 2

Make a hard-wired connection from the external supply to the screw terminals on the bottom of the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if miswired with the wrong power source.

You can connect a MicroLogix 1100 controller to an Ethernet network via the Ethernet port (Channel 1). You do not need to use an Ethernet interface card, such as the Ethernet Interface (ENI) and (ENIW), 1761-NET-ENI and 1761-NET-ENIW, to connect your MicroLogix 1100 controller to an Ethernet network. For additional information on connecting to an Ethernet network, see Connect to Networks via Ethernet Interface on page 155 .

<!-- image -->

## Ethernet Connections

The Ethernet connector, Channel 1, is an RJ45, 10/100 Base-T connector. The pinout for the connector is shown in Table 16 .

Table 16 - RJ45 Connector Pinout

| Pin Pin Name               |
|----------------------------|
| 1 Tx+                      |
| 2 Tx                            |
| 3 Rx+                      |
| 4 Not used by 10/100Base-T |
| 5 Not used by 10/100Base-T |
| 6 Rx                            |
| 7 Not used by 10/100Base-T |
| 8 Not used by 10/100Base-T |

End view of RJ45 plug Looking into an RJ45 jack

<!-- image -->

<!-- image -->

When to use straight-through and cross-over cable:

- MicroLogix 1100 controller Ethernet port to 10/100 Base-T Ethernet switch cables uses a straight-through pinout (1-1, 2-2, 3-3, 6-6).
- Direct point-to-point 10/100 Base-T cables connecting the MicroLogix 1100 controller Ethernet port directly to another Ethernet port (or a computer 10/100Base-T port) require a cross-over pinout (1-3, 2-6, 3-1, 6-2).

## Notes:

## Use the LCD and Keypad

The LCD and keypad are shown in Figure 67 .

Figure 67 - Controller LCD and Keypad

<!-- image -->

| Feature Description                                               |
|-------------------------------------------------------------------|
| 1 LCD                                                             |
| 2  LCD screen keypad (ESC, OK, Up, Down, Left, and Right buttons) |

Table 17 - LCD and Keypad

<!-- image -->

## Operating Principles

Figure 68 - MicroLogix 1100 LCD Menu Structure Tree

<!-- image -->

## Startup Screen

The Startup screen displays whenever the controller is powered up.

Figure 69 - LCD Default Startup Screen

<!-- image -->

You can customize this Startup screen in your application program by defining a string data file that contains the string to display on the Startup screen and specifying the CBS element of the LCD Function File to the address of this string file.

Figure 70 shows an example of a customized Startup screen.

Table 18 - Main Menu Items

|                                                                                                     | Menu Item Description For details, see                      |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| I/O Status  Displays the I/O Status screen, which shows the I/O status of the embedded digital I/O. | I/O Status on page 76                                       |
| Monitoring Allows you to view and change the data value of a bit and an integer file.               | Monitor Bit File on page 77 Monitor Integer File on page 82 |

Figure 70 - Customized Startup Screen Example

<!-- image -->

For more information on how to create and use a customized Startup screen, see the LCD Function File described in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

After the default Startup screen or your customized Startup screen is displayed for 3 seconds, either the default screen (the I/O Status screen) is displayed by default, or a user-defined screen is displayed if your application uses a custom default screen.

## Main Menu and Default Screen

The Main menu consists of five menu items: I/O Status, Monitoring, Mode Switch, User Displ, and Advance Set.

Figure 71 - LCD Main Menu

?

<!-- image -->

Table 18 - Main Menu Items (Continued)

|                                                                                                                                                                                                                                                                                                                    | Menu Item Description For details, see                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mode Switch Allows you to change the mode switch selection.                                                                                                                                                                                                                                                        | Use the Mode Switch on page 88                                                                                                                                               |
| User Displ Displays the user-defined LCD screen                                                                                                                                                                                                                                                                    | Use a User-defined LCD Screen on page 90                                                                                                                                     |
| Advance Set Allows you to configure or view the following: • Change the key in mode for value entry for a trimpot. • Use the Communications Toggle functionality. • View the Ethernet port configuration. • Change the data value of trimpots. • View system information, such as OS series and firmware revision. | •  Change Key In Mode on page 92 •  Communications Toggle Functionality on page 94 •  Ethernet Port Configuration on page 95 •  Trimpots on page 96 •  I/O Status on page 76 |

Figure 72 - LCD Default Screen - I/O Status Screen

Figure 72 is the default screen of the display, allowing you to monitor the controller and I/O Status. For more information on the I/O Status screen, see I/O Status on page 76 .

<!-- image -->

## Operating Buttons

<!-- image -->

| Button Function                                         |
|---------------------------------------------------------|
| Move cursor                                             |
| Choose file numbers, values, and so on                  |
| OK Next menu level, store your entry, apply the changes |
| ESC Previous menu level, cancel your entry              |

## Using Menus to Choose Values

<!-- image -->

| Press To   |                                                                                                                     |
|------------|---------------------------------------------------------------------------------------------------------------------|
| OK         | • Go to the next menu level. • Store your entry. • Apply the changes.                                               |
| ESC        | • Go to the previous menu level. • Cancel your entry since the last Ok . • Press repeatedly to go to the main menu. |
|            | • Change menu item. • Change value. • Change position.                                                              |

.

## Select Between Menu Items

<!-- image -->

## Cursor Display

<!-- image -->

Flashing value is presented as an empty rectangle for explanation purpose.

<!-- image -->

There are two different cursor types:

Selection cursor (the symbol " ") is displayed left to the selected item.

- Move the cursor with the up/down arrows

Full block navigation is shown as a flashing block:

- Change position with left/right arrows
- Change values with up/down arrows

## I/O Status

## Setting Values

<!-- image -->

<!-- image -->

Left/right arrow moves the cursor between the digits of the value (+02714). Up/down arrow = Changes the value

Up arrow = Increment

Down arrow = Decrement

The MicroLogix 1100 controller provides I/O status indicators on the LCD screen. You can view the status of inputs and outputs on the I/O Status screen on the LCD, as shown in Figure 73 . The I/O status indicators on this screen are updated every 100 ms to reflect the current I/O status in real time, regardless of controller scan time.

Figure 73 - I/O Status Screen

<!-- image -->

A solid rectangle displays when the input or output is energized. An empty rectangle displays when the input or output is not energized.

## IMPORTANT

If no user-defined LCD screen is used, the I/O Status screen displays:

- 5 seconds after the controller has powered-up
- When the user enters the I/O Status screen from other screen using the LCD menu. If you are at the other screen and want to view I/O status, you have to enter the I/O Status screen manually using the menu. Otherwise, the current screen is displayed continuously.

## Monitor Bit File

## IMPORTANT

If a user-defined LCD screen is used, the I/O Status screen displays:

- When the user holds down the ESC key for more than 3 seconds
- When time out is enabled, that is, the timeout period is set to a positive value, and the timeout period is passed. You can enable and disable timeout and set the timeout period using the TO element in the LCD Function File. For more information, see the LCD Function File that is described in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .
- If time out is disabled, that is, the timeout period is set to zero, and a custom LCD screen is displayed, it is displayed continuously until the user gives an input to change to other screen. For more information, Use a User-defined LCD Screen on page 90 .

## View I/O Status

Follow these steps to view the status of inputs and outputs on the LCD.

1. On the Main Menu screen, select I/O Status by using the Up and Down keys on the LCD keypad.
2. Press OK on the LCD keypad. The I/O Status screen displays.
3. If you have finished viewing I/O status, press ESC to return to the Main Menu screen, as shown in step 1 .

<!-- image -->

<!-- image -->

The LCD allows you to view and change the data values of 48 bits in a user-defined file. You can access to this functionality via the Monitoring screen of the LCD.

To monitor the bit file on the LCD, you have to specify its file number in the Target Bit File Number (TBF) element of the LCD Function File and download your application program to the controller. The TBF element can only be changed by a program download.

## Target Bit File Number (TBF)

|                                                               | Feature Address Data Format Type   | User Program Access   |
|---------------------------------------------------------------|------------------------------------|-----------------------|
| Target Bit File Number LCD:0.TBF Word (INT) Control Read-only |                                    |                       |

Table 19 - Bit File Number 3 Example

| Bit Number Data Address Protection Bit Bit Number Data Address Protection Bit Bit Number Data Address Protection Bit   |                                                   |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 0 B3:0/0 B3:3/0 16 B3:1/0 B3:4/0 32 B3:2/0 B3:5/0                                                                      |                                                   |
|                                                                                                                        | 1 B3:0/1 B3:3/1 17 B3:1/1 B3:4/1 33 B3:2/1 B3:5/1 |
| 2 B3:0/2 B3:3/2 18 B3:1/2 B3:4/2 34 B3:2/2 B3:5/2                                                                      |                                                   |
| 3 B3:0/3 B3:3/3 19 B3:1/3 B3:4/3 35 B3:2/3 B3:5/3                                                                      |                                                   |
| 4 B3:0/4 B3:3/4 20 B3:1/4 B3:4/4 36 B3:2/4 B3:5/4                                                                      |                                                   |
| 5 B3:0/5 B3:3/5 21 B3:1/5 B3:4/5 37 B3:2/5 B3:5/5                                                                      |                                                   |
| 6 B3:0/6 B3:3/6 22 B3:1/6 B3:4/6 38 B3:2/6 B3:5/6                                                                      |                                                   |
| 7 B3:0/7 B3:3/7 23 B3:1/7 B3:4/7 39 B3:2/7 B3:5/7                                                                      |                                                   |
| 8 B3:0/8 B3:3/8 24 B3:1/8 B3:4/8 40 B3:2/8 B3:5/8                                                                      |                                                   |
| 9 B3:0/9 B3:3/9 25 B3:1/9 B3:4/9 41 B3:2/9 B3:5/9                                                                      |                                                   |
| 10 B3:0/10 B3:3/10 26 B3:1/10 B3:4/10 42 B3:2/10 B3:5/10                                                               |                                                   |
| 11 B3:0/11 B3:3/11 27 B3:1/11 B3:4/11 43 B3:2/11 B3:5/11                                                               |                                                   |
| 12 B3:0/12 B3:3/12 28 B3:1/12 B3:4/12 44 B3:2/12 B3:5/12                                                               |                                                   |
| 13 B3:0/13 B3:3/13 29 B3:1/13 B3:4/13 45 B3:2/13 B3:5/13                                                               |                                                   |
| 14 B3:0/14 B3:3/14 30 B3:1/14 B3:4/14 46 B3:2/14 B3:5/14                                                               |                                                   |
| 15 B3:0/15 B3:3/15 31 B3:1/15 B3:4/15 47 B3:2/15 B3:5/15                                                               |                                                   |

The bit number that is displayed on the LCD corresponds to the data address as illustrated in the table. The protection bit defines whether the data is editable or read-only. When the protection bit is set (1), the corresponding data address is considered read-only by the LCD. The "Protected!" message is displayed whenever a read-only element is active on the LCD. When the protection bit is clear (0) or the protection bit does not exist, no additional message is displayed and the data within the corresponding address is editable from the LCD keypad.

## IMPORTANT

Although the LCD does not allow protected data to be changed from its keypad, the control program or other communication devices do have access to this data. Protection bits only provide LCD write protection. They do not provide any overwrite protection to data from ladder logic, HMI, or programming software. It is the users' responsibility to verify that data is not inadvertently overwritten.

<!-- image -->

- Remaining addresses within the target file can be used without restrictions (addresses B3:6/0 and above, in this example).
- The LCD always starts at bit 0 of a data file. It cannot start at any other address within the file.

The value that is stored in the TBF element identifies the bit file with which the LCD interfaces. Valid bit files are B3, and B10 through B255. When the LCD reads a valid bit file number, it can access up to the first 48 bits (0...47) of the specified file on the LCD screen. The next 48 bits in the target bit file (48...95) are used to define the read-only or read/write privileges for the first 48 bits.

The only bit file that the LCD interfaces with is the file that is specified in the TBF element.

## IMPORTANT

Use your programming software to verify that the bit file you specify in the TBF element, and the appropriate number of elements, exist in the MicroLogix 1100 user program.

Table 19 shows an example of how the LCD uses the configuration information with bit file number 3 (LCD:0.TBF=3).

## Monitor a Bit File

For the explanations in this section, we assume the followings in the application program:

- A bit file B3, which is 7 elements long (7 words = 112 bits), is defined with the preset data, as shown in Figure 74 .
- The TBF element of the LCD Function File is set to 3 to specify the bit file B3 as the target bit file to monitor on the LCD, as shown in Figure 75 .
- The controller mode is set to Remote Run.

Figure 74 - File B3 Data

<!-- image -->

Figure 75 - LCD Function File

<!-- image -->

Follow these steps to view and change the data values of the bit file B3.

1. On the Main Menu screen, select Monitoring by using the Up and Down keys on the LCD keypad.
2. Press OK on the LCD keypad. The Bit/Integer File Select screen displays.
3. If Bit is selected, as shown in step 2, press OK . If not selected, press the Up or Down key to select it, and then press OK.
4. The current data value (ON) of the B3:0/0 bit is displayed. Note that "0/0" flashes, which means the cursor is at the target bit position.
5. To change the data value of the B3:0/0 bit to OFF (0): First, press OK to select the displayed address and move the cursor to the data value
6. position. Then, "ON" flashes, which means the cursor is at the data value position.
6. Press the Down key. Then, the data value is represented as "OFF". Note that "OFF" continues to flash, which means the cursor is still at the data value position.

<!-- image -->

<!-- image -->

<!-- image -->

7. Press OK to apply the changes. Then, the new value OFF (0) is applied. The target bit, "0/0" in this example, flashes. The cursor is moved automatically to the target bit position.

<!-- image -->

You can identify this change of data value is reflected to your RSLogix 500 programming software.

<!-- image -->

- When the cursor is at the data value position, press the Down key to change the data value of a bit from ON (1) to OFF (0). Press the Up key to change from OFF (0) to ON (1).

<!-- image -->

After changing the data value of a target bit, press OK to apply the changes or press ESC to discard the changes.

8. Now, we view an example of the data value of a protected bit, B3:0/2. Press the Up key twice. Then, the target bit changes to "0/2" and its data value is displayed with the "Protected!" message. Because the B3:3/2 is set (1), the B3:0/2 bit is a protected bit.
9. Try to move the cursor to the data value position by pressing OK. Because the B3:0/2 bit is a protected bit, you find that the cursor does not move to the data value position.

<!-- image -->

## Monitor Integer File

10. Press the Up key once to view the data value of the B3:0/3 bit. Because the B3:0/3 bit is not a protected bit, only its data value, OFF (0) in this example, displays without the "Protected!" message.
11. Press the Up key once to view the data value of the B3:0/4 bit. You find that the B3:0/3 bit is a protected bit and its data value is ON (1).
12. Hold down the Up key until the target bit becomes "2/15".

<!-- image -->

Press the Up key again, and you find the target bit does not change to "3/0". It is because the maximum range of bits you can monitor with the LCD is the first 48 bits (3 words) of the specified target bit file.

## IMPORTANT

The maximum range of bits you can monitor with the Bit File Monitoring functionality on the LCD is the first 48 bits (3 words).

13. Try to press the Up and Down keys to change the target bit to another bit. Try to change its data value using the OK, Up and Down keys.
14. If you have finished monitoring the bit file, B3, press ESC to return to the Bit/Integer File Select screen, as shown in step 2 .

The LCD allows you to view and change the data value of an integer file. You can access to this functionality via the Monitoring screen of the LCD.

To monitor an integer file on the LCD, you have to specify its file number in the Target Integer File Number (TIF) element of the LCD Function File and download your application program to the controller. The TIF element can only be changed by a program download.

## Target Integer File Number (TIF)

|                                                                   | Feature Address Data Format Type   | User Program Access   |
|-------------------------------------------------------------------|------------------------------------|-----------------------|
| Target Integer File Number LCD:0.TIF Word (INT) Control Read-only |                                    |                       |

The value that is stored in the TIF element identifies the integer file with which the LCD interfaces. The LCD can read or write to any valid integer file within the controller. Valid integer files are N3 through N255. When the LCD reads a valid integer file number, it can access up to the first 48 elements (words 0…47) of the specified file on the LCD screen. The next 48 bits (words 48…50) are used to define the read-only or read/write privileges for the first 48 elements.

The only integer file that the LCD interfaces with is the file that is specified in the TIF element.

## IMPORTANT

The maximum range of bits you can monitor with the Bit File Monitoring functionality on the LCD is the first 48 bits (3 words).

Table 20 shows an example of how the LCD uses the configuration information with integer file number 7 (LCD:0.TIF=7).

Table 20 - Integer File Number 7 Example

| Element Number Data Address Protection Bit Element Number Data Address Protection Bit Element Number Data Address Protection Bit   |                                                       |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| 0 N7:0 N7:48/0 16 N7:16 N7:49/0 32 N7:32 N7:50/0                                                                                   |                                                       |
| 1 N7:1 N7:48/1 17 N7:17 N7:49/1 33 N7:33 N7:50/1                                                                                   |                                                       |
| 2 N7:2 N7:48/2 18 N7:18 N7:49/2 34 N7:34 N7:50/2                                                                                   |                                                       |
| 3 N7:3 N7:48/3 19 N7:19 N7:49/3 35 N7:35 N7:50/3                                                                                   |                                                       |
| 4 N7:4 N7:48/4 20 N7:20 N7:49/4 36 N7:36 N7:50/4                                                                                   |                                                       |
| 5 N7:5 N7:48/5 21 N7:21 N7:49/5 37 N7:37 N7:50/5                                                                                   |                                                       |
| 6 N7:6 N7:48/6 22 N7:22 N7:49/6 38 N7:38 N7:50/6                                                                                   |                                                       |
| 7 N7:7 N7:48/7 23 N7:23 N7:49/7 39 N7:39 N7:50/7                                                                                   |                                                       |
| 8 N7:8 N7:48/8 24 N7:24 N7:49/8 40 N7:40 N7:50/8                                                                                   |                                                       |
| 9 N7:9 N7:48/9 25 N7:25 N7:49/9 41 N7:41 N7:50/9                                                                                   |                                                       |
| 10 N7:10 N7:48/10 26 N7:26 N7:49/10 42 N7:42 N7:50/10                                                                              |                                                       |
| 11 N7:11 N7:48/11 27 N7:27 N7:49/11 43 N7:43 N7:50/11                                                                              |                                                       |
| 12 N7:12 N7:48/12 28 N7:28 N7:49/12 44 N7:44 N7:50/12                                                                              |                                                       |
|                                                                                                                                    | 13 N7:13 N7:48/13 29 N7:29 N7:49/13 45 N7:45 N7:50/13 |
|                                                                                                                                    | 14 N7:14 N7:48/14 30 N7:30 N7:49/14 46 N7:46 N7:50/14 |
| 15 N7:15 N7:48/15 31 N7:31 N7:49/15 47 N7:47 N7:50/15                                                                              |                                                       |

The element number that is displayed on the LCD corresponds to the data address as illustrated in the table. The protection bit defines whether the data is editable or read-only. When the protection bit is set (1), the corresponding data address is considered read-only by the LCD. The "Protected!" message is displayed whenever a read-only element is active on the LCD. When the protection bit is clear (0) or the protection bit does not exist, no additional message is displayed and the data within the corresponding address is editable from the LCD keypad.

## IMPORTANT

Although you cannot change protected data from the LCD keypad, the control program or other communication devices have access to protected data. Protection bits do not provide any overwrite protection to data within the target integer file. It is entirely the user's responsibility to verify that data is not inadvertently overwritten.

<!-- image -->

- Remaining addresses within the target file can be used without restrictions (addresses N7:51 and above, in this example).
- The LCD always starts at word 0 of a data file. It cannot start at any other address within the file.

## Monitor an Integer File

For the explanations in this section, we assume the following in the application program:

- An integer file N7, which is 53 elements long (53 words), is defined with the preset data, as shown in Figure 76 .

<!-- image -->

- The TIF element of the LCD Function File is set to 7 to specify the integer file N7 as the target integer file to monitor on the LCD, as shown in Figure 77 .
- The controller mode is set to Remote Run.

Figure 77 - LCD Function File

<!-- image -->

Follow these steps to view and change the data values of the integer file N7.

1. On the Main Menu screen, select Monitoring by using the Up and Down keys on the LCD keypad.
2. Press OK on the LCD keypad. The Bit/Integer File Select screen displays.
3. If Integer is selected, as shown in step 2, press OK. If not selected, press the Down key to select it, then press OK.
4. The current data value (ON) of the N7:0 word displays. The target word "0", which is right to "N7:", flashes, which means the cursor is at the target word position.
5. We change the data value of the N7:0 word to the negative decimal value -1300. First, press OK to move the cursor to the data value position. Then, the last digit of "+00000" flashes, which means the cursor is at the data value position.

<!-- image -->

<!-- image -->

<!-- image -->

6. Press the Left key twice. Then, the cursor positions at the third digit. Press the Up key three times to change the third digit to 3.
7. Press the Left key once. Then, press the Up key once. The second digit changes to "1". Note that "1" still flashes, which means the cursor is still at the data value position.
8. Press the Left key once. Then, press the Down key once. The sign digit changes to "-". Note that "-" is still flashing, which means the cursor is still at the data value position.
9. Press OK to apply the changes. Then, the new value -1300 is applied. The target word "0", which is right to "N7:", flashes. The cursor is moved automatically to the target word position.

<!-- image -->

<!-- image -->

<!-- image -->

You can identify that this change of data value is reflected to your RSLogix 500 programming software.

<!-- image -->

<!-- image -->

After changing the data value of a target word, press OK to apply the changes or press ESC to discard the changes.

10. Now, we view the data value of a protected word N7:1. Press the Up key once. Then, the target word changes to "1" and its data value displays with the "Protected!" message. Because the N7:48/1 bit is set (1), the N7:1 word is a protected word.
11. Try to move the cursor to the data value position by pressing OK. Because the N7:1 word is protected, you find that the cursor does not move to the data value position.
12. Press the Up key once to view the data value of the N7:2 word. Because the N7:2 word is not protected, only its data value, 0 in this example, is displayed without the "Protected!" message.
13. Hold down the Up key until the target word becomes "47".

<!-- image -->

<!-- image -->

Press the Up key again, and you find the target word does not change to "48". It is because the maximum range of words you can monitor with the LCD is the first 48 words of the specified target integer file.

## Use the Mode Switch

| IMPORTANT   | The maximum range of words you can monitor with the Integer File Monitoring functionality on the LCD is the first 48 words (0...47) of the target integer file.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

14. Try to press the Up and Down keys to change the target word to another word. Try to change its data value using the OK, Up, Down, Right and Left keys.
15. If you have finished monitoring the integer file N7, press ESC to return to the Main Menu screen, as shown in step 2 .

The MicroLogix 1100 controller provides the controller mode switch on the LCD. The possible positions of the mode switch are PROGRAM, REMOTE, and RUN. You can change mode switch position using the Mode Switch screen on the LCD. In this example, the mode switch position is set to REMOTE.

<!-- image -->

All built-in LCD screens except the Boot Message screen display the current mode switch position, at their top-right portion. In this example, the mode switch position is set to RUN.

<!-- image -->

## Controller Modes

Table 21 shows the possible controller modes when the mode switch positions at PROGRAM, REMOTE, or RUN. For example, if the Mode Switch is at RUN and you want to test a control program with running it for one scan, you have to first change the mode switch position to REMOTE before you run the control program in the Remote Test single scan mode with your RSLogix 500 programming software.

Table 21 - Possible Controller Modes by Mode Switch Position

| When the Mode Switch Positions at Possible Controller Modes are   |                                                                     |
|-------------------------------------------------------------------|---------------------------------------------------------------------|
| PROGRAM                                                           | Download in progress                                                |
| PROGRAM                                                           | Program mode                                                        |
| PROGRAM                                                           | Suspend mode – Operation halted by execution of the SUS instruction |

Table 21 - Possible Controller Modes by Mode Switch Position (Continued)

| When the Mode Switch Positions at Possible Controller Modes are                   |
|-----------------------------------------------------------------------------------|
| Remote download in progress                                                       |
| Remote program mode                                                               |
| REMOTE Remote suspend mode – Operation halted by execution of the SUS instruction |
| Remote Run mode                                                                   |
| Remote Test continuous mode                                                       |
| Remote Test single scan mode                                                      |
| RUN Run mode                                                                      |

## Change Mode Switch Position

Mode Switch position can be changed at two different times using the LCD keypad. One is when the controller is powered up, and the other is while the controller is powered on.

Mode Switch position can be set to either PROG or RUN when the controller is powered up. This allows the controller operation, which differs from the previous mode, that is, any program under RUN before can be stopped or any new program can be run when the controller is powered up.

To forcibly set Mode Switch to RUN when the controller is powered up:

- Press OK for 5 seconds when the controller is powered up. The following LCD screen appears if it's successfully done.

<!-- image -->

To forcibly set Mode Switch to PROG when the controller is powered up:

- Press ESC for 5 seconds when the controller is powered up. The following LCD screen appears if it's successfully done.

<!-- image -->

Note that I/O output status may be changed for some programs.

## Use a User-defined LCD Screen

While the controller is powered on, follow these steps to change the position of the Mode Switch.

1. On the Main Menu screen, select Mode Switch by using the Up and Down keys on the LCD keypad.
2. Press OK on the LCD keypad. The Mode Switch screen displays.

<!-- image -->

<!-- image -->

The arrow indicates the current Mode Switch position.

3. When the Up or Down key is pressed, the mode indicated by the arrow blinks if the mode is different from the current mode of the controller. Press OK to set the controller to the mode indicated by the arrow.
4. If you have finished changing the mode switch position, press ESC to return to the Main Menu screen, as shown in step 1 .

The MicroLogix 1100 controller allows you to use user-defined LCD screens instead of the default built-in screens.

To use a user-defined screen, you must create a group of appropriate instructions using the LCD instruction in your application program. For more information on how to create a userdefined LCD screen, see the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

By using the User Displ menu item, you can change from the default built-in screens to a userdefined screen and back on the LCD.

## User-defined LCD Screen

Follow these steps to display the user-defined screen implemented in your application program.

1. On the Main Menu screen, select User Displ by using the Up and Down keys on the LCD keypad. If the menu items are not displayed on the Main Menu screen, scroll down the screen by pressing the Down key.
2. Press OK on the LCD keypad.

<!-- image -->

If no user-defined screen is used in your application program, the following screen displays.

The U-MSG indicator on the top of the LCD displays as a solid rectangle. It means that the LCD is in User-defined LCD mode.

<!-- image -->

If a user-defined screen is used in your application program, the LCD screen displays, according to the specific instructions used in your program.

COMM0COMM1

DCO

DCOMM
BAT. L

O
U-MSG

<!-- image -->

T
LO

T.

## Configure Advanced Settings

## Change Key In Mode

3. Press ESC longer than 3 seconds to return to the Main Menu screen.

<!-- image -->

With the Advanced Settings menu, which is a submenu under the main menu of the LCD, you can use the following features:

- Change Key In mode
- Use Communications Toggle functionality
- View Ethernet port configuration
- Use trimpots
- View system information
- View fault code

You can access to the Advanced Settings Menu screen by selecting Advance Set on the Main Menu screen.

<!-- image -->

## Key In Modes

There are two Key In modes, Continuous and Discrete.

<!-- image -->

The Key In mode has effect only when you change the data value of a trimpot on a trimpot screen, either Trimpot 0 or Trimpot 1 screen. For more information on how to change the data value of a trimpot, see Changing Data Value of a Trimpot on page 97 .

The current Key In mode determines how the value changes are applied when you press the Up and Down keys to change the data value for a trimpot. When set to Continuous, the changes apply immediately when you press the Up and Down keys. When set to Discrete, the changes apply only when you press OK after you have changed the value using the Up and Down keys.

By using the Key In Mode screen, as shown in Figure 78, you can change the Key In mode to use.

Figure 78 - Key In Mode Screen

<!-- image -->

## Change Key In Mode

To change the current Key In mode, perform the following:.

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items are not displayed on the Main Menu screen, you must scroll down the screen by pressing the Down key.
2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.
3. Select KeyIn Mode using the Up and Down keys, then press OK.

<!-- image -->

<!-- image -->

## Communications Toggle Functionality

4. The Key In Mode screen displays. The current mode, Continuous in this example, is selected marked up with the symbol " ".
5. Press the Up or Down key to select the different mode, Discrete in this example. Then, press OK.
6. The Key In Mode Change Notification screen displays.
7. Press ESC to return to the Advanced Settings Menu screen, as shown in step 2 .

<!-- image -->

<!-- image -->

<!-- image -->

The MicroLogix 1100 controller provides the Communications Toggle functionality, which allows you to switch between the user-defined communication configuration and the default communications mode on Channel 0. See Use the Communications Toggle Functionality on page 52 for information on this feature.

## Ethernet Port Configuration

The Ethernet Port Configuration screen of the LCD displays the MAC and IP addresses assigned to the controller.

Follow these steps to view the Ethernet port configuration for your controller.

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items are not displayed on the Main Menu screen, scroll down the screen by pressing the Down key.
2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.
3. If ENET Cfg is selected, press OK. If not, select ENET Cfg using the Up and Down keys, then press OK.
4. The Ethernet Port Configuration screen displays.

<!-- image -->

<!-- image -->

When an IP address is not yet assigned to your controller, only the MAC address that is assigned to your controller, which is represented as XXXXXXXXXXXX, displays.

<!-- image -->

A MAC address is a 12-digit hexadecimal number. Your controller ships with a unique MAC address assigned in the factory. You can identify the MAC address of your controller by opening the expansion module cover on your controller.

## Trimpots

When an IP address is assigned to your controller, both of MAC address and IP address of your controller are displayed. In this example, the MAC address is represented as XXXXXXXXXXXX, which is a 12-digit hexadecimal number. The IP address is represented as xxx.xxx.xxx.xxx, where each xxx is a decimal number between 0…255.

5. Press ESC to return to the Advanced Settings Menu screen, as shown in step 2 .

<!-- image -->

## Trimpot Operation

The MicroLogix 1100 controller provides two trimming potentiometers (trimpots, POT0 and POT1), which allow modification of integer data within the controller. The data value of each trimpot can be used throughout the control program for timers, counters, analog presets, and so on, depending upon the requirements of the application.

You can change the data value of each trimpot using the trimpot screens that are provided by the LCD. To access the Trimpot Set screen, which is the top screen for the trimpot functionality, select TrimPot Set on the LCD default menu screen, and press OK on the LCD keypad.

<!-- image -->

Trimpot data is updated continuously whenever the controller is powered-up.

## Changing Data Value of a Trimpot

Follow these steps to change the data value of a trimpot, either POT0 or POT1.

1. On the Main Menu screen, select TrimPot Set by using the Up and Down keys on the LCD keypad.
2. Press OK on the LCD keypad. The TrimPot Select screen displays.

<!-- image -->

<!-- image -->

The last trim pot whose data value you changed is selected by default. If you are accessing to this screen for the first time, POT0 is selected by default.

3. Select a trimpot, either POT0 or POT1, whose data value you want to change using the Up and Down keys on the LCD keypad. In this example, we select POT0.
4. Press OK on the LCD keypad. The Trimpot 0 screen displays.

<!-- image -->

TMIN and TMAX indicate the range of data values for the trimpots, both POT0 and POT1. The factory default for TMIN, TMAX, and POT0 values are 0, 250, and 0 in decimal, respectively. TMIN and TMAX on this screen are read-only, but you can change them using the LCD Function File in your application program. The TMIN and TMAX elements can only be changed by a program download.

For more information on how to change trimpot configurations including TMIN and TMAX, see the LCD Function File described in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

IMPORTANT

The same TMIN and TMAX values are used for both trimpots, POT0 and POT1. This behavior is intended by design for simplicity in the trimpot configuration.

## View System Information

When you enter this screen, the last digit of the POT0 value flashes. It indicates the current digit. Press the Up and Down keys on the LCD keypad to change the value of the current digit. Press the Left and Right keys to select another digit as the current digit.

If the Key In mode is set to Continuous, the changes are applied immediately after you press the Up and Down keys. While if it is set to Discrete, you have to press OK to apply the changes after you change the data value. For more information on how to set the Key In mode, see Change Key In Mode on page 92 .

<!-- image -->

The Key In mode has an effect only when you change the data value of a trimpot on a trimpot screen, either the Trimpot 0 or Trimpot 1 screen.

5. If you have finished changing the data value of the selected trimpot, POT0 in this example, press ESC to return to the TrimPot Select screen, as shown in step 2 .

## Trimpot Configuration in LCD Function File

The configuration for trimpots in the LCD Function File, including trimpot low and high values for data value range, is described in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

## Error Conditions

Error conditions regarding the trimpot functionality are described in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

The System Information screen of the LCD allows you to identify the system information for your controller.

Follow these steps to view the system information for your controller.

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items are not displayed on the Main Menu screen, scroll down the screen by pressing the Down key.
2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.
3. If System Info is selected, press OK. If not, select System Info using the Up and Down keys, then press OK.

<!-- image -->

<!-- image -->

## View Fault Code

4. The System Information screen displays.

You can identify the catalog number, operating system firmware revision number, and boot firmware revision number of your controller.

<!-- image -->

5. Press ESC to return to the Advanced Settings Menu screen, as shown in step 2 .

The Fault Code screen of the LCD displays the fault code when a fault occurs.

When a fault occurs, the Fault Code screen does not display automatically. Only the FAULT LED on the controller flashes in red light. Therefore, you must navigate into the Fault Code screen to identify the fault code on the LCD.

Follow these steps to view the fault code when a fault occurs.

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items are not displayed on the Main Menu screen, scroll down the screen by pressing the Down key.
2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.
3. If Fault Code is selected, press OK. If not, select Fault Code using the Up and Down keys, then press OK.
4. The Fault Code screen displays.

<!-- image -->

<!-- image -->

If no fault occurred, "0000h" displays.

<!-- image -->

If a fault occurred, its fault code displays.

<!-- image -->

<!-- image -->

For more information on a specific fault code, see the Online Help of your RSLogix 500 programming software.

5. Press ESC to return to the Advanced Settings Menu screen, as shown in step 2 .

## Real-time Clock Operation

<!-- image -->

## Use Real-time Clock and Memory Modules

The MicroLogix 1100 controller has a built-in real-time clock (RTC). You can order a memory module as an accessory.

<!-- image -->

For more information on real-time clock function file and memory module information file, see the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

One type of memory module is available for use with the MicroLogix 1100 controller.

| Catalog Number Function Memory Size   |
|---------------------------------------|
| 1763-MM1 Memory Module 128 KB         |

## Operation at Power-up and Entering a Run or Test Mode

At power-up and when the controller enters a run or test mode, the values (date, time, and status) of the RTC are written to the RTC Function File in the controller.

Table 22 indicates the accuracy of the RTC for various temperatures.

Table 22 - RTC Accuracy

| Ambient Temperature  Accuracy(1)        |
|-----------------------------------------|
| 0 °C (32 °F) -13...-121 seconds/month   |
| 25 °C (77 °F) +54...-5 seconds/month    |
| 40 °C (104 °F) +29...-78 seconds/month  |
| 55 °C (131 °F) -43...-150 seconds/month |

## Write Data to the Real-time Clock

When valid data is sent to the real-time clock from the programming device or another controller, the new values take effect immediately.

The real-time clock does not allow you to load or store invalid date or time data.

## RTC Battery Operation

The real-time clock uses the same replaceable battery that the controller uses. The RTC Function File features a battery low indicator bit (RTC:0/BL), which shows the status of the replacement battery. When the battery is low, the indicator bit is set (1). This means that the battery wire connector could be disconnected or if the battery is connected, the battery may be ready to fail in the next two weeks. In the latter case, the replacement battery must be replaced with a new one. When the battery low indicator bit is clear (0), the battery level is acceptable.

The Battery Low (BAT.LO) indicator on the LCD display of the controller also shows the status of the replaceable battery. When the battery is low, the indicator displays as a solid rectangle ( ). When the battery level is acceptable, the indicator displays as an empty rectangle ( ), as shown in Figure 79 .

## Memory Module Operation

Figure 79 - LCD Battery Level Indicator

<!-- image -->

If the RTC battery is low and the controller is powered, the RTC operates normally. If the controller power is removed and the RTC battery is low, RTC data is lost.

<!-- image -->

ATTENTION: Operating with a low battery indication for more than 14 days (8 hours without a battery) may result in invalid RTC data unless power is on continuously.

The memory module supports the following features:

- User Program, User Data, and Recipe Back-up
- User Program Compare
- Data File Download Protection
- Memory Module Write Protection
- Removal/Insertion Under Power
- Memory Module Information File
- Program/Data Download
- Program/Data Upload

<!-- image -->

ATTENTION: Electrostatic discharge can damage the memory module. Do not touch the connector pins or other sensitive areas.

## User Program, User Data, and Recipe Back-up

The memory module provides a simple and flexible program, data and recipe transport mechanism, allowing the user to transfer the program, data, and recipe to the controller without the use of a personal computer and programming software.

The memory module can store one user program at a time.

During program transfers to or from the memory module, the controller's RUN LED flashes.

## Program Compare

The memory module can also provide application security, allowing you to specify that if the program stored in the memory module does not match the program in the controller, the controller will not enter an executing (run or test) mode. To enable this feature, set the S:2/9 bit in the system status file. See "Status System File" in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 for more information.

## Data File Download Protection

The memory module supports data file download protection. This allows user data to be saved (not overwritten) during a download.

<!-- image -->

Data file download protection is only functional if the processor does not have a fault, the size of all protected data files in the memory module exactly match the size of protected data files within the controller, and all protected data files are of the same type. See "Protecting Data Files During Download" in the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

## Memory Module Write Protection

The memory module supports write-once, read-many behavior. Write protection is enabled using your programming software.

IMPORTANT

Once set, write protection cannot be removed. A change cannot be made to the control program stored in a write-protected memory module. If a change is required, use another memory module.

## Removal/Insertion Under Power

The memory module can be installed or removed at any time without risk of damage to either the memory module or the controller, except during a data transaction. If the memory module is removed during a data transaction, data corruption can occur.

If a memory module is installed while the MicroLogix 1100 controller is executing, the memory module is not recognized until either a power cycle occurs, or until the controller is placed in a non-executing mode (program mode, suspend mode, or fault condition).

## Memory Module Information File

The controller has a Memory Module Information (MMI) File, which provides status from the attached memory module. At power-up or on detection of a memory module being inserted, the catalog number, series, revision, and type are identified and written to the MMI file. If a memory module is not attached, zeros are written to the MMI file. See the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001, for more information.

## Program/Data Download

To download the program and data from a memory module to the controller's memory, on the "Comms" menu in your RSLogix 500 programming software, point "EEPROM" and then select "Load from EEPROM".

<!-- image -->

For more information on program/data download, see your RSLogix 500 programming software documentation.

## Program/Data Upload

To upload the program and data from the controller's memory to a memory module, on the "Comms" menu in your RSLogix 500 programming software, point "EEPROM" and then select "Store to EEPROM".

<!-- image -->

For more information on program/data upload, see your RSLogix 500 programming software documentation.

## Notes:

## Overview of Online Editing

## Online Editing

Online editing of ladder programs is available when using MicroLogix 1100 controller. Use this function to make changes to a pre-existing ladder program. Online editing functions consist of inserting, replacing, and deleting rungs in an existing ladder program while online with the processor.

Only one programming device can perform an online edit of a user program at a time. When an online editing session begins, an access from other programming devices are rejected by the MicroLogix 1100 controller.

<!-- image -->

ATTENTION: Before initiating an online editing session, we recommend that you fully understand the possible results of the edit to the system under control. Failure to properly edit a running program could result in unexpected controller operation. Physical injury or equipment damage may result. While three instructions, MSG, PTO, and PWM, are supported by program mode online edit, they are not supported by RUNTIME (RUN mode) online edit. See the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 for additional details.

Table 23 summarizes the differences between offline and online editing.

Table 23 - Differences Between Offline and Online Editing

| Offline Online                                                |                                                                      |
|---------------------------------------------------------------|----------------------------------------------------------------------|
| No restrictions exist. Full editing capabilities are allowed. | Data table file resizing is not permitted.                           |
| No restrictions exist. Full editing capabilities are allowed. | Program file creation and deletion are not permitted.                |
| No restrictions exist. Full editing capabilities are allowed. | Alteration of file protection is not permitted.                      |
| No restrictions exist. Full editing capabilities are allowed. | Alteration of static and constant data file values is not permitted. |
| No restrictions exist. Full editing capabilities are allowed. | Indexing across file boundary selections is not permitted.           |
| No restrictions exist. Full editing capabilities are allowed. | Force protection selection is not permitted.                         |
| No restrictions exist. Full editing capabilities are allowed. | I/O configuration is not permitted.                                  |

## IMPORTANT

It is important to keep in mind that some ladder instructions, when programmed online, cause data table values to change. These instructions are those that require timer, counter, and control addresses to be specified. This is discussed later in the chapter.

## Online Editing Terms

The following terms are used throughout this chapter.

- Assemble edits — Deletes any rungs marked with Delete or Replace edit zone markers during an online editing session. Inserted or modified rungs remain. All edit zone markers are removed when this function is complete.
- Cancel edits — Deletes any inserted or modified rungs added during an online editing session. Rungs marked with Delete and Replace edit zone markers remain. All edit zone markers are removed when this function is complete.
- Test edits — Allows you to verify that the changes you entered are not going to cause improper machine operation before you make the changes a permanent part of your ladder program.
- Untest edits — Allows you to disable testing

<!-- image -->

- Edit zone markers — Appear on the power rail of the ladder program display. They indicate the type of edit taking place on the rung.
- Accept rung — Incorporates the edits of a rung into the ladder program
- Online edit session — Begins when a user tries to edit rungs while online. Any other programming device that was monitoring the user program is removed from the program monitor display.
- Modify rung — When an existing rung is modified two edit zones are created. The original rung is indicated by replace zone markers on the power rail. A copy of the original rung is made so you can insert, delete, or modify instructions. This rung is indicated by insert zone markers on the power rail. Thus, an IR pair is created when you modify a rung.
- Runtime online editing — The user program is executing when an edit takes place. Any rungs that are inserted, modified, or deleted remain in the ladder program and are indicated by edit zone markers on the power rail. Edit zone markers remain after an action is completed.
- Program online editing — The user program is not executing when an edit session begins. Any action that inserts, deletes, or modifies a rung takes place immediately.

Figure 80 shows the process that is involved when performing a runtime online edit.

Figure 80 - Online Edit Runtime Process

<!-- image -->

## Effects of Online Editing On Your System

The following section covers the effects of online editing on your system. Keep these items in mind while using the online editing function.

## System Impacts

The scan time and interrupt latency can be extended when accepting a rung, assembling, or canceling edits.

Memory limitations – Online edit can be performed until there is insufficient program memory available in the processor. Note that, before assemble edits, all edited rungs are in the processor memory consuming memory, although they are not executed.

## Data Table File Size

Online editing cannot change the size of existing data tables nor can new ones be created. However, some ladder instructions, when programmed cause data table values to change. These instructions are those that require timer, counter, and control addresses to be specified.

## Directions and Cautions for MicroLogix 1100 Online Edit User

## Online Edit Error

If either electrical interference, communication loss, or a power cycle occur during an online edit session, program integrity may be impacted. In this case, the controller generates the 1F fault code, clears the user program, and loads the default program.

## Change the RSLinx "Configure CIP Option" (OS Series A FRN 1, 2, and 3 only)

Change the RSLinx "Configure CIP Option" to prevent ownership fault when a MicroLogix 1100 controller is connected using the RSLinx® Classic EtherNet/IP driver.

Several RSLogix 500 Online operations require obtaining the processor Edit Resource/ Processor Ownership to confirm that one programming terminal has exclusive capability of performing any of these operations at a time. These operations include downloading, online editing, and applying channel configuration changes.

In addition to reducing the number of RSLinx Messaging Connections per PLC to one, it is also recommended that the Messaging Connection Retry Interval be increased from the default of 1.25 seconds to 8 seconds as shown in Figure 81 .

Figure 81 - Increase Message Connection Retry Interval

<!-- image -->

## A Download is Required Before Starting Online Editing

At least one download is required before starting online editing.

If you are using a MicroLogix 1100 controller from the out-of-box state or after clearing the processor memory or a firmware update, at least one download is required before starting online edits. If not, an error occurs and the programming software goes offline due to default image mismatch between the RSLogix 500 programming software and the MicroLogix 1100 controller. You can also see the fault code 1Fh, which is a user-defined fault code.

## Types of Online Editing

To help prevent this error, you must download the program to the MicroLogix 1100 controller, although the program is empty.

This problem happens only in the out-of-box state or after clearing processor memory.

<!-- image -->

ATTENTION: PTO and PWM instructions may not be deleted during runtime online edit. This is because if the PTO or PWM instructions were deleted during runtime online edit, outputs could stop in an unpredictable state, causing unexpected equipment operation.

If you attempt to insert or modify a rung with MSG, PTO, and PWM instruction, the following error message is generated by the programming software "Error: Online editing of PTO, PWM, and MSG are not allowed on ML1100 RUN mode." And, the rung with MSG, PTO, and PWM instruction is not accepted.

<!-- image -->

In online edit during PROGRAM mode (program online edit), there are no restrictions. For example, a user can insert an MSG instruction if a related MG file or MG/RI file is already defined in the data file.

<!-- image -->

ATTENTION: When editing a rung that contains an MCR instruction, both the MCR start and MCR end rungs must be edited (whether it be test/assemble/ cancel) simultaneously. We recommend that you fully understand the possible results of the edit to the system under control. Failure to properly edit a running program could result in unexpected controller operation. Physical injury or equipment damage may result.

<!-- image -->

ATTENTION: If you use EII or STI interrupts and your application requires a quick interrupt latency, the online edit feature is not recommended. The online editing feature may increase the interrupt latency response time. To achieve minimum interrupt latency, place the mode switch in the LCD screen in the RUN mode. This prevents the use of the online editing feature.

The type of online editing is dependent on the MicroLogix 1100 controller's mode switch position in the LCD display and the processor's mode. There are two types of online editing:

- Program Online Editing — When the controller is in either PROG mode or REM Program mode
- Runtime Online Editing — When the controller is in either REM Test or REM Run mode

Table 24 summarizes the MicroLogix 1100 controller mode switch positions in the LCD and modes that enable online editing.

<!-- image -->

Table 24 - Mode Switch Positions

| Mode Switch Position MicroLogix 1100 Controller Mode Editing Mode   |
|---------------------------------------------------------------------|
| RUN Run Not Available                                               |
| PROGram Program Program Online Editing                              |
| REMote Remote Program Program Online Editing                        |
| REMote Remote Test Program Online Editing                           |
| REMote Remote Run Program Online Editing                            |

## IMPORTANT

Online editing is not available when the mode switch in the LCD screen is in the RUN position.

<!-- image -->

ATTENTION: Use the online editing function while in RUN mode to make minor changes to the ladder program. We recommend developing your program offline since ladder rung logic changes take effect immediately after testing your edits. Improper machine operation may occur, causing personnel injury or equipment damage.

## Edit Functions in Runtime Online Editing

During a runtime online editing session, the processor is executing ladder logic. The edit zone markers tell the processor that changes exist, but the changes are not executed until you test the edits.

Deleted and replaced (modified) rungs are not removed from the program and inserted rungs are not executed until you assemble the edits.

## Edit Functions in Program Online Editing

During a program online editing session, the processor is not executing ladder logic. This mode is like the offline editing mode. If a runtime online editing session was performed before entering the offline editing mode, edit marked rungs (I, IR, and D) appear in the program.

If you perform a program online edit, once you accept or delete the rung, the edits take effect immediately and the power rail is displayed as a solid line. If you edit a rung with edit zone markers, the markers are removed when the rung is accepted.

## Notes:

## MicroLogix 1100 Controller Specifications

## General Specifications

|                                                 |                                                                                                                | Description 1763-L16AWA 1763-L16BWA 1763-L16BBB 1763-L16DWD                                                    |                                                                                                                |                                                                                                                |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Dimensions, HxWxD                               | 90 x 110 x 87 mm 3.5 x 4.33 x 3.43 in. Height is 104 mm (4.09 in.) with DIN latch open                         | 90 x 110 x 87 mm 3.5 x 4.33 x 3.43 in. Height is 104 mm (4.09 in.) with DIN latch open                         | 90 x 110 x 87 mm 3.5 x 4.33 x 3.43 in. Height is 104 mm (4.09 in.) with DIN latch open                         | 90 x 110 x 87 mm 3.5 x 4.33 x 3.43 in. Height is 104 mm (4.09 in.) with DIN latch open                         |
| Shipping weight 0.9 kg (2.0 lbs)                |                                                                                                                |                                                                                                                |                                                                                                                |                                                                                                                |
|                                                 | Number of I/O 12 inputs (10 digital and 2 analog) and 6 outputs                                                | Number of I/O 12 inputs (10 digital and 2 analog) and 6 outputs                                                | Number of I/O 12 inputs (10 digital and 2 analog) and 6 outputs                                                | Number of I/O 12 inputs (10 digital and 2 analog) and 6 outputs                                                |
| Power supply voltage                            | 100…240V AC (-15%, +10%) @ 47…63 Hz                                                                            | 100…240V AC (-15%, +10%) @ 47…63 Hz                                                                            | 24V DC (-15%, +10%) Class 2 SELV                                                                               | 12…24V DC (-15%, +10%) Class 2 SELV                                                                            |
|                                                 | Heat dissipation See System Loading and Heat Dissipation on page 165                                           | Heat dissipation See System Loading and Heat Dissipation on page 165                                           | Heat dissipation See System Loading and Heat Dissipation on page 165                                           | Heat dissipation See System Loading and Heat Dissipation on page 165                                           |
| Power supply inrush current, max                | 120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                                                                  | 120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                                                                  | 24V DC: 15 A for 20 ms                                                                                         |                                                                                                                |
| Maximum power consumption 46VA 52VA             |                                                                                                                |                                                                                                                | 35 W See Figure 82                                                                                             |                                                                                                                |
| 24V DC sensor power None                        |                                                                                                                | 250 mA @ 24V DC AC Ripple < 500 mV peak-to-peak 400 µF max                                                     | None                                                                                                           |                                                                                                                |
| Input circuit type                              | Digital: 120V AC                                                                                               | Digital: 24V DC sinking/sourcing (standard and high-speed)                                                     | Digital: 24V DC sinking/sourcing (standard and high-speed)                                                     |                                                                                                                |
| Input circuit type                              | Analog: 0…10V DC                                                                                               | Analog: 0…10V DC                                                                                               | Analog: 0…10V DC                                                                                               |                                                                                                                |
| Output circuit type Relay Relay Relay/FET Relay |                                                                                                                |                                                                                                                |                                                                                                                |                                                                                                                |
| Pilot duty rating                               | Ordinary location – B300, R150 Hazardous location – C300, R150                                                 | Ordinary location – B300, R150 Hazardous location – C300, R150                                                 | Ordinary location – B300, R150 Hazardous location – C300, R150                                                 | Ordinary location – B300, R150 Hazardous location – C300, R150                                                 |
|                                                 | Temperature, operating -20…+65 °C (-4…+149 °F) ambient                                                         | Temperature, operating -20…+65 °C (-4…+149 °F) ambient                                                         | Temperature, operating -20…+65 °C (-4…+149 °F) ambient                                                         | Temperature, operating -20…+65 °C (-4…+149 °F) ambient                                                         |
|                                                 | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                          | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                          | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                          | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                          |
|                                                 | Relative humidity 5%…95% noncondensing                                                                         | Relative humidity 5%…95% noncondensing                                                                         | Relative humidity 5%…95% noncondensing                                                                         | Relative humidity 5%…95% noncondensing                                                                         |
| Vibration                                       | Operating: 10…500 Hz, 5 g, 0.015 in. max peak-to-peak, 2 hours each axis Relay Operation: 1.5 g                | Operating: 10…500 Hz, 5 g, 0.015 in. max peak-to-peak, 2 hours each axis Relay Operation: 1.5 g                | Operating: 10…500 Hz, 5 g, 0.015 in. max peak-to-peak, 2 hours each axis Relay Operation: 1.5 g                | Operating: 10…500 Hz, 5 g, 0.015 in. max peak-to-peak, 2 hours each axis Relay Operation: 1.5 g                |
| Shock, operating                                | 30 g; 3 pulses each direction, each axis Relay Operation: 10 g                                                 | 30 g; 3 pulses each direction, each axis Relay Operation: 10 g                                                 | 30 g; 3 pulses each direction, each axis Relay Operation: 10 g                                                 | 30 g; 3 pulses each direction, each axis Relay Operation: 10 g                                                 |
|                                                 | Shock, nonoperating 50 g panel mounted (40 g DIN Rail mounted); 3 pulses each direction, each axis             | Shock, nonoperating 50 g panel mounted (40 g DIN Rail mounted); 3 pulses each direction, each axis             | Shock, nonoperating 50 g panel mounted (40 g DIN Rail mounted); 3 pulses each direction, each axis             | Shock, nonoperating 50 g panel mounted (40 g DIN Rail mounted); 3 pulses each direction, each axis             |
|                                                 | Terminal screw torque 0.56 N•m (5.0 lb•in) rated                                                               | Terminal screw torque 0.56 N•m (5.0 lb•in) rated                                                               | Terminal screw torque 0.56 N•m (5.0 lb•in) rated                                                               | Terminal screw torque 0.56 N•m (5.0 lb•in) rated                                                               |
| Agency certification                            | UL Listed Industrial Control Equipment for use in Class 1 Division 2, Hazardous Locations, Groups A, B, C, D   | UL Listed Industrial Control Equipment for use in Class 1 Division 2, Hazardous Locations, Groups A, B, C, D   | UL Listed Industrial Control Equipment for use in Class 1 Division 2, Hazardous Locations, Groups A, B, C, D   | UL Listed Industrial Control Equipment for use in Class 1 Division 2, Hazardous Locations, Groups A, B, C, D   |
| Agency certification                            | cUL Listed Industrial Control Equipment for use in Canada                                                      | cUL Listed Industrial Control Equipment for use in Canada                                                      | cUL Listed Industrial Control Equipment for use in Canada                                                      | cUL Listed Industrial Control Equipment for use in Canada                                                      |
| Agency certification                            | CE marked for all applicable directives                                                                        | CE marked for all applicable directives                                                                        | CE marked for all applicable directives                                                                        | CE marked for all applicable directives                                                                        |
| Agency certification                            | RCM marked for all applicable acts                                                                             | RCM marked for all applicable acts                                                                             | RCM marked for all applicable acts                                                                             | RCM marked for all applicable acts                                                                             |
| ESD immunity                                    | EN 61000-4-2 4 kV contact, 8 kV air, 4 kV indirect                                                             | EN 61000-4-2 4 kV contact, 8 kV air, 4 kV indirect                                                             | EN 61000-4-2 4 kV contact, 8 kV air, 4 kV indirect                                                             | EN 61000-4-2 4 kV contact, 8 kV air, 4 kV indirect                                                             |
| Radiated RF immunity                            | EN 61000-4-3 10V/m, 26…1000 MHz (alternatively, 80…1000 MHz), 80% amplitude modulation, +900 MHz keyed carrier | EN 61000-4-3 10V/m, 26…1000 MHz (alternatively, 80…1000 MHz), 80% amplitude modulation, +900 MHz keyed carrier | EN 61000-4-3 10V/m, 26…1000 MHz (alternatively, 80…1000 MHz), 80% amplitude modulation, +900 MHz keyed carrier | EN 61000-4-3 10V/m, 26…1000 MHz (alternatively, 80…1000 MHz), 80% amplitude modulation, +900 MHz keyed carrier |
| Fast transient immunity                         | EN 61000-4-4 2 kV, 5 kHz Communications cables such as Ethernet, RS-232, and RS-485: 1 kV, 5 kHz               | EN 61000-4-4 2 kV, 5 kHz Communications cables such as Ethernet, RS-232, and RS-485: 1 kV, 5 kHz               | EN 61000-4-4 2 kV, 5 kHz Communications cables such as Ethernet, RS-232, and RS-485: 1 kV, 5 kHz               | EN 61000-4-4 2 kV, 5 kHz Communications cables such as Ethernet, RS-232, and RS-485: 1 kV, 5 kHz               |

## Specifications

<!-- image -->

## General Specifications (Continued)

|                          | Description 1763-L16AWA 1763-L16BWA 1763-L16BBB 1763-L16DWD                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Surge transient immunity | EN 61000-4-5 Unshielded communications cable: 2 kV CM (common mode), 1 kV DM (differential mode) Shielded communications cable: 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC power supply input: 4 kV CM (common mode), 2 kV DM (differential mode) DC power supply input: 500V CM (common mode), 500V DM (differential mode) AC/DC auxiliary output: 500V CM (common mode), 500V DM (differential mode) | EN 61000-4-5 Unshielded communications cable: 2 kV CM (common mode), 1 kV DM (differential mode) Shielded communications cable: 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC power supply input: 4 kV CM (common mode), 2 kV DM (differential mode) DC power supply input: 500V CM (common mode), 500V DM (differential mode) AC/DC auxiliary output: 500V CM (common mode), 500V DM (differential mode) | EN 61000-4-5 Unshielded communications cable: 2 kV CM (common mode), 1 kV DM (differential mode) Shielded communications cable: 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC power supply input: 4 kV CM (common mode), 2 kV DM (differential mode) DC power supply input: 500V CM (common mode), 500V DM (differential mode) AC/DC auxiliary output: 500V CM (common mode), 500V DM (differential mode) | EN 61000-4-5 Unshielded communications cable: 2 kV CM (common mode), 1 kV DM (differential mode) Shielded communications cable: 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC power supply input: 4 kV CM (common mode), 2 kV DM (differential mode) DC power supply input: 500V CM (common mode), 500V DM (differential mode) AC/DC auxiliary output: 500V CM (common mode), 500V DM (differential mode) |
| Conducted RF immunity    | EN 61000-4-6 10V, 150 kHz…80 MHz                                                                                                                                                                                                                                                                                                                                                                                                         | EN 61000-4-6 10V, 150 kHz…80 MHz                                                                                                                                                                                                                                                                                                                                                                                                         | EN 61000-4-6 10V, 150 kHz…80 MHz                                                                                                                                                                                                                                                                                                                                                                                                         | EN 61000-4-6 10V, 150 kHz…80 MHz                                                                                                                                                                                                                                                                                                                                                                                                         |
| Conducted emissions      | EN 55011 AC power supply input: 150 kHz…30 MHz                                                                                                                                                                                                                                                                                                                                                                                           | EN 55011 AC power supply input: 150 kHz…30 MHz                                                                                                                                                                                                                                                                                                                                                                                           | EN 55011 AC power supply input: 150 kHz…30 MHz                                                                                                                                                                                                                                                                                                                                                                                           | EN 55011 AC power supply input: 150 kHz…30 MHz                                                                                                                                                                                                                                                                                                                                                                                           |
| Radiated emissions       | EN 55011 30…1000 MHz                                                                                                                                                                                                                                                                                                                                                                                                                     | EN 55011 30…1000 MHz                                                                                                                                                                                                                                                                                                                                                                                                                     | EN 55011 30…1000 MHz                                                                                                                                                                                                                                                                                                                                                                                                                     | EN 55011 30…1000 MHz                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Line related tests       | EN 61000-4-11 AC power supply input: • Voltage drop: -30% for 10 ms, -60% for 100 ms • Voltage interrupt: at voltage greater than -95% for 5 s • Voltage fluctuation: +10% for 15 min, -10% for 15 min DC power supply input:                                                                                                                                                                                                            | EN 61000-4-11 AC power supply input: • Voltage drop: -30% for 10 ms, -60% for 100 ms • Voltage interrupt: at voltage greater than -95% for 5 s • Voltage fluctuation: +10% for 15 min, -10% for 15 min DC power supply input:                                                                                                                                                                                                            | EN 61000-4-11 AC power supply input: • Voltage drop: -30% for 10 ms, -60% for 100 ms • Voltage interrupt: at voltage greater than -95% for 5 s • Voltage fluctuation: +10% for 15 min, -10% for 15 min DC power supply input:                                                                                                                                                                                                            | EN 61000-4-11 AC power supply input: • Voltage drop: -30% for 10 ms, -60% for 100 ms • Voltage interrupt: at voltage greater than -95% for 5 s • Voltage fluctuation: +10% for 15 min, -10% for 15 min DC power supply input:                                                                                                                                                                                                            |

Figure 82 - MicroLogix 1100 DC Input Power Requirements for 1763-L16BBB and 1763-L16DWD Unit

<!-- image -->

## Digital Input Specifications

|                                                     |                                                   | 1763-L16BWA, 1763-L16BBB                                                   | 1763-L16BWA, 1763-L16BBB                                                   |
|-----------------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|
|                                                     | Description 1763-L16AWA                           | Inputs 0...3 (4 high-speed DC inputs)                                      | Inputs 4 and Higher (6 standard DC inputs)                                 |
| On-state voltage range 79…132V AC                   |                                                   | 14…24V DC 14…26.4V DC (+10%) @ 65 °C/149 °F 14…30V DC (+25%) @ 30 °C/86 °F | 10…24V DC 10…26.4V DC (+10%) @ 65 °C/149 °F 10…30V DC (+25%) @ 30 °C/86 °F |
| Off-state voltage range 0…20V AC 0…5V DC            |                                                   |                                                                            |                                                                            |
| Operating frequency 47 Hz…63 Hz                     |                                                   | 0 Hz…20 kHz 0 Hz…40 kHz(1)                                                 | 0 Hz…1 kHz (scan time dependent)                                           |
| On-state current: Min Nom Max                       | 5.0 mA @ 79V AC 12 mA @ 120V AC 16.0 mA @ 132V AC | 2.5 mA @ 14V DC 9.8 mA @ 24V DC 12.0 mA @ 30V DC                           | 2.0 mA @ 10V DC 8.5 mA @ 24V DC 12.0 mA @ 30V DC                           |
| Off-state leakage current, max 2.5 mA 1.5 mA        |                                                   |                                                                            |                                                                            |
| Nominal impedance                                   | 12 kΩ @ 50 Hz 10 kΩ @ 60 Hz                       | 3.1 kΩ                                                                     | 3.1 kΩ                                                                     |
| Inrush current @ 120V AC, max 250 mA Not applicable |                                                   |                                                                            |                                                                            |

## Digital Input Specifications for 1763-L16DWD

|                                       | 1763-L16DWD                                      |                                            |
|---------------------------------------|--------------------------------------------------|--------------------------------------------|
| Description                           | Inputs 0...3 (4 high-speed DC inputs)            | Inputs 4 and Higher (6 standard DC inputs) |
| On-state voltage range                | 10…24V DC @ 65 °C/149 °F 10…30V DC @ 30 °C/86 °F |                                            |
| Off-state voltage range 0…5V DC       |                                                  |                                            |
| Operating frequency                   | 0 Hz…40 kHz(1)                                   | 0 Hz…1 kHz                                 |
| On-state current: Min Nom Max         | 2.0 mA @ 10V DC 8.5 mA @ 24V DC 12.0 mA @ 30V DC |                                            |
| Off-state leakage current, max 1.5 mA |                                                  |                                            |
| Nominal impedance 2.61 kΩ             |                                                  | 3.1 kΩ                                     |
| Maximum inrush current Not applicable |                                                  |                                            |

## Analog Input Specifications

| Description 1763-L16AWA, 1763-L16BWA, 1763-L16BBB, 1763-L16DWD   |
|------------------------------------------------------------------|
| Voltage input range 0…10.0V DC, - 1 LSB                          |
| Type of data 10-bit unsigned integer                             |
| Input coding (0...10.0V DC, - 1 LSB) 0…+1,023                    |
| Voltage input impedance 210 kΩ                                   |
| Input resolution 10 bit                                          |
| Non-linearity ±1.0% of full scale                                |
| Overall accuracy ° y -20…+65 °C (-4…+149 °F)  ±1.0% of full scale                                                                  |
| Voltage input overvoltage protection 10.5V DC                    |
| Field wiring to logic isolation Non-isolated with logic          |

## Output Specifications For Hazardous Locations Applications (Class I Division 2, Groups A, B, C, D) - General

| Description                                            |                                                                  | 1763-L16BBB                                                      |                            |
|--------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|----------------------------|
| Relay and FET Outputs                                  | Relay and FET Outputs                                            | Relay and FET Outputs                                            | Relay and FET Outputs      |
| Maximum controlled load 1080VA 360VA                   | Maximum controlled load 1080VA 360VA                             |                                                                  |                            |
| Maximum Continuous Current                             | Maximum Continuous Current                                       | Maximum Continuous Current                                       | Maximum Continuous Current |
| Current per group common 3 A 3 A                       | Current per group common 3 A 3 A                                 |                                                                  |                            |
| Current per controller                                 | @ 150V max 18 A or a total of per-point loads, whichever is less | @ 150V max 18 A or a total of per-point loads, whichever is less |                            |
| Current per controller                                 | @ 240V max 18 A or a total of per-point loads, whichever is less | @ 240V max 18 A or a total of per-point loads, whichever is less |                            |
| Relay Outputs                                          | Relay Outputs                                                    | Relay Outputs                                                    | Relay Outputs              |
| Turn on time/Turn off time, max                        | 10 ms(1)                                                         | 10 ms(1)                                                         |                            |
| Relay life - Electrical (Resistive Load) See Figure 83 | Relay life - Electrical (Resistive Load) See Figure 83           |                                                                  |                            |
| Relay life - Mechanical 10,000,000 cycles              | Relay life - Mechanical 10,000,000 cycles                        |                                                                  |                            |
| Load current, min 10 mA                                | Load current, min 10 mA                                          |                                                                  |                            |

## Relay Contact Ratings (1)

| Maximum Volts   | Amperes           | Amperes Continuous  p Make Break Make Break                   |                                 |
|-----------------|-------------------|-------------------|---------------------------------|
| 240V AC(2)      |                   | Amperes Continuous  p Make Break Make Break                   | 7.5 A 0.75 A 2.5 A 1800VA 180VA |
| 120V AC(3)      |                   |                   | 15.0 A 1.5 A 2.5 A 1800VA 180VA |
| 125V DC(4)      | 0.22 A 1.0 A 28VA | 0.22 A 1.0 A 28VA |                                 |

<!-- image -->

ATTENTION: Do not exceed the "Current per group common" specification.

## Output Specifications For Ordinary (Non-Hazardous) Locations only - General

| Description                                            | 1763-L16AWA, 1763-L16BWA, 1763-L16DWD  1763-L16BBB               |                                                                  |                            |
|--------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|----------------------------|
| Relay and FET Outputs                                  | Relay and FET Outputs                                            | Relay and FET Outputs                                            | Relay and FET Outputs      |
| Maximum controlled load 1440VA 720VA                   | Maximum controlled load 1440VA 720VA                             |                                                                  |                            |
| Maximum Continuous Current                             | Maximum Continuous Current                                       | Maximum Continuous Current                                       | Maximum Continuous Current |
| Current per group common                               | 5 A(1)                                                           | 5 A                                                              |                            |
| Current per controller                                 | @ 150V max 30 A or a total of per-point loads, whichever is less | @ 150V max 30 A or a total of per-point loads, whichever is less |                            |
| Current per controller                                 | @ 240V max 20 A or a total of per-point loads, whichever is less | @ 240V max 20 A or a total of per-point loads, whichever is less |                            |
| Relay Outputs                                          | Relay Outputs                                                    | Relay Outputs                                                    | Relay Outputs              |
| Turn on time/Turn off time, max                        | 10 ms(2)                                                         | 10 ms(2)                                                         |                            |
| Relay life - Electrical (Resistive Load) See Figure 83 | Relay life - Electrical (Resistive Load) See Figure 83           |                                                                  |                            |
| Relay life - Mechanical 10,000,000 cycles              | Relay life - Mechanical 10,000,000 cycles                        |                                                                  |                            |
| Load current, min 10 mA                                | Load current, min 10 mA                                          |                                                                  |                            |

## Relay Contact Ratings (1)

| Maximum Volts   | Amperes           | Amperes Continuous  p Make Break Make Break                   | Voltamperes               | Voltamperes   |
|-----------------|-------------------|-------------------|---------------------------|---------------|
| 240V AC(2)      | 15.0 A 1.5 A      | 5.0 A(3)          | 3600VA 360VA              |               |
| 120V AC(4)      |                   | 5.0 A(3)          | 30.0 A 3.0 A 3600VA 360VA |               |
| 125V DC(5)      | 0.22 A 1.0 A 28VA | 0.22 A 1.0 A 28VA |                           |               |

<!-- image -->

ATTENTION: Do not exceed the "Current per group common" specification.

Figure 83 - Relay Life Chart

<!-- image -->

## BBB FET Output Specifications

|                                                                       | Description General Operation                      | High-speed Operation (1) (Output 2 and 3 Only)              |
|-----------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------|
|                                                                       | Power supply voltage 24V DC (-15%, +10%)           | Power supply voltage 24V DC (-15%, +10%)                    |
| On-state voltage drop: @ maximum load current @ maximum surge current | 1V DC 2.5V DC                                      | Not applicable Not applicable                               |
| Current rating per point: Maximum load Minimum load Maximum leakage   | See Figure 84 1.0 mA 1.0 mA                        | 100 mA 10 mA 1.0 mA                                         |
| Surge current per point: Peak current Maximum surge duration g Maximum rate of repetition @ 30 °C (86 °F) °° p Maximum rate of repetition @ 55 °C (131 °F)                                                                       | 4.0 A 10 ms Once every second Once every 2 seconds | Not applicable Not applicable Not applicable Not applicable |
| Turn-on time, max 0.1 ms 6 µs                                         |                                                    |                                                             |
| Turn-off time, max 1.0 ms 18 µs                                       |                                                    |                                                             |
| Repeatability, max Not applicable 2 µs                                |                                                    |                                                             |
|                                                                       |                                                    | Drift, max Not applicable 1 µs per 5 °C (9 °F)              |

Figure 84 - Maximum Output Current (Temperature Dependent)

<!-- image -->

## AC Input Filter Settings

|                             | ON Delay (ms) OFF Delay (ms)   | ON Delay (ms) OFF Delay (ms)    |
|-----------------------------|--------------------------------|---------------------------------|
| Nominal Filter Setting (ms) |                                | Minimum Maximum Minimum Maximum |
|                             |                                | 8 2 20 10 20                    |

## High-speed DC Input Filter Settings (Inputs 0…3)

| Nominal Filter Setting (ms)   | ON Delay (ms) OFF Delay (ms)             | Maximum Counter Frequency (Hz) 50% Duty Cycle   |
|-------------------------------|------------------------------------------|-------------------------------------------------|
| Nominal Filter Setting (ms)   | Minimum Maximum Minimum Maximum          | Maximum Counter Frequency (Hz) 50% Duty Cycle   |
|                               | 00125 0.005 0.0125 0.003 0.0085          | 40.0 kHz(1)                                     |
|                               |                                          | 0.025 0.005 0.025 0.005 0.025 20.0 kHz          |
|                               |                                          | 0.075 0.040 0.075 0.045 0.075 6.7 kHz           |
|                               |                                          | 0.100 0.050 0.100 0.060 0.100 5.0 kHz           |
|                               |                                          | 0.250 0.170 0.250 0.210 0.250 2.0 kHz           |
|                               |                                          | 0.500 0.370 0.500 0.330 0.500 1.0 kHz           |
|                               |                                          | 1.00 0.700 1.000 0.800 1.000 0.5 kHz            |
|                               |                                          | 2.000 1.700 2.000 1.600 2.000 250 Hz            |
|                               |                                          | 4.000 3.400 4.000 3.600 4.000 125 Hz            |
| 8.000(2)                      |                                          | 6.700 8.000 7.300 8.000 63 Hz                   |
|                               | 16.000 14.000 16.000 14.000 16.000 31 Hz |                                                 |

## Standard DC Input Filter Settings (Inputs 4 and Higher)

| Nominal Filter Setting (ms)   | ON Delay (ms) OFF Delay (ms)             | Maximum Frequency (Hz) 50% Duty Cycle   |
|-------------------------------|------------------------------------------|-----------------------------------------|
| Nominal Filter Setting (ms)   | Minimum Maximum Minimum Maximum          | Maximum Frequency (Hz) 50% Duty Cycle   |
|                               |                                          | 0.500 0.090 0.500 0.020 0.500 1.0 kHz   |
|                               |                                          | 1.000 0.500 1.000 0.400 1.000 0.5 kHz   |
|                               |                                          | 2.000 1.100 2.000 1.300 2.000 250 Hz    |
|                               |                                          | 4.000 2.800 4.000 2.700 4.000 125 Hz    |
| 8.000(1)                      | 5.800 8.000 5.300 8.000 63 Hz            |                                         |
|                               | 16.000 11.000 16.000 10.000 16.000 31 Hz |                                         |

## Working Voltage – 1763-L16AWA

|                                           | Description 1763-L16AWA                                                                                                                                                                        |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power supply input to backplane isolation | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Input group to backplane isolation        | Verified by one of the following dielectric tests: 1517V AC for 1 s or 2145V DC for 1 s 132V AC Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Input group to input group isolation      | Verified by one of the following dielectric tests: 1517V AC for 1 s or 2145V DC for 1 s 132V AC Working Voltage (basic insulation)                                                             |
| Output group to backplane isolation       | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Output group to output group isolation    | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC Working Voltage (basic insulation) 150V AC Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage – 1763-L16BWA

|                                                                             | Description 1763-L16BWA                                                                             |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Power supply input to backplane isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Power supply input to backplane isolation                                   | 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s             |
| Input group to backplane isolation and input group to input group isolation | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Output group to backplane isolation                                         | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Output group to backplane isolation                                         | 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Output group to output group isolation                                      | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Output group to output group isolation                                      | 265V AC Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage – 1763-L16BBB

|                                                                             | Description 1762-L16BBB                                                                             |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s             |
| Input group to backplane isolation and input group to input group isolation | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| FET output group to backplane isolation                                     | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s             |
| FET output group to backplane isolation                                     | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Relay output group to backplane isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Relay output group to backplane isolation                                   | 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Relay output group to relay output group and FET output group isolation     | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Relay output group to relay output group and FET output group isolation     | 265V AC Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage – 1763-L16DWD

|                                                                             | Description 1763-L16DWD                                                                             |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s             |
| Input group to backplane isolation and input group to input group isolation | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Output group to backplane isolation                                         | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Output group to backplane isolation                                         | 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Output group to output group isolation                                      | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s             |
| Output group to output group isolation                                      | 265V AC Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## 1762 Expansion I/O Specifications

## General Specifications – Digital I/O Modules

| Attribute Value                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions Height: 90 mm (3.54 in.), 110 mm (4.33 in.) (including mounting tabs) Width: 87 mm (3.43 in.) Depth: 40.4 mm (1.59 in.) |
| Enclosure type rating None (open-style)                                                                                            |

## Input Specifications – 1762-IA8, 1762-IQ8, 1762-IQ16, 1762-IQ32T, 1762-IQ8OW6

|                                                                                                                                                     |                                                                                                                                                      |                                                                                                                                                                                       |                                                                                                                                                    | Attribute 1762-IA8 1762-IQ8 1762-IQ16 1762-IQ32T 1762-IQ8OW6                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                     |                                                                                                                                                      | Shipping weight, approx. (with carton)                                                                                                                                                | 209 g (0.46 lbs.) 200 g (0.44 lbs.) 230 g (0.51 lbs.) 200 g (0.44 lbs.) 280 g (0.62 lbs.)                                                          |                                                                                                                                                    |
| Voltage category 100/120V AC                                                                                                                        | 24V DC (sinking/ sourcing)( )(1)                                                                                                                     | 24V DC (sinking/ sourcing)( )(1)                                                                                                                                                      | 24V DC (sinking/ sourcing)( )(1)                                                                                                                   | 24V DC (sinking/sourcing)( )(1)                                                                                                                    |
| Operating voltage range 79…132V AC at 47…63 Hz                                                                                                      | 10…30V DC at 30 °C (86 °F) 10…26.4V DC at  55 °C (131 °F)                                                                                            | 10…30V DC 10…26.4V DC (2)(3)                                                                                                                                                          | 10…30V DC (24 points) at °° 30 °C (86 °F) 10…26.4V DC (23 points) at °° 60 °C (140 °F)                                                                                                                                                    | 10…30V DC at 30 °C (86 °F) 10…26.4V DC at 65 °C (149 °F)                                                                                           |
|                                                                                                                                                     |                                                                                                                                                      | Number of inputs 8 8 16 32 8                                                                                                                                                          |                                                                                                                                                    |                                                                                                                                                    |
| Bus current draw, max 50 mA at 5V DC (0.25 W) 50 mA at 5V DC (0.25 W)                                                                               |                                                                                                                                                      | 70 mA at 5V DC (0.35 W)(3)                                                                                                                                                            | 170 mA at 5V DC 0 mA at 24V DC                                                                                                                     | 110 mA at 5V DC 80 mA at 24V DC                                                                                                                    |
| Heat dissipation, max 2.0 W 3.7 W                                                                                                                   |                                                                                                                                                      | 4.3 W at 26.4V 5.4 W at 30V(3)                                                                                                                                                        | 5.4 W at 26.4V DC 6.8 W at 30V DC                                                                                                                  | 5.0 W at 30V DC 4.4 W at 26.4V DC  (The Watts per point, plus the min W, with all points energized)                                                |
| On delay: 20.0 ms Off delay: 20.0 ms                                                                                                                | On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                   | Signal delay, max  On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                                 | On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                 | On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                 |
|                                                                                                                                                     |                                                                                                                                                      |                                                                                                                                                                                       | Off-state voltage, max 20V AC 5V DC 5V DC 5V DC 5V DC                                                                                              |                                                                                                                                                    |
|                                                                                                                                                     |                                                                                                                                                      |                                                                                                                                                                                       | Off-state current, max 2.5 mA 1.5 mA 1.5 mA 1.0 mA 1.5 mA                                                                                          |                                                                                                                                                    |
| On-state voltage, min 79V AC (min) 132V AC (max) 10V DC 10V DC 10V DC 10V DC                                                                        |                                                                                                                                                      |                                                                                                                                                                                       |                                                                                                                                                    |                                                                                                                                                    |
| 5.0 mA min at 79V AC 47 Hz 12.0 mA nom. at 120V AC 60 Hz 16.0 mA max at 132V AC 63 Hz                                                               | 2.0 mA min at 10V DC 8.0 mA nom. at 24V DC 12.0 mA max at 30V DC                                                                                     | On-state current 2.0 mA min at 10V DC 8.0 mA nom. at 24V DC 12.0 mA max at 30V DC                                                                                                     | 1.6 mA min at 10V DC 2.0 mA min at 15V DC 5.7 mA max at 26.4V DC 6.5 mA max at 30.0V DC                                                            | 10 mA at 5V DC                                                                                                                                     |
|                                                                                                                                                     | Inrush current, max 250 mA Not applicable Not applicable Not applicable 250 mA                                                                       |                                                                                                                                                                                       |                                                                                                                                                    |                                                                                                                                                    |
| 12 kΩ at 50 Hz 10 kΩ at 60 Hz                                                                                                                       | 3 kΩ                                                                                                                                                 | Nominal impedance  3 kΩ                                                                                                                                                               | 4.7 kΩ                                                                                                                                             | 3 kΩ                                                                                                                                               |
| IEC input compatibility Type 1+ Type 1+ Type 1+ Type 1 Type 1+                                                                                      |                                                                                                                                                      |                                                                                                                                                                                       |                                                                                                                                                    |                                                                                                                                                    |
| Group 1: inputs 0…7 (internally connected commons)                                                                                                  | Group 1: inputs 0…7 (internally connected commons)                                                                                                   | Isolated groups  Group 1: inputs 0…7 Group 2: inputs 8…15                                                                                                                             | Group 1: Inputs 0…7 Group 2: Inputs 8…15 Group 3: Inputs 16…23 Group 4: Inputs 24…31                                                               | Group 1: inputs 0…3 Group 2: inputs 4…7                                                                                                            |
| Verified by one of the following dielectric tests: 1517V AC for 1 s or 2145V DC for 1 s 132V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V ACAC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Input group to backplane isolation Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Vendor I.D. code 1                                                                                                                                  | Vendor I.D. code 1                                                                                                                                   | Vendor I.D. code 1                                                                                                                                                                    | Vendor I.D. code 1                                                                                                                                 | Vendor I.D. code 1                                                                                                                                 |
| Product type code 7                                                                                                                                 | Product type code 7                                                                                                                                  | Product type code 7                                                                                                                                                                   | Product type code 7                                                                                                                                | Product type code 7                                                                                                                                |
|                                                                                                                                                     | Product code 114 96 97 99 98                                                                                                                         |                                                                                                                                                                                       |                                                                                                                                                    |                                                                                                                                                    |

## Digital I/O Modules

## Output Specifications – 1762-OA8, 1762-OB8, 1762-OB16, 1762-OB32T, 1762-OV32T

|                                                                                            |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    | Attribute 1762-OA8 1762-OB8 1762-OB16 1762-OB32T 1762-OV32T                                                                                        |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Shipping weight, approx. (with carton)                                                     |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    | 215 g (7.58 oz.) 210 g (7.41 oz.) 235 g (8.29 oz.) 200 g (7.05 oz.) 200 g (7.05 oz.)                                                               |
| Voltage category 100…240V AC 24V DC 24V DC 24V DC sourcing 24V DC sinking                  |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
|                                                                                            | Operating voltage range 85…265V AC at 47…63 Hz 20.4…26.4V DC 20.4…26.4V DC 10.2…26.4V DC 10.2…26.4V DC                                              |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| Number of outputs 8 8 16 32 32                                                             |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| Bus current draw, max                                                                      | 115 mA at 5V DC (0.575 W)                                                                                                                           | 115 mA at 5V DC (0.575 W) 175 mA at 5V DC (0.88 W)                                                                                                 |                                                                                                                                                    | 175 mA at 5V DC 0 mA at 24V DC                                                                                                                     | 175 mA at 5V DC 0 mA at 24V DC                                                                                                                     |
| Heat dissipation, max 2.9 W 1.61 W                                                         |                                                                                                                                                     |                                                                                                                                                    | 2.9 W at 30 °C (86 °F) 2.1 W at 55 °C (131 °F)                                                                                                     |                                                                                                                                                    | 3.4 W at 26.4 DC 2.7 W at 26.4V DC                                                                                                                 |
| Signal delay, max – resistive load                                                         | On delay: 1/2 cycle Off delay: 1/2 cycle                                                                                                            | On delay: 0.1 ms Off delay: 1.0 ms                                                                                                                 | On delay: 0.1 ms Off delay: 1.0 ms                                                                                                                 | On delay: 0.5 ms Off delay: 4.0 ms                                                                                                                 | On delay: 0.5 ms Off delay: 4.0 ms                                                                                                                 |
| Off-state leakage current, max                                                             | 2 mA at 132V 2.5 mA at 265V                                                                                                                         |                                                                                                                                                    |                                                                                                                                                    | 1.0 mA 1.0 mA 0.1 mA at 26.4V DC 0.1 mA at 26.4V DC                                                                                                |                                                                                                                                                    |
| On-state current, min 10 mA 1.0 mA 1.0 mA 1.0 mA 1.0 mA                                    |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| On-state voltage drop, max 1.5V at 0.5 A 1.0V DC 1.0V DC 0.3V DC at 0.5 A 0.3V DC at 0.5 A |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| Continuous current per point, max                                                          | 0.25 A at 55 °C (131 °F) 0.5 A at 30 °C (86 °F)                                                                                                     | 0.5 A at 55 °C (131 °F) 1.0 A at 30 °C (86 °F)                                                                                                     | 0.5 A at 55 °C (131 °F) 1.0 A at 30 °C (86 °F)                                                                                                     |                                                                                                                                                    | 0.5 A at 60 °C (140 °F) 0.5 A at 60 °C (140 °F)                                                                                                    |
| Continuous current per common, max                                                         | 1.0 A at 55 °C (131 °F) 2.0 A at 30 °C (86 °F)                                                                                                      | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                     | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                     |                                                                                                                                                    | 2.0 A at 60 °C (140 °F) 2.0 A at 60 °C (140 °F)                                                                                                    |
| Continuous current per module, max                                                         | 2.0 A at 55 °C (131 °F) 4.0 A at 30 °C (86 °F)                                                                                                      | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                     | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                     |                                                                                                                                                    | 4.0 A at 60 °C (140 °F) 4.0 A at 60 °C (140 °F)                                                                                                    |
| Surge current, max                                                                         | 5.0 A (Repeatability is once every 2 s for a duration of 25 ms)                                                                                     | 2.0 A (Repeatability is once °° py  every 2 s at 55 °C (131 °F), ° y  once every second at 30 °C ° y  (86 °F) for a duration of 10 ms)                                                                                                                                                    | 2.0 A (Repeatability is once °° py  every 2 s at 55 °C (131 °F), ° y  once every second at 30 °C ° y  (86 °F) for a duration of 10 ms)                                                                                                                                                    | 2.0 A (Repeatability is once °° py  every 2 s at 60 °C (140 °F) for 10 ms)                                                                                                                                                    | 2.0 A (Repeatability is once °° py  every 2 s at 60 °C (140 °F) for 10 ms)                                                                                                                                                    |
| Isolated groups                                                                            | Group 1: Outputs 0…3 Group 2: Outputs 4…7                                                                                                           | Group 1: Outputs 0…7 Group 1: Outputs 0…15                                                                                                         |                                                                                                                                                    | Group 1: Outputs 0…15 Group 2: Outputs 16…31 (internally connected to common)                                                                      | Group 1: Outputs 0…15 Group 2: Outputs 16…31 (internally connected to common)                                                                      |
| Output group to backplane isolation                                                        | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Output group to output group isolation                                                     | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Not applicable                                                                                                                                     | Not applicable                                                                                                                                     | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Vendor I.D. code 1                                                                         |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| Product type code 7                                                                        |                                                                                                                                                     |                                                                                                                                                    | Product code 119 101 103                                                                                                                           |                                                                                                                                                    | 100 102                                                                                                                                            |

## Output Specifications – 1762-OW8, 1762-OW16, 1762-OX6I, 1762-IQ8OW6

|                                        |                                                                                                                   |                                                          |                                                                         | Attribute 1762-OW8 1762-OW16 1762-OX6I 1762-IQ8OW6   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------|
| Shipping weight, approx. (with carton) |                                                                                                                   |                                                          | 228 g (0.50 lbs.) 285 g (0.63 lbs.) 220 g (0.485 lbs) 280 g (0.62 lbs.) |                                                      |
|                                        | Voltage category AC/DC normally open relay AC/DC normally open relay AC/DC Type C Relay AC/DC normally open relay |                                                          |                                                                         |                                                      |
| Operating voltage range                | 5…265V AC 5…125V DC                                                                                               | 5…265V AC 5…125V DC                                      | 5…265V AC 5…125V DC                                                     | 5…265V AC 5…125V DC                                  |
| Number of outputs 8 16 6 6             |                                                                                                                   |                                                          |                                                                         |                                                      |
| Bus current draw, max                  | 80 mA at 5V DC (0.40 W) 90 mA at 24V DC (2.16 W)                                                                  | 140 mA at 5V DC (0.70 W)(1) 180 mA at 24V DC (4.32 W)(1) | 110 mA at 5V DC (0.55 W) 110 mA at 24V DC (2.64 W)                      | 110 mA at 5V DC 80 mA at 24V DC                      |

## Output Specifications – 1762-OW8, 1762-OW16, 1762-OX6I, 1762-IQ8OW6 (Continued)

|                                                       |                                                                                                        |                                                                             | Attribute 1762-OW8 1762-OW16 1762-OX6I 1762-IQ8OW6                                                 |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Heat dissipation, max 2.9 W                           | 6.1 W(1)                                                                                               | 2.8 W                                                                       | 5.0 W at 30V DC 4.4 W at 26.4V DC (The Watts per point, plus the min W, with all points energized) |
| Signal delay, max – resistive load                    | On Delay: 10 ms Off Delay: 10 ms On Delay: 10 ms Off Delay: 10 ms                                      | On Delay: 10 ms (max) 6 ms (typical) Off Delay: 20 ms (max) 12 ms (typical) | On-delay: 10 ms (max) Off-delay: 10 ms (max)                                                       |
| Off-state leakage, max 0 mA 0 mA 0 mA 0 mA            |                                                                                                        |                                                                             |                                                                                                    |
| On-state current, min 10 mA 10 mA 100 mA 10 mA        |                                                                                                        |                                                                             |                                                                                                    |
| On-state voltage drop, max Not Applicable             |                                                                                                        |                                                                             |                                                                                                    |
| Continuous current per point, max 2.5 A. See Table 25 |                                                                                                        | 7 A See Table 26                                                            | 2.5 A See Table 25                                                                                 |
| Continuous current per common, max                    | 8 A 8 A                                                                                                | 7 A See Table 26                                                            | 8 A                                                                                                |
| Continuous current per module, max 16 A 16 A          |                                                                                                        | 30 A See Table 27                                                           | 8 A                                                                                                |
| Surge current, max See Table 25                       |                                                                                                        | See Table 26                                                                | See Table 25                                                                                       |
| Isolated groups                                       | Group 1: Outputs 0…3 Group 2: Outputs 4…7 Group 1: Outputs 0…7 Group 2: Outputs 8…15                   | All 6 Outputs Individually Isolated                                         | Group 3: Outputs 0…5                                                                               |
| Output group to backplane isolation                   | 265V AC working voltage (IEC Class 2 reinforced insulation)                                            |                                                                             | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s            |
| Output group to output group isolation                | 265V AC working voltage (basic insulation) 150V AC working voltage (IEC Class 2 reinforced insulation) |                                                                             | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s            |
| Vendor I.D. code 1                                    |                                                                                                        |                                                                             |                                                                                                    |
| Product type code 7                                   |                                                                                                        |                                                                             |                                                                                                    |
| Product code 120                                      | 121                                                                                                    |                                                                             | 124 98                                                                                             |

Table 25 - Relay Contact Ratings – 1762-OW8, 1762-OW16, and 1762-IQ8OW6

|               | Maximum Volts Amperes Continuous   | Amperes Voltamperes   | Amperes Voltamperes       |
|---------------|------------------------------------|-----------------------|---------------------------|
|               | Maximum Volts Amperes Continuous   |                       | Make Break Make Break     |
| 240V AC       | 2.5 A(1)                           |                       | 7.5 A 0.75 A 1800VA 180VA |
| 120V AC       | 2.5 A(1)                           |                       | 15 A 1.5 A 1800VA 180VA   |
| 125V DC 1.0 A |                                    | 0.22 A(2)             |                           |
| 24V DC 2.0 A  |                                    | 1.2 A(2)              | 28VA                      |

Table 26 - Relay Contact Ratings 1762-OX6I

| Maximum Volts            | Continuous Amps per Point (Max)(1)   | Amperes (2)   | Amperes (2)           | Voltamperes   | Voltamperes   |
|--------------------------|--------------------------------------|---------------|-----------------------|---------------|---------------|
| Maximum Volts            | Continuous Amps per Point (Max)(1)   |               | Make Break Make Break |               |               |
| 240V AC 5.0 A 15 A 1.5 A |                                      |               |                       | 3600VA 360VA  |               |
| 120V AC                  | 7.0 A(3)                             |               | 30 A 3.0 A            | 3600VA 360VA  |               |
| 125V DC 2.5 A 0.4 A      |                                      |               |                       | 50VA(4)       |               |
| 24V DC                   | 7.0 A(3)                             | 7.0 A         |                       | 168VA(4)      |               |

## Environmental Specifications

| Attribute Value                                  |                                                                                          |
|--------------------------------------------------|------------------------------------------------------------------------------------------|
| Temperature, operating                           | IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock):  °°°° pg  -20 °C ≤ Ta ≤ +65 °C (-4 °F ≤ Ta ≤ +149 °F)                                                                                          |
| Temperature, ambient, max 65 °C (140 °F)         |                                                                                          |
| Temperature, surrounding air, max 65 °C (140 °F) |                                                                                          |
| Temperature, nonoperating                        | IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock): °° -40…+85 °C (-40…+185 °F)                                                                                          |
| Relative humidity                                | IEC 60068-2-30 (Test Db, Unpackaged Damp Heat): 5…95% noncondensing                      |
| Vibration                                        | IEC 60068-2-6 (Test Fc, Operating): 5 g @ 10…500 Hz                                      |
| Shock, operating                                 | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30 g - Panel mounted                         |
| Shock, nonoperating                              | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30 g - Panel mounted 40 g - DIN rail mounted |
|                                                  | Emissions IEC 61000-6-4                                                                  |
| ESD immunity                                     | EC 61000-4-2: 4 kV contact discharges 8 kV air discharges                                |
| Radiated RF immunity                             | IEC 61000-4-3: 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                        |

Table 27 - Module Load Ratings 1762-OX6I

|                | Volts (Max) Controlled Load (Current) per Module (Max)   |
|----------------|----------------------------------------------------------|
| 240V AC 6 A    |                                                          |
| 120V AC        | 12 A(1)                                                  |
| 125V DC 11.5 A |                                                          |
| 24V DC         | 30 A(2)                                                  |

Figure 85 - Relays Used vs. Maximum Current per Relay (24V DC) 1762-OX6I

<!-- image -->

## Environmental Specifications (Continued)

| Attribute Value          |                                                                                                                                                                                                                               |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EFT/B immunity           | IEC 61000-4-4: ±2 kV @ 5 kHz on power ports ±2 kV @ 5 kHz on signal ports ±1 kV @ 5 kHz on communication ports                                                                                                                |
| Surge transient immunity | IEC 61000-4-5: ±2 kV line-line(DM) and ±4 kV line-earth(CM) on AC power ports ±500V line-line(DM) and ±1 kV line-earth(CM) on signal ports ±1 kV line-earth(CM) on shielded ports ±2 kV line-earth(CM) on communication ports |
| Conducted RF immunity    | IEC 61000-4-6: 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                                                        |

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us                                      | UL Listed Industrial Control Equipment, certified for U.S. and Canada. See UL File E322657. UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for U.S. and Canada. See UL File E334470.                                                                                                                                                                                                                  |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) European Union 2014/35/EU LVD, compliant with: EN 61131-2; Programmable Controllers (Clause 11) European Union 2011/62/EU RoHS, compliant with: EN IEC 63000; Technical Documentation |
| RCM                                          | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emmissions                                                                                                                                                                                                                                                                                                                                                 |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                                                                                                                                                             |
| UKCA                                         | 2016 No. 1091 – Electromagnetic Compatibility Regulations 2016 No. 1101 – Electrical Equipment (Safety) Regulations 2012 No. 3032 – Restriction of the Use of Certain Hazardous Substances in Electrical and Electronic Equipment Regulations                                                                                                                                                                                           |

## Analog I/O Modules

## Common Specifications – 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4, 1762-OF4

|                   | Attribute 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4, 1762-OF4                                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions HxWxD  | 90 x 87 x 40 mm Height including mounting tabs is 110 mm (3.54 x 3.43 x 1.58 in.) Height including mounting tabs is 4.33 in.                                                           |
|                   | Module power status indicator On: Indicates power is applied                                                                                                                           |
| Recommended cable | Belden 8761 (shielded) For 1762-IT4, shielded thermocouple extension wire for the specific type of thermocouple you are using. Follow the thermocouple manufacturer’s recommendations. |

## General Specifications – 1762-IF2OF2, 1762-IF4, 1762-OF4, 1762-IR4, 1762-IT4

| Specification 1762-IF2OF2 1762-IF4 1762-OF4 1762-IR4 1762-IT4   |                                    |                                                                          |                                   |                              |                               |
|-----------------------------------------------------------------|------------------------------------|--------------------------------------------------------------------------|-----------------------------------|------------------------------|-------------------------------|
| Shipping weight, approx. (with carton)                          |                                    | 240 g (0.53 lbs.) 235 g (0.517 lbs.) 260 g (0.57 lbs.) 220 g (0.53 lbs.) |                                   |                              |                               |
| Bus current draw, max                                           | 40 mA @ 5V DC 105 mA @ 24V DC      | 40 mA @ 5V DC 50 mA @ 24V DC                                             | 40 mA @ 5V DC 165 mA @ 24V DC     | 40 mA @ 5V DC 50 mA @ 24V DC | 40 mA @ 5V DC 50 mA @ 24V DC  |
| Analog normal operating range                                   | Voltage: 0…10V DC Current: 4…20 mA | Voltage: -10…+10V DC Current: 4…20 mA                                    | Voltage 0…10V DC Current: 4…20 mA |                              | Not applicable Not applicable |

## General Specifications – 1762-IF2OF2, 1762-IF4, 1762-OF4, 1762-IR4, 1762-IT4 (Continued)

| Specification 1762-IF2OF2 1762-IF4 1762-OF4 1762-IR4 1762-IT4   |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Full scale(1) analog ranges                                     | Voltage: 0…10.5V DC Current: 0…21 mA                                                                                                             | Voltage: -10.5…+10.5V DC Current: -21…+21 mA                                                                                                     | Voltage:0…10.5V DC Current: 0…21 mA                                                                                |                                                                                                                                                                | Not applicable Not applicable                                          |
|                                                                 | Resolution 12 bits (unipolar)                                                                                                                    | 15 bits (bipolar) (2)                                                                                                                            | 12 bits (unipolar)                                                                                                 | Input filter and configuration dependent                                                                                                                       | 15 bits plus sign                                                      |
| Repeatability (3)                                               | ±0.12%(2)                                                                                                                                        | ±0.12%(2)                                                                                                                                        | ±0.12%(2)                                                                                                          | ±0.1 °C (±0.18 °F) for Ni and NiFe ±0.2 °C (±0.36 °F)…±0.2 °C (±0.36 °F) for other RTD inputs ±0.04 ohm for 150 ohm resistances ±0.2 ohm for other resistances | See Table 28                                                           |
| Input and output group to system isolation                      | 30V AC/30V DC rated working voltage (4) (N.E.C. Class 2 required) (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC rated working voltage (4) (N.E.C. Class 2 required) (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC rated working voltage (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC working voltage type test: 500V AC or 707V DC for 1 minute                                                                                       | 30V AC/30V DC working voltage qualification test: 720V DC for 1 minute |
| Vendor I.D. code 1 1 1 1 1                                      |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |
| Product type code 10 10 10 10 10                                |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |
| Product code 75 67 66 65 64                                     |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |

## Input Specifications – 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4

|                                              | Attribute 1762-IF2OF2 1762-IF4 1762-IR4 1762-IT4                                             |                                                                                    |                                                                                  |                                                                                  |
|----------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|                                              | Number of inputs 2 differential (unipolar) 4 differential (bipolar) 4                        |                                                                                    |                                                                                  | 4 input channels plus 1 CJC sensor                                               |
| Update time (typical) 2.5 ms                 |                                                                                              | 130, 250, 290, 450, 530 ms (selectable)                                            | Input filter and configuration dependent                                         | NA                                                                               |
|                                              | A/D converter type Successive approximation Successive approximation Delta-Sigma Delta-Sigma |                                                                                    |                                                                                  |                                                                                  |
| Common mode voltage range (1)                |                                                                                              | ±27V ±27V NA ±10V                                                                  |                                                                                  |                                                                                  |
| Common mode rejection (2)                    |                                                                                              | > 55 dB at 50 Hz and 60 Hz > 55 dB at 50 Hz and 60 Hz                              | >110 dB at 50 Hz (with 10 Hz or 60 Hz filter)                                    | >110 dB at 50 Hz (with 10 Hz or 60 Hz filter)                                    |
| Non-linearity (in percent full scale)        | ±0.12%(3)                                                                                    | ±0.12%(3)                                                                          | ±0.05% NA                                                                        |                                                                                  |
| Typical overall accuracy (4)                 | ±0.55% full scale at -20…+65 °C (-4…+149 °F)(3) ±0.3% full scale at 25 °C (77 °F)            | ±0.32% full scale at -20…+65 °C (-4…+149 °F)(3) ±0.24% full scale at 25 °C (77 °F) | ±0.5 °C (0.9 °F) for Pt 385 NA                                                   |                                                                                  |
| Input impedance                              | Voltage Terminal: 200 kΩ Current Terminal: 250 Ω                                             | Voltage Terminal: 200 kΩ Current Terminal: 275 Ω                                   | >10 MΩ                                                                           | >10 MΩ                                                                           |
| Current input protection ±32 mA ±32 mA NA NA |                                                                                              |                                                                                    |                                                                                  |                                                                                  |
| Voltage input protection ±30V ±30V NA NA     |                                                                                              |                                                                                    |                                                                                  |                                                                                  |
| Channel diagnostics                          | Over or under range or open circuit condition by bit reporting for analog inputs             | Over or under range or open circuit condition by bit reporting for analog inputs   | Over or under range or open circuit condition by bit reporting for analog inputs | Over or under range or open circuit condition by bit reporting for analog inputs |

## Input Specifications 1762-IR4

|                                                                       | Attribute 1762-IR4                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input types                                                           | 100 Ω Platinum 385 200 Ω Platinum 385 500 Ω Platinum 385 1000 Ω Platinum 385 100 Ω Platinum 3916 200 Ω Platinum 3916 500 Ω Platinum 3916 1000 Ω Platinum 3916 10 Ω Copper 426 120 Ω Nickel 672 120 Ω Nickel 618 604 Ω Nickel-Iron 518 0...150 Ω 0...500 Ω 0...1000 Ω 0...3000 Ω |
|                                                                       | Heat dissipation 1.5 Total Watts (The Watts per point, plus the minimum Watts, with all points enabled)                                                                                                                                                                         |
| Normal mode rejection ratio                                           | 70 dB minimum at 50 Hz with the 10 Hz or 50 Hz filter selected 70 dB minimum at 60 Hz with the 10 Hz or 60 Hz filter selected                                                                                                                                                   |
| Typical accuracy [Auto-calibration enabled] at 25 °° ypy  °C (77 °F) ambient with module operating temperature at 25 °C (77 °F)( )(1)                                                                       | ±0.5 °C (0.90 °F) for Pt 385 ±0.4 °C (0.72 °F) for Pt 3916 ±0.2 °C (0.36 °F) for Ni ±0.3 °C (0.54 °F) for NiFe ±0.6 °C (1.08 °F) for Cu ±0.15 Ω for 150 Ω range ±0.5 Ω for 500 Ω range ±1.0 Ω for 1000 Ω range ±1.5 Ω for 3000 Ω range                                          |
| Typical accuracy [Auto-calibration enabled] at 0…55 °C (32…131 °F)(1) | ±0.9 °C (1.62 °F) for Pt 385 ±0.8 °C (1.40 °F) for Pt 3916 ±0.4 °C (0.72 °F) for Ni ±0.5 °C (0.90 °F) for NiFe ±1.1 °C (1.98 °F) for Cu ±0.25 Ω for 150 Ω range ±0.8 Ω for 500 Ω range ±1.5 Ω for 1000 Ω range ±2.5 Ω for 3000 Ω range                                          |
| Accuracy drift at 0…55 °C (32…131 °F)                                 | ±0.026 °C/°C (0.026 °F/°F) for Pt 385 ±0.023 °C/°C (0.023 °F/°F) for Pt 3916 ±0.012 °C/°C (0.012 °F/°F) for Ni ±0.015 °C/°C (0.015 °F/°F) for NiFe ±0.032 °C/°C (0.032 °F/°F) for Cu ±0.007 Ω/°C (0.012 Ω/°F) for 150 Ω range °° g ±0.023 Ω/°C (0.041 Ω/°F) for 500 Ω range °° g ±0.043 Ω/°C (0.077 Ω/°F) for 1000 Ω range °° g ±0.07 Ω/°C (0.130 Ω/°F) for 3000 Ω range                                                                                                                                                                                                                                                                                 |
|                                                                       | Excitation current source 0.5 mA and 1.0 mA selectable per channel                                                                                                                                                                                                              |
| Open-circuit detection time (2)                                       | 6…1212 ms                                                                                                                                                                                                                                                                       |
| Input channel configuration                                           | Via configuration software screen or the user program (by writing a unique bit pattern into the module’s configuration file). See your controller’s user manual to determine if user program configuration is supported.                                                        |
| Calibration                                                           | The module performs auto-calibration on channel enable and on a configuration change between channels. You can also program the module to calibrate every 5 minutes.                                                                                                            |
| Maximum overload at input terminals ±35V DC continuous                |                                                                                                                                                                                                                                                                                 |
|                                                                       | Cable impedance, max 25 Ω − Operating with >25 Ω reduces accuracy.                                                                                                                                                                                                              |
| Channel to channel isolation ±10V DC                                  |                                                                                                                                                                                                                                                                                 |

## Input Specifications 1762-IT4

| Attribute Value             |                                                                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Heat dissipation 1.5 Total Watts (The Watts per point, plus the minimum Watts, with all points energized)                                           |
|                             | Response speed per channel Input filter and configuration dependent                                                                                 |
| Rated working voltage (1)   | 30V AC/30V DC                                                                                                                                       |
| Normal mode rejection ratio | 85 dB (minimum) at 50 Hz (with 10 Hz or 50 Hz filter) 85 dB (minimum) at 60 Hz (with 10 Hz or 60 Hz filter)                                         |
|                             | Cable impedance, max 25 Ω (for specified accuracy)                                                                                                  |
| Open-circuit detection time | 7 ms…1.515 s(2)                                                                                                                                     |
| Calibration                 | The module performs auto-calibration upon power-up and whenever a channel is enabled. You can also program the module to calibrate every 5 minutes. |

## Input Specifications 1762-IT4 (Continued)

| Attribute Value                     |                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|                                     | CJC accuracy ±1.3 °C (±2.34 °F)                                                                                              |
| Maximum overload at input terminals | ±35V DC continuous(3)                                                                                                        |
| Input channel configuration         | Via configuration software screen or the user program (by writing a unique bit pattern into the module’s configuration file) |

## 1762-IT4 Accuracy

| Input Type (1)                                                                                                     | With Auto-calibration Enabled Without Auto-calibration                              |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|                                                                                                                    | Maximum Temperature Drift(2)                                                        |
| @ 25 °C [77 °F] Ambient @ 0…60 °C [32…140 °F]                                                                      | Ambient @ 0…60 °C [32…140 °F] Ambient                                               |
| Thermocouple J (-210…+1200 °C [-346…+2192 °F]) ±0.6 °C [±1.1 °F] ±0.9 °C [±1.7 °F] ±0.0218 °C/ °C [±0.0218 °F/ °F] |                                                                                     |
| Thermocouple N (-200…+1300 °C [-328…+2372 °F]) ±1 °C [±1.8 °F] ±1.5 °C [±2.7 °F] ±0.0367 °C/ °C [±0.0367 °F/ °F]   |                                                                                     |
| Thermocouple N (-210…-200 °C [-346…-328 °F]) ±1.2 °C [±2.2 °F] ±1.8 °C [±3.3 °F] ±0.0424 °C/ °C [±0.0424 °F/ °F]   |                                                                                     |
| Thermocouple T (-230…+400 °C [-382…+752 °F]) ±1 °C [±1.8 °F] ±1.5 °C [±2.7 °F] ±0.0349 °C/ °C [±0.0349 °F/ °F]     |                                                                                     |
| Thermocouple T (-270…-230 °C [-454…-382 °F]) ±5.4 °C [±9.8 °F] ±7.0 °C [±12.6 °F] ±0.3500 °C/ °C [±0.3500 °F/ °F]  |                                                                                     |
| Thermocouple K (-230…+1370 °C [-382…+2498 °F]) ±1 °C [±1.8 °F] ±1.5 °C [±2.7 °F] ±0.4995 °C/ °C [±0.4995 °F/ °F]   |                                                                                     |
| Thermocouple K (-270…-225 °C [-454…-373 °F]) ±7.5 °C [±13.5 °F] ±10 °C [± 18 °F] ±0.0378 °C/ °C [±0.0378 °F/ °F]   |                                                                                     |
| Thermocouple E (-210…+1000 °C [-346…+1832 °F]) ±0.5 °C [±0.9 °F] ±0.8 °C [±1.5 °F] ±0.0199 °C/ °C [±0.0199 °F/ °F] |                                                                                     |
| Thermocouple E (-270…-210 °C [-454…-346 °F]) ±4.2 °C [±7.6 °F] ±6.3 °C [±11.4 °F] ±0.2698 °C/ °C [±0.2698 °F/ °F]  |                                                                                     |
|                                                                                                                    | Thermocouple R ±1.7 °C [±3.1 °F] ±2.6 °C [±4.7 °F] ±0.0613 °C/ °C [±0.0613 °F/ °F]  |
|                                                                                                                    | Thermocouple S ±1.7 °C [±3.1 °F] ±2.6 °C [± 4.7 °F] ±0.0600 °C/ °C [±0.0600 °F/ °F] |
|                                                                                                                    | Thermocouple C ±1.8 °C [±3.3 °F] ±3.5 °C [±6.3 °F] ±0.0899 °C/ °C [±0.0899 °F/ °F]  |
|                                                                                                                    | Thermocouple B ±3.0 °C [±5.4 °F] ±4.5 °C [±8.1 °F] ±0.1009 °C/ °C [±0.1009 °F/ °F]  |
|                                                                                                                    | ±50 mV ±15 µV ±25 µV ±0.44 µV/ °C [±0.80 µV/ °F]                                    |
|                                                                                                                    | ±100 mV ±20 µV ±30 µV ±0.69 µV/ °C [±01.25 µV/ °F]                                  |

Table 28 - 1762-IT4 Repeatability at 25 °C (77 °F)( )(1)
(2)

| Input Type Repeatability for 10 Hz Filter                         |
|-------------------------------------------------------------------|
| Thermocouple J ±0.1 °C [±0.18 °F]                                 |
| Thermocouple N (-110…+1300 °C [-166…+2372 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple N (-210…-110 °C [-346…-166 °F]) ±0.25 °C [±0.45 °F]  |
| Thermocouple T (-170…+400 °C [-274…+752 °F]) ±0 .1 °C [±0.18 °F]  |
| Thermocouple T (-270…-170 °C [-454…-274 °F]) ±1.5 °C [±2.7 °F]    |
| Thermocouple K (-270…+1370 °C [-454…+2498 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple K (-270…-170 °C [-454…-274 °F]) ±2.0 °C [±3.6 °F]    |
| Thermocouple E (-220…+1000 °C [-364…+1832 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple E (-270…-220 °C [-454…-364 °F]) ±1.0 °C [±1.8 °F]    |
| Thermocouples S and R ±0.4 °C [±0.72 °F]                          |
| Thermocouple C ±0.2 °C [±0.36 °F]                                 |
| Thermocouple B ±0.7 °C [±1.26 °F]                                 |
| ±50 mV ±6 µV                                                      |
| ±100 mV ±6 µV                                                     |

## Environmental Specifications

| Attribute Value                      |                                                                                                                                                                       |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      | Temperature, storage -40…+85 °C (-40…+185 °F)                                                                                                                         |
| Temperature, operating               | -20…+65 °C (-4…+149 °F)(1)                                                                                                                                            |
|                                      | Operating humidity 5…95% noncondensing                                                                                                                                |
| Operating altitude 2000 m (6561 ft.) |                                                                                                                                                                       |
|                                      | Vibration Operating: 10…500 Hz, 5 g, 0.030 in. max peak-to-peak                                                                                                       |
|                                      | Shock Operating: 30 g                                                                                                                                                 |
|                                      | Emissions IEC 61000-6-4                                                                                                                                               |
| ESD immunity                         | IEC 61000-4-2: 6 kV contact discharges 8 kV air discharges                                                                                                            |
| Radiated RF immunity                 | IEC 61000-4-3: 10V/m with 1 kHz sine wave 80% AM from 80…1000 MHz 3V/m with 1 kHz sine wave 80% AM from 1.4…2.0 GHz 1V/m with 1 kHz sine wave 80% AM from 2.0…2.7 GHz |
| EFT/B immunity                       | IEC 61000-4-4: ±2 kV @ 5 kHz on signal ports                                                                                                                          |
| Surge transient immunity             | IEC 61000-4-5: ±1 kV line-earth(CM) on shielded ports                                                                                                                 |
| Conducted RF immunity                | IEC 61000-4-6: 10V rms with 1 Hz sine wave 80% AM from 150 kHz…80 MHz(2)                                                                                              |

<!-- image -->

## Output Specifications – 1762-IF2OF2, 1762-OF4

| Specification 1762-IF2OF2 1762-OF4                      |                                                                                                                        |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Number of outputs 2 single-ended (unipolar)             | 4 single-ended (unipolar)(2)                                                                                           |
| Update time (typical) 4.5 ms 2.5 ms                     |                                                                                                                        |
|                                                         | D/A converter type Resistor string R-2R ladder voltage switching                                                       |
|                                                         | Resistive load on current output 0…500 Ω (includes wire resistance) 0…500 Ω (includes wire resistance)                 |
| Load range on voltage output > 1 kΩ                     | > 1 kΩ                                                                                                                 |
| Reactive load, current output < 0.1 mH < 0.1 mH         |                                                                                                                        |
| Reactive load, voltage output < 1 µF < 1 µF             |                                                                                                                        |
| Typical overall accuracy (1)                            | ±1.17% full scale @ -20…+65 °C (2) ±0.5% full scale @ 25 °C ±1.17% full scale @ -20…+65 °C(2) ±0.5% full scale @ 25 °C |
| Output ripple range 0…500 Hz (referred to output range) | < ±0.1% < ±0.1%                                                                                                        |
| Non-linearity (in percent full scale)  < ±0.59%(2)      | < ±0.59%(2)                                                                                                            |
| Open and short-circuit protection Continuous Continuous |                                                                                                                        |
| Output protection ±32 mA ±32 mA                         |                                                                                                                        |

Table 29 - Valid Input/Output Data Word Formats/Ranges for 1762-IF2OF2

| Normal Operating Range Full Scale Range RAW/Proportional Data Scaled-for-PID   |                        |
|--------------------------------------------------------------------------------|------------------------|
| 0…10V DC                                                                       | 10.5V DC 32,760 16,380 |
| 0…10V DC                                                                       | 0.0V DC 0 0            |
| 4…20 mA                                                                        | 21.0 mA 32,760 16,380  |
| 4…20 mA                                                                        | 20.0 mA 31,200 15,600  |
| 4…20 mA                                                                        | 4.0 mA 6,240 3,120     |
| 4…20 mA                                                                        | 0.0 mA 0 0             |

For more detailed 1762-IT4 accuracy information, see the MicroLogix 1200 Thermocouple/mV Input Module User Manual, publication 1762-UM002 .

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                              | UL UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations                                                                                                                  |
|                                              | cUL UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for Canada.                                                                                          |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
| RCM                                          | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                 |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                               |

## Notes:

## MicroLogix 1100 Replacement Kits

## Lithium Battery (1763-BA)

## Replacement Parts

Table 30 provides a list of replacement parts and their catalog number.

Table 30 - MicroLogix 1100 Controller Replacement Parts

| Description Catalog Number   |
|------------------------------|
| Lithium Battery 1763-BA      |

## IMPORTANT

When the controller's Battery Low indicator is lit, check whether the battery wire connector is connected correctly or replace the replaceable battery with a new one immediately. When the indicator turns on, it means that either the battery is disconnected, or that the battery requires replacement. The controller is designed to operate for up to 2 weeks, from the time that the indicator first turns on. We recommend that you replace the battery immediately when the indicator turns on.

## Installation

Follow the procedure below to ensure proper replaceable battery installation.

1. Insert a battery into the battery pocket with wires facing up.
2. Insert the battery wire connector into the battery connector.
3. Secure the battery connector wires along the wire guide, as shown in Figure 86 .

<!-- image -->

Figure 86 - Replaceable Battery Wire Connection

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

Three or More Batteries

Procedures for the transportation of three or more batteries shipped together within the United States are specified by the Department of Transportation (DOT) in the Code of Federal Regulations, CFR49, "Transportation." An exemption to these regulations, DOT - E7052, covers the transport of certain hazardous materials classified as flammable solids. This exemption authorizes transport of lithium batteries by motor vehicle, rail freight, cargo vessel, and cargoonly aircraft, providing certain conditions are met. Transport by passenger aircraft is not permitted.

A special provision of DOT-E7052 (11th Rev., October 21, 1982, par. 8-a) provides that:

"Persons that receive cell and batteries covered by this exemption may reship them pursuant to the provisions of 49 CFR 173.22a in any of these packages authorized in this exemption including those in which they were received."

The Code of Federal Regulations, 49 CFR 173.22a, relates to the use of packaging authorized under exemptions. In part, it requires that you must maintain a copy of the exemption at each facility where the packaging is being used in connection with shipment under the exemption.

Shipment of depleted batteries for disposal may be subject to specific regulation of the countries involved or to regulations endorsed by those countries, such as the IATA Articles Regulations of the International Air Transport Association, Geneva, Switzerland.

IMPORTANT

Regulations for transportation of lithium batteries are periodically revised. See www.dot.gov for the latest shipping information.

- Do not charge the batteries. An explosion could result or the cells could overheat causing burns.
- Do not open, puncture, crush, or otherwise mutilate the batteries. A possibility of an explosion exists and/or toxic, corrosive, and flammable liquids would be exposed.
- Do not incinerate or expose the batteries to high temperatures. Do not attempt to solder batteries. An explosion could result.
- Do not short positive and negative terminals together. Excessive heat can build up and cause severe burns.

## Disposal

<!-- image -->

ATTENTION: Do not incinerate or dispose of lithium batteries in general trash collection. Explosion or violent rupture is possible. Batteries should be collected for disposal in a manner to prevent against short-circuiting, compacting, or destruction of case integrity and hermetic seal.

For disposal, batteries must be packaged and shipped in accordance with transportation regulations, to a proper disposal site. The U.S. Department of Transportation authorizes shipment of "Lithium batteries for disposal" by motor vehicle only in regulation 173.1015 of CFR 49 (effective January 5, 1983). For additional information contact:

U.S. Department of Transportation Research and Special Programs Administration 400 Seventh Street, S.W. Washington, D.C. 20590

Although the Environmental Protection Agency at this time has no regulations specific to lithium batteries, the material contained may be considered toxic, reactive, or corrosive. The person disposing of the material is responsible for any hazard created in doing so. State and local regulations may exist regarding the disposal of these materials.

For a lithium battery product safety data sheet, contact the manufacturer:

Sanyo Energy Corporation Tadarand U.S. Battery Division San Diego, CA 92173 Port Washington, NY 11050

2001 Sanyo Avenue 2 Seaview Blvd. (619) 661-4801 (516) 621-4980

## Notes:

## Understand the Controller Status Indicators

## Troubleshoot Your System

The MicroLogix 1100 controller provides three groups of status indicators:

- The LED status indicators on the top of the controller
- The status indicators on the LCD
- The I/O status indicators on the LCD

Together they provide a mechanism to determine the current status of the controller if a programming device is not present or available.

## Controller Status Indicators

Figure 87 - Controller Status Indicator Location

<!-- image -->

| Status Indicator Color Indicates   |                                                                         |
|------------------------------------|-------------------------------------------------------------------------|
| POWER                              | Off No input power or power error condition                             |
| POWER                              | Steady green Power on                                                   |
| RUN                                | Off Not executing the user program                                      |
| RUN                                | Steady green Executing the user program in run mode                     |
| RUN                                | Flashing green Memory module transfer occurring                         |
| FAULT                              | Off No fault detected                                                   |
| FAULT                              | Flashing red Application fault detected                                 |
| FAULT                              | Steady red Controller hardware faulted                                  |
| FORCE                              | Off No forces installed                                                 |
| FORCE                              | Steady amber Forces installed                                           |
| FORCE                              | Flashing amber Forces installed in force files, but forcing is disabled |

Table 31 - Controller Status Indicators

<!-- image -->

## Status Indicators on the LCD

Figure 88 - Status Indicators on the LCD

<!-- image -->

Table 32 - Status Indicators on the LCD

|          | Indicator Color Indicates                                                     |
|----------|-------------------------------------------------------------------------------|
| COMM 0   | Off (empty rectangle) Not transmitting through RS-232/RS-485 port (Channel 0) |
| COMM 0   | On (solid rectangle) Transmitting through RS-232/RS-485 port (Channel 0)      |
| COMM 1   | Off (empty rectangle) Not transmitting through Ethernet port (Channel 1)      |
| COMM 1   | On (solid rectangle) Transmitting through Ethernet port (Channel 1)           |
| DCOMM(1) | Off (empty rectangle) Configured communications                               |
| DCOMM(1) | On (solid rectangle) Default communications                                   |
| BAT. LO  | Off (empty rectangle) Battery level is acceptable                             |
| BAT. LO  | On (solid rectangle) Battery low                                              |
| U-MSG    | Off (empty rectangle) Default display mode                                    |
| U-MSG    | On (solid rectangle) Customized display mode                                  |

## I/O Status Indicators on the LCD

Figure 89 - I/O Status Indicators on the LCD

I/O LED screen on the LCD

<!-- image -->

Table 33 - I/O Status Indicators on the LCD

|           | Indicator Color Indicates                                 |
|-----------|-----------------------------------------------------------|
| INPUTS(1) | Off (empty rectangle) Input is not energized              |
| INPUTS(1) | On (solid rectangle) Input is energized (terminal status) |
| OUTPUTS   | Off (empty rectangle) Output is not energized             |
| OUTPUTS   | On (solid rectangle) Output is engerized (logic status)   |

Table 34 - Error Conditions

|                                         | If the LEDS Indicate The Following Error Exists Probable Cause Recommended Action   |                                        |                                                                                                                                                      |
|-----------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| All LEDs off                            | No input power or power supply error                                                |                                        | No line power Verify proper line voltage and connections to the controller.                                                                          |
| All LEDs off                            | No input power or power supply error                                                | Power supply overloaded                | This problem can occur intermittently if power supply is overloaded when output loading and temperature varies.                                      |
| Power and FAULT LEDs on solid           | Hardware faulted                                                                    |                                        | Processor hardware error Cycle power. Contact your local Allen-Bradley representative if the error persists.                                         |
| Power and FAULT LEDs on solid           | Hardware faulted                                                                    |                                        | Loose wiring Verify connections to the controller.                                                                                                   |
| Power LED on and FAULT LED flashing     | Application fault                                                                   | Hardware/software major fault detected | For error codes and Status File information, see MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 . |
| RUN, FORCE, and FAULT LEDs all flashing | Operating system fault                                                              | Missing or corrupt operating system    | See Missing or Corrupt OS LED Pattern on page 144 .                                                                                                  |

## Normal Operation

The POWER and RUN status indicators are On. If forcing is enabled and forces are installed in the I/O force files, the FORCE status indicator turns on and remains on until all forces are removed. If forcing is disabled and forces are installed in the I/O force files, the FORCE status indicator flashes and remains flashing until all forces are removed from the I/O force files.

## Error Conditions

If an error exists within the controller, the controller status indicators operate as described in Table 34 .

## Controller Error Recovery Model

Figure 90 helps you diagnose software and hardware problems in the micro controller. The model provides common questions you might ask to help troubleshoot your system. See the recommended pages within the model for further help.

Figure 90 - Controller Error Recovery Model

<!-- image -->

## Analog Expansion I/O Diagnostics and Troubleshooting

Table 36 - Module Error Table

|                                                 | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   |
|-------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
|                                                 | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                       |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
|                                                 |                                                             | 0000000000000000                                            |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1 | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |

## Module Error Field

The purpose of the module error field is to classify module errors into three distinct groups, as described in Table 37. The type of error determines what kind of information exists in the extended error information field. These types of module errors are typically reported in the controller's I/O status file. See MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 for more information.

## Module Operation and Channel Operation

The module performs operations at two levels:

- Module level
- Channel level

Module-level operations include functions such as power-up, configuration, and communication with the controller.

Internal diagnostics are performed at both levels of operation. Both module hardware and channel configuration error conditions are reported to the controller. Channel overrange or underrange conditions are reported in the module's input data table. Module hardware errors are reported in the controller's I/O status file. See MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 for more information.

When a fault condition is detected, the analog outputs are reset to zero.

## Power-up Diagnostics

At module power-up, a series of internal diagnostic tests are performed.

Table 35 - Module Status LED State Table

| If Module Status LED is Indicated Condition Corrective Action                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------|
| On Proper Operation No action is required.                                                                                             |
| Off Module Fault  Cycle power. If condition persists, replace the module. Call your local distributor or Allen-Bradley for assistance. |

## Critical and Non-critical Errors

Non-critical module errors are recoverable. Channel errors (overrange or underrange errors) are non-critical. Non-critical error conditions are indicated in the module input data table. Non-critical configuration errors are indicated by the extended error code.

Critical module errors are conditions that prevent normal or recoverable operation of the system. When these types of errors occur, the system leaves the run mode of operation.

Critical and non-critical module errors are indicated in Table 38 .

## Module Error Definition Table

Analog module errors are expressed in two fields as four-digit Hex format with the most significant digit as "don't care" and irrelevant. The two fields are "Module Error" and "Extended Error Information". The structure of the module error data is shown in Table 36 .

Table 37 - Module Error Types

| Error Type  Module Error Field Value Bits 11 through 09 (Binary)   | Description                                                                                                                                                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                    | No Errors 000 No error is present. The extended error field holds no additional information.                                                                                                         |
|                                                                    | Hardware Errors 001 General and specific hardware error codes are specified in the extended error information field.                                                                                 |
| Configuration Errors 010                                           | Module-specific error codes are indicated in the extended error field. These error codes correspond to options that you can change directly. For example, the input range or input filter selection. |

## Extended Error Information Field

Check the extended error information field when a non-zero value is present in the module error field. See Table 38 and Table 39 .

<!-- image -->

If no errors are present in the module error field, the extended error information field is set to zero.

## Hardware Errors

General or module-specific hardware errors are indicated by module error code 2. See Table 38 and Table 39 .

## Configuration Errors

If you set the fields in the configuration file to invalid or unsupported values, the module ignores the invalid configuration, generates a non-critical error, and keeps operating with the previous configuration.

Table 38 and Table 39 list the configuration error codes defined for the module.

## Error Codes

Table 38 - Extended Error Codes for 1762-IF2OF2

| Error Type                                            | Error Description                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------------|
| Error Type                                            | No Error X000 000 0 0000 0000 No error                                      |
| General Common Hardware Error                         | X200 001 0 0000 0000 General hardware error; no additional information      |
| General Common Hardware Error                         | X201 001 0 0000 0001 Power-up reset state                                   |
| Hardware-specific Error X210 001 0 0001 0000 Reserved |                                                                             |
| Configuration Error                                   | X400 010 0 0000 0000 General configuration error; no additional information |
| Configuration Error                                   | X401 010 0 0000 0001 Invalid input data format selected (channel 0)         |
| Configuration Error                                   | X402 010 0 0000 0010 Invalid input data format selected (channel 1)         |
| Configuration Error                                   | X403 010 0 0000 0011 Invalid output data format selected (channel 0)        |
| Configuration Error                                   | X404 010 0 0000 0100 Invalid output data format selected (channel 1)        |

Table 39 - Extended Error Codes for 1762-IF4 and 1762-OF4

| Error Type  Module Error Code                         | Hex Equivalent (1) Extended Error Information Code   | Error Description                                                      |
|-------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------|
| Error Type  Module Error Code                         | Binary Binary                                        | Error Description                                                      |
|                                                       | No Error X000 000 0 0000 0000 No error               |                                                                        |
| General Common Hardware Error                         |                                                      | X200 001 0 0000 0000 General hardware error; no additional information |
| General Common Hardware Error                         |                                                      | X201 001 0 0000 0001 Power-up reset state                              |
| Hardware-specific Error X300 001 1 0000 0000 Reserved |                                                      |                                                                        |

.

Table 39 - Extended Error Codes for 1762-IF4 and 1762-OF4 (Continued)

| Error Type          | Error Description                                                      |
|---------------------|------------------------------------------------------------------------|
| Error Type          | Error Description                                                      |
| Configuration Error | X401 010 0 0000 0001 Invalid range select (Channel 0)                  |
| Configuration Error | X402 010 0 0000 0010 Invalid range select (Channel 1)                  |
| Configuration Error | X403 010 0 0000 0011 Invalid range select (Channel 2)                  |
| Configuration Error | X404 010 0 0000 0100 Invalid range select (Channel 3)                  |
| Configuration Error | X405 010 0 0000 0101 Invalid filter select (Channel 0) – 1762-IF4 only |
| Configuration Error | X406 010 0 0000 0110 Invalid filter select (Channel 1) – 1762-IF4 only |
| Configuration Error | X407 010 0 0000 0111 Invalid filter select (Channel 2) – 1762-IF4 only |
| Configuration Error | X408 010 0 0000 1000 Invalid filter select (Channel 3) – 1762-IF4 only |
| Configuration Error | X409 010 0 0000 1001 Invalid format select (Channel 0)                 |
| Configuration Error | X40A 010 0 0000 1010 Invalid format select (Channel 1)                 |
| Configuration Error | X40B 010 0 0000 1011 Invalid format select (Channel 2)                 |
| Configuration Error | X40C 010 0 0000 1100 Invalid format select (Channel 3)                 |

(1) X represents “Don’t Care”.

## Calling Rockwell Automation for Assistance

If you need to contact Rockwell Automation or local distributor for assistance, it is helpful to obtain the following (prior to calling):

- Controller type, series letter, revision letter, and firmware (FRN) number of the controller
- Controller indicator status
- Controller error codes (See MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, Publication 1763-RM001 for error code information.)

## Notes:

## Prepare for Firmware Update

<!-- image -->

## Use ControlFLASH to Upgrade Your Operating System

The operating system (OS) can be upgraded through the communication port on the controller. To download a new operating system, you must have the ControlFLASH™ Upgrade Kit, which is described in the ControlFLASH User Manual, publication 1756-UM105 .

The newer OS firmware for the controller is prepared in DMK disk image format which requires ControlFLASH version 13.00 or later.

To download new OS firmware for a MicroLogix controller, go to the Rockwell Automation Product Compatibility and Download Center (PCDC) at rok.auto/pcdc .

Before upgrading the controller's operating system, you must:

- Install ControlFLASH software on your computer.
- Extract the DMK kit containing the latest firmware (for ControlFLASH version 13.00 or later only).
- Prepare the controller for updating.

## IMPORTANT

Installing a new operating system deletes the user program on the controller. After the operating system upgrade is successful, you must transfer your control program back to the controller. The communication parameters are described in Table 7 .

## Install ControlFLASH Software

To install ControlFLASH properly, see the Install ControlFLASH section in ControlFLASH User Manual, publication 1756-UM105 .

If a ControlFLASH directory does not exist, one is created in your Program Files directory.

## Use DMK Extraction Tool for Firmware Upgrade

This section applies only to the newer OS firmware prepared in DMK format which requires ControlFLASH version 13.00 or later.

1. Launch the DMK Extraction Tool application under Programs &gt; Flash &gt; Programming Tools.
2. Select Browse and choose the location of the DMK file in the system.
3. Select OK.
4. Select one or more DMK files that you want to extract, then select Extract. The DMK Extraction Progress dialog box appears.
5. After the extraction is complete, select OK to close the dialog box.
6. Select Cancel to close the DMK Extraction Tool.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Sequence of Operation

Once the DMK files have been extracted from a folder, they are no longer shown when the DMK Extraction Tool is used again to browse the same folder.

<!-- image -->

## Prepare the Controller for Firmware Update

Connect the computer COM port to channel 0 on the MicroLogix 1100 using a 1761-CBL-PM02 cable.

Controller Configuration

The controller must be configured for default communications (use the Communications Toggle functionality which is available on the LCD; DCOMM indicator on) and be in the Program mode (use the Mode Switch which is available on the LCD.) to allow the download of a new operating system.

See Use the Communications Toggle Functionality on page 52 for information about how to use the Communications Toggle functionality.

See Use the Mode Switch on page 88 for information about controller modes and how to use the Mode Switch.

The following steps detail the key events in the upgrade process.

1. Controller mode and communications parameters are checked. The screen as shown below is displayed on the LCD as well.
2. Download begins.

<!-- image -->

## Missing or Corrupt OS LED Pattern

3. During the download, the Run, Force, and Fault LEDs perform a walking bit pattern. The screen as shown below is displayed on the LCD as well.
4. When the download is complete, the integrity of the new OS is checked. If the new OS is corrupt, the controller sends an error message to the download tool and flashes the Missing or Corrupt OS LED pattern. See Missing or Corrupt OS LED Pattern on page 144 below.
5. Following a successful transfer, the Run, Force, and Fault LEDs flash on and remain on for five seconds. Then the controller resets.

<!-- image -->

When an operating system download is not successful or if the controller does not contain a valid operating system, the controller flashes the Run, Force, and Fault LEDs on and off.

## RS-232 Communication Interface

## RS-485 Communication Interface

## DF1 Full-duplex Protocol

<!-- image -->

## Connect to Networks via RS-232/RS-485 Interface

The following protocols are supported from the RS-232/RS-485 communication channel (Channel 0):

- DF1 Full-duplex
- DF1 Half-duplex master/slave
- DF1 Radio modem
- DH-485
- Modbus RTU master/slave
- ASCII

The communications port on the MicroLogix 1100 controller utilizes a combined RS-232/RS-485 interface. RS-232 and RS-485 are Electronics Industries Association (EIA) standards that specify the electrical and mechanical characteristics for serial binary communication. They provide various system configuration possibilities. RS-232 and RS-485 define electrical connection characteristics, not protocols.

One of the biggest benefits of an RS-232 interface is that it lets you integrate telephone and radio modems into your control system (using the appropriate DF1 protocol only, not DH-485 protocol), but it is for point-to-point connections only between two devices.

The RS-485 interface supports connection of up to 32 devices in a multidrop hard-wired configuration using DH-485, DF1 Half-duplex (a) , or Modbus protocols. Also, the RS-485 interface supports connection in a multidrop hard-wired configuration using ASCII protocols.

DF1 Full-duplex protocol provides a point-to-point connection between two devices. DF1 Fullduplex protocol combines data transparency (American National Standards Institute ANSI X3.28-1976 specification subcategory D1) and 2-way simultaneous transmission with embedded responses (subcategory F1).

MicroLogix 1100 controllers support the DF1 Full-duplex protocol via RS-232 connection to external devices, such as computers, or other controllers that support DF1 Full-duplex.

DF1 is an open protocol. See the DF1 Protocol and Command Set Reference Manual, publication 1770-RM516, for more information.

DF1 Full-duplex protocol (also referred to as DF1 point-to-point protocol) is useful where RS-232 point-to-point communication is required. DF1 protocol controls message flow, detects and signals errors, and retries if errors are detected.

## Example DF1 Full-Duplex Connections

For information about required network connecting equipment, see Communication Connections on page 51 .

## DF1 Half-duplex Protocol

Figure 91 - Example of DF1 Full-duplex Connections

<!-- image -->

DF1 Half-duplex protocol is a multi-drop single master/multiple slave network. DF1 Half-duplex protocol supports data transparency (American National Standards Institute ANSI - X3.28-1976 specification subcategory D1). In contrast to DF1 Full-duplex, communication takes place in one direction at a time. You can use the RS-232/RS-485 port on the MicroLogix 1100 controller as both a half-duplex programming port and a half-duplex peer-to-peer messaging port.

## DF1 Half-duplex Operation

A DF1 Half-duplex master device initiates all communication by polling each slave device. The slave device can only transmit when it is polled by the master. It is the master's responsibility to poll each slave on a regular and sequential basis to allow slave devices an opportunity to communicate.

An additional feature of the DF1 Half-duplex protocol is that it is possible for a slave device to enable a MSG write or read to/from another slave. When the initiating slave is polled, the MSG is sent to the master. The master recognizes that the message is not intended for it, but for another slave, so the master immediately forwards the message to the intended slave. The master does this automatically; you do not need to program the master to move data between slave nodes. This slave-to-slave transfer can also be used by programming software to allow slave-to-slave upload and download of programs to processors (including the master) on the DF1 Half-duplex link.

A MicroLogix 1100 controller can act as the master or as a slave on a Half-duplex network. When the MicroLogix 1100 controller is a slave device, a master device is required to run the network. Several other Allen-Bradley products support the DF1 Half-duplex master protocol. They include the SLC 5/03 and higher processors, enhanced PLC-5 processors, MicroLogix 1200 or MicroLogix 1500 controllers, and RSLinx software (version 2.x or later).

DF1 Half-duplex supports up to 255 devices (address 0…254) with address 255 reserved for master broadcasts. As a DF1 Half-duplex slave device, the MicroLogix 1100 controller supports broadcast reception. As a DF1 Half-duplex master, the MicroLogix 1100 controller supports both the reception and initiation of broadcast write commands (via the MSG instruction). The MicroLogix 1100 controller also supports Half-duplex modems using RTS/CTS hardware handshaking.

Figure 92 - Example of DF1 Half-duplex Connections

<!-- image -->

## Considerations When Communicating as a DF1 Slave on a Multi-drop Link

When communication is between either your programming software and a MicroLogix Programmable Controller or between two MicroLogix 1100 Programmable Controllers via slaveto-slave communication on a larger multi-drop link, the devices depend on a DF1 Half-duplex master to give each of them access in a timely manner. As the number of slave devices increase, the time between when slave devices are polled also increases. This increase in time may also be large if you are using low communication rates. As these time periods grow, consider increasing the poll timeout and reply timeout values for slave devices.

## IMPORTANT

If a program download is started when using DF1 Half-duplex, but then is interrupted due to electromagnetic interference or other events, discontinue communications to the controller for the ownership timeout period and then restart the program download. The ownership timeout period is 60 seconds. After the timeout, you can re-establish communications with the processor and try the program download again. The only other way to remove program ownership is to cycle power on the processor.

## Use Modems with MicroLogix Programmable Controllers

The types of modems you can use with MicroLogix controllers include the following:

- Dial-up phone modems

A MicroLogix controller, on the receiving end of the dial-up connection, can be configured for DF1 Full-duplex protocol with or without handshaking. The modem connected to the MicroLogix controller should support auto-answer. The MicroLogix 1100 controller supports ASCII out communications. Therefore, it can cause a modem to initiate or disconnect a phone call.

- Leased-line modems

Leased-line modems are used with dedicated phone lines that are typically leased from the local phone company. The dedicated lines can be in a point-to-point topology to support full-duplex communications between two modems or in a multi-drop topology to support half-duplex communications between three or more modems.

- Radio modems

Radio modems can be implemented in a point-to-point topology to support either halfduplex or full-duplex communications, or in a multi-drop topology to support half-

## DH-485 Communication Protocol

duplex communications between three or more modems. MicroLogix 1100 controllers also support the DF1 Radio Modem protocol.

- Line drivers

Line drivers, also called short-haul modems, do not actually modulate the serial data, but rather condition the electrical signals to operate reliably over long transmission distances (up to several miles). Line drivers are available in full-duplex and half-duplex models. Allen-Bradley's AIC+ Advanced Interface Converter is a half-duplex line driver that converts an RS-232 electrical signal into an RS-485 electrical signal, increasing the signal transmission distance from 15…1219 m (50…4000 ft.), 2438 m (8000 ft.) when bridged.

For point-to-point full-duplex modem connections that do not require any modem handshaking signals to operate, use DF1 Full-duplex protocol with no handshaking. For pointto-point Full-duplex modem connections that require RTS/CTS handshaking, use DF1 Fullduplex protocol with handshaking.

For radio modem connections, use DF1 Radio Modem protocol, especially if store and forward capability is required.

For general multi-drop modem connections, or for point-to-point modem connections that require RTS/CTS handshaking, use DF1 Half-duplex slave protocol. In this case, one (and only one) of the other devices must be configured for DF1 Half-duplex master protocol.

## IMPORTANT

Never attempt to use DH-485 protocol through modems under any circumstance.

<!-- image -->

All MicroLogix controllers support RTS/CTS modem handshaking when configured for DF1 Full-duplex protocol with the control line parameter set to Full-duplex Modem Handshaking or DF1 Half-duplex slave protocol with the control line parameter set to "Half-Duplex Modem". No other modem handshaking lines (for instance, Data Set Ready and Data Terminal Ready) are supported by MicroLogix 1100 controller. MicroLogix 1100 controller also does not support DCD (Data Carrier Detect).

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

Table 40 - DF1 Full-Duplex Configuration Parameters

| Parameter Options              |
|--------------------------------|
| Communication Rate 9600, 19.2K |
| Node Address 1…31 decimal      |
| Token Hold Factor 1…4          |

See Software Considerations on page 150 for tips on setting the parameters listed above.

## Devices that use the DH-485 Network

In addition to the MicroLogix controllers, the devices that are shown in Table 41 also support the DH-485 network.

Table 41 - Devices that Support a DH-485 Network

| Catalog Number Description Installation Function Publication                                                                       |                                                    |                                                                                                                                                                                                   |                                  |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
|                                                                                                                                    |                                                    | Bulletin 1762 MicroLogix 1200 Series A or later These controllers support DH-485 communications.                                                                                                  | 1762-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1764 MicroLogix 1500 Series A or later These controllers support DH-485 communications.                                                                                                  | 1764-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1766 MicroLogix 1400 Series A or later These controllers support DH-485 communications.                                                                                                  | 1766-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1747 Processors SLC 500 Processors SLC Chassis These processors support a variety of I/O requirements and functionality.                                                                 | 1747-UM011                       |
|                                                                                                                                    | 1746-BAS BASIC Module SLC Chassis                  | Provides an interface for SLC 500 devices to foreign devices. Program in BASIC to interface the 3 channels (2 RS232 and 1 DH-485) to printers, modems, or the DH-485 network for data collection. | 1746-UM004 1746-PM001 1746-RM001 |
|                                                                                                                                    |                                                    | 1784-KTX, 1784-KTXD PC DH-485 IM PCI Computer Bus Provides DH-485 using RSLinx software                                                                                                           | 1784-UM527                       |
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

The maximum length of the communication cable is 1219 m (4000 ft.). This is the total cable distance from the first node to the last node in a segment. However, two segments can be used to extend the DH-485 network to 2438 m (8000 ft.). For additional information on connections using the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

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

## IMPORTANT

Set all devices to the same maximum node address.

## MicroLogix Remote Packet Support

MicroLogix controllers can respond and initiate with communications (or commands) that do not originate on the local DH-485 network. This is useful in installations where communication is needed between DH-485 and DH+™ networks.

The example below shows how to send messages from a device on the DH+ network to a MicroLogix controller on the DH-485 network. This method uses an SLC 5/04 processor as the bridge connection.

When using this method (as shown in the illustration below):

- PLC-5 devices can send read and write commands to MicroLogix controllers.
- MicroLogix controllers can respond to MSG instructions received.
- MicroLogix controllers can initiate MSG instructions to devices on the DH+ network.
- The computer can send read and write commands to MicroLogix controllers.
- The computer can do remote programming of MicroLogix controllers.

<!-- image -->

Use a 1763-NC01 series A or later cable to connect a MicroLogix 1100 controller to a DH-485 network.

You can connect a MicroLogix 1100 controller to your DH-485 network directly without using a RS-232 to RS-485 converter and optical isolator, such as the AIC+ Advanced Interface Converter, 1761-NET-AIC, as shown in Figure 94, because Channel 0 has isolation and RS-485 built-in.

Figure 93 - Communication Between DH-485 and DH+ Networks with MicroLogix Controllers

<!-- image -->

## Example DH-485 Connections

The following network diagrams provide examples of how to connect MicroLogix controllers to the DH-485 network. You can connect a MicroLogix 1100 controller to your DH-485 network directly without using a RS-232 to RS-485 converter and optical isolator, such as the AIC+ Advanced Interface Converter, 1761-NET-AIC, as shown in Figure 94, because Channel 0 has isolation and RS-485 built-in.

However, you can use an AIC+ to connect other controllers to a DH-485 network.

Figure 94 - DH-485 Network with a MicroLogix 1100 Controller

<!-- image -->

<!-- image -->

This 3-node network is not expandable.

## Modbus Communication Protocol

## ASCII

Modbus is a Half-Duplex, master-slave communications protocol. The Modbus network master reads and writes coils and registers. Modbus protocol allows a single master to communicate with a maximum of 247 slave devices. MicroLogix 1100 controllers support Modbus RTU saster and Modbus RTU slave protocol.

For more information on how to configure your MicroLogix 1100 controller for Modbus protocol, see the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001. For more information about the Modbus protocol, see the Modbus Protocol Specifications (available from www.modbus.org).

ASCII provides connection to other ASCII devices, such as barcode readers, weigh scales, serial printers, and other intelligent devices.

You can use ASCII by configuring the RS-232/RS-485 port, channel 0 for the ASCII driver. For detailed configuration information, see the MicroLogix 1100 Programmable Controllers Instruction Set Reference Manual, publication 1763-RM001 .

## MicroLogix 1100 Controllers and Ethernet Communication

## MicroLogix 1100 Performance Considerations

<!-- image -->

## Connect to Networks via Ethernet Interface

Ethernet is a local area network that provides communication between various devices at 10…100 Mbps. The physical communication media options for the MicroLogix 1100 controllers are:

- Built-in
- Twisted-pair (10/100Base-T)
- With media converters or hubs
- Fiber optic
- Broadband
- Thick-wire coaxial cable (10Base-5)
- Thin-wire coaxial cable (10Base-2)

The MicroLogix 1100 controller supports Ethernet communication via the Ethernet communication channel 1 shown.

<!-- image -->

Actual performance of an MicroLogix 1100 controller varies according to:

- Size of Ethernet messages
- Frequency of Ethernet messages
- Network loading
- Implementation of and performance of your processor application program

Table 42 - Optimal Performance: RSLinx Software to MicroLogix 1100 Series A OS FRN 3 Controller (2-node Ethernet network)

|                                | Operation Words MSG per Second Words per Second   |
|--------------------------------|---------------------------------------------------|
| Single Typed Read 1 20 20      |                                                   |
| Single Typed Reads 20 20 400   |                                                   |
| Single Typed Reads 100 20 2000 |                                                   |

Table 43 - Optimal Performance: MicroLogix 1100 FRN 3 to MicroLogix 1100 Series A OS FRN 3 Controller (2-node Ethernet network)

|                                 | Operation Words MSG per Second Words per Second   |
|---------------------------------|---------------------------------------------------|
| Single Typed Read 1 11 11       |                                                   |
| Single Typed Reads 20 11 220    |                                                   |
| Single Typed Reads 100 11 1,100 |                                                   |

## MicroLogix 1100 and Computer Connections to the Ethernet Network

Table 44 - Optimal Performance: RSLinx Software to MicroLogix 1100 Series B OS FRN 4 Controller

|                                 | Operation Words MSG per Second Words per Second   |
|---------------------------------|---------------------------------------------------|
| Single Typed Read 1 50 50       |                                                   |
| Single Typed Reads 20 50 2,500  |                                                   |
| Single Typed Reads 100 50 5,000 |                                                   |

Table 45 - Optimal Performance: MicroLogix 1100 Series A OS FRN 3 to MicroLogix 1100 Series B OS FRN 4 Controller

|                                 | Operation Words MSG per Second Words per Second   |
|---------------------------------|---------------------------------------------------|
| Single Typed Read 1 18 18       |                                                   |
| Single Typed Reads 20 18 360    |                                                   |
| Single Typed Reads 100 18 1,800 |                                                   |

Table 46 - Optimal Performance: MicroLogix 1100 Series B OS FRN 4 to MicroLogix 1100 Series B OS FRN 4 Controller

|              | Operation Words MSG per Second Words per Second   |
|--------------|---------------------------------------------------|
| 1 20 20      | Single Typed Read                                 |
| 20 20 400    | Single Typed Reads                                |
| 100 20 2,000 | Single Typed Reads                                |

The MicroLogix 1100 Ethernet connector conforms to ISO/IEC 8802-3 STD 802.3 and utilizes 10/100Base-T media. Connections are made directly from the MicroLogix 1100 controller to an Ethernet hub or switch. The network setup is simple and cost effective. Typical network topology is shown in Figure 96 .

Figure 96 - Ethernet Network Topology

<!-- image -->

## IMPORTANT

The MicroLogix 1100 controller contains a 10/100Base-T RJ45 Ethernet connector, which connects to standard Ethernet hubs or switches via 8-wire twisted-pair straight-through cable. To access other Ethernet mediums, use 10/100Base-T media converters or Ethernet hubs or switches that can be connected together via fiber, thin-wire, or thickwire coaxial cables, or any other physical media commercially available with Ethernet hubs or switches.

## Connect an Ethernet switch on the Ethernet Network

The MicroLogix 1100 Ethernet port supports the following Ethernet settings:

- 10 Mbps half-duplex or full-duplex
- 100 Mbps half-duplex or full-duplex

Mode selection can be automatic, based on the IEEE 802.3 auto negotiation protocol. In most cases, using the auto negotiation function results in proper operation between a switch port and MicroLogix 1100 Ethernet port.

With RSLogix500 programming software version 7.00.00 or later, you can manually set the communication rate and duplex mode of an Ethernet port you have connected to the switch port. The settings of the Ethernet port and the switch port must match.

## IMPORTANT

## Cables

Shielded and non-shielded twisted-pair 10/100Base-T cables with RJ45 connectors are supported. The maximum cable length between a MicroLogix 1100 Ethernet port and a 10/100Base-T port on an Ethernet hub or switch (without repeaters or fiber) is 100 m (323 ft.). However, in an industrial application, keep the cable length to a minimum.

<!-- image -->

The Ethernet cabling with straight-through method is recommended as shown in Table 47. Do not make the incorrect connection.

Table 47 - Straight-through Cabling

| Pin Pin Name Cable Color               |
|----------------------------------------|
| 1 Tx+ Orange/white                     |
| 2 Tx- Orange                           |
| 3 Rx+ Green/white                      |
| 4 Not used by 10/100Base-T Blue        |
| 5 Not used by 10/100Base-T Blue/white  |
| 6 Rx- Green                            |
| 7 Not used by 10/100Base-T Brown/white |
| 8 Not used by 10/100Base-T Brown       |

The standard Ethernet cable is terminated in accordance with EIA/TIA 568B on both ends. The crossover cable is terminated to EIA/TIA 568B at one end and EIA/TIA 568A at the other, exactly as shown in Figure 97 .

Figure 97 and Figure 98 show how the TIA/EIA 568A and 568B are to be terminated. There are four pairs of wires contained in a CAT5 UTP cable. These pairs of cables are color-coded white blue/blue, white orange/orange, white green/green, and white brown/brown. They are also numbered one to four in the order shown.

Figure 97 - EIA/TIA 568A and 568B Ethernet Cable

<!-- image -->

When connecting the MicroLogix 1100 Ethernet port to a 10/100Base-T Ethernet switch, note the following recommendations:

- Use the auto negotiation function for both the switch port and the MicroLogix 1100 Ethernet port.
- If you want to force to a specific speed/duplex mode, you should force the MicroLogix 1100 Ethernet port and leave the switch in auto negotiation mode to match speed/duplex settings of the MicroLogix 1100 Ethernet port.
- If you want to disable the auto negotiation function for both ports, then you should only force both the switch and the MicroLogix 1100 port to either 100 Mbps half-duplex or 10 Mbps half-duplex. If you attempt to force both the switch and the MicroLogix1100 port to either 100 Mbps full-duplex or 10 Mbps full-duplex, the Ethernet link does not establish and Ethernet communications does not work.

## Ethernet Connections

Figure 98 - EIA/TIA 568A and 568B Cable Termination

<!-- image -->

<!-- image -->

The most common wiring for RJ45 cables is the straight-through cable that means that pin 1 of the plug on one end is connected to pin 1 of the plug on the other end. The straight-through RJ45 cable is commonly used to connect network cards with hubs on 10Base-T and 100Base-Tx networks. On network cards, pair 1…2 is the transmitter, and pair 3…6 is the receiver. The other two pairs are not used. On hubs pair 1…2 is the receiver and 3…6 the transmitter. Wire your cables with the same color sequence. In this cable layout, all pins are wired one-to-one to the other side. The pins on the RJ45 connector are assigned in pairs, and every pair carries one differential signal. Each line pair has to be twisted.

In small network where only two Ethernet devices must be connected together, a crossover RJ45 cable is necessary, where the transmit and receive lines on both RJ45 connectors are cross connected. The color coding for the crossover RJ45 cable have been defined in the EIA/TIA 568A standard. In a crossover cable layout, remember that one end is normal, and the other end has the crossover configuration.

TCP/IP is the mechanism used to transport Ethernet messages. On top of TCP, EtherNet/IP protocol is required to establish sessions and to send the MSG commands. You can initiate connections by either a client program (RSLinx software) or a processor.

The client program or processor must first establish a connection to the MicroLogix 1100 controller to enable the controller to receive solicited messages from a client program or another processor.

To send an outgoing message, the MicroLogix 1100 controller must first establish a connection with the destination node at a specified IP address on the Ethernet network. A connection is established when a MSG instruction executes and no previous connection exists.

When a MSG instruction executes, the MicroLogix 1100 controller checks to see whether a connection has been established with the destination node. If a connection has not been established, the MicroLogix 1100 controller attempts to establish a connection of the peer type.

To receive messages from another device on Ethernet, an incoming connection must be established. This incoming connection is made by the sending processor and uses one incoming connection in the receiving processor.

The MicroLogix 1100 controller supports a maximum of 32 connections, allowing a maximum of 16 outgoing and a maximum of 16 incoming simultaneous connections with up to 32 other devices or applications. The connections are dedicated as follows:

| Number of Connections(1) Dedicated to   |
|-----------------------------------------|
| 16 Outgoing connections                 |
| 16 Incoming connections                 |

## Duplicate IP address Detection

## Configure the Ethernet Channel on the MicroLogix 1100 Controller

Table 48 - Ethernet Configuration Parameters

|                       | Parameter Description                                                                                                                                                                                                                                     |                           | Default Status   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|------------------|
|                       | Hardware Address The MicroLogix 1100 controller Ethernet hardware address                                                                                                                                                                                 | Ethernet hardware address | Read-only        |
| IP Address            | The MicroLogix 1100 controller Internet address (in network byte order). The Internet address must be specified to connect to the TCP/IP network.                                                                                                         | 0 (undefined) Read/write  |                  |
| Subnet Mask           | The MicroLogix 1100 controller subnet mask (in network byte order). The subnet mask is used to interpret IP addresses when the Internet is divided into subnets. A subnet mask of all zeros indicates that no subnet mask has been configured.            | 0 (undefined) Read/write  |                  |
| Gateway Address       | The address of a gateway (in network byte order) that provides connection to another IP network. A gateway address of all zeros indicates that no gateway has been configured.                                                                            | 0 (undefined) Read/write  |                  |
| Default Domain Name   | The default domain name can have the following formats: ’a.b.c’, ’a.b’ or ’a’, where a, b, c must start with a letter, end with a letter or digit, and have as interior characters only letters, digits, or hyphens. The maximum length is 63 characters. | NULL (undefined)          | Read/write       |
| Primary Name Server   | The IP address of the computer acting as the local Ethernet network Primary Domain Name System (DNS) server                                                                                                                                               | 0 (undefined) Read/write  |                  |
| Secondary Name Server | The IP address of the computer acting as the local Ethernet network Secondary Domain Name System (DNS) server.                                                                                                                                            | 0 (undefined) Read/write  |                  |

## IMPORTANT

For outgoing connections, no more that one connection per destination node is established. If multiple MSG instructions use the same destination node, they share the same connection.

The MicroLogix 1100 controller series B firmware supports duplicate IP address detection.

When you change the IP address or connect one of the MicroLogix controllers to an EtherNet/IP network, the MicroLogix 1100 controller checks to make sure that the IP address that is assigned to this device does not match the address of any other network device. The MicroLogix 1100 controller checks every 2 minutes for a duplicate IP address on the network. If the MicroLogix 1100 controller determines that there is a conflict (another device on the network with a matching IP address), the following message is posted on the LCD display.

<!-- image -->

To correct this conflict, use the instructions in this chapter to change the IP address of the EtherNet/IP device. Then cycle power to the device or reset the device (such as disconnecting the Ethernet cable and reconnecting the cable).

There is also the possibility that two EtherNet/IP devices can detect a conflict simultaneously. If this occurs, remove the device with the incorrect IP address or correct its conflict. To get the second device out of conflict mode, cycle power to the module or disconnect its Ethernet cable and reconnect the cable. The MicroLogix 1100 controller checks every 2 minutes for a duplicate IP address on the network.

There are two ways to configure the MicroLogix 1100 Ethernet channel 1.

- With a BOOTP or DHCP request at controller power-up
- Manually setting the configuration parameters using RSLogix 500 programming software

The configuration parameters are shown in Table 48 .

Table 48 - Ethernet Configuration Parameters (Continued)

|                                    | Parameter Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Default Status                                                                           |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| BOOTP Enable                       | The BOOTP enable switch. When BOOTP is enabled, the MicroLogix 1100 controller attempts to learn its network related parameters at power-up via a BOOTP request. There must be a BOOTP server on the network capable of responding to this BOOTP request. When both BOOTP and DHCP are disabled, the MicroLogix 1100 controller uses the locally configured network-related parameters (IP address, subnet mask, broadcast address, and so on).                                                                                    | 1 (enabled) Read/write                                                                   |
| DHCP Enable                        | The DHCP auto configuration enable switch. When DHCP is enabled, a DHCP server automatically assigns network-related parameters to the MicroLogix 1100 controller when it signs in a TCP/IP network. There must be a DHCP server on the network capable of allocating network addresses and configuring parameters to newly attached device. When both BOOTP and DHCP are disabled, the MicroLogix 1100 controller uses the locally configured network-related parameters (IP address, subnet mask, broadcast address, and so on). | 0 (disabled) Read/write                                                                  |
| SNMP Server Enable                 | The SNMP enable switch. Select to enable SNMP (Simple Network Management Protocol). Not applicable to the MicroLogix 1100 controller.                                                                                                                                                                                                                                                                                                                                                                                              | 0 (disabled) Read/write                                                                  |
| SMTP Client Enable (Series B only) | The SMTP Client service enable switch. When SMTP is enabled, the MicroLogix 1100 controller is capable of transmitting email messages that are generated by a 485CIF write message with a string element. There must be an SMTP process email service. This provides a versatile mechanism to report alarms, status, and other data-related functions.                                                                                                                                                                             | 0 (disabled) Read/write                                                                  |
| Auto Negotiate and Port Setting    | When Auto Negotiate is disabled (unchecked), the Ethernet speed/duplex is forced to either 10 Mbps/Half duplex, 10 Mbps/Full-duplex, 100 Mbps/Half-duplex, or 100 Mbps/Full-duplex, as selected in the Port Setting field. When Auto Negotiate is enabled (checked), the Port Setting field allows you to select the range of speed/duplex settings that the MicroLogix 1100 controller negotiates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Auto Negotiate enabled and Port Setting. 10/100 Mbps Full-duplex/ Half-duplex Read/write |
| MSG Connection Timeout             | The amount of time (in ms) allowed for a MSG instruction to establish a connection with the destination node. The MSG Connection Timeout has 250 ms resolution and a range from 250…65,500.                                                                                                                                                                                                                                                                                                                                        | 15,000 ms Read/write                                                                     |
| MSG Reply Timeout                  | The amount of time (in ms) that the MicroLogix 1100 controller will wait for a reply to a command that it has initiated via a MSG instruction. The MSG Reply Timeout has 250 ms resolution and a range from 250…65,500.                                                                                                                                                                                                                                                                                                            | 3,000 ms Read/write                                                                      |
| Inactivity Timeout (Series B only) | The amount of time (in minutes) that a MSG connection could remain inactive before it is ended. The Inactivity Timeout has a 1 minute resolution and a range from 1…65,500 minutes.                                                                                                                                                                                                                                                                                                                                                | 30 minutes Read/write                                                                    |

## Configure Using RSLogix 500 Programming Software

## Configure Using BOOTP

See the online documentation provided with your programming software.

Bootstrap protocol (BOOTP) is a low-level protocol that TCP/IP nodes use to obtain startup information. By default, the MicroLogix 1100 controller broadcasts BOOTP requests at powerup. The BOOTP Valid parameter remains clear until a BOOTP reply has been received. BOOTP lets you dynamically assign IP addresses to processors on the Ethernet Link.

To use BOOTP, a BOOTP server must exist on the local Ethernet subnet. The server is a computer that has BOOTP server software installed and reads a text file containing network information for individual nodes on the network.

The host system's BOOTP configuration file must be updated to service requests from MicroLogix 1100 controllers. The parameters in Table 49 must be configured.

Table 49 - Configuration Parameters

|             | Parameter Description                                                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|             | IP Address A unique IP Address for the MicroLogix 1100 controller                                                                          |
| Subnet Mask | Specifies the net and local subnet mask as per the standard on subnetting RFC 950, Internet Standard Subnetting Procedure                  |
| Gateway     | Specifies the IP address of a gateway on the same subnet as the MicroLogix 1100 controller that provides connections to another IP network |

When BOOTP is enabled, the following events occur at power-up:

- The processor broadcasts a BOOTP-request message containing its hardware address over the local network or subnet.
- The BOOTP server compares the hardware address with the addresses in its look-up table.
- The BOOTP server sends a message back to the processor with the IP address and other network information that corresponds to the hardware address it received.

With all hardware and IP addresses in one location, you can easily change IP addresses in the BOOTP configuration file if your network must be changed.

The BOOTP request can be disabled by clearing the BOOTP Enable parameter in the channel configuration file. When both BOOTP Enable and DHCP are cleared (disabled), the MicroLogix 1100 controller uses the existing channel configuration data.

## IMPORTANT

If BOOTP is disabled, or no BOOTP server exists on the network, you must use RSLogix 500 programming software to enter/change the IP address for each processor or you must use DHCP instead of it.

## Using the Rockwell Automation BOOTP/DHCP Utility

The Rockwell Automation BOOTP/DHCP server utility is a standalone program that incorporates the functionality of standard BOOTP software with a user-friendly graphical interface. It is located in the Utils directory on the RSLogix 500 installation CD.

The newest version of the utility can be downloaded from the Product Compatibility and Download Center (PCDC) at rok.auto/pcdc. The device must have BOOTP enabled (factory default) or DHCP enabled to use the utility.

To configure your device using the BOOTP utility, perform the following steps.

1. Run the BOOTP/DHCP server utility software. It asks you to configure your network settings before using the BOOTP/DHCP server tool. Enter your Ethernet settings for Subnet Mask and Gateway. If you are not sure about it, get help from your system administrator. Just leave Primary DNS, Secondary DNS, and Domain Name. If the corresponding information is allocated to the computer where the BOOTP/DHCP server utility is installed, enter the same information.)
2. In the Request History panel, you see the hardware addresses of devices that issue BOOTP or DHCP requests.

<!-- image -->

<!-- image -->

## Use a DHCP Server To Configure Your Processor

## Subnet Masks and Gateways

3. Double-click the hardware address of the device that you want to configure. You see the New Entry pop-up window with the device's Ethernet Address (MAC).
4. Enter the IP Address and Description that you want to assign to the device, and select OK. Leave Hostname blank.

<!-- image -->

The device is added to the Relation List, and displays the Ethernet Address (MAC) and corresponding IP Address, Subnet Mask, and Gateway (if applicable).

<!-- image -->

A DHCP server automatically assigns IP addresses to client stations signing onto a TCP/IP network. DHCP is based on BOOTP and maintains some backward compatibility. The main difference is that BOOTP was designed for manual configuration, while DHCP allows for dynamic allocation of network addresses and configurations to newly attached devices.

<!-- image -->

ATTENTION: The processor must be assigned a fixed network address. The IP address of the processor must not be dynamically provided. Failure to observe this precaution may result in unintended machine motion or loss of process control.

Configure subnet masks and gateways using the Ethernet Channel 1 configuration screen.

## IMPORTANT

If BOOTP is enabled, you can't change any of the advanced Ethernet communications characteristics.

If your network is divided into subnetworks that use gateways or routers, you must indicate the following information when configuring Channel 1:

- Subnet mask
- Gateway address

A subnet mask is a filter that a node applies to IP addresses to determine if an address is on the local subnet or on another subnet. If an address is located on another subnetwork, messages are routed through a local gateway to be transferred to the destination subnetwork.

If your network is not divided into subnets, then leave the subnet mask field at the default.

|                                                                  | If you Then                                                                                                                    |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Manually configure Channel 1 and have a network with subnets     | • Verify that the BOOTP enable field is disabled • Use your programming software to enter the subnet mask and gateway address. |
| Use BOOTP to configure Channel 1 and have a network with subnets | • Verify that BOOTP is enabled • Include the subnet masks and gateway addresses                                                |

## Manually Configuring Channel 1 for Controllers on Subnets

If you manually configure Channel 1 for a MicroLogix 1100 controller on a subnet, clear the checkbox for both of the "BOOTP Enable" and "DHCP Enable" options, as shown in Figure 99 .

Figure 99 - Channel Configuration Example

<!-- image -->

See Table 50 to configure the subnet mask and gateway address fields for each controller via your programming software.

Table 50 - Subnet Mask and Gateway Address Fields

|                 |                                                                                                                                                                       | This field Specifies Configure by Doing the Following                                                                                                                                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Subnet Mask     | The controller’s subnet mask. The subnet mask is used to interpret IP addresses when the Internet is divided into subnets.                                            | Enter an address of the following form: a.b.c.d Where: a, b, c, d are between 0...255 (decimal) If your network is not divided into subnets, then leave the subnet mask field at the default. If you change the default and must reset it, type 0.0.0.0. |
| Gateway Address | The IP address of the gateway that provides a connection to another IP network. This field is required when you communicate with other devices not on a local subnet. | Enter an address of the following form: a.b.c.d Where: a, b, c, d are between 0...255 (decimal) The default address is No Gateway.                                                                                                                       |

## MicroLogix 1100 Embedded Web Server Capability

MicroLogix 1100 controllers include not only the embedded web server that allows viewing of module information, TCP/IP configuration, and diagnostic information, but the capabilities that also allow viewing of the data file via Ethernet using a standard web browser.

For more information on MicroLogix 1100 embedded web server capability, see the MicroLogix 1100 Embedded Web Server User Manual, publication 1763-UM002 .

## Notes:

## System Loading Calculations

<!-- image -->

## System Loading and Heat Dissipation

<!-- image -->

A maximum of four 1762 expansion I/O modules, in any combination, can be connected to a MicroLogix 1100 controller. You can use this appendix to determine the power supply load and heat dissipation for your system.

The MicroLogix 1100 controller is designed to support up to any four 1762 expansion I/O modules.

When you connect MicroLogix accessories and expansion I/O, an electrical load is placed on the controller power supply. This section shows how to calculate the load of your control system.

The following example is provided to illustrate system loading calculation. The system calculation procedure accounts for the amount of 5V DC and 24V DC current that is consumed by the controller, expansion I/O, and user-supplied equipment. Use the System Loading Worksheet on page 166 to calculate your controller configuration.

## System Loading Example Calculations

Current Loading

Table 51 - Calculating the Current for Expansion I/O

|                                                | n A B n x A n x B                                     |                                                      |
|------------------------------------------------|-------------------------------------------------------|------------------------------------------------------|
| Catalog Number (1)                             | Device Current Requirements (max) Calculated Current  | Device Current Requirements (max) Calculated Current |
| Number of Modules                              | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                      |
| 1762-IA8 2 50 0 100 0                          |                                                       |                                                      |
| 1762-IF4 40 50                                 |                                                       |                                                      |
| 1762-IF2OF2 40 105                             |                                                       |                                                      |
| 1762-IQ8 50 0                                  |                                                       |                                                      |
| 1762-IQ16  70(2)                               | 0                                                     |                                                      |
| 1762-IQ32T 170 0                               |                                                       |                                                      |
| 1762-IR4 40 50                                 |                                                       |                                                      |
| 1762-IT4 40 50                                 |                                                       |                                                      |
| 1762-OA8 115 0                                 |                                                       |                                                      |
| 1762-OB8 115 0                                 |                                                       |                                                      |
| 1762-OB16 175 0                                |                                                       |                                                      |
| 1762-OB32T 175 0                               |                                                       |                                                      |
| 1762-OF4 40 165                                |                                                       |                                                      |
| 1762-OV32T 175 0                               |                                                       |                                                      |
| 1762-OW8 2 80 90 160 180                       |                                                       |                                                      |
| 1762-OW16  140(2)                              | 180(2)                                                |                                                      |
| 1762-OX6I 110 110                              |                                                       |                                                      |
| 1762-IQ8OW6 110 80                             |                                                       |                                                      |
| Total Modules (4 maximum): 4 Subtotal: 260 180 |                                                       |                                                      |

## Validate the System

The example systems shown in Table 52 and Table 53 are verified to be acceptable configurations. The systems are valid because:

- Calculated Current Values &lt; Maximum Allowable Current Values
- Calculated System Loading &lt; Maximum Allowable System Loading

Table 52 - Validating Systems using 1763-L16AWA, 1763-L16BBB, or 1763-L16DWD

| Maximum Allowable Values Calculated Values                                            |                                                                                                 |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Current Current (Subtotal from Table 51)                                              |                                                                                                 |
|                                                                                       | 800 mA @ 5V DC 700 mA @ 24V DC 0 mA + 260 mA = 260 mA @ 5V DC 120 mA + 180 mA = 300 mA @ 24V DC |
| System Loading System Loading                                                         |                                                                                                 |
| 20.8 W = (260 mA x 5V) + (300 mA x 24V) = (1,300 mW) + (7,200 mW) = 8,500 mW = 8.50 W |                                                                                                 |

Table 53 - Validating Systems using 1763-L16BWA

| Maximum Allowable Values Calculated Values                                                   | Maximum Allowable Values Calculated Values                                                                    |                                                                                                               |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Current for Devices Connected to the +24V DC Sensor Supply Sum of all sensor currents        | Current for Devices Connected to the +24V DC Sensor Supply Sum of all sensor currents                         |                                                                                                               |
| 200 mA @ 24V DC 140 mA @ 24V DC (example sensor value)                                       | 200 mA @ 24V DC 140 mA @ 24V DC (example sensor value)                                                        |                                                                                                               |
| Current for MicroLogix Accessories and Expansion I/O Current Values (Subtotal from Table 51) | Current for MicroLogix Accessories and Expansion I/O Current Values (Subtotal from Table 51)                  |                                                                                                               |
|                                                                                              |                                                                                                               | 800 mA @ 5V DC 700 mA @ 24V DC 0 mA + 260 mA = 260 mA @ 5V DC 120 mA + 180 mA = 300 mA @ 24V DC               |
| System Loading System Loading                                                                | System Loading System Loading                                                                                 |                                                                                                               |
| 16.4 W                                                                                       | = (140 mA x 24V) + (260 mA x 5V) + (300 mA x 24V) = (3,360 mW) + (1,300 mW) + (7,200 mW) = 11,860 mW = 11.9 W | = (140 mA x 24V) + (260 mA x 5V) + (300 mA x 24V) = (3,360 mW) + (1,300 mW) + (7,200 mW) = 11,860 mW = 11.9 W |

## System Loading Worksheet

Table 54 , Table 55, and Table 56 are provided for system loading validation. See System Loading Example Calculations on page 165 .

## Current Loading

Table 54 - Calculating the Current for Expansion I/O

|                    | n A B n x A n x B                                     |                                                |
|--------------------|-------------------------------------------------------|------------------------------------------------|
| Catalog Number (1) | Device Current Requirements Calculated Current        | Device Current Requirements Calculated Current |
| Number of Modules  | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                |
| 1762-IA8 50 0      |                                                       |                                                |
| 1762-IF4 40 50     |                                                       |                                                |
| 1762-IF2OF2 40 105 |                                                       |                                                |
| 1762-IQ8 50 0      |                                                       |                                                |
| 1762-IQ16  70(2)   | 0                                                     |                                                |
| 1762-IQ32T 170 0   |                                                       |                                                |
| 1762-IR4 40 50     |                                                       |                                                |
| 1762-IT4 40 50     |                                                       |                                                |
| 1762-OA8 115 0     |                                                       |                                                |
| 1762-OB8 115 0     |                                                       |                                                |
| 1762-OB16 175 0    |                                                       |                                                |
| 1762-OB32T 175 0   |                                                       |                                                |
| 1762-OF4 40 165    |                                                       |                                                |
| 1762-OV32T 175 0   |                                                       |                                                |
| 1762-OW8 80 90     |                                                       |                                                |
| 1762-OW16  140(2)  | 180(2)                                                |                                                |

1762-OX6I 110 110

1762-IQ8OW6 110 80

Total Modules (4 maximum): Subtotal:

(1) See your expansion I/O Installation Instructions for Current Requirements not listed in this table.

(2) Only applicable for series B and series C I/O modules.

Table 54 - Calculating the Current for Expansion I/O (Continued)

Catalog Number (1)

n A B n x A n x B

Number of Modules

Device Current Requirements Calculated Current

@ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA)

## Table 55 - Validating Systems using 1763-L16AWA, 1763-L16BBB, or 1763-L16DWD

## Maximum Allowable Values Calculated Values

Current Current (Subtotal from Table 54)

800 mA @ 5V DC 700 mA @ 24V DC mA @ 5V DC mA @ 24V DC

System Loading System Loading

20.8 W

= (\_\_\_\_\_\_\_\_ mA x 5V) + (\_\_\_\_\_\_\_\_ mA x 24V)

- [ ] = \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW

- [ ] = \_\_\_\_\_\_\_\_\_\_ mW

= \_\_\_\_\_\_\_\_\_\_ W

## Table 56 - Validating Systems using 1763-L16BWA

## Maximum Allowable Values Calculated Values

Current for Devices Connected to the +24V DC Sensor Supply Sum of all sensor currents

200 mA @ 24V DC mA @ 24V DC

Current for MicroLogix Accessories and Expansion I/O Current (Subtotal from Table 54)

800 mA @ 5V DC 700 mA @ 24V DC mA @ 5 V DC mA @ 24V DC

System Loading System Loading

16.4 W

= (\_\_\_\_\_\_\_\_ mA x 24V) + (\_\_\_\_\_\_\_\_ mA x 5V) + (\_\_\_\_\_\_\_\_ mA x 24V)

= \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW

= \_\_\_\_\_\_\_\_\_\_ mW

= \_\_\_\_\_\_\_\_\_\_ W

Calculating Heat Dissipation Use Table 57 when you must determine the heat dissipation of your system for installation in
SifiSi an enclosure. For System Loading, take the value from the appropriate System Loading Worksheet on page 166 .

Table 57 - Heat Dissipation

| Heat Dissipation                                                                                                                                                              | Heat Dissipation   | Heat Dissipation   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|
| Catalog Number  Equation or Constant Calculation Sub-Total                                                                                                                    |                    |                    |
| 1763-L16AWA 15.2 W + (0.4 x System Loading) 15.2 W + (0.4 x ______ W) ______ W                                                                                                |                    |                    |
| 1763-L16BWA 15.7 W + (0.4 x System Loading) 15.7 W + (0.4 x ______ W) ______ W                                                                                                |                    |                    |
| 1763-L16BBB 17.0 W + (0.3 x System Loading) 17.0 W + (0.3 x ______ W) ______ W                                                                                                |                    |                    |
| 1763-L16DWD 17.0 W + (0.3 x System Loading) 17.0 W + (0.3 x ______ W) ______ W                                                                                                |                    |                    |
| 1762-IA8 2.0 W x number of modules 2.0 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-IF4 2.0 W x number of modules 2.0 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-IF2OF2 2.6 W x number of modules 2.6 W x _________ ______ W                                                                                                              |                    |                    |
| 1762-IQ8 3.7 W x number of modules 3.7 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-IQ16  5.4 W(1) x number of modules 5.4 W(1) x _________  ______ W                                                                                                        |                    |                    |
| 1762-IQ32T  6.8 W x number of modules (at 30.0V DC) 5.4 W x number of modules (at 26.4V DC) 6.8 W x _________ (at 30.0V DC) 5.4 W x _________ (at 26.4V DC) ______ W ______ W |                    |                    |
| 1762-IR4 1.5 W x number of modules 1.5 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-IT4 1.5 W x number of modules 1.5 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-OA8 2.9 W x number of modules 2.9 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-OB8 1.6 W x number of modules 1.6 W x _________ ______ W                                                                                                                 |                    |                    |
| 1762-OB16 2.9 W x number of modules 2.9 W x _________ ______ W                                                                                                                |                    |                    |

Table 57 - Heat Dissipation (Continued)

| Catalog Number                                                   |                                            |                                             |
|------------------------------------------------------------------|--------------------------------------------|---------------------------------------------|
| Catalog Number                                                   | Equation or Constant Calculation Sub-Total |                                             |
| 1762-OB32T 3.4 W x number of modules 3.4 W x _________ ______ W  |                                            |                                             |
| 1762-OF4 3.8 W x number of modules 3.8 W x _________ ______ W    |                                            |                                             |
| 1762-OV32T 2.7 W x number of modules 2.7 W x _________ ______ W  |                                            |                                             |
| 1762-OW8 2.9 W x number of modules 2.9 W x _________ ______ W    |                                            |                                             |
| 1762-OW16  6.1 W(1) x number of modules 6.1 W(1) x _________     | ______ W                                   |                                             |
| 1762-OX6I 2.8 W x number of modules 2.8 W x _________ ______ W   |                                            |                                             |
| 1762-IQ8OW6 4.4 W x number of modules 4.4 W x _________ ______ W |                                            |                                             |
| Add Subtotals to determine Heat Dissipation                      | ______ W                                   | Add Subtotals to determine Heat Dissipation |

(1) Only applicable for series B and series C I/O modules.

The following terms and abbreviations are used throughout this manual.

address

A character string that uniquely identifies a memory location. For example, I:1/0 is the memory address for the data located in the Input file location word1, bit 0.

AIC+ Advanced Interface Converter

A device that provides a communication link between various networked devices. 1761-NET-AIC.

application 1) A machine or process monitored and controlled by a controller.

- 2) The use of computer-based or processor-based routines for specific purposes.

baud rate

The speed of communication between devices. All devices must communicate at the same baud rate on a network.

bit The smallest storage location in memory that contains either a 1 (ON) or a 0 (OFF).

block diagrams A schematic drawing.

Boolean operators

Logical operators such as AND, OR, NAND, NOR, NOT, and Exclusive-OR that can be used singularly or in combination to form logic statements or circuits. Can have an output response of T or F.

branch

A parallel logic path within a rung of a ladder program.

communication scan

A part of the controller’s operating cycle. Communication with other devices, such as software running on a personal computer, takes place.

controller

A device, such as a programmable controller, used to monitor input devices and control output devices.

controller overhead

An internal portion of the operating cycle used for housekeeping and set-up purposes.

control profile

The means by which a controller determines which outputs turn on under what conditions.

counter

1) An electro-mechanical relay-type device that counts the occurrence of some event. May be pulses developed from operations such as switch closures or interruptions of light beams. 2) In controllers, a software counter eliminates the need for hardware counters. The software counter can be given a preset count value to count up or down whenever the counted event occurs.

CPU (Central Processing Unit) The decision-making and data storage section of a programmable controller.

data table

The part of processor memory that contains I/O values and files where data is monitored, manipulated, and changed for control purposes.

DIN rail

Manufactured according to Deutsche Industrie Normenausshus (DIN) standards, a metal railing designed to ease installation and mounting of your controller.

download

Data is transferred from a programming or storage device to another device.

DTE (Data Terminal Equipment)

Equipment that is attached to a network to send or receive data, or both.

embedded I/O

Embedded I/O is the controller’s on-board I/O.

EMI

Electromagnetic interference.

encoder

- 1) A rotary device that transmits position information.

2) A device that transmits a fixed number of pulses for each revolution.

<!-- image -->

executing mode Any run or test mode.

expansion I/O

Expansion I/O is I/O that is connected to the controller via a bus or cable. MicroLogix 1200 controllers use Bulletin 1762 expansion I/O.

false

The status of an instruction that does not provide a continuous logical path on a ladder rung.

FIFO (First-In-First-Out)

The order that data is entered into and retrieved from a file.

file A collection of information organized into one group.

full-duplex

A bidirectional mode of communication where data may be transmitted and received simultaneously (contrast with half-duplex).

half-duplex

A communication link in which data transmission is limited to one direction at a time.

hard disk

A storage area in a personal computer that may be used to save processor files and reports for future use.

high byte

Bits 8…15 of a word.

input device A device, such as a push button or a switch, that supplies signals to the input circuits of the controller.

inrush current

The temporary surge current produced when a device or circuit is initially energized.

instruction

A mnemonic and data address defining an operation to be performed by the processor. A rung in a program consists of a set of input and output instructions. The input instructions are evaluated by the controller as being true or false. In turn, the controller sets the output instructions to true or false.

instruction set

The set of general purpose instructions available with a given controller.

I/O (Inputs and Outputs)

Consists of input and output devices that provide and/or receive data from the controller.

jump

Change in normal sequence of program execution, by executing an instruction that alters the program counter (sometimes called a branch). In ladder programs a JUMP (JMP) instruction causes execution to jump to a labeled rung.

ladder logic A program written in a format resembling a ladder-like diagram. The program is used by a programmable controller to control devices.

least significant bit (LSB) The digit (or bit) in a binary word (code) that carries the smallest value of weight.

LED (Light Emitting Diode)

Used as status indicator for processor functions and inputs and outputs.

LIFO (Last-In-First-Out)

The order that data is entered into and retrieved from a file.

low byte

Bits 0…7 of a word.

logic A process of solving complex problems through the repeated use of simple functions that can be either true or false. General term for digital circuits and programmed instructions to perform required decision making and computational functions.

Master Control Relay (MCR) A mandatory hard-wired relay that can be de-energized by any series-connected emergency stop switch. Whenever the MCR is de-energized, its contacts open to de-energize all application I/O devices.

mnemonic

A simple and easy to remember term that is used to represent a complex or lengthy set of information.

modem

Modulator/demodulator. Equipment that connects data terminal equipment to a communication line.

modes

Selected methods of operation. Example: run, test, or program.

negative logic The use of binary logic in such a way that “0” represents the voltage level normally associated with logic 1 (for example, 0 = +5V, 1 = 0V). Positive is more conventional (for example, 1 = +5V, 0 = 0V).

network

A series of stations (nodes) connected by some type of communication medium. A network may be made up of a single link or multiple links.

nominal input current

The current at nominal input voltage.

normally closed

Contacts on a relay or switch that are closed when the relay is de-energized or the switch is deactivated; they are open when the relay is energized or the switch is activated. In ladder programming, a symbol that allows logic continuity (flow) if the referenced input is logic “0” when evaluated.

normally open

Contacts on a relay or switch that are open when the relay is de-energized or the switch is deactivated. (They are closed when the relay is energized or the switch is activated.) In ladder programming, a symbol that allows logic continuity (flow) if the referenced input is logic “1” when evaluated.

off-delay time

The OFF delay time is a measure of the time required for the controller logic to recognize that a signal has been removed from the input terminal of the controller. The time is determined by circuit component delays and by any filter adjustment applied.

offline

Describes devices not under direct communication.

offset

The steady-state deviation of a controlled variable from a fixed point.

off-state leakage current When an ideal mechanical switch is opened (off-state) no current flows through the switch. Practical semiconductor switches, and the transient suppression components which are sometimes used to protect switches, allow a small current to flow when the switch is in the off state. This current is referred to as the off-state leakage current. To ensure reliable operation, the off-state leakage current rating of a switch should be less than the minimum operating current rating of the load that is connected to the switch.

on-delay time

The ON delay time is a measure of the time required for the controller logic to recognize that a signal has been presented at the input terminal of the controller.

one-shot

A programming technique that sets a bit for only one program scan.

online

Describes devices under direct communication. For example, when RSLogix 500 is monitoring the program file in a controller.

operating voltage

For inputs, the voltage range needed for the input to be in the On state. For outputs, the allowable range of user-supplied voltage.

output device A device, such as a pilot light or a motor starter coil, that is controlled by the controller.

processor

A Central Processing Unit. See CPU (Central Processing Unit) on page 169 .

processor file

The set of program and data files used by the controller to control output devices. Only one processor file may be stored in the controller at a time.

program file

The area within a processor file that contains the ladder logic program.

program mode

When the controller is not executing the processor file and all outputs are de-energized.

program scan

A part of the controller’s operating cycle. During the scan the ladder program is executed and the output data file is updated based on the program and the input data file.

programming device

Executable programming package used to develop ladder diagrams.

protocol The packaging of information that is transmitted across a network.

read To acquire data from a storage place. For example, the processor reads information from the input data file to solve the ladder program.

relay An electrically operated device that mechanically switches electrical circuits.

relay logic A representation of the program or other logic in a form normally used for relays.

restore To download (transfer) a program from a personal computer to a controller.

reserved bit A status file location that the user should not read or write to.

retentive data Information associated with data files (timers, counters, inputs, and outputs) in a program that is preserved through power cycles.

RS-232 An EIA standard that specifies electrical, mechanical, and functional characteristics for serial binary communication circuits. A single-ended serial communication interface.

run mode This is an executing mode during which the controller scans or executes the ladder program, monitors input devices, energizes output devices, and acts on enabled I/O forces.

rung Ladder logic is comprised of a set of rungs. A rung contains input and output instructions. During Run mode, the inputs on a rung are evaluated to be true or false. If a path of true logic exists, the outputs are made true. If all paths are false, the outputs are made false.

save To upload (transfer) a program stored in memory from a controller to a personal computer; OR to save a program to a computer hard disk.

scan time The time required for the controller to execute the instructions in the program. The scan time may vary depending on the instructions and each instruction's status during the scan.

sinking A term used to describe current flow between an I/O device and controller I/O circuit — typically, a sinking device or circuit provides a path to ground, low, or negative side of power supply.

sourcing A term used to describe current flow between an I/O device and controller I/O circuit — typically, a sourcing device or circuit provides a path to the source, high, or positive side of power supply.

status The condition of a circuit or system, represented as logic 0 (OFF) or 1 (ON).

terminal A point on an I/O module that external I/O devices, such as a push button or pilot light, are wired to.

throughput The time between when an input turns on and the corresponding output turns on.

true The status of an instruction that provides a continuous logical path on a ladder rung.

upload Data is transferred to a programming or storage device from another device.

watchdog timer A timer that monitors a cyclical process and is cleared at the conclusion of each cycle. If the watchdog runs past its programmed time period, it causes a fault.

workspace The main storage available for programs and data and allocated for working storage.

write To copy data to a storage device. For example, the processor writes the information from the output data file to the output modules.

## Numerics

1762-24AWA wiring diagram 35 1762-IA8 wiring diagram 39 1762-IF2OF2 input type selection 45 output type selection 45 terminal block layout 46 wiring 46 1762-IF4 input type selection 47 terminal block layout 48 1762-IQ16 wiring diagram 40 1762-IQ32T wiring diagram 40 1762-IQ8 wiring diagram 39 1762-OA8 wiring diagram 41 1762-OB16 wiring diagram 41 1762-OB32T wiring diagram 42 1762-OB8 wiring diagram 41 1762-OV32T wiring diagram 42 1762-OW16 wiring diagram 43 1762-OW8 wiring diagram 43 1762-OX6I wiring diagram 44 5/05 processors Ethernet communications 155 A address 169 Advanced Interface Converter. See AIC+ AIC+ applying power to 67 attaching to the network 67 connecting 63 definition 169 installing 67 recommended user supplied components 66 safety consideration 67 selecting cable 65 analog channel wiring guidelines 37 analog expansion I/O 137 diagnostics 137 module operation vs. channel operation 137 power-up diagnostics 137 system wiring guidelines 45 troubleshooting 137 analog inputs analog channel wiring guidelines 37 application 169 B battery 101 processor battery life expectancy 129 processor replacement battery 129 baud rate 169 bit 169 block diagrams 169

Boolean operators 169

## BOOTP

configuring SLC 5/05 160 - 162 using the Rockwell Utility 161

branch

169

Buttons 74

C

## cable pinout

MicroLogix 1100 Channel 0 to modem cable 57 , 63

## cables

planning routes for DH485 connections 150 selection guide for the AIC+ 65

calling for assistance 139

## common mode rejection ratio

specification 124

## communication

DeviceNet 68

Ethernet 68

communication connections 51

communication options 14

communication protocols

DF1 Full-Duplex DF1 Half-Duplex DH485 148

Ethernet 155

Modbus 154

communication scan 169

## communications toggle push button

using 52

## component descriptions 12

1762 expansion I/O 12 communication cables 13 memory module 12 real-time clock 12

configuration errors 138

connecting expansion I/O

28

connecting the system

AIC+ 63 , 67 DeviceNet network 68 DF1 Full-Duplex protocol 55 DF1 isolated point-to-point connection DH485 network 59

55

connecting to DF1 Half-Duplex network 57

contactors (bulletin 100), surge suppressors for 32

control profile 169

## ControlFlash

missing/corrupt OS LED pattern 144 sequence of operation 143 using 141

145

146

```
controller 169 grounding 32 I/O wiring 37 LED status error conditions 135 LED status normal operation 135 minimizing electrical noise 37 mounting 24 mounting dimensions 23 mounting on DIN rail 25 mounting on panel 26 preventing excessive heat 18 status indicators 133 controller overhead 169 controller spacing 24 counter 169 CPU (Central Processing Unit) 169 Cursor display 75 D data table 169 default communication configuration 51 DeviceNet Communications 68 DeviceNet network connecting 68 DF1 Full-Duplex protocol connecting 55 description 145 example system configuration 145 using a modem 56 , 147 DF1 Half-Duplex protocol description 146 DH485 communication protocol configuration parameters 59 , 149 DH485 network configuration parameters 150 connecting 59 devices that use the network 149 example system configuration 152 installation 61 planning considerations 149 DIN rail 169 disconnecting main power 16 download 169 DTE (Data Terminal Equipment) 169 E Electronics Industries Association (EIA) ) 145 EMI 169 encoder 169 error recovery model 136 errors configuration 138 critical 137 extended error information field 138 hardware 138 module error field 137 non-critical 137 Ethernet advanced functions 162 messaging 155 processor performance 155 using the SLC 5/05 processors 155
```

```
executing mode 170 expansion I/O 1762-IF2OF2 input type selection 45 1762-IF2OF2 output type selection 45 expansion I/O mounting 27 mounting on DIN rail 27 expansion I/O wiring 39 1762-IA8 wiring diagram 39 1762-IF2OF2 wiring 46 1762-IF4 terminal block layout 48 1762-IQ16 wiring diagram 40 1762-IQ32T wiring diagram 40 1762-IQ8 wiring diagram 39 1762-OA8 wiring diagram 41 1762-OB16 wiring diagram 41 1762-OB32T wiring diagram 42 1762-OB8 wiring diagram 41 1762-OV32T wiring diagram 42 1762-OW16 wiring diagram 43 1762-OW8 wiring diagram 43 1762-OX6I wiring diagram 44 analog wiring guidelines 45 extended error information field 138 F false 170 FIFO (First-In-First-Out) ) 170 file 170 Full-Duplex 55 full-duplex 170 G general considerations 15 grounding the controller 32 H Half-Duplex 58 , 170 hard disk 170 hardware errors 138 hardware features 11 heat dissipation calculating 167 heat protection 18 high byte 170 I I/O (Inputs and Outputs) 170 input device 170 input states on power down 18 inrush current 170 installing ControlFlash software 141 memory module 22 instruction 170 instruction set 170 isolated link coupler installing 61 isolation transformers power considerations 17
```

| J                                                                     | off-state leakage current  171                             |
|-----------------------------------------------------------------------|------------------------------------------------------------|
| jump  170                                                             | one-shot  171 online  171                                  |
| L                                                                     | Online Editing  105 Terms  105                             |
| ladder logic  170                                                     | Operating buttons  74                                      |
| least significant bit (LSB)  170                                      | operating voltage  171                                     |
| )                                                                     | 171                                                        |
|                                                                       | output device                                              |
| LED (Light Emitting Diode)  170                                       |                                                            |
| LIFO (Last-In-First-Out)  170 lithium battery (1747-BA)               | P                                                          |
| disposing  131                                                        |                                                            |
|                                                                       | performance                                                |
| handling  130 installing  129                                         | Ethernet processor  155                                    |
| storing  130                                                          | planning considerations for a network                      |
| transporting  130                                                     | power considerations                                       |
| logic  170                                                            | input states on power down  18 isolation transformers  17  |
| low byte  170                                                         | loss of power source  17 other line conditions  18         |
| M                                                                     | overview  17 power supply inrush  17                       |
| master control relay  18                                              | power distribution  17                                     |
| emergency-stop switches  19                                           | power source                                               |
| using ANSI/CSA symbols schematic  21 20                               | loss of                                                    |
| using IEC symbols schematic  Master Control Relay (MCR)  )  170       | 17 power supply inrush                                     |
| master control relay circuit                                          | power considerations  17 preparing for upgrade             |
| periodic tests  17                                                    | 141                                                        |
| memory module                                                         | preventing excessive heat  18                              |
| data file protection  103                                             | processor  171                                             |
| operation  102                                                        | processor file  171                                        |
| program compare  102                                                  | program file  171                                          |
| program/data/recipe backup  102 removal/installation under power  103 | program mode  171 171                                      |
| write protection  103                                                 | program scan                                               |
| Menu structure  72 37                                                 | programming  171                                           |
|                                                                       | 13 programming device                                      |
| minimizing electrical noise                                           |                                                            |
| mnemonic  170                                                         | protocol  172                                              |
| Modbus communication protocol  154                                    |                                                            |
|                                                                       | R                                                          |
| modem  170 modems using with MicroLogix controllers  147              | read  172 real-time clock operation  101                   |
| module error field  137                                               | battery operation                                          |
| modes  171                                                            | 101                                                        |
| motor starters (bulletin 509)                                         | removal/installation under power  101                      |
| surge suppressors  32                                                 | writing data  101 172                                      |
| motor starters (bulletin 709)                                         | 172                                                        |
| surge suppressors  32                                                 | relay  relay logic                                         |
|                                                                       | relays                                                     |
| N                                                                     | surge suppressors for  32                                  |
| 171                                                                   | remote packet support  151 replacement battery  129        |
| negative logic  network  171                                          | disposing  131                                             |
| nominal input current                                                 | handling  130                                              |
| 171 171                                                               | installing                                                 |
| normally closed                                                       | 129 storing  130 transporting                              |
| normally open  171                                                    | 130                                                        |
|                                                                       | replacement kits  129 replacement parts  reserved bit  172 |
| O                                                                     | 129                                                        |
| offline  171                                                          | restore  172                                               |
| Offline Editing                                                       |                                                            |
| 105                                                                   | retentive data                                             |
| offset  171                                                           |                                                            |
|                                                                       | 172                                                        |
|                                                                       | RS-232  172                                                |

RS-232 communication interface 145

run mode 172 rung 172 S safety circuits 16 safety considerations 15 disconnecting main power 16 hazardous location 15 master control relay circuit periodic tests 17 periodic tests of master control relay circuit 17 power distribution 17 safety circuits 16 save 172 scan time 172 sinking 172 sinking and sourcing wiring diagrams 35 sinking wiring diagram 1762-24BWA 35 sourcing 172 sourcing wiring diagram 1762-24BWA 36 , 37 status 172 surge suppressors for contactor 32 for motor starters 32 for relays 32 recommended 32 using 30 system configuration DF1 Full-Duplex examples 145 DH485 connection examples 152 system loading example calculations 165 limitations 165 worksheet 166 system loading and heat dissipation 165 T terminal 172 terminal block layouts 1762-IF2OF2 46 1762-IF4 48 controllers 33 terminal groupings 34 terminal groupings 34 throughput 172 Trimpot Information Function File 97 trimpot operation 96 trimpots changing values 96 , 97

error conditions 98

location 96

troubleshooting 133

true 172

## U

upload 172

using communications toggle functionality 52

using communications toggle push button 52

using emergency-stop switches 19

using memory modules 101

using real-time clock 101

using trimpots 96

## W

## wiring diagram

1762-IA8 39

1762-IF2OF2 differential sensor 46

1762-IF2OF2 single-ended sensor 47

1762-IQ16 40

1762-IQ32T 40

1762-IQ8 39

1762-L24BXB output 37

1762-OA8 41

1762-OB16 41

1762-OB32T 42

1762-OB8 41

1762-OV32T 42

1762-OW16 43

1762-OW8 43

1762-OX6I 44

1763-L16AWAE input 35

1763-L16AWAE output 36

1763-L16BBBE sinking 36

1763-L16BBBE sourcing 36

1763-L16BWAE output 36

1763-L16BWAE sinking 36

1763-L16BWAE sourcing 36

terminal block layouts 33 , 46 , 48

wiring diagrams 33

wiring recommendation 29

wiring your controller 29

workspace 172

write 172

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

Allen-Bradley, ControlFLASH, DH+, DTAM Micro, DTAM Plus, expanding human possibility, FactoryTalk, INTERCHANGE, MicroLogix, PanelView, PLC-5, Rockwell Automation, RSLinx, RSLinx Classic, RSLogix 500, SLC, SLC 5/03, SLC 500, and TechConnect are trademarks of Rockwell Automation, Inc.

CIP, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility?

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIA PACIFIC:Rockwell Automation SEA Pte Ltd, 2 Corporation Road, #04-05, Main Lobby,Corporation Place,Singapore 618494,Tel:(65)6510 6608