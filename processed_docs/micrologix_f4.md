<!-- image -->

## MicroLogix 1400 Programmable Controllers

Bulletins 1766 Controllers and 1762 Expansion I/O

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

IMPORTANT

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

Preface

|                         | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|                         | Purpose of this Manual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11       |
|                         | Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                       |
|                         | Summary of Changes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11        |
|                         | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11     |
|                         | Chapter 1                                                                                                                                 |
| Hardware Overview       | Hardware Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13      |
|                         | Component Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14         |
|                         | MicroLogix 1400 Memory Module and Built-in Real-time Clock . . . . . . . . . . . . . . . . . . 14                                         |
|                         | 1762 Expansion I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                  |
|                         | Communication Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15         |
|                         | Programming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16  |
|                         | Firmware Revision History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16                |
|                         | Communication Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17         |
|                         | Chapter 2                                                                                                                                 |
| Install Your Controller | Installation Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19        |
|                         | Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19      |
|                         | Hazardous Location Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                        |
|                         | Disconnect Main Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                |
|                         | Safety Circuits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20       |
|                         | Power Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20           |
|                         | Proof Tests of Master Control Relay Circuit. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                         |
|                         | Power Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21       |
|                         | Isolation Transformers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21             |
|                         | Power Supply Inrush . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21              |
|                         | Loss of Power Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21              |
|                         | Input States on Power Down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                   |
|                         | Other Types of Line Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22                   |
|                         | Help Prevent Excessive Heat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22          |
|                         | Master Control Relay . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22     |
|                         | Emergency Stop Switches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                  |
|                         | Install a Memory Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24        |
|                         | Use the Battery. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 |
|                         | Connect the Battery Wire Connector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                       |
|                         | Controller Mounting Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26             |
|                         | Controller and Expansion I/O Spacing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                |
|                         | Mount the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27    |
|                         | DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27          |
|                         | Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28         |
|                         | 1762 Expansion I/O Module Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                   |
|                         | Mount 1762 Expansion I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29               |
|                         | DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29          |

## Table of Contents

|                           | Connect Expansion I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30            |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                           | Chapter 3                                                                                                                               |
| Wire Your Controller      | Wiring Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33    |
|                           | Wiring Recommendation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                |
|                           | Wire without Spade Lugs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33              |
|                           | Wire with Spade Lugs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34            |
|                           | Use Surge Suppressors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34      |
|                           | Recommended Surge Suppressors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                         |
|                           | Ground the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36   |
|                           | Wiring Diagrams. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 |
|                           | Terminal Block Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37             |
|                           | Sinking and Sourcing Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40               |
|                           | 1766-L32BWA, 1766-L32AWA, 1766-L32BXB, 1766-L32BWAA, 1766-L32AWAA, 1766-                                                                |
|                           | L32BXBA Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                |
|                           | Controller I/O Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 |
|                           | Minimize Electrical Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42            |
|                           | Wire Your Analog Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43        |
|                           | Analog Channel Wiring Guidelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43                   |
|                           | Minimize Electrical Noise on Analog Channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44                           |
|                           | Ground Your Analog Cable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44               |
|                           | Expansion I/O Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45   |
|                           | Digital Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45            |
|                           | Analog Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51      |
|                           | Chapter 4                                                                                                                               |
| Communication Connections | Supported Communication Protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                |
|                           | Default Communication Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                |
|                           | Use the Communications Toggle Functionality. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                     |
|                           | Change Communication Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                         |
|                           | Connect to the RS-232 Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60       |
|                           | Make a DF1 Point-to-Point Connection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60                      |
|                           | Modem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61   |
|                           | Connect to a DF1 Half-Duplex Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                       |
|                           | Connect to a RS-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65          |
|                           | DH-485 Configuration Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                     |
|                           | Recommended Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67              |
|                           | DH-485 Communication Cable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                   |
|                           | Connect the Communication Cable to the DH-485 Connector . . . . . . . . . . . . . . . . . . . 67                                        |
|                           | Ground and Terminate the DH-485 Network. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68                             |
|                           | Connect the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69 |
|                           | Cable Selection Guide. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70           |
|                           | Recommended User-Supplied Components. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                                |
|                           | Install and Attach the AIC+. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72             |
|                           | Power the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72       |
|                           | Connect to Ethernet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73    |
|                           | Ethernet Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74           |

## LCD and Keypad

## Chapter 5

| Operating Principles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76        |
|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Startup Screen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76             |
| Main Menu and Default Screen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77                        |
| Operating Buttons. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79               |
| Select Between Menu Items . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                      |
| Cursor Display. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80            |
| Set Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80         |
| I/O Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80 |
| View I/O Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81            |
| Monitor User Defined Target Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                |
| Target User Defined File Number (TUF) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                            |
| Monitor a Bit File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83           |
| Monitor Integer Files. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85               |
| Monitor Double Integer files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                   |
| Monitor Floating Point Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                   |
| Monitor System Status Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                    |
| Mode Switch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93    |
| Controller Modes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93              |
| Change Mode Switch Position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                        |
| User-defined LCD Screen. . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  95           |
| User-defined LCD Screen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                     |
| Configure Advanced Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                |
| Change Key In Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96          |
| Key In Modes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96            |
| Change Key In Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                 |
| Communications Toggle Functionality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                      |
| Ethernet Network Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                 |
| View Ethernet Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                 |
| Configure the IP Address . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99                   |
| Configure the Ethernet Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                     |
| Configure Ethernet Protocol Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                           |
| Trim Pots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105   |
| Trim Pot Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                |
| Change Data Value of a Trim Pot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                         |
| Trim Pot Configuration in LCD Function File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                               |
| Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106              |
| View System Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107              |
| View Fault Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107       |
| Save or Load Communication EEPROM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                         |
| Save Communication EEPROM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                           |
| Load communication EEPROM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                           |
| LCD setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110   |
| Configure Contrast Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                    |
| Configure the Back Light . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                  |
| Protocol Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112          |
| Modbus RTU Slave Node Address . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112                             |
| Set the LCD Password . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114                    |

|                            | Activate the LCD Password . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115               |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
|                            | Deactivate the LCD Password . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116                 |
|                            | Change LCD Password . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117             |
|                            | Chapter 6                                                                                                                             |
| Real-Time Clock and Memory | Real-Time Clock Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119       |
| Modules                    | Operation at Power-up and Entering a Run or Test Mode . . . . . . . . . . . . . . . . . . . . . 119                                   |
|                            | Write Data to the Real-Time Clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119                 |
|                            | RTC Battery Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119           |
|                            | Memory Module Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120       |
|                            | User Program, User Data, Datalog, and Recipe Back-up . . . . . . . . . . . . . . . . . . . . . . 120                                  |
|                            | Program Compare . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120           |
|                            | Data File Download Protection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120                |
|                            | Memory Module Write Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121                  |
|                            | Removal/Insertion Under Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121                   |
|                            | Memory Module Information File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121                  |
|                            | Program /Data Download. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121               |
|                            | Program /Data Upload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121            |
|                            | Chapter 7                                                                                                                             |
| Online Editing             | Overview of Online Editing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123    |
|                            | Online Editing Terms. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123         |
|                            | Effects of Online Editing On Your System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124              |
|                            | System Impacts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124        |
|                            | Data Table File Size. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124       |
|                            | Online Edit Error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124     |
|                            | Directions and Cautions for MicroLogix 1400 Online Editing User . . . . . . . . . . . . . . . . . . . 124                             |
|                            | A Download is Required Before Starting Online Editing . . . . . . . . . . . . . . . . . . . . . . . 124                               |
|                            | Types of Online Editing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125  |
|                            | Edit Functions in Runtime Online Editing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126                     |
|                            | Edit Functions in Program Online Editing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126                      |
|                            | Chapter 8                                                                                                                             |
| Auto Reset Functionality   | Automatic Controller Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127         |
|                            | Enable the Status Bit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127         |
|                            | Appendix A                                                                                                                            |
| Specifications             | Working Voltage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133       |
|                            | 1762 Expansion I/O Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134         |
|                            | Analog Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138       |
|                            | Appendix B                                                                                                                            |
| Replacement Parts          | MicroLogix 1400 Controller Replacement Kits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145                  |
|                            | Lithium Battery (1747-BA) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145     |
|                            | Installation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145  |
|                            | Battery Handling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145       |
|                            | Storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146 |

|                             | Transportation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146                |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|                             | Disposal. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146           |
|                             | Appendix C                                                                                                                                      |
| Troubleshoot Your System    | Understand the Controller Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149                           |
|                             | Controller Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149                      |
|                             | Status Indicators on the LCD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150                        |
|                             | I/O Status Indicators on the LCD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150                          |
|                             | Normal Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151                  |
|                             | Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151                |
|                             | Controller Error Recovery Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151                   |
|                             | Analog Expansion I/O Diagnostics and Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . . 152                                    |
|                             | Module Operation and Channel Operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152                                   |
|                             | Power-up Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153                      |
|                             | Critical and Non-Critical Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153                        |
|                             | Module Error Definition Table. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153                        |
|                             | Error Codes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154              |
|                             | Contact Rockwell Automation for Assistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155                            |
|                             | Appendix D                                                                                                                                      |
| Use ControlFLASH to Upgrade | Prepare for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157                   |
| Your Operating System       | Install ControlFLASH Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157                         |
|                             | Use DMK Extraction Tool for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157                                     |
|                             | Prepare the Controller for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159                                    |
|                             | Use ControlFLASH for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160                          |
|                             | ControlFLASH Error Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166                   |
|                             | Missing or Corrupt OS state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168               |
|                             | Recover from Missing or Corrupt OS State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168                                  |
|                             | Appendix E                                                                                                                                      |
| Connect to Networks Via RS                             | RS-232 Communication Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169                      |
| 232/RS-485 Interface        | RS-485 Communication Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169                      |
|                             | DF1 Full-duplex Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169              |
|                             | DF1 Half-duplex Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170              |
|                             | DF1 Half-duplex Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170                       |
|                             | Considerations When Communicating as a DF1 Slave on a Multi-drop Link . . . . . . . 171                                                         |
|                             | Using Modems with MicroLogix Programmable Controllers . . . . . . . . . . . . . . . . . . . . 171                                               |
|                             | DH-485 Communication Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172                       |
|                             | DH-485 Configuration Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172                              |
|                             | Devices that use the DH-485 Network. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173                                |
|                             | Important DH-485 Network Planning Considerations . . . . . . . . . . . . . . . . . . . . . . . . . 173                                          |
|                             | Example DH-485 Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176                            |
|                             | Modbus Communication Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178                       |
|                             | ASCII . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178 |
|                             | Distributed Network Protocol (DNP3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178                       |
|                             | Disable Serial Channels 0 and 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178                   |

## MicroLogix 1400 Distributed Network Protocol

## Appendix F

| Channel Configuration for DNP3 Slave . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 179                    |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| Channel 0 and Channel 2 Link Layer Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . 179                                    |
| Channel 1 Link Layer Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180                        |
| DNP3 Slave Application Layer Configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181                               |
| Channel 0 and Channel 2 Link Layer Configuration Parameters . . . . . . . . . . . . . . . . 183                                             |
| Channel 1 (Ethernet) Link Layer Configuration Parameters . . . . . . . . . . . . . . . . . . . . 186                                        |
| DNP3 Slave Application Layer Configuration Parameters . . . . . . . . . . . . . . . . . . . . . 189                                         |
| DNP3 Slave Application Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199              |
| Function Codes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199             |
| Internal Indications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202             |
| DNP3 Objects and Controller Data Files. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203                   |
| DNP3 Data Files. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205            |
| DNP3 Configuration Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205                  |
| DNP3 Binary Input Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 209                  |
| DNP3 Binary Output Object. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 210                    |
| DNP3 Double Bit Binary Input Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212                         |
| DNP3 Counter Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213                 |
| DNP3 Frozen Counter Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 215                      |
| DNP3 Analog Input Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217                    |
| DNP3 Analog Output Object . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220                     |
| DNP3 BCD Object. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221              |
| DNP3 Data-Set Object. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222                 |
| Object Quality Flags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230              |
| DNP3 Device Attribute Object. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232             |
| Event Reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234     |
| Generate Events . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234             |
| DNP3 10K Event Logging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237                    |
| Control Generating Event . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238                  |
| Report Event By Polled Response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239                         |
| Report Event By Unsolicited Response . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239                            |
| Collision Avoidance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241       |
| Time Synchronization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241         |
| Download a User Program Via DNP3 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242                            |
| Default Directories and Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242                   |
| Generate *.IMG files using RSLogix 500/RSLogix Micro . . . . . . . . . . . . . . . . . . . . . . . 243                                      |
| Rules for File Authentication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244                   |
| Rules for Downloading a User Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245                              |
| Rules for Uploading a User Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246                          |
| Rules for Initializing a User Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246                       |
| Rules for uploading Communication Status Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246                                  |
| Start and Stop User Programs (Mode Change) Via DNP3 Network. . . . . . . . . . . . . . . 246                                                |
| Initialize User Program. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247                |
| Start User Program. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247               |
| Stop User Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247               |
| Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247 |
| Diagnostics for Ethernet Channel (Channel 1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252                              |
| Function Codes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257     |

|                         | Implementation Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259             |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|                         | Appendix G                                                                                                                                     |
| Connect to Networks Via | MicroLogix 1400 Controllers and Ethernet Communication . . . . . . . . . . . . . . . . . . . . . . . . 267                                     |
| Ethernet Interface      | MicroLogix 1400 Performance Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267                             |
|                         | MicroLogix 1400 and PC Connections to the                                                                                                      |
|                         | Ethernet Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268         |
|                         | Connecting an Ethernet switch on the Ethernet Network. . . . . . . . . . . . . . . . . . . . . . 268                                           |
|                         | Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269         |
|                         | Ethernet Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270            |
|                         | Duplicate IP Address Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270                 |
|                         | Configure the Ethernet Channel on the MicroLogix 1400 . . . . . . . . . . . . . . . . . . . . . . . . . . 271                                  |
|                         | Configure Using RSLogix 500/RSLogix Micro Programming Software. . . . . . . . . . . . . . . . 272                                              |
|                         | Configure Using BOOTP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272              |
|                         | Using the Rockwell Automation BOOTP/DHCP Utility. . . . . . . . . . . . . . . . . . . . . . . . . . 273                                        |
|                         | Use a DHCP Server To Configure Your Processor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275                              |
|                         | Subnet Masks and Gateways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275                  |
|                         | Manually Configure Channel 1 for Controllers on Subnets . . . . . . . . . . . . . . . . . . . . . 275                                          |
|                         | MicroLogix 1400 Embedded Web Server Capability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276                                 |
|                         | Disable the Ethernet Channel. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276                |
|                         | Appendix H                                                                                                                                     |
| System Loading and Heat | System Loading Calculations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279                 |
| Dissipation             | System Loading Example Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279                                |
|                         | System Loading Worksheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280                 |
|                         | Current Loading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280                |
|                         | Calculating Heat Dissipation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282               |
|                         | Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 283       |
|                         | Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . 287 |

## Notes:

## About This Publication

## Purpose of this Manual

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

## Additional Resources

## Additional Resources

|                                                                                                             | Resource Description                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001                           | Information on the MicroLogix 1400 Controllers instruction set.                                                                                                                                |
| MicroLogix 1400 Programmable Controllers Installation Instructions, publication 1766 -IN001                 | Information on mounting and wiring the MicroLogix 1400 Controllers, including a mounting template for easy installation.                                                                       |
| Advanced Interface Converter (AIC+) User Manual, publication 1761-UM004                                     | A description on how to install and connect an AIC+. This manual also contains information on network wiring.                                                                                  |
| DeviceNet Interface User Manual, publication 1761-UM005                                                     | Information on how to install, configure, and commission a DeviceNet® Interface.                                                                                                               |
| DF1 Protocol and Command Set Reference Manual, publication 1770-6.5.16                                      | Information on DF1 open protocol.                                                                                                                                                              |
| Modbus Protocol Specifications available from www.modbus.org                                                | Information about the Modbus protocol.                                                                                                                                                         |
| Distributed Network Protocol (DNP3) Specifications Available from www.dnp.org                               | Information about the Distributed Network Protocol.                                                                                                                                            |
| System Security Design Guidelines Reference Manual, publication SECURE-RM001                                | Provides guidance on how to conduct security assessments, implement Rockwell Automation® products in a secure system, harden the control system, manage user access, and dispose of equipment. |
| UL Standards Listing for Industrial Control Products, publication CMPNTS-SR002                              | Assists original equipment manufacturers (OEMs) with construction of panels, to help ensure that they conform to the requirements of Underwriters Laboratories.                                |
| American Standards, Configurations, and Ratings: Introduction to Motor Circuit Design, publication IC-AT001 | Provides an overview of American motor circuit design based on methods that are outlined in the NEC.                                                                                           |

Use this manual if you are responsible for designing, installing, programming, or troubleshooting control systems that use MicroLogix™ 1400 controllers.

You should have a basic understanding of electrical circuitry and familiarity with relay logic. If you do not, obtain the proper training before using this product.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This manual is a reference guide for MicroLogix 1400 controllers and 1762 expansion I/O. It describes the procedures you use to install, wire, and troubleshoot your controller. This manual:

- Explains how to install and wire your controllers
- Gives you an overview of the MicroLogix 1400 controller system

See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001, for the MicroLogix 1400 instruction set and for application examples to show the instruction set in use. See your RSLogix 500®/RSLogix™ Micro programming software user documentation for more information on programming your MicroLogix 1400 controller.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic Page                                  |
|---------------------------------------------|
| Updated template throughout                 |
| Added 1762 Expansion I/O Specifications 134 |
| Updated Certifications 135                  |

These documents contain additional information concerning related products from Rockwell Automation.

## Additional Resources (Continued)

|                                                                                                                    | Resource Description                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley® industrial automation controls and assemblies.                                                                                                                                                                               |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications                                                            | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

You can view or download publications at rok.auto/literature .

## Hardware Features

## Hardware Overview

The MicroLogix 1400 programmable controller contains a power supply, input and output circuits, a processor, an isolated combination RS-232/RS-485 communication port, an Ethernet port, and a non-isolated RS-232 communication port. Each controller supports 32 discrete I/O points (20 digital inputs, 12 discrete outputs) and 6 analog I/O points (4 analog inputs and 2 analog outputs: 1766-L32BWAA, 1766-L32AWAA, and 1766-L32BXBA only).

Figure 1 shows the hardware features of the controller.

Figure 1 - Controller Hardware Features

<!-- image -->

Left side view Top view

## Controller Description

| Description Description                                                               |                                                                                |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| 1 Comm port 2 – 9-pin D-shell RS-232C connector 8 Battery connector                   |                                                                                |
|                                                                                       | 2 Memory module 9 Output terminal block                                        |
| 3 User 24V (for 1766-BWA and 1766-BWAA only) 10 LCD display                           |                                                                                |
|                                                                                       | 4 Input terminal block 11 Status indicator panel                               |
| 5 LCD display keypad (ESC, OK, Up, Down, Left, Right) 12 Comm port 1 – RJ45 connector |                                                                                |
|                                                                                       | 6 Battery compartment 13 Comm port 0 – 8-pin mini DIN RS-232C/RS-485 connector |
| 7 1762 expansion bus connector                                                        |                                                                                |

<!-- image -->

<!-- image -->

## Controller Input and Output Description

| Catalog Number      | Description   | Description   | Description                                                                                        | Description                        | Description                               |
|---------------------|---------------|---------------|----------------------------------------------------------------------------------------------------|------------------------------------|-------------------------------------------|
| Catalog Number      |               |               | Input Power User Power Embedded Discrete I/O Embedded Analog I/O Comm. Ports                       |                                    |                                           |
| 1766-L32BWA         | 100/240V AC   | 24V DC        | 12 fast 24V DC inputs 8 normal 24V DC inputs 12 relay outputs                                      | None                               | 1 RS-232/RS-485(1) 1 Ethernet 1 RS-232(2) |
| 1766-L32AWA         | 100/240V AC   |               | 20 120V AC inputs 12 relay outputs                                                                 | None                               | 1 RS-232/RS-485(1) 1 Ethernet 1 RS-232(2) |
| 1766-L32BXB 24V DC  |               | None          | 12 fast 24V DC inputs 8 normal 24V DC inputs 6 relay outputs 3 fast DC outputs 3 normal DC outputs | None                               | 1 RS-232/RS-485(1) 1 Ethernet 1 RS-232(2) |
| 1766-L32BWAA        | 100/240V AC   | 24V DC        | 12 fast 24V DC inputs 8 normal 24V DC inputs 12 relay outputs                                      | 4 voltage inputs 2 voltage outputs | 1 RS-232/RS-485(1) 1 Ethernet 1 RS-232(2) |
| 1766-L32AWAA        | 100/240V AC   | None          | 20 120V AC inputs 12 relay outputs                                                                 | 4 voltage inputs 2 voltage outputs | 1 RS-232/RS-485(1) 1 Ethernet 1 RS-232(2) |
| 1766-L32BXBA 24V DC |               | None          | 12 fast 24V DC inputs 8 normal 24V DC inputs 6 relay outputs 3 fast DC outputs 3 normal DC outputs | 4 voltage inputs 2 voltage outputs | 1 RS-232/RS-485(1) 1 Ethernet 1 RS-232(2) |

- (2) Non-isolated RS-232. Standard D-sub connector

## Component Descriptions

## MicroLogix 1400 Memory Module and Built-in Real-time Clock

The controller has a built-in real-time clock to provide a reference for applications that need timebased control.

The controller is shipped with a memory module port cover in place. You can order a memory module, 1766-MM1, as an accessory. The memory module provides optional backup of your user program and data, and is a means to transport your programs between controllers.

The program and data in your MicroLogix 1400 is non-volatile and is stored when the power is lost to the controller. The memory module provides additional backup that can be stored separately. The memory module does not increase the available memory of the controller.

Figure 2 - 1766-MM1 Memory Module

<!-- image -->

## Communication Cables

## 1762 Expansion I/O Modules

1762 expansion I/O modules can be connected to the MicroLogix 1400 controller, as shown in Figure 3 .

<!-- image -->

A maximum of seven I/O modules, in any combination, can be connected to a controller. See Appendix H to determine how much heat a certain combination generates.

Figure 3 - 1762 Expansion I/O Modules

1762 expansion I/O module 1762 expansion I/O modules connected to a MicroLogix 1400 controller

<!-- image -->

## Expansion I/O Modules

| Catalog Number Description                                                             |
|----------------------------------------------------------------------------------------|
| 1762-IA8 8-point 120V AC input module                                                  |
| 1762-IQ8 8-point sink/source 24V DC input module                                       |
| 1762-IQ16 16-point sink/source 24V DC input module                                     |
| 1762-IQ32T 32-point sink/source 24V DC input module                                    |
| 1762-OA8 8-point 120/240V AC Triac output module                                       |
| 1762-OB8 8-point sourcing 24V DC output module                                         |
| 1762-OB16 16-point sourcing 24V DC output module                                       |
| 1762-OB32T 32-point sourcing 24V DC output module                                      |
| 1762-OV32T 32-point sinking 24V DC output module                                       |
| 1762-OW8 8-point AC/DC relay output module                                             |
| 1762-OW16 16-point AC/DC relay output module                                           |
| 1762-OX6I 6-point isolated AC/DC relay output module                                   |
| 1762-IQ8OW6 8-point sink/source 24V DC input and 6-point AC/DC relay output module     |
| 1762-IF4 4-channel voltage/current analog input module                                 |
| 1762-OF4 4-channel voltage/current analog output module                                |
| 1762-IF2OF2 Combination 2-channel input 2-channel output voltage/current analog module |
| 1762-IR4 4-channel RTD/resistance input module                                         |
| 1762-IT4 4-channel thermocouple/mV input module                                        |

Use only the following communication cables with the MicroLogix 1400 controllers. These cables are required for Class I Div. 2 applications.

- 1761-CBL-AM00, Series C or later
- 1761-CBL-AP00, Series C or later
- 1761-CBL-PM02, Series C or later
- 1761-CBL-HM02, Series C or later
- 1763-NC01, Series A or later
- 1747-CP3, Series A or later

<!-- image -->

## Programming

Table 1 - MicroLogix 1400 Controllers

| Catalog Number OS Revision Letter   | OS(1)  Series Letter   | OS Firmware Release Number   | Release Date Enhancement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------|------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1766-L32AWA 1766-L32BWA 1766-L32BBB |                        |                              | A A FRN1 August 2005 Initial product release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 1766-L32AWA 1766-L32BWA 1766-L32BBB |                        | A B FRN2 October 2005        | According to the SRAM component, MicroLogix 1400 could cause Hard-fault at the start of the Operating System in a very high temperature environment. Corrected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 1766-L32AWA 1766-L32BWA 1766-L32BBB |                        |                              | A C FRN3 February 2006 Added Data file write feature through web server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1766-L32AWA 1766-L32BWA 1766-L32BBB |                        | B A FRN4 February 2007       | • Direct connection to RS-485 Network for DF1 half-duplex master driver • Direct connection to RS-485 Network for DF1 half-duplex slave driver • Direct connection to RS-485 Network for ASCII driver • Selectable Stop/Data Bits for Modbus master RTU driver • Selectable Stop/Data Bits for Modbus slave RTU driver • Selectable Stop/Data Bits for ASCII driver • Settable Inactivity Timeout feature for Ethernet driver • Unsolicited Ethernet messaging to RSLinx® OPC topic • CIP™ Generic messaging through the Ethernet port • Unconnected EtherNet/IP protocol for Ethernet driver • IP conflict detection mechanism • Email feature • Ethernet MSG break bit • DNS functionality when the email feature is used • Change IP address with Ethernet MSG instruction • ST file type for all PCCC commands • HSC (High-Speed Counter) up to 40 KHz • PTO/PWM up to 40 KHz • 2-channel Analog Input Filter • Web View Disable for Data Files |
| 1766-L32AWA 1766-L32BWA 1766-L32BBB |                        | B B FRN5 May 2007            | • Fixed anomaly for CIP Messaging Error when CIP Service Code is 4Bh or 4Ch. • Fixed anomaly for the EtherNet/IP List Identity reply. • Fixed anomaly for window size error in TCP/IP stack. • Improved system interrupt delay time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1766-L32DWD B B FRN5 May 2007       |                        |                              | • Initial Product release. Supports the features that are listed above for the 1766- L32AWA, 1766-L32BWA, and 1766-L32BBB controllers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

(1) OS = Operating system

<!-- image -->

## ATTENTION: UNSUPPORTED CONNECTION

Do not connect a MicroLogix 1400 controller to another MicroLogix family controller such as MicroLogix 1000, MicroLogix 1200, MicroLogix 1500, or the network port of a 1747-DPS1 port splitter with a 1761-CBL-AM00 (8-pin mini-DIN to 8-pin mini-DIN) cable or equivalent.

This type of connection damages the RS-232/RS-485 communication port (Channel 0) of the MicroLogix 1400 and/or the controller itself. The communication pins that are used for RS-485 communications on the MicroLogix 1400 are alternately used for 24V power on the other MicroLogix controllers and the network port of the 1747-DPS1 port splitter.

Program the MicroLogix 1400 controller using RSLogix 500/RSLogix Micro software, version 8.10.00 or later for Series A controllers and version 8.30.00 or later for Series B and Series C controllers. Communication cables for programming are available separately from the controller and software.

## Firmware Revision History

Features are added to the controllers through firmware updates. Use the listing in Table 1 to be sure that your controller's firmware is at the level you need. Firmware updates are not required, but they allow you to access to the new features.

## Communication Options

MicroLogix 1400 controllers provide three communications ports: an isolated combination RS-232/ RS-485 communication port (Channel 0), an Ethernet port (Channel 1), and a non-isolated RS-232 communication port (Channel 2).

You can connect Channel 0 and Channel 2 ports on the MicroLogix 1400 controller to the following:

- Operator interfaces, personal computers, and so on, with DF1 full-duplex point-to-point
- A DH-485 network
- A DF1 Radio Modem network
- A DF1 half-duplex network as an RTU master or RTU slave
- A Modbus network as an RTU master or RTU slave
- An ASCII network
- An Ethernet network using the Ethernet Interface module (catalog number 1761-NET-ENI, or 1761-NET-ENIW)
- A DNP3 network as a slave

When connecting to an RS-485 network with DH-485, DF1 half-duplex master/slave, Modbus RTU master/slave, or DNP3 slave protocols, you can connect the MicroLogix 1400 controller directly via Channel 0 without an Advanced Interface Converter, catalog number 1761-NET-AIC. The Channel 0 combo port provides both RS-232 and RS-485 isolated connections. The appropriate electrical interface is selected through your choice of communication cable. The existing MicroLogix 1761 communication cables provide an interface to the RS-232 drivers. The 1763-NC01 cable provides an interface to the RS-485 drivers.

You can also connect the controller to serial devices, such as barcode readers, weigh scales, serial printers, and other intelligent devices, using ASCII. See Default Communication Configuration on page 57 for the configuration settings for Channel 0. MicroLogix 1400 controller can be connected directly to the RS-485 network via channel 0, using ASCII.

The MicroLogix 1400 supports EtherNet/IP™ communication via the Ethernet communication Channel 1. In addition, either Modbus TCP or DNP3 over IP can be enabled for Channel 1. You can connect your controller to a local area network that provides communication between various devices at 10 Mbps or 100 Mbps. This port supports CIP explicit messaging (message exchange) only. The controller cannot be used for CIP implicit messaging (real-time I/O messaging). The controller also includes an embedded web server that allows viewing of not only module information, TCP/IP configuration, and diagnostic information, but also includes the data table memory map and data table monitor screen using a standard web browser.

See Chapter 4 for more information on how to connect to the available communication options.

## Notes:

## Installation Considerations

## Safety Considerations

## Install Your Controller

Most applications require installation in an industrial enclosure (Pollution Degree 2(a)) to reduce the effects of electrical interference (Over Voltage Category II (b) ) and environmental exposure. Locate your controller as far as possible from power lines, load lines, and other sources of electrical noise such as hard-contact switches, relays, and AC motor drives. For more information on proper grounding guidelines, see Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Vertical mounting of the controller is not supported due to heat build-up considerations.

ATTENTION: Be careful of metal chips when drilling mounting holes for your controller or other equipment within the enclosure or panel. Drilled fragments that fall into the controller or I/O modules could cause damage. Do not drill holes above a mounted controller if the protective debris shields are removed or the processor is installed.

WARNING: Do not place the MicroLogix 1400 programmable controller in direct sunlight. Prolonged exposure to direct sunlight could degrade the LCD display and have adverse effects on the controller.

The controller is not designed for outdoor use.

Safety considerations are an important element of proper system installation. Actively considering the safety of yourself and others, and the condition of your equipment, is of primary importance. We recommend reviewing the following safety considerations.

## Hazardous Location Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D, or non-hazardous locations only. The following WARNING statement applies to use in hazardous locations.

(a) Pollution Degree 2 is an environment where normally only non-conductive pollution occurs except that occasionally temporary conductivity caused by condensation shall be expected.

(b) Overvoltage Category II is the load level section of the electrical distribution system. At this level, transient voltages are controlled and do not exceed the impulse voltage capability of the products insulation.

<!-- image -->

<!-- image -->

## WARNING: EXPLOSION HAZARD

- Substitution of components may impair suitability for Class I Division 2.
- Do not replace components or disconnect equipment unless power has been switched off.
- Do not connect or disconnect components unless power has been switched off.
- This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.
- All wiring must comply with N.E.C. article 501-10(b) and/or in accordance with Section 18-1J2 of the Canadian Electrical Code, and in accordance with the authority having jurisdiction.
- For applicable equipment (for example, relay modules), exposure to some chemicals may degrade the sealing properties of the materials that are used in these devices:
- Relays, epoxy

It is recommended that you periodically inspect these devices for any degradation of properties and replace the module if degradation is found.

Use only the following communication cables in Class I Division 2 hazardous locations.

| Environment Classification Communication Cables   |                                 |
|---------------------------------------------------|---------------------------------|
| Class I Division 2 Hazardous Environment          | 1761-CBL-AC00 Series C or later |
| Class I Division 2 Hazardous Environment          | 1761-CBL-AM00 Series C or later |
| Class I Division 2 Hazardous Environment          | 1761-CBL-AP00 Series C or later |
| Class I Division 2 Hazardous Environment          | 1761-CBL-PM02 Series C or later |
| Class I Division 2 Hazardous Environment          | 1761-CBL-HM02 Series C or later |
| Class I Division 2 Hazardous Environment          | 2707-NC9 Series C or later      |
| Class I Division 2 Hazardous Environment          | 1763-NC01 Series A or later     |
| Class I Division 2 Hazardous Environment          | 1747-CP3 Series                 |

## Disconnect Main Power

<!-- image -->

WARNING: Explosion Hazard

Do not replace components, connect equipment, or disconnect equipment unless power has been switched off.

The main power disconnect switch should be located where operators and maintenance personnel have quick and easy access to it. In addition to disconnecting electrical power, all other sources of power (pneumatic and hydraulic) should be de-energized before working on a machine or process that is controlled by a controller.

## Safety Circuits

<!-- image -->

WARNING: Explosion Hazard

Do not connect or disconnect connectors while the circuit is live.

Circuits installed on the machine for safety reasons, like overtravel limit switches, stop push buttons, and interlocks, should always be hard-wired directly to the master control relay. These devices must be wired in series so that when any one device opens, the master control relay is deenergized, which removes power to the machine. Never alter these circuits to defeat their function. Serious injury or machine damage could result.

## Power Distribution

There are some points about power distribution that you should know:

## Power Considerations

- The master control relay must be able to inhibit all machine motion by removing power to the machine I/O devices when the relay is de-energized. It is recommended that the controller remain powered even when the master control relay is de-energized.
- If you are using a DC power supply, interrupt the load side rather than the AC line power. This avoids the additional delay of power supply turn-off. The DC power supply should be powered directly from the fused secondary of the transformer. Power to the DC input and output circuits should be connected through a set of master control relay contacts.

## Proof Tests of Master Control Relay Circuit

Any part can fail, including the switches in a master control relay circuit. The failure of one of these switches could cause an open circuit, which is a safe power-off failure. However, if one of these switches shorts out, it no longer provides any safety protection. These switches should be tested periodically to verify that they stop machine motion when needed.

The following explains the power considerations for the micro controllers.

## Isolation Transformers

Consider using an isolation transformer in the AC line to the controller. This type of transformer provides isolation from your power distribution system to reduce the electrical noise that enters the controller and is often used as a step-down transformer to reduce line voltage. Any transformer that is used with the controller must have a sufficient power rating for its load. The power rating is expressed in volt-amperes (VA).

## Power Supply Inrush

During power-up, the MicroLogix 1400 power supply allows a brief inrush current to charge internal capacitors. Many power lines and control transformers can supply inrush current for a brief time. If the power source cannot supply this inrush current, the source voltage could sag momentarily.

The only effect of limited inrush current and voltage sag on the MicroLogix 1400 is that the power supply capacitors charge more slowly. However, consider the effect of a voltage sag on other equipment. For example, a deep voltage sag could reset a computer that is connected to the same power source. The following considerations determine whether the power source is required to supply a high inrush current:

- The power-up sequence of devices in a system
- The amount of the power source voltage sag if the inrush current cannot be supplied
- The effect of voltage sag on other equipment in the system

If the entire system is powered-up simultaneously, a brief sag in the power source voltage typically does not affect any equipment.

## Loss of Power Source

The power supply is designed to withstand brief power losses without affecting the operation of the system. The time that the system is operational during power loss is called program scan holdup time after loss of power. The duration of the power supply hold-up time depends on the type and state of the I/O, but is typically between 10 milliseconds and 3 seconds. When the duration of power loss reaches this limit, the power supply signals the processor that it can no longer provide adequate DC power to the system. This is referred to as a power supply shutdown. The processor then performs an orderly shutdown of the controller.

## Input States on Power Down

The power supply hold-up time previously described is longer than the turn-on and turn-off times of the inputs. Because of this, the input state change from On to Off that occurs when power is removed could be recorded by the processor before the power supply shuts down the system.

## Master Control Relay

Understanding this concept is important. The user program should be written to take this effect into account.

## Other Types of Line Conditions

Occasionally the power source to the system can be temporarily interrupted. It is also possible that the voltage level drops substantially below the normal line voltage range for a period of time. Both of these conditions are considered to be a loss of power for the system.

Help Prevent Excessive Heat For most applications, normal convective cooling keeps the controller within the specified operating range. Confirm that the specified temperature range is maintained. Proper spacing of components within an enclosure is sufficient for heat dissipation.

In some applications, a substantial amount of heat is produced by other equipment inside or outside the enclosure. In this case, place blower fans inside the enclosure to help with air circulation and to reduce hot spots near the controller.

Additional cooling provisions might be necessary when high ambient temperatures are encountered.

<!-- image -->

Do not bring in unfiltered outside air. Place the controller in an enclosure to protect it from a corrosive atmosphere. Harmful contaminants or dirt could cause improper operation or damage to components. In extreme cases, you can use air conditioning to protect against heat build-up within the enclosure.

A hard-wired master control relay (MCR) provides a reliable means for emergency machine shutdown. Since the master control relay allows the placement of several emergency stop switches in different locations, its installation is important from a safety standpoint. Overtravel limit switches or mushroom-head push buttons are wired in series so that when any of them opens, the master control relay is de-energized. This removes power to input and output device circuits. See Figure 4 on page 23 and Figure 5 on page 24 .

<!-- image -->

ATTENTION: Never alter these circuits to defeat their function since serious injury and/or machine damage could result.

<!-- image -->

If you are using an external DC power supply, interrupt the DC output side rather than the AC line side of the supply to avoid the additional delay of power supply turn-off. The AC line of the DC output power supply should be fused.

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

Figure 4 and Figure 5 show the master control relay wired in a grounded system.

<!-- image -->

In most applications input circuits do not require MCR protection; however, if you must remove power from all field devices, you must include MCR contacts in series with input power wiring.

Figure 4 - Schematic (Using IEC Symbols)

<!-- image -->

Figure 5 - Schematic (Using ANSI/CSA Symbols)

<!-- image -->

## Install a Memory Module

To install the memory module, do as follows:

1. Remove the memory module port cover.
2. Align the connector on the memory module with the connector pins on the controller.
3. Firmly seat the memory module into the controller.

<!-- image -->

<!-- image -->

## Use the Battery

<!-- image -->

4. Use a screwdriver as in step 1 to remove the memory module in the future.

The MicroLogix 1400 controller is equipped with a replaceable battery (catalog number 1747-BA). The Battery Low indicator on the LCD display of the controller shows the status of the replaceable battery. When the battery is low, the indicator is set (displayed as a solid rectangle). This means that either the battery wire connector is disconnected, or the battery fails within 2 weeks if it is connected.

## IMPORTANT

The MicroLogix 1400 controller ships with the battery wire connector connected. Ensure that the battery wire connector is inserted into the connector port if your application needs battery power. For example, when using a real-time clock (RTC).

If yo9u replace the battery when the controller is powered down you will lose all user application memory. Replace the battery when the controller is powered on.

See Guidelines for Handling Lithium Batteries Installation Instructions, publication 1747-IN515, for more information on installation, handling, usage, storage, and disposal of the battery.

See RTC Battery Operation on page 119, for more information on the use of the battery in relation with RTC.

<!-- image -->

WARNING: When you connect or disconnect the battery an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that the area is nonhazardous before proceeding.

For Safety information on the handling of lithium batteries, including handling and disposal of leaking batteries, see the Guidelines for Handling Lithium Batteries Technical Data, publication AG-TD054 .

## IMPORTANT

When the controller's Battery Low indicator is set (displayed as a solid rectangle) with the battery wire connector connected, you should install a new battery immediately.

## Connect the Battery Wire Connector

To connect the battery wire connector to the battery connector, do as follows:

1. Insert the replaceable battery wire connector into the controller's battery connector.
2. Secure the battery connector wires so that it does not block the 1762 expansion bus connector as shown in Figure 6 on page 26 .

## Controller Mounting Dimensions

Figure 6 - Secure Battery Connector Wires

<!-- image -->

Mounting Dimensions

<!-- image -->

1766-L32BWA, 1766-L32AWA, 1766-L32BXB, 1766-L32BWAA, 1766-L32AWAA, 1766-L32BXBA

| Dimension Measurement   |
|-------------------------|
| A 90 mm (3.5 in.)       |
| B 180 mm (7.087 in.)    |
| C 87 mm (3.43 in.)      |

## Controller and Expansion I/O Spacing

## Mount the Controller

The controller mounts horizontally, with the expansion I/O extending to the right of the controller. Allow 50 mm (2 in.) of space on all sides of the controller system for adequate ventilation. Maintain spacing from enclosure walls, wireways, adjacent equipment, and so on, as shown in Figure 7 .

Figure 7 - Controller Spacing

<!-- image -->

MicroLogix 1400 controllers are suitable for use in an industrial environment when installed in accordance with these instructions. Specifically, this equipment is intended for use in clean, dry environments (Pollution degree 2 (a) ) and to circuits not exceeding Over Voltage Category II (b) (IEC 60664-1).(c)

<!-- image -->

<!-- image -->

ATTENTION: Do not remove the protective debris shield until after the controller and all other equipment in the panel near the controller are mounted and wiring is complete. Once wiring is complete, remove protective debris shield. Failure to remove shield before operating can cause overheating.

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

<!-- image -->

For environments with greater vibration and shock concerns, use the panel mounting method described on page 28, rather than DIN rail mounting.

## DIN Rail Mounting

The maximum extension of the latch is 14 mm (0.55 in.) in the open position. A flat-blade screwdriver is required for removal of the controller. The controller can be mounted to EN5002235x7.5 or EN50022-35x15 DIN rails. DIN rail mounting dimensions are shown below.

(a) Pollution Degree 2 is an environment where, normally, only non-conductive pollution occurs except that occasionally a temporary conductivity caused by condensation shall be expected.

(b) Over Voltage Category II is the load level section of the electrical distribution system. At this level transient voltages are controlled and do not exceed the impulse voltage capability of the product's insulation.

(c) Pollution Degree 2 and Over Voltage Category II are International Electrotechnical Commission (IEC) designations.

## Mount on DIN Rail

<!-- image -->

| Dimension Height     |
|----------------------|
| A 90 mm (3.5 in.)    |
| B 27.5 mm (1.08 in.) |
| C 27.5 mm (1.08 in.) |

To install your controller on the DIN rail, do as follows:

1. Mount your DIN rail. (Make sure that the placement of the controller on the DIN rail meets the recommended spacing requirements, see Controller and Expansion I/O Spacing on page 27 . See the mounting template inside the back cover of this document.)
2. Close the DIN latch, if it is open.
3. Hook the top slot over the DIN rail.
4. While pressing the controller down against the top of the rail, snap the bottom of the controller into position.
5. Leave the protective debris shield attached until you are finished wiring the controller and any other devices.

To remove your controller from the DIN rail:

1. Place a flat-blade screwdriver in the DIN rail latch at the bottom of the controller.
2. Holding the controller, pry downward on the latch until the latch locks in the open position.
3. Repeat steps 1 and 2 for the second DIN rail latch.
4. Unhook the top of the DIN rail slot from the rail.

<!-- image -->

## Panel Mounting

Mount to panel using #8 or M4 screws. To install your controller using mounting screws:

1. Remove the mounting template from inside the back cover of MicroLogix 1400 Programmable Controllers Installation Instructions, publication 1766-IN001 .
2. Secure the template to the mounting surface. Make sure your controller is spaced properly. See Controller and Expansion I/O Spacing on page 27 .
3. Drill holes through the template.
4. Remove the mounting template.
5. Mount the controller.

<!-- image -->

## 1762 Expansion I/O Module Dimensions

## Mount 1762 Expansion I/O Modules

6. Leave the protective debris shield in place until you are finished wiring the controller and any other devices.

<!-- image -->

Expansion I/O Module Dimensions

<!-- image -->

| Dimension Measurement   |
|-------------------------|
| A 90 mm (3.5 in.)       |
| B 40 mm (1.57 in.)      |
| C 87 mm (3.43 in.)      |

<!-- image -->

ATTENTION: During panel or DIN rail mounting of all devices, be sure that all debris such as metal chips and wire stands, is kept from falling into the module. Debris that falls into the module could cause damage when the module is under power.

## DIN Rail Mounting

The module can be mounted using the following DIN rails:

- 35 x 7.5 mm (EN 50 022 – 35 x 7.5), or
- 35 x 15 mm (EN 50 022 – 35 x 15).

Before mounting the module on a DIN rail, close the DIN rail latch. Press the DIN rail mounting area of the module against the DIN rail. The latch momentarily opens and locks into place.

Use DIN rail end anchors (Allen-Bradley part number 1492-EA35 or 1492-EAH35) for vibration or shock environments. Figure 8 shows the location of the end anchors.

## Connect Expansion I/O Modules

Figure 8 - End Anchor Position

<!-- image -->

<!-- image -->

1762 expansion I/O modules must be mounted horizontally as illustrated.

<!-- image -->

For environments with greater vibration and shock concerns, use the panel mounting method described below, instead of DIN rail mounting.

## Panel Mounting

Use the dimensional template shown in Figure 9 to mount the module. The preferred mounting method is to use two M4 or #8 pan head screws per module. Mounting screws are required on every module.

## Figure 9 - Dimensional Template

For more than 2 modules: (number of modules – 1) x 40 mm (1.59 in.)

<!-- image -->

The expansion I/O module is attached to the controller or another I/O module by means of a flat ribbon cable after mounting, as shown in Figure 10 .

Figure 10 - Attach Expansion I/O Modules

<!-- image -->

<!-- image -->

Use the pull loop on the connector to disconnect modules. Do not pull on the ribbon cable.

<!-- image -->

You can connect up to seven expansion I/O modules to a controller.

<!-- image -->

<!-- image -->

ATTENTION: Remove power before removing or inserting an I/O module. When you remove or insert a module with power applied, an electrical arc may occur. An electrical arc can cause personal injury or property damage by:

- Sending an erroneous signal to your system's field devices, causing the controller to fault
- Causing an explosion in a hazardous environment

Electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance, reducing product reliability.

WARNING: EXPLOSION HAZARD

In Class I Division 2 applications, the bus connector must be fully seated and the bus connector cover must be snapped in place.

In Class I Division 2 applications, all modules must be mounted in direct contact with each other as shown on page 23. If DIN rail mounting is used, an end stop must be installed ahead of the controller and after the last 1762 I/O module.

## Notes:

## Wiring Requirements

## Wire Your Controller

## Wiring Recommendation

<!-- image -->

ATTENTION: Before you install and wire any device, disconnect power to the controller system.

<!-- image -->

ATTENTION: Calculate the maximum possible current in each power and common wire. Observe all electrical codes dictating the maximum current allowable for each wire size. Current above the maximum ratings may cause wiring to overheat, which can cause damage.

United States Only: If the controller is installed within a potentially hazardous environment, all wiring must comply with the requirements stated in the National Electrical Code 501-10 (b).

- Allow for at least 50 mm. (2 in.) between I/O wiring ducts or terminal strips and the controller.
- Route incoming power to the controller by a path separate from the device wiring. Where paths must cross, their intersection should be perpendicular.

<!-- image -->

Do not run signal or communications wiring and power wiring in the same conduit. Wires with different signal characteristics should be routed by separate paths.

- Separate wiring by signal type. Bundle wiring with similar electrical characteristics together.
- Separate input wiring from output wiring.
- Label wiring to all devices in the system. Use tape, shrink-tubing, or other dependable means for labeling purposes. In addition to labeling, use colored insulation to identify wiring based on signal characteristics. For example, you can use blue for DC wiring and red for AC wiring.

Table 2 - Wire Requirements

| Wire Type   | Wire Size (2 wire maximum per terminal screw)    | Wire Size (2 wire maximum per terminal screw)   |
|-------------|--------------------------------------------------|-------------------------------------------------|
|             | 1 wire per terminal 2 wire per terminal          |                                                 |
|             | Solid Cu-90°C (194°F) #12…#20 AWG #16…#20 AWG    |                                                 |
|             | Stranded Cu-90°C (194°F) #14…#20 AWG #18…#20 AWG |                                                 |

## Wire without Spade Lugs

When wiring without spade lugs, we recommend that you keep the finger-safe covers in place. Loosen the terminal screw and route the wires through the opening in the finger-safe cover. Tighten the terminal screw making sure the pressure plate secures the wire.

<!-- image -->

## Use Surge Suppressors

<!-- image -->

## Wire with Spade Lugs

The diameter of the terminal screw head is 5.5 mm (0.220 in.). The input and output terminals of the MicroLogix 1400 controller are designed for a 6.35 mm (0.25 in.) wide spade (standard for #6 screw for up to 14 AWG) or a 4 mm (metric #4) fork terminal.

When using spade lugs, use a small, flat-blade screwdriver to pry the finger-safe cover from the terminal blocks as shown below. Then loosen the terminal screw.

<!-- image -->

Because of the potentially high current surges that occur when switching inductive load devices, such as motor starters and solenoids, the use of some type of surge suppression to protect and extend the operating life of the controllers output contacts is required. Switching inductive loads without surge suppression can significantly reduce the life expectancy of relay contacts. By adding a suppression device directly across the coil of an inductive device, you prolong the life of the output or relay contacts. You also reduce the effects of voltage transients and electrical noise from radiating into adjacent systems.

Figure 11 shows an output with a suppression device. We recommend that you locate the suppression device as close as possible to the load device.

Figure 11 - Output with Suppression Device

<!-- image -->

If the outputs are DC, we recommend that you use a 1N4004 diode for surge suppression, as shown below. For inductive DC load devices, a diode is suitable. A 1N4004 diode is acceptable for most applications. A surge suppressor can also be used. Table 3 on page 36 for recommended suppressors. As shown below, these surge suppression circuits connect directly across the load device.

<!-- image -->

Suitable surge suppression methods for inductive AC load devices include a varistor, an RC network, or an Allen-Bradley surge suppressor, all shown below. These components must be appropriately rated to suppress the switching transient characteristic of the particular inductive device. See Recommended Surge Suppressors on page 35 for recommended suppressors.

Figure 12 - Surge Suppression for Inductive AC Load Devices

<!-- image -->

## Recommended Surge Suppressors

Use the Allen-Bradley surge suppressors shown in Table 3 for use with relays, contactors, and starters.

Table 3 - Recommended Surge Suppressors

|                                                               | Device Coil Voltage Suppressor Catalog Number   | Type(1)   |
|---------------------------------------------------------------|-------------------------------------------------|-----------|
|                                                               | 24…48V AC 100-KFSC50                            |           |
|                                                               | 110…280V AC 100-KFSC280                         | RC        |
|                                                               | 380…480V AC 100-KFSC480                         |           |
| Bulletin 100/104K 700K                                        | 12…55 V AC, 12…77V DC 100-KFSV55                | MOV       |
| Bulletin 100/104K 700K                                        | 56…136 VAC, 78…180V DC 100-KFSV136              | MOV       |
| Bulletin 100/104K 700K                                        | 137…277V AC, 181…250 V DC 100-KFSV277           | MOV       |
| Bulletin 100/104K 700K                                        | 12…250V DC 100-KFSD250 Diode                    |           |
| Bulletin 100C, (C09…C97)                                      | 24…48V AC  100-FSC48(2)                         | RC (1)    |
| Bulletin 100C, (C09…C97)                                      | 110…280V AC  100-FSC280                         | RC (1)    |
| Bulletin 100C, (C09…C97)                                      | 380…480V AC  100-FSC480(1)                      | RC (1)    |
|                                                               | 12…55V AC, 12…77V DC  100-FSV55(1)              | MOV       |
|                                                               | 56…136V AC, 78…180V DC  100-FSV136(1)           | MOV       |
|                                                               | 137…277V AC, 181…250V DC  100-FSV277(1)         | MOV       |
|                                                               | 278…575V AC  100-FSV575(1)                      | MOV       |
|                                                               | 12…250V DC  100-FSD250(1)                       | Diode     |
| Bulletin 509 motor starter size 0…5                           | 12…120V AC 599-K04                              | MOV       |
| Bulletin 509 motor starter size 0…5                           | 240…264V AC 599-KA04                            | MOV       |
| Bulletin 509 motor starter size 6                             | 12…120V AC  199-FSMA1(3)                        | RC        |
| Bulletin 509 motor starter size 6                             | 12…120V AC  199-GSMA1(4)                        | MOV       |
| Bulletin 700 R/RM relay                                       | AC coil Not Required                            | MOV       |
| Bulletin 700 R/RM relay                                       | 24…48V DC 199-FSMA9                             | MOV       |
| Bulletin 700 R/RM relay                                       | 50…120V DC 199-FSMA10                           | MOV       |
| Bulletin 700 R/RM relay                                       | 130…250V DC 199-FSMA11                          | MOV       |
| Bulletin 700 Type N, P, PK or PH relay                        | 6…150V AC/DC 700-N24 RC                         |           |
|                                                               | 24…48V AC/DC 199-FSMA9                          | MOV       |
|                                                               | 50…120V AC/DC 199-FSMA10                        | MOV       |
|                                                               | 130…250V AC/DC 199-FSMA11                       |           |
|                                                               | 6…300V DC 199-FSMZ-1 Diode                      |           |
| Miscellaneous electromagnetic devices limited to 35 sealed VA | 6…150V AC/DC 700-N24 RC                         |           |

Varistor is not recommended for use on the relay outputs.

(2) Catalog numbers for screw-less terminals include the string CR after 100-.

For example: Catalog number 100-FSC48 becomes catalog number 100-CRFSC48; Catalog number 100-FSV55 becomes 100-CRFSV55; and so on.

(3) For use on the interposing relay

(4) For use on the contactor or starter

## Ground the Controller

In solid-state control systems, grounding and wire routing helps limit the effects of noise due to electromagnetic interference (EMI). Run the ground connection from the ground screw of the controller to the ground bus prior to connecting any devices. Use AWG #14 wire. For AC-powered controllers, this connection must be made for safety purposes.

<!-- image -->

ATTENTION: All devices connected to the RS-232/485 communication port must be referenced to controller ground, or be floating (not referenced to a potential other than ground). Failure to follow this procedure may result in property damage or personal injury.

- For 1766-L32BWA and 1766-L32BWAA controllers, the COM of the sensor supply is also connected to chassis ground internally. The 24V DC sensor power source should not be used to power output circuits. It should only be used to power input devices.
- For 1766-L32BXB and 1766-L32BXBA controllers, the VDC NEUT or common terminal of the power supply is also connected to chassis ground internally.

## Wiring Diagrams

This product is intended to be mounted to a well grounded mounting surface such as a metal panel. See Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional information. Additional grounding connections from the mounting tab or DIN rail, if used, are not required unless the mounting surface cannot be grounded.

<!-- image -->

Use all four mounting positions for panel mounting installation.

<!-- image -->

<!-- image -->

ATTENTION: Remove the protective debris strip before applying power to the controller. Failure to remove the strip may cause the controller to overheat.

The following illustrations show the wiring diagrams for the MicroLogix 1400 controllers. Controllers with DC inputs can be wired as either sinking or sourcing inputs. Sinking and sourcing does not apply to AC inputs. See Sinking and Sourcing Wiring Diagrams on page 40 .

Figure 13 to Figure 15 show the controller terminal block layouts. The shading on the labels indicates how the terminals are grouped.

<!-- image -->

This symbol denotes a protective earth ground terminal which provides a low impedance path between electrical circuits and earth for safety purposes and provides noise immunity improvement. This connection must be made for safety purposes on AC-powered controllers.

<!-- image -->

<!-- image -->

This symbol denotes a functional earth ground terminal which provides a low impedance path between electrical circuits and earth for non-safety purposes, such as noise immunity improvement.

## Terminal Block Layouts

<!-- image -->

ATTENTION: When you connect or disconnect the Removable Terminal Block (RTB) with field side power applied, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

WARNING: When used in a Class I Division 2, hazardous location, this equipment must be mounted in a suitable enclosure. All wiring must be in accordance with Class I Division 2 wiring methods of Article 501 of the National Electrical Code and/or in accordance with Section 18-1J2 of the Canadian Electrical Code, and in accordance with the authority having jurisdiction.

Figure 13 - 1766-L32BWA/L32BWAA

<!-- image -->

Input terminal block

<!-- image -->

<!-- image -->

Output terminal block

ATTENTION: The 24V DC sensor supply of the 1766-L32BWA and 1766-L32BWAA controllers should not be used to power output circuits. It should only be used to power input devices, for example, sensors and switches. See Master Control Relay on page 22 for information on MCR wiring in output circuits.

Figure 14 - 1766-L32AWA/L32AWAA

Input terminal block

<!-- image -->

<!-- image -->

Output terminal block

Table 5 - Output Terminal Grouping

|                           | Controllers Output Group Description Voltage Terminal  Output Terminal   |
|---------------------------|--------------------------------------------------------------------------|
| 1766-L32BWA 1766--L32BWAA | Group 0 Isolated relay output VAC/DC0 OUT 0                              |
| 1766-L32BWA 1766--L32BWAA | Group 1 Isolated relay output VAC/DC1 OUT 1                              |
| 1766-L32BWA 1766--L32BWAA | Group 2 Isolated relay output VAC/DC2 OUT 2                              |
| 1766-L32BWA 1766--L32BWAA | Group 3 Isolated relay output VAC/DC3 OUT 3                              |
| 1766-L32BWA 1766--L32BWAA | Group 4 Isolated relay output VAC/DC4 OUT 4, OUT 5                       |
| 1766-L32BWA 1766--L32BWAA | Group 5 Isolated relay output VAC/DC5 OUT 6, OUT 7                       |
| 1766-L32BWA 1766--L32BWAA | Group 6 Isolated relay output VAC/DC6 OUT 8…11                           |
| 1766-L32AWA 1766-L32AWAA  | Group 0 Isolated relay output VAC/DC0 OUT 0                              |
| 1766-L32AWA 1766-L32AWAA  | Group 1 Isolated relay output VAC/DC1 OUT 1                              |
| 1766-L32AWA 1766-L32AWAA  | Group 2 Isolated relay output VAC/DC2 OUT 2                              |
| 1766-L32AWA 1766-L32AWAA  | Group 3 Isolated relay output VAC/DC3 OUT 3                              |
| 1766-L32AWA 1766-L32AWAA  | Group 4 Isolated relay output VAC/DC4 OUT 4, OUT 5                       |
| 1766-L32AWA 1766-L32AWAA  | Group 5 Isolated relay output VAC/DC5 OUT 6, OUT 7                       |
| 1766-L32AWA 1766-L32AWAA  | Group 6 Isolated relay output VAC/DC6 OUT 8…11                           |
| 1766-L32BXB 1766-L32BXBA  | Group 0 Isolated relay output VAC/DC0 OUT 0                              |
| 1766-L32BXB 1766-L32BXBA  | Group 1 Isolated relay output VAC/DC1 OUT 1                              |
| 1766-L32BXB 1766-L32BXBA  | Group 2 FET output VDC2/COM 2 OUT 2…7                                    |
| 1766-L32BXB 1766-L32BXBA  | Group 3 Isolated relay output VAC/DC3 OUT 8                              |
| 1766-L32BXB 1766-L32BXBA  | Group 4 Isolated relay output VAC/DC4 OUT 9                              |
| 1766-L32BXB 1766-L32BXBA  | Group 5 Isolated relay output VAC/DC5 OUT 10, OUT 11                     |

<!-- image -->

WARNING: If you connect or disconnect wiring while the field-side power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

Figure 15 - 1766-L32BXB/L32BXBA

Table 4 - Wire Types and Sizes

| Wire Type Wire Size                         |
|---------------------------------------------|
| Solid wire Cu-90 °CC (194 °FF) 14…22 AWG    |
| Stranded wire Cu-90 °CC (194 °FF) 16…22 AWG |

Wiring torque = 0.791 N•m (7 lb•in) rated

Input terminal block

<!-- image -->

<!-- image -->

Output terminal block

## Sinking and Sourcing Wiring Diagrams

<!-- image -->

WARNING: The local programming terminal port is intended for temporary use only and must not be connected or disconnected unless the area is free of ignitable concentrations of flammable gases or vapors.

Any of the MicroLogix 1400 DC embedded input groups can be configured as sinking or sourcing depending on how the DC COM is wired on the group.

|                | Type Definition                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sinking Input  | The input energizes when high-level voltage is applied to the input terminal (active high). Connect the power supply VDC (-) to the input group’s COM terminal. |
| Sourcing Input | The input energizes when low-level voltage is applied to the input terminal (active low). Connect the power supply VDC (+) to the input group’s COM terminal.   |

<!-- image -->

ATTENTION: The 24V DC sensor power source must not be used to power output circuits. It should only be used to power input devices (for example. sensors, switches). See Master Control Relay on page 22 for information on MCR wiring in output circuits.

## 1766-L32BWA, 1766-L32AWA, 1766-L32BXB, 1766-L32BWAA, 1766L32AWAA, 1766-L32BXBA Wiring Diagrams

<!-- image -->

In Figure 16 to Figure 22, lower case alphabetic subscripts are appended to commonterminal connections to indicate that different power sources may be used for different isolated groups, if desired.

Figure 16 - 1766-L32AWA/L32AWAA Input Wiring Diagram (1)

<!-- image -->

(1) Do not use "NOT USED" terminals as connection points.

Figure 17 - 1766-L32BWA/L32BWAA Sinking Input Wiring Diagram

gp g g

<!-- image -->

Figure 20 - 1766-L32BXB/L32BXBA Sourcing Input Wiring Diagram

<!-- image -->

<!-- image -->

Figure 21 - 1766-L32AWA/L32AWAA and 1766-L32BWA/L32BWAA Output Wiring Diagram

<!-- image -->

Figure 22 - 1766-L32BXB/L32BXBA Output Wiring Diagram

<!-- image -->

## Controller I/O Wiring

## Minimize Electrical Noise

Because of the variety of applications and environments where controllers are installed and operating, it is impossible to ensure that all environmental noise is removed by input filters. To help reduce the effects of environmental noise, install the MicroLogix 1400 system in a properly rated (for example, NEMA) enclosure. Make sure that the MicroLogix 1400 system is properly grounded.

A system may malfunction due to a change in the operating environment after a period of time. We recommend periodically checking system operation, particularly when new machinery or other noise sources are installed near the MicroLogix 1400 system.

## Wire Your Analog Channels

Analog input circuits can monitor voltage signals and convert them to serial digital data.

<!-- image -->

The controller does not provide loop power for analog inputs. Use a power supply that matches the transmitter specifications as shown.

The analog output can support a voltage function as shown in the following illustration.

Figure 23 - Analog Output

<!-- image -->

## Analog Channel Wiring Guidelines

Consider the following when wiring your analog channels:

- The analog common (COM) is connected to earth ground inside the module. These terminals are not electrically isolated from the system. They are connected to chassis ground.
- Analog channels are not isolated from each other.
- Use Belden 8761, or equivalent, shielded wire.
- Under normal conditions, the drain wire (shield) should be connected to the metal mounting panel (earth ground). Keep the shield connection to earth ground as short as possible.

- To ensure optimum accuracy for voltage type inputs, limit overall cable impedance by keeping all analog cables as short as possible. Locate the I/O system as close to your voltage type sensors or actuators as possible.
- The controller does not provide loop power for analog inputs. Use a power supply that matches the transmitter specifications as shown in Figure 24 .

Figure 24 - Analog Input Transmitter Specifications

<!-- image -->

## Minimize Electrical Noise on Analog Channels

Inputs on analog channels employ digital high-frequency filters that significantly reduce the effects of electrical noise on input signals. However, because of the variety of applications and environments where analog controllers are installed and operated, it is impossible to ensure that all environmental noise is removed by the input filters.

Several specific steps can be taken to help reduce the effects of environmental noise on analog signals:

- install the MicroLogix 1400 system in a properly rated enclosure, for example, NEMA. Make sure that the MicroLogix 1400 system is properly grounded.
- use Belden cable #8761 for wiring the analog channels, making sure that the drain wire and foil shield are properly earth grounded.
- route the Belden cable separately from any AC wiring. Additional noise immunity can be obtained by routing the cables in grounded conduit.

## Ground Your Analog Cable

Use shielded communication cable (Belden #8761). The Belden cable has two signal wires (black and clear), one drain wire, and a foil shield. The drain wire and foil shield must be grounded at one end of the cable.

IMPORTANT Do not ground the drain wire and foil shield at both ends of the cable

<!-- image -->

## Expansion I/O Wiring

## Digital Wiring Diagrams

Figure 25 to Figure 37 show the digital expansion I/O module wiring diagrams.

Figure 25 - 1762-IA8 Wiring Diagram

<!-- image -->

Figure 26 - 1762-IQ8 Wiring Diagram

<!-- image -->

Figure 27 - 1762-IQ16 Wiring Diagram

<!-- image -->

Figure 28 - 1762-IQ32T Wiring Diagram

<!-- image -->

Figure 29 - 1762-OA8 Wiring Diagram

<!-- image -->

Figure 30 - 1762-OB8 Wiring Diagram

<!-- image -->

Figure 31 - 1762-OB16 Wiring Diagram

<!-- image -->

Figure 32 - 1762-OB32T Wiring Diagram

<!-- image -->

Figure 33 - 1762-OV32T Wiring Diagram

<!-- image -->

Figure 34 - 1762-OW8 Wiring Diagram

<!-- image -->

Figure 35 - 1762-OW16 Wiring Diagram

<!-- image -->

Figure 36 - 1762-OX6I Wiring Diagram

<!-- image -->

Figure 37 - 1762-IQ8OW6 Wiring Diagram

<!-- image -->

## Analog Wiring

Consider the following when wiring your analog modules:

- The analog common (COM) is not connected to earth ground inside the module. All terminals are electrically isolated from the system.
- Channels are not isolated from each other.
- Use Belden 8761, or equivalent, shielded wire.
- Under normal conditions, the drain wire (shield) should be connected to the metal mounting panel (earth ground). Keep the shield connection to earth ground as short as possible.

- To ensure optimum accuracy for voltage type inputs, limit overall cable impedance by keeping all analog cables as short as possible. Locate the I/O system as close to your voltage type sensors or actuators as possible.
- The module does not provide loop power for analog inputs. Use a power supply that matches the input transmitter specifications.

## 1762-IF2OF2 Input Type Selection

Select the input type, current or voltage, using the switches located on the module's circuit board and the input type/range selection bits in the Configuration Data File. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001. You can access the switches through the ventilation slots on the top of the module. Switch 1 controls channel 0; switch 2 controls channel 1. The factory default setting for both switch 1 and switch 2 is Current. Switch positions are shown in Figure 38 .

## Figure 38 - 1762-IF2OF2 Switch Positions

1762-IF2OF2 Output Type Selection

<!-- image -->

The output type selection, current or voltage, is made by wiring to the appropriate terminals, Iout or Vout, and by the type/range selection bits in the Configuration Data File. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

<!-- image -->

ATTENTION: Analog outputs may fluctuate for less than a second when power is applied or removed. This characteristic is common to most analog outputs. While the majority of loads will not recognize this short signal, it is recommended that preventive measures be taken to ensure that connected equipment is not affected.

## 1762-IF2OF2 Wiring

Figure 39 shows the 1762-IF2OF2 analog expansion I/O terminal block.

## Figure 39 - 1762-IF2OF2 Terminal Block Layout

<!-- image -->

<!-- image -->

Figure 40 - Differential Sensor Transmitter Types

<!-- image -->

Figure 41 - Single-ended Sensor/Transmitter Types

<!-- image -->

(1) All power supplies are rated N.E.C. Class 2.

## 1762-IF4 Input Type Selection

Select the input type, current or voltage, using the switches located on the module's circuit board and the input type/range selection bits in the Configuration Data File. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001. You can access the switches through the ventilation slots on the top of the module.

Figure 42 - 1762-IF4 Switch Location

<!-- image -->

Figure 43 - 1762-IF4 Terminal Block Layout

<!-- image -->

Figure 44 - Differential Sensor Transmitter Types

<!-- image -->

<!-- image -->

Grounding the cable shield at the module end only usually provides sufficient noise immunity. However, for best cable shield performance, earth ground the shield at both ends, using a 0.01 µF capacitor at one end to block AC power ground currents, if necessary.

Figure 45 - Sensor/Transmitter Types

<!-- image -->

## 1762-OF4 Output Type Selection

The output type selection, current or voltage, is made by wiring to the appropriate terminals, I out or V out, and by the type/range selection bits in the Configuration Data File.

Figure 46 - 1762-OF4 Terminal Block Layout

<!-- image -->

Figure 47 - 1762-OF4 Wiring

<!-- image -->

## Notes:

## Supported Communication Protocols

## Default Communication Configuration

## Communication Connections

The method you use and cabling required to connect your controller depends on what type of system you are employing. This chapter also describes how the controller establishes communication with the appropriate network.

The MicroLogix 1400 controllers provide three communication channels, an isolated RS-232/RS-485 communication port (Channel 0), an Ethernet port (Channel 1) and a non-isolated RS-232 communication port (Channel 2).

MicroLogix 1400 controllers support the following communication protocols from the primary RS232/RS-485 communication channel 0 and the RS-232 communication channel 2:

- DH-485
- DF1 Full-duplex
- DF1 Half-duplex master and slave
- DF1 Radio modem
- Modbus RTU master and slave
- ASCII
- DNP3 slave

The Ethernet communication channel, Channel 1, allows you to connect your controller to a local area network for various devices providing 10 Mbps/100 Mbps transfer rate. MicroLogix 1400 controllers support EtherNet/IP with CIP explicit messaging (message exchange), BOOTP/DHCP Client, HTTP Server, SMTP Client, DNS Client, SNMP Server, Socket Interface with CIP Generic messaging, Modbus TCP Client/Server and DNP3 over IP. MicroLogix 1400 controllers do not support Ethernet I/O master capability through CIP implicit messaging (real-time I/O messaging).

For more information on MicroLogix 1400 communications, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

The MicroLogix 1400 communication Channel 0 has the following default communication configuration.

<!-- image -->

For Channel 0, the default configuration is present when:

- The controller is powered up for the first time.
- The communications toggle functionality specifies default communications (specified using the LCD Display. The DCOMM indicator on the LCD Display is on, that is, lit in solid rectangle).
- An OS upgrade is completed.

See LCD and Keypad on page 75 for more information on using the LCD Display.

See Connect to Networks Via RS-232/RS-485 Interface on page 169 for more information on communicating.

| Parameter Default           |
|-----------------------------|
| Baud Rate 19.2 Kbps         |
| Parity None                 |
| Source ID (Node Address) 1  |
| Control Line No handshaking |
| Error Detection CRC         |

Table 6 - DF1 Full-duplex Default Configuration Parameters

<!-- image -->

## Use the Communications Toggle Functionality

Table 6 - DF1 Full-duplex Default Configuration Parameters (Continued)

| Parameter Default                         |
|-------------------------------------------|
| Embedded Responses Auto detect            |
| Duplicate Packet (Message) Detect Enabled |
| ACK Timeout counts 50                     |
| NAK retries 3                             |
| ENQ retries 3                             |
| Stop Bits 1                               |
| Data Bits 8                               |

The Communications Toggle Functionality can be operated using the LCD display on the controller, as shown in Figure 48 .

Use the Communications Toggle Functionality to change from the user-defined communication configuration to the default communications mode and back on Channel 0. The Default Communications (DCOMM) indicator on the LCD display operates to show when the controller is in the default communications mode. Hold down the OK key more than 5 seconds to toggle the communication mode on the Main Menu screen.

Figure 48 - Main Menu Screen

<!-- image -->

<!-- image -->

The Communication Toggle Functionality only affects the communication configuration of Channel 0.

## Change Communication Configuration

Follow the procedure below to change from the user-defined communication configuration to the default communications mode and back. In this example, we start from the Main Menu screen of the LCD display, as shown. If necessary, press ESC repeatedly until you return to the Main Menu screen.

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items shown do not display on the Main Menu screen, scroll down the screen by pressing the Down key.
2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.

<!-- image -->

<!-- image -->

3. Select DCOMM Cfg using the Up and Down keys, and then press OK.
4. The DCOMM Configuration screen displays. In this example, the current status is Disable.

<!-- image -->

<!-- image -->

000000

## DCOMM Cfg: Enable Disable

The DCOMM status indicator, which is the fourth of the six indicators at the top left of the LED display, displays as an empty rectangle. It means that the communication configuration is set to a user-defined communication mode.

5. Use the Up arrow to change the indicator position so that it points to Enable. Press OK to change to the default communication mode.

DISP

<!-- image -->

## DICOMM Cfg: Enable Disable

The DCOMM Mode Change Notification screen display. It indicates that the communication configuration is changed to the default communication mode. The DCOMM status indicator displays a solid rectangle.

RUN Comms config set to DF1 default

RUN

RUN

## Connect to the RS-232 Port

Table 7 - Available Communication Cables

| Communication Cables Length                                                                          |
|------------------------------------------------------------------------------------------------------|
| 1761-CBL-AM00 Series C or later cables are required for Class I Div 2 applications. 45 cm (17.7 in.) |
| 1761-CBL-AP00 Series C or later cables are required for Class I Div 2 applications. 45 cm (17.7 in.) |
| 1761-CBL-PM02 Series C or later cables are required for Class I Div 2 applications. 2 m (6.5 ft)     |
| 1761-CBL-HM02 Series C or later cables are required for Class I Div 2 applications. 2 m (6.5 ft)     |
| 2707-NC9 Series C or later cables are required for Class I Div 2 applications. 15 m (49.2 ft)        |
| 1763-NC01 Series A or later 30 cm (11.8 in.)                                                         |
| 1747-CP3 Series A or later 3 m (9.8 ft)                                                              |

<!-- image -->

## ATTENTION: UNSUPPORTED CONNECTION

Do not connect a MicroLogix 1400 controller to another MicroLogix family controller such as MicroLogix 1200 or to the 1747-DPS1 Network port using a 1761-CBL-AM00 (8-pin mini-DIN to 8-pin mini-DIN) cable or equivalent.

This type of connection will cause damage to the RS-232/RS-485 communication port (Channel 0) of the MicroLogix 1400 and/or the controller itself. Communication pins used for RS-485 communications are alternately used for 24V power on the other MicroLogix controllers and the 1747-DPS1 network port.

## Make a DF1 Point-to-Point Connection

You can connect the MicroLogix 1400 programmable controller to your personal computer using a serial cable (1761-CBL-PM02) from your personal computer's serial port to the controller's Channel 0. The recommended protocol for this configuration is DF1 Full-Duplex.

You can connect a MicroLogix 1400 controller to your personal computer directly without using an external optical isolator, such as Advanced Interface Converter (AIC+), catalog number 1761-NETAIC, as shown in the illustration below, because Channel 0 is isolated within the controller.

If you change to the user-defined configuration from the default configuration mode by selecting Disable and pressing OK, the DCOMM Mode Change Notification displays.

<!-- image -->

6. Press ESC to return to the Advanced Set Menu screen, as shown in step 3 .

There are two ways to connect the MicroLogix 1400 programmable controller to your personal computer using the DF1 protocol: using a point-to-point connection, or using a modem. Descriptions of these methods follow.

<!-- image -->

ATTENTION: All devices connected to the RS-232/RS-485 communication port must be referenced to controller ground, or be floating (not referenced to a potential other than ground). Failure to follow this procedure may result in property damage or personal injury.

- For 1766-L32BWA controllers, the COM of the sensor supply is also connected to chassis ground internally. The 24V DC sensor power source should not be used to power output circuits. It should only be used to power input devices.
- For 1766-L32BXB controllers, the VDC NEUT or common terminal of the power supply is also connected to chassis ground internally.

<!-- image -->

- (1) Series C or later cables are required for Class I Div 2 applications.

## Modem

You can use modems to connect a personal computer to one MicroLogix 1400 controller (using DF1 Full-Duplex protocol), to multiple controllers (using DF1 Half-Duplex protocol), or Modbus RTU Slave protocol via Channel 0, as shown in the following illustration. See Connect to Networks Via RS-232/ RS-485 Interface on page 169 for information on types of modems you can use with the micro controllers.

## IMPORTANT

Do not attempt to use DH-485 protocol through modems under any circumstance. The communication timing using DH-485 protocol is not supported by modem communications.

<!-- image -->

- (1) Series C or later cables are required for Class I Div 2 applications.

You can connect a MicroLogix 1400 controller to your modem directly without using an external optical isolator, such as AIC+, catalog number 1761-NET-AIC, as shown in the illustration below, because Channel 0 is isolated within the controller.

## MicroLogix 1400 Channel 0 to Modem Cable Pinout

When connecting MicroLogix 1400 Channel 0 to a modem using an RS-232 cable, the maximum that the cable length may be extended is 15.24 m (50 ft).

| DTE Device MicroLogix 1400 Channel 0   | DCE Device (Modem or PanelView™ Terminal)   | DCE Device (Modem or PanelView™ Terminal)   |
|----------------------------------------|---------------------------------------------|---------------------------------------------|
|                                        | 8-Pin 25-Pin 9-Pin                          |                                             |
|                                        | 7 TXD TXD 2 3                               |                                             |
|                                        | 4 RXD RXD 3 2                               |                                             |
|                                        | 2 GND GND 7 5                               |                                             |
|                                        | 1 B(+) DCD 8 1                              |                                             |
|                                        | 8 A(-) DTR 20 4                             |                                             |
|                                        | 5 DCD DSR 6 6                               |                                             |
|                                        | 6 CTS CTS 5 8                               |                                             |
|                                        | 3 RTS RTS 4 7                               |                                             |

<!-- image -->

ATTENTION: Do not connect pins 1 and 8. This connection will cause damage to the RS-232/RS-485 communication port (channel 0) of the MicroLogix 1400 and/or the controller itself.

## Construct Your Own Modem Cable

If you construct your own modem cable, the maximum cable length is 15.24 m (50 ft) with a 25-pin or 9-pin connector. Figure 49 shows a typical pinout for constructing a straight-through cable.

Figure 49 - Typical Straight-through Cable Pinout

| Pins 4 and 6 are internally connected for 1766-LEC only   | AIC+ Optical isolator or 1766-LEC Channel 2   | AIC+ Optical isolator or 1766-LEC Channel 2   | AIC+ Optical isolator or 1766-LEC Channel 2   |
|-----------------------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| Pins 4 and 6 are internally connected for 1766-LEC only   |                                               | 9-pin 25-pin 9-pin                            |                                               |
| Pins 4 and 6 are internally connected for 1766-LEC only   |                                               | 3 TXD TXD 2 3                                 |                                               |
| Pins 4 and 6 are internally connected for 1766-LEC only   |                                               | 2 RXD RXD 3 2                                 |                                               |
| Pins 4 and 6 are internally connected for 1766-LEC only   |                                               | 5 GND GND 7 5                                 |                                               |
| Pins 4 and 6 are internally connected for 1766-LEC only   |                                               | 1 CD CD 8 1                                   |                                               |
|                                                           |                                               | 4 DTR DTR 20 4                                |                                               |
|                                                           |                                               | 6 DSR DSR 6 6                                 |                                               |
|                                                           |                                               | 8 CTS CTS 5 8                                 |                                               |
|                                                           |                                               | 7 RTS RTS 4 7                                 |                                               |

## Construct Your Own Null Modem Cable

If you construct your own null modem cable, the maximum cable length is 15.24m (50 ft) with a 25pin or 9-pin connector. Figure 50 shows a typical pinout.

## Figure 50 - Typical Null Modem Cable Pinout

<!-- image -->

| Optical isolator Modem   | Optical isolator Modem   | Optical isolator Modem   | Optical isolator Modem   |
|--------------------------|--------------------------|--------------------------|--------------------------|
| 9-pin 25-pin 9-pin       |                          |                          |                          |
| 3 TXD TXD 2 3            |                          |                          |                          |
| 2 RXD RXD 3 2            |                          |                          |                          |
| 5 GND GND 7 5            |                          |                          |                          |
| 1 CD CD 8 1              |                          |                          |                          |
| 4 DTR DTR 20 4           |                          |                          |                          |
| 6 DSR DSR 6 6            |                          |                          |                          |
| 8 CTS CTS 5 8            |                          |                          |                          |
| 7 RTS RTS 4 7            |                          |                          |                          |

## Connect to a DF1 Half-Duplex Network

Table 8 shows available parameters for a communication port that is configured for DF1 Halfduplex slave.

Table 8 - DF1 Half-Duplex Configuration Parameters

| Parameter Options                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                   | Baud Rate 300, 600, 1200, 2400, 4800, 9600, 19.2 Kbps, 38.4 Kbps                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                   | Parity none, even                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                   | Node Address 0...254 decimal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                   | Control Line no handshaking, half duplex modem (RTS/CTS handshaking, no handshaking (DH-485 network)                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Error Detection CRC, BCC          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| EOT Suppression                   | enabled, disabled When EOT Suppression is enabled, the slave does not respond when polled if no message is queued. This saves modem transmission power and time when there is no message to transmit.                                                                                                                                                                                                                                                                                                                                   |
| Duplicate Packet (Message) Detect | enabled, disabled Detects and eliminates duplicate responses to a message. Duplicate packets may be sent under noisy communication conditions if the sender’s Message Retries are not set to 0.                                                                                                                                                                                                                                                                                                                                         |
| Poll Timeout (x20 ms)             | 0...65,535 (can be set in 20 ms increments) Poll Timeout only applies when a slave device initiates a MSG instruction. It is the amount of time that the slave device waits for a poll from the master device. If the slave device does not receive a poll within the Poll Timeout, a MSG instruction error is generated, and the ladder program needs to re-queue the MSG instruction. If you are using a MSG instruction, it is recommended that a Poll Timeout value of zero not be used. Poll Timeout is disabled when set to zero. |
| RTS Off Delay (x20 ms)            | 0...65,535 (can be set in 20 ms increments) Specifies the delay time between when the last serial character is sent to the modem and when RTS is deactivated. Gives the modem extra time to transmit the last character of a packet.                                                                                                                                                                                                                                                                                                    |
| RTS Send Delay (x20 ms)           | 0...65,535 (can be set in 20 ms increments) Specifies the time delay between setting RTS until checking for the CTS response. For use with modems that are not ready to respond with CTS immediately upon receipt of RTS.                                                                                                                                                                                                                                                                                                               |
| Message Retries                   | 0...255 Specifies the number of times a slave device attempts to resend a message packet when it does not receive an ACK from the master device. For use in noisy environments where message packets may become corrupted in transmission.                                                                                                                                                                                                                                                                                              |
| Pre Transmit Delay (x1 ms)        | 0...65,535 (can be set in 1 ms increments) • When the Control Line is set to no handshaking, this is the delay time before transmission. Required for 1761-NET-AIC physical Half duplex networks. The 1761-NET-AIC needs delay time to change from transmit to receive mode. • When the Control Line is set to DF1 Half-duplex modem, this is the minimum time delay between receiving the last character of a packet and the RTS assertion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

DF1 Half-duplex Master/Slave Network

Use Figure 51 for DF1 Half-duplex master/slave protocol without hardware handshaking.

Figure 51 - DF1 Half-duplex Master/Slave Protocol

<!-- image -->

(1) DB-9 RS-232 port

(2) Mini-DIN 8 RS-232 port

(3) RS-485 port

(4)Series C or later cables are required for Class I Div 2 applications.

## DF1 Half-Duplex Network (Using PC and Modems)

<!-- image -->

## Connect to a RS-485 Network

The network diagrams on the next pages provide examples of how to connect MicroLogix 1400 controllers to the RS-485 network.

You can connect a MicroLogix 1400 controller to your RS-485 network directly without using an external optical isolator, such as Advanced Interface Converter (AIC+), catalog number 1761-NETAIC, as shown in the illustrations below, because Channel 0 is isolated within the controller.

<!-- image -->

Use a 1763-NC01 Series A or later (8-pin mini-DIN to 6-pin RS-485 connector) cable or equivalent to connect a MicroLogix 1400 controller to a RS-485 network.

<!-- image -->

MicroLogix 1400 controllers support various protocols on the RS-485 network, including DH-485, DF1 Half-duplex master/slave, Modbus RTU master/slave, ASCII and DNP3 slave protocols. In this section, DH-485 protocol is used as an example. Any physical connection should be the same as other protocols.

## DH-485 Configuration Parameters

When MicroLogix communications are configured for DH-485, the following parameters can be changed:

Table 9 - DH-485 Configuration Parameters

| Parameter Options           |
|-----------------------------|
| Baud Rate 9600, 19.2 Kbps   |
| Node Address 1...31 decimal |
| Token Hold Factor 1...4     |

See Software Considerations on page 174 for tips on setting the parameters listed in Table 9 .

DH-485 Network with a MicroLogix 1400 Controller

Typical 3-Node Network (Channel 0 Connection)

<!-- image -->

PanelView 550

<!-- image -->

## Recommended Tools

To connect a DH-485 network to additional devices, you need tools to strip the shielded cable and to attach the cable to the AIC+ Advanced Interface Converter. We recommend the following equipment (or equivalent):

## Working with Cable for DH-485 Network

| Description Part Number Manufacturer                   |
|--------------------------------------------------------|
| Shielded twisted pair cable #3106A or #9842 Belden     |
| Stripping tool Not applicable Not applicable           |
| 1/8” slotted screwdriver Not applicable Not applicable |

## DH-485 Communication Cable

The suggested DH-485 communication cable is either Belden #3106A or #9842. The cable is jacketed and shielded with one or two twisted-wire pairs and a drain wire.

One pair provides a balanced signal line and one additional wire is used for a common reference line between all nodes on the network. The shield reduces the effect of electrostatic noise from the industrial environment on network communication.

The communication cable consists of a number of cable segments daisy-chained together. The total length of the cable segments cannot exceed 1219 m (4000 ft). However, two segments can be used to extend the DH-485 network to 2438 m (8000 ft). For additional information on connections using the AIC+, see Advanced Interface Converter (AIC+) User Manual, publication 1761-UM004 .

When cutting cable segments, make them long enough to route them from one AIC+ to the next, with sufficient slack to prevent strain on the connector. Allow enough extra cable to prevent chafing and kinking in the cable.

Use these instructions for wiring the Belden #3106A or #9842 cable. See Cable Selection Guide on page 70 if you are using standard Allen-Bradley cables.

## Connect the Communication Cable to the DH-485 Connector

<!-- image -->

A daisy-chained network is recommended. Do not make the incorrect connection shown below:

<!-- image -->

## Single Cable Connection

When connecting a single cable to the DH-485 connector, use Figure 52 .

Figure 52 - Single Cable Connection

<!-- image -->

## Multiple Cable Connection

When connecting multiple cables to the DH-485 connector, use Figure 53 .

Figure 53 - Multiple Cable Connection

<!-- image -->

## Connections using Belden #3106A Cable

| For this Wire/Pair Connect this Wire To this Terminal   |                                                |
|---------------------------------------------------------|------------------------------------------------|
|                                                         | Shield/drain Non-jacketed Terminal 2 – Shield  |
|                                                         | Blue Blue Terminal 3 – (Common)                |
| White/orange                                            | White with orange stripe Terminal 4 – (Data B) |
| White/orange                                            | Orange with white stripe Terminal 5 – (Data A) |

## Connections using Belden #9842 Cable

|              | For this Wire/Pair Connect this Wire To this Terminal   |
|--------------|---------------------------------------------------------|
|              | Shield/drain Non-jacketed Terminal 2 – Shield           |
| Blue/white   | White with blue stripe  Cut back – no connection(1)     |
| Blue/white   | Blue with white stripe Terminal 3 – (Common)            |
| White/orange | White with orange stripe Terminal 4 – (Data B)          |
| White/orange | Orange with white stripe Terminal 5 – (Data A)          |

## Ground and Terminate the DH-485 Network

Only one connector at the end of the link must have Terminals 1 and 2 jumpered together. This provides an earth ground connection for the shield of the communication cable.

Both ends of the network must have Terminals 5 and 6 jumpered together, as shown in Figure 54 . This connects the termination impedance (of 120 ohm) that is built into each AIC+ or the 1763-NC01 cable as required by the DH-485 specification.

## Connect the AIC+

Figure 54 - End-of-Line Termination

<!-- image -->

MicroLogix 1400 Channel 0 to DH-485 Communication Cable Pinout

When connecting MicroLogix 1400 Channel 0 to DH-485 communication cable pinout using an RS-232 cable, the maximum that the cable length may be extended is 15.24 m (50 ft). See Figure 55 .

Figure 55 - DH-485 Communications Cable Pinout

<!-- image -->

You can connect a MicroLogix 1400 controller to a DH-485 network via Channel 0 directly without using an optical isolator, such as AIC+, catalog number 1761-NET-AIC, because Channel 0 is isolated. However, you need to use an AIC+ to connect your PC or other MicroLogix family products, such as MicroLogix 1200, to a DH-485 network.

Figure 56 shows the external wiring connections and specifications of the AIC+.

<!-- image -->

Figure 56 - External Wiring Connections

| Item Description Item Description   |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 1 Port 1 – DB-9 RS-232, DTE 4       | DC Power source selector switch (cable = port 2 power source, External = external power source connected to item 5) |
|                                     | 2 Port 3 – RS-485 Phoenix plug 5 Terminals for external 24V DC power supply and chassis ground                      |
| 3 Port 2 – mini-DIN 8 RS-232 DTE    |                                                                                                                     |

For additional information on connecting the AIC+, see Advanced Interface Converter (AIC+) User Manual , publication 1761-UM004 .

## Cable Selection Guide

<!-- image -->

|                                   |                               | Cable Length Connections from to AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-----------------------------------|-------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) | 45 cm (17.7 in.) 2 m (6.5 ft) | SLC 5/03 or SLC 5/04 processors, ch 0 Port 2 Yes External                   |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) | 45 cm (17.7 in.) 2 m (6.5 ft) | MicroLogix 1200 ch 0 Port 1 Yes External                                    |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) | 45 cm (17.7 in.) 2 m (6.5 ft) | MicroLogix 1400 ch 2 Port 2 Yes External                                    |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) | 45 cm (17.7 in.) 2 m (6.5 ft) | PanelView 550 through NULL modem adapter Port 2 Yes External                |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) | 45 cm (17.7 in.) 2 m (6.5 ft) | DTAM™ Plus / DTAM™ Micro Port 2 Yes External                                |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) | 45 cm (17.7 in.) 2 m (6.5 ft) | PC COM port Port 2 Yes External                                             |                                      |

(1) External power supply required unless the AIC+ is powered by the device connected to port 2, then the selection switch should be set to cable .

(2) Series C or later cables are required.

<!-- image -->

|                  |                  | Cable Length Connections from to AIC+         | External Power Supply Required (1)   | Power Selection Switch Setting   |
|------------------|------------------|-----------------------------------------------|--------------------------------------|----------------------------------|
| 1761-CBL-AM00(2) | 45 cm (17.7 in.) | MicroLogix 1200 ch 0 Port 2 No Cable          |                                      |                                  |
| 1761-CBL-HM02(2) | 2 m (6.5 ft)     | To port 2 on another AIC+ Port 2 Yes External |                                      |                                  |

(1) External power supply required unless the AIC+ is powered by the device connected to port 2, then the selection switch should be set to cable .

(2) Series C or later cables are required.

<!-- image -->

|                           |                               | Cable Length Connections from to AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|---------------------------|-------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1747-CP3 1761-CBL-AC00(1) | 3 m (9.8 ft) 45 cm (17.7 in.) | SLC 5/03 or SLC 5/04 processor, channel 0 Port 1 Yes External               |                                      |
| 1747-CP3 1761-CBL-AC00(1) | 3 m (9.8 ft) 45 cm (17.7 in.) | PC COM port Port 1 Yes External                                             |                                      |
| 1747-CP3 1761-CBL-AC00(1) | 3 m (9.8 ft) 45 cm (17.7 in.) | PanelView 550 through NULL modem adapter Port 1 Yes External                |                                      |
| 1747-CP3 1761-CBL-AC00(1) | 3 m (9.8 ft) 45 cm (17.7 in.) | DTAM Plus / DTAM Micro Port 1 Yes External                                  |                                      |
| 1747-CP3 1761-CBL-AC00(1) | 3 m (9.8 ft) 45 cm (17.7 in.) | Port 1 on another AIC+ Port 1 Yes External                                  |                                      |
| 1747-CP3 1761-CBL-AC00(1) | 3 m (9.8 ft) 45 cm (17.7 in.) | MicroLogix 1400 ch 2 Port 2 Yes External                                    |                                      |

(1) External power supply required unless the AIC+ is powered by the device connected to port 2, then the selection switch should be set to cable .

<!-- image -->

| Cable Length Connections from to AIC+                                       | External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-----------------------------------------------------------------------------|--------------------------------------|--------------------------------------|
| straight 9-25 pin — Modem or other communication device Port 1 Yes External |                                      |                                      |

(1) External power supply required unless the AIC+ is powered by the device connected to port 2, then the selection switch should be set to cable .

<!-- image -->

|                             |                               | Cable Length Connections from to AIC+                      | External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-----------------------------|-------------------------------|------------------------------------------------------------|--------------------------------------|--------------------------------------|
| 1761-CBL-AS03 1761-CBL-AS09 | 3 m (9.8 ft) 9.5 m (31.17 ft) | SLC 500 Fixed, SLC 5/01, SLC 5/02, and SLC 5/03 processors |                                      | Port 3 Yes External                  |
| 1761-CBL-AS03 1761-CBL-AS09 | 3 m (9.8 ft) 9.5 m (31.17 ft) | PanelView 550 RJ45 port Port 3 Yes External                |                                      |                                      |

1761-CBL-PM02 Series C (or equivalent) Cable Wiring Diagram

<!-- image -->

## Recommended User-Supplied Components

These components can be purchased from your local electronics supplier.

## User Supplied Components

Figure 57 - Port Pinout

| Component Recommended Model                                                                                     |
|-----------------------------------------------------------------------------------------------------------------|
| External power supply and chassis ground Power supply rated for 20.4…28.8V DC                                   |
| NULL modem adapter Standard AT                                                                                  |
| Straight 9-25 pin RS-232 cable  See Figure 57 and Table 10 on page 72 for port information if making own cables |

1761-CBL-AP00 or 1761-CBL-PM02

<!-- image -->

Table 10 - Cable Assignment

| Pin Port 1: DB-9 RS-232  Port 2(1): (1761-CBL-PM02 cable) Port 3: RS-485 Connector   |
|--------------------------------------------------------------------------------------|
| 1 Received line signal detector (DCD) 24V DC Chassis ground                          |
| 2 Received data (RxD) Ground (GND) Cable shield                                      |
| 3 Transmitted data (TxD) Request to send (RTS) Signal ground                         |
| 4  DTE ready (DTR) (2) Received data (RxD)(3) DH-485 data B                          |
| 5 Signal common (GND) Received line signal detector (DCD) DH-485 data A              |
| 6  DCE ready (DSR)(2)  Clear to send (CTS)(3)  Termination                           |
| 7 Request to send (RTS) Transmitted data (TxD) Not Applicable                        |
| 8 Clear to send (CTS) Ground (GND) Not Applicable                                    |
| 9 Not Applicable Not Applicable Not Applicable                                       |

## Safety Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D or non-hazardous locations only.

<!-- image -->

WARNING: EXPLOSION HAZARD

AIC+ must be operated from an external power source.

This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.

See Safety Considerations on page 19 for additional information.

## Install and Attach the AIC+

1. Take care when installing the AIC+ in an enclosure so that the cable connecting the MicroLogix controller to the AIC+ does not interfere with the enclosure door.
2. Carefully plug the terminal block into the RS-485 port on the AIC+ you are putting on the network. Allow enough cable slack to prevent stress on the plug.
3. Provide strain relief for the Belden cable after it is wired to the terminal block. This guards against breakage of the Belden cable wires.

## Power the AIC+

MicroLogix 1000, 1200, and 1500 programmable controllers support 24V DC communication power on Channel 0. When connected to the 8-pin mini-DIN connector on the 1761-NET-AIC, 1761-NET-ENI, and the 1761-NET-ENIW, these controllers provide the power for the interface converter modules. The MicroLogix 1400 does not provide 24V DC communication power through communication ports. Instead these pins are used to provide RS-485 communications directly. Any AIC+, ENI, or ENIW not connected to a MicroLogix 1200 controller requires a 24V DC power supply.

If both the controller and external power are connected to the AIC+, the power selection switch determines what device powers the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if a higher voltage supply is used.

Set the DC Power Source selector switch to EXTERNAL before connecting the power supply to the AIC+. Figure 58 shows where to connect external power for the AIC+.

## Connect to Ethernet

Figure 58 - External Power for AIC+

<!-- image -->

<!-- image -->

ATTENTION: Always connect the CHS GND (chassis ground) terminal to the nearest earth ground. This connection must be made whether or not an external 24V DC supply is used.

Power Options

Below are two options for powering the AIC+:

- Use the 24V DC user power supply built into the MicroLogix 1000, 1200, or 1500 controller. The AIC+ is powered through a hard-wired connection using a communication cable (1761CBL-HM02, or equivalent) connected to port 2.
- Use an external DC power supply with the following specifications:
- operating voltage: 24V DC (-15%/+20%)
- output current: 150 mA minimum
- rated NEC Class 2

Make a hard-wired connection from the external supply to the screw terminals on the bottom of the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/ +20%). Permanent damage results if mis-wired with the wrong power source.

You can connect directly a MicroLogix 1400 to an Ethernet network via the Ethernet port (Channel 1). You do not need to use an Ethernet interface card, such as the Ethernet Interface (ENI) and (ENIW), catalog number 1761-NET-ENI and 1761-NET-ENIW, to connect your MicroLogix 1400 controller to an Ethernet network. For additional information on connecting to an Ethernet network, see Connect to Networks Via Ethernet Interface on page 267 .

<!-- image -->

## Ethernet Connections

The Ethernet connector, Channel 1, is an RJ45, 10/100Base-T connector. The pin-out for the connector is shown in Table 11 .

Table 11 - RJ54 Connector Pinout

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

End view of RJ 45 plug Looking into a RJ45 jack

8 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8

<!-- image -->

<!-- image -->

<!-- image -->

For information on how to select the proper cable, see Guidance for Selecting Cables for EtherNet/IP Networks White Paper, publication ENET-WP007 .

## LCD and Keypad

The LCD and keypad are shown in Figure 59 .

Figure 59 - Controller Part Identification

<!-- image -->

| Feature Description                                               |
|-------------------------------------------------------------------|
| 10 LCD                                                            |
| 5  LCD screen keypad (ESC, OK, Up, Down, Left, and Right buttons) |

Table 12 - LCD and Keypad

<!-- image -->

## Operating Principles

Figure 60 - MicroLogix 1400 LCD Menu Structure Tree

<!-- image -->

## Startup Screen

The Startup screen displays whenever the controller is powered up.

Figure 61 - LCD Default Startup Screen

You can customize this Startup screen in your application program by defining a ASCII data file that contains the bitmap format image to display on the Startup screen and specifying the CBL element of the LCD Function File to the address of this ASCII file.

Figure 62 shows an example of a customized Startup screen.

Figure 62 - Customized Startup Screen Example

<!-- image -->

Your imported Bitmap file format should meet the following criteria:

- Image resolution: 128 x 64 pixels (black/white image)
- Image size: 1088 bytes (consisting of image header = 62 bytes
+ raw image data size = 1024 bytes
+ padding data: 2 bytes)

To load a customized boot logo image to your controller, the CBL (Customized Boot Logo ASCII File) element in the LCD Function File should be configured properly. If the CBL element is set to 0 (default) or if the indexed ASCII file does not exist, the embedded default logo displays.

<!-- image -->

<!-- image -->

Once a valid bitmap file is imported successfully, you should see the data in ASCII data files.

Make sure that the second element (file size) in the first ASCII data file is 0x0440 (1088 bytes) in hexadecimal value.

After a power cycle, you should see the customized boot logo on your LCD display.

For more information on how to create and use a customized Startup screen, see the LCD function file described in the MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

After the default Startup screen or your customized Startup screen displays for 3 seconds, either the default screen (the I/O Status screen) displays by default, or a user-defined screen displays if your application uses a custom default screen.

## Main Menu and Default Screen

The Main menu consists of five menu items: I/O Status, Monitoring, Mode Switch, User Display, and Advanced Set.

## Main Menu Items

Figure 64 - LCD Default Screen – I/O Status Screen

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Menu Item Description For details, see:                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I/O Status  Displays the I/O Status screen, which shows the I/O status of the embedded digital I/O.                                                                                                                                                                                                                                                                                                                                                                     | I/O Status on page 80                                                                                                                                                                                                                                                                |
| Monitoring Allows you to view and change the data value of a bit and an integer file.                                                                                                                                                                                                                                                                                                                                                                                   | Monitor User Defined Target Files on page 82 Monitor Integer Files on page 85                                                                                                                                                                                                        |
| Mode Switch Allows you to change the mode switch selection.                                                                                                                                                                                                                                                                                                                                                                                                             | Mode Switch on page 93                                                                                                                                                                                                                                                               |
| User Display Displays the user defined LCD screen                                                                                                                                                                                                                                                                                                                                                                                                                       | User-defined LCD Screen on page 95                                                                                                                                                                                                                                                   |
| Advanced Set Allows you to configure or view the following: • Change the Key In mode for value entry for a trim pot. • Use the communications toggle functionality. • View and change the Ethernet network configuration. • Change the data value of trim pots. • View system information, such as operating system series and firmware version. • User communication EEPROM functionality. • Change LCD contrast and backlight option. • Modbus RTU Slave Node Address | •  Change Key In Mode on page 96 •  Communications Toggle Functionality on page 98 •  View Ethernet Status on page 98 •  Trim Pots on page 105 •  I/O Status on page 80 Save or Load Communication EEPROM on page 108 •  LCD setup on page 110 •  Protocol Configuration on page 112 |
| Security Allows you to set, activate, deactivate and change the LCD password.                                                                                                                                                                                                                                                                                                                                                                                           | LCD Password Setup on page 114                                                                                                                                                                                                                                                       |

.

<!-- image -->

<!-- image -->

Figure 64 is the default screen of the display, allowing you to monitor controller and I/O Status. For more information on the I/O Status screen, I/O Status on page 80 .

Figure 63 - LCD Main Menu

<!-- image -->

Note: The Security menu is available in firmware revision 21.000 or later.

## Operating Buttons

<!-- image -->

## Use Menus to Choose Values

<!-- image -->

| Press To   |                                                                                                                 |
|------------|-----------------------------------------------------------------------------------------------------------------|
| OK         | • Go to next menu level. • Store your entry. • Apply the changes.                                               |
| ESC        | • Go to previous menu level. • Cancel your entry since the last Ok . • Press repeatedly to go to the main menu. |
|            | • Change menu item. • Change value. • Change position.                                                          |

## Select Between Menu Items

<!-- image -->

<!-- image -->

## Cursor Display

<!-- image -->

D

## I/O Status

<!-- image -->

## Set Values

<!-- image -->

There are two different cursor types:

Selection cursor (the symbol) displays left of the selected item.

- Move cursor with the up/down arrows

Full block navigation shows as a flashing block:

- Change position with left/right arrows
- Change values with up/down arrows

<!-- image -->

Left/right arrow moves the cursor between the digits of the value.

Up/down arrow changes the value.

Up arrow = increment

Down arrow = decrement

The MicroLogix 1400 controller provides I/O status indicators on the LCD screen. You can view the status of inputs and outputs on the I/O Status screen on the LCD, as in Figure 65 on page 81. The I/ O status indicators on this screen are updated every 100 ms to reflect the current I/O status in real time, regardless of controller scan time.

Figure 65 - I/O Status Screen

<!-- image -->

A solid rectangle displays when the input or output is energized. An empty rectangle displays when the input or output is not energized.

## IMPORTANT

## IMPORTANT

If no user defined LCD screen is used, the I/O Status screen displays,

- 5 seconds after the controller has powered-up.
- When you enter the I/O Status screen from other screen using the LCD menu. If you are at another screen and want to view I/O status, you have to enter the I/O Status screen manually using the menu. Otherwise, the current screen displays continuously.

If a user defined LCD screen is used, the I/O Status screen displays,

- When you hold down the ESC key for more than 3 seconds.
- When time out is enabled, that is, the time out period is set to a positive value, and the time out period is passed. You can enable and disable time out and set the time out period using the TO element in the LCD Function File. For more information, see the LCD Function File described in MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .
- If time out is disabled, that is, the time out period is set to zero (0), and a custom LCD screen displays, it displays continuously until you give an input to change to another screen. For more information, see User-defined LCD Screen on page 95 .

## View I/O Status

Follow these steps to view the status of inputs and outputs on the LCD.

1. On the Main Menu screen, select I/O Status by using the Up and Down keys on the LCD keypad, as shown.
2. Then, press OK on the LCD keypad. The I/O Status screen displays, as shown.

<!-- image -->

<!-- image -->

## Monitor User Defined Target Files

3. If you have finished viewing I/O status, press ESC to return to the Main Menu screen, as shown in step 1 .

The LCD allows you to view and change the data values of 256 bits, words or double integers in a user defined file. You can access to this functionality via the Monitoring screen of the LCD screen.

To monitor the bit file on the LCD screen, you have to specify its file number in the Target User Defined File Number (TUF) element of the LCD Function File and download your application program to the controller. The TUF element can only be changed by a program download.

## Target User Defined File Number (TUF)

|                                                                        | Feature Address Data Format Type User Program Access   |
|------------------------------------------------------------------------|--------------------------------------------------------|
| Target User Defined File Number LCD:0.TUF Word (int) Control Read Only |                                                        |

The value stored in the TUF element identifies the bit file with which the LCD will interface. Valid bit files are B3, and B10 through B255. When the LCD reads a valid bit file number, it can access up to 256 bits (0...255) on the LCD screen. The protection bit (LCD edit disable) in the data file properties of target bit file are used to define the read-only or read/write privileges for its file.

The file type that the LCD interfaces with is bit, integer, double integer or float file specified in the TUF element.

## IMPORTANT

Use your programming software to ensure that the bit file you specify in the TUF element, as well as the appropriate number of elements, exist in the MicroLogix 1400 user program.

The data protection for a file depends on the LCD edit disable setting. When LCD Edit Disable is set (1: Checked) in file properties, the corresponding data file is considered read-only by and the "Protected!" message displays. When LCD Edit Disable is clear (0: Unchecked), the "UnProtected!" message displays and the corresponding data file is editable from the LCD keypad.

## IMPORTANT

Although you cannot change protected data from the LCD keypad, the control program or other communication devices do have access to this data. The Protection bit (LCD Edit Disable) only provides write protection from the LCD keypad. This does not provide any overwrite protection from ladder logic, HMI, or programming software. It is the user's responsibility to ensure that data is not inadvertently overwritten.

<!-- image -->

The LCD always starts at bit 0 of a data file. It cannot start at any other address within the file.

## Monitor a Bit File

For explanations in this section, we assume the following in the application program:

- A bit file B3, which is 256 elements long (256 words = 4096 bits), is defined with the preset data, as shown.
- LCD Edit Disable is set to unchecked (disable)
- The TUF element of the LCD Function File is set to 3 to specify the bit file B3 as the target bit file to monitor on the LCD, as shown.
- The controller mode is set to REMOTE RUN.

<!-- image -->

<!-- image -->

<!-- image -->

Follow these steps to view and change the data values of the bit file B3.

1. On the Main Menu screen, select Monitoring by using the Up and Down keys on the LCD keypad.

REMOTE

1/0

Status

Monitor ing

Mode

Switch

2. Press OK on the LCD keypad. The File Number prompt displays.

REMOTE File Hum? 003 Data Type: B Press OK to edit

3. If number 3 is selected, as shown in step 2, press OK. If not selected, press Up or Down to select it and then press OK.
4. The current data value (ON) of the B3:0/0 bit displays as shown. Note that "0/0" flashes, which means the cursor is at the target bit position.
5. To change the data value of the B3:0/0 bit to OFF (0): First, press OK to select the displayed address and move the cursor to the data value position. Then, "ON" flashes, which means the cursor is at the data value position.
6. Press the Down key. Then, the data value is represented as "OFF". Note that "OFF" continues to flash, which means the cursor is still at the data value position.
7. Press OK to apply the changes. Then, the new value OFF (0) is applied. Note that the target bit, "0/0" in this example, flashes. The cursor moves automatically to the target bit position.

DODDO

REMOTE

010:68

NO=

UnProtected!

REMOTE

010:68 =OFF UnProtected!

<!-- image -->

You can identify that this change of data value is reflected to your RSLogix 500/RSLogix Micro programming software.

<!-- image -->

- When the cursor is at the data value position, press Down to change the data value of a bit from ON (1) to OFF (0). Press Up to change from OFF (0) to ON (1). After changing the data value of a target bit, press OK to apply the changes or press

ESC to discard the changes.

8. Now, we will view an example of the data value of a protected property. If LCD Edit Disable is set to checked (enable), the "Protected!" message displays and this data file cannot be edited from the LCD.
9. Try to move the cursor to the data value position by pressing OK. Because the B3:0/0 bit is a protected bit, you will find that the cursor does not move to the data value position.
10. Hold down the Up key until the target bit becomes "255/15", as shown. The maximum range of bits you can monitor with the LCD is 256 words of specified target bit file.
11. If you have finished monitoring the bit file, B3, press ESC to return to the Bit/Integer File Select screen, as shown in step 2 .

<!-- image -->

<!-- image -->

## Monitor Integer Files

The LCD allows you to view and change the data value of an integer file. You can access to this functionality from the Monitoring screen of the LCD.

To monitor an integer file on the LCD, you have to specify its file number in the Target User Defined File Number (TUF) element of the LCD Function File and download your application program to the controller. The TUF element can only be changed by a program download.

The value stored in the TUF element identifies the integer file with which the LCD interfaces. Valid integer files are N7, and N10…N255. When the LCD reads a valid integer file number, it can access

up to 256 bits (0…255) on the LCD screen. The protection bit (LCD edit disable) in the data file properties of the target integer file are used to define the read-only or read/write privileges for its file.

Valid file type include Bit, Integer, Double integer or Float, as specified in the TUF element.

## IMPORTANT

Use your programming software to ensure that the integer file you specify in the TUF element, as well as the appropriate number of elements, exists in the MicroLogix 1400 user program.

The example below shows how the LCD uses the configuration information with integer file number 7 (LCD:0.TUF=7).

The data protection for its file depends on the setting for LCD Edit Disable. If LCD Edit Disable is set to 1 in file properties, the corresponding data file is considered read-only by the LCD and the "Protected!" message displays.

## IMPORTANT

Although you cannot change protected data from the LCD keypad, the control program or other communication devices have access to protected data. Protection bits do not provide any overwrite protection to data within the target integer file. It is entirely the user's responsibility to ensure that data is not inadvertently overwritten.

<!-- image -->

The LCD always starts at word 0 of a data file. It cannot start at any other address within the file.

For explanations in this section, we assume the following in the application program:

- An integer file N7, which is 256 elements long (256 words), is defined with the preset data, as shown.
- The TUF element of the LCD Function File is set to 7 to specify the integer file N7 as the target integer file to monitor on the LCD, as shown.

<!-- image -->

<!-- image -->

- The controller mode is set to REMOTE RUN.

Follow these steps to view and change the data values of the integer file N7.

1. On the Main Menu screen, select Monitoring by using the Up and Down keys on the LCD keypad.

REMOTE

1/0 Status Monitor ing Mode Switch

2. Press OK on the LCD keypad. The File Number prompt displays.

REMOTE File Num? 007 Data Type : N Press OK to edit

3. If Integer is selected, as shown in step 2, press OK. If not selected, press Down to select it and then press OK.
4. The current data value (ON) of the N7:0 word displays. Note that the target word "0", which is right next to "N7:", flashes, which means the cursor is at the target word position.
5. We will change the data value of the N7:0 word to the negative decimal value -1300. First, press OK to move the cursor to the data value position. The last digit of "+00000" flashes, which means the cursor is at the data value position.
6. Press the Left key twice. The cursor positions at the third digit. Press Up three times to change the third digit to 3.
7. Press the Left key once. Then, press Up once. The second digit changes to "1". Note that "1" continues to flash, which means the cursor is still at the data value position.

REMOTE

## N7 :0 二+ 68668 UnProtected!

REMOTE

N7 :0

二+

88300

UnProtected!

0口口口口

REMOTE

N7 : 8 =+01388 UnProtected!

8. Press the Left key once. Then, press Down once. The sign digit changes to "-", as shown. Note that "-" continues to flash, which means the cursor is still at the data value position.
9. Press OK to apply the changes. Then, the new value -1300 is applied. Note that the target word "0", which is right next to "N7:", flashes. The cursor is moved automatically to the target word position.

<!-- image -->

You can identify that this change of data value is reflected to your RSLogix 500/RSLogix Micro programming software, as shown.

<!-- image -->

<!-- image -->

After changing the data value of a target word, press OK to apply the changes or press ESC to discard the changes.

10. Now, we will view an example of the data value of a protected property. If LCD Edit Disable is set to checked (enable), the "Protected!" message displays and this data file cannot be edited by the LCD.

<!-- image -->

<!-- image -->

11. Try to move the cursor to the data value position by pressing OK. Because the N7:0 word is protected, the cursor does not move to the data value position.

## IMPORTANT

The maximum range of words you can monitor with the Integer File Monitoring functionality on the LCD is the first 256 words (0…255) of the target integer file.

12. If you have finished monitoring the integer file N7, press ESC to return to the Main Menu screen, as shown in step 2 .

## Monitor Double Integer files

The LCD allows you to view and change the data value of a double integer file. You can access to this functionality using the Monitoring screen of the LCD.

To monitor a double integer file on the LCD, you have to specify its file number in the Target User Defined File Number (TUF) element of the LCD Function File and download your application program to the controller. The TUF element can only be changed by a program download.

The value stored in the TUF element identifies the double integer file with which the LCD interfaces. Valid double integer files are L9, and L10…L255. When the LCD reads a valid double integer file number, it can access up to 256 words (0…255) on the LCD screen. The protection bit (LCD edit disable) in the data file properties of target integer file are used to define the read-only or read/ write privileges for its file.

Valid file type include Bit, Integer, Double integer or Float, as specified in the TUF element.

The data protection for its file depends on the setting for LCD Edit Disable. If LCD Edit Disable is set to 1 in file properties, the corresponding data file is considered read-only by the LCD and the Protected! message displays.

## IMPORTANT

Although you cannot change protected data from the LCD keypad, the control program or other communication devices do have access to this data. The Protection bit (LCD Edit Disable) only provides write protection from the LCD keypad. This does not provide any overwrite protection from ladder logic, HMI, or programming software. It is your responsibility to ensure that data is not inadvertently overwritten.

For explanations in this section, we assume the following in the application program:

- A bit file L9, which is 256 elements long (256 words), is defined with the preset data, as shown.
- LCD Edit Disable is set to unchecked (disable).

<!-- image -->

<!-- image -->

- The TUF element of the LCD Function File is set to 9 to specify the integer file L9 as the target file to monitor on the LCD, as shown.

The controller mode is set to REMOTE RUN.

<!-- image -->

Follow these steps to view and change the data values of the double integer file L9.

1. On the Main Menu screen, select Monitoring by using the Up and Down keys on the LCD keypad.
2. Press OK on the LCD keypad. The File Number prompt displays.
3. If Integer is selected, as shown in step 2, press OK. If not selected, press Down to select it and then press OK.
4. The current data value (ON) of the L9:0 word displays. Note that the target word 0, which is at the right L9:, flashes, which means the cursor is at the target word position.

<!-- image -->

<!-- image -->

100000

REMOTE

0:67

二+

0000000000

UnProtected!

5. We will change the data value of the L9:0 word to the negative decimal value -1300. First, press OK to move the cursor to the data value position. Then, the last digit of +0000000000 flashes, which means the cursor is at the data value position.
6. Press the Left key twice. The cursor positions at the third digit. Press Up three times to change the third digit to 3.
7. Press the Left key once. Then, press Up once. The second digit changes to 1. Note that 1 continues to flash, which means the cursor is still at the data value position.
8. Press the Left key once. Then, press Down once. The sign digit changes to -, as shown. Note that - continues to flash, which means the cursor is still at the data value position.
9. Press OK to apply the changes. The new value -1300 is applied. Note that the target word 0, which is to the right of L9:, flashes. The cursor moves automatically to the target word position.
10. You can identify that this change of data value is reflected to your RSLogix 500/RSLogix Micro programming software.

100000

REMOTE

0:67

二+

6868866388

UnProtected!

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

After changing the data value of a target double word, press OK to apply the changes or press ESC to discard the changes.

11. Now, we will view an example of the data value of a protected property. If LCD Edit Disable is set to checked (enable), the Protected! message displays and this data file cannot be edited by the LCD.
12. Try to move the cursor to the data value position by pressing OK. Because this double integer file is protected, you will find that the cursor does not move to the data value position.
13. If you have finished monitoring the double integer file, L9, press ESC to return to the File Number question screen, as shown in step 2 .

<!-- image -->

<!-- image -->

## Monitor Floating Point Files

In this section, this assumption regarding the application program is made:

- The TUF element of the LCD Function File is set to 8. This specifies the floating point file F8 as the target file to monitor via the LCD.

Most of the steps outlined in this section are similar to those found in Monitor Double Integer files on page 89. However, you cannot edit floating point files from the LCD.

<!-- image -->

The Protected! message displays on the LCD for floating point files.

<!-- image -->

MicroLogix 1400 Series A controllers display an Unprotected! message but you cannot edit the corresponding data file.

## Monitor System Status Files

In this section, this assumption regarding the application program is made:

## Mode Switch

- The TUF element of the LCD Function File is set to 2. This specifies the system status file S2 as the target file to monitor via the LCD.

The format string on the third line displays as decimal, hexadecimal, or binary for each word element, depending on what each elements means.

<!-- image -->

For more information, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

The MicroLogix 1400 controller provides the controller mode switch on the LCD. The possible positions of the mode switch are PROGRAM, REMOTE, and RUN. You can change mode switch position using the Mode Switch screen on the LCD, as shown. In this example, the mode switch position is set to REMOTE.

<!-- image -->

All the built-in LCD screens except the Boot Message screen display the current mode switch position, at their top right portion, as shown. In this example, the mode switch position is set to RUN.

<!-- image -->

## Controller Modes

Table 13 shows the possible controller modes when the mode switch positions at PROGRAM, REMOTE, or RUN. For example, if the Mode Switch is at RUN and you want to test a control program with running it for a single scan, you have to first change mode switch position to REMOTE before you run the control program in the remote test single scan mode with your RSLogix 500 or RSLogix Micro programming software.

Table 13 - Possible Controller Modes by Mode Switch Position

| When the Mode Switch Positions at Possible Controller Modes are   |                                                                     |
|-------------------------------------------------------------------|---------------------------------------------------------------------|
| PROGRAM                                                           | Download in progress                                                |
| PROGRAM                                                           | Program mode                                                        |
| PROGRAM                                                           | Suspend mode — operation halted by execution of the SUS instruction |

Table 13 - Possible Controller Modes by Mode Switch Position (Continued)

| When the Mode Switch Positions at Possible Controller Modes are                   |
|-----------------------------------------------------------------------------------|
| Remote download in progress                                                       |
| Remote program mode                                                               |
| REMOTE Remote suspend mode — operation halted by execution of the SUS instruction |
| Remote run mode                                                                   |
| Remote test continuous mode                                                       |
| Remote test single scan mode                                                      |
| RUN Run mode                                                                      |

## Change Mode Switch Position

Mode Switch position can be changed at two different times using LCD keypad. One is when the controller is powered up, and the other is while the controller is powered on.

Mode Switch position can be set to either PROG or RUN when the controller is powered up. This allows the controller operation which is different from the previous mode, that is, any program under RUN before can be stopped or any new program can be run when the controller is powered up.

To forcibly set Mode Switch to RUN when the controller is powered up:

1. Press OK for 5 seconds when the controller is powered up. The following LCD screen appears if successfully done.

<!-- image -->

To forcibly set Mode Switch to PROG when the controller is powered up:

1. Press ESC for 5 seconds when the controller is powered up. The following LCD screen appears if successfully done.

<!-- image -->

Note that I/O output status may be changed for some programs.

While the controller is powered on, follow these steps to change the position of the Mode Switch.

1. On the Main Menu screen, select Mode Switch by using the Up and Down keys on the LCD keypad.

<!-- image -->

## User-defined LCD Screen

2. Press OK on the LCD keypad. The Mode Switch screen displays, as shown.

<!-- image -->

The arrow indicates current Mode Switch position.

3. When the Up or Down key is pressed, the mode indicated by the arrow blink if the mode is different from the current mode of controller. Press OK to set the controller to the mode indicated by the arrow.
4. If you have finished changing mode switch position, press ESC to return to the Main Menu screen, as shown in step 1 .

The MicroLogix 1400 controller allows you to use user-defined LCD screens instead of the default built-in screens.

To use a user-defined screen, you need to create a group of appropriate instructions using the LCD instruction in your application program. For more information on how to create a user defined LCD screen, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

By using the User Display menu item, you can change from the default built-in screens to a userdefined screen and back on the LCD.

## User-defined LCD Screen

Follow these steps to display the user-defined screen implemented in your application program.

1. On the Main Menu screen, select User Display by using the Up and Down keys on the LCD keypad, as shown. If the menu items shown in the figure below are not displayed on the Main Menu screen, scroll down the screen by pressing the Down key.

<!-- image -->

Note: The Security menu is available in firmware revision 21.000 or later.

2. Press OK on the LCD keypad.

If no user-defined screen is used in your application program, the screen displays, as shown.

<!-- image -->

<!-- image -->

RUN

Note that the U-DISP indicator on the top of the LCD displays is a solid rectangle. It means the LCD is in User-defined LCD mode.

If a user-defined screen is used in your application program, the LCD screen displays, as shown, according to the specific instructions used in your program.

## Configure Advanced Settings

## Change Key In Mode

<!-- image -->

3. Press ESC longer than 3 seconds to return to the Main Menu screen.

<!-- image -->

With the Advanced Set menu, which is a sub-menu under the main menu of the LCD, you can use the following features:

- change Key In mode
- use communications toggle functionality
- configure Ethernet Network Configuration
- use trim pots
- view system information
- view fault code
- save/load Communication EEPROM
- change LCD contrast and back light
- view/change the Modbus RTU Slave Node address

You can access the Advanced Set Menu screen shown, by selecting Advanced Set on the Main Menu screen.

<!-- image -->

## Key In Modes

There are two Key In modes, Continuous and Discrete.

<!-- image -->

The Key In mode has an effect only when you change the data value of a trim pot on a trim pot screen, either Trim Pot 0 or Trim Pot 1 screen. For more information on how to change the data value of a trim pot, see Change Data Value of a Trim Pot on page 105 .

The current Key In mode determines how the value changes are applied when you press Up and Down to change the data value for a trim pot. When set to Continuous, the changes apply immediately when you press the Up and Down keys. When set to Discrete, the changes apply only when you press OK after you have changed the value using the Up and Down keys.

By using the Key In Mode screen shown, you can change the Key In mode to use.

RUN

## KeyI n Mode: Cont sronut: Discrete

## Change Key In Mode

To change the current Key In mode, perform the following:

1. On the Main Menu screen, select Advance Set by using the Up and Down keys on the LCD keypad. If the menu items do not display on the Main Menu screen as shown, scroll down the screen by pressing the Down key.

RUN

User Disp Ae Actyanced Set Security

Note: The Security menu is available in firmware revision 21.000 or later.

2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.
3. Select KeyIn Mode using the Up and Down keys, and then press OK.
4. The Key In Mode screen displays. The current mode, Continuous in this example, is selected marked up with the symbol.

<!-- image -->

RUN

KeyIn IMode: Continuous Discrete

5. Press Up or Down to select the different mode, Discrete in this example. Press OK.

RUN

KeyIn Mode: Cont inuous Discrete

6. The Key In Mode Change Notification screen displays, as shown.

## Communications Toggle Functionality

## Ethernet Network Configuration

<!-- image -->

7. Press ESC to return to the Advanced Set Menu screen, as shown in step 2 .

The MicroLogix 1400 controller provides the Communications Toggle functionality, which allows you to switch between the user-defined communication configuration and the default communications mode configuration on Channel 0. See Use the Communications Toggle Functionality on page 58 for more information on this feature.

## View Ethernet Status

The Ethernet configuration screen of the LCD displays the MAC and IP addresses assigned to the controller.

Follow these steps to view the Ethernet configuration for your controller.

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad, as shown. If the menu items does not display on the Main Menu screen as shown, scroll down the screen by pressing the Down key.

<!-- image -->

Note: The Security menu is available in firmware revision 21.000 or later.

2. Press OK on the LCD keypad. The Advanced Set Menu screen displays, as shown.
3. If ENET Cfg is selected, press OK. Otherwise, select ENET Cfg using the Up and Down keys, and then press OK.
4. The Ethernet Configuration screen displays. Press OK on the LCD Status menu.
5. When an IP address is not yet assigned to your controller, only the MAC address that is assigned to your controller, represented as XXXXXXXXXXXX below, displays. A MAC address is a 12-digit hexadecimal number. Your controller ships with a unique MAC address assigned in the factory. You can identify the MAC address of your controller by opening the expansion module cover on your controller.

<!-- image -->

<!-- image -->

<!-- image -->

6. When an IP address is assigned to your controller, both the MAC and IP addresses of your controller display. In this example, the MAC address is represented as XXXXXXXXXXXX. The IP address is represented as xxx.xxx.xxx.xxx, where each xxx is a decimal number between 0…255.
7. Press ESC to return to the Advanced Set Menu screen, as shown in step 2 .

<!-- image -->

## Configure the IP Address

The IP Address screen of the LCD displays Ethernet network configuration assigned to the controller.

Follow these steps to edit the Ethernet network configuration for your controller.

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad, as shown. If the menu items do not display on the Main Menu screen as shown, scroll down the screen by pressing the Down key.

<!-- image -->

Note: The Security menu is available in firmware revision 21.000 or later.

2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays, as shown. If ENET Cfg is selected, press OK. Otherwise, select ENET Cfg using the Up and Down keys, and then press OK.

<!-- image -->

3. If IP Address is selected, press OK, If not, select IP Address using the Up and Down keys, and then press OK.

REMOTE

ENET Cfg:

Status

IP

Address

4. The password screen displays. Press Up, Down, Left and Right keys to enter the master password up to a maximum of 10 digits. In this example, the current master password is allocated as 1234.

REMOTE ENET Setup Master Password:

Note: For firmware revisions 21.000 or later the LCD password screen displays.

REMOTE ENET/ Setup: Password: 0000000000

5. Enter the master password, then press OK on the LCD keypad.

REMOTE ENET Setup: Master Password: 1234

Note: For firmware revisions 21.000 or later, press OK on the LCD password screen.

REMOTE ENET/ Setup: Password: 1 234000000

6. If the master password is incorrect, an error message displays.

REMOTE LLUL ENET Setup: Password I Wrong!

7. If the password is correct, the Ethernet network type screen displays as shown. Press Up or Down key to select the appropriate Ethernet mode.

8. If you press OK at the static mode, the IP address flashes.

9. Configure the IP address and press OK. The Subnet Mask screen displays.

10. Configure the Subnet Mask and press OK. The Gateway address displays.

11. Configure the Gateway address and press OK. The Primary DNS displays.

12. Configure the Primary DNS and press OK. The Secondary DNS displays.

To exit the Network configuration Menu, press ESC on the LCD keypad at any time.

REMOTE ETH Mode: bootp Press [U/D] key

REMOTE ENET Mode: static IP address 192. 168. 100. 201

REMOTE ENET Mode: static Subnet Mask 255. 255. 255. 000

REMOTE ENET Mode: static Gateway address 192. 168.100. 001

REMOTE ENETI Mode: static Pri DNS 100. 100. 100. 001

REMOTE ENET Mode: static Sec SNO 100. 100. 100. 002

<!-- image -->

## Configure the Ethernet Port

The Port Settings screen of the LCD displays the Ethernet port settings assigned to the controller.

Follow these steps to edit the Ethernet port settings for your controller.

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad. If the menu items do not display on the Main Menu screen as shown, scroll down the screen by pressing the Down key.

REMOTE User Displ ay Actyanced Set Security

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays.
3. If ENET Cfg is selected, press OK. If not, select ENET Cfg using the Up and Down keys, and then press OK.
4. If Port Setting is selected, press OK, If not, select Port Setting using the Up and Down keys, and then press OK.

<!-- image -->

<!-- image -->

000000 REMOTE ENET Cfg: Port Setting Protocol setup

5. The password screen displays. Press Up, Down, Left and Right to enter Master password with maximum 10 digits. In this example, the current Master password is allocated as 1234.

000000 REMOTE ENET Setup: Master Password:

Note: For firmware revisions 21.000 or later the LCD password screen displays.

00000 ? REMOTE ENET/ Setup: Password: 0000000000

After entering the Master password, press the OK key on the LCD keypad.

<!-- image -->

<!-- image -->

<!-- image -->

6. If the Master password is correct, the last configuration displays. In this example, the auto negotiation function is enabled and the 10/100 Mbps link configuration shows.

7. Press Up and Down to select auto disable menu, then press OK. The fourth line on the LCD flashes. Press Up and Down to configure the Ethernet port to 100 Mbps Full-duplex forced.

## Configure Ethernet Protocol Setup

The Ethernet Protocol Setup screen of the LCD displays Ethernet Protocol settings assigned to the controller.

Follow these steps to edit the Ethernet Protocol settings for your controller.

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad, as shown below. If the menu items shown in the figure below are not displayed on the Main Menu screen, you need to scroll down the screen by pressing the Down key.

Note: The Security menu is available in firmware revision 21.000 or later.

2. Press OK on the LCD keypad. The Advanced Settings Menu screen displays, as shown below.

3. If ENET Cfg is selected, press OK. If not, select ENET Cfg using the Up and Down keys, and then press OK.

Any change to this feature’s configuration does not take effect until after the next power cycle.

0OL000

REMOTE

Auto: Enabl e

10/100M F1H

0O00D0

REMOTE

Auto: Enabl e

10/100M F/H

REMOTE User Displ: Ae Acyanced Set Security

REMOTE Key In Mode LICOMM Cfg ENET Cfg

REMOTE KeyI n Mode CICOMM Cfg ENET Cfg

4. If Protocol setup is selected, press OK. If not, select Protocol setup using the Up and Down keys, and then press OK.

5. The password screen displays. Press Up, Down, Left and Right keys to enter a master password up to a maximum of 10 digits. In this example, the current master password is allocated as 1234.

Note: For firmware revisions 21.000 or later the LCD password screen displays.

After entering the Master password, press the OK key on the LCD keypad.

6. The following menu displays.

7. If you want to change the SNMP setting, press Up or Down and press OK to apply the change.

REMOTE ENET Cfg: Port Setting Protocol setup

REMOTE ENET Setup: Master Password:

00000 REMOTE ENET/ Setup: Password: 0080000000

REMOTE

SNMP: Enab l ed

HTTP: Enabl ed

REMOTE

SNMP: DiSabled

HTTP: Enabl ed

Power ***810

## Trim Pots

8. To change the HTTP setting, press Up or Down and press OK to apply the change.

REMOTE

SNMP: Enabled

HTTP: Enabl ed

REMOTE

SNMP: Enabl ed

HTTP: Disabled

Power

Cycle***

<!-- image -->

To exit the Protocol Setup Menu, press ESC on the LCD keypad at any time.

## Trim Pot Operation

The MicroLogix 1400 controller provides two trimming potentiometers (trim pots, POT0 and POT1) which allow modification of integer data within the controller. The data value of each trim pot can be used throughout the control program for timers, counters, analog presets, depending upon the requirements of the application.

You can change the data value of each trim pot using the trim pot screens provided by the LCD. To access to the Trim Pot Set screen, which is the top screen for the trim pot functionality, select TrimPot Set on the LCD default menu screen, as shown below, and press OK on the LCD keypad.

<!-- image -->

Trim pot data is updated continuously whenever the controller is powered-up.

## Change Data Value of a Trim Pot

Follow these steps to change the data value of a trim pot, either POT0 or POT1.

1. On the Main Menu screen, select TrimPot Set by using the Up and Down keys on the LCD keypad.

RUN

TrimPot Set System Info Fault Code

<!-- image -->

2. Then, press OK on the LCD keypad. The trim pot select screen displays, as shown below.
3. The last trim pot whose data value you changed is selected by default. If you are accessing to this screen for the first time, POT0 is selected by default.
4. Select a trim pot, either POT0 or POT1, whose data value you want to change using the Up and Down keys on the LCD keypad. In this example, we will select POT0.
5. Then, press OK on the LCD keypad. The trim pot0 screen displays, as shown below.

<!-- image -->

<!-- image -->

TMIN and TMAX indicate the range of data value for the trim pots, both POT0 and POT1. The factory default for TMIN, TMAX, and POT0 values are 0, 250, and 0 in decimal, respectively. TMIN and TMAX on this screen are read only, but you can change them using the LCD Function File in your application program. The TMIN and TMAX elements can only be changed by a program download.

For more information on how to change trim pot configuration including TMIN and TMAX, see the LCD Function File described in the MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

## IMPORTANT

The same TMIN and TMAX values are used for both trim pots, POT0 and POT1. This behavior is intended by design for simplicity in Trim Pot configuration.

When you enter this screen, the last digit of the POT0 value flashes. It indicates the current digit. Press Up and Down on the LCD keypad to change the value of the current digit. Press Left and Right to select a different digit as the current digit.

If the key in mode is set to Continuous, the changes are applied immediately after you press Up and Down. While, if it is set to Discrete, you have to press OK to apply the changes after you change the data value. For more information on how to set the key in mode, Change Key In Mode on page 96 .

The KeyIn mode has an effect only when you change the data value of a trim pot on a Trim Pot screen, either the Trim Pot 0 or Trim Pot 1 screen.

<!-- image -->

6. If you have finished changing the data value of the selected trim pot, POT0 in this example, press ESC to return to the trim pot select screen, as shown in step 2 .

## Trim Pot Configuration in LCD Function File

The configuration for trim pots in the LCD Function File, including trim pot low and high values for data value range, is described in the MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

## Error Conditions

Error conditions regarding trim pot functionality are described in the MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

## View System Information

## View Fault Code

The System Information screen of the LCD allows you to identify the system information for your controller.

Follow these steps to view the system information for your controller.

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad, as shown below. If the menu items shown in the figure below do not display on the Main Menu screen, you need to scroll down the screen by pressing the Down key.

<!-- image -->

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Then, press OK on the LCD keypad. The Advanced Set Menu screen displays, as shown below.
3. If System Info is selected, press OK.

<!-- image -->

If not, select System Info using the Up and Down keys, and press OK.

4. The System Information screen displays.

You can identify the catalog number, operating system firmware revision number, and boot firmware revision number of your controller.

RUN

Cat:1766-LEC

0S FRN:1. 0

BT FRN:1. 0

<!-- image -->

5. Press ESC to return to the Advanced Set Menu screen, as shown in step 3 .

The Fault Code screen of the LCD displays the fault code when a fault occurs.

When a fault occurs, the Fault Code screen does not display automatically. Only the FAULT LED on the controller flashes in red light. Therefore, you need to navigate into the Fault Code screen to identify the fault code on the LCD.

Follow these steps to view the fault code when a fault occurs.

## Save or Load Communication EEPROM

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad, as shown below. If the menu items shown in the figure below do not display on the Main Menu screen, you need to scroll down the screen by pressing the Down key.

<!-- image -->

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Then, press OK on the LCD keypad. The Advanced Set Menu screen displays, as shown below.
3. If Fault Code is selected, press OK.

<!-- image -->

If not, select Fault Code using the Up and Down keys, and then press OK.

4. The Fault Code screen displays.

If no fault occurred, "0000h" displays, as shown below.

<!-- image -->

If a fault is occurred, its fault code displays, as shown below.

RUN

<!-- image -->

Major Error Code=0029h

For more information on a specific fault code, see the Online Help of your RSLogix 500/ RSLogix Micro programming software.

5. Press ESC to return to the Advanced Set Menu screen, as shown in step 2 .

At the communication EEPROM screen, you can load/save user programs and data to or from the Memory module.

## Save Communication EEPROM

Follow these steps to save user program and data from controller's memory to memory module.

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad.

If the menu items shown do not display on the Main Menu screen, scroll down by pressing the Down key.

REMOTE

User

Acyanced

Displ ay

Security

Set

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Press OK on the LCD keypad.
3. Select Comms EEPROM using the Down key, and then press OK.

REMOTE Comms EEPROM LCD Setup

4. Select Store to MM to save user program and data, and then press OK.

REMOTE Comms EEPROM: Store to HM Load from HM

5. If your controller is in a non-executing mode, skip to the next step. Otherwise switch your controller to a non-executing mode.

REMOTE Mode: remote RUN RUN-&gt;PROG mode Conf irm?

6. The usual method for using a memory module is to reuse the device. Select Reuse Device or Write Only by pressing Up or Down.

REMOTE

1. Reuse Aa0 ice

2. Write

Only

Select

## IMPORTANT

Num?1

Once set to Write Only mode, write protection cannot be removed. If a change is required, use a different memory module. For more information on this, see Memory Module Operation on page 120 .

Once Write Only is set, write protection cannot be removed. A change cannot be made to the control program stored in a write protected memory module. If a change is required, use a different memory module.

For more information on transferring data to and from memory modules, see Memory Module Operation on page 120 .

## LCD setup

7. This screen appears if the save is complete. Press OK to go back to executing mode.

<!-- image -->

## Load communication EEPROM

Follow these steps to load user programs and data from the memory module to the controller's memory.

1. Select Load from MM to load user programs and data.
2. If your controller is in a non-executing mode, skip to the next step. Otherwise switch your controller to a non-executing mode.
3. This screen appears if the load from the memory module is complete. Press OK to go back to executing mode.

<!-- image -->

<!-- image -->

<!-- image -->

For more information on transferring data to and from memory modules, see Memory Module Operation on page 120 .

<!-- image -->

In the LCD Setup screen, you can configure the contrast value and backlight for the LCD.

## Configure Contrast Value

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad.
2. If the menu items shown are not displayed on the Main Menu screen, scroll down by pressing the Down key.

.CD Setup:

Contrast

Back

Light

5. Adjust the contrast value using the Left and Right keys on the LCD keypad.

<!-- image -->

## Configure the Back Light

1. On the Main Menu screen, select Advanced Set by using the Up and Down keys on the LCD keypad.

If the menu items shown are not displayed on the Main Menu screen, scroll down by pressing the Down key.

<!-- image -->

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Press OK on the LCD keypad.

REMOTE

User

Display

Acyanced

Security

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Press OK on the LCD keypad.
3. Select LCD Setup, using the Up and Down keys on the LCD keypad. When the LCD Setup menu screen displays, press OK.
4. Select Contrast to adjust the contrast of LCD.

<!-- image -->

REMOTE

Set

## Protocol Configuration

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

3. Select LCD Setup, using the Up and Down keys on the LCD keypad. When the LCD Setup menu screen displays, press OK.

4. Select Back Light to adjust back lighting options for the LCD.

5. The default value for the back light is 30 seconds. You can adjust back light time using the Up and Down keys on the LCD keypad.

The following section provides a step-by-step guide on how to change the Modbus Node address.

## Modbus RTU Slave Node Address

You can set the Modbus RTU Slave Node address for Channel 0 or 2.

Change the Modbus RTU Slave Node address

1. On the Main Menu screen, select Advanced Set by using the Up or Down arrow key on the LCD keypad. If the menu items shown in the figure are not displayed on the Main Menu screen below, you need to scroll down the screen by pressing the Down key.

Note: The Security menu is available in firmware revision FRN 21 and higher.

2. Then, press OK on the LCD keypad. The Advanced Settings Menu screen displays.

The node address change will only be applicable after a power cycle.

REMOTE Comms EEPROM LCD Setup

REMOTE .CD Setup: Contrast Back Light

REMOTE

LCD Setup:

BackL ight=1

30sec

LO

00000

RUN

User Displ Ae Acyanced Set Security

3. Select the Protocol Cfg using the Up and Down arrow keys, and then press OK.

4. Select the Modbus RTU Sl and then press OK.

5. The Modbus RTU Slave screen displays. Channel 0 is selected below.

6. Press Up or Down to select a different channel, Channel 2 in this example, then press OK.

7. If the channel selected is not configured with the Modbus RTU Slave driver, then Modbus Not Configured displays, as shown below.

RUN

KeyI n Mode Cfg DCOMM ENET Cfg

RUN Conms EEPROM LCD Setup Protocol Cfg

RUN

Modbus RTU SI

RUN

Modbus RTu Slaye

Charnel θ

Channel 2

RUN Modbus RTU Slaye Channel θ Channel 2

RUN

Modbus Hot Configured!

## LCD Password Setup

8. If channel 0 is configured with the Modbus RTU Slave driver with node address 100, the following screen will appear as shown.
9. If channel 2 is configured with the Modbus RTU Slave driver with node address 100, the following screen will appear as shown.
10. The user can configure the node address for either channel by using the Up and Down arrow keys. Once the address is changed, press OK to confirm the change. The following screen appears.

<!-- image -->

<!-- image -->

<!-- image -->

The following section provides a step-by-step guide on how to set, change, activate and deactivate the LCD Password in firmware revision FRN 21 and higher.

## Set the LCD Password

1. On the Main Menu, select Security by using the Up and Down keys on the LCD keypad. If the menu items shown are not displayed on the Main Menu screen, scroll down by pressing the Down key.
2. Select Security to set the LCD Password. If LCD Password is not set, Activate PWD menu screen displays.

<!-- image -->

RUN

Actvate PHD

<!-- image -->

<!-- image -->

<!-- image -->

3. Select Activate PWD menu to set the LCD Password. LCD Password screen displays. Digit at current cursor position blinks always.

4. Press Up or Down to change the digit and Left or Right to move the cursor position. Enter the LCD Password up to a maximum of 10 digits. In this example, the current LCD Password is allocated as 1234.

5. Press OK on the LCD keypad to set the entered password. A confirmation screen displays.

6. Press OK to set and activate the LCD Password. When the Password is activated a key symbol appears at the top of the display.

## Activate the LCD Password

1. On the Main Menu, select Security by using the Up and Down keys on the LCD keypad. If the menu items shown are not displayed on the Main Menu screen, scroll down by pressing the Down key.

0000

RUN

Enter P assword 0000000000

HESC]

[OK]

RUN

Enter Password: 1234000000

[ESC]

[OK]

RUN Activate PHD pro tection? [ESC] [OK]

OE RUN HActivate PHO Deactivate PHD PHO

000000 OL RUN User Displ: Ae Acvanced Set Security

2. Select Security. If the LCD Password is set, the LCD Password configuration menu screen displays.

3. Select Activate PWD to activate the LCD Password which is already stored in controller but deactivated. A confirmation screen displays.

4. Press OK. The existing LCD Password is activated. When the Password is activated a key symbol appears at the top of the display.

## Deactivate the LCD Password

1. On the Main Menu, select Security by using the Up and Down keys on the LCD keypad.

2. Select Security to deactivate the LCD Password. If an LCD Password is set, the LCD Password configuration menu screen displays.

RUN Activate PHD Deactivate PHD Change PHD

100000 RUN Activate PHD pro tection? H[ESC] [OK]

OF RUN Activate PHO Deactivate PHD afueyn PHD

00000 Y RUN User Displ AP Acyanced Set Security

000000 RUN Activate PHO eactivate PHD Change PHD

<!-- image -->

<!-- image -->

3. Select Deactivate PWD to deactivate the LCD Password. An authentication screen displays.

4. Enter the LCD Password and press OK to deactivate the LCD Password. A notification screen displays and the key symbol no longer appears at the top of the screen.

5. Press OK.

The LCD Password remains stored in the controller but is deactivated.

## Change LCD Password

1. On the Main Menu, select Security by using the Up and Down keys on the LCD keypad.

2. Select Security to change the LCD Password. If an LCD Password is set, the LCD Password configuration menu screen displays.

3. Select Change PWD to change the LCD Password. The LCD password change screen displays.

4. Press Up or Down to change the digit and press Left or Right to move the cursor position. Enter the old (current) and new LCD Passwords.

In this example, the old and new LCD Passwords are 1234 and 5670000009.

OF RUN Enter P: assword: 0000000000 H[ESC] [OK]

L0000 RUN Password protect ion is deactivat i pa [OK]

00000 RUN User Displ AP Acyanced Set Security

0000 RUN Activate PHD Deactivate PHD Change PHO

RUN 0ld: 0000000000 New: 0000000000 HESC] [OK]

<!-- image -->

5. Note: If you want to clear the LCD Password, instead of deactivating it, enter the new password as 0000000000. A confirmation screen displays.
6. Press OK to clear the LCD Password. A confirmation screen displays.
7. Press OK on the LCD keypad to change the password. A confirmation screen displays.

<!-- image -->

<!-- image -->

<!-- image -->

## Real-Time Clock Operation

<!-- image -->

## Real-Time Clock and Memory Modules

The MicroLogix 1400 controller has a built-in real-time clock (RTC). You can order a memory module as an accessory.

<!-- image -->

For more information on real-time clock function file and memory module information file, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

One type of memory module is available for use with the MicroLogix 1400 controller.

| Catalog Number Function Memory Size   |
|---------------------------------------|
| 1766-MM1 Memory Module 384 KB         |

## Operation at Power-up and Entering a Run or Test Mode

At power-up and when the controller enters a run or test mode, the values (date, time and status) of the RTC are written to the RTC Function File in the controller.

The following table indicates the accuracy of the RTC for various temperatures.

## RTC Accuracy

| Ambient Temperature  Accuracy(1)      |
|---------------------------------------|
| 0 °C (32 °F) -13…-121 seconds/month   |
| 25 °C (77 °F) +54…-5 seconds/month    |
| 40 °C (104 °F) +29…-78 seconds/month  |
| 55 °C (131 °F) -43…-150 seconds/month |

## Write Data to the Real-Time Clock

When valid data is sent to the real-time clock from the programming device or another controller, the new values take effect immediately.

The real-time clock does not allow you to load or store invalid date or time data.

## RTC Battery Operation

The real-time clock uses the same replaceable battery that the controller uses. The RTC Function File features a battery low indicator bit (RTC:0/BL), which shows the status of the replacement battery. When the battery is low, the indicator bit is set (1). This means that the battery wire connector could be disconnected or if the battery is connected, the battery may be ready to fail in the next two weeks. In the latter case, the replacement battery needs to be replaced with a new one. When the battery low indicator bit is clear (0), the battery level is acceptable.

The Battery Low (BAT.LO) indicator on the LCD display of the controller also shows the status of the replaceable battery. When the battery is low, the indicator displays as a solid rectangle ( ). When the battery level is acceptable, the indicator displays as an empty rectangle ( ), as shown below.

## Memory Module Operation

<!-- image -->

If the RTC battery is low and the controller is powered, the RTC operates normally. If the controller power is removed and the RTC battery is low, RTC data is lost.

<!-- image -->

ATTENTION: Operating with a low battery indication for more than 2 weeks may result in invalid RTC data unless power is on continuously.

The memory module supports the following features:

- User Program, User Data, Datalog, and Recipe Back-up
- User Program Compare
- Data File Download Protection
- Memory Module Write Protection
- Removal/Insertion Under Power

<!-- image -->

ATTENTION: Electrostatic discharge can damage the Memory Module. Do not touch the connector pins or other sensitive areas.

## User Program, User Data, Datalog, and Recipe Back-up

The memory module provides a simple and flexible program, data, DataLog, and Recipe transport mechanism, allowing the user to transfer the program, data, DataLog, and Recipe to the controller without the use of a personal computer and programming software.

The memory module can store one user program at a time.

During program transfers to or from the memory module, the controller's RUN LED flashes.

## Program Compare

The memory module can also provide application security, allowing you to specify that if the program stored in the memory module does not match the program in the controller, the controller will not enter an executing (run or test) mode. To enable this feature, set the S:2/9 bit in the system status file. See "Status System File" in the MicroLogix 1400 Programmable Controllers Reference Manual, Publication 1766-RM001 for more information.

## Data File Download Protection

The memory module supports data file download protection. This allows user data to be saved (not overwritten) during a download.

<!-- image -->

Data file download protection is only functional if the processor does not have a fault, size of all protected data files in the memory module exactly match the size of protected data files within the controller, and all protected data files are of the same type. See "Protecting Data Files During Download" in the MicroLogix 1400 Programmable Controllers Reference Manual, Publication 1766-RM001 .

## Memory Module Write Protection

The memory module supports write-once, read-many behavior. Write protection is enabled using your programming software.

## IMPORTANT

Once set, write protection cannot be removed. A change cannot be made to the control program stored in a write protected memory module. If a change is required, use a different memory module.

## Removal/Insertion Under Power

The memory module can be installed or removed without risk of damage to either the memory module or the controller, except during a data transaction. If the memory module is removed during a data transaction, data corruption can occur.

If a memory module is installed while the MicroLogix 1400 controller is executing, the memory module is not recognized until either a power cycle occurs, or until the controller is placed in a nonexecuting mode (program mode, suspend mode or fault condition).

## Memory Module Information File

The controller has a Memory Module Information (MMI) File which provides status from the attached memory module. At power-up or on detection of a memory module being inserted, the catalog number, series, revision, and type are identified and written to the MMI file. If a memory module is not attached, zeros are written to the MMI file. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001, for more information.

## Program /Data Download

To download the program and data from a memory module to the controller's memory, on the "Comms" menu in your RSLogix 500/RSLogix Micro programming software, point "EEPROM" and then select "Load from EEPROM".

<!-- image -->

With MicroLogix 1400 controllers, you can also use the LCD and the LCD buttons on the module to transfer applications to or from the controller.

For more information on program/data download, see your RSLogix 500/RSLogix Micro programming software documentation.

## Program /Data Upload

To upload the program and data from the controller's memory to a memory module, on the "Comms" menu in your RSLogix 500/RSLogix Micro programming software, point "EEPROM" and then select "Store to EEPROM".

<!-- image -->

With MicroLogix 1400 controllers, you can also use the LCD and the LCD buttons on the module to transfer applications to or from the controller.

For more information on program/data upload, see your RSLogix 500/RSLogix Micro programming software documentation.

## Overview of Online Editing

## Online Editing

Online editing of ladder programs is available when using MicroLogix 1400 controllers. Use this function to make changes to a pre-existing ladder program. Online editing functions consist of inserting, replacing, and deleting rungs in an existing ladder program while online with the processor.

Only one programming device can perform an online edit of a user program at a time. When an online editing session begins, an access from other programming devices are rejected by MicroLogix 1400 controllers.

<!-- image -->

WARNING: Before initiating an online editing session, we recommend that you fully understand the possible results of the edit to the system under control. Failure to properly edit a running program could result in unexpected controller operation. Physical injury or equipment damage may result.

While three instructions, MSG, PTO, and PWM, are supported by program mode online edit, they are not supported by RUNTIME (RUN mode) online edit. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 for additional details.

The following table summarizes the differences between offline and online editing.

|                                                               | Offline Online                                                       |
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

- Assemble Edits – Deletes any rungs marked with Delete or Replace edit zone markers during an online editing session. Inserted or modified rungs remain. All edit zone markers are removed when this function is complete.
- Cancel Edits – Deletes any inserted or modified rungs added during an online editing session. Rungs marked with Delete and Replace edit zone markers remain. All edit zone markers are removed when this function is complete.
- Test Edits – Allows you to verify that the changes you entered are not going to cause improper machine operation before you make the changes a permanent part of your ladder program.
- Untest Edits – Allows you to disable testing
- Edit Zone markers – Appear on the power rail of the ladder program display. They indicate the type of edit taking place on the rung.

<!-- image -->

## Effects of Online Editing On Your System

## Directions and Cautions for MicroLogix 1400 Online Editing User

- Accept Rung – Incorporates the edits of a single rung into the ladder program
- Online edit session – Begins when a user tries to edit rungs while online. Any other programming device that was monitoring the user program is removed from the program monitor display.
- Modify rung – When an existing rung is modified two edit zones are created. The original rung is indicated by replace zone markers on the power rail. A copy of the original rung is made so you can insert, delete, or modify instructions. This rung is indicated by insert zone markers on the power rail. Thus, an IR pair is created when you modify a rung.
- Runtime online editing – The user program is executing when an edit takes place. Any rungs that are inserted, modified, or deleted remain in the ladder program and are indicated by edit zone markers on the power rail. Edit zone markers remain after an action is completed.
- Program online editing – The user program is not executing when an edit session begins. Any action that inserts, deletes, or modifies a rung takes place immediately.

The following section covers the effects of online editing on your system. Keep these items in mind while using the online editing function.

## System Impacts

The scan time and interrupt latency can be extended when accepting a rung, assembling, or canceling edits.

Memory limitations – Online edit can be performed until there is insufficient program memory available in the processor. Note that, before assemble edits, all the edited rungs are in the processor memory consuming memory, although they are not executed.

## Data Table File Size

Online editing cannot change the size of existing data tables nor can new ones be created. However, some ladder instructions, when programmed cause data table values to change. These instructions are those that require timer, counter, and control addresses to be specified.

## Online Edit Error

If either electrical interference, communication loss, or a power cycle occur during online edit session, program integrity may be impacted. In this case, the controller will generate the 1F fault code, clear the user program, and load the default program.

## A Download is Required Before Starting Online Editing

At least one download is required before you can start online editing.

If you are using a MicroLogix 1400 controller from out-of-box state or after clearing the processor memory or a firmware upgrade, at least one download is required before starting online edits. If not, an error occurs and programming software will go offline due to a default image mismatch between RSLogix 500 programming software and the MicroLogix 1400 controller. You can also see the fault code 1Fh which is a user defined fault code.

In order to prevent this error, you need to download the program to the MicroLogix 1400 controller, although the program is empty.

This problem happens only in out-of-box state or after clear processor memory.

## Types of Online Editing

<!-- image -->

<!-- image -->

ATTENTION: PTO and PWM instructions may not be deleted during runtime online edit. This is because if the PTO or PWM instructions were deleted during runtime online edit, outputs could stop in an unpredictable state, causing unexpected equipment operation.

If you attempt to insert or modify a rung with MSG, PTO, and PWM instruction, the following error message is generated by programming software error: Online editing of PTO, PWM, and MSG are not allowed on ML1400 RUN mode. The rung with MSG, PTO, and PWM instruction is not accepted.

<!-- image -->

In online edit during PROGRAM mode (program online edit), there are no restrictions. For example, a user can insert MSG instruction if related MG file or MG/RI file is already defined in data file.

<!-- image -->

ATTENTION: When editing a rung that contains an MCR instruction, both the MCR start and MCR end rungs must be edited (whether it be test/assemble/cancel) at the same time. We recommend that you fully understand the possible results of the edit to the system under control. Failure to properly edit a running program could result in unexpected controller operation. Physical injury or equipment damage may result.

<!-- image -->

ATTENTION: If you use EII or STI interrupts and your application requires a quick interrupt latency, the online edit feature is not recommended. Online editing feature may increase the interrupt latency response time. To ensure minimum interrupt latency, place the mode switch in LCD screen in the RUN mode. This prevents the use of the online editing feature.

The type of online editing is dependent on the MicroLogix 1400 controller's mode switch position in LCD display and the processor's mode. There are two types of online editing:

- Program Online Editing — When the controller is in either PROG mode or REM Program mode
- Runtime Online Editing — When the controller is in either REM Test or REM Run mode

The following table summarizes the MicroLogix 1400 controller mode switch positions in LCD and modes that enable online editing.

| Mode Switch Position  MicroLogix 1400 Controller Mode  Editing Mode   |
|-----------------------------------------------------------------------|
| RUN RUN Not Available                                                 |
| PROGram Program Program Online Editing                                |
| REMote REMote Program Program Online Editing                          |
| REMote REMote Test Runtime Online Editing                             |
| REMote REMote Run Runtime Online Editing                              |

IMPORTANT

Online editing is not available when the mode switch in LCD screen is in the RUN position.

<!-- image -->

ATTENTION: Use the online editing function while in the RUN mode to make minor changes to the ladder program. We recommend developing your program offline since ladder rung logic changes take effect immediately after testing your edits. Improper machine operation may occur, causing personnel injury or equipment damage.

## Edit Functions in Runtime Online Editing

During a runtime online editing session, the processor is executing ladder logic. The edit zone markers tell the processor that changes exist, but the changes are not executed until you test the edits.

Deleted and replaced (modified) rungs are not removed from the program and inserted rungs are not executed until you assemble or test the edits.

## Edit Functions in Program Online Editing

During a program online editing session, the processor is not executing ladder logic. This mode is like the offline editing mode. If a runtime online editing session is performed prior to entering the offline editing mode, edit marked rungs (I, R, and D) appear in the program.

If you perform a program online edit, once you accept or delete the rung, the edits take effect immediately and the power rail is displayed as a solid line. If you edit a rung with edit zone markers, the markers are removed when the rung is accepted.

## Automatic Controller Recovery

## Auto Reset Functionality

MicroLogix 1400 controllers with firmware revision 21.007 or later have the added ability to automatically recover from 2H, 4H, 8H, and 9H faults when Auto Reset Status Bit S:36/1 is enabled.

## Enable the Status Bit

1. In RSLogix 500/RSLogix Micro, open the S2 – Status file under Data Files in the MicroLogix 1400 project tree.
2. In the Status data file, set Status Bit S:36/1 to 1. The default for the status bit is 0 (disabled).
3. Download the project to the controller.

<!-- image -->

<!-- image -->

## Enable Auto Reset

Valid selections are Enabled (1) and Disabled (0). Default value is Disabled (0).

When the Auto Reset functionality is Enabled (1) and the MicroLogix 1400 controller encounters a 2H, 4H, 8H, or 9H fault, the controller recovers by performing an automatic restart and then loads the latest user program (a) and user data(b) from NVRAM.

(a) Latest user program means the program that you downloaded or a user program that you successfully edited online, whichever is the latest.

(b) Latest user data means data that you downloaded as part of a program download or user data that you successfully edited online, whichever is the latest.

<!-- image -->

Once the MicroLogix 1400 controller restores the user project and user data, the controller recovers to one of two possible states, depending on the mode prior to encountering the fault:

- If the controller was operating in Remote Run mode, then the controller recovers to Program mode.
- If the controller was operating in Hard Run mode, the controller transitions to a recoverable fault state.

The Auto Reset functionality does not work in the following conditions:

1. If the user project or user data back-up is corrupted – The controller reports a 1H error.
2. If you installed a memory module and selected Load Always or Load on Error.

## IMPORTANT

- The Auto Reset functionality is disabled by default.
- After the controller auto resets, you need to put the controller to Run mode.
- Controller run-time data is lost. The initial data that you set is restored.
- With Auto Reset enabled, the controller scan time could increase by approximately 30 ms, if you change configuration while online or when you edit the user program online.

## General Specifications

| Description 1766-L32AWA/A 1766-L32BWA/A 1766-L32BXB/A                                      |                                                                                            |                                                                                            |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| 90 x 180 x 87 mm 3.5 x 7.08 x 3.43 in.                                                     | 90 x 180 x 87 mm 3.5 x 7.08 x 3.43 in.                                                     | 90 x 180 x 87 mm 3.5 x 7.08 x 3.43 in.                                                     |
| Shipping weight 900 g (31.74 oz.)                                                          | Shipping weight 900 g (31.74 oz.)                                                          | Shipping weight 900 g (31.74 oz.)                                                          |
| Number of I/O 24 inputs (20 digital and 4 analog) and 14 outputs (12 digital and 2 analog) | Number of I/O 24 inputs (20 digital and 4 analog) and 14 outputs (12 digital and 2 analog) | Number of I/O 24 inputs (20 digital and 4 analog) and 14 outputs (12 digital and 2 analog) |
| Power supply voltage 100…240V AC @ 47…63 Hz 24V DC Class 2 SELV                            | Power supply voltage 100…240V AC @ 47…63 Hz 24V DC Class 2 SELV                            |                                                                                            |
| Heat dissipation See System Loading and Heat Dissipation .                                 | Heat dissipation See System Loading and Heat Dissipation .                                 | Heat dissipation See System Loading and Heat Dissipation .                                 |
| Power supply inrush current  120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                 | Power supply inrush current  120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                 | 24V DC: 15 A for 20 ms                                                                     |
| Power consumption  100VA 130VA (Series C)                                                  | 120VA 150VA (Series C)                                                                     | 50 W 7.5 W (with no 1762 expansion I/O)                                                    |
| 24V DC sensor power none                                                                   | 24V DC at 250 mA 400 µF max                                                                | none                                                                                       |
| Input circuit type Digital: 120V AC Analog: 0…10V DC                                       | Digital: 24V DC sink/source (standard and high-speed) Analog: 0…10V DC                     | Digital: 24V DC sink/source (standard and high-speed) Analog: 0…10V DC                     |
| Output circuit type Relay Relay/FET                                                        | Output circuit type Relay Relay/FET                                                        |                                                                                            |
| Relay life – Electrical See Relay Life Chart                                               | Relay life – Electrical See Relay Life Chart                                               | Relay life – Electrical See Relay Life Chart                                               |
| Relay life – Mechanical 20,000,000 cycles                                                  | Relay life – Mechanical 20,000,000 cycles                                                  | Relay life – Mechanical 20,000,000 cycles                                                  |
| Enclosure type rating None (open-style)                                                    | Enclosure type rating None (open-style)                                                    | Enclosure type rating None (open-style)                                                    |
| Terminal screw torque 0.791 N•m (7.0 lb•in) rated                                          | Terminal screw torque 0.791 N•m (7.0 lb•in) rated                                          | Terminal screw torque 0.791 N•m (7.0 lb•in) rated                                          |

## Specifications for Inputs

|                                                            |                                                   | 1766-L32BWA/A, 1766-L32BXB/A                                                       | 1766-L32BWA/A, 1766-L32BXB/A                                                     |
|------------------------------------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|                                                            | Description 1766-L32AWA/A                         | Inputs 0...11 (12 high-speed DC inputs)                                            | Inputs 12 and higher (8 standard DC inputs)                                      |
| On-state voltage range 79…132V AC                          |                                                   | 4.5…24V DC (4.5…26.4V DC (+10%) at 60 °C/140 °F (4.5…30V DC (+25%) at 30 °C/86 °F) | 10…24V DC (10…26.4V DC(+10%) at 60 °C/140 °F) (10…30V DC (+25%) at 30 °C/86 °F   |
| Off-state voltage range 0…20V AC 0…1.5V DC 0…5V DC         |                                                   |                                                                                    |                                                                                  |
|                                                            |                                                   |                                                                                    | Operating frequency 47...63 Hz 0 Hz...100 kHz 0 Hz...1 kHz (scan time dependent) |
| On-state current Min Nom Max                               | 9.0 mA @ 79V AC 12 mA @ 120V AC 16.0 mA @ 132V AC | 7.0 mA @ 4.5V DC 9.5 mA @ 24V DC 10.0 mA @ 30V DC                                  | 3.0 mA @ 10V DC 5.0 mA @ 24V DC 5.5 mA @ 30V DC                                  |
| Off-State Leakage Current 2.5 mA max 0.1 mA max 1.5 mA max |                                                   |                                                                                    |                                                                                  |
| Nominal Impedance                                          | 12 kΩ at 50 Hz 10 kΩ at 60 Hz                     | 2.0 kΩ                                                                             | 5.5 kΩ                                                                           |
| Inrush Current (max) at 120V AC 30 A                       |                                                   |                                                                                    |                                                                                  |

## Analog Inputs

| Description 1766-L32AWA/A, 1766-L32BWA/A, 1766-L32BXB/A   |
|-----------------------------------------------------------|
| Voltage input range 0…10.0V DC – 1 LSB                    |
| Type of data 12-bit unsigned integer                      |
| Input coding (0…10.0V DC – 1 LSB) 0…4095                  |
| Voltage input impedance >199 kΩ                           |

## Specifications

<!-- image -->

## Analog Inputs (Continued)

| Description 1766-L32AWA/A, 1766-L32BWA/A, 1766-L32BXB/A          |
|------------------------------------------------------------------|
| Input resolution 12 bit                                          |
| Non-linearity ±0.5% of full scale                                |
| Overall accuracy ° y -20…+65 °C (-4…+149 °F)  ±1.0% of full scale                                                                  |
| Update time 100/20/16.67/4 ms (selectable)                       |
| Voltage input overvoltage protection 10.5V DC                    |
| Field wiring to logic isolation Non-isolated with internal logic |

## Analog Outputs

| Description 1766-L32AWA/A, 1766-L32BWA/A, 1766-L32BXB/A   |
|-----------------------------------------------------------|
| Number of inputs 2 single-ended                           |
| Voltage output range 0…10V DC – 1 LSB                     |
| Type of data 12-bit unsigned integer                      |
| Step response 2.5 ms @ 95%                                |
| Load range Voltage output >1 KΩ                           |
| Output coding (0…10V DC) 0…4095                           |
| Output resolution 12 bit                                  |
| Analog output setting time, max 3 ms                      |
| Overall Accuracy ° y -20…+60 °C (-4…+140 °F) ±1.0% of full scale                                                           |
| Electrical isolation Non-isolated with internal logic     |
| Cable length 30 m (98 ft) shielded cable                  |

## Relay and FET Outputs

|                                       | Description 1766-L32AWA/A, 1766-L32BWA/A 1766-L32BXB/A   |                                                       |                   |
|---------------------------------------|----------------------------------------------------------|-------------------------------------------------------|-------------------|
| Maximum controlled load 1440VA 1080VA | Maximum controlled load 1440VA 1080VA                    |                                                       |                   |
| Maximum Continuous Current:           | Maximum Continuous Current:                              | Maximum Continuous Current:                           |                   |
| Current per channel and group common  | Current per channel and group common                     | 2.5 A per channel 8 A max channel 8...11 common       | 2.5 A per channel |
| Current per controller                | at 150V max                                              | 28 A or a total of per-point loads, whichever is less |                   |
| Current per controller                | at 240V max                                              | 20 A or a total of per-point loads, whichever is less |                   |

## Relay Outputs

| Description 1766-L32AWA/A, 1766-L32BWA/A, 1766-L32BXB/A   |
|-----------------------------------------------------------|
| Turn On Time/Turn Off Time, max  10 ms(1)                 |
| Load current, min 10 mA                                   |

## Relay Contact Ratings (1)

| Maximum Volts Amperes     | Amperes Continuous Volt-Amperes Continuous Make Break Make Break                           |                                         |
|---------------------------|---------------------------|-----------------------------------------|
|                           |                           | 240V AC 7.5 A 0.75 A 2.5 A 1800VA 180VA |
|                           |                           | 120V AC 15.0 A 1.5 A 2.5 A 1800VA 180VA |
| 250V DC 0.11 A 1.0 A 28VA | 250V DC 0.11 A 1.0 A 28VA |                                         |
| 125V DC 0.22 A 1.0 A 28VA | 125V DC 0.22 A 1.0 A 28VA |                                         |

<!-- image -->

ATTENTION: Do not exceed the Current per group common specification.

## Relay Life Chart

Figure 66 - MicroLogix 1400 DC Input Power Requirements for 1766-L32BXB/A Unit 1766-L32BXB/A Typical Power Requirements

<!-- image -->

Figure 67 - 1766-L32BXB, 1766-L32BXBA FET Output Maximum Output current (temperature dependent):

<!-- image -->

FET Current per Point FET Total Current

<!-- image -->

<!-- image -->

## AC Input Filter Settings

|                             | ON Delay (ms) OFF Delay (ms)   | ON Delay (ms) OFF Delay (ms)    |
|-----------------------------|--------------------------------|---------------------------------|
| Nominal Filter Setting (ms) |                                | Minimum Maximum Minimum Maximum |
|                             | 8 2.3 2.5 11 12                |                                 |

## High-Speed DC Input Filter Settings (Inputs 0…11)

| Nominal Filter Setting (ms)   | ON Delay (ms) OFF Delay (ms)             | Maximum Counter Frequency (Hz) 50% Duty Cycle   |
|-------------------------------|------------------------------------------|-------------------------------------------------|
| Nominal Filter Setting (ms)   | Minimum Maximum Minimum Maximum          | Maximum Counter Frequency (Hz) 50% Duty Cycle   |
|                               |                                          | 0.005 0.001 0.005 0.001 0.005 100.0 kHz         |
|                               |                                          | 0.008 0.003 0.008 0.003 0.008 60.0 kHz          |
|                               |                                          | 0.0125 0.0075 0.0125 0.007 0.0115 40.0 kHz      |
|                               |                                          | 0.025 0.019 0.025 0.018 0.023 20.0 kHz          |
|                               |                                          | 0.075 0.062 0.072 0.066 0.074 6.7 kHz           |
|                               |                                          | 0.100 0.089 0.100 0.088 0.098 5.0 kHz           |
|                               |                                          | 0.250 0.229 0.250 0.228 0.248 2.0 kHz           |
|                               |                                          | 0.500 0.459 0.500 0.455 0.492 1.0 kHz           |
|                               |                                          | 1.00 0.918 0.995 0.910 0.979 0.5 kHz            |
|                               |                                          | 2.000 1.836 1.986 1.820 1.954 250 Hz            |
|                               |                                          | 4.000 3.672 3.968 3.640 3.904 125 Hz            |
| 8.000(1)                      |                                          | 7.312 7.868 7.280 7.804 63 Hz                   |
|                               | 16.000 14.592 15.668 14.560 15.604 31 Hz |                                                 |

(1) Default setting

## Standard DC Input Filter Settings (Inputs 4 and higher)

| Nominal Filter Setting (ms)   | ON Delay (ms) OFF Delay (ms)             | Maximum Frequency (Hz) 50% Duty Cycle   |
|-------------------------------|------------------------------------------|-----------------------------------------|
| Nominal Filter Setting (ms)   | Minimum Maximum Minimum Maximum          | Maximum Frequency (Hz) 50% Duty Cycle   |
|                               |                                          | 0.500 0.107 0.439 0.024 0.499 1.0 kHz   |
|                               |                                          | 1.000 0.597 0.964 0.470 0.978 0.5 kHz   |
|                               |                                          | 2.000 1.437 1.864 1.415 1.990 250 Hz    |
|                               |                                          | 4.000 3.397 3.964 3.095 3.790 125 Hz    |
| 8.000(1)                      |                                          | 6.757 7.564 6.735 7.690 63 Hz           |
|                               | 16.000 14.597 15.964 13.455 14.890 31 Hz |                                         |

(1) Default setting

Table 14 - 1766-L32BXB, 1766-L32BXBA FET Output

|                                                                 | Description General Operation                      | High-Speed Operation (1) (Output 2, 3 and 4 Only)           |
|-----------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------|
|                                                                 | Power supply voltage 24V DC (-15%, 10%) Class 2    | Power supply voltage 24V DC (-15%, 10%) Class 2             |
| On-state voltage drop: at max load current at max surge current | 1V DC 2.5V DC                                      | Not Applicable Not Applicable                               |
| Current rating per point max load min load max leakage          | See Figure 67 50 mA 1.0 mA                         | 100 mA 50 mA 1.0 mA                                         |
| Surge current per point: peak current max surge duration g max rate of repetition at 30 °C (86 °F) °° p max rate of repetition at 60 °C (140 °F)                                                                 | 4.0 A 10 ms once every second once every 2 seconds | Not Applicable Not Applicable Not Applicable Not Applicable |
| Turn-On Time, max 11 µs 28 ns                                   |                                                    |                                                             |
| Turn-Off Time, max 89 µs 3.5 µs                                 |                                                    |                                                             |

## Working Voltage for 1766-L32AWA/A

|                                           | Description Recommendation                                                                                                                                                                               |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power Supply Input to Backplane Isolation | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Input Group to Backplane Isolation        | Verified by one of the following dielectric tests: 1517V AC for 1 second or 2145V DC for 1 second 132V AC Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Input Group to Input Group Isolation      | Verified by one of the following dielectric tests: 1517V AC for 1 second or 2145V DC for 1 second 132V AC Working Voltage (basic insulation)                                                             |
| Output Group to Backplane Isolation       | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                            |
| Output Group to Output Group Isolation    | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1second 265V AC Working Voltage (basic insulation), 150V AC Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage for 1766-L32BWA/A

|                                                                             | Description Recommendation                                                                                                                                                                            |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power Supply Input to Backplane Isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Input Group to Backplane Isolation and Input Group to Input Group Isolation | Verified by one of the following dielectric tests: 1100V AC for 1 second or 1697V DC for 1 second 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Output Group to Backplane Isolation                                         | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation).                                        |
| Output Group to Output Group Isolation                                      | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage for 1766-L32BXB/A

|                                                                             | Description Recommendation                                                                           |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Input Group to Backplane Isolation and Input Group to Input Group Isolation | Verified by one of the following dielectric tests: 1100V AC for 1 second or 1697V DC for 1 second    |
| Input Group to Backplane Isolation and Input Group to Input Group Isolation | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                           |
| FET Output Group to Backplane Isolation                                     | Verified by one of the following dielectric tests: 1100V AC for 1 second or 1697V DC for 1 second    |
| FET Output Group to Backplane Isolation                                     | 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                           |
| Relay Output Group to Backplane Isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second    |
| Relay Output Group to Backplane Isolation                                   | 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Relay Output Group to Relay Output Group and FET Output Group Isolation     | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second    |
| Relay Output Group to Relay Output Group and FET Output Group Isolation     | 265V AC Working Voltage (basic insulation), 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Analog Input Filter Settings

| Analog Input Filter Settings Filter Bandwidth (-3 dB Freq Hz) Sampling Frequency   |
|------------------------------------------------------------------------------------|
| 250 Hz 250 Hz 1 kHz                                                                |
| 60 Hz 60 Hz 1 kHz                                                                  |
| 50 Hz 50 Hz 1 kHz                                                                  |
| 10 Hz 10 Hz 1 kHz                                                                  |

## Working Voltage

## 1762 Expansion I/O Specifications

## General Specifications – Discrete I/O Modules

| Attribute Value                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions Height: 90 mm (3.54 in.), 110 mm (4.33 in.) (including mounting tabs) Width: 87 mm (3.43 in.) Depth: 40.4 mm (1.59 in.) |
| Enclosure type rating None (open-style)                                                                                            |

## Environmental Specifications

| Attribute Value                                  |                                                                                                                                                                                                                               |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating                           | IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock): °°°° pg  -20 °C ≤ Ta ≤ +65 °C (-4 °F ≤ Ta ≤ +149 °F)                                                                                                                                                                                                                               |
| Temperature, ambient, max 65 °C (140 °F)         |                                                                                                                                                                                                                               |
| Temperature, surrounding air, max 65 °C (140 °F) |                                                                                                                                                                                                                               |
| Temperature, nonoperating                        | IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock): °° -40…+85 °C (-40…+185 °F)                                                                                                                                                                                                                               |
| Relative humidity                                | IEC 60068-2-30 (Test Db, Unpackaged Damp Heat): 5…95% noncondensing                                                                                                                                                           |
| Vibration                                        | IEC 60068-2-6 (Test Fc, Operating): 5 g @ 10…500 Hz                                                                                                                                                                           |
| Shock, operating                                 | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30 g - Panel mounted                                                                                                                                                              |
| Shock, nonoperating                              | IEC 60068-2-27 (Test Ea, Unpackaged Shock): 30 g - Panel mounted 40 g - DIN rail mounted                                                                                                                                      |
|                                                  | Emissions IEC 61000-6-4                                                                                                                                                                                                       |
| ESD Immunity                                     | EC 61000-4-2: 4 kV contact discharges 8 kV air discharges                                                                                                                                                                     |
| Radiated RF Immunity                             | IEC 61000-4-3: 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                                                                                                                             |
| EFT/B Immunity                                   | IEC 61000-4-4: ±2 kV @ 5 kHz on power ports ±2 kV @ 5 kHz on signal ports ±1 kV @ 5 kHz on communication ports                                                                                                                |
| Surge Transient Immunity                         | IEC 61000-4-5: ±2 kV line-line(DM) and ±4 kV line-earth(CM) on AC power ports ±500V line-line(DM) and ±1 kV line-earth(CM) on signal ports ±1 kV line-earth(CM) on shielded ports ±2 kV line-earth(CM) on communication ports |
| Conducted RF Immunity                            | IEC 61000-4-6: 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                                                        |

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us                                      | UL Listed Industrial Control Equipment, certified for U.S. and Canada. See UL File E322657. UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for U.S. and Canada. See UL File E334470.                                                                                                                                                                                                                  |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) European Union 2014/35/EU LVD, compliant with: EN 61131-2; Programmable Controllers (Clause 11) European Union 2011/62/EU RoHS, compliant with: EN IEC 63000; Technical Documentation |
| RCM                                          | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emmissions                                                                                                                                                                                                                                                                                                                                                 |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                                                                                                                                                             |
| UKCA                                         | 2016 No. 1091 – Electromagnetic Compatibility Regulations 2016 No. 1101 – Electrical Equipment (Safety) Regulations 2012 No. 3032 – Restriction of the Use of Certain Hazardous Substances in Electrical and Electronic Equipment Regulations                                                                                                                                                                                           |

## Input Specifications – 1762-IA8, 1762-IQ8, 1762-IQ16, 1762-IQ32T, 1762-IQ8OW6

|                                                                                                        |                                                                                         |                                                                  |                                                                                         | Specification 1762-IA8 1762-IQ8 1762-IQ16 1762-IQ32T 1762-IQ8OW6                                    |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Shipping weight, approx. (with carton)                                                                 | 209 g (0.46 lbs.) 200 g (0.44 lbs.) 230 g (0.51 lbs.) 200g (0.44 lbs.) 280g (0.62 lbs.) |                                                                  |                                                                                         |                                                                                                     |
| Voltage category 100/120V AC                                                                           | 24V DC (sink/source)(1)                                                                 | 24V DC (sink/source)(1)                                          | 24V DC (sink/source)(1)                                                                 | 24V DC (sink/source) (1)                                                                            |
| Operating voltage range 79V AC…132V AC at 47 Hz…63 Hz                                                  | 10…30V DC at 30 °C (86 °F) 10…26.4V DC at 55 °C (131 °F)                                | 10…30V DC 10…26.4V DC (3)(2)                                     | 10…30V DC (24 points) at °° 30 °C (86 °F) 10…26.4V DC (23 points) at °° 60 °C (140 °F)                                                                                         | 10…30V DC at 30 °C (86 °F) 10…26.4V DC at 65 °C (149 °F)                                            |
|                                                                                                        |                                                                                         | Number of inputs 8 8 16 32 8                                     |                                                                                         |                                                                                                     |
| Bus current draw, max 50 mA at 5V DC (0.25 W) 50 mA at 5V DC (0.25 W)                                  |                                                                                         | 70 mA at 5V DC (0.35 W) (3)                                      | 170 mA at 5V DC 0 mA at 24V DC                                                          | 110 mA at 5V DC 80 mA at 24V DC                                                                     |
| Heat dissipation, max 2.0 W 3.7 W                                                                      |                                                                                         | 4.3 W at 26.4V 5.4 W at 30V(3)                                   | 5.4 W at 26.4V DC 6.8 W at 30V DC                                                       | 5.0 W at 30V DC 4.4 W at 26.4V DC (The Watts per point, plus the min W, with all points energized.) |
| Signal delay, max  On delay: 20.0 ms Off delay: 20.0 ms                                                | On delay: 8.0 ms Off delay: 8.0 ms                                                      | On delay: 8.0 ms Off delay: 8.0 ms                               | On delay: 8.0 ms Off delay: 8.0 ms                                                      | On delay: 8.0 ms Off delay: 8.0 ms                                                                  |
| Off-state voltage, max 20V AC 5V DC 5V DC 5V DC 5V DC                                                  |                                                                                         |                                                                  |                                                                                         |                                                                                                     |
| Off-state current, max 2.5 mA 1.5 mA 1.5 mA 1.0 mA 1.5 mA                                              |                                                                                         |                                                                  |                                                                                         |                                                                                                     |
| On-state voltage, min 79V AC (min) 132V AC (max) 10V DC 10V DC 10V DC 10V DC                           |                                                                                         |                                                                  |                                                                                         |                                                                                                     |
| On-state current 5.0 mA min at 79V AC 47 Hz 12.0 mA nom. at 120V AC 60 Hz 16.0 mA max at 132V AC 63 Hz | 2.0 mA min at 10V DC 8.0 mA nom. at 24V DC 12.0 mA max at 30V DC                        | 2.0 mA min at 10V DC 8.0 mA nom. at 24V DC 12.0 mA max at 30V DC | 1.6 mA min at 10V DC 2.0 mA min at 15V DC 5.7 mA max at 26.4V DC 6.5 mA max at 30.0V DC | 10 mA at 5V DC                                                                                      |
|                                                                                                        | Inrush current, max 250 mA Not applicable Not applicable Not applicable 250 mA          |                                                                  |                                                                                         |                                                                                                     |
| Nominal impedance  12K Ω at 50 Hz 10K Ω at 60 Hz                                                       | 3K Ω                                                                                    | 3K Ω                                                             | 4.7K Ω                                                                                  | 3K Ω                                                                                                |
|                                                                                                        |                                                                                         | IEC input compatibility Type 1+ Type 1+ Type 1+ Type 1 Type 1+   |                                                                                         |                                                                                                     |
| Isolated groups  Group 1: inputs 0…7 (internally connected commons)                                    | Group 1: inputs 0…7 (internally connected commons)                                      | Group 1: inputs 0…7; Group 2: inputs 8…15                        | Group 1: Inputs 0…7; Group 2: Inputs 8…15; Group 3: Inputs 16…23; Group 4: Inputs 24…31 | Group 1: inputs 0…3; Group 2: inputs 4…7                                                            |

## Input Specifications – 1762-IA8, 1762-IQ8, 1762-IQ16, 1762-IQ32T, 1762-IQ8OW6 (Continued)

|                                                                                                                                                      |                                                                                                                                                                                         |                                                                                                                                                    |                                                                                                                                                    | Specification 1762-IA8 1762-IQ8 1762-IQ16 1762-IQ32T 1762-IQ8OW6                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Verified by one of the following dielectric tests: 1517V AC for 1 s or 2145V DC for 1 s. 132V AC working voltage (IEC Class 2 reinforced insulation) | Input group to backplane isolation Verified by one of the following dielectric tests: 1200V ACAC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Vendor I.D. code 1                                                                                                                                   | Vendor I.D. code 1                                                                                                                                                                      | Vendor I.D. code 1                                                                                                                                 | Vendor I.D. code 1                                                                                                                                 | Vendor I.D. code 1                                                                                                                                 |
| Product type code 7                                                                                                                                  | Product type code 7                                                                                                                                                                     | Product type code 7                                                                                                                                | Product type code 7                                                                                                                                | Product type code 7                                                                                                                                |
|                                                                                                                                                      | Product code 114 96 97 99 98                                                                                                                                                            |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |

## Output Specifications – 1762-OA8, 1762-OB8, 1762-OB16, 1762-OB32T, 1762-OV32T

| Specification 1762-OA8 1762-OB8 1762-OB16 1762-OB32T 1762-OV32T                            |                                                                                                                                                      |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Shipping weight, approx. (with carton)                                                     |                                                                                                                                                      |                                                                                                                                                     |                                                                                                                                                     | 215 g (7.58 oz.) 210 g (7.41 oz.) 235 g (8.29 oz.) 200 g (7.05 oz.) 200 g (7.05 oz.)                                                                |                                                                                                                                                     |
| Voltage category 100…240V AC 24V DC 24V DC 24V DC source 24V DC sink                       |                                                                                                                                                      |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
|                                                                                            | Operating voltage range 85…265V AC at 47…63 Hz 20.4…26.4V DC 20.4…26.4V DC 10.2…26.4V DC 10.2…26.4V DC                                               |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| Number of outputs 8 8 16 32 32                                                             |                                                                                                                                                      |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| Bus current draw, max                                                                      | 115 mA at 5V DC (0.575 W)                                                                                                                            |                                                                                                                                                     | 115 mA at 5V DC (0.575 W) 175 mA at 5V DC (0.88 W)                                                                                                  | 175 mA at 5V DC 0 mA at 24V DC                                                                                                                      | 175 mA at 5V DC 0 mA at 24V DC                                                                                                                      |
| Heat dissipation, max 2.9 W 1.61 W                                                         |                                                                                                                                                      |                                                                                                                                                     | 2.9 W at 30 °C (86 °F) 2.1 W at 55 °C (131 °F)                                                                                                      |                                                                                                                                                     | 3.4 W at 26.4 DC 2.7 W at 26.4V DC                                                                                                                  |
| Signal delay, max – resistive load                                                         | On delay: 1/2 cycle Off delay: 1/2 cycle                                                                                                             | On delay: 0.1 ms Off delay: 1.0 ms                                                                                                                  | On delay: 0.1 ms Off delay: 1.0 ms                                                                                                                  | On delay: 0.5 ms Off delay: 4.0 ms                                                                                                                  | On delay: 0.5 ms Off delay: 4.0 ms                                                                                                                  |
| Off-state leakage current, max                                                             | 2 mA at 132V, 2.5 mA at 265V                                                                                                                         |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     | 1.0 mA 1.0 mA 0.1 mA at 26.4V DC 0.1 mA at 26.4V DC                                                                                                 |
| On-state current, min 10 mA 1.0 mA 1.0 mA 1.0 mA 1.0 mA                                    |                                                                                                                                                      |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| On-state voltage drop, max 1.5V at 0.5 A 1.0V DC 1.0V DC 0.3V DC at 0.5 A 0.3V DC at 0.5 A |                                                                                                                                                      |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| Continuous current per point, max                                                          | 0.25 A at 55 °C (131 °F) 0.5 A at 30 °C (86 °F)                                                                                                      | 0.5 A at 55 °C (131 °F) 1.0 A at 30 °C (86 °F)                                                                                                      | 0.5 A at 55 °C (131 °F) 1.0 A at 30 °C (86 °F)                                                                                                      |                                                                                                                                                     | 0.5 A at 60 °C (140 °F) 0.5 A at 60 °C (140 °F)                                                                                                     |
| Continuous current per common, max                                                         | 1.0 A at 55 °C (131 °F) 2.0 A at 30 °C (86 °F)                                                                                                       | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                      | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                      |                                                                                                                                                     | 2.0 A at 60 °C (140 °F) 2.0 A at 60 °C (140 °F)                                                                                                     |
| Continuous current per module, max                                                         | 2.0 A at 55 °C (131 °F) 4.0 A at 30 °C (86 °F)                                                                                                       | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                      | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                      |                                                                                                                                                     | 4.0 A at 60 °C (140 °F) 4.0 A at 60 °C (140 °F)                                                                                                     |
| Surge current, max                                                                         | 5.0 A (Repeatability is once every 2 s for a duration of 25 ms.                                                                                      | 2.0 A (Repeatability is once °° py  every 2 s at 55 °C (131 °F), ° y  once every second at 30 °C ° y  (86 °F) for a duration of 10 ms.)                                                                                                                                                     | 2.0 A (Repeatability is once °° py  every 2 s at 55 °C (131 °F), ° y  once every second at 30 °C ° y  (86 °F) for a duration of 10 ms.)                                                                                                                                                     | 2.0 A (Repeatability is once °° py  every 2 s at 60 °C (140 °F) for 10 ms)                                                                                                                                                     | 2.0 A (Repeatability is once °° py  every 2 s at 60 °C (140 °F) for 10 ms)                                                                                                                                                     |
| Isolated groups                                                                            | Group 1: Outputs 0…3 Group 2: Outputs 4…7                                                                                                            | Group 1: Outputs 0…7 Group 1: Outputs 0…15                                                                                                          |                                                                                                                                                     | Group 1: Outputs 0…15 Group 2: Outputs 16…31 (internally connected to common)                                                                       | Group 1: Outputs 0…15 Group 2: Outputs 16…31 (internally connected to common)                                                                       |
| Output group to backplane isolation                                                        | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s. 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s. 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s. 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s. 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Output group to output group isolation                                                     | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (IEC Class 2 reinforced insulation) | Not applicable                                                                                                                                      | Not applicable                                                                                                                                      | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s. 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s. 75V DC working voltage (IEC Class 2 reinforced insulation) |

## Output Specifications – 1762-OA8, 1762-OB8, 1762-OB16, 1762-OB32T, 1762-OV32T (Continued)

| Specification 1762-OA8 1762-OB8 1762-OB16 1762-OB32T 1762-OV32T   |         |
|-------------------------------------------------------------------|---------|
| Vendor I.D. code 1                                                |         |
| Product type code 7                                               |         |
| Product code 119 101 103                                          | 100 102 |

## Output Specifications – 1762-OW8, 1762-OW16, 1762-OX6I, 1762-IQ8OW6

|                                                                                                                                                                                                 |                                                                                                                                                                                                 |                                                                                                                                                                                                 | Specification 1762-OW8 1762-OW16 1762-OX6I 1762-IQ8OW6                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shipping weight, approx. (with carton) 228 g (0.50 lbs.) 285 g (0.63 lbs.) 220 g (0.485 lbs) 280 g (0.62 lbs.)                                                                                  |                                                                                                                                                                                                 |                                                                                                                                                                                                 |                                                                                                                                                                                                 |
| Voltage category AC/DC normally open relay AC/DC normally open relay AC/DC Type C Relay                                                                                                         |                                                                                                                                                                                                 |                                                                                                                                                                                                 | AC/DC normally open relay                                                                                                                                                                       |
| 5…265V AC 5…125V DC                                                                                                                                                                             | Operating voltage range  5…265V AC 5…125V DC                                                                                                                                                    | 5…265V AC 5…125V DC                                                                                                                                                                             | 5…265V AC 5…125V DC                                                                                                                                                                             |
|                                                                                                                                                                                                 | Number of outputs 8 16 6 6                                                                                                                                                                      |                                                                                                                                                                                                 |                                                                                                                                                                                                 |
| 80 mA at 5V DC (0.40 W) 90 mA at 24V DC (2.16 W)                                                                                                                                                | Bus current draw, max  140 mA at 5V DC (0.70 W)(1) 180 mA at 24V DC (4.32 W) (1)                                                                                                                | 110 mA at 5V DC (0.55 W) 110 mA at 24V DC (2.64 W)                                                                                                                                              | 110 mA at 5V DC 80 mA at 24V DC                                                                                                                                                                 |
| Heat dissipation, max 2.9 W                                                                                                                                                                     | 6.1 W(1)                                                                                                                                                                                        | 2.8 W                                                                                                                                                                                           | 5.0 W at 30V DC 4.4 W at 26.4V DC (The Watts per point, plus the min W, with all points energized.)                                                                                             |
| On Delay: 10 ms Off Delay: 10 ms                                                                                                                                                                | Signal delay, max – resistive load  On Delay: 10 ms Off Delay: 10 ms                                                                                                                            | On Delay: 10 ms (max) 6 ms (typical) Off Delay: 20 ms (max) 12 ms (typical)                                                                                                                     | On-delay: 10 ms (max) Off-delay: 10 ms (max)                                                                                                                                                    |
|                                                                                                                                                                                                 | Off-state leakage, max 0 mA 0 mA 0 mA 0 mA                                                                                                                                                      |                                                                                                                                                                                                 |                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |                                                                                                                                                                                                 | On-state current, min 10 mA 10 mA 100 mA 10 mA                                                                                                                                                  |                                                                                                                                                                                                 |
| On-state voltage drop, max Not Applicable                                                                                                                                                       | On-state voltage drop, max Not Applicable                                                                                                                                                       | On-state voltage drop, max Not Applicable                                                                                                                                                       | On-state voltage drop, max Not Applicable                                                                                                                                                       |
| Continuous current per point, max 2.5 A. See Table 15                                                                                                                                           | Continuous current per point, max 2.5 A. See Table 15                                                                                                                                           | 7 A See Table 16 .                                                                                                                                                                              | 2.5 A See Table 15 .                                                                                                                                                                            |
| Continuous current per common, max 8 A 8 A                                                                                                                                                      |                                                                                                                                                                                                 | 7 A See Table 16                                                                                                                                                                                | .  8 A                                                                                                                                                                                          |
|                                                                                                                                                                                                 | Continuous current per module, max 16 A 16 A                                                                                                                                                    | 30 A See Table 17 .                                                                                                                                                                             | 8 A                                                                                                                                                                                             |
| Surge current, max See Table 15. See Table 16. See Table 15                                                                                                                                     | Surge current, max See Table 15. See Table 16. See Table 15                                                                                                                                     |                                                                                                                                                                                                 | .                                                                                                                                                                                               |
| Group 1: Outputs 0…3 Group 2: Outputs 4…7                                                                                                                                                       | Isolated groups  Group 1: Outputs 0…7 Group 2: Outputs 8…15                                                                                                                                     | All 6 Outputs Individually Isolated.                                                                                                                                                            | Group 3: Outputs 0…5                                                                                                                                                                            |
| Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (IEC Class 2 reinforced insulation)                                            | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (IEC Class 2 reinforced insulation)                                            | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (IEC Class 2 reinforced insulation)                                            | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (IEC Class 2 reinforced insulation)                                            |
| Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (basic insulation) 150V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (basic insulation) 150V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (basic insulation) 150V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s. 265V AC working voltage (basic insulation) 150V AC working voltage (IEC Class 2 reinforced insulation) |
| Vendor I.D. code 1                                                                                                                                                                              | Vendor I.D. code 1                                                                                                                                                                              | Vendor I.D. code 1                                                                                                                                                                              | Vendor I.D. code 1                                                                                                                                                                              |
| Product type code 7                                                                                                                                                                             | Product type code 7                                                                                                                                                                             | Product type code 7                                                                                                                                                                             | Product type code 7                                                                                                                                                                             |
| Product code 120                                                                                                                                                                                | 121                                                                                                                                                                                             | 124 98                                                                                                                                                                                          |                                                                                                                                                                                                 |

Table 15 - Relay Contact Ratings – 1762-OW8, 1762-OW16, and 1762-IQ8OW6

|               | Maximum Volts Amperes Continuous   | Amperes Volt-Amperes   | Amperes Volt-Amperes      |                       |
|---------------|------------------------------------|------------------------|---------------------------|-----------------------|
|               |                                    |                        |                           | Make Break Make Break |
| 240V AC       | 2.5 A(1)                           |                        | 7.5 A 0.75 A 1800VA 180VA |                       |
| 120V AC       | 2.5 A(1)                           |                        | 15 A 1.5 A 1800VA 180VA   |                       |
| 125V DC 1.0 A |                                    | 0.22 A(2)              |                           |                       |
|               |                                    | 28VA 24V DC 2.0 A 1 2 A(2) 1.2 A(2)                        |                           |                       |

Table 16 - Relay Contact Ratings 1762-OX6I

| Volts (Max)              | Continuous Amps per Point (Max)(1)   | Amperes (2)   | Amperes (2)                    | Volt-Amperes   | Volt-Amperes          |
|--------------------------|--------------------------------------|---------------|--------------------------------|----------------|-----------------------|
| Volts (Max)              | Continuous Amps per Point (Max)(1)   |               |                                |                | Make Break Make Break |
| 240V AC 5.0 A 15 A 1.5 A |                                      |               |                                | 3600VA 360VA   |                       |
| 120V AC                  | 7.0 A(3)                             |               | 30 A 3.0 A                     | 3600VA 360VA   |                       |
| 125V DC 2.5 A 0.4 A      |                                      |               |                                | 50VA(4)        |                       |
|                          |                                      |               | 24V DC 7.0 A(3) 7.0 A 168VA(4) |                |                       |

g 
(3) 6 A in ambient temperatures above 40 °C (104 °F)

(4) DC Make/Break Volt-amperes must be limited to 50VA for DC voltages between 28V DC and 125V DC. DC Make/Break Volt-amperes below 28V DC are limited by the 7 A Make/Break current limit.

Table 17 - Module Load Ratings 1762-OX6I

|                | Volts (Max) Controlled Load (Current) per Module (Max)   |
|----------------|----------------------------------------------------------|
| 240V AC 6 A    |                                                          |
| 120V AC        | 12 A(1)                                                  |
| 125V DC 11.5 A |                                                          |
| 24V DC         | 30 A(2)                                                  |

- (1) Current per relay is limited to 6 A at ambient temperatures above 40 °C (104 °F).

(2) 24 A in ambient temperatures above 40 °C (104 °F). Limited by ambient temperature and the number of relays controlling loads. See Figure 68 .

Figure 68 - Relays Used vs. Maximum Current per Relay (24V DC) 1762-OX6I

<!-- image -->

## Analog Modules

## Common Specifications – 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4, 1762-OF4

| Specification 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4, 1762-OF4                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions HxWxD 90 x 87 x 40 mm height including mounting tabs is 110 mm (3.54 x 3.43 x 1.58 in.) height including mounting tabs is 4.33 in.                                                              |
| Temperature, storage -40…+85 °C (-40…+185 °F)                                                                                                                                                              |
| Temperature, operating  -20…+65 °C (-4…+149 °F) (1)                                                                                                                                                        |
| Operating humidity 5…95% noncondensing                                                                                                                                                                     |
| Operating altitude 2000 m (6561 ft)                                                                                                                                                                        |
| Vibration Operating: 10…500 Hz, 5 g, 0.030 in. max peak-to-peak                                                                                                                                            |
| Shock Operating: 30 g                                                                                                                                                                                      |
| Module power status indicator On: Indicates power is applied.                                                                                                                                              |
| Recommended cable Belden 8761 (shielded) — For 1762-IT4, shielded thermocouple extension wire for the specific type of thermocouple you are using. Follow the thermocouple manufacturer’s recommendations. |

## Environmental Specifications

| Attribute Value          |                                                                                                                                                                       |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          | Emissions IEC 61000-6-4                                                                                                                                               |
| ESD immunity             | IEC 61000-4-2: 6 kV contact discharges 8 kV air discharges                                                                                                            |
| Radiated RF immunity     | IEC 61000-4-3: 10V/m with 1 kHz sine wave 80% AM from 80…1000 MHz 3V/m with 1 kHz sine wave 80% AM from 1.4…2.0 GHz 1V/m with 1 kHz sine wave 80% AM from 2.0…2.7 GHz |
| EFT/B immunity           | IEC 61000-4-4: ±2 kV @ 5 kHz on signal ports                                                                                                                          |
| Surge transient immunity | IEC 61000-4-5: ±1 kV line-earth(CM) on shielded ports                                                                                                                 |
| Conducted RF immunity    | IEC 61000-4-6: 10V rms with 1 Hz sine wave 80% AM from 150 kHz…80 MHz(1)                                                                                              |

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                              | UL UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations                                                                                                                  |
|                                              | cUL UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for Canada.                                                                                          |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
| RCM                                          | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                 |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                               |

## General Specifications – 1762-IF2OF2, 1762-IF4, 1762-OF4, 1762-IR4, 1762-IT4

|                                            | Specification 1762-IF2OF2 1762-IF4 1762-OF4 1762-IR4 1762-IT4                                                                                    |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Shipping weight, approx. (with carton)     |                                                                                                                                                  | 240 g (0.53 lbs.) 235 g (0.517 lbs.) 260 g (0.57 lbs.) 220 g (0.53 lbs.)                                                                         |                                                                                                                    |                                                                                                                                                                |                                                                        |
| Bus current draw, max                      | 40 mA at 5V DC 105 mA at 24V DC                                                                                                                  | 40 mA at 5V DC 50 mA at 24V DC                                                                                                                   | 40 mA at 5V DC 165 mA at 24V DC                                                                                    | 40 mA at 5V DC 50 mA at 24V DC                                                                                                                                 | 40 mA at 5V DC 50 mA at 24V DC                                         |
| Analog normal operating range              | Voltage: 0…10V DC Current: 4…20 mA                                                                                                               | Voltage: -10…+10V DC Current: 4…20 mA                                                                                                            | Voltage 0…10V DC Current: 4…20 mA                                                                                  |                                                                                                                                                                | NA NA                                                                  |
| Full scale(1) analog ranges                | Voltage: 0…10.5V DC Current: 0…21 mA                                                                                                             | Voltage: -10.5…+10.5V DC Current: -21…+21 mA                                                                                                     | Voltage: 0…10.5V DC Current: 0…21 mA                                                                               |                                                                                                                                                                | NA NA                                                                  |
|                                            | Resolution 12 bits (unipolar)                                                                                                                    | 15 bits (bipolar) (2)                                                                                                                            | 12 bits (unipolar)                                                                                                 | Input filter and configuration dependent                                                                                                                       | 15 bits plus sign                                                      |
| Repeatability (3)                          | ±0.12% (2)                                                                                                                                       | ±0.12% (2)                                                                                                                                       | ±0.12% (2)                                                                                                         | ±0.1 °C (±0.18 °F) for Ni and NiFe ±0.2 °C (±0.36 °F)…±0.2 °C (±0.36 °F) for other RTD inputs ±0.04 ohm for 150 ohm resistances ±0.2 ohm for other resistances | See Table 18                                                           |
| Input and output group to system isolation | 30V AC/30V DC rated working voltage (4) (N.E.C. Class 2 required) (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC rated working voltage (4) (N.E.C. Class 2 required) (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC rated working voltage (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC working voltage type test: 500V AC or 707V DC for 1 minute                                                                                       | 30V AC/30V DC working voltage qualification test: 720V DC for 1 minute |
| Vendor I.D. code 1 1 1 1 1                 |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |
| Product type code 10 10 10 10 10           |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |
| Product code 75 67 66 65 64                |                                                                                                                                                  |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                                |                                                                        |

## Input Specifications – 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4

|                                                  | Specification 1762-IF2OF2 1762-IF4 1762-IR4 1762-IT4                                         |                                                                                   |                                                                                   |                                                                                                          |
|--------------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
|                                                  |                                                                                              |                                                                                   |                                                                                   | Number of inputs 2 differential (unipolar) 4 differential (bipolar) 4 4 input channels plus 1 CJC sensor |
| Update time (typical) 2.5 ms                     |                                                                                              | 130, 250, 290, 450, 530 ms (selectable)                                           | Input filter and configuration dependent                                          | NA                                                                                                       |
|                                                  | A/D converter type Successive approximation Successive approximation Delta-Sigma Delta-Sigma |                                                                                   |                                                                                   |                                                                                                          |
| Common mode voltage range (1)                    |                                                                                              | ±27V ±27V NA ±10V                                                                 |                                                                                   |                                                                                                          |
| Common mode rejection (2)                        |                                                                                              | > 55 dB at 50 Hz and 60 Hz > 55 dB at 50 Hz and 60 Hz                             | >110 dB at 50 Hz (with 10 Hz or 60 Hz filter)                                     | >110 dB at 50 Hz (with 10 Hz or 60 Hz filter)                                                            |
| Non-linearity (in percent full scale) ±0.12% (3) |                                                                                              | ±0.12% (2)                                                                        | ±0.05% NA                                                                         |                                                                                                          |
| Typical overall accuracy (4)                     | ±0.55% full scale at - 20…+65 °C(2) ±0.3% full scale at 25 °C                                | ±0.32% full scale at -20…+65 °C (2) ±0.24% full scale at 25 °C                    | ±0.5 °C ( °F) for Pt 385 NA                                                       |                                                                                                          |
| Input impedance                                  | Voltage Terminal: 200 kΩ Current Terminal: 250 Ω                                             | Voltage Terminal: 200 kΩ Current Terminal: 275 Ω                                  | >10 MΩ                                                                            | >10 MΩ                                                                                                   |
| Current input protection ±32 mA ±32 mA NA NA     |                                                                                              |                                                                                   |                                                                                   |                                                                                                          |
| Voltage input protection ±30V ±30V NA NA         |                                                                                              |                                                                                   |                                                                                   |                                                                                                          |
| Channel diagnostics                              | Over or under range or open circuit condition by bit reporting for analog inputs.            | Over or under range or open circuit condition by bit reporting for analog inputs. | Over or under range or open circuit condition by bit reporting for analog inputs. | Over or under range or open circuit condition by bit reporting for analog inputs.                        |

## Input Specifications 1762-IR4

| Specification 1762-IR4                                                 |                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input types                                                            | 100 Ω Platinum 385 200 Ω Platinum 385 500 Ω Platinum 385 1000 Ω Platinum 385 100 Ω Platinum 3916 200 Ω Platinum 3916 500 Ω Platinum 3916 1000 Ω Platinum 3916 10 Ω Copper 426 120 Ω Nickel 672 120 Ω Nickel 618 604 Ω Nickel-Iron 518 0...150 Ω 0...500 Ω 0...1000 Ω 0...3000 Ω |
|                                                                        | Heat dissipation 1.5 Total Watts (The Watts per point, plus the minimum Watts, with all points enabled.)                                                                                                                                                                        |
| Normal mode rejection ratio                                            | 70 dB minimum at 50 Hz with the 10 Hz or 50 Hz filter selected 70 dB minimum at 60 Hz with the 10 Hz or 60 Hz filter selected                                                                                                                                                   |
| Typical accuracy [Auto-calibration enabled] at 25 °C ° ypy  (77 °F) ambient with module operating temperature at 25 °C (77 °F) (1)                                                                        | ±0.5 °C ( °F) for Pt 385 ±0.4 °C ( °F) for Pt 3916 ±0.2 °C ( °F) for Ni ±0.3 °C ( °F) for NiFe ±0.6 °C ( °F) for Cu ±0.15 Ω for 150 Ω range ±0.5 Ω for 500 Ω range ±1.0 Ω for 1000 Ω range ±1.5 Ω for 3000 Ω range                                                              |
| Typical accuracy [Auto-calibration enabled] at 0…55 ° C (32…131 °F)(1) | ±0.9 °C ( °F) for Pt 385 ±0.8 °C ( °F) for Pt 3916 ±0.4 °C ( °F) for Ni ±0.5 °C ( °F) for NiFe ±1.1 °C ( °F) for Cu ±0.25 Ω for 150 Ω range ±0.8 Ω for 500 Ω range ±1.5 Ω for 1000 Ω range ±2.5 Ω for 3000 Ω range                                                              |
| Accuracy drift at 0…55 ° C (32…131 °F)                                 | ±0.026 °C/°C (0.026 °F/°F) for Pt 385 ±0.023 °C/°C (0.023 °F/°F) for Pt 3916 ±0.012 °C/°C (0.012 °F/°F) for Ni ±0.015 °C/°C (0.015 °F/°F) for NiFe ±0.032 °C/°C (0.032 °F/°F) for Cu ±0.007 Ω/ °C (0.012 Ω/ °F) for 150 Ω range °° g ±0.023 Ω/ °C (0.041 Ω/ °F) for 500 Ω range °° g ±0.043 Ω/ °C (0.077 Ω/ °F) for 1000 Ω range °° g ±0.07 Ω/ °C (0.130 Ω/ °F) for 3000 Ω range                                                                                                                                                                                                                                                                                 |
|                                                                        | Excitation current source 0.5 mA and 1.0 mA selectable per channel                                                                                                                                                                                                              |

## Input Specifications 1762-IR4 (Continued)

| Specification 1762-IR4                                 |                                                                                                                                                                                                                          |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open-circuit detection time (2)                        | 6…1212 ms                                                                                                                                                                                                                |
| Input channel configuration                            | Via configuration software screen or the user program (by writing a unique bit pattern into the module’s configuration file). See your controller’s user manual to determine if user program configuration is supported. |
| Calibration                                            | The module performs auto-calibration on channel enable and on a configuration change between channels. You can also program the module to calibrate every 5 minutes.                                                     |
| Maximum overload at input terminals ±35V DC continuous |                                                                                                                                                                                                                          |
|                                                        | Cable impedance, max 25 Ω − Operating with >25 Ω reduces accuracy.                                                                                                                                                       |
| Channel to channel isolation ±10V DC                   |                                                                                                                                                                                                                          |

- (1) Accuracy is dependent upon the Analog/Digital converter filter rate selection, excitation current selection, data format, and input noise.

(2) Open-circuit detection time is equal to channel update time.

## Input Specifications 1762-IT4

| Specification Value                 |                                                                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|                                     | Heat dissipation 1.5 Total Watts (The Watts per point, plus the minimum Watts, with all points energized.)                                          |
|                                     | Response speed per channel Input filter and configuration dependent.                                                                                |
| Rated working voltage (1)           | 30V AC/30V DC                                                                                                                                       |
| Normal mode rejection ratio         | 85 dB (minimum) at 50 Hz (with 10 Hz or 50 Hz filter) 85 dB (minimum) at 60 Hz (with 10 Hz or 60 Hz filter)                                         |
|                                     | Cable impedance, max 25 Ω (for specified accuracy)                                                                                                  |
| Open-circuit detection time         | 7 ms…1.515 s(2)                                                                                                                                     |
| Calibration                         | The module performs auto-calibration upon power-up and whenever a channel is enabled. You can also program the module to calibrate every 5 minutes. |
|                                     | CJC accuracy ±1.3 °C (±2.34 °F)                                                                                                                     |
| Maximum overload at input terminals | ±35V DC continuous(3)                                                                                                                               |
| Input channel configuration         | Via configuration software screen or the user program (by writing a unique bit pattern into the module’s configuration file).                       |

Table 18 - 1762-IT4 Repeatability at 25 °C (77 °F) (1)(2)

| Input Type Repeatability for 10 Hz Filter                            |
|----------------------------------------------------------------------|
| Thermocouple J ±0.1 °C [±0.18 °F]                                    |
| Thermocouple N (-110…+1300 °C [-166…+2372 °F]) ±0.1 °C [±0.18 °F]    |
| Thermocouple N (-210…-110 °C [-346…-166 °F]) ±0.25 °C [±0.45 °F]     |
| Thermocouple T (-170…+400 °C [-274…+752 °F]) ±0.1 °C [±0.18 °F]      |
| Thermocouple T (-270…-170 °C [-454…-274 °F]) ±1.5 °C [±2.7 °F]       |
| Thermocouple K (-270…+1370 °C [-454 °F…+2498 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple K (-270…-170 °C [-454…-274 °F]) ±2.0 °C [±3.6 °F]       |
| Thermocouple E (-220…+1000 °C [-364…+1832 °F]) ±0.1 °C [±0.18 °F]    |
| Thermocouple E (-270…-220 °C [-454…-364 °F]) ±1.0 °C [±1.8 °F]       |
| Thermocouples S and R ±0.4 °C [±0.72 °F]                             |
| Thermocouple C ±0.2 °C [±0.36 °F]                                    |
| Thermocouple B ±0.7 °C [±1.26 °F]                                    |
| ±50 mV ±6 µV                                                         |
| ±100 mV ±6 µV                                                        |

## 1762-IT4 Accuracy

| Input Type (1)                                                                                                       | With Auto-calibration Enabled Without Auto-calibration                               |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|                                                                                                                      | Maximum Temperature Drift (2)                                                        |
| at 25 °C [77 °F] Ambient at 0…60 °C [32…140 °F] Ambient                                                              | at 0…60 °C [32…140 °F] Ambient                                                       |
| Thermocouple J (-210…+1200 °C [-346…+2192 °F]) ±0.6 °C [± 1.1 °F] ±0.9 °C [± 1.7 °F] ±0.0218 °C/ °C [±0.0218 °F/ °F] |                                                                                      |
| Thermocouple N (-200…+1300 °C [-328…+2372 °F]) ±1 °C [± 1.8 °F] ±1.5 °C [±2.7 °F] ±0.0367 °C/ °C [±0.0367 °F/ °F]    |                                                                                      |
| Thermocouple N (-210…-200 °C [-346…-328 °F]) ±1.2 °C [±2.2 °F] ±1.8 °C [±3.3 °F] ±0.0424 °C/ °C [±0.0424 °F/ °F]     |                                                                                      |
| Thermocouple T (-230…+400 °C [-382…+752 °F]) ±1 °C [± 1.8 °F] ±1.5 °C [±2.7 °F] ±0.0349 °C/ °C [±0.0349 °F/ °F]      |                                                                                      |
| Thermocouple T (-270…-230 °C [-454…-382 °F]) ±5.4 °C [± 9.8 °F] ±7.0 °C [±12.6 °F] ±0.3500 °C/ °C [±0.3500 °F/ °F]   |                                                                                      |
| Thermocouple K (-230…+1370 °C [-382…+2498 °F]) ±1 °C [± 1.8 °F] ±1.5 °C [±2.7 °F] ±0.4995 °C/ °C [±0.4995 °F/ °F]    |                                                                                      |
| Thermocouple K (-270…-225 °C [-454…-373 °F]) ±7.5 °C [± 13.5 °F] ±10 °C [± 18 °F] ±0.0378 °C/ °C [±0.0378 °F/ °F]    |                                                                                      |
| Thermocouple E (-210…+1000 °C [-346…+1832 °F]) ±0.5 °C [± 0.9 °F] ±0.8 °C [±1.5 °F] ±0.0199 °C/ °C [±0.0199 °F/ °F]  |                                                                                      |
| Thermocouple E (-270…-210 °C [-454…-346 °F]) ±4.2 °C [± 7.6 °F] ±6.3 °C [±11.4 °F] ±0.2698 °C/ °C [±0.2698 °F/ °F]   |                                                                                      |
|                                                                                                                      | Thermocouple R ±1.7 °C [± 3.1 °F] ±2.6 °C [± 4.7 °F] ±0.0613 °C/ °C [±0.0613 °F/ °F] |
|                                                                                                                      | Thermocouple S ±1.7 °C [± 3.1 °F] ±2.6 °C [± 4.7 °F] ±0.0600 °C/ °C [±0.0600 °F/ °F] |
|                                                                                                                      | Thermocouple C ±1.8 °C [±3.3 °F] ±3.5 °C [±6.3 °F] ±0.0899 °C/ °C [±0.0899 °F/ °F]   |
|                                                                                                                      | Thermocouple B ±3.0 °C [±5.4 °F] ±4.5 °C [±8.1 °F] ±0.1009 °C/ °C [±0.1009 °F/ °F]   |
| ±50 mV ±15 µV ±25 µV                                                                                                 | ±0.44μV/ °C [±0.80µV/ °F]                                                            |
| ±100 mV ±20 µV ±30 µV                                                                                                | ±0.69μV/ °C [±01.25µV/ °F]                                                           |

<!-- image -->

## Output Specifications – 1762-IF2OF2, 1762-OF4

| Specification 1762-IF2OF2 1762-OF4                      |                                                                                                                            |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Number of outputs 2 single-ended (unipolar)             | 4 single-ended (unipolar)(2)                                                                                               |
| Update time (typical) 4.5 ms 2.5 ms                     |                                                                                                                            |
| D/A converter type Resistor string                      | R-2R ladder voltage switching                                                                                              |
|                                                         | Resistive load on current output 0…500 Ω (includes wire resistance) 0…500 Ω (includes wire resistance)                     |
| Load range on voltage output > 1 kΩ                     | > 1 KΩ                                                                                                                     |
| Reactive load, current output < 0.1 mH < 0.1 mH         |                                                                                                                            |
| Reactive load, voltage output < 1 µF < 1 µF             |                                                                                                                            |
| Typical overall accuracy (1)                            | ±1.17% full scale at -20…+65 °C (2) ±0.5% full scale at 25 °C ±1.17% full scale at -20…+65 °C(2) ±0.5% full scale at 25 °C |
| Output ripple range 0…500 Hz (see output range)         | < ±0.1% < ±0.1%                                                                                                            |
| Non-linearity (in percent full scale)  < ±0.59%(2)      | < ±0.59%(2)                                                                                                                |
| Open and short-circuit protection Continuous Continuous |                                                                                                                            |
| Output protection ±32 mA ±32 mA                         |                                                                                                                            |

For more detailed 1762-IT4 accuracy information, see MicroLogix 1200 Thermocouple/ mV Input Module User Manual, publication 1762-UM002 .

## Valid Input/output Data Word Formats/Ranges – 1762-IF2OF2

| Normal Operating Range Full Scale Range RAW/Proportional Data Scaled-for-PID   |                      |
|--------------------------------------------------------------------------------|----------------------|
| 0…10V DC                                                                       | 10.5V DC 32760 16380 |
| 0…10V DC                                                                       | 0.0V DC 0 0          |
| 4…20 mA                                                                        | 21.0 mA 32760 16380  |
| 4…20 mA                                                                        | 20.0 mA 31200 15600  |
| 4…20 mA                                                                        | 4.0 mA 6240 3120     |
| 4…20 mA                                                                        | 0.0 mA 0 0           |

## Notes:

## MicroLogix 1400 Controller Replacement Kits

## Lithium Battery (1747-BA)

## Replacement Parts

The table below provides a list of replacement parts and their catalog number.

| Description Catalog Number   |
|------------------------------|
| Lithium Battery 1747-BA      |

## IMPORTANT

When the controller's Battery Low indicator is lit, check whether the battery wire connector is connected correctly or replace the replaceable battery with a new one immediately. When the indicator turns on, it means that either the battery is disconnected, or that the battery requires replacement. The controller is designed to operate for up to 2 weeks, from the time that the indicator first turns on. We recommend that you replace the battery immediately when the indicator turns on.

## Installation

Follow the procedure below to ensure proper replaceable battery installation.

1. Insert a battery into the battery pocket with wires facing up.
2. Insert the battery wire connector into the battery connector.
3. Secure the battery connector wires around the 1762 expansion bus connector as shown in Figure 69 .

Figure 69 - Lithium Battery Installation

<!-- image -->

## Battery Handling

Follow the procedure below to ensure proper battery operation and reduce personnel hazards.

- Use only for the intended operation.
- Do not ship or dispose of cells except according to recommended procedures.

<!-- image -->

- Do not ship on passenger aircraft.

<!-- image -->

## Storage

Store lithium batteries in a cool, dry environment, typically 20…25 °C (68…77 °F) and 40…60% humidity. Store the batteries and a copy of the battery instruction sheet in the original container, away from flammable materials.

## Transportation

One or Two Batteries

Each battery contains 0.23 g (0.008 oz.) of lithium. Therefore, up to two batteries can be shipped together within the United States without restriction. Regulations governing shipment to or within other countries may differ.

Three or More Batteries

Procedures for the transportation of three or more batteries shipped together within the United States are specified by the Department of Transportation (DOT) in the Code of Federal Regulations, CFR49, "Transportation." An exemption to these regulations, DOT – E7052, covers the transport of certain hazardous materials classified as flammable solids. This exemption authorizes transport of lithium batteries by motor vehicle, rail freight, cargo vessel, and cargo-only aircraft, providing certain conditions are met. Transport by passenger aircraft is not permitted.

A special provision of DOT-E7052 (11th Rev., October 21, 1982, par. 8-a) provides that:

"Persons that receive cell and batteries covered by this exemption may reship them pursuant to the provisions of 49 CFR 173.22a in any of these packages authorized in this exemption including those in which they were received."

The Code of Federal Regulations, 49 CFR 173.22a, relates to the use of packaging authorized under exemptions. In part, it requires that you must maintain a copy of the exemption at each facility where the packaging is being used in connection with shipment under the exemption.

Shipment of depleted batteries for disposal may be subject to specific regulation of the countries involved or to regulations endorsed by those countries, such as the IATA Articles Regulations of the International Air Transport Association, Geneva, Switzerland.

IMPORTANT

Regulations for transportation of lithium batteries are periodically revised. See http://www.dot.gov for the latest shipping information.

## Disposal

<!-- image -->

ATTENTION: Do not incinerate or dispose of lithium batteries in general trash collection. Explosion or violent rupture is possible. Batteries should be collected for disposal in a manner to prevent against short-circuiting, compacting, or destruction of case integrity and hermetic seal.

## ATTENTION:

- Do not charge the batteries. An explosion could result or the cells could overheat causing burns.
- Do not open, puncture, crush, or otherwise mutilate the batteries. A possibility of an explosion exists and/or toxic, corrosive, and flammable liquids would be exposed.
- Do not incinerate or expose the batteries to high temperatures. Do not attempt to solder batteries. An explosion could result.
- Do not short positive and negative terminals together. Excessive heat can build up and cause severe burns.

For disposal, batteries must be packaged and shipped in accordance with transportation regulations, to a proper disposal site. The U.S. Department of Transportation authorizes shipment of "Lithium batteries for disposal" by motor vehicle only in regulation 173.1015 of CFR 49 (effective January 5, 1983). For additional information contact:

U.S. Department of Transportation Research and Special Programs Administration 400 Seventh Street, S.W. Washington, D.C. 20590

Although the Environmental Protection Agency at this time has no regulations specific to lithium batteries, the material contained may be considered toxic, reactive, or corrosive. The person disposing of the material is responsible for any hazard created in doing so. State and local regulations may exist regarding the disposal of these materials.

For a lithium battery product safety data sheet, contact the manufacturer:

Sanyo Energy Corporation Tadarand U.S. Battery Division San Diego, CA 92173 Port Washington, NY 11050

2001 Sanyo Avenue 2 Seaview Blvd. (619) 661-4801 (516) 621-4980

## Notes:

## Understand the Controller Status Indicators

## Troubleshoot Your System

The MicroLogix 1400 controller provides three groups of status indicators:

- the LED status indicators on the top of the controller,
- the status indicators on the LCD
- the I/O status indicators on the LCD.

Together they provide a mechanism to determine the current status of the controller if a programming device is not present or available.

## Controller Status Indicators

Figure 70 - Controller Status Indicator Location

<!-- image -->

## Controller Status Indicators

| Status Indicator Color Indicates   |                                                                         |
|------------------------------------|-------------------------------------------------------------------------|
| POWER                              | Off No input power, or power error condition                            |
| POWER                              | Green Power on                                                          |
| RUN                                | Off Not executing the user program                                      |
| RUN                                | Green Executing the user program in run mode                            |
| RUN                                | Green flashing Memory module transfer occurring                         |
| FAULT                              | Off No fault detected                                                   |
| FAULT                              | Red flashing Application fault detected                                 |
| FAULT                              | Red Controller hardware faulted                                         |
| FORCE                              | Off No forces installed                                                 |
| FORCE                              | Amber Forces installed                                                  |
| FORCE                              | Amber flashing Forces installed in force files but forcing is disabled. |

<!-- image -->

## Status Indicators on the LCD

Figure 71 - Status Indicators on the LCD

<!-- image -->

## Status Indicators on the LCD

|          |                       | Indicator Color Indicates                           |
|----------|-----------------------|-----------------------------------------------------|
| COMM 0   | Off (empty rectangle) | Not transmitting via RS-232/RS-485 port (Channel 0) |
| COMM 0   | On (solid rectangle)  | Transmitting via RS-232/RS-485 port (Channel 0)     |
| COMM 1   | Off (empty rectangle) | Not transmitting via Ethernet port (Channel 1)      |
| COMM 1   | On (solid rectangle)  | Transmitting via Ethernet port (Channel 1)          |
| COMM 2   | Off (empty rectangle) | Not transmitting via RS-232 port (Channel 2)        |
| COMM 2   | On (solid rectangle)  | Transmitting via RS-232 port (Channel 2)            |
| DCOMM(1) | Off (empty rectangle) | Configured communications (Channel 0)               |
| DCOMM(1) | On (solid rectangle)  | Default communications (Channel 0)                  |
| BAT. LO  | Off (empty rectangle) | Battery level is acceptable                         |
| BAT. LO  | On (solid rectangle)  | Battery low                                         |
| U-DISP   | Off (empty rectangle) | Default display mode                                |
| U-DISP   | On (solid rectangle)  | Customized display mode                             |

(1) When using a MicroLogix 1400 controller, the DCOMM LED applies only to Channel 0.

## I/O Status Indicators on the LCD

Figure 72 - I/O Status Indicators on the LCD

<!-- image -->

Table 19 - Status Indicator Error Conditions

|                                     | If the LEDS indicate: The Following Error Exists Probable Cause Recommended Action   |                                        |                                                                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| All LEDs off                        | No input power or power supply error                                                 |                                        | No line Power Verify proper line voltage and connections to the controller.                                                          |
| All LEDs off                        | No input power or power supply error                                                 | Power Supply Overloaded                | This problem can occur intermittently if power supply is overloaded when output loading and temperature varies.                      |
| Power and FAULT LEDs on solid       | Hardware faulted                                                                     |                                        | Processor Hardware Error Cycle power. Contact your local Allen-Bradley representative if the error persists.                         |
| Power and FAULT LEDs on solid       | Hardware faulted                                                                     |                                        | Loose Wiring Verify connections to the controller.                                                                                   |
| Power LED on and FAULT LED flashing | Application fault                                                                    | Hardware/Software Major Fault Detected | For error codes and Status File information, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 . |
| RUN FORCE FAULT LEDs all flashing   | Operating system fault                                                               | Missing or Corrupt Operating System    | See Recover from Missing or Corrupt OS State .                                                                                       |

## Controller Error Recovery Model

Figure 73 helps you diagnose software and hardware problems in the micro controller. The module provides common questions you might ask to help troubleshoot your system. See the recommended pages within the module for further help.

## I/O Status Indicators on the LCD

|           |                       | Indicator Color Indicates            |
|-----------|-----------------------|--------------------------------------|
| INPUTS(1) | Off (empty rectangle) | Input is not energized               |
| INPUTS(1) | On (solid rectangle)  | Input is energized (terminal status) |
| OUTPUTS   | Off (empty rectangle) | Output is not energized              |
| OUTPUTS   | On (solid rectangle)  | Output is energized (logic status)   |

## Normal Operation

The POWER and RUN status indicators are On. If forcing is enabled and forces are installed in I/O force files, the FORCE status indicator turns on and remains on until all forces are removed. And if forcing is disabled and forces are installed in I/O force files, the FORCE status indicator flashes and remains flashing until forces are removed from I/O force files.

## Error Conditions

If an error exists within the controller, the controller status indicators operate as described in Table 19 .

## Analog Expansion I/O Diagnostics and Troubleshooting

Figure 73 - Error Recovery Model

<!-- image -->

## IMPORTANT

From firmware revision 21.007 or later, you can enable an automatic fault recovery mechanism to recover the controller from 2H, 4H, 8H and 9H error codes. For more information see Auto Reset Functionality .

## Module Operation and Channel Operation

The module performs operations at two levels:

- module level
- channel level

Module-level operations include functions such as power-up, configuration, and communication with the controller.

Internal diagnostics are performed at both levels of operation. Both module hardware and channel configuration error conditions are reported to the controller. Channel over-range or under-range conditions are reported in the module's input data table. Module hardware errors are reported in the controller's I/O status file. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 for more information.

When a fault condition is detected, the analog outputs are reset to zero.

## Module Error Table

| “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   |                                                 |                                                 |                                                 |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
|                                                             | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                       |                                                             |                                                             |                                                 |                                                 |                                                 |
|                                                             |                                                             | 0000000000000000                                            |                                                             |                                                 |                                                 |                                                 |
|                                                             |                                                             |                                                             | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1 | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1 | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1 |

## Module Error Field

The purpose of the module error field is to classify module errors into three distinct groups, as described in the table below. The type of error determines what kind of information exists in the extended error information field. These types of module errors are typically reported in the controller's I/O status file. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 for more information.

.

## Module Error Types

| Error Type  Module Error Field Value Bits 11 through 09 (Binary)   | Description                                                                                                                                                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                    | No Errors 000 No error is present. The extended error field holds no additional information.                                                                                                         |
|                                                                    | Hardware Errors 001 General and specific hardware error codes are specified in the extended error information field.                                                                                 |
| Configuration Errors 010                                           | Module-specific error codes are indicated in the extended error field. These error codes correspond to options that you can change directly. For example, the input range or input filter selection. |

## Extended Error Information Field

Check the extended error information field when a non-zero value is present in the module error field. See Table 20 .

<!-- image -->

If no errors are present in the module error field, the extended error information field is set to zero.

## Power-up Diagnostics

At module power-up, a series of internal diagnostic tests are performed.

## Module Status LED State Table

| If module status LED is Indicated condition Corrective action                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------|
| On Proper Operation No action required                                                                                                 |
| Off Module Fault  Cycle power. If condition persists, replace the module. Call your local distributor or Allen-Bradley for assistance. |

## Critical and Non-Critical Errors

Non-critical module errors are recoverable. Channel errors (over-range or under-range errors) are non-critical. Non-critical error conditions are indicated in the module input data table. Non-critical configuration errors are indicated by the extended error code. See Table 20 .

Critical module errors are conditions that prevent normal or recoverable operation of the system. When these types of errors occur, the system leaves the run mode of operation. Critical module errors are indicated in Table 20 .

## Module Error Definition Table

Analog module errors are expressed in two fields as four-digit Hex format with the most significant digit as "don't care" and irrelevant. The two fields are "Module Error" and "Extended Error Information". The structure of the module error data is shown below.

Table 20 - Extended Error Codes for 1762-IF2OF2

| Error Type                                            | Error Description                                                           |
|-------------------------------------------------------|-----------------------------------------------------------------------------|
| Error Type                                            | No Error X000 000 0 0000 0000 No error                                      |
| General Common Hardware Error                         | X200 001 0 0000 0000 General hardware error; no additional information      |
| General Common Hardware Error                         | X201 001 0 0000 0001 Power-up reset state                                   |
| Hardware-Specific Error X210 001 0 0001 0000 Reserved |                                                                             |
| Configuration Error                                   | X400 010 0 0000 0000 General configuration error; no additional information |
| Configuration Error                                   | X401 010 0 0000 0001 Invalid input data format selected (channel 0)         |
| Configuration Error                                   | X402 010 0 0000 0010 Invalid input data format selected (channel 1)         |
| Configuration Error                                   | X403 010 0 0000 0011 Invalid output data format selected (channel 0)        |
| Configuration Error                                   | X404 010 0 0000 0100 Invalid output data format selected (channel 1)        |

(1) X represents “Don’t Care”.

Table 21 - Extended Error Codes for 1762-IF4 and 1762-OF4

| Error Type                    | Error Description                                                           |
|-------------------------------|-----------------------------------------------------------------------------|
| Error Type                    | No Error X000 000 0 0000 0000 No error                                      |
| General Common Hardware Error | X200 001 0 0000 0000 General hardware error; no additional information      |
| General Common Hardware Error | X201 001 0 0000 0001 Power-up reset state                                   |
| Hardware Specific Error                               | X300 001 1 0000 0000 Reserved                                               |
| Configuration Error           | X400 010 0 0000 0000 General configuration error; no additional information |
| Configuration Error           | X401 010 0 0000 0001 Invalid range select (Channel 0)                       |
| Configuration Error           | X402 010 0 0000 0010 Invalid range select (Channel 1)                       |
| Configuration Error           | X403 010 0 0000 0011 Invalid range select (Channel 2)                       |
| Configuration Error           | X404 010 0 0000 0100 Invalid range select (Channel 3)                       |
| Configuration Error           | X405 010 0 0000 0101  Invalid filter select (Channel 0) – 1762-IF4 only     |
| Configuration Error           | X406 010 0 0000 0110  Invalid filter select (Channel 1) – 1762-IF4 only     |
| Configuration Error           | X407 010 0 0000 0111  Invalid filter select (Channel 2) – 1762-IF4 only     |
| Configuration Error           | X408 010 0 0000 1000  Invalid filter select (Channel 3) – 1762-IF4 only     |
| Configuration Error           | X409 010 0 0000 1001 Invalid format select (Channel 0)                      |
| Configuration Error           | X40A 010 0 0000 1010 Invalid format select (Channel 1)                      |
| Configuration Error           | X40B 010 0 0000 1011 Invalid format select (Channel 2)                      |
| Configuration Error           | X40C 010 0 0000 1400 Invalid format select (Channel 3)                      |

(1) X represents “Don’t Care”.

## Hardware Errors

General or module-specific hardware errors are indicated by module error code 2.

Configuration Errors

If you set the fields in the configuration file to invalid or unsupported values, the module ignores the invalid configuration, generates a non-critical error, and keeps operating with the previous configuration.

Table 20 lists the configuration error codes defined for the module.

## Error Codes

## Contact Rockwell Automation for Assistance

If you need to contact Rockwell Automation or local distributor for assistance, it is helpful to obtain the following (prior to calling):

- Controller type, series letter, revision letter, and firmware (FRN) number of the controller
- Controller indicator status
- Controller error codes. See MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 for error code information.

## Notes:

## Prepare for Firmware Update

<!-- image -->

## Use ControlFLASH to Upgrade Your Operating System

The operating system (OS) firmware can be upgraded through the Ethernet port of the controller. To download a new operating system, you must have the ControlFLASH™ Upgrade Kit referred to in ControlFLASH User Manual, publication 1756-UM105, as newer controller's operating system (OS) firmware is prepared in DMK format and requires ControlFLASH version 13.00 or higher.

Before upgrading the controller operating system, you must:

- Install ControlFLASH software on your personal computer.
- Extract the DMK kit that contains the latest Firmware – for ControlFLASH version 13.00 or higher only.
- Prepare the controller for updating.

## Install ControlFLASH Software

To install ControlFLASH properly, see the Install ControlFLASH section in ControlFLASH User Manual, publication 1756-UM105 .

If a ControlFLASH directory does not exist, one is created in your Program Files directory.

## Use DMK Extraction Tool for Firmware Update

This section applies only to newer OS firmware prepared in DMK format, which requires ControlFLASH version 13.00 or higher.

1. Launch the DMK Extraction Tool application under Programs &gt; Flash Programming Tools.

<!-- image -->

2. Select Browse and choose the location of DMK file in the system.
3. Select OK.
4. Select one or more DMK files that you want extract and select Extract.
5. Select OK. Select Cancel to close the DMK Extraction Tool.

<!-- image -->

<!-- image -->

<!-- image -->

6. Once you have extracted the DMK files, they no longer appear in the Extraction Tool folder.

<!-- image -->

## Prepare the Controller for Firmware Update

1. It is important that the SNMP server is enabled before the firmware update begins. You can check if the SNMP server is enabled by looking at the Channel Configuration page for Channel 1 in RSLogix 500/RSLogix Micro. If the SNMP server is not enabled, you can still enable it in the channel configuration page.

<!-- image -->

Alternatively, you can enable SNMP with the LCD display. For more information, see Configure Ethernet Protocol Setup on page 103

## IMPORTANT

The user program is cleared as part of the operating system upgrade process. You must restore your program after successfully loading the operating system upgrade. The Ethernet communication configuration parameters are retained after a successful firmware update.

## IMPORTANT

A power cycle is needed in order for the changes in the Channel Configuration page to be applied.

2. Ensure that you complete the IP configuration for the OS firmware update. Note the assigned IP address of the controller.

If the IP address is not configured, you can still perform the IP configuration with Static, BOOTP or DHCP settings. Once the IP configuration is done, it is used throughout the firmware update process.

## Use ControlFLASH for Firmware Update

If the IP configuration has been done, the IP address may be read from the processor when online with RSLogix 500/RSLogix Micro. In the Channel Configuration dialog box, select the Chan. 1 – System tab or use the LCD.

3. Set the controller to Program mode before you start the firmware update (access the Mode Switch from the LCD).

See Mode Switch for information about controller modes and how to use the Mode Switch.

See View Ethernet Status to find how to browse for the controller's IP address.

<!-- image -->

ATTENTION: Do not interrupt the update procedure once you have begun to download the firmware. If the update procedure is interrupted, the controller is in a Missing or Corrupt OS state on the next power-up.

To recover the controller from a missing/corrupt OS state, see Missing or Corrupt OS state .

1. Launch the ControlFLASH application under Programs &gt; Flash Programming Tools. If the Ethernet connection (IP configuration) has not been established, attach an Ethernet cable to the controller from your computer (or a hub), and ensure that the Ethernet connection is intact throughout the upgrade process.

## IMPORTANT

If you are connecting to the controller through a hub, you can use a standard Ethernet patch cable.

If you are connecting to the controller directly from your computer, you must use an Ethernet crossover cable.

The Welcome to ControlFLASH dialog box displays.

<!-- image -->

2. Select Next.
3. Select the appropriate catalog number from the Catalog Number dialog box and select Next.

<!-- image -->

The AB\_SNMP.DLL – Enter IP Address dialog box displays.

<!-- image -->

4. Type in the IP address for the processor.

## IMPORTANT

Use the IP address that was configured earlier, or use an available IP address that is assigned to by your network administrator.

5. Select Get Info. If the IP address was previously configured and the necessary information about the controller is obtained, go to step 9 .
6. The AB\_SNMP – BOOTP Server dialog box displays, indicating that this IP address has not been configured into the processor.
7. Enter the hardware address of the controller that is being upgraded (as noted in step 2 of Prepare the Controller for Firmware Update) and select OK.

<!-- image -->

For the IP address to be configured using the ControlFLASH BOOTP server, enable the BOOTP settings in the controller, see step 2 of Prepare the Controller for Firmware Update .

<!-- image -->

8. The AB\_SNMP – BOOTP Server Running dialog box may take several seconds or minutes to appear.

<!-- image -->

You may need to wait several seconds before you are returned to the AB\_SNMP.DLL – Enter IP Address dialog box. Within several seconds, the Device Identification box displays the processor's current revision information.

9. Select OK.
10. Select the appropriate firmware revision according to the controller series that is to be upgraded from the dialog box and select Next.

<!-- image -->

<!-- image -->

The Summary dialog box displays.

<!-- image -->

11. Select Finish.

The ControlFLASH dialog box displays.

<!-- image -->

12. Select Yes if the firmware revision matches the controller series.

A ControlFLASH warning displays for MicroLogix 1400 Series B controllers only.

<!-- image -->

A ControlFLASH warning displays for MicroLogix 1400 Series C controllers only.

<!-- image -->

If your computer has multiple Ethernet interface installed, the following dialog box displays the assigned IP addresses of each of the listed Ethernet interfaces. Otherwise, go to step 16 .

<!-- image -->

13. Highlight the IP address of the PC Ethernet interface that connects to the Ethernet network hosting the target processor. and select OK.
14. You may need to wait several seconds before the Progress dialog box displays (a typical sequence is shown below). While the download is in progress, the RUN status indicator, FAULT status indicator and FORCE status indicator display a Walking Pattern (First RUN status indicator ON, then FAULT status indicator ON and then FORCE status indicator ON in sequence). When the updating starts, the POWER status indicator and the FORCE status indicator stay solid ON.

## Stage 1

The concurrent ControlFLASH and LCD displays during the Firmware download are shown here.

A BOOT screen displays:

<!-- image -->

Stage 2

<!-- image -->

## Stage 3

<!-- image -->

The BOOT screen displays:

<!-- image -->

The Run, Fault, and Force status indicators display a walking Pattern.

<!-- image -->

The BOOT screen displays:

<!-- image -->

At this stage, the Power and Force status indicators are solid ON. After updating the controller, the BOOT screen displays:

<!-- image -->

15. After the controller update is complete, a dialog box prompts you to wait for the controller to reset, verify that the POWER status indicator is steady green, and verify the FAULT status indicator is turned OFF.
16. Select OK.
17. Enter the hardware address if prompted. Otherwise, the AB\_SNMP – BOOTP Server Running dialog box may appear.

<!-- image -->

<!-- image -->

<!-- image -->

If the AB\_SNMP – BOOTP Server Running dialog box appears and if there is no response from the controller for more than 30 seconds, select Cancel.

The Update Status dialog box displays. If the update was successful, the status text box is green and has an appropriate message.

<!-- image -->

## ControlFLASH Error Messages

If the update was not successful, the status text box is red and has an appropriate message.

<!-- image -->

If the following dialog box appears, it indicates that the controller ended up in a Missing/ Corrupt OS state. The current revision number reflects the version of Boot Firmware. To recover the controller from this state, see Recover from Missing or Corrupt OS State .

<!-- image -->

18. Select OK. The Welcome to ControlFLASH dialog box displays.
19. To continue to upgrade additional controllers, select Next or select Cancel to exit the program.

<!-- image -->

If you select cancel, you are prompted to verify that you want to end the update session.

<!-- image -->

The following are error messages that you can receive.

- Invalid Catalog Number
- Target Module Not in Proper State for Programming
- Failed to Receive Initial TFTP Request from Target
- Communication error during TFTP transfer

## Invalid Catalog Number

<!-- image -->

The error message displays if the ControlFLASH tool is unable to match the processor to the catalog number that was selected in the Catalog Number dialog box.

To clear this error:

1. Select OK. The Catalog Number dialog box appears.
2. Select the correct catalog number in the dialog box, and proceed with the update.
3. Restart the firmware update procedure as described in the section Use ControlFLASH for Firmware Update .

Target Module Not in Proper State for Programming

<!-- image -->

This error message displays when the target module is not in a proper state for programming.

## To clear this error:

1. Put the controller in the PROGRAM mode.
2. Restart the firmware update procedure as described in the section Use ControlFLASH for Firmware Update. If the error occurs again, cycle power and restart the firmware upgrade process.

Failed to Receive Initial TFTP Request from Target

<!-- image -->

This error message displays when the initial TFTP request is not received.

## To clear this error:

1. Connect the controller Ethernet directly to the computer Ethernet port using a crossover cable, or disable or uninstall any firewall VPN or virus protection software running on the computer.
2. Cycle power to the processor.
3. Restart the firmware update procedure as described in the section Use ControlFLASH for Firmware Update .

Communication error during TFTP transfer

<!-- image -->

This error message displays when there is a communication error during TFTP transfer.

## Missing or Corrupt OS state

To clear this error:

1. Check that your Ethernet connections are intact.
2. Cycle power to the processor.
3. Restart the firmware update procedure as described in the section Use ControlFLASH for Firmware Update
4. If the error still persists, connect the controller Ethernet directly to the computer Ethernet port using a crossover cable, and then repeat from step 2 .

The Boot Firmware runs the controller in this state.

<!-- image -->

ATTENTION: Do not interrupt the update procedure, once you have begun to download the firmware. If the update procedure is interrupted, the controller is in a Missing or Corrupt OS state on the next power-up.

When the controller is in this state, the controller shows either one of the following:

- The POWER status indicator is solid ON and the RUN, FAULT, and FORCE status indicators are blinking simultaneously. The BOOT screen displays:
- The POWER and FAULT status indicators are solid ON and the BOOT screen displays:

1766-LEC BOOT FRN: 21. 00

ready. .

1766-LEC BOOT FRN: 21. 00 Fpga Corrupt

When the LCD displays the Fpga Corrupt information, the status indicators do not show the Walking pattern during the firmware update process.

## Recover from Missing or Corrupt OS State

To recover from this controller state, you must restart the operating system firmware update as follows:

1. Ensure that the Ethernet connections are intact. SNMP is enabled by default in the controller.
2. If the IP address was configured during the Preparing for firmware update stage, the same IP configuration is retained in the controller.
3. Start the firmware update as explained in Use ControlFLASH for Firmware Update .

## RS-232 Communication Interface

## RS-485 Communication Interface

## DF1 Full-duplex Protocol

<!-- image -->

## Connect to Networks Via RS-232/RS-485 Interface

The following protocols are supported from the RS-232/RS-485 combination communication channel (Channel 0) and the RS-232 communication channel (Channel 2):

- DF1 full-duplex
- DF1 Half-duplex master/slave
- DF1 Radio Modem
- DH-485
- Modbus RTU master/slave
- ASCII
- DNP3 slave

The communications port on Channel 0 of the MicroLogix 1400 controller uses a combined, isolated RS-232/RS-485 interface. RS-232 and RS-485 are Electronics Industries Association (EIA) standards that specify the electrical and mechanical characteristics for serial binary communication. They provide various system configuration possibilities (RS-232 and RS-485 define electrical connection characteristics, not protocols).

The MicroLogix 1400 controller supports an additional, non-isolated RS-232 interface on Channel 2. One of the biggest benefits of an RS-232 interface is that it lets you integrate telephone and radio modems into your control system (using the appropriate DF1 protocol only, not the DH-485 protocol), but it is for point-to-point connections only between two devices.

The RS-485 interface supports connection of devices in a multi-drop hard-wired configuration using DH-485, DF1-Half Duplex, Modbus, or DNP3 protocols. Also, the RS-485 interface supports connection in a multi-drop hard-wired configuration using ASCII protocols.

The DF1 full-duplex protocol provides a point-to-point connection between two devices. DF1 fullduplex protocol combines data transparency (American National Standards Institute ANSI – X3.281976 specification subcategory D1) and 2-way simultaneous transmission with embedded responses (subcategory F1).

The MicroLogix controller supports the DF1 full-duplex protocol via RS-232 connection to external devices, such as computers, or other controllers that support DF1 full-duplex.

DF1 is an open protocol. See DF1 Protocol and Command Set Reference Manual, publication 1770-RM516, for more information.

DF1 full-duplex protocol (also referred to as DF1 point-to-point protocol) is useful where RS-232 point-to-point communication is required. The DF1 protocol controls message flow, detects and signals errors, and retries if errors are detected.

## Example DF1 Full-duplex Connections

For information on equipment required for network connection, see Communication Connections .

## DF1 Half-duplex Protocol

<!-- image -->

DF1 Half-duplex protocol is a multi-drop single master/multiple slave network. DF1 half-duplex protocol supports data transparency (American National Standards Institute ANSI – X3.28-1976 specification subcategory D1). In contrast to DF1 full-duplex, communication takes place in one direction at a time. You can use the RS-232/RS-485 port on the MicroLogix as both a half-duplex programming port and a Half-duplex peer-to-peer messaging port.

## DF1 Half-duplex Operation

A DF1 half-duplex master device initiates all communication by polling each slave device. The slave device can only transmit when it is polled by the master. It is the master's responsibility to poll each slave on a regular and sequential basis to allow slave devices an opportunity to communicate.

An additional feature of the DF1 Half-duplex protocol is that it is possible for a slave device to enable an MSG write or read to/from another slave. When the initiating slave is polled, the MSG is sent to the master. The master recognizes that the message is not intended for it, but for another slave, so the master immediately forwards the message to the intended slave. The master forwards the message automatically; you do not need to program the master to move data between slave nodes. The slave-to-slave transfer can also be used by programming software to allow slave-to-slave upload and download of programs to processors (including the master) on the DF1 half-duplex link.

A MicroLogix 1400 controller can act as the master or as a slave on a Half-duplex network. When the MicroLogix 1400 controller is a slave device, a master device is required to run the network. Several other Allen-Bradley products support the DF1 Half-duplex master protocol. They include the SLC 5/03 and higher processors, enhanced PLC-5 processors, MicroLogix 1200 or MicroLogix 1500 controller, and RSLinx software (version 2.x and higher).

DF1 half-duplex supports up to 255 devices (address 0…254) with address 255 reserved for master broadcasts. As a DF1 half-duplex slave device, the MicroLogix supports broadcast reception. As a DF1 half-duplex master, the MicroLogix 1400 controller supports both the reception and initiation of broadcast write commands (via the MSG instruction). The MicroLogix also supports Half-duplex modems using RTS/CTS hardware handshaking.

<!-- image -->

## Considerations When Communicating as a DF1 Slave on a Multi-drop Link

When communication is between either your programming software and a MicroLogix controller or between two MicroLogix 1400 controllers via slave-to-slave communication on a larger multi-drop link, the devices depend on a DF1 half-duplex master to give each of them access in a timely manner. As the number of slave devices increases, the time between when slave devices are polled also increases. The increase in time could also be large if you are using low communication rate. As these time periods grow, consider increasing the poll timeout and reply timeout values for slave devices.

## IMPORTANT

If a program download is started when using DF1 half-duplex, but then is interrupted due to electromagnetic interference or other events, discontinue communications to the controller for the ownership timeout period and then restart the program download. The ownership timeout period is 60 s. After the timeout, you can re-establish communications with the processor and try the program download again. The only other way to remove program ownership is to cycle power on the processor.

## Using Modems with MicroLogix Programmable Controllers

The types of modems you can use with MicroLogix controllers include the following:

- Dial-up phone modems.

A MicroLogix controller, on the receiving end of the dial-up connection, can be configured for the DF1 full-duplex protocol with or without handshaking. The modem connected to the MicroLogix controller must support auto-answer. The MicroLogix 1400 controller supports ASCII out communications. Therefore, it can cause a modem to initiate or disconnect a phone call.

- Leased-line modems.

Leased-line modems are used with dedicated phone lines that are typically leased from the local phone company. The dedicated lines can be in a point-to-point topology to support full-duplex communications between two modems or in a multi-drop topology to support

- half-duplex communications between three or more modems.
- Radio modems.

Radio modems can be implemented in a point-to-point topology to support either halfduplex or full-duplex communications, or in a multi-drop topology to support half-duplex communications between three or more modems. The MicroLogix 1400 controller also supports the DF1 Radio Modem protocol.

## DH-485 Communication Protocol

- Line drivers.

Line drivers, also called short-haul modems, do not actually modulate the serial data, but rather condition the electrical signals to operate reliably over long transmission distances (up to several miles). Line drivers are available in full-duplex and half-duplex models. AllenBradley's AIC+ Advanced Interface Converter is a half-duplex line driver that converts an RS-232 electrical signal into an RS-485 electrical signal, increasing the signal transmission distance from 50…4000 ft (8000 ft when bridged).

For point-to-point full-duplex modem connections that do not require any modem handshaking signals to operate, use the DF1 full-duplex protocol with no handshaking. For point-to-point fullduplex protocol with handshaking.

For radio modem connections, use the DF1 Radio Modem protocol, especially if store and forward capability is required.

For general multi-drop modem connections, or for point-to-point modem connections that require RTS/CTS handshaking, use the DF1 half-duplex master protocol.

## IMPORTANT

Never attempt to use the DH-485 protocol through modems under any circumstance.

<!-- image -->

All MicroLogix controllers support RTS/CTS modem handshaking when configured for DF1 full-duplex protocol with the control line parameter set to full-duplex Modem Handshaking or DF1 half-duplex slave protocol with the control line parameter set to half-duplex Modem.

MicroLogix 1400 controllers also support Data Carrier Detect (DCD) line for the DF1 Radio Modem protocol. For other protocols, you can only access the DCD signal from your ladder logic. MicroLogix 1400 controllers do not support any other modem handshaking lines (such as Data-Set™ Ready and Data Terminal Ready).

The DH-485 protocol defines the communication between multiple devices that coexist on a single pair of wires. DH-485 protocol uses RS-485 half-duplex as its physical interface – RS-485 is a definition of electrical characteristics; it is not a protocol. RS-485 uses devices that can coexisting on a common data circuit, thus allowing data to be easily shared between devices.

The DH-485 network offers:

- Interconnection of 32 devices
- Multi-master (peer-to-peer) capability
- Token-passing access control
- The ability to add or remove nodes without disrupting the network
- Maximum network segment of 1219 m (4000 ft.)

The DH-485 protocol supports two classes of devices: initiators and responders. All initiators on the network get a chance to initiate message transfers. To determine which initiator has the right to transmit, a token-passing algorithm is used.

Control of message transfers on the DH-485 network is performed by rotating the token along the nodes on the network. A node holding the token can send a message onto the network. Each node is allowed a fixed number of transmissions (based on the Token Hold Factor) each time it receives the token. After a node sends a message, it passes the token to the next device.

The allowable range of node addresses is 1…31. There must be at least one initiator on the network, such as a MicroLogix controller, or an SLC 5/02 or later processor.

## DH-485 Configuration Parameters

When MicroLogix communications are configured for DH-485, the following parameters can be changed:

Table 23 - Devices that Support a DH-45 Network

| Catalog Number Description Installation Function Publication                                                                       |                                                    |                                                                                                                                                                                                    |                                  |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
|                                                                                                                                    |                                                    | Bulletin 1762 MicroLogix 1200 Series A or later These controllers support DH-485 communications.                                                                                                   | 1762-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1763 MicroLogix 1100 Series A or later These controllers support DH-485 communications.                                                                                                   | 1763-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1747 Processors SLC 500 Processors SLC™ Chassis These processors support various I/O requirements and functionality.                                                                      | 1747-UM011                       |
|                                                                                                                                    | 1746-BAS BASIC Module SLC Chassis                  | Provides an interface for SLC 500 devices to foreign devices. Program in BASIC to interface the 3 channels (2 RS-232 and 1 DH-485) to printers, modems, or the DH-485 network for data collection. | 1746-UM004 1746-PM001 1746-RM001 |
|                                                                                                                                    |                                                    | 1784-PKTX, 1784-PKTXD PC DH-485 IM PCI Computer bus Provides DH-485 using RSLinx.                                                                                                                  | 1784-UM522                       |
| 1784-PCMK PCMCIA IM                                                                                                                |                                                    | PCMCIA slot in computer  Provides DH-485 using RSLinx.                                                                                                                                             | 1784-UM519                       |
| 2711-K5A2, 2711-B5A2, 2711-K5A5, 2711-B5A5, 2711-K5A1, 2711-B5A1, 2711-K9A2, 2711-T9A2, 2711-K9A5, 2711-T9A5, 2711-K9A1, 2711-T9A1 | PanelView 550 and PanelView 900 Operator Terminals | Panel Mount Provides an electronic operator interface for SLC 500 processors.                                                                                                                      | 2711-UM014                       |

## Important DH-485 Network Planning Considerations

Carefully plan your network configuration before installing any hardware. Some of the factors that can affect system performance are:

- amount of electrical noise, temperature, and humidity in the network environment.
- number of devices on the network.
- connection and grounding quality in installation.
- amount of communication traffic on the network.
- type of process being controlled.
- network configuration.

The major hardware and software issues you must resolve before installing a network are discussed in the following sections.

## Hardware Considerations

You must decide the length of the communication cable, where you route it, and how to protect it from the environment where it is installed.

When the communication cable is installed, you must know how many devices are to be connected during installation and how many devices can be added in the future. The following sections help you understand and plan the network.

Number of Devices and Length of Communication Cable

The maximum length of the communication cable is 1219 m (4000 ft). This is the total cable distance from the first node to the last node in a segment. However, two segments can be used to extend

Table 22 - DF1 Full-duplex Configuration Parameters

| Parameter Options              |
|--------------------------------|
| Communication rate 9600, 19.2K |
| Node Address 1…31 decimal      |
| Token Hold Factor 1…4          |

See Software Considerations on page 174 for tips on setting the parameters listed in Table 22 .

## Devices that use the DH-485 Network

In addition to the MicroLogix controllers, the devices that are shown in Table 23 also support the DH-485 network.

the DH-485 network to 2438 m (8000 ft.). For additional information on connections using the AIC+, see Advanced Interface Converter DeviceNet Interface Installation Instructions, publication 1761IN002 .

## Planning Cable Routes

Follow these guidelines to help protect the communication cable from electrical interference:

- Keep the communication cable at least 1.52 m (5 ft.) from any electric motors, transformers, rectifiers, generators, arc welders, induction furnaces, or sources of microwave radiation.
- If you must run the cable across power feed lines, run the cable at right angles to the lines.
- If you do not run the cable through a contiguous metallic wireway or conduit, keep the communication cable at least 0.15 m (6 in.) from AC power lines of less than 20 A, 0.30 m (1 ft.) from lines greater than 20 A, but only up to 100K VA, and 0.60 m (2 ft.) from lines of 100K VA or more.
- If you run the cable through a contiguous metallic wireway or conduit, keep the communication cable at least 0.08 m (3 in.) from AC power lines of less than 20 A, 0.15 m (6 in.) from lines greater than 20 A, but only up to 100K VA, and 0.30 m (1 ft.) from lines of 100 K VA or more.

Run the communication cable through a conduit to provide extra protection from physical damage and electrical interference. If you route the cable through a conduit, follow these additional recommendations:

- Use ferromagnetic conduits near critical sources of electrical interference. You can use aluminum conduit in non-critical areas.
- Use plastic connectors to couple between aluminum and ferromagnetic conduit. Make an electrical connection around the plastic connector (use pipe clamps and the heavy gauge wire or wire braid) to hold both sections at the same potential.
- Ground the entire length of conduit by attaching it to the building earth ground.
- Do not let the conduit touch the plug on the cable.
- Arrange the cables loosely within the conduit. The conduit should contain only serial communication cables.
- Install the conduit so that it meets all applicable codes and environmental specifications.

For more information on planning cable routes, see Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

## Software Considerations

Software considerations include the configuration of the network and the parameters that can be set to the specific requirements of the network. The following are major configuration factors that have a significant effect on network performance:

- number of nodes on the network
- addresses of those nodes
- Communication rate

The following sections explain network considerations and describe ways to select parameters for optimum network performance (speed). See your programming software's user manual for more information.

## Number of Nodes

The number of nodes on the network directly affects the data transfer time between nodes. Unnecessary nodes (such as a second programming terminal that is not being used) slow the data transfer rate. The maximum number of nodes on the network is 32.

## Setting Node Addresses

The best network performance occurs when node addresses are assigned in sequential order. Assign initiators, such as computers, the lowest numbered addresses to minimize the time time

that is required to initialize the network. The valid range for the MicroLogix controllers is 1...31 (controllers cannot be node 0). The default setting is 1. The node address is stored in the controller Communications Status file (CS0:5/0…CS0:5/7).

## Setting Controller Communication Rate

The best network performance occurs at the highest communication rate, which is 19,200. 19,200 is the default communication rate for a MicroLogix device on the DH-485 network. All devices must be at the same communication rate. The rate is stored in the controller Communications Status file (CS0:5/8…CS0:5/15).

## Setting Maximum Node Address

Once you have an established a network set-up and are confident that you are not adding more devices, you can enhance performance by adjusting the maximum node address of your controllers. Set it to the highest node address being used.

## IMPORTANT

Set all devices to the same maximum node address.

## MicroLogix Remote Packet Support

MicroLogix controllers can respond and initiate with communications (or commands) that do not originate on the local DH-485 network. This is useful in installations where communication is needed between DH-485 and Data Highway Plus™ (DH+™) networks.

The example below shows how to send messages from a device on the DH+ network to a MicroLogix controller on the DH-485 network. This method uses an SLC 5/04 processor as the bridge connection.

## When using the method shown in Figure 75:

- PLC-5 devices can send read and write commands to MicroLogix controllers.
- MicroLogix controllers can respond to MSG instructions received.
- The MicroLogix controllers can initiate MSG instructions to devices on the DH+ network.
- The PC can send read and write commands to MicroLogix controllers.
- The PC can do remote programming of MicroLogix controllers.

<!-- image -->

Use a 1763-NC01 Series A or later cable to connect a MicroLogix 1400 controller to a DH-485 network.

You can connect a MicroLogix 1400 controller to your DH-485 network directly without using an RS-232 to RS-485 converter and optical isolator, such as the AIC+, catalog number 1761-NET-AIC, as shown in Figure 75, because Channel 0 has isolation and RS485 built-in.

Figure 75 - MicroLogix 1400 Controller in a DH-485 Network

<!-- image -->

## Example DH-485 Connections

The following network diagrams provide examples of how to connect MicroLogix controllers to the DH-485 network. You can connect a MicroLogix 1400 controller to your DH-485 network directly without using an RS-232 to RS-485 converter and optical isolator, such as the Advanced Interface Converter (AIC+), catalog number 1761-NET-AIC, as shown in Figure 76, because Channel 0 has isolation and RS-485 built-in.

However, you can use an AIC+ to connect Channel 2 of the MicroLogix 1400 controller to a DH-485 network.

Figure 76 - DH-485 Network with a MicroLogix Controller

<!-- image -->

<!-- image -->

This 3-node network is not expandable.

## Modbus Communication Protocol

## ASCII

## Distributed Network Protocol (DNP3)

Modbus is a Half-duplex, master-slave communications protocol. The Modbus network master reads and writes coils and registers. The Modbus protocol allows a single master to communicate with a maximum of 247 slave devices. MicroLogix 1400 controllers support Modbus RTU master and Modbus RTU slave protocol.

For more information on how to configure your MicroLogix 1400 controller for Modbus protocol, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001. For more information about the Modbus protocol, see the Modbus Protocol Specifications (available from https://www.modbus.org).

ASCII provides connection to other ASCII devices, such as barcode readers, weigh scales, serial printers, and other intelligent devices.

You can use ASCII by configuring the RS-232/RS-485 port, Channel 0 and the RS-232 port, Channel 2 for the ASCII driver. For detailed configuration information, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

For more information on how to configure your MicroLogix 1400 controller for Distributed Network Protocol, see Channel Configuration for DNP3 Slave. For more information about the Distributed Network Protocol, see the Distributed Network Protocol Specifications, available from https://www.dnp.org .

Disable Serial Channels 0 and 2 In RSLogix 500 software, you can disable Serial Channels 0 and/or 2 to enhance security.

1. Open the Channel Configuration in the MicroLogix 1400 project tree and select a channel.
2. From the Driver dropdown list, select Shutdown.
3. Select Apply and O100K.

<!-- image -->

The selected serial channels are disabled.

## IMPORTANT

At least 1 of the 3 channels must be active to enable communication with the RSLogix 500 software. You cannot disable the last serial channel if the other 2 channels (Serial, Ethernet) are already configured as disabled.

## Channel Configuration for DNP3 Slave

<!-- image -->

## MicroLogix 1400 Distributed Network Protocol

The default communication protocol for the serial ports Channel 0 and Channel 2 in the MicroLogix 1400 controller is DF1 full-duplex. To communicate with Distributed Network Protocol (DNP3), the channel must be configured for the DNP3 protocol.

The default communication protocol for the Ethernet Channel 1 in the controller is EtherNet/IP. To communicate with DNP3 over IP protocol in the MicroLogix 1400 Series B and Series C controller, the channel must be configured to use the DNP3 protocol.

The MicroLogix 1400 Series A controller supports DNP3 protocol via Channel 0 and/or Channel 2 Serial ports.

The MicroLogix 1400 Series B and Series C controller also supports DNP3 over IP protocol via Channel 1 Ethernet port.

To program the controller, use RSLogix 500/RSLogix Micro software, version 8.10.00 or later for Series A controller and version 8.30.00 or later for Series B and Series C controllers, and version 11.

In RSLogix 500/RSLogix Micro, open Channel Configuration in the MicroLogix 1400 controller project tree.

<!-- image -->

There are four configurations that are related to the DNP3 protocol in RSLogix 500/RSLogix Micro software:

- Channel 0 configuration
- Channel 2 configuration
- Channel 1 configuration
- DNP3 Slave Application Layer configuration.

## Channel 0 and Channel 2 Link Layer Configuration

Link Layer related configuration can be done in the Channel 0 and/or Channel 2 tab.

<!-- image -->

## Channel 1 Link Layer Configuration

In RSLogix 500/RSLogix Micro, open Channel Configuration in the MicroLogix 1400 Series B and Series C controller project tree.

To enable DNP3 over IP protocol, check DNP3 over IP Enable in the Channel 1 configuration.

Unlike the serial port configuration, you must cycle power to the controller after you download the Ethernet port configuration to enable the DNP3 over IP feature.

Link Layer related configuration can also be done in the Chan. 1 – DNP3 tab.

<!-- image -->

DNP3 Slave Application Layer Configuration

<!-- image -->

Application Layer related configuration can be done in the DNP3 Slave tab.

For MicroLogix 1400 Series A controllers, you can see the tabs shown in Figure 77 .

Figure 77 - MicroLogix 1400 Series A Controller Tabs

<!-- image -->

If you want to communicate with the DNP3 protocol using Channel 0 port, set both Channel 0 and DNP3 slave configurations. If you want to communicate with the DNP3 protocol using Channel 2 port, set Channel 2 and DNP3 slave configurations.

If you want to communicate with the DNP3 protocol using both Channel 0 port and Channel 2 port, Channel 0, set Channel 2 and DNP3 slave configurations.

In this case, the channel that is directed in the DNP3 slave configuration supports full functionality. But, the other port supports limited functionality and it does not support some features like Unsolicited Response.

Channel 0 and Channel 2 ports share the DNP3 slave configuration if the channels are both are configured to the DNP3 protocol. Any changes in the the DNP3 Slave configuration tab affects both channels.

For the MicroLogix 1400 Series B and Series C controllers, you can see the tabs shown in Figure 78 .

Figure 78 - MicroLogix 1400 Series B and Series C Controller Tabs

<!-- image -->

Channel 0, Channel 1, and Channel 2 ports share the DNP3 slave configuration if the three channels are configured for the DNP3 protocol. Any changes in the DNP3 Slave configuration tab affects all channels.

## Channel 0 and Channel 2 Link Layer Configuration Parameters

Driver

Set his selection to DNP3 Slave to communicate with the DNP3 protocol.

Node Address

This value is a node address of this DNP3 Slave. The valid range is 0…65519. Default value is 1.

Baud

The selections can be 38.4K, 19200, 9600, 4800, 2400, 1200, 600, and 300. Default selection is 19200.

Parity

The selections can be NONE, EVEN, and ODD. Default selection is NONE.

Stop Bits

The selections can be 1, 1.5, and 2. Default selection is 1.

Enable Master Address Validation

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the controller accepts the requests from any DNP3 master.

When the selection is Enabled (Checked), the controller accepts the requests only from the DNP3 master that is configured in the Master Node0…Master Node4. The maximum number of master node Addresses for the Master Address Validation is 5.

## Enable Self-Address

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When this bit is Disabled (Unchecked), any packets that contain the destination address 65532(FFFCh) are ignored.

When this bit is Enabled (Checked), any packets that contain the destination address 65532(FFFCh) are accepted and processed.

## Master Node0

This value is used to:

- Validate the Master node address when the Enable Master Address Validation is Enabled (Checked)
- Send Unsolicited Response when Unsolicited Response functionality is enabled. An Unsolicited Response is sent out to the DNP3 Master having this address.

The valid range is 0…65519. Default value is 0.

Master Node1, Master Node2, Master Node3, Master Node4

The valid range is 0…65519. Default value is 0.

This value is used to check validation for Master node address when Enable Master Address Validation is Enabled (Checked).

Control

For Channel 0, the selections can be No Handshaking, half-duplex Modem (CTS/RTS handshaking) and No Handshaking (DH-485 Network).

Default selection is No Handshaking.

For Channel 2, the selections can be No Handshaking, and half-duplex Modem (CTS/RTS handshaking).

Default selection is No Handshaking.

When the controller is connected to DNP3 Master using the RS-232 line directly, you must select No Handshaking. If you want to use the Modem line in a half-duplex network, you must select halfduplex Modem (CTS/RTS handshaking). If the controller is connected to an RS-485 network and a 1763-NC01 cable is used, you must select No Handshaking (DH-485 Network).

If you want to send an ASCII string via a serial channel that is configured to the DNP3 slave protocol, use AWA and AWT instructions to control the Modem.

For Cabling and Connections, seeCommunication Connections .

For AWA and AWT instructions, see MicroLogix 1400 Programmable Controllers Reference Manual, 1766-RM001 .

Request LL Confirmation

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), Primary Frames from the controller are sent out with the function code FC\_UNCONFIRMED\_USER\_DATA (4).

When the selection is Enabled (Checked), Primary Frames from the controller are sent out with the function code FC\_CONFIRMED\_USER\_DATA (3). In this case, the controller waits for the confirmation and retries the Frame if it did not receive the confirmation from DNP3 Master within the time Confirmation Timeout (x1 ms).

Send LL Confirmation

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the optional Secondary Frame is not sent out with the function code FC\_NACK (1) or FC\_NOT\_SUPPORTED (15).

When the selection is Enabled (Checked), the optional Secondary Frame is sent out with the function code FC\_NACK (1) or FC\_NOT\_SUPPORTED (15).

Confirmation Timeout (x20 ms)

When Request LL Confirmation is enabled, the controller waits to receive a confirmation frame until this timeout has expired.

The valid range is 1…65535. Default value is 1.

Message Retries

When Confirmation Timeout (x1 ms) has expired and this parameter was nonzero value, the controller tries to send retry packets.

The valid range is 0…255. Default value is 0.

Pre-transmit Delay (x1 ms)

The controller waits for the specified time before sending the packet.

The valid range is 0…65535. Default value is 0.

RTS Off Delay (x20 ms)

When the Control is set at half-duplex Modem (CTS/RTS handshaking), this feature is enabled. This specifies a time delay between the end of a transmission and the RTS signal drop.

The valid range is 0…65535. Default value is 0.

RTS Send Delay (x20 ms)

When the Control is set at half-duplex Modem (CTS/RTS handshaking), this entry is enabled. This specifies a time delay between the raising of the RTS and the initiation of a transmission.

The valid range is 0…65535. Default value is 0.

Max Random Delay (x1 ms)

This parameter is used with Pre-transmit Delay (x1 ms) for Collision Avoidance on the RS-485 network. For more details, see Collision Avoidance on page 241 .

The valid range is 0…65535. Default value is 0.

Table 24 - Endpoint Types

| Endpoint Type Connection Description   |                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Listening endpoint                     | A single TCP server connection | Any of the requests are accepted and the responses are transmitted via this connection. The unsolicited responses are transmitted via this connection when this connection is available.                                                                                                                                                                                                                                                                                                                                                         |
| Listening endpoint                     | UDP datagram                   | Accepts only broadcast packets when the DNP3 destination node is one of 0xFFFD, 0xFFFE, and 0xFFFF in the request.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Dual endpoint                          | A single TCP server connection | Any of the requests are accepted and the responses are transmitted via this connection. The unsolicited responses are transmitted via this connection when this connection is available. This connection has a higher priority than the Client connection.                                                                                                                                                                                                                                                                                       |
| Dual endpoint                          | A single TCP client connection | Any of the requests are accepted and the responses are transmitted via this connection. The unsolicited responses are transmitted via this connection when this connection is available. The controller does not request a TCP client connection to DNP3 Master until an unsolicited response is generated.                                                                                                                                                                                                                                      |
| Dual endpoint                          | UDP datagram                   | Accepts only broadcast packets when the DNP3 destination node is one of 0xFFFD, 0xFFFE, and 0xFFFF in the request.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Datagram endpoint UDP datagram only    |                                | Any of the requests are accepted and the responses are transmitted via this connection. All responses can be transmitted to the different DNP3 master port according to the configuration of the parameters Remote UDP Port Number and Master IP Address0. If this parameter is not set to 0, the solicited responses are sent to the DNP3 master port that is configured. If this parameter is set to 0, the solicited responses are sent to the DNP3 master port that sent the request. TCP connection is not available in this configuration. |

The parameter DNP3 over IP Enable is configured in the Channel 1 tab and other parameters are configured in the Chan. 1 – DNP3 tab.

## DNP3 over IP Enable

The valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked). You must power cycle for the changes to take effect.

When the selection is Disabled (Unchecked), DNP3 service over Ethernet is disabled after powercycle.

When the selection is Enabled (Checked), DNP3 service over Ethernet is enabled after the powercycle.

Enable Master Address Validation

The valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

## Channel 1 (Ethernet) Link Layer Configuration Parameters

This section is only applicable for MicroLogix 1400 Series B and Series C controllers.

The DNP3 over IP subsystem in the controller supports Listening endpoint, TCP dual endpoint, and Datagram endpoint type.

Listening endpoint type supports a single TCP connection as a server and UDP datagram.

TCP dual endpoint type supports a single TCP connection as a server, a single TCP connection as a Client and a UDP datagram.

Datagram endpoint type supports UDP datagram from DNP3 masters. The default TCP and UDP port numbers are 20000 and the port numbers are configurable.

You can determine the endpoint type by the parameter endpoint type. According to the parameter, the controller works as different endpoint types. See Table 24 for each configuration.

When the selection is Disabled (Unchecked), the controller accepts the requests from any DNP3 Master.

When the selection is Enabled (Checked), the controller accepts the requests only from the DNP3 Master Node Address that is configured in the parameters Master Node0, and Master Node1, Master Node2, Master Node3, Master Node4. The maximum number of Master Node Address Validation is 5.

## Enable Self-Address

The valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When this bit is Disabled (Unchecked), any packets that contain the destination address 65532 (FFFCh) are ignored.

When this bit is Enabled (Checked), any packets that contain the destination address 65532 (FFFCh) are accepted and processed.

## Enable Access Control

The valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the controller accepts the requests from any DNP3 Master.

When the selection is Enabled (Checked), the controller accepts the requests only from the DNP3 master IP address which is configured in the parameters Master IP Address0 to Master IP Address4. The maximum number of Master IP Address for the Access Control is 5.

End endpoint Type

The valid selections are Listening, Dual, and Datagram Only.

Default is Listening end endpoint Type.

Master Node0

## This value is used to:

- Validate Master node address when the Enable Master Address Validation is Enabled (Checked)
- Send Unsolicited Response when Unsolicited Response functionality is enabled. An Unsolicited Response is sent out to the DNP3 Master having this address.

The valid range is 0…65519. Default value is 0.

Master Node1, Master Node2, Master Node3, Master Node4

This value is used for validation of the Master node address when the Enable Master Address Validation is Enabled (Checked). This value is only valid when the Enable Master Address Validation is Enabled (Checked).

The valid range is 0…65519. Default value is 0.

Master IP Address0

This value is used to:

- Validate Master IP address when the Enable Access Control is Enabled (Checked)
- Send Unsolicited Response when Unsolicited Response functionality is enabled. An Unsolicited Response is sent out to the DNP3 Master having this address.

The valid value is an IP address. Default value is 0.0.0.0.

Master IP Address1, Master IP Address2, Master IP Address3, Master IP Address4

This value is used for validation of the Master IP address when the Enable Access Control is Enabled (Checked). This value is only valid when the Enable Access Control is Enabled (Checked).

The valid value is an IP address. Default value is 0.0.0.0.

Remote TCP Port Number

This value is used to configure the Master TCP Port Number for Unsolicited Response.

The valid range is 0…65535. Default value is 20000.

Remote UDP Port Number for Initial Unsolicited

This value is used to configure the Master UDP Port Number for Initial Unsolicited Response if the parameter End endpoint Type is selected as Datagram Only.

The valid range is 0…65535. Default value is 20000.

Remote UDP Port Number

This value is used to configure Master UDP Port Number if the parameter End Endpoint Type is selected as Datagram Only.

The valid range is 0…65535. Default value is 20000.

Keep Alive Interval (x1 s)

This parameter specifies a time interval for the TCP Keep Alive mechanism.

If the timer times out, the controller transmits a keep-alive message. The keep-alive message is a DNP Data Link Layer status request (FC\_REQUEST\_LINK\_STATUS). If a response is not received to the keep-alive message, the controller deems the TCP connection to be broken and closes the TCP connection.

The valid range is 1…65535. Default value is 10.

Slave Node Address

This value is a node address of this DNP3 Slave.

The valid range is 0…65519. Default value is 1.

Local TCP Port Number

This value is used to configure the Local TCP Port Number that is used for TCP socket listening.

The valid range is 0…65535. Default value is 20000.

Local UDP Port Number

This value is used to configure the Local UDP Port Number that is used for UDP socket listening.

The valid range is 0…65535. Default value is 20000.

Diagnostic File Number

The diagnostic file number is used to store the diagnostics for the troubleshooting of the DNP3 Ethernet subsystem. The status of the DNP3 TCP and UDP subsystem is stored to this data file.

The value of this parameter is N file only. Valid range is 0, 7, 9…255. Default value is 0.

See Diagnostics on page 247 .

## DNP3 Slave Application Layer Configuration Parameters

Channel for Unsolicited Response

Only channels that are already configured for the DNP3 protocol appear in the Channel for Unsolicited Response dropdown menu. All Unsolicited Responses are transmitted via this selected channel.

Channel 1 is only supported in MicroLogix 1400 Series B and Series C controllers.

Valid selections are Enabled (Checked) and Disabled (Unchecked), with disabled as the default value.

Restore Events After Power Cycle

When the selection is Disabled (Unchecked), DNP3 events that are generated before a power cycle are flushed after a power cycle. When the option is Enabled (Checked), all DNP3 events are restored after a power cycle.

## Enable Unsolicited On Start Up

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the controller does not send any enabled Unsolicited Responses after a restart until it has received a FC\_ENABLE\_UNSOLICITED (20) command from the DNP3 Master.

When the selection is Enabled (Checked), the controller sends any enabled Unsolicited Responses after a restart to the DNP3 master unconditionally.

Enable Unsolicited For Class1

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), Unsolicited Response is disabled for Class 1 events. To help prevent overflowing of the event buffer, the DNP3 master should poll for Class 1 events.

When the selection is Enabled (Checked), Unsolicited Response is enabled for Class 1 events.

Enable Unsolicited For Class2

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), Unsolicited Response is disabled for Class 2 events. To help prevent overflowing of the event buffer, the DNP3 master should poll for Class 2 events.

When the selection is Enabled (Checked), Unsolicited Response is enabled for Class 2 events.

Enable Unsolicited For Class3

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), Unsolicited Response is disabled for Class 3 events. To help prevent overflowing of the event buffer, the DNP3 master should poll for Class 3 events.

When the selection is Enabled (Checked), Unsolicited Response is enabled for Class 3 events.

Send Initial Unsolicited Null Response On Start Up

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the controller does not send an Unsolicited NULL Response with a RESTART IIN bit on startup.

When the selection is Enabled (Checked), the controller sends an Unsolicited NULL Response with a RESTART IIN bit on startup.

This selection is also used for sending the RESTART IIN bit during driver and channel configuration changes. See Internal Indications on page 202 for details.

## Enable Confirmation

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the controller sends Response packets with the CON bit set in its header under the following conditions only:

- When the response has Event data
- When the response is a multi-fragment response
- When the Unsolicited Response is sent

When the selection is Enabled (Checked), the controller always sends Response packets with the CON bit set in its header, which causes the DNP3 Master to send replies confirming that it received each Response packet without error.

Enable Time Synchronization On Start Up Only

Valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

This parameter is used with Time Synchronization Interval (x1 mins).

When the selection is Disabled (Unchecked), the controller sets the IIN1.4 bit on power-up and every interval that is configured in Time Synchronization Interval (x1 mins).

When the selection is Enabled (Checked), the controller only sets the NEED\_TIME Internal Indication bit (IIN1.4) upon startup.

Time Synchronization Interval (x1 mins)

This parameter is used with Enable Time Synchronization On Start Up Only. Only valid when Enable Time Synchronization On Start Up Only is Disabled (Unchecked).

The valid range is 0…32767. Default value is 0. As long as the parameter is set for greater than 0, the NEED\_TIME Internal Indication (IIN1.4) bit are set at startup and then after every Time Synchronization Interval minutes.

When the parameter Enable Time Synchronization On Start Up Only is Disabled (Unchecked) and the parameter Time Synchronization Interval (x1 mins) is configured to 0, the IIN1.4 bit is never turned on.

## Max Response Size

The controller sends an Application Layer frame to fit in Max Response Size. If the Response packet size is larger than this value, the controller fragments the Response packet.

The valid range is 27…2048 in bytes. Default value is 2048.

## Confirmation Timeout (x1 ms)

When Enable Confirmation is enabled, the controller waits for Application Layer Confirmation until the Confirmation Timeout (x1 ms) has expired.

The valid range is 100…65535 in 1 ms increments. Default value is 10000.

## Number of Retries

This parameter is only for Unsolicited Response. If this value has the maximum that is 65535, it means infinite retries of the Unsolicited Response.

The valid range is 0…65535. Default value is 0.

## Number of Class1 Events

If the controller is configured not to initiate an Unsolicited Response, this parameter is used to limit the maximum number of events that are generated and logged into the event buffer for Class 1 events. In this case, value 0 is disabled to generate the event.

If the controller is configured to generate an Unsolicited Response, and the number of queued Class 1 events is reached to this value, an Unsolicited Response is initiated.

The valid range is 0…6013 or 0…10000. See DNP3 10K Event Logging. Default value is 10.

Hold Time after Class1 Events (x1 s)

This parameter is only for Unsolicited Response. The controller holds the events during Hold Time after Class1 Events (x1 s) before initiating an Unsolicited Response.

The valid range is 0…65535. Default value is 5.

The value of 0 indicates that responses are not delayed due to this parameter.

Parameters Number of Class1 Events and Hold Time after Class1 Events (x1 s) are used together so that if either one of the criteria is met, an Unsolicited Response is transmitted.

By default, the Hold time is retriggered for each new event detected.

You can choose not to retrigger the hold timer for each new event that is detected by setting Status Bit S:36/12 to 1 before downloading to the controller. The default state of this Status Bit S:36/12 is 0.

## Number of Class2 Events

If the controller is configured not to initiate an Unsolicited Response, this parameter is used to limit the maximum number of events that are generated and logged into the event buffer for Class 2 events. In this case, value 0 is disabled to generate the event.

If the controller is configured to generate Unsolicited Response, and the number of queued Class 2 events is reached to this value, Unsolicited Response is initiated.

The valid range is 0…6013 or 0…10000.

See DNP3 10K Event Logging on page 237. Default value is 10.

Hold Time after Class2 Events (x1 s)

This parameter is only for Unsolicited Response. The controller holds the events during Hold Time after Class2 Events (x1 s) before initiating an Unsolicited Response.

The valid range is 0…65535. Default value is 5.

The value of 0 indicates that responses are not delayed due to this parameter.

Parameters Number of Class2 Events and Hold Time after Class2 Events (x1 s) are used together so that if either one of the criteria is met, an Unsolicited Response is transmitted.

By default, the Hold time is retriggered for each new event detected.

You can choose not to retrigger the hold timer for each new event that is detected by setting Status Bit S:36/12 to 1 before downloading to the controller. The default state of this Status Bit S:36/12 is 0.

## Number of Class3 Events

If the controller is configured not to initiate an Unsolicited Response, this parameter is used to limit the maximum number of events that are generated and logged into the event buffer for Class 3 events. In this case, value 0 is disabled to generate the event.

If the controller is configured to generate Unsolicited Response, and the number of queued Class 3 events is reached to this value, Unsolicited Response is initiated.

The valid range is 0…6013 or 0…10000. SeeDNP3 10K Event Logging on page 237. Default value is 10.

Hold Time after Class3 Events (x1 s)

This parameter is only for Unsolicited Response. The controller holds the events during Hold Time after Class3 Events (x1 s) before initiating an Unsolicited Response.

The valid range is 0…65535. Default value is 5.

The value of 0 indicates that responses are not delayed due to this parameter.

The Number of Class3 Events and Hold Time after Class3 Events (x1 s) parameters are used together so that if either one of the criteria is met, an Unsolicited Response is transmitted.

By default, the Hold time is retriggered for each new event detected.

You can choose not to retrigger the hold timer for each new event that is detected by setting Status Bit S:36/12 to 1 before downloading to the controller. The default state of this Status Bit S:36/12 is 0.

Select Timeout (x1 s)

The valid range is 1…65535. Default value is 10.

This parameter is used for controlling CROB (Control Relay Output Block) and AOB (Analog Output Block). After receiving the request with the function code FC\_SELECT(3), DNP3 master should send the request with the function code FC\_OPERATE(4) within this configured time.

DNP3 Object Data File Number

The DNP3 Object Data File Numbers define the mapping of the listed DNP3 objects to controller data table files. The number of elements that are defined for each of those data table files also defines the number of corresponding DNP3 objects.

See DNP3 Objects and Controller Data Files on page 203 for more details.

DNP3 Object Config File Number

The DNP3 Object Config File Numbers define the mapping of the listed DNP3 object properties (class number, online/offline status, object quality flags, deadbands, and/or thresholds) to controller data table files.

See DNP3 Objects and Controller Data Files on page 203 for more details.

DNP3 Secure Authentication

This section is applicable only to MicroLogix 1400 Series B and Series C controllers.

The controller implements the DNP3 Secure Authentication that is based on the DNP3 Specification, Supplement to Volume 2, Secure Authentication, Version 2.00.

DNP3 Secure Authentication has been implemented in the DNP3 Application Layer of the controller system. If you configure any parameters regarding DNP3 Secure Authentication in the DNP3 Slave Application Layer configuration, it affects all ports that are configured for the DNP3 protocol in the controller.

Enable Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

The valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Disabled (Unchecked).

When the selection is Disabled (Unchecked), the controller disables the DNP3 Secure Authentication subsystem.

When the selection is Enabled (Checked), the controller enables the DNP3 Secure Authentication subsystem.

Enable Aggressive Mode in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

The valid selections are Enabled (Checked) and Disabled (Unchecked). Default value is Enabled (Checked).

When the selection is Disabled (Unchecked), the controller disables DNP3 Aggressive Mode in the Secure Authentication subsystem.

When the selection is Enabled (Checked), the controller enables DNP3 Aggressive Mode in the Secure Authentication subsystem.

Critical FCs File Number in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This file number is used to define the list of the critical function codes in Secure Authentication. A critical function code should be defined in a word element in this file. The maximum number of elements in this file should not exceed 32 (the maximum number of the function codes that can be defined).

The value of this parameter is N file only. Valid range is 0, 7, 9…255. Default value is 0.

When this file number is configured to 0 and there is no configuration file that is assigned, some function codes are considered as critical by default. See Table 25 for the critical function codes. When this file number of this parameter is not 0 and it is a valid N data file, all function codes are considered as non-critical. In this case, you must define all critical function codes in this file.

The function code 0(FC\_CONFIRM) is considered as critical once the file number is configured newly. If you don't want the function code 0 to be considered as critical, the number of elements in the file should be adjusted and the element value 0 should not be in any elements.

Table 25 - Function Codes

|                             | Function Code Critical FCs File Number = 0 Critical FCs File Number = 0   |
|-----------------------------|---------------------------------------------------------------------------|
|                             | 0 (0x00) - optional                                                       |
|                             | 1 (0x01) - optional                                                       |
|                             | 2 (0x02) critical optional                                                |
|                             | 3 (0x04) critical optional                                                |
|                             | 4 (0x04) critical optional                                                |
|                             | 5 (0x05) critical optional                                                |
|                             | 6 (0x06) critical optional                                                |
|                             | 7 (0x07) - optional                                                       |
|                             | 8 (0x08) - optional                                                       |
|                             | 9 (0x09) - optional                                                       |
| 10 (0x0A) - optional        |                                                                           |
| 11 (0x0B) - -               |                                                                           |
| 12 (0x0C) - -               |                                                                           |
| 13 (0x0D) critical optional |                                                                           |
| 14 (0x0E) critical optional |                                                                           |
| 15 (0x0F) N.A. N.A.         |                                                                           |
| 16 (0x10) critical optional |                                                                           |
|                             | 17 (0x11) critical optional                                               |
|                             | 18 (0x12) critical optional                                               |
| 19 (0x13) N.A. N.A.         |                                                                           |
| 20 (0x14) critical optional |                                                                           |
| 21 (0x15) critical optional |                                                                           |
| 22 (0x16) - -               |                                                                           |
| 23 (0x17) - optional        |                                                                           |
| 24 (0x18) critical optional |                                                                           |
| 25 (0x19) - optional        |                                                                           |
| 26 (0x1A) - optional        |                                                                           |
|                             | 27 (0x1B) - optional                                                      |
| 28 (0x1C) - optional        |                                                                           |
| 29 (0x1D) critical optional |                                                                           |
|                             | 30 (0x1E) - optional                                                      |
| 31 (0x1F) critical optional |                                                                           |
| 32 (0x20) N.A. N.A.         |                                                                           |
| 33 (0x21) N.A. N.A.         |                                                                           |
| 129 (0x81) - optional       |                                                                           |
| 130 (0x82) - optional       |                                                                           |
| 131 (0x83) N.A. N.A.        |                                                                           |

Expected Session Key Change Interval (x1 s) in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This parameter is used for configuring the expected session key change interval in seconds.

The valid range is 0…7200 (2 hrs). Default value is 1800 (30 mins).

When DNP3 Master does not change the Session Key within this time that is configured, the controller invalidates the Session Key and its state for each user.

Expected Session Key Change Count in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This parameter is used for configuring the expected session key change count.

The valid range is 1…10000. Default value is 2000.

Reply Timeout (x100 ms) in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This parameter is used for configuring the reply timeout in 100 ms.

The valid range is 0…1200 (120 s). Default value is 20 (2 s).

Maximum Error Count in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series Controllers.

This parameter is used for configuring the maximum error count.

The valid range is 0…10. Default value is 2.

HMAC Algorithm in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This parameter is used for configuring the HMAC Algorithm.

- 1 = HMAC SHA-1 truncated to four octets (serial)
- 2 = HMAC SHA-1 truncated to 10 octets (networked)
- 3 = HMAC SHA-256 truncated to eight octets (serial)
- 4 = HMAC SHA-256 truncated to 16 octets (networked)

The valid range is 1…4. Default value is 2.

User Info Config File Number in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This file number is used to define user information Secure Authentication.

The value of this parameter is N file only. Valid range is 0, 7, 9…255. Default value is 0.

In RSLogix 500/RSLogix Micro software, when this parameter is configured properly, you can see a DNP3 Auth User Info Config File tree in Channel Configuration.

<!-- image -->

<!-- image -->

Table 26 shows the structure of the DNP3 Secure Authentication User Info Configuration File. An Update Key is composed of 16 bytes and must be entered in as 32 hexadecimal digits.

Table 26 - DNP3 Secure Authentication User Info Configuration File Structure

| Word Offset Name  Default Value By Controller (DEC)   | Default Value By RSLogix 500 (DEC)   | Valid Range (DEC) Description   |
|-------------------------------------------------------|--------------------------------------|---------------------------------|
| 0 User Number 0 1 0…65535 For User 1                  |                                      |                                 |
|                                                       |                                      | 1 Reserved 0 0 0 For User 1     |
| 2 Update Key (0) 0 0 0…65535                          |                                      |                                 |
| 3 Update Key (1) 0 0 0…65535                          |                                      |                                 |
| 4 Update Key (2) 0 0 0…65535                          |                                      |                                 |
| 5 Update Key (3) 0 0 0…65535                          |                                      |                                 |
| 6 Update Key (4) 0 0 0…65535                          |                                      |                                 |
| 7 Update Key (5) 0 0 0…65535                          |                                      |                                 |
| 8 Update Key (6) 0 0 0…65535                          |                                      |                                 |
| 9 Update Key (7) 0 0 0…65535                          |                                      |                                 |
| 10 User Number 0 0 0…65535 For User 2                 |                                      |                                 |
|                                                       |                                      | 11 Reserved 0 0 0 For User 1    |
| 12 Update Key (0) 0 0 0…65535                         |                                      |                                 |
| 13 Update Key (1) 0 0 0…65535                         |                                      |                                 |
| 14 Update Key (2) 0 0 0…65535                         |                                      |                                 |
| 15 Update Key (3) 0 0 0…65535                         |                                      |                                 |
| 16 Update Key (4) 0 0 0…65535                         |                                      |                                 |
| 17 Update Key (5) 0 0 0…65535                         |                                      |                                 |
| 18 Update Key (6) 0 0 0…65535                         |                                      |                                 |
| 19 Update Key (7) 0 0 0…65535                         |                                      |                                 |
| 90 User Number 0 0 0…65535 For User 10                |                                      |                                 |
|                                                       |                                      | 91 Reserved 0 0 0 For User 10   |
| 92 Update Key (0) 0 0 0…65535                         |                                      |                                 |
| 93 Update Key (1) 0 0 0…65535                         |                                      |                                 |
| 94 Update Key (2) 0 0 0…65535                         |                                      |                                 |
| 95 Update Key (3) 0 0 0…65535                         |                                      |                                 |
| 96 Update Key (4) 0 0 0…65535                         |                                      |                                 |
| 97 Update Key (5) 0 0 0…65535                         |                                      |                                 |
| 98 Update Key (6) 0 0 0…65535                         |                                      |                                 |
| 99 Update Key (7) 0 0 0…65535                         |                                      |                                 |

Diagnostic File Number in Secure Authentication

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

The diagnostic file number is used to store the diagnostics for the troubleshooting of the DNP3 Secure Authentication subsystem.

The value of this parameter is N file only. Valid range is 0, 7, 9…255. Default value is 0.

For the content of the configuration data file, see Table 43 in the Diagnostics section.

Default Variation Config File Number

This parameter is supported only in MicroLogix 1400 Series B and Series C controllers.

This file number is used to define default variations in a response to a Class 0 poll request.

The value of this parameter is N file only. Valid range is 0, 7, 9…255. Default value is 0.

In RSLogix 500/RSLogix Micro software, when this parameter is configured properly, you can see a DNP3 Default Variation Config File tree in Channel Configuration.

Table 27 shows the structure of the DNP3 Default Variation Configuration File.

<!-- image -->

<!-- image -->

Table 27 - DNP3 Default Variation Configuration File

| Word Offset Default Variation for Objects  Group and Standard Default Variation  Alternate Default Variations   |
|-----------------------------------------------------------------------------------------------------------------|
| 0 Binary Input Static Object g1v1 v2                                                                            |
| 1 Binary Input Change Object g2v3 v1, v2                                                                        |
| 2 Binary Output Static Object g10v2 none                                                                        |
| 3 Reserved -                                                                                                    |
| 4 Double Bit Binary Input Static Object g3v1 v2                                                                 |
| 5 Double Bit Binary Input Change Object g4v3 v1, v2                                                             |
| 6 16-bit Counter Static Object g20v6 v2                                                                         |
| 7 32-bit Counter Static Object g20v5 v1                                                                         |
| 8 Frozen 16-bit Counter Static Object g21v10 v2, v6                                                             |

Table 27 - DNP3 Default Variation Configuration File (Continued)

| Word Offset Default Variation for Objects  Group and Standard Default Variation   | Alternate Default Variations   |
|-----------------------------------------------------------------------------------|--------------------------------|
| 9 Frozen 32-bit Counter Static Object g21v9 v1, v5                                |                                |
| 10 16-bit Counter Change Object g22v2 none                                        |                                |
| 11 32-bit Counter Change Object g22v1 none                                        |                                |
| 12 Frozen 16-bit Counter Change Object g23v2 v6                                   |                                |
| 13 Frozen 32-bit Counter Change Object g23v1 v5                                   |                                |
| 14 16-bit Analog Input Static Object g30v4 v2                                     |                                |
| 15 32-bit Analog Input Static Object g30v3 v1                                     |                                |
| 16 Short Floating endpoint Analog Input Static Object g30v5 none                  |                                |
| 17 16-bit Analog Input Change Object g32v2 v4                                     |                                |
| 18 32-bit Analog Input Change Object g32v1 v3                                     |                                |
| 19 Short Floating endpoint Analog Input Change Object g32v5 v7                    |                                |
| 20 16-bit Analog Output Static Object g40v2 none                                  |                                |
| 21 32-bit Analog Output Static Object g40v1 none                                  |                                |
| 22 Short Floating endpoint Analog Output Static Object g40v3 none                 |                                |
| 23 Reserved -                                                                     |                                |
| 24 Reserved -                                                                     |                                |
| 25 Reserved -                                                                     |                                |
| 26 Small BCD Object g101v1 none                                                   |                                |
| 27 Reserved -                                                                     |                                |
| 28 Reserved -                                                                     |                                |
| 29 Reserved -                                                                     |                                |
| 30 Reserved -                                                                     |                                |
| 31 Reserved -                                                                     |                                |

## Disable EtherNet/IP Incoming Connections

## IMPORTANT

You cannot disable the EtherNet/IP Incoming Connections if both serial Channels 0 and 2 are already configured as disabled.

See Disable the Ethernet Channel for an alternative way to disable the Ethernet channel.

If you have a critical application and do not want to allow any EtherNet/IP Incoming Connections, use the parameter Disable EtherNet/IP Incoming Connections.

1. From the Channel 1 Ethernet Channel Configuration tab, select the checkbox to disable the EtherNet/IP Incoming Connections.

<!-- image -->

## DNP3 Slave Application Layer

2. Select Apply and OK.
3. Perform a power cycle in order for the changes to take effect.

The controller does not allow any incoming EtherNet/IP connections anymore. This means that you cannot use RSLogix 500/RSLogix Micro over Ethernet port to monitor or change the configuration/user program.

For more information about Ethernet Port Disable, see MicroLogix 1400 Programmable Controllers Reference Manual, publication 1766-RM001 .

This section covers DNP3 slave application layer function codes and internal indications.

For details of packet formats for the request and response, see the DNP3 protocol specifications.

## Function Codes

FC\_CONFIRM (FC Byte = 0x00)

00 – Confirm

A DNP3 master sends a message with this function code to confirm receipt of a response fragment. In a general environment, the controller receives a response with this function code. But the controller can generate a response with this function code when a DNP3 Master sends a request with the CON bit set in the application control header.

FC\_READ (FC Byte = 0x01)

01 – Read

The READ function code is used by a DNP3 master to request data from the controller.

FC\_WRITE (FC Byte = 0x02)

02 – Write

The WRITE function code is used to write the contents of DNP3 objects from the DNP3 master to the controller. This function code is used for clearing bit IIN1.7 [DEVICE\_RESTART], to set time in the controller, and to download user programs to the controller.

FC\_SELECT (FC Byte = 0x03)

03 – Select

The SELECT function code is used with the OPERATE function code as part of the select-beforeoperate method for issuing control requests. This procedure is used for controlling binary output (CROB) or analog output (AOB) objects.

FC\_OPERATE (FC Byte = 0x04)

04 – Operate

See FC\_SELECT (FC Byte = 0x03) on page 199 .

FC\_DIRECT\_OPERATE (FC Byte = 0x05)

05 – Direct Operate

This direct operate function is similar to the FC\_OPERATE function code except that no preceding select command is required.

FC\_DIRECT\_OPERATE\_NR (FC Byte = 0x06)

06 – Direct Operate No Resp

See FC\_DIRECT\_OPERATE (FC Byte = 0x05). No response message is returned when this request is issued from a DNP3 master.

## FC\_IMMED\_FREEZE (FC Byte = 0x07)

## 07 – Immediate Freeze

Upon receiving a request with this function, the controller copies the current value of a counter point to a separate memory location associated with the same point. The copied value remains constant until the next freeze operation to the same point.

## FC\_IMMED\_FREEZE\_NR (FC Byte = 0x08)

## 08 – Immediate Freeze No Resp

See FC\_IMMED\_FREEZE (FC Byte = 0x07). No response message is returned when this request is issued from a DNP3 master.

## FC\_FREEZE\_CLEAR (FC Byte = 0x09)

## 09 – Freeze and Clear

Upon receiving a request with this function, the controller copies the current value to the frozen value, then clears the current value to 0 immediately.

## FC\_FREEZE\_CLEAR\_NR (FC Byte = 0x0A)

## 10 – Freeze and Clear No Resp

See FC\_FREEZE\_CLEAR (FC Byte = 0x09). No response message is returned when this request is issued from a DNP3 master.

## FC\_COLD\_RESTART (FC Byte = 0x0D)

## 13 – Cold Restart

This function code forces the controller to perform a complete restart upon powering up.

## FC\_WARM\_RESTART (FC Byte = 0x0E)

14 – Warm Restart

This function code forces the controller to perform a partial reset.

This applies only to the MicroLogix 1400 Series B and Series C controller.

## FC\_INITIALIZE\_APPL (FC Byte = 0x10)

## 16 – Initialize Application

This function code is used to initialize the user program that is downloaded by RSLogix 500/ RSLogix Micro software.

## FC\_START\_APPL (FC Byte = 0x11)

## 17 – Start Application

This function code is used to start the user program that is downloaded by RSLogix 500/RSLogix Micro software.

<!-- formula-not-decoded -->

18 Stop Application

This function code is used to stop the user program that is downloaded by RSLogix 500/RSLogix Micro software.

## FC\_ENABLE\_UNSOLICITED (FC Byte = 0x14)

## 20 – Enable Unsolicited Message

This function is used to enable dynamically unsolicited messages generated in the controller.

FC\_DISABLE\_UNSOLICITED (FC Byte = 0x15)

21 – Disable Unsolicited Message

This function is used to disable dynamically unsolicited messages generated in the controller.

FC\_DELAY\_MEASURE (FC Byte = 0x17)

23 – Delay Measurement used for Non-LAN Procedure

This function code is used to measure the communication channel delay time.

<!-- formula-not-decoded -->

24 – Record Current Time is used for LAN Procedure

This function code is used in the procedure synchronize time the controllers that communicate over a LAN.

This applies only to MicroLogix 1400 Series B and Series C controllers.

<!-- formula-not-decoded -->

25 – Open File

This function code is used to make a file available for reading or writing.

<!-- formula-not-decoded -->

26 – Close File

After the file read or write operation, this function code is used to unlock the file.

<!-- formula-not-decoded -->

27 – Delete File

A DNP3 master uses this function code to delete a file.

<!-- formula-not-decoded -->

28 – Get File Information

This function code is for the master to retrieve information about a file in the controller.

This applies only to MicroLogix 1400 Series B and Series C controllers.

FC\_AUTHENTICATE\_FILE (FC Byte = 0x1D)

29 – Authenticate File

This function code is used to obtain an authentication key that is needed to open or delete a file.

<!-- formula-not-decoded -->

30 – Abort File

This function code is used to request immediate termination of the current read/write operation and close the file, without saving.

This applies only to MicroLogix 1400 Series B and Series C controllers.

<!-- formula-not-decoded -->

31 – Activate Config

This function code is used to begin using the configuration or executable code that is specified by the objects that are included in the request.

This applies only to MicroLogix 1400 Series B and Series C controllers.

## FC\_AUTHENTICATION\_REQUEST (FC Byte = 0x20)

## 32 – Authentication Request

The master uses this function code to send authentication messages to the controller that require a response.

This applies only to MicroLogix 1400 Series B and Series C controllers.

FC\_AUTHENTICATION\_REQUEST\_NR (FC Byte = 0x21)

## 33 – Authentication Request No Resp

This function code is used by the master to send authentication messages when no return response is required.

This applies only to MicroLogix 1400 Series B and Series C controllers.

<!-- formula-not-decoded -->

129 – Response

All responses except for Unsolicited Response messages use this function code.

FC\_UNSOLICITED\_RESPONSE (FC Byte = 0x82)

## 130 – Unsolicited Response

Unsolicited Responses always use this function code regardless of which DNP3 objects are included.

FC\_AUTHENTICATION\_RESPONSE (FC Byte = 0x83)

131 – Authentication Response

This function code is used to issue authentication messages to the master. This applies only to MicroLogix 1400 Series B and Series C controllers.

## Internal Indications

Internal Indication bits are set under the following conditions of the controllers:

- IIN1.0: ALL\_STATIONS. This bit is set when an all-stations message is received.
- IIN1.1: CLASS\_1\_EVENTS. This bit is set when Class 1 event data is available.
- IIN1.2: CLASS\_2\_EVENTS. This bit is set when Class 2 event data is available.
- IIN1.3: CLASS\_3\_EVENTS. This bit is set when Class 3 event data is available.
- IIN1.4: NEED\_TIME. This bit is set when time synchronization is required.
- IIN1.5: LOCAL\_CONTROL. This bit is set when the controller is in Non-executing mode.
- IIN1.6: DEVICE\_TROUBLE. This bit is set when the controller is in Fault mode.
- IIN1.7: DEVICE\_RESTART. This bit is set when the DNP3 driver is configured, in channel configuration, or when the controller has been restarted. To set this bit during the driver configuration and channel configuration, you must select the Send Init. Unsol. Null Resp. on Restart setting and set Status Bit S:36/13 to 1 before downloading to the controller.
- IIN2.0: NO\_FUNC\_CODE\_SUPPORT. This bit is set when a request that has an unknown function code is received.
- IIN2.1: OBJECT\_UNKNOWN. This bit is set when a request that has an unknown object is received.
- IIN2.2: PARAMETER\_ERROR. This bit is set when a request with a qualifier/range field that cannot be processed is received.
- IIN2.3: EVENT\_BUFFER\_OVERFLOW. This bit is set when an event buffer overflow condition exists in the controller and at least one unconfirmed event is lost.
- IIN2.4: ALREADY\_EXECUTING. Not supported.

## DNP3 Objects and Controller Data Files

- IIN2.5: CONFIG\_CORRUPT. This bit is set when a bad file type and bad file number are detected.
- IIN2.6: Reserved.
- IIN2.7: Reserved.

You can access the last transmitted IIN bits in the response by accessing the element of the Communication Status file, CS0:58 or CS2:58. For more details, see Diagnostics .

All DNP3 Objects that are supported in the controller are summarized in Implementation Table .

Data file types that are used in DNP3 Objects are not the same as the types used in the MicroLogix controller, but they are similar. Mapping is required between DNP3 data files and controller data files.

## Overview

The following are DNP3 data objects that are implemented in the controller:

- DNP3 Binary Input Object
- DNP3 Double Bit Binary Input Object
- DNP3 Binary Output Object
- DNP3 Counter Object
- DNP3 Frozen Counter Object
- DNP3 Analog Input Object
- DNP3 Analog Output Object
- DNP3 BCD Object
- DNP3 Data-Set Object (Series B and Series C controllers only)

Some of the objects are divided into several Object files to map data files in the controller.

- Counter Object — 16-bit and 32-bit Counter Object File
- Analog Input Object — 16-bit and 32-bit Analog Input Object File, and Short Floating Point Analog Input Object File.
- Analog Output Object — 16-bit and 32-bit Analog Output Object File, and Short Floating Point Analog Output Object File.

## For MicroLogix 1400 Series A controllers:

<!-- image -->

## For MicroLogix 1400 Series B and Series C controllers:

<!-- image -->

Each of the data files for a DNP3 Object have a file number in the user memory as shown in Table 28. You can configure the Data file number for each DNP3 Object in the DNP3 Slave tab of the DNP3 Slave Application Layer Configuration. File types for this object file can be Binary, Integer, Long, or Float data files.

The file numbers for each DNP3 Object cannot be in conflict with each other.

## DNP3 Data Files

Table 28 - Relationship between DNP3 Object Database and MicroLogix Data Files

| DNP Objects MicroLogix Data Files         | DNP Objects MicroLogix Data Files               | DNP Objects MicroLogix Data Files                                                                     |                               |
|-------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------|
| Object Name                               | Maximum Configurable Index                      | Related Groups File name for Data File Type File Number                                               | Maximum Configurable Elements |
|                                           |                                                 | Binary Input Object 1, 2 4096 Binary Input Object File Only B file 3, 9…255 256                       |                               |
|                                           |                                                 | Double Bit Binary Input Object 3, 4 2048 Double Bit Binary Input Object File Only B file 3, 9…255 256 |                               |
|                                           |                                                 | Binary Output Object 10, 12 4096 Binary Input Object File Only B file 3, 9…255 256                    |                               |
| Counter Object 20, 22 256                 |                                                 | 16-bit Counter Object File Only N file 7, 9…255                                                       | 256                           |
| Counter Object 20, 22 256                 |                                                 | 32-bit Counter Object File Only L file 9…255                                                          | 256                           |
| Frozen Counter Object 21, 23              | reflection of Counter Object that is configured | reflection of 16-bit Counter Object File                                                              | ---                           |
| Frozen Counter Object 21, 23              | reflection of Counter Object that is configured | reflection of 32-bit Counter Object File                                                              | ---                           |
| Analog Input Object 30, 32 256            |                                                 | 16-bit Analog Input Object File Only N file 7, 9…255                                                  | 256                           |
| Analog Input Object 30, 32 256            |                                                 | 32-bit Analog Input Object File Only L file 9…255                                                     | 256                           |
| Analog Input Object 30, 32 256            |                                                 | Short Floating Point Analog Input Object File Only F file 8, 9…255                                    | 256                           |
| Analog Output Object 40, 41 256           |                                                 | 16-bit Analog Output Object File Only N file 7, 9…255                                                 | 256                           |
| Analog Output Object 40, 41 256           |                                                 | 32-bit Analog Output Object File Only L file 9…255                                                    | 256                           |
| Analog Output Object 40, 41 256           |                                                 | Short Floating Point Analog Output Object File Only F file 8, 9…255                                   | 256                           |
|                                           |                                                 | BCD Object 101 256 Small BCD Object File Only N file 7, 9…255 256                                     |                               |
| Data-Set Object(In Series B and Series C) | 10                                              | 85, 87, 88  Data-Set Prototypes Object File                                                           | Only N file 7, 9…255 10       |
| Data-Set Object(In Series B and Series C) | 10                                              | 86, 87, 88 Data-Set Descriptors Object File                                                           | Only N file 7, 9…255 10       |

The firmware automatically evaluates the index number of DNP objects of each type as per the number of elements. For example, if a Binary Input object file was configured as an element, the highest index number of the Binary Input object is 15. The index number can only increase by 16. If a Double-bit Binary Input object file was configured as an element, the highest index number of the Double-bit Binary Input object is 7. The index number can only increase by 8.

As another example, if a 16-bit Analog Input object file was configured as an element, the highest index number is 1. Except for Binary and Double-bit Binary type objects, the index number can increase by 1.

## DNP3 Configuration Files

You can set configuration files for each object. These configuration files allow you to configure parameters such as Class level and Object Flag bit information for each element. Only a Binary Data file type can be used for a configuration file.

Table 29 - Relationship between MicroLogix Data Files and Configuration Files

| MicroLogix Data Files Configuration Files File Type File Number   |                                                                                                | Maximum Configurable Elements   |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------|---------------------------------|
| Binary Input File                                                 | Binary Input Config File                                                                       | Only B file 3, 9…255 256        |
| Binary Input File                                                 | Binary Input Online Config File (In Series B and Series C)                                     | Only B file 3, 9…255 256        |
| Double Bit Binary Input File                                      | Double-bit Binary Input Config File                                                            |                                 |
| Double Bit Binary Input File                                      | Only B file 3, 9…255 256 Double-bit Binary Input Online Config File (In Series B and Series C) |                                 |
|                                                                   | Binary Output File Binary Output Config File Only B file 3, 9…255 256                          |                                 |
| 16-bit Counter File                                               | 16-bit Counter Config File Only B file 3, 9…255                                                | 256                             |
| 16-bit Counter File                                               | 16-bit Counter Threshold Config File (In Series B and Series C) Only N file 7, 9…255           | 256                             |
| 32-bit Counter File                                               | 32-bit Counter Config File Only B file 3, 9…255                                                | 256                             |
| 32-bit Counter File                                               | 32-bit Counter Threshold Config File (In Series B and Series C) Only L file 9…255              | 256                             |
|                                                                   | Frozen 16-bit Counter File Frozen 16-bit Counter Config File Only B file 3, 9…255 256          |                                 |
|                                                                   | Frozen 32-bit Counter File Frozen 32-bit Counter Config File Only B file 3, 9…255 256          |                                 |

Table 29 - Relationship between MicroLogix Data Files and Configuration Files (Continued)

| MicroLogix Data Files Configuration Files File Type File Number   |                                                                                                                |                          | Maximum Configurable Elements   |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------|---------------------------------|
| 16-bit Analog Input File                                          | 16-bit Analog Input Config File Only B file 3, 9…255                                                           |                          | 256                             |
| 16-bit Analog Input File                                          | 16-bit Analog Input Deadband Config File (In Series B and Series C)                                            | Only N file 7, 9…255     | 256                             |
| 32-bit Analog Input File                                          | 32-bit Analog Input Config File Only B file 3, 9…255                                                           |                          | 256                             |
| 32-bit Analog Input File                                          | 32-bit Analog Input Deadband Config File (In Series B and Series C)                                            | Only L file 9…255        | 256                             |
| Short Floating Point Analog Input File                            | Short Floating Point Analog Input Config File Only B file 3, 9…255                                             |                          | 256                             |
| Short Floating Point Analog Input File                            | Short Floating Point Analog Input Deadband Config File (In Series B and Series C)                              | Only F file 8, 9…255     | 256                             |
|                                                                   | 16-bit Analog Output File 16-bit Analog Output Config File (In Series B and Series C) Only B file 3, 9…255 256 |                          |                                 |
|                                                                   | 32-bit Analog Output File 32-bit Analog Output Config File (In Series B and Series C) Only B file 3, 9…255 256 |                          |                                 |
| Short Floating Point Analog Output File                           | Short Floating Point Analog Output Config File (In Series B and Series C)                                      | Only B file 3, 9…255 256 |                                 |
|                                                                   | Small BCD File Small BCD Class Config File Only B file 3, 9…255 256                                            |                          |                                 |

For Binary Input, Double Bit Binary Input, and Small BCD type data, you can configure Class information in the Configuration file. The lower 2 bits in the elements of the Configuration files are the configuration of Class information to the relative objects. Other bits are reserved.

## Related Configuration Files:

- Binary Input Config File Number
- Double Bit Binary Input Config File Number

## Class Information Configuration for Binary Input, Double Bit Binary Input, and Small BCD

| Bit Offset 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|----------------------------------------------------|
| Element 0 r r r r r r r r r r r r r r C1 C0        |
| Element 1 r r r r r r r r r r r r r r C1 C0        |
| Element 2 r r r r r r r r r r r r r r C1 C0        |
| Element 3 r r r r r r r r r r r r r r C1 C0        |
| Element 4 r r r r r r r r r r r r r r C1 C0        |
| Element 5 r r r r r r r r r r r r r r C1 C0        |
| …                                                  |

r: reserved

C1/C0: Class level, 0…3

For Binary Input, Element\_0 for data index 0…15

For Double-bit Binary Input, Element \_0 for data index 0…7

For Binary Input and Binary Output type data, you can configure Online information of the object flag in the Configuration file. If this bit is set, the Online bit (bit 0) in the object flag for each point is set when you read Status type objects. You can set this information using ladder logic.

## Related Configuration File:

- Binary Input Online Config File Number (In Series B and Series C)
- Binary Output Online Config File Number

## Binary Input and Binary Output Type Configuration Data File

| Bit Offset 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|----------------------------------------------------|
| Element 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0          |
| Element 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0          |
| Element 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0          |
| Element 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0          |
| Element 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0          |

## Binary Input and Binary Output Type Configuration Data File (Continued)

| Bit Offset 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|----------------------------------------------------|
| Element 5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0          |
| …                                                  |

0: Offline

1: Online

For Binary Output, Element\_0 for data index 0…15

For other Input type data, you can configure Class information and the object flag information in the Configuration file. The lower 2 bits in the elements of the Configuration files are the configuration of Class information to the relevant objects. The upper byte of the configuration file of these objects is used to configure the object flag. Other bits are reserved.

Two new bits are defined in MicroLogix 1400 Series B and Series C controllers. The bit TE is used to generate an event by setting it regardless of the change of state. This bit can be used to generate the timed events. Once the ladder logic or communications sets the bit, the controller clears it automatically after generating an event at the end of the scan. The bit DCE is used to suppress the events by the change of state.

For example, if you want to trigger an event for an analog point every 15 minutes, you should set the TE bit every 15 minutes by the ladder logic. But, in this case, you may not want the state change events to be generated. Then, set the bit DCE. You can get the timed events every 15 minutes.

## Related Configuration File Number:

- 16-bit Counter Config File Number
- 32-bit Counter Config File Number
- 16-bit Frozen Counter Config File Number
- 32-bit Frozen Counter Config File Number
- 16-bit Analog Input Config File Number
- 32-bit Analog Input Config File Number
- Short Floating Point Analog Input Config File Number

## Class and Object Configuration for Other Input Data Type

| Bit Offset 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0       |
|--------------------------------------------------------|
| Element 0 F7 F6 F5 F4 F3 F2 F1 F0 r r DCE TE r r C1 C0 |
| Element 1 F7 F6 F5 F4 F3 F2 F1 F0 r r DCE TE r r C1 C0 |
| Element 2 F7 F6 F5 F4 F3 F2 F1 F0 r r DCE TE r r C1 C0 |
| Element 3 F7 F6 F5 F4 F3 F2 F1 F0 r r DCE TE r r C1 C0 |
| Element 4 F7 F6 F5 F4 F3 F2 F1 F0 r r DCE TE r r C1 C0 |
| Element 5 F7 F6 F5 F4 F3 F2 F1 F0 r r DCE TE r r C1 C0 |
| …                                                      |

TE: Trigger Event for the point (In Series B and Series C)

DCE: Disable change of state Event for the point (In Series B and Series C)

For other Inputs, Element \_0 for data index 0

F7…F0: Object Flags, FLAG7/FLAG6/FLAG5/LOCAL\_FORCED/REMOTE\_FORCED/COMM\_LOST/RESTART/ONLINE

For Counter type data, you can configure Threshold information in the Configuration file. Each element can be configured to the threshold value for each point. A counter event is generated if the absolute value of the difference between the present value of a counter point and the value that was most recently queued as an event for that point exceeds the threshold value that was configured in this file.

## Related Configuration File Numbers:

- 16-bit Counter Threshold Config File Number (In Series B and Series C)
- 32-bit Counter Threshold Config File Number (In Series B and Series C)

## Analog Output Configuration Data File

| Bit Offset 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|----------------------------------------------------|
| Element 0 F7 F6 F5 F4 F3 F2 F1 F0 r r r r r r r r  |
| Element 1 F7 F6 F5 F4 F3 F2 F1 F0 r r r r r r r r  |
| Element 2 F7 F6 F5 F4 F3 F2 F1 F0 r r r r r r r r  |
| Element 3 F7 F6 F5 F4 F3 F2 F1 F0 r r r r r r r r  |
| Element 4 F7 F6 F5 F4 F3 F2 F1 F0 r r r r r r r r  |
| Element 5 F7 F6 F5 F4 F3 F2 F1 F0 r r r r r r r r  |
| …                                                  |

r: reserved

F7…F0: Object Flags, FLAG7/FLAG6/FLAG5/LOCAL\_FORCED/REMOTE\_FORCED/COMM\_LOST/RESTART/ONLINE

For Small BCD type data, you can configure Class information in the Configuration file. The lower 2 bits in each element of the Configuration files are the configuration of Class information to the relevant objects. The P0 bit in the first element is to exclude Small BCD Data from Class 0 poll responses. Other bits are reserved.

| Word Offset Description         |
|---------------------------------|
| Element 0 Threshold for point 0 |
| Element 1 Threshold for point 1 |
| Element 2 Threshold for point 2 |
| Element 3 Threshold for point 3 |
| Element 4 Threshold for point 4 |
| Element 5 Threshold for point 5 |

For Analog Input type data, you can configure deadband information in the Configuration file. Each element can be configured to the deadband value for each point. An analog input event is generated if the absolute value of the difference between the present value of an analog input point and the value that was most recently queued as an event for that point exceeds the deadband value that was configured in this file.

Related Configuration File Numbers:

- 16-bit Analog Input Deadband Config File Number (In Series B and Series C)
- 32-bit Analog Input Deadband Config File Number (In Series B and Series C)
- Short Floating Point Analog Input Deadband Config File Number (In Series B and Series C)

| Word Offset Description        |
|--------------------------------|
| Element 0 Deadband for point 0 |
| Element 1 Deadband for point 1 |
| Element 2 Deadband for point 2 |
| Element 3 Deadband for point 3 |
| Element 4 Deadband for point 4 |
| Element 5 Deadband for point 5 |

For Analog Output type data, you can configure the object flag information in the Configuration file. The upper byte of the configuration file of these objects is used to configure the object flag. Other bits are reserved.

## Related Configuration File Numbers:

- 16-bit Analog Input Deadband Config File Number (In Series B and Series C)
- 32-bit Analog Input Deadband Config File Number (In Series B and Series C)
- Short Floating Point Analog Input Deadband Config File Number (In Series B and Series C)

## Small BCD Configuration File Data

| Bit Offset 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |       |
|----------------------------------------------------|-------|
| Element 0 r r r r r r r r PO r r r r r C1 C0       |       |
| Element 1 r r r r r r r r r r r r r r C1 C0        |       |
| Element 2 r r r r r r r r r r r r r r C1 C0        |       |
| Element 3 r r r r r r r r r r r r r r C1 C0        |       |
| Element 4 r r r r r r r r r r r r r r C1 C0        |       |
| Element 5 r r r r r r r r r r r r r r C1 C0        |       |
| …                                                  | C1 C0 |

r: reserved

C1/C0 : Class level, 0…3

For Small BCD, Element\_0 for data index 0

P0: 0 for including Small BCD Data to Class 0 poll response

## DNP3 Binary Input Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read the object with all variations.

Binary Input Static Objects:

- g1v0 – Binary Input – All Variations
- g1v1 – Binary Input – Packed format (default)
- g1v2 – Binary Input – With flags

Binary Input Event Objects:

- g2v0 – Binary Input Event – All Variations
- g2v1 – Binary Input Event – Without time
- g2v2 – Binary Input Event – With absolute time
- g2v3 – Binary Input Event – With relative time (default)

## Related Object File Number:

- Binary Input Object File Number

Related Configuration File Number:

- Binary Input Config File Number

To generate a Binary Input Object from the DNP3 Subsystem in the controller, you should configure the Binary Input Object File Number in the DNP3 Slave Application Layer Configuration file.

When the Binary Input Object File is configured, the Index number starts from 0. 1 bit is used for one Index.

## Related Configuration File Numbers:

- Small BCD Config File Number

As an example, a Binary Input Object File is configured as shown. This file has 10 elements and 160 Binary Input points. Index 0 of the Binary Input Object is B10:0/0, Index 1 is B10:0/1 and Index 159 is B10:9/15.

<!-- image -->

As an example, a Binary Input Config File shown has 10 elements. B30:0/0 and B30:0/1 can be configured for Class Level 0, 1, 2, or 3 for DNP3 Index 0…15 of the Binary Input Object File. B30:1/0 and B30:1/1 can be configured for Class Level for DNP3 Index 16…31 of the Binary Input Object File. Default Class Level is 0. Any other bits are reserved.

Class Level of Index 0…15 is 1(B30:0/0 and B30:0/1), Class Level of Index 16…31 is 2(B30:1/0 and B30:1/1), Class Level of Index 32…47 is 3(B30:2/0 and B30:2/1), and Class Level of other Indexes are 0.

<!-- image -->

## DNP3 Binary Output Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read the object with Any Variation.

Binary Output Static Objects:

- g10v0 – Binary Output – All Variations
- g10v2 – Binary Output – Output status with flags (default)

Binary Output Command Objects:

- g12v1 – Binary Command – Control relay output block (CROB)

Related Object File Number:

- Binary Output Object File Number

Related Configuration File Number:

- Binary Output Config File Number

To generate a Binary Output Object from the DNP3 Subsystem in the controller, you should configure the Binary Output Object File Number in the DNP3 Slave Application Layer Configuration file.

When the Binary Output Object File is configured, the Index number starts from 0. 1 bit is used for one Index.

As an example, a Binary Output Object File is configured as shown. This file has 10 elements and 160 Binary Output points. Index 0 of the Binary Output Object is B11:0/0, Index 1 is B11:0/1 and Index 159 is B11:9/15.

<!-- image -->

As an example, a Binary Output Config File shown has 10 elements. Each bit can be configured for Online information (if the corresponding point is active or not, 0=offline, 1=online) of the Binary Output points. B31:0/0 is for Index 0, B31:0/1 is for Index 1 and B31:9/15 is for Index 159. In the example, all bits are cleared and all of the points are in an offline state.

If this bit is set, all Online bits in the status flag of each Binary Output point is set when you read Binary Output Status objects.

Binary Command – Control Relay Output Block (CROB)

<!-- image -->

The controller has three control models for Binary Output Control. They are Activation model, Complementary latch model, and Complementary two-output model.

For the Complementary two-output model, two bits are required to control this model in the Binary output object. The point index is different than in the Activation or Complementary latch model. The

Table 30 - Point Index

| Binary Output Database Index Activation Model or Complementary Latch Model Complementary Two-output Model   |
|-------------------------------------------------------------------------------------------------------------|
| 0 BO Index 0 BO Close Index 0                                                                               |
| 1 BO Index 1 BO Trip Index 0                                                                                |
| 2 BO Index 2 BO Close Index 1                                                                               |
| 3 BO Index 3 BO Trip Index 1                                                                                |
| 4 BO Index 4 BO Close Index 2                                                                               |
| 5 BO Index 5 BO Trip Index 2                                                                                |
| …… …                                                                                                        |
| 4094 BO Index 4094 BO Close Index 2047                                                                      |
| 4095 BO Index 4095 BO Trip Index 2047                                                                       |

These control codes and point models are implemented in the controller:

- 0x00 (NUL/NUL): Clear field Off
- 0x20 (NUL/NUL): Clear field On
- 0x01 (Pulse On/NUL): Clear field Off. Activation Model
- 0x21 (Pulse On/NUL): Clear field On. Activation Model
- 0x03 (Latch On/NUL): Clear field Off, Complementary latch model
- 0x23 (Latch On/NUL): Clear field On. Complementary latch model
- 0x04 (Latch Off/NUL): Clear field Off. Complementary latch model
- 0x24 (Latch Off/NUL): Clear field On. Complementary latch model
- 0x41 (Pulse On/Close): Clear field Off. Complementary two-output model
- 0x61 (Pulse On/Close): Clear field On. Complementary two-output model
- 0x81 (Pulse On/Trip): Clear field Off. Complementary two-output model
- 0xA1 (Pulse On/Trip): Clear field On. Complementary two-output model

When the controller is in Non-executing mode, the controller does not accept a Binary Command. The controller returns a Control Status Code 7 in response. To access objects 12(CROB), the controller must be in Executing mode.

Executing mode includes Run, Remote Run, Test Continuous Scan, and Test Single Scan modes. Any others are Non-executing modes.

## DNP3 Double Bit Binary Input Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read an object with Any variation.

Double-bit Binary Input Static Objects:

- g3v0 – Double-bit Binary Input – All Variations
- g3v1 – Double-bit Binary Input – Packed format (default)
- g3v2 – Double-bit Binary Input – With flags

Double-bit Binary Input Event Objects:

- g4v0 – Double-bit Binary Input Event – All Variations
- g4v1 – Double-bit Binary Input Event – Without time
- g4v2 – Double-bit Binary Input Event – With absolute time
- g4v3 – Double-bit Binary Input Event – With relative time (default)

Related Object File Number:

point index varies as shown in Table 30 on page 212. The maximum number of Binary Output index for Complementary two-output model is 2048.

- Double Bit Binary Input Object File Number

Related Configuration File Number:

- Double Bit Binary Input Config File Number

To generate a Double Bit Binary Input Object from the DNP3 Subsystem in the controller, you should configure the Double Bit Binary Input Object File Number in the DNP3 Slave Application Layer Configuration file.

When the Double Bit Binary Input Object File is configured, the Index number starts from 0. 2 bits are used for one Index.

As an example, a Double Bit Binary Input Object File is shown. This file has 10 elements and 80 Double Bit Binary Input points. Index 0 of the Double Bit Binary Input Object is B20:0/0 and B20:0/1, Index 1 is B20:0/2 and B20:0/3, and Index 79 is B20:9/14 and B20:9/15.

<!-- image -->

As an example, a Double Bit Binary Input Config File is shown. This file has 10 elements. B39:0/0 and B39:0/1 can be configured for Class Level 0, 1, 2, or 3 for DNP3 Index 0…7 of the Double Bit Binary Input Object File. B39:1/0 and B39:1/1 can be configured for Class Level for DNP3 Index 8…15 of the Double-bit Binary Input Object File. Default Class Level is 0. Any other bits are reserved. So, in the example, Class Level of Index 0…7 is 1(B39:0/0 and B39:0/1), Class Level of Index 8…15 is 2(B39:1/0 and B39:1/1), Class Level of Index 16…23 is 3(B39:2/0 and B39:2/1), and Class Level of other Indexes are 0.

<!-- image -->

## DNP3 Counter Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read an object with Any variation.

## Counter Static Objects:

- g20v0 – Counter – Any Variation
- g20v1 – Counter – 32-bit with flag
- g20v2 – Counter – 16-bit with flag
- g20v5 – Counter – 32-bit without flag (default)
- g20v6 – Counter – 16-bit without flag (default)

## Counter Event Objects:

- g22v0 – Counter Event – Any Variation
- g22v1 – Counter Event – 32-bit with flag (default)
- g22v2 – Counter Event – 16-bit with flag (default)

## Related Object File Number:

- 16-bit Counter Object File Number
- 32-bit Counter Object File Number

## Related Configuration File Number:

- 16-bit Counter Config File Number
- 32-bit Counter Config File Number

To generate a Counter Object from the DNP3 Subsystem in the controller, you should configure Counter Object File Numbers in the DNP3 Slave Application Layer Configuration file.

When only one Counter Object File is configured, the Index number starts from 0 for the configured object. One word is used for one Index of a 16-bit Counter Object and one double word is used for one Index of a 32-bit Counter Object.

If both the 16-bit Counter Object File Number and 32-bit Counter Object File Number were configured in the DNP3 Slave Application Layer Configuration file, the starting index number of 16-bit Counter Object is 0 and the starting index number of 32-bit Counter Object starts from the ending index number of the 16-bit Counter Object. For example, if 10 elements of a 16-bit Counter Object were configured and 10 elements of a 32-bit Counter Object were configured, the index number is:

- 16-bit Counter Object: From 0…9
- 32-bit Counter Object: From 10…19

Let's suppose you configured both 16-bit and 32-bit Counter Object Files as. Data File N12 has 10 elements and L13 has 10 elements accordingly. In total, 20 Counter Object indexes are configured. Index 0 of the Counter Object is N12:0, Index 1 is N12:1, Index 10 is L13:0, and Index 19 is L13:9.

<!-- image -->

As an example, a Counter Config File is shown. These files have 10 elements for each. B32:0/0 and B32:0/1 can be configured for Class Level 0, 1, 2, or 3 for DNP3 Index 0 of the 16-bit Counter Object File. B32:1/0 and B32:1/1 can be configured for Class Level for DNP3 Index 1 of the Counter Object File. Default Class Level is 0. Any other bits are reserved. So, in the example, for 16-bit Counter Config File, Class Level of Index 0 is 1(B32:0/0 and B32:0/1), Class Level of Index 1 is 2(B32:1/0 and B32:1/1), Class Level of Index 2 is 3(B32:2/0 and B32:2/1), and Class Level of other Indexes are 0.

<!-- image -->

For a 32-bit Counter Config File, Class Level of Index 10 is 1(B33:0/0 and B33:0/1), Class Level of Index 11 is 2(B33:1/0 and B33:1/1), Class Level of Index 12 is 3(B33:2/0 and B33:2/1), and Class Level of other Indexes are 0.

<!-- image -->

## DNP3 Frozen Counter Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read the object with all variations.

Frozen Counter Static Objects:

- g21v0 – Frozen Counter – All Variations
- g21v1 – Frozen Counter – 32-bit with flag
- g21v2 – Frozen Counter – 16 bit with flag
- g21v5 – Frozen Counter – 32-bit with flag and time
- g21v6 – Frozen Counter – 16-bit with flag and time
- g21v9 – Frozen Counter – 32-bit without flag (default)
- g21v10 – Frozen Counter – 16-bit without flag (default)

Frozen Change Event Objects:

- g23v0 – Frozen Counter Event – All Variations
- g23v1 – Frozen Counter Event – 32-bit with flag (default)
- g23v2 – Frozen Counter Event – 16-bit with flag (default)
- g23v5 – Frozen Counter Event – 32-bit with flag and time
- g23v6 – Frozen Counter Event – 16-bit with flag and time

## Related Object File Number:

- 16-bit Counter Object File Number
- 32-bit Counter Object File Number

## Related Configuration File Number:

- 16-bit Frozen Counter Config File Number
- 32-bit Frozen Counter Config File Number

To generate a Frozen Counter Object from the DNP3 Subsystem in the controller, you should configure the Counter Object File Number in the DNP3 Slave Application Layer Configuration file.

The number of elements for a Frozen Counter Object is the same as the number of Counter Objects. For example, if 10 Counter elements were configured, 10 Frozen Counter elements are generated in the controller internally. You cannot access the Frozen Counter database directly.

There is one buffer for a Frozen Counter Object. Read the Frozen Counter Object before you send another request with Freeze function codes. If two consecutive Freeze function codes are received without Read operation into them for a Frozen Counter Object, the second Freeze operation overwrites the values of Frozen Counter Objects.

If both 16-bit Counter Object File Number and 32-bit Counter Object File Number were configured in the DNP3 Slave Application Layer Configuration file, the 16-bit Frozen Counter Object starting index number is 0 and the 32-bit Frozen Counter Object starting index number of starts after the last index number for the 16-bit Frozen Counter Object. For example, if 10 elements of 16-bit Counter Object were configured and 10 elements of 32-bit Counter Object were configured, the index numbers are:

- 16-bit Frozen Counter Object: From 0…9
- 32-bit Frozen Counter Object: From 10…19

When only one of the Counter Object Files was configured, the Index number starts from 0 for the configured object.

As an example, a Frozen Counter Config File is shown. These files have 10 elements for each. B34:0/0 and B34:0/1 can be configured for Class Level 0, 1, 2 or 3 for DNP3 Index 0 of the 16 bits Frozen Counter Object File. B34:1/0 and B34:1/1 can be configured for Class Level for DNP3 Index 1 of the Counter Object File. Default Class Level is 0. Any other bits are reserved. So, in the example, for 16-bit Frozen Counter Config File, Class Level of Index 0 is 1(B34:0/0 and B34:0/1), Class Level of Index 1 is 2(B34:1/0 and B34:1/1), Class Level of Index 2 is 3(B34:2/0 and B34:2/1), and Class Level of other Indexes are 0.

<!-- image -->

For 32-bit Frozen Counter Config File, Class Level of Index 10 is 1(B35:0/0 and B35:0/1), Class Level of Index 11 is 2(B35:1/0 and B35:1/1), Class Level of Index 12 is 3(B35:2/0 and B35:2/1), and Class Level of other Indexes are 0.

<!-- image -->

## DNP3 Analog Input Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read the object with Any variation.

Analog Input Static Objects:

- g30v0 – Analog Input – Any Variations
- g30v1 – Analog Input – 32-bit with flag
- g30v2 – Analog Input – 16-bit with flag
- g30v3 – Analog Input – 32-bit without flag (default)
- g30v4 – Analog Input – 16-bit without flag (default)
- g30v5 – Analog Input – Single-prec flt-pt with flag (default)

Analog Input Event Objects:

- g32v0 – Analog Input Event – Any Variation
- g32v1 – Analog Input Event – 32-bit without time (default)
- g32v2 – Analog Input Event – 16-bit without time (default)
- g32v3 – Analog Input Event – 32-bit with time
- g32v4 – Analog Input Event – 16-bit with time

- g32v5 – Analog Input Event – Single-prec flt-pt without time (default)
- g32v7 – Analog Input Event – Single-prec flt-pt with time

## Related Object File Number:

- 16-bit Analog Input Object File Number
- 32-bit Analog Input Object File Number
- Short Floating Point Analog Input Object File Number

## Related Configuration File Number:

- 16-bit Analog Input Config File Number
- 32-bit Analog Input Config File Number
- Short Floating Point Analog Input Config File Number

To generate an Analog Input Object from the DNP3 Subsystem in the controller, you should configure the Analog Input Object File Number in the DNP3 Slave Application Layer Configuration file.

When only one Analog Input Object File is configured, the Index number starts from 0 for the configured object. One word is used for one Index of 16-bit Analog Input Object, one double word is used for one Index of 32-bit Analog Input Object, and one short float is used for one Index of Short Floating Point Analog Input Object.

If 16-bit Analog Input Object File Number, 32-bit Analog Input Object File Number, and Short Floating Point Analog Input Object File Number were configured in the DNP3 Slave Application Layer Configuration file, the starting index number of 16-bit Analog Input Object is 0 and the starting index number of 32-bit Analog Input Object starts from the ending index number of 16-bit Analog Input Object.

For example, if 10 elements of 16-bit Analog Input Object were configured, 10 elements of 32-bit Analog Input Object, and 10 elements of Short Floating Point Analog Input Object were configured, the index numbers are:

- 16-bit Analog Input Object: From 0…9
- 32-bit Analog Input Object: From 10…19
- Short Floating Point Analog Input Object: From 20…29

As an example, a configuration of 16-bit, 32-bit, and Short Floating Point Analog Input Object Files is shown. Data File N14 has 10 elements, L15 has 10 elements and F16 has 10 elements accordingly. A total of 30 Analog Input Object indexes are configured. Index 0 of the Analog Input Object is N14:0, Index 10 is L15:0, Index 20 is F16:0, and Index 29 is F16:9.

<!-- image -->

<!-- image -->

<!-- image -->

As an example, an Analog Input Config File is shown. These files have 10 elements each.

B36:0/0 and B36:0/1 can be configured for Class Level 0, 1, 2 or 3 for DNP3 Index 0 of the 16-bit Analog Input Object File.

B36:1/0 and B36:1/1 can be configured for Class Level for DNP3 Index 1 of the Analog Input Object File. Default Class Level is 0. Any other bits are reserved.

In the example, for 16-bit Analog Input Config File, Class Level of Index 0 is 1(B36:0/0 and B36:0/1), Class Level of Index 1 is 2(B36:1/0 and B36:1/1), Class Level of Index 2 is 3(B36:2/0 and B36:2/1), and Class Level of other Indexes are 0.

<!-- image -->

For a 32-bit Analog Input Config File, Class Level of Index 10 is 1(B37:0/0 and B37:0/1), Class Level of Index 11 is 2(B37:1/0 and B37:1/1), Class Level of Index 12 is 3(B37:2/0 and B37:2/1), and Class Level of other Indexes are 0.

<!-- image -->

For Short Floating Point Analog Input Config File, Class Level of Index 20 is 1(B38:0/0 and B38:0/1), Class Level of Index 21 is 2(B38:1/0 and B38:1/1), Class Level of Index 22 is 3(B38:2/0 and B38:2/1), and Class Level of other Indexes are 0.

<!-- image -->

## DNP3 Analog Output Object

The supported object group and variations are listed in this section. The controller responds with the default group and variation when the DNP3 Master requests to read an object with Any variation.

## Analog Output Status Objects:

- g40v0 – Analog Output Status – Any Variations
- g40v1 – Analog Output Status – 32-bit with flag (default)
- g40v2 – Analog Output Status – 16-bit with flag (default)
- g40v3 – Analog Output Status – Single-prec flt-pt with flag (default)

## Analog Output Command Objects:

- g41v1 – Analog Output – 32-bit
- g41v2 – Analog Output – 16-bit
- g41v3 – Analog Output – Single-prec flt-pt

## Related Object File Number:

- 16-bit Analog Output Object File Number
- 32-bit Analog Output Object File Number
- Short Floating Point Analog Output Object File Number

## Related Configuration File Number:

- – None

To generate an Analog Output Object from the DNP3 Subsystem in the controller, you should configure the Analog Output Object File Number in the DNP3 Slave Application Layer Configuration file.

When only one of the Analog Output Object Files is configured, the Index number starts from 0 for the configured object. One word is used for one Index of 16-bit Analog Output Object, one double word is used for one Index of 32-bit Analog Output Object, and one short float is used for one Index of Short Floating Point Analog Output Object.

If the 16-bit Analog Output Object File Number, 32-bit Analog Output Object File Number, and Short Floating Point Analog Output Object File Number are configured in the DNP3 Slave Application Layer Configuration file, the starting index number of 16-bit Analog Output Object is 0 and the starting index number of 32-bit Analog Output Object starts from the last index number of 16-bit Analog Output Object.

For example, if 10 elements of 16-bit Analog Output Object are configured, 10 elements of 32-bit Analog Output Object, and 10 elements of Short Floating Point Analog Output Object are configured, the index numbers are:

- 16-bit Analog Output Object: From 0…9
- 32-bit Analog Output Object: From 10…19
- Short Floating Point Analog Output Object: From 20…29

As an example, 16-bit, 32-bit, and Short Floating Point Analog Output Object Files are configured as. Data File N17 has 10 elements, L18 has 10 elements and F19 has 10 elements accordingly. A total of 30 Analog Output Object index are configured. Index 0 of the Analog Output Object is N17:0, Index 10 is L18:0, Index 20 is F19:0, and Index 29 is F19:9.

Analog Output Command – Control Analog Output Block (AOB)

<!-- image -->

When the controller is in Non-executing mode, the controller does not accept an Analog Output Command. The controller returns a Control Status Code 7 in the response. To access the objects 41(AOB), the controller mode should be in Executing mode.

Executing mode includes Run, Remote Run, Test Continuous Scan, and Test Single Scan modes. Any other modes are Non-executing modes.

## DNP3 BCD Object

The supported object group and variations are:

Numeric Static Objects:

- g101v1 – Binary-Coded Decimal Integer – Small

Related Object File Number:

- Small BCD Object File Number

Related Configuration File Number:

- Small BCD Config File Number

To generate a Small BCD Object from the DNP3 Subsystem in the controller, you should configure the Small BCD Object File Number in the DNP3 Slave Application Layer Configuration file.

When a Small BCD Object File is configured, the Index number starts from 0. One word is used for one Index of Small BCD Object.

As an example, a Small BCD Object File is configured as shown. Data File N21 has 10 elements. Index 0 of the Small BCD Object is N21:0, Index 1 is N21:1, and Index 9 is N21:9.

<!-- image -->

As an example, a Small BCD Config File is configured as shown. The file has 10 elements. B40:0/0 and B40:0/1 can be configured for Class Level 0, 1, 2, or 3 for DNP3 Index 0 of the Small BCD Object File. B40:1/0 and B40:1/1 can be configured for Class Level for DNP3 Index 1 of the Small BCD Object File. Default Class Level is 0. Any other bits are reserved.

In the example, for a Small BCD Config File, Class Level of Index 0 is 1(B40:0/0 and B40:0/1), Class Level of Index 1 is 2(B40:1/0 and B40:1/1), Class Level of Index 2 is 3(B40:2/0 and B40:2/1), and Class Level of other Indexes are 0.

<!-- image -->

## DNP3 Data-Set Object

This feature is supported only in MicroLogix 1400 Series B and Series C controllers.

These object groups and variations are supported.

## Data-Set Objects:

- g85v0 – Data-Set Prototype – Any Variation
- g85v1 – Data-Set Prototype – With UUID
- g86v1 – Data-Set Descriptor – Data-Set contents
- g86v2 – Data-Set Descriptor – Characteristics
- g87v0 – Static Data-Set – Any Variation
- g87v1 – Static Data-Set – Present value
- g88v0 – Event Data-Set – Any Variation
- g88v1 – Event Data-Set – Snapshot

Related Object/Configuration File Number:

- Data-Set Prototypes Object File Number
- Data-Set Descriptors Object File Number

To generate a Data-Set Object from the DNP3 Subsystem in the controller, configure the Data-Set Prototypes/Descriptors Object File Number in the DNP3 Slave Application Layer Configuration file and also the Maximum Number of Data-Set Prototypes/Descriptors Files.

Each Data-Set Prototypes Object file (N data file) can have up to 10 elements of Data-Set Prototypes, and each Data-Set Descriptors Object file (N data file) can have up to 10 elements of Data-Set Descriptors.

As an example, with Data-Set Prototypes files, if you configure Data-Set Prototypes Object File Numbers to 50 and Maximum Number of Data-Set Prototypes Files to 9, N Data files 50…58 are reserved to store the structure of the Data-Set Prototypes configuration.

<!-- image -->

As an example, with Data-Set Descriptors files, if you configure Data-Set Descriptors Object File Number to 60 and Maximum Number of Data-Set Descriptors File to 9, N Data files 60…68 are reserved to store the structure of the Data-Set Descriptors configuration.

<!-- image -->

Once the Data-Set Prototypes and Descriptors are configured in the DNP3 Slave Application Layer Configuration of RSLogix 500/RSLogix Micro software, you can see the DNP3 DS Prototype X and DNP3 DS Descriptor X trees under the Channel Configuration of RSLogix 500/RSLogix Micro software, where X is the element numbers of each Prototype or Descriptor.

<!-- image -->

For DNP3 DS Prototype X, you can configure the controller to construct the Data-Set Prototype objects.

<!-- image -->

For DNP3 DS Descriptor X, you can configure the controller to construct the Data-Set Descriptor objects.

Data-Set Prototypes Configuration Parameters

<!-- image -->

These parameters are used to construct Data-Set Prototypes object.

<!-- image -->

Number of Prototypes Elements: 0…10. This must be the same as the number of the Prototype elements that are configured.

Prototype Element Configuration: Each Prototypes element is configured in this configuration. Double-click an element to edit it.

<!-- image -->

Descriptor Code: UUID for element 1. NSPC/NAME/DAEL for element 2 or higher.

Data Type Code: NONE for element 1. NONE/VSTR/UINT/INT/FLT/OSTR/BSTR/TIME for element 2 or higher.

Max Data Length (bytes): 0 for element 1. 0…255 for element 2 or higher.

Ancillary Value: Binary Array in hexadecimal for element 1. ASCII strings for element 2 or higher. Maximum 32 bytes.

## Data-Set Descriptors Configuration Parameters

These parameters are used to construct Data-Set Descriptors objects.

<!-- image -->

Number of Descriptor Elements: 0…10. This must be the same as the number of the Descriptor elements that are configured.

Characteristics: Used to assign characteristics to this Descriptor.

- RD – set if Data-Set is readable.
- ST – set if the outstation maintains a static Data-Set.
- EV – set if the outstation generates a Data-Set event.

Event Class – Used to assign Event Class to this Descriptor.

- 0 – None
- 1 – Class 1
- 2 – Class 2
- 3 – Class 3

Trigger Event: Set this parameter to generate an event unconditionally. The ladder logic can also set the bit to generate timed events. Once the ladder logic or communications sets this parameter, the controller clears it automatically after generating an event at the end of the scan. This parameter is stored as a bit in the relevant Data-Set Descriptor Config file and the bit can be accessed by Nx:2/4 where x is the relevant Data-Set Descriptor Config file number.

Disable Change of State Event: Set the parameter to suppress the events that are generated by any Event Occurrence Condition.

Event Occurrence Condition: The conditions of Data-Set Event for each Data-Set Descriptor can be configured by Data-Set Event Occurrence Condition 0/1/2/3 in the DNP3 Data-Set Descriptors Object File. When one of the values that points to the Event Occurrence Condition 0/1/2/3 are changed or the criteria are met, the controller generates a Data-Set Event, retrievable using the object g88v1.

This table shows the supported conditions for Point Addressing. Double-click each case element to edit it.

<!-- image -->

Point Addressing under Event Occurrence Conditions: Valid selections are shown.

|                                                                                 | Point Address Type Point Type Point Index Event Occurrence Condition                                                            |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Standard DNP3 Point NONE: No point type is associated. 0 No Event is generated. |                                                                                                                                 |
| BI: Binary input 0…4095                                                         | When the Point Type and Point Index are point to a specific point, if the value of the point is changed, an event is generated. |
| B2I: Double-bit input 0…2047                                                    | When the Point Type and Point Index are point to a specific point, if the value of the point is changed, an event is generated. |
| CI: Counter 0…511                                                               | When the Point Type and Point Index are point to a specific point, if the value of the point is changed, an event is generated. |
| AI: Analog input 0…767                                                          | When the Point Type and Point Index are point to a specific point, if the value of the point is changed, an event is generated. |
| BCD: BCD point 0…255                                                            | When the Point Type and Point Index are point to a specific point, if the value of the point is changed, an event is generated. |
|                                                                                 | Reserved for others. Reserved for others. No Event is generated.                                                                |

A Data-Set event can consume any number of event buffers, depending on the Data-Set configuration. This is only applicable for Data-Set events. The event for other objects consumes a single event buffer. When using Data-Set events, increase the number of events in the DNP3 Slave configuration.

Descriptor Element Configuration: Each Descriptors element is configured in this here. Double-click each element to edit it.

<!-- image -->

Descriptor Code: NONE, NAME, DAEL, PTYP

<!-- image -->

Data Type Code: NONE, VSTR, UINT, INT, FLT, OSTR, BSTR, TIME

Max Data Length (bytes): 0…255

Ancillary Value: Any string. This can be a binary array or ASCII string, up to 16 words.

Point Addressing under Descriptor Element Configuration: Data-Set value for each Data-Set element is configured by:

- Point Address Type
- Point Type
- Point Index
- File Number
- File Element
- File Sub-element

When these values are configured properly according to the supported data files, the controller responds with a g87v1 object that is filled with the value in the data file. Table 31 shows the supported data files for the Point Addressing.

Table 31 - Point Address Type — Standard DNP3 Point

| Point Address Type Data Type Code   |                                             | Maximum Data Length (bytes)                   |                                        | Point Type Point Index Low Byte Point Index High Byte                                                                                    |                                                                                                                                          |
|-------------------------------------|---------------------------------------------|-----------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Standard DNP3 Point                 | NONE = 0 0                                  |                                               | NONE = 0: No point type is associated. | 0                                                                                                                                        |                                                                                                                                          |
| Standard DNP3 Point                 | UINT = 2 INT = 3 OSTR = 5 BSTR = 6 TIME = 7 | 0 0, 1, 2, or 4 0, 1, 2, or 4 0…255 0…255 0…6 | BI= 1: Binary input                    | 0…4095 max When the Data Types other than OSTR and BSTR are used, the Point Index must be set to a point offset that is divisible by 16. | 0…4095 max When the Data Types other than OSTR and BSTR are used, the Point Index must be set to a point offset that is divisible by 16. |
| Standard DNP3 Point                 | UINT = 2 INT = 3 OSTR = 5 BSTR = 6 TIME = 7 | 0 0, 1, 2, or 4 0, 1, 2, or 4 0…255 0…255 0…6 | B2I= 3: Double-bit input               | 0…2047 max When the Data Types other than OSTR and BSTR are used, the Point Index must be set to a point offset that is divisible by 8.  | 0…2047 max When the Data Types other than OSTR and BSTR are used, the Point Index must be set to a point offset that is divisible by 8.  |
| Standard DNP3 Point                 | UINT = 2 INT = 3 OSTR = 5 BSTR = 6 TIME = 7 | 0 0, 1, 2, or 4 0, 1, 2, or 4 0…255 0…255 0…6 | CI= 20: Counter                        | 0…511 max                                                                                                                                |                                                                                                                                          |
| Standard DNP3 Point                 | UINT = 2 INT = 3 OSTR = 5 BSTR = 6 TIME = 7 | 0 0, 1, 2, or 4 0, 1, 2, or 4 0…255 0…255 0…6 | AI= 30: Analog input                   | 0…767 max                                                                                                                                |                                                                                                                                          |
| Standard DNP3 Point                 | UINT = 2 INT = 3 OSTR = 5 BSTR = 6 TIME = 7 | 0 0, 1, 2, or 4 0, 1, 2, or 4 0…255 0…255 0…6 | BCD= 101: BCD point                    | 0…255 max                                                                                                                                |                                                                                                                                          |

Table 32 - Point Address Type — MicroLogix Data File

| Point Address Type Data Type Code   | Maximum Data Length (bytes)   |                                          |                              | File Number File Element File Sub-element   |
|-------------------------------------|-------------------------------|------------------------------------------|------------------------------|---------------------------------------------|
| MicroLogix Data File                |                               |                                          | NONE = 0 0 0 0 0             |                                             |
| MicroLogix Data File                |                               | VSTR = 1 0…82 9…255 (ST) 9…255 0…40      |                              |                                             |
| MicroLogix Data File                | UINT = 2 0, 1, 2, or 4        | 2(S) 3, 9…255 (B) 7, 9…255 (N) 9…255 (L) | 0…65 for S 0…255 for B, N, L | 0 for S, N, L 0…15 for B                    |
| MicroLogix Data File                | INT = 3 0, 1, 2, or 4         | 2(S) 3, 9…255 (B) 7, 9…255 (N) 9…255 (L) | 0…65 for S 0…255 for B, N, L | 0 for S, N, L 0…15 for B                    |
| MicroLogix Data File                |                               | FLT = 4 0 or 4 8, 9…255 (F) 0…255 0      |                              |                                             |
| MicroLogix Data File                | OSTR = 5 0…255                | 2(S) 3, 9…255 (B) 7, 9…255 (N)           | 0…65 for S 0…255 for B, N,   | 0 for S, N 0…15 for B                       |
|                                     | BSTR = 6 0…255                | 2(S) 3, 9…255 (B) 7, 9…255 (N)           | 0…65 for S 0…255 for B, N,   | 0 for S, N 0…15 for B                       |

Table 32 - Point Address Type — MicroLogix Data File (Continued)

| Point Address Type Data Type Code   | Maximum Data Length (bytes)   |                                          |                              | File Number File Element File Sub-element   |
|-------------------------------------|-------------------------------|------------------------------------------|------------------------------|---------------------------------------------|
| TIME = 7 0…6                        |                               | 2(S) 3, 9…255 (B) 7, 9…255 (N) 9…255 (L) | 0…65 for S 0…255 for B, N, L | 0 for S, N, L 0…15 for B                    |

When the Descriptor Code is selected as PTYP, the Point Addressing parameters for the Descriptor element are replaced by 10 Point Addressing parameters. Configure the Descriptor elements in the same order of the DAEL elements in the relevant Prototypes.

<!-- image -->

For instance, if Prototype 0 includes a Namespace at Index 2 and Name at Index 3, then the first DAEL in the Prototype 0 is at Index 4. The Prototype DAEL at Index 4 matches Point Address 4 in the PTYP element configuration. Because of this, Point Address 4 in the PTYP element configuration of the Descriptor should be configured properly.

<!-- image -->

<!-- image -->

## Object Quality Flags

The object flag is composed of an 8-bit string for some DNP3 objects. Table 33 to Table 40 show Flag Descriptions for each object. The ONLINE, RESTART, COMM\_LOST, REMOTE\_FORCED and LOCAL\_FORCED flags are common to all object group types that contain flags.

There are some rules for the Object flag set or clear for each bit by the controller. The rules are also applied to Event data.

- When the controller is in Non-executing mode, the object flag is always all 0.
- When the controller is in Executing mode and there is no configuration file, only the Online flag in the object flag is set.
- When the controller is in Executing mode and there is a configuration file, the flags in the object flag are set according to the upper byte of the configuration file.

Table 33 - Object Flags for Binary Input

| Bit Offset Name Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE In Series A controllers: 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode. In Series B and Series C controllers: 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is or was in Executing mode and the configuration file exists. |
| 1 RESTART Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2 COMM_LOST Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3 REMOTE_FORCED Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                               |
| 4 LOCAL_FORCED Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                |
| 5 CHATTER_FILTER Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                              |
| 6 reserved Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                    |
| 7 STATE Reflects point state of Binary Input point.                                                                                                                                                                                                                                                                                                                                                                               |

## Table 34 - Object Flags for Double Binary Input

| Bit Offset Name Description                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE In Series A controllers: 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode. In Series B and Series C controllers: 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is or was in Executing mode and the configuration file exists. |
| 1 RESTART Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2 COMM_LOST Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3 REMOTE_FORCED Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                               |
| 4 LOCAL_FORCED Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                                |
| 5 CHATTER_FILTER Always 0. Not used.                                                                                                                                                                                                                                                                                                                                                                                              |
| 6 STATE Reflects point state of Double-bit Binary Input point. Double-bit LSB.                                                                                                                                                                                                                                                                                                                                                    |
| 7 STATE Reflects point state of Double-bit Binary Input point. Double-bit MSB                                                                                                                                                                                                                                                                                                                                                     |

## Table 35 - Object Flags for Binary Output

| Bit Offset Name Description                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 1 RESTART Always 0. Not used.                                                                                                                                                                                                                     |
| 2 COMM_LOST Always 0. Not used.                                                                                                                                                                                                                   |
| 3 REMOTE_FORCED Always 0. Not used.                                                                                                                                                                                                               |
| 4 LOCAL_FORCED Always 0. Not used.                                                                                                                                                                                                                |
| 5 reserved Always 0. Not used.                                                                                                                                                                                                                    |
| 6 reserved Always 0. Not used.                                                                                                                                                                                                                    |
| 7 STATE Reflects point state of Binary Output point.                                                                                                                                                                                              |

## Table 36 - Object Flags for Counter

|                 | Bit Offset Name Description                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE        | 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 1 RESTART       | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 2 COMM_LOST     | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 3 REMOTE_FORCED | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 4 LOCAL_FORCED  | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 5 ROLLOVER      | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 6 DISCONTINUITY | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 7 reserved      | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |

## Table 37 - Object Flags for Analog Input

|                 | Bit Offset Name Description                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE        | 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 1 RESTART       | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 2 COMM_LOST     | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 3 REMOTE_FORCED | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 4 LOCAL_FORCED  | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 5 OVER_RANGE    | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 6 REFERENCE_ERR | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 7 reserved      | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |

Table 38 - Object Flags for Analog Output

| Bit Offset Name Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE  0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode. |
| 1 RESTART Always 0. Not used.                                                                                       |
| 2 COMM_LOST Always 0. Not used.                                                                                     |
| 3 REMOTE_FORCED Always 0. Not used.                                                                                 |
| 4 LOCAL_FORCED Always 0. Not used.                                                                                  |
| 5 reserved Always 0. Not used.                                                                                      |
| 6 reserved Always 0. Not used.                                                                                      |
| 7 reserved Always 0. Not used.                                                                                      |

Table 39 - Object Flags for Analog Output for Series A controllers

| Bit Offset Name Description                                                                                         |
|---------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE  0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode. |
| 1 RESTART Always 0. Not used.                                                                                       |
| 2 COMM_LOST Always 0. Not used.                                                                                     |
| 3 REMOTE_FORCED Always 0. Not used.                                                                                 |
| 4 LOCAL_FORCED Always 0. Not used.                                                                                  |
| 5 reserved Always 0. Not used.                                                                                      |
| 6 reserved Always 0. Not used.                                                                                      |
| 7 reserved Always 0. Not used.                                                                                      |

Table 40 - Object Flags for Analog Output for Series B and Series C controllers

|                 | Bit Offset Name Description                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 ONLINE        | 0 when the controller is or was in Non-executing mode. 1 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 1 RESTART       | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 2 COMM_LOST     | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 3 REMOTE_FORCED | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 4 LOCAL_FORCED  | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 5 reserved      | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 6 reserved      | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |
| 7 reserved      | 0 when the controller is or was in Non-executing mode. 0 when the controller is or was in Executing mode and the configuration file does not exist. May be 1 when the controller is in Executing mode and the configuration file exists. |

## DNP3 Device Attribute Object

The Device Attribute object can be used to identify DNP3 Slave devices. With the controller, some of the variations are written so that you can read or write your own strings in your application.

The object group of the Device Attribute object is 0. The supported range of the variation is 211…255.

The R/W property shows if the object is Read Only, Read, or Write. If the R/W property is writable, the value that is written by the DNP3 master device is stored to nonvolatile memory.

The object group of the Device Attribute is 0. The supported range of the variation is 211…255.

## Object Group 0, Variations for Attribute Set 0

| Variation Read/write  Attribute Data Type   | Length in Bytes (Series A)   | Max Length in Bytes (Series B and Series C)                         | Description Value (Series A) Value (Series B)                                                                                                                                                                                      |                                                                                       |
|---------------------------------------------|------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| 211 Read Only VSTR 27 0 for DNP3            |                              | Identifier of support for user specific attributes                                                                     | Returns the identifier for user specific attributes. Rockwell Automation, Inc., 1                                                                                                                                                                                                                                    | Returns the identifier for user-specific attributes. "", NULL for DNP3.               |
| 212 Read Only UINT 4 2                      |                              | Number of master-defined Data Set prototypes                                                                     | 0 0                                                                                                                                                                                                                                |                                                                                       |
| 213 Read Only UINT 4 2                      |                              | Number of outstation-defined Data-Set prototypes                    | 0                                                                                                                                                                                                                                  | The configured number in the DNP3 Slave Application Layer Configuration file. 10, max |
| 214 Read Only UINT 4 2                      |                              | Number of master-defined Data Sets                                                                     |                                                                                                                                                                                                                                    | 0 0                                                                                   |
| 215 Read Only UINT 4 2                      |                              | Number of outstation-defined Data-Sets                              | 0                                                                                                                                                                                                                                  | The configured number in the DNP3 Slave Application Layer Configuration file. 10, max |
| 216 Read Only UINT 4 2                      |                              | Max number of binary outputs per request                            | 10 10                                                                                                                                                                                                                              |                                                                                       |
|                                             |                              | 217 Read Only UINT 4 2 Local timing accuracy 10,000 in microseconds |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 218 Read Only UINT 4 2 Duration of timing accuracy 0 in seconds     |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 219 Read Only INT 1 1 Support for analog output events 0 0          |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 220 Read Only UINT 4 2 Max analog output index 256*3                |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 221 Read Only UINT 4 2 Number of analog outputs 0…256*3             |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 222 Read Only INT 1 1 Support for binary output events 0            |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 223 Read Only UINT 4 2 Max binary output index 256*16               |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 224 Read Only UINT 4 2 Number of binary outputs 0…256*16            |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 225 Read Only INT 1 1 Support for frozen counter events 1           |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 226 Read Only INT 1 1 Support for frozen counters 1                 |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 227 Read Only INT 1 1 Support for counter events 1                  |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 228 Read Only UINT 4 2 Max counter index 256*2                      |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 229 Read Only UINT 4 2 Number of counter points 0…256*2             |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 230 Read Only INT 1 1 Support for frozen analog inputs 0            |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 231 Read Only INT 1 1 Support for analog input events 1             |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 232 Read Only UINT 4 2 Maximum analog input index 256*3             |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 233 Read Only UINT 4 2 Number of analog input points 0…256*3        |                                                                                                                                                                                                                                    |                                                                                       |
| 234 Read Only INT 1 1                       |                              | Support for double-bit binary input events                          | 1                                                                                                                                                                                                                                  |                                                                                       |
| 235 Read Only UINT 4 2                      |                              | Maximum double-bit binary input index                               | 256*8                                                                                                                                                                                                                              |                                                                                       |
| 236 Read Only UINT 4 2                      |                              | Number of double-bit binary input points                            | 0…256*8                                                                                                                                                                                                                            |                                                                                       |
|                                             |                              | 237 Read Only INT 1 1 Support for binary input events 1             |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 238 Read Only UINT 4 2 Max binary input index 256*16                |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 239 Read Only UINT 4 2 Number of binary input points 0…256*16       |                                                                                                                                                                                                                                    |                                                                                       |
|                                             |                              | 240 Read Only UINT 4 2 Max transmit fragment size                   | 2048 (27…2048). When this value is written to the controller, the communication configuration file is changed to this value.                                                                                                       |                                                                                       |
|                                             |                              | 241 Read Only UINT 4 2 Max receive fragment size 2048               |                                                                                                                                                                                                                                    |                                                                                       |
| 242 Read Only VSTR                          | length of the string value   | length of the string value Device manufacturer's software version   | This variation returns firmware FRN. FRN 1.00. Supported ranges: FRN x.yy, FRN x.yyy, FRN xx.yy, or FRN xx.yyy where x, xx is 0 ~ 99 and yy, yyy 00 ~ 999. For example, FRN 1.00, FRN 1.05, FRN 12.05, FRN 102.27, or FRN 103.117. |                                                                                       |

## Object Group 0, Variations for Attribute Set 0 (Continued)

| Variation Read/write  Attribute Data Type   | Length in Bytes (Series A)                | Max Length in Bytes (Series B and Series C)   |                                                         | Description Value (Series A) Value (Series B)                                                                                                                                                      |                                                                                                                                                                                                    |
|---------------------------------------------|-------------------------------------------|-----------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 243 Read Only VSTR                          | length of the string value                | length of the string value                    | Device manufacturer's hardware version                  | This variation returns the hardware series and revision of the controller. HW SER A/REV 01.                                                                                                        | This variation returns the hardware series and revision of the controller. HW SER A/REV 03.                                                                                                        |
| 243 Read Only VSTR                          | length of the string value                | length of the string value                    | Device manufacturer's hardware version                  | Supported ranges: HW SER x/REV yy where x is A ~ F and yy is 00 ~ 31. For example, HW SER A/REV 01, HW SER B/REV 03, or HW SER C/REV 31.                                                           | Supported ranges: HW SER x/REV yy where x is A ~ F and yy is 00 ~ 31. For example, HW SER A/REV 01, HW SER B/REV 03, or HW SER C/REV 31.                                                           |
|                                             |                                           |                                               | 244 - - - - Reserved for future assignment - -          |                                                                                                                                                                                                    |                                                                                                                                                                                                    |
| 245 Read/write VSTR                         | length of the string value, max 255 bytes | length of the string value, max 255 bytes     | User-assigned location name "". Non-NULL ended.         |                                                                                                                                                                                                    |                                                                                                                                                                                                    |
| 246 Read/write VSTR                         | length of the string value, max 255 bytes | length of the string value, max 255 bytes     | User-assigned ID code/number "". Non-NULL ended.        |                                                                                                                                                                                                    |                                                                                                                                                                                                    |
| 247 Read/write VSTR                         | length of the string value, max 255 bytes | length of the string value, max 255 bytes     | User-assigned device name "". Non-NULL ended.           |                                                                                                                                                                                                    |                                                                                                                                                                                                    |
|                                             |                                           |                                               |                                                         | 248 Read Only VSTR 12 12 Device serial number This variation returns Ethernet MAC ID. 0000BCxxxxxx.                                                                                                | 248 Read Only VSTR 12 12 Device serial number This variation returns Ethernet MAC ID. 0000BCxxxxxx.                                                                                                |
|                                             |                                           |                                               | 249 Read Only VSTR 6 6 DNP subset and conformance       | This variation returns the Subset level and Test procedure version. 2:2008.                                                                                                                        | This variation returns the Subset level and Test procedure version. 2:2009.                                                                                                                        |
| 250 Read Only VSTR                          | length of the string value                | length of the string value                    | Device manufacturer's product name and model            | This variation returns the Catalog Number and OS Series of the controller. 1766-L32BWA SER A.                                                                                                      | This variation returns the Catalog Number and OS Series of the controller. 1766-L32BWA SER B.                                                                                                      |
| 250 Read Only VSTR                          | length of the string value                | length of the string value                    | Device manufacturer's product name and model            | Supported ranges: 1766-L32xxxa SER y where xxxa is BWA, AWA, BXB, BWAA, AWAA, or BXBA and y is A ~ F. For example, 1766-L32BWA SER A, 1766-L32AWA SER B, 1766-L32BXB SER C, or 1766-L32BWAA SER A. | Supported ranges: 1766-L32xxxa SER y where xxxa is BWA, AWA, BXB, BWAA, AWAA, or BXBA and y is A ~ F. For example, 1766-L32BWA SER A, 1766-L32AWA SER B, 1766-L32BXB SER C, or 1766-L32BWAA SER A. |
|                                             |                                           |                                               | 251 - - - - Reserved for future assignment - -          |                                                                                                                                                                                                    |                                                                                                                                                                                                    |
|                                             |                                           |                                               | 252 Read Only VSTR 13 19 Device manufacturer's name     | This variation returns the Company name. Allen-Bradley.                                                                                                                                            | This variation returns the Company name. Rockwell Automation for DNP3.                                                                                                                             |
|                                             |                                           |                                               | 253 Read Only - - - Reserved for future assignment - -  |                                                                                                                                                                                                    |                                                                                                                                                                                                    |
|                                             |                                           |                                               | 254 Read Only - - - Non-specific all attributes request | This variable returns all variations in this group except this variation.                                                                                                                          | This variable returns all variations in this group except this variation.                                                                                                                          |
|                                             |                                           |                                               | 255 Read Only - - - List of attribute variations        | This variation returns the R/W property for each variation. From g0v211…g0v253. 0 for Read Only 1 for Read or Write                                                                                | This variation returns the R/W property for each variation. From g0v211…g0v253. 0 for Read Only 1 for Read or Write                                                                                |

## Event Reporting

This section covers how to generate DNP3 events from DNP3 Data Objects and how to report the generated events by polled response or unsolicited response.

## Generate Events

The controller has a separate buffer area that you can use to log DNP3 events internally.

The maximum number of the Events that can be logged is 6013 or 10000 (see DNP3 10K Event Logging on page 237), regardless of the Event data type. With Series B and Series C controllers, a Data-Set event can consume multiple numbers of the event buffers.

If the number of the generated events reaches this value, the controller sets IIN2.3 [EVENT\_BUFFER\_OVERFLOW]. Further events are not logged until the logged events are reported to DNP3 Master and the buffer is available.

The elements CS0:67 or CS2:67 in the Communication status file show how many events are logged to the event buffer. The logged events are not removed until they are reported to DNP3 Master successfully. Logged event can also be cleared when one of the following events occurs:

- New OS firmware update
- New user program download

Figure 79 shows how to generate events for a Binary Input Object and a 16-bit Analog Input Object. In the DNP3 Slave configuration, the Binary Input Object Data File Number is configured to 10 and its Configuration File Number is configured to 30. 16-bit Analog Input Object Data File Number is configured to 14 and its Configuration File Number is configured to 36.

Figure 79 - Generate Events for Binary Input Object

<!-- image -->

Four files are generated automatically in the tree list of the Data Files.

<!-- image -->

You must adjust the number of the elements for each file according to your application. In this example, the number of the elements is 10 for Binary Input Object File and 10 for 16-bit Analog Input Object File.

In the Binary Input Config File, the bit 1/bit 0 of B30:0, B30:1 and B30:2 are configured to 0/1, 1/0 and 1/1 respectively. The event for the index 0…15 of Binary Input Object are generated as a Class 1 event, the event for the index 16…31, as a Class 2 event and the event for the index 32…47, as a

Class 3 event, if there are any changes for the points (B10:0, B10:1 or B10:2). For any other Binary Input points, the events are not generated.

<!-- image -->

<!-- image -->

In the same manner, this 16-bit Analog Input Object File has bit 1/bit 0 of B36:0, B36:1 and B36:2 configured to 0/1, 1/0 and 1/1 respectively. The event for the index 0 of 16-bit Analog Input Object is generated as a Class 1 event, the event for the index 1 as a Class 2 event, and the event for the index 2 as a Class 3 event, if there are any changes for the points (N14:0, N14:1 or N14:2). For any other 16-bit Analog Input points, the events will not be generated.

?

<!-- image -->

## DNP3 10K Event Logging

The number of events that are logged can be increased from 6013…10000 by using the memory space of Recipe and Data log. A status bit S:36/11 is used to differentiate between the two DNP3 configurations on controller power-up. When the downloaded user program has the S:36/11 bit set, on the next power cycle, the 10,000 event configuration is loaded. Similarly, if the downloaded user program has the S:36/11 bit reset to zero, on the next power cycle, the 6013 event logging configuration is loaded.

<!-- image -->

When the controller is configured for 10,000 events logging, Recipe and/or Data Logging operations are not allowed. If the user program has either of the two configurations (DLG and/or RCP) when 10000 DNP3 event logging is enabled, the controller enters a fault state (0x2A) when switching from Program to Run mode.

Table 41 - Data File List

|                                                            | Name Number Type Scope Debug Words Elements Last   |
|------------------------------------------------------------|----------------------------------------------------|
|                                                            | Output 0 O Global No 18 6 O:5                      |
|                                                            | Input 1 I Global No 24 8 I:7                       |
|                                                            | Status 2 S Global No 0 66 S:65                     |
|                                                            | Binary 3 B Global No 1 1 B3:0                      |
|                                                            | Timer 4 T Global No 3 1 T4:0                       |
| Counter 5 C Global No 3 1 C5:0                             |                                                    |
| Control 6 R Global No 3 1 R6:0                             |                                                    |
| Integer 7 N Global No 1 1 N7:0                             |                                                    |
|                                                            | Float 8 F Global No 2 1 F8:0                       |
| 16-bit Analog Input Object File 11 N Global No 10 10 N11:9 |                                                    |
| Binary Output Object File 12 B Global No 10 10 B12:0       |                                                    |
| 16-bit Analog Input Config File 21 B Global No 10 10 B21:9 |                                                    |
| A16I OLD 30 N Global No 10 10 N30:9                        |                                                    |
| A16I DEADB 31 N Global No 10 10 N31:9                      |                                                    |
| A16I Temp 32 N Global No 10 10 N32:9                       |                                                    |

When there is a change in configuration either from 6013…10000 event logs or from 10000…6013 event logs in the last downloaded user program, a power cycle is needed to apply the configuration, without which the controller enters a fault state (0x2B) when switched to Run mode.

The s:36/11 bit has to be set to one or zero in the user program before downloading. This bit is readonly when the controller is in Program or Run mode.

## Control Generating Event

The controller checks all elements in the Object Data file for changes at the end of a scan and generates events where needed.

The key method to turn on and off event generating by ladder logic is to assign or unassign the Class information bits in the Object Config Files.

The following example shows how to control the event generation condition by ladder logic and implements Deadband for Analog Input Objects (which is only necessary for MicroLogix 1400 Series A).

In this example, for 16-bit Analog Input point 0 (N11:0), if the absolute value of the difference between the present value of N11:0 and the value that was most recently queued as an event for that point exceeds the deadband value, then an event is generated for that point.

---TotalRungsin File=3

<!-- image -->

In MicroLogix 1400 Series B and Series C controllers, new configuration files are defined for the Deadband for Analog Input Objects and the Threshold for Counter Objects. The feature of the configuration files replaces the ladder program in this section.

## Report Event By Polled Response

When a DNP3 Master sends a poll to read Class events, any events that are logged to the event buffer are reported in the polled response.

When using both Channel 0 and Channel 2 Serial ports for DNP3 communication, event polling requests should be sent to one Channel at a time. This avoids mis-reporting of events to different DNP3 masters on different Channels. For example, Master A and Master B are connected to Channel 0 and Channel 2 respectively, and 5000 events are logged in the event buffer. Master A sends an event polling request, and only 50 events can be fit in an application layer fragment. The first 50 events are sent to Master A and the next 50 events can be sent to Master B instead.

## Report Event By Unsolicited Response

To initiate and send Unsolicited Responses to a DNP3 Master, the following parameters should be configured correctly. For more details, see DNP3 Slave Application Layer Configuration Parameters on page 189 .

- Master Node 0
- Channel for Unsolicited Response
- Enable Unsolicited On Start Up
- Enable Unsolicited For Class1
- Enable Unsolicited For Class2
- Enable Unsolicited For Class3
- Send Initial Unsolicited On Start Up

- Number of Class1 Events
- Hold Time after Class1 Events (x1s)
- Number of Class2 Events
- Hold Time after Class2 Events (x1s)
- Number of Class3 Events
- Hold Time after Class3 Events (x1s)
- DNP3 Object Data File Number
- DNP3 Object Config File Number
- content of the Config File

In some cases, the controller does not send an Unsolicited Response even though the parameters are configured properly.

- Normally, when the parameter Enable Unsolicited On Start Up is checked, the controller initiates an Unsolicited Response with the function code ENABLE\_UNSOLICITED(20), if there are any events that are logged into the event buffer. However, when a request with the function code DISABLE\_UNSOLICITED(21) is received, an Unsolicited Response will not be sent.
- When the parameter Enable Unsolicited On Start Up is unchecked, the controller does not trigger the Unsolicited Response until a request with the function code ENABLE\_UNSOLICITED(20) from the DNP3 Master is received.

Figure 80 shows how to initiate and send the Unsolicited Response. Master Node 0 in Channel 0 Configuration tab indicates that the Unsolicited Response is reported to the Master with the node address 3.

Figure 80 - Initiate and Send an Unsolicited Response

<!-- image -->

The parameter Channel for Unsolicited Response in the DNP3 Slave Configuration tab indicates that the Unsolicited Response is reported via Channel 0 only. In this example, an Initial Unsolicited Response is sent on startup and all events of class 1, 2 and 3 are reported. Since Hold Times are configured to 5 seconds, generated events are reported after 5 seconds.

## Collision Avoidance

## Time Synchronization

<!-- image -->

The controller currently supports the first of the two methods for collision avoidance.

- Detecting transmitted data (TX/RX line on RS-485 communication).
- Detecting out-of-band carrier (DCD on RS-232C communication).

When the controller is connected to the RS-485 network, it monitors all data on the link. If the controller is preparing to transmit a packet and finds the link busy, it waits for an interval that is defined by the Backoff\_Time until it is no longer busy.

Backoff\_Time = Pre Transmit Delay (x1 ms) + Max Random Delay (x1 ms)

The Pre Transmit Delay (x1 ms) in the Link Layer Channel Configuration file is a fixed delay and the Max Random Delay (x1 ms) in the Channel Configuration file is a maximum random delay for Channel 0 and Channel 2. You must specify those parameters to get the collision avoidance mechanism.

After the Backoff\_Time, the controller tries again, either indefinitely, or up to a configurable maximum number of retries. If a maximum is used, the protocol considers this as a link failure.

An RTC Function file updates the time value in the embedded RTC module of the controller every 2 seconds. This resolution is insufficient to log DNP3 events in a DNP3 subsystem. Another timer, incremented by 1 millisecond in the DNP3 Slave subsystem, serves to provide appropriate resolution.

These two timers are synchronized by the following conditions:

- power up
- a request for time synchronization from DNP3 Master.

At power-up, the DNP3 subsystem gets the time from an RTC function file in the controller. For the RTC function file to acquire the correct time, the RTC module should be enabled before a power cycle to acquire the correct time from the RTC function file.

## Download a User Program Via DNP3 Network

In this example RTC function file, the RTC module is disabled. To enable it, select Set Date &amp; Time while it is online.

<!-- image -->

When there is a write request for time synchronization from a DNP3 Master, the DNP3 subsystem synchronizes its timer with the time from DNP3 Master and the time in the RTC module is synchronized with the time from DNP3 Master.

This table shows RTC Accuracy. Configure the NEED\_TIME IIN bit according to this table, so that a DNP3 Master can send the time synchronization request for more accurate times in the controller.

## RTC Accuracy

<!-- image -->

| Ambient Temperature  RTC Accuracy(1)    |
|-----------------------------------------|
| 0 °C (32 °F) -13...-121 seconds/month   |
| 25 °C (77 °F) 54...-5 seconds/month     |
| 40 °C (104 °F) 29...-78 seconds/month   |
| 55 °C (131 °F) -43...-150 seconds/month |

- (1) These numbers are maximum worst case values over a 31-day month.

Using File-Control/Status of Requested Operation objects, a user program can be downloaded/ uploaded/initialized via DNP3 communication. Also, Serial Channel 0 Status File, Ethernet Channel 1 Status File, and Serial Channel 2 Status File can be uploaded from the controller.

All File-Control/Status of Requested Operation objects and supported File-Control/Status of Requested Operation objects are methods that are listed in this section. Unsolicited Response for File-Control/Status of Requested Operation objects is not supported. All responses are sent to DNP3 Master with81 h81h).

- g70v1 File-Control – File identifier: superseded, not supported
- g70v2 File-Control – Authentication: supported
- g70v3 File-Control – File command: supported
- g70v4 File-Control – File command status: supported
- g70v5 File-Control – File transport: supported
- g70v6 File-Control – File transport status: supported
- g70v7 File-Control – File descriptor: supported
- g70v8 File-Control – File specification string: not supported by Series A controllers, supported by Series B and Series C controllers
- g91v1 Status of Requested Operation – Activate configuration: not supported by Series A controllers, supported by Series B and Series C controllers

## Default Directories and Files

The controller has default directories and files for file handling in a DNP3 subsystem.

The default directories and files can be read from the controller using the function code OPEN\_FILE(25), Read(1), and CLOSE\_FILE(26).

Currently supported directories are /EXE and /DIAG. Supported files are listed in this section. These directories/files cannot be removed and cannot be created using DNP3 requests.

Table 42 - Supported Files and Directories

| Root Level Directory Level File Level Full Name String to Access   |
|--------------------------------------------------------------------|
| / /                                                                |
| EXE /EXE                                                           |
| [processorName].IMG /EXE/[processorName].IMG                       |
| DIAG /DIAG                                                         |
| CH0.CSF /DIAG/CH0.CSF                                              |
| CH1.ESF /DIAG/CH1.ESF                                              |
| CH2.CSF /DIAG/CH2.CSF                                              |

- The directory/file names must all be in capital letters.
- Root level can only be a directory marker. The directory marker is / for Series A, or \ for Series B and Series C.
- Directory level can only contain directories.
- File level can only contain files.

The directory marker is different in MicroLogix 1400 Series A and Series B and Series C controllers. The directory marker is / for Series A and \ for Series B and Series C controllers. In this document, / is used to explain the File Object feature.

## Generate *.IMG files using RSLogix 500/RSLogix Micro

Typically, RSLogix 500/RSLogix Micro stores the ladder program as RSLogix™ Files (*.RSS). However, to download a ladder program using a File Object via the DNP3 network, you must save your ladder program in the RSLogix IMG Files (*.IMG) format.

After you write your ladder program, select Save As … from the File menu of the RSLogix 500/ RSLogix Micro software. Select the save type as RSLogix IMG Files (*.IMG).

<!-- image -->

After saving the file, you can see the file ML1400A\_DNP3S.IMG. Use this file for download.

<!-- image -->

## IMPORTANT

RSLogix 500/RSLogix Micro v8.10.00 and MicroLogix 1400 Series A controllers do not support the opening of *.IMG files. Be sure to store your ladder program in the RSLogix Files (*.RSS) format before generating RSLogix IMG Files (*.IMG). Otherwise, you could lose the latest modifications to your ladder program.

## IMPORTANT

RSLogix 500/RSLogix Micro v8.30.00 and MicroLogix 1400 Series B and Series C controllers support the opening of *.IMG files. However, some information is not stored into the IMG file, for example, rung comments. Be sure to store your ladder program in the RSLogix Files (*.RSS) format before generating RSLogix IMG Files (*.IMG).

## Rules for File Authentication

The File Authentication process is optional, and unnecessary when the master password of the downloaded ladder program is not configured.

Note: There is no master password for the ML1400 Series B (Enhanced Password Security) program, so the file authentication process does not apply for ML1400 Series B (Enhanced Password Security). If you need file security, we recommend turning on the DNP3 authentication feature.

When RSLogix 500/RSLogix Micro configure the password in the ladder program, the DNP3 master sends a request with the function code AUTHENTICATE\_FILE (29) to authenticate permission before file operation.

The object g70v2 is used for File Authentication, with two parameters:

- Username — from the Processor Name in the Controller Properties dialog in RSLogix 500/ RSLogix Micro
- Password — from the Master Password in the Controller Properties dialog in RSLogix 500/ RSLogix Micro.

In the example , Username is DNP3\_A and Password is 12345(*****).

<!-- image -->

Once the DNP3 Master receives a proper Authentication Key (nonzero value) from the controller, the the Authentication Key must be used for sending the request with the function code OPEN\_FILE(25) or DELETE\_FILE(27).

<!-- image -->

## Rules for Downloading a User Program

A DNP3 master should send the function code OPEN\_FILE(25), WRITE(2), and the CLOSE\_FILE(26) to download user programs.

When a master sends the function code OPEN\_FILE(25) with the file command object, the file name string in the File command object must be in this directory and the file name format:

- /EXE/[processorName].IMG

The directory and file name extension string must all be in capital letters and the string size cannot exceed 64 bytes. The file name [processorName] is from the Processor Name in the Controller Properties dialog in RSLogix 500/RSLogix Micro.

This ladder program [processorName].IMG is generated from RSLogix 500/RSLogix Micro. The DNP3 master should send the [processorName].IMG file without any modification.

When the MicroLogix 1400 Series A controller receives a request with the function code WRITE(2) for User Program download, the controller activates all configurations and channel configurations after the last application file segment is received. For the MicroLogix 1400 Series B and Series C controller, the function code Activate Configuration (0x1F) is supported.

Unlike the Series A controller, the MicroLogix 1400 Series B and Series C controller does not activate all configurations and channel configurations after the last application file segment is received. To activate all configurations, you must send a command with the function code, Activate Configuration (0x1F) after downloading the user program.

The maximum file size is 384 Kbytes. The controller supports downloading up to 256 Kbyte size of user program when Recipe is not configured. When Recipe is configured, the Maximum file size is 384 Kbytes.

The first application segment of the ladder program should be larger than or equal to the size of the System Exe File structure, 64 bytes.

An application segment of the ladder program cannot exceed 2048 bytes.

When the controller receives the first application segment, it acquires Edit Resource from the system. If the last application segment is received properly, the controller returns Edit Resource to the system. After acquiring Edit Resource, each of the application segments should be received within the Edit Resource/Owner Timeout.

The controller checks the integrity of the program after receiving the last application segment. If the downloaded user program fails the integrity check, the controller clears the downloaded user

program and restores the default user program. In this case, the configured Channel configuration is not changed from the last valid configuration.

A user program cannot be downloaded while the controller is in Executing mode. Before downloading, send a mode change request with the function code STOP\_APPL(18). See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 for more details.

Executing modes include Run, Remote Run, Test Continuous Scan, and Test Single Scan modes. Any others are Non-executing modes.

## Rules for Uploading a User Program

A DNP3 master should send the function code OPEN\_FILE(25), READ(1), and CLOSE\_FILE(26) for uploading user programs.

When a master sends the function code OPEN\_FILE(25) with the file command object, the file name string in the File command object must be in this directory and the file name format:

- /EXE/[processorName].IMG

The directory and file name extension string must all be in capital letters and the string size cannot exceed 64 bytes. The file name [processorName] is from the Processor Name in the Controller Properties dialog in RSLogix 500/RSLogix Micro.

The maximum file size is 384 Kbytes. The controller supports uploading of user programs up to 256 Kbyte in size when Recipe is not configured. When Recipe is configured, the Maximum file size is 384 Kbytes.

The first application segment of the ladder program should be larger than or equal to the size of the System Exe File structure, 64 bytes.

An application segment of the ladder program cannot exceed 2048 bytes.

## Rules for Initializing a User Program

A DNP3 master should send the function code DELETE\_FILE(27) for initializing user programs.

When the controller receives a request with the function code DELETE\_FILE(27), it clears the current user program that is downloaded into the controller, and restores the default user program.

User programs cannot be initialized while the controller is in Executing mode. Before initializing programs, a mode change request should be sent with the function code STOP\_APPL(18).

## Rules for uploading Communication Status Files

A DNP3 master should send the function code OPEN\_FILE(25), READ(1), and CLOSE\_FILE(26) for uploading Communication Status Files.

The function code WRITE(2) for downloading Communication Status Files is not supported.

The file name should be /DIAG/CH0.CSF, /DIAG/CH1.ESF, and /DIAG/CH2.CSF for Channel 0, Channel 1, and Channel 2 respectively.

## Start and Stop User Programs (Mode Change) Via DNP3 Network

This section covers how to change the controller mode via the DNP3 network.

To change the controller mode, use the function codes FC\_INITIALIZE\_APPL (16), FC\_START\_APPL (17), and FC\_STOP\_APPL (18).

## Diagnostics

If the qualifier code is 5Bh, the Application Identifier Object should be used. The Application Identifier is a string that cannot exceed 10 bytes. The string of Application Identifier is taken from the name in the Properties of the ladder file #2 in RSLogix 500/RSLogix Micro. In this example, the Application Identifier is DNP3\_TASK.

<!-- image -->

If the qualifier code is 06h, the controller does not check the string of the Application Identifier.

## Initialize User Program

If the controller receives the function code FC\_INITIALIZE\_APPL (16) with the object Application Identifier (g90v1), it changes mode to Remote Program. If the controller is in a fault mode, the controller clears the fault before changing the mode to Remote Program.

## Start User Program

If the controller receives the function code FC\_START\_APPL (17) with the object Application Identifier (g90v1), it changes its mode to Remote Run. If the controller is in a fault mode, it sends the command with the function code FC\_INITIALIZE\_APPL (16) before the command with the function code FC\_START\_APPL (17).

## Stop User Program

If the controller receives the function code FC\_STOP\_APPL (18) with the object Application Identifier (g90v1), it changes its mode to Remote Program. If the controller is in a fault mode, it sends the command with the function code FC\_INITIALIZE\_APPL (16) before sending the command with the function code FC\_STOP\_APPL (18).

Errors in a DNP3 Slave subsystem are logged in the Communication Status File. There are 71 words for the troubleshooting.

This section shows the 71 words of the communication status file for each Channel 0 or Channel 2 port.

Table 43 - Communication Status File Words

| Words Offset File/Element Description for Channel 0 File/Element Description for Channel 2   | Description                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                              | 0 CS0:0 CS2:0 General Status Category Block ID                                                                                                                                                                                                               |
|                                                                                              | 1 CS0:1 CS2:1 Length – 8 bytes (4 words including format code)                                                                                                                                                                                               |
|                                                                                              | 2 CS0:2 CS2:2 Format Code – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 3 CS0:3 CS2:3 Communications Configuration Error Code                                                                                                                                                                                                        |
| 4 CS0:4 CS2:4                                                                                | bit 15: Reserved – Always 0 bit 14: Modem Lost Bit bits 5…13: Reserved – Always 0 bit 4: Communications Active Bit bit 3: Selection Status Bit bit 2: Outgoing Message Command Pending bit 1: Incoming Message Reply Pending bit 0: Incoming Command Pending |
| 5 CS0:5 CS2:5                                                                                | bits 8…15: Communication rate that the selected link layer driver is operating at out communication channel. bits 0…7: Node Address                                                                                                                          |
|                                                                                              | 6 CS0:6 CS2:6 Diagnostic Counters Category Identifier                                                                                                                                                                                                        |
| 7 CS0:7 CS2:7 Length                                                                         |                                                                                                                                                                                                                                                              |
|                                                                                              | 8 CS0:8 CS2:8 Format Code                                                                                                                                                                                                                                    |
| 9 CS0:9 CS2:9                                                                                | bits 4…15: Reserved modem control line states – Always 0 bit 3: Data Carrier Detect bit 2: Reserved modem control line state – Always 0 bit 1: Request to Send bit 0: Clear to Send                                                                          |
|                                                                                              | 10 CS0:10 CS2:10 Total Packets Sent                                                                                                                                                                                                                          |
|                                                                                              | 11 CS0:11 CS2:11 Total Packets Received for this node                                                                                                                                                                                                        |
|                                                                                              | 12 CS0:12 CS2:12 Total Packets Observed                                                                                                                                                                                                                      |
|                                                                                              | 13 CS0:13 CS2:13 Undelivered Message Packets                                                                                                                                                                                                                 |
|                                                                                              | 14 CS0:14 CS2:14 Message Packets Retried                                                                                                                                                                                                                     |
|                                                                                              | 15 CS0:15 CS2:15 NAK Packets Received                                                                                                                                                                                                                        |
|                                                                                              | 16 CS0:16 CS2:16 Link Layer Error Count                                                                                                                                                                                                                      |
| 17 CS0:17 CS2:17                                                                             | 2: ERR_TOO_SHORT 3: ERR_TOO_LONG 4: ERR_UART_ERROR 5: ERR_BAD_CRC 6: ERR_CTS_TIMEOUT 7: ERR_CTS_DROP_MID_PKT 8: ERR_UNKNOWN_CHAR                                                                                                                             |
|                                                                                              | 18 CS0:18 CS2:18 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 19 CS0:19 CS2:19 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 20 CS0:20 CS2:20 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 21 CS0:21 CS2:21 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 22 CS0:22 CS2:22 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 23 CS0:23 CS2:23 Data Link Layer Active Node Table                                                                                                                                                                                                           |
| 24 CS0:24 CS2:24 Length                                                                      |                                                                                                                                                                                                                                                              |
|                                                                                              | 25 CS0:25 CS2:25 Format Code                                                                                                                                                                                                                                 |
|                                                                                              | 26 CS0:26 CS2:26 Number of Nodes                                                                                                                                                                                                                             |
|                                                                                              | 27 CS0:27 CS2:27 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 28 CS0:28 CS2:28 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 29 CS0:29 CS2:29 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 30 CS0:30 CS2:30 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 31 CS0:31 CS2:31 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 32 CS0:32 CS2:32 Reserved – Always 0                                                                                                                                                                                                                         |
|                                                                                              | 34 CS0:34 CS2:34 Reserved – Always 0                                                                                                                                                                                                                         |

Table 43 - Communication Status File Words (Continued)

| Words Offset File/Element Description for Channel 0 File/Element Description for Channel 2   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                              | 35 CS0:35 CS2:35 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 36 CS0:36 CS2:36 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 37 CS0:37 CS2:37 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 38 CS0:38 CS2:38 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 39 CS0:39 CS2:39 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 40 CS0:40 CS2:40 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 41 CS0:41 CS2:41 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 42 CS0:42 CS2:42 Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 43 CS0:43 CS2:43 List Category ID (10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                              | 44 CS0:44 CS2:44 Length (14)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                              | 45 CS0:45 CS2:45 Format Code (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                              | 46 CS0:46 CS2:46 Pre-Send Time Delay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 47 CS0:47 CS2:47 Node Address for this Slave                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                              | 48 CS0:48 CS2:48 Reserved – always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 49 CS0:49 CS2:49 RTS Send Delay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                              | 50 CS0:50 CS2:50 RTS Off Delay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 51 CS0:51 CS2:51                                                                             | bits 0…7: Communication rate bits 8…9: Parity bits 10…15: Reserved – Always 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                              | 52 CS0:52 CS2:52 List Category ID (6)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                              | 53 CS0:53 CS2:53 Length (32)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                              | 54 CS0:54 CS2:54 Format Code (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 55 CS0:55 CS2:55                                                                             | 1: FC_CANNOT_BROADCAST – Reserved 2: FC_NOT_SUPPORTED – The received packet has an unsupported Function Code. 3: OBJ_NOT_SUPPORTED – The received packet has unsupported objects. 4: BAD_REQUEST_LENGTH – Reserved 5: CONFIGURATION_ERROR – The error is caused by the invalid configuration during packet generating. For example, invalid Data-Set Configuration. 6: BAD_PARAMETER – The received packet has invalid parameters except Function Code and Object Codes. For example, invalid Qualifier codes. 7: BAD_FILE_TYPE – The error is caused by invalid configuration in the DNP3 Slave Application Layer. Invalid File Type specified. 8: BAD_FILE_NUMBER – The error is caused by invalid configuration in the DNP3 Slave Application Layer. Invalid File Number specified. 9: BAD_DNP3_ADDRESS – The error is caused by invalid configuration in the DNP3 Slave Application Layer. Invalid File Number specified. 10: TABLE_WRITE_PROTECTED – The specified DNP3 object data file has been locked to be written. 11: TABLE_ACCESS_DENIED – The specified DNP3 object data file has been locked to be read or written. 12: TABLE_OWNERSHIP_ERROR – The specified DNP3 object data file has been locked to be read or written. If an error code is within 6…12, the related file number and element number are shown in Word 59 and Word 60. |
|                                                                                              | 56 CS0:56 CS2:56 Application Layer Error Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                              | 57 CS0:57 CS2:57 Function Code that caused the last error                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                              | 58 CS0:58 CS2:58 Last Transmitted IIN in the response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                              | 59 CS0:59 CS2:59 Data file number of last error request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                              | 60 CS0:60 CS2:60 Data element number of last error request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                              | 61 CS0:61 CS2:61 Received Confirm Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                              | 62 CS0:62 CS2:62 Received Read Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                              | 63 CS0:63 CS2:63 Received Write Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                              | 64 CS0:64 CS2:64 Received Etc Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                              | 65 CS0:65 CS2:65 Transmitted Solicited Response Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                              | 66 CS0:66 CS2:66 Transmitted Unsolicited Response Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                              | 67 CS0:67 CS2:67 Number of events to be reported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

Table 43 - Communication Status File Words (Continued)

| Words Offset File/Element Description for Channel 0   | File/Element Description for Channel 2   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 68 CS0:68 CS2:68                                      |                                          | Transport Function Layer Error Codes 0: NO_ERROR – No error found in the Transport Layer. 1: DISCARD_NOT_FIRST_SEG – The received packet was discarded since it was not a first segment. 2: DISCARD_DUPLICATED_AND_MORE_SEG – The received packet was discarded since it had the same sequence number as previous, more segments are expected. 3: DISCARD_DUPLICATED_AND_FINAL_SEG – The received packet was discarded since it had the same sequence number as the previous, final segment received. 4: DISCARD_OUT_OF_ORDER_SEG – The received packet was discarded since the sequence number was out of order. |
|                                                       |                                          | 69 CS0:69 CS2:69 Transport Layer Error Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                       |                                          | 70 CS0:70 CS2:70 End Of List Category ID (0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

The elements can be seen in the Function Files for each Channel.

<!-- image -->

<!-- image -->

For the elements of the DNP3 Slave Link Layer diagnostic counter CS0:9…CS0:17 and CS2:9…CS2:17, the counter values are available with the structured display in RSLogix 500/RSLogix Micro.

<!-- image -->

## Table 44 - Data File for Troubleshooting

| Word Offset Description Category           |                                                          |
|--------------------------------------------|----------------------------------------------------------|
| 0 Counter for Commands Received            | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 1 Counter for Commands Received with Error | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 2 Counter for Replies Sent                 | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 3 Reserved                                 | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 4 Reserved                                 | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 5 Reserved                                 | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 6 Error Count in sessions                  | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 7 Error Code in sessions*                  | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 8 Incoming Message Connections             | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 9 Maximum Connections Allowed              | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 10 Counter for Commands Transmitted        | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 11 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 12 Counter for Replies Received            | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 13 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 14 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 15 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 16 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 17 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 18 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |
| 19 Reserved                                | TCP Server – Link Layer Diagnostics for DNP3 TCP Server. |

For the elements of the DNP3 Slave Application Layer diagnostic counter CS0:55…CS0:69 and CS2:55…CS2:69, the counter values are available with the structured display in RSLogix 500/ RSLogix Micro software.

<!-- image -->

<!-- image -->

## Diagnostics for Ethernet Channel (Channel 1)

This feature is supported only in MicroLogix 1400 Series B and Series C controllers.

Diagnostic Counters and Errors in the DNP3 slave subsystem for the Ethernet channel are logged in the Data File. The data file is configured in the parameter Diagnostic File Number. This table shows the 80 words of the data file for the troubleshooting.

Table 44 - Data File for Troubleshooting (Continued)

| Word Offset Description Category                                                                                                                                                                                                                                                                                                                                                                                |                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| 20 Counter for Commands Received                                                                                                                                                                                                                                                                                                                                                                                | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 21 Counter for Commands Received with Error                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 22 Counter for Replies Sent                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 23 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 24 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 25 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 26 Error Count in sessions                                                                                                                                                                                                                                                                                                                                                                                      | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 27 Error Code in sessions*                                                                                                                                                                                                                                                                                                                                                                                      | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 28 Number of Sockets in use                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 29 Maximum Sockets Allowed                                                                                                                                                                                                                                                                                                                                                                                      | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 30 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 31 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 32 Counter for Replies Received                                                                                                                                                                                                                                                                                                                                                                                 | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 33 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 34 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 35 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 36 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 37 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 38 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 39 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | UDP Datagram – Link Layer Diagnostics for DNP3 UDP.        |
| 40 Counter for Commands Sent                                                                                                                                                                                                                                                                                                                                                                                    | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 41 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 42 Counter for Replies Received                                                                                                                                                                                                                                                                                                                                                                                 | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 43 Counter for Replies Received with Error                                                                                                                                                                                                                                                                                                                                                                      | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 44 Counter for Replies Timed Out                                                                                                                                                                                                                                                                                                                                                                                | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 45 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 46 Error Count in sessions                                                                                                                                                                                                                                                                                                                                                                                      | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 47 Error Code in sessions*                                                                                                                                                                                                                                                                                                                                                                                      | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 48 Outgoing Message Connections                                                                                                                                                                                                                                                                                                                                                                                 | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 49 Maximum Connections Allowed                                                                                                                                                                                                                                                                                                                                                                                  | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 50 Counter for Commands Received                                                                                                                                                                                                                                                                                                                                                                                | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 51 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 52 Counter for Replies Transmitted                                                                                                                                                                                                                                                                                                                                                                              | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 53 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 54 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 55 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 56 Reserved                                                                                                                                                                                                                                                                                                                                                                                                     | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 57 Reserved, Firmware use only                                                                                                                                                                                                                                                                                                                                                                                  | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 58 Reserved, Firmware use only                                                                                                                                                                                                                                                                                                                                                                                  | TCP Client – Link Layer Diagnostics for DNP3 TCP Client.   |
| 59 Reserved, Firmware use only                                                                                                                                                                                                                                                                                                                                                                                  |                                                            |
| 60 Application Layer Error Codes: 0: NO_ERROR – No error found in the Application Layer. 1: FC_CANNOT_BROADCAST – Reserved 2: FC_NOT_SUPPORTED – The received packet has an unsupported Function Code. 3: OBJ_NOT_SUPPORTED – The received packet has unsupported objects. 4: BAD_REQUEST_LENGTH – Reserved 5: CONFIGURATION_ERROR – The error is caused by the invalid configuration during packet generating. | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |

## Table 44 - Data File for Troubleshooting (Continued)

| Word Offset Description Category                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| 60 6: BAD_PARAMETER – The received packet has invalid parameters except Function Code and Object Codes. For example, invalid Qualifier codes. 7: BAD_FILE_TYPE – The error is caused by invalid configuration in DNP3 Slave Application Layer. Invalid File Type specified. 8: BAD_FILE_NUMBER – The error is caused by invalid configuration in DNP3 Slave Application Layer. Invalid File Number specified. 9: BAD_DNP3_ADDRESS – The error is caused by invalid configuration in DNP3 Slave Application Layer. Invalid File Number specified. 10: TABLE_WRITE_PROTECTED – The specified DNP3 object data file has been locked to be written. 11: TABLE_ACCESS_DENIED – The specified DNP3 object data file has been locked to be read or written. 12: TABLE_OWNERSHIP_ERROR – The specified DNP3 object data file has been locked to be read or written. If an error code is within 6…12, the related file number and element number are shown in Word 64 and Word 65. | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 61 Application Layer Error Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 62 Function Code that caused the last error                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 63 Last Transmitted IIN in the response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 64 Data file number of last error request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 65 Data element number of last error request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 66 Received Confirm Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 67 Received Read Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 68 Received Write Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 69 Received Function Code Counter other than Confirm, Read, and Write Function Codes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 70 Transmitted Solicited Response Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 71 Transmitted Unsolicited Response Function Code Counter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | DNP3 Slave – Application Layer Diagnostics for DNP3 Slave. |
| 72 Number of events to be reported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                            |
| 73 Transport Function Layer Error Codes: 0: NO_ERROR – No error found in the Transport Layer. 1: DISCARD_NOT_FIRST_SEG – The received packet was discarded since it was not a first segment. 2: DISCARD_DUPLICATED_AND_MORE_SEG – The received packet was discarded since it had the same sequence number as previous, more segments are expected. 3: DISCARD_DUPLICATED_AND_FINAL_SEG – The received packet was discarded since it had the same sequence number as the previous, final segment received. 4: DISCARD_OUT_OF_ORDER_SEG – The received packet was discarded since the sequence number was out of order.                                                                                                                                                                                                                                                                                                                                                     |                                                            |
| 74 Transport Layer Error Count                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                            |
| 75 Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                            |
| 76 Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                            |
| 77 Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                            |
| 78 Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                            |
| 79 Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                            |

Word offset 7, 27, and 47 reflect the Error Codes that have been caused in the sessions for DNP3 TCP Server, UDP, and TCP Client respectively. The following table lists the possible ranges of the Error Code. Any others are reserved.

## Table 45 - Error Codes

| Value (DEC) Mnemonic Description                              |
|---------------------------------------------------------------|
| 0 NO ERROR No error found.                                    |
| 1 ERR_SOCKET_CREATE Socket error during Create operation.     |
| 2 ERR_SOCKET_LISTEN Socket error during Listen operation.     |
| 3 ERR_SOCKET_BIND Socket error during Bind operation.         |
| 4 ERR_SOCKET_ACCEPT Socket error during Accept operation.     |
| 5 ERR_SOCKET_CONNECT Socket error during Connect operation.   |
| 6 ERR_SOCKET_SEND Socket error during Send operation.         |
| 7 ERR_SOCKET_RECEIVE Socket error during Receive operation.   |
| 8 ERR_SOCKET_UNLISTEN Socket error during Unlisten operation. |
| 9 ERR_SOCKET_UNBIND Socket error during Unbind operation.     |

Table 45 - Error Codes (Continued)

| Value (DEC) Mnemonic Description                                                   |
|------------------------------------------------------------------------------------|
| 10 ERR_SOCKET_UNACCEPT Socket error during Unaccept operation.                     |
| 11 ERR_SOCKET_DISCONNECT Socket error during Disconnect operation.                 |
| 12 ERR_SOCKET_DELETE Socket error during Delete operation.                         |
| 13…14 Reserved —                                                                   |
| 15 ERR_QUE_FULL Firmware use only                                                  |
| 16 ERR_BUFFER_ALLOC Firmware use only                                              |
| 17 ERR_PACKET_ALLOC Firmware use only                                              |
| 18 ERR_PACKET_RELEASE Firmware use only                                            |
| 19…29 Reserved —                                                                   |
| 30 ERR_CONN_REJECTED Incoming Connection is rejected by the IP address validation. |
| 31 ERR_INVALID_HEADER_CRC Received packet header has an invalid CRC.               |
| 32 ERR_INVALID_HEADER Received packet header has invalid packet format.            |
| 33 ERR_INVALID_PACKET_CRC Received packet has an invalid CRC.                      |
| 34 ERR_BAD_PACKET_RECEIVED Received packet is unknown.                             |
| 35 ERR_PACKET_REJECTED Received packet is rejected.                                |
| 36 ERR_CONNECTION_BROKEN The connection has been broken for some reason.           |
| 37…49 Reserved —                                                                   |
| 50 ERR_INVALID_IP_ADDRESS Target IP Address is invalid.                            |
| 51 ERR_INVALID_PORT Target Port Number is invalid.                                 |
| 52… Reserved —                                                                     |

For the elements of the DNP3 Slave Application Layer diagnostic counter element offset 60…74, the counter values available with the structured display in RSLogix 500/RSLogix Micro software as shown.

<!-- image -->

If the data file is not configured in the parameter Diagnostic File Number of the Chan. 1 – DNP3 configuration, the Channel 1 – Ext dialog box displays as shown.

<!-- image -->

## Diagnostics for Secure Authentication

This feature is supported only in MicroLogix 1400 Series B and Series C controllers.

Table 46 - Secure Authentication Diagnostics

| Word Offset   | Current State Description                                                               |
|---------------|-----------------------------------------------------------------------------------------|
| CH0 CH1 CH2   |                                                                                         |
|               | 0 50 100 Security Idle/Wait for Reply Authentication Error Counter                      |
|               | 2 52 102 Security Idle/Wait for Reply Reserved                                          |
|               | 3 53 103 Security Idle/Wait for Reply Reserved                                          |
|               | 4 54 104 Security Idle/Wait for Reply Reserved                                          |
|               | 5 55 105 Security Idle/Wait for Reply Reserved                                          |
|               | 6 56 106 Security Idle Event Counter for Rx Unsolicited Non-Critical ASDU               |
|               | 7 57 107 Security Idle Event Counter for Rx Non-Critical ASDU                           |
|               | 8 58 108 Security Idle Event Counter for Rx Critical ASDU                               |
|               | 9 59 109 Security Idle Event Counter for Rx Critical ASDU                               |
|               | 10 60 110 Security Idle Event Counter for Rx Valid Reply                                |
|               | 11 61 111 Security Idle Event Counter for Rx Invalid Reply                              |
|               | 12 62 112 Security Idle Event Counter for Reply Timeout                                 |
|               | 13 63 113 Security Idle Event Counter for Max Invalid Replies Or Comm Failure Detected  |
|               | 14 64 114 Security Idle Event Counter for Max Invalid Replies Or Comm Failure Detected  |
|               | 15 65 115 Security Idle Event Counter for Rx Error Message                              |
|               | 16 66 116 Security Idle Event Counter for Key Change Timeout                            |
|               | 17 67 117 Security Idle Event Counter for Expected Key Change Timeout                   |
|               | 18 68 118 Security Idle Event Counter for Expected Key Change Timeout                   |
|               | 19 69 119 Security Idle Event Counter for Rx Key Status Request                         |
|               | 20 70 120 Security Idle Event Counter for Rx Valid Aggressive Mode Request              |
|               | 21 71 121 Security Idle Event Counter for Rx Valid Aggressive Mode Request              |
|               | 22 72 122 Security Idle Event Counter for Rx Invalid Aggressive Mode Request            |
|               | 23 73 123 Security Idle Event Counter for Rx Valid Key Change                           |
|               | 24 74 124 Security Idle Event Counter for Rx Invalid Key Change                         |
|               | 25 75 125 Security Idle Event Counter for Rx Challenge                                  |
|               | 26 76 126 Security Idle Reserved                                                        |
|               | 27 77 127 Security Idle Counter for Ignored events                                      |
|               | 28 78 128 Wait for Reply Event Counter for Rx Unsolicited Non-Critical ASDU             |
|               | 29 79 129 Wait for Reply Event Counter for Rx Non-Critical ASDU                         |
|               | 30 80 130 Wait for Reply Event Counter for Rx Critical ASDU                             |
|               | 31 81 131 Wait for Reply Event Counter for Rx Critical ASDU                             |
|               | 32 82 132 Wait for Reply Event Counter for Rx Valid Reply                               |
|               | 33 83 133 Wait for Reply Event Counter for Rx Invalid Reply                             |
|               | 34 84 134 Wait for Reply Event Counter for Reply Timeout                                |
|               | 35 85 135 Wait for Reply Event Counter for Max Invalid Replies Or Comm Failure Detected |
|               | 36 86 136 Wait for Reply Event Counter for Max Invalid Replies Or Comm Failure Detected |
|               | 37 87 137 Wait for Reply Event Counter for Rx Error Message                             |
|               | 38 88 138 Wait for Reply Event Counter for Key Change Timeout                           |
|               | 39 89 139 Wait for Reply Event Counter for Expected Key Change Timeout                  |
|               | 40 90 140 Wait for Reply Event Counter for Expected Key Change Timeout                  |
|               | 41 91 141 Wait for Reply Event Counter for Rx Key Status Request                        |

Counters in the DNP3 Slave Secure Authentication subsystem are logged in the Data File. The data file is configured in the parameter Diagnostic File Number in Secure Authentication. The following table shows the 150 words of the data file for the troubleshooting.

The 50 words are used to log the counters for each channel. Word offset 0…49 is for Channel 0, word offset 50…99 is for Channel 1, and word offset 100…149 is for Channel 2.

Words 6…49, 56…99, and 106…149 are the event counter for Challenger State Machine that is stated in the DNP3 Specification, Supplement to Volume 2, Secure Authentication, Version 2.00.

Table 46 - Secure Authentication Diagnostics (Continued)

| Word Offset   | Current State Description                                                     | Word Offset   |
|---------------|-------------------------------------------------------------------------------|---------------|
| CH0 CH1 CH2   | Current State Description                                                     |               |
|               | 42 92 142 Wait for Reply Event Counter for Rx Valid Aggressive Mode Request   |               |
|               | 43 93 143 Wait for Reply Event Counter for Rx Valid Aggressive Mode Request   |               |
|               | 44 94 144 Wait for Reply Event Counter for Rx Invalid Aggressive Mode Request |               |
|               | 45 95 145 Wait for Reply Event Counter for Rx Valid Key Change                |               |
|               | 46 96 146 Wait for Reply Event Counter for Rx Invalid Key Change              |               |
|               | 47 97 147 Wait for Reply Event Counter for Rx Challenge                       |               |
|               | 48 98 148 Wait for Reply Reserved                                             |               |
|               | 49 99 149 Wait for Reply Counter for Ignored events                           |               |

## Function Codes

These tables show the Application Layer Function codes that are implemented in the controller.

Table 47 - Function Codes for MicroLogix 1400 Series A Controllers

|                                                                | Message Type Function Code Name MicroLogix 1400 Support Description                                                                                              |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                | Confirmation 0 (0x00) FC_CONFIRM Yes Controller parses/sends                                                                                                     |
|                                                                | Request 1 (0x01) FC_READ Yes Controller parses                                                                                                                   |
|                                                                | Request 2 (0x02) FC_WRITE Yes Controller parses                                                                                                                  |
|                                                                | Request 3 (0x03) FC_SELECT Yes Controller parses                                                                                                                 |
|                                                                | Request 4 (0x04) FC_OPERATE Yes Controller parses                                                                                                                |
| Request 5 (0x05) FC_DIRECT_OPERATE Yes Controller parses       |                                                                                                                                                                  |
| Request 6 (0x06) FC_DIRECT_OPERATE_NR Yes Controller parses    |                                                                                                                                                                  |
| Request 7 (0x07) FC_IMMED_FREEZE Yes Controller parses         |                                                                                                                                                                  |
| Request 8 (0x08) FC_IMMED_FREEZE_NR Yes Controller parses      |                                                                                                                                                                  |
| Request 9 (0x09) FC_FREEZE_CLEAR Yes Controller parses         |                                                                                                                                                                  |
| Request 10 (0x0A) FC_FREEZE_CLEAR_NR Yes Controller parses     |                                                                                                                                                                  |
| Request 11 (0x0B) FC_FREEZE_AT_TIME No                         |                                                                                                                                                                  |
| Request 12 (0x0C) FC_FREEZE_AT_TIME_NR No                      |                                                                                                                                                                  |
| Request 13 (0x0D) FC_COLD_RESTART Yes                          | Controller parses. The controller should not be in the executing mode and any program and files should not be in an open state.                                  |
| Request 14 (0x0E) FC_WARM_RESTART No                           |                                                                                                                                                                  |
| Request 15 (0x0F) FC_INITIALIZE_DATA No Obsolete               |                                                                                                                                                                  |
| Request 16 (0x10) FC_INITIALIZE_APPL Yes                       | Controller parses. Clears fault and changes the controller mode to Remote Program. See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 . |
| Request 17 (0x11) FC_START_APPL Yes                            | Controller parses. Clears fault and changes the controller mode to Remote Run. See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 .     |
| Request 18 (0x12) FC_STOP_APPL Yes                             | Controller parses. Changes the controller mode to Remote Program. See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 .                  |
| Request 19 (0x13) FC_SAVE_CONFIG No Deprecated.                |                                                                                                                                                                  |
|                                                                | Request 20 (0x14) FC_ENABLE_UNSOLICITED Yes Controller parses                                                                                                    |
| Request 21 (0x15) FC_DISABLE_UNSOLICITED Yes Controller parses |                                                                                                                                                                  |
| Request 22 (0x16) FC_ASSIGN_CLASS No                           |                                                                                                                                                                  |
|                                                                | Request 23 (0x17) FC_DELAY_MEASURE Yes Controller parses. Used for non-LAN                                                                                       |
| Request 24 (0x18) FC_RECORD_CURRENT_TIME No Used for LAN       |                                                                                                                                                                  |
|                                                                | Request 25 (0x19) FC_OPEN_FILE Yes Controller parses                                                                                                             |
|                                                                | Request 26 (0x1A) FC_CLOSE_FILE Yes Controller parses                                                                                                            |
|                                                                | Request 27 (0x1B) FC_DELETE_FILE Yes Controller parses                                                                                                           |
| Request 28 (0x1C) FC_GET_FILE_INFO No                          |                                                                                                                                                                  |
| Request 29 (0x1D) FC_AUTHENTICATE_FILE Yes Controller parses   |                                                                                                                                                                  |
| Request 30 (0x1E) FC_ABORT_FILE No                             |                                                                                                                                                                  |
| Request 31 (0x1F) FC_ACTIVATE_CONFIG No                        |                                                                                                                                                                  |

Table 47 - Function Codes for MicroLogix 1400 Series A Controllers (Continued)

|                                                                  | Message Type Function Code Name MicroLogix 1400 Support Description   |
|------------------------------------------------------------------|-----------------------------------------------------------------------|
| Request 32 (0x20) FC_AUTHENTICATE_REQ No                         |                                                                       |
| Request 33 (0x21) FC_AUTHENTICATE_ERR No                         |                                                                       |
| 34 (0x22)…128 (0x80) No Reserved.                                |                                                                       |
|                                                                  | Response 129 (0x81) FC_RESPONSE Yes Controller sends                  |
| Response 130 (0x82) FC_UNSOLICITED_RESPONSE Yes Controller sends |                                                                       |
| Response 131 (0x83) FC_AUTHENTICATE_RESP No                      |                                                                       |
| 132 (0x84)…255 (0xFF) No Reserved.                               |                                                                       |

Table 48 - Function Codes for MicroLogix 1400 Series B and Series C Controllers

|                                                                | Message Type Function Code Name MicroLogix 1400 Support Description                                                                                              |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                | Confirmation 0 (0x00) FC_CONFIRM Yes Controller parses/sends                                                                                                     |
|                                                                | Request 1 (0x01) FC_READ Yes Controller parses                                                                                                                   |
|                                                                | Request 2 (0x02) FC_WRITE Yes Controller parses                                                                                                                  |
|                                                                | Request 3 (0x03) FC_SELECT Yes Controller parses                                                                                                                 |
|                                                                | Request 4 (0x04) FC_OPERATE Yes Controller parses                                                                                                                |
| Request 5 (0x05) FC_DIRECT_OPERATE Yes Controller parses       |                                                                                                                                                                  |
| Request 6 (0x06) FC_DIRECT_OPERATE_NR Yes Controller parses    |                                                                                                                                                                  |
| Request 7 (0x07) FC_IMMED_FREEZE Yes Controller parses         |                                                                                                                                                                  |
|                                                                | Request 8 (0x08) FC_IMMED_FREEZE_NR Yes Controller parses                                                                                                        |
| Request 9 (0x09) FC_FREEZE_CLEAR Yes Controller parses         |                                                                                                                                                                  |
| Request 10 (0x0A) FC_FREEZE_CLEAR_NR Yes Controller parses     |                                                                                                                                                                  |
| Request 11 (0x0B) FC_FREEZE_AT_TIME No                         |                                                                                                                                                                  |
| Request 12 (0x0C) FC_FREEZE_AT_TIME_NR No                      |                                                                                                                                                                  |
| Request 13 (0x0D) FC_COLD_RESTART Yes                          | Controller parses. The controller should not be in the executing mode and any program and files should not be in an open state.                                  |
| Request 14 (0x0E) FC_WARM_RESTART No Controller parses         |                                                                                                                                                                  |
| Request 15 (0x0F) FC_INITIALIZE_DATA No Obsolete               |                                                                                                                                                                  |
| Request 16 (0x10) FC_INITIALIZE_APPL Yes                       | Controller parses. Clears fault and changes the controller mode to Remote Program. See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 . |
| Request 17 (0x11) FC_START_APPL Yes                            | Controller parses. Clears fault and changes the controller mode to Remote Run. See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 .     |
| Request 18 (0x12) FC_STOP_APPL Yes                             | Controller parses. Changes the controller mode to Remote Program. See Start and Stop User Programs (Mode Change) Via DNP3 Network on page 246 .                  |
| Request 19 (0x13) FC_SAVE_CONFIG No Deprecated.                |                                                                                                                                                                  |
| Request 20 (0x14) FC_ENABLE_UNSOLICITED Yes Controller parses  |                                                                                                                                                                  |
| Request 21 (0x15) FC_DISABLE_UNSOLICITED Yes Controller parses |                                                                                                                                                                  |
| Request 22 (0x16) FC_ASSIGN_CLASS No                           |                                                                                                                                                                  |
|                                                                | Request 23 (0x17) FC_DELAY_MEASURE Yes Controller parses. Used for non-LAN                                                                                       |
|                                                                | Request 24 (0x18) FC_RECORD_CURRENT_TIME No Controller parses. Used for LAN                                                                                      |
|                                                                | Request 25 (0x19) FC_OPEN_FILE Yes Controller parses                                                                                                             |
|                                                                | Request 26 (0x1A) FC_CLOSE_FILE Yes Controller parses                                                                                                            |
| Request 27 (0x1B) FC_DELETE_FILE Yes Controller parses         |                                                                                                                                                                  |
| Request 28 (0x1C) FC_GET_FILE_INFO No Controller parses        |                                                                                                                                                                  |
| Request 29 (0x1D) FC_AUTHENTICATE_FILE Yes Controller parses   |                                                                                                                                                                  |
|                                                                | Request 30 (0x1E) FC_ABORT_FILE No Controller parses                                                                                                             |
| Request 31 (0x1F) FC_ACTIVATE_CONFIG No Controller parses      |                                                                                                                                                                  |
| Request 32 (0x20) FC_AUTHENTICATE_REQ No Controller parses     |                                                                                                                                                                  |
| Request 33 (0x21) FC_AUTHENTICATE_ERR No Controller parses     |                                                                                                                                                                  |
| 34 (0x22)…128 (0x80) No Reserved.                              |                                                                                                                                                                  |
| Response 129 (0x81) FC_RESPONSE Yes Controller sends           |                                                                                                                                                                  |

Table 48 - Function Codes for MicroLogix 1400 Series B and Series C Controllers (Continued)

|                                                                  | Message Type Function Code Name MicroLogix 1400 Support Description   |
|------------------------------------------------------------------|-----------------------------------------------------------------------|
| Response 130 (0x82) FC_UNSOLICITED_RESPONSE Yes Controller sends |                                                                       |
| Response 131 (0x83) FC_AUTHENTICATE_RESP No Controller sends     |                                                                       |
| 132 (0x84)…255 (0xFF) No Reserved.                               |                                                                       |

## Implementation Table

The MicroLogix 1400 controller supports DNP3 Certification Subset Level 2.

Table 49 identifies which object groups and variations, function codes, and qualifiers that the device supports in both requests and responses. The Request and Response columns identify all requests and responses that could be sent/parsed by a DNP3 Master, or must be parsed/sent by the controller.

The implementation table lists all functionality that is required by either DNP3 Master or controller as defined within the DNP3 IED Conformance Test Procedures. Any functionality beyond the highest subset level that is supported is indicated by grayed table cells.

Table 49 - Implementation Table for Series A controllers

|                               |                                                                   | Request DNP3 master could issue Controller must parse   | Request DNP3 master could issue Controller must parse                                                               | Response DNP3 master must parse Controller could issue   | Response DNP3 master must parse Controller could issue   |
|-------------------------------|-------------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                               |                                                                   |                                                         | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) Function Codes (dec) Qualifier Codes (hex) |                                                          |                                                          |
| 0 211…239 241…243 248…250 252 | Device Attribute                                                  | 1 (read)                                                | 00 (start-stop)                                                                                                     | 129 (response)                                           | 00 (start-stop)                                          |
| 0  240 245…247                | Device Attribute                                                  | 1 (read)  2 (write)                                     | 00 (start-stop)  00 (start-stop)                                                                                    | 129 (response)                                           | 00 (start-stop)                                          |
| 0 254                         | Device Attribute – Non-specific all attributes request            | 1 (read)                                                | 00, 01 (start-stop) 06 (no range, or all)                                                                           |                                                          |                                                          |
| 0 255                         | Device Attributes – List of attribute variations                  | 1 (read)                                                | 00, 01 (start-stop) 06 (no range, or all)                                                                           | 129 (response)                                           | 00 (start-stop)                                          |
|                               | 1 0 Binary Input – Any Variation 1 (read) 06 (no range, or all)   |                                                         |                                                                                                                     |                                                          |                                                          |
|                               | 1 1 Binary Input – Packed format                                  | 1 (read)                                                | 06 (no range, or all) 129 (response) 00, 01 (start-stop)                                                            |                                                          |                                                          |
|                               | 1 2 Binary Input – With flags                                     | 1 (read)                                                | 06 (no range, or all) 129 (response) 00, 01 (start-stop)                                                            |                                                          |                                                          |
|                               | 2 0 Binary Input Event – Any Variation 1 (read)                   |                                                         | 06 (no range, or all) 07, 08 (limited qty)                                                                          |                                                          |                                                          |
|                               | 2 1 Binary Input Event – Without time 1 (read)                    |                                                         | 06 (no range, or all) 07, 08 (limited qty)                                                                          | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 2 2                           | Binary Input Event – With absolute time                           | 1 (read)                                                | 06 (no range, or all) 07, 08 (limited qty)                                                                          | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 2 3                           | Binary Input Event – With relative time                           | 1 (read)                                                | 06 (no range, or all) 07, 08 (limited qty)                                                                          | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 3 0                           | Double-bit Binary Input – Any Variation                           | 1 (read)                                                | 06 (no range, or all)                                                                                               |                                                          |                                                          |
| 3 1                           | Double-bit Binary Input – Packed format                           | 1 (read)                                                | 06 (no range, or all)                                                                                               | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                               | 3 2 Double-bit Binary Input – With flags 1 (read)                 |                                                         | 06 (no range, or all)                                                                                               | 129 (response)                                           | 00, 01 (start-stop)                                      |
| 4 0                           | Double-bit Binary Input Event – Any Variation                     | 1 (read)                                                | 06 (no range, or all) 07, 08 (limited qty)                                                                          |                                                          |                                                          |
| 4 1                           | Double-bit Binary Input Event – Without time                      | 1 (read)                                                | 06 (no range, or all) 07, 08 (limited qty)                                                                          | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 4 2                           | Double-bit Binary Input Event – With absolute time                | 1 (read)                                                | 06 (no range, or all) 07, 08 (limited qty)                                                                          | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 4 3                           | Double-bit Binary Input Event – With relative time                | 1 (read)                                                | 06 (no range, or all) 07, 08 (limited qty)                                                                          | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                               | 10 0 Binary Output – Any Variation 1 (read) 06 (no range, or all) |                                                         |                                                                                                                     |                                                          |                                                          |
| 10 2                          | Binary Output – Output status with flags                          | 1 (read)                                                | 06 (no range, or all) 129 (response) 00, 01 (start-stop)                                                            |                                                          |                                                          |

Table 49 - Implementation Table for Series A controllers (Continued)

| DNP Object Group & Variation   | DNP Object Group & Variation                                       | Request DNP3 master could issue                                                                                     | Request DNP3 master could issue                          | Response DNP3 master must parse Controller could issue   | Response DNP3 master must parse Controller could issue   |
|--------------------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                |                                                                    | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) Function Codes (dec) Qualifier Codes (hex) |                                                          |                                                          |                                                          |
| 12 1                           | Binary Command – Control relay output block (CROB)                 | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack)                                                            |                                                          |                                                          | 17, 28 (index) 129 (response) Echo of request            |
|                                | 20 0 Counter – Any Variation                                       | 1 (read) 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)                                           | 06 (no range, or all)                                    |                                                          |                                                          |
|                                | 20 1 Counter – 32-bit with flag                                    | 1 (read) 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)                                           | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 20 2 Counter – 16-bit with flag                                    | 1 (read) 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)                                           |                                                          |                                                          | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |
|                                | 20 5 Counter – 32-bit without flag                                 | 1 (read) 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)                                           |                                                          |                                                          | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |
|                                | 20 6 Counter – 16-bit without flag                                 | 1 (read) 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)                                           | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 21 0 Frozen Counter – Any Variation 1 (read) 06 (no range, or all) |                                                                                                                     |                                                          |                                                          |                                                          |
|                                | 21 1 Frozen Counter – 32-bit with flag                             | 1 (read)                                                                                                            |                                                          |                                                          | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |
|                                | 21 2 Frozen Counter – 16-bit with flag                             | 1 (read)                                                                                                            | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
| 21 5                           | Frozen Counter – 32-bit with flag and time                         | 1 (read)                                                                                                            | 06 (no range, or all)                                    | 129 (response)                                           | 00, 01 (start-stop)                                      |
| 21 6                           | Frozen Counter – 16-bit with flag and time                         | 1 (read)                                                                                                            | 06 (no range, or all)                                    | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                | 21 9 Frozen Counter – 32-bit without flag 1 (read)                 |                                                                                                                     | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 21 10 Frozen Counter – 16-bit without flag 1 (read)                |                                                                                                                     | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 22 0 Counter Event – Any Variation 1 (read)                        |                                                                                                                     | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                          |
|                                | 22 1 Counter Event – 32-bit with flag                              | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 22 2 Counter Event – 16-bit with flag                              | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 23 0                           | Frozen Counter Event – Any Variation                               | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                          |
| 23 1                           | Frozen Counter Event – 32-bit with flag                            | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 23 2                           | Frozen Counter Event – 16-bit with flag                            | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 23 5                           | Frozen Counter Event – 32-bit with flag and time                   | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 23 6                           | Frozen Counter Event – 16-bit with flag and time                   | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 30 0 Analog Input – Any Variation 1 (read) 06 (no range, or all)   |                                                                                                                     |                                                          |                                                          |                                                          |
|                                | 30 1 Analog Input – 32-bit with flag                               | 1 (read)                                                                                                            | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 30 2 Analog Input – 16-bit with flag                               | 1 (read)                                                                                                            | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 30 3 Analog Input – 32-bit without flag                            | 1 (read)                                                                                                            | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 30 4 Analog Input – 16-bit without flag                            | 1 (read)                                                                                                            | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |

Table 49 - Implementation Table for Series A controllers (Continued)

| DNP Object Group & Variation   | DNP Object Group & Variation                                                                        | Request DNP3 master could issue                          | Request DNP3 master could issue                          | Response DNP3 master must parse Controller could issue   | Response DNP3 master must parse Controller could issue                                                              |
|--------------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
|                                |                                                                                                     |                                                          |                                                          |                                                          | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) Function Codes (dec) Qualifier Codes (hex) |
| 30 5                           | Analog Input – Single-prec flt-pt with flag                                                         | 1 (read)                                                 | 06 (no range, or all)                                    | 129 (response)                                           | 00, 01 (start-stop)                                                                                                 |
|                                | 32 0 Analog Input Event – Any Variation 1 (read)                                                    |                                                          | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                                                                                     |
| 32 1                           | Analog Input Event – 32-bit without time                                                            | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                                                                                      |
| 32 2                           | Analog Input Event – 16-bit without time                                                            | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                                                                                      |
| 32 3                           | Analog Input Event – 32-bit with time                                                               | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                                                                                      |
| 32 4                           | Analog Input Event – 16-bit with time                                                               | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                                                                                      |
| 32 5                           | Analog Input Event – Single-prec flt-pt without time                                                | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                                                                                      |
| 32 7                           | Analog Input Event – Single-prec flt-pt with time                                                   | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                                                                                      |
| 40 0                           | Analog Output Status – Any Variation                                                                |                                                          | 1 (read) 06 (no range, or all)                           |                                                          |                                                                                                                     |
| 40 1                           | Analog Output Status – 32-bit with flag                                                             | 1 (read)                                                 | 06 (no range, or all)                                    | 129 (response)                                           | 00, 01 (start-stop)                                                                                                 |
| 40 2                           | Analog Output Status – 16-bit with flag                                                             | 1 (read)                                                 | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                                                                                     |
| 40 3                           | Analog Output Status – Single-prec flt-pt with flag                                                 | 1 (read)                                                 | 06 (no range, or all)                                    | 129 (response)                                           | 00, 01 (start-stop)                                                                                                 |
|                                | 41 1 Analog Output – 32-bit                                                                         | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack) | 17, 28 (index)                                           | 129 (response)                                           | echo of request                                                                                                     |
|                                | 41 2 Analog Output – 16-bit                                                                         | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack) |                                                          |                                                          | 17, 28 (index) 129 (response) echo of request                                                                       |
|                                | 41 3 Analog Output – Single-prec flt-pt                                                             | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack) | 17, 28 (index)                                           | 129 (response)                                           | echo of request                                                                                                     |
|                                | 50 1 Time and Date – Absolute time                                                                  | 1 (read)                                                 | 07 (limited qty = 1)                                     | 129 (response)                                           | 07 (limited qty) (qty = 1)                                                                                          |
|                                |                                                                                                     |                                                          | 2 (write) 07 (limited qty = 1)                           |                                                          |                                                                                                                     |
| 50 3  51 1                     | Time and Date – Absolute time at last recorded time Time and Date CTO – Absolute time, synchronized |                                                          |                                                          | 129 (response) 130 (unsol. resp)                         | 07 (limited qty) (qty = 1)                                                                                          |
| 51 2                           | Time and Date CTO – Absolute time, unsynchronized                                                   |                                                          |                                                          | 129 (response) 130 (unsol. resp)                         | 07 (limited qty) (qty = 1)                                                                                          |
|                                |                                                                                                     | 52 1 Time Delay – Coarse 129 (response)                  |                                                          |                                                          | 07 (limited qty) (qty = 1)                                                                                          |
|                                |                                                                                                     | 52 2 Time Delay – Fine 129 (response)                    |                                                          |                                                          | 07 (limited qty) (qty = 1)                                                                                          |
|                                | 60 1 Class Objects – Class 0 data 1 (read) 06 (no range, or all)                                    |                                                          |                                                          |                                                          |                                                                                                                     |
|                                |                                                                                                     | 1 (read)                                                 | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                                                                                     |
|                                | 60 2 Class Objects – Class 1 data                                                                   | 20 (enbl. unsol.) 21 (dab. unsol.)                       | 06 (no range, or all)                                    |                                                          |                                                                                                                     |
|                                | 60 3 Class Objects – Class 2 data 1 (read)                                                          |                                                          | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                                                                                     |

Table 49 - Implementation Table for Series A controllers (Continued)

| DNP Object Group & Variation                     | DNP Object Group & Variation                     | Request DNP3 master could issue Controller must parse                                                               | Request DNP3 master could issue Controller must parse   | Response DNP3 master must parse Controller could issue   | Response DNP3 master must parse Controller could issue   |
|--------------------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                                  |                                                  | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) Function Codes (dec) Qualifier Codes (hex) |                                                         |                                                          |                                                          |
|                                                  | 60 4 Class Objects – Class 3 data                | 1 (read)                                                                                                            | 06 (no range, or all) 07, 08 (limited qty)              |                                                          |                                                          |
|                                                  | 60 4 Class Objects – Class 3 data                | 20 (enbl. unsol.) 21 (dab. unsol.)                                                                                  | 06 (no range, or all)                                   |                                                          |                                                          |
|                                                  | 70 2 File-Control – authentication               | 29 (authenticate file)                                                                                              | 5B (free format)                                        | 129 (response)                                           | 5B (free format)                                         |
|                                                  | 70 3 File Control – file command                 | 25 (open file)                                                                                                      | 5B (free format)                                        |                                                          |                                                          |
|                                                  | 70 3 File Control – file command                 | 27 (delete file)                                                                                                    | 5B (free format)                                        |                                                          |                                                          |
|                                                  | 70 4 File Control – file command status          | 26 (close file)                                                                                                     | 5B (free format)                                        | 129 (response)                                           | 5B (free format)                                         |
|                                                  | 70 5 File Control – file transport               | 1 (read file)                                                                                                       | 5B (free format)                                        |                                                          |                                                          |
|                                                  | 70 5 File Control – file transport               | 2 (write file)                                                                                                      | 5B (free format)                                        |                                                          |                                                          |
|                                                  | 70 6 File Control – file transport status        |                                                                                                                     |                                                         | 129 (response)                                           | 5B (free format)                                         |
|                                                  | 70 7 File-Control – file descriptor              |                                                                                                                     |                                                         | 129 (response)                                           | 5B (free format)                                         |
| 80 1                                             | Internal Indications – Packed format             | 1 (read file)                                                                                                       | 00, 01 (start-stop)                                     | 129 (response)                                           | 00, 01 (start-stop)                                      |
| 80 1                                             | Internal Indications – Packed format             | 2 (write file)                                                                                                      | 00 (start-stop) index=7                                 |                                                          |                                                          |
|                                                  | 90 1 Application – Identifier                    | 16 (init. appl.) 17 (start appl.) 18 (stop appl.)                                                                   | 5B (free format) 06 (no range, or all)                  |                                                          |                                                          |
| 101 1                                            | Binary Coded Decimal Integers – small            | 1 (read file)                                                                                                       | 06 (no range, or all)                                   | 129 (response)                                           | 00, 01 (start-stop)                                      |
| 101 1                                            |                                                  |                                                                                                                     |                                                         | 130 (unsol. resp)                                        | 17, 28 (index)                                           |
| 101 2                                            | Binary Coded Decimal Integers – medium           |                                                                                                                     |                                                         |                                                          |                                                          |
| No Object (function code only) 13 (cold restart) | No Object (function code only) 13 (cold restart) | No Object (function code only) 13 (cold restart)                                                                    |                                                         |                                                          |                                                          |
| No Object (function code only) 23 (delay meas.)  | No Object (function code only) 23 (delay meas.)  | No Object (function code only) 23 (delay meas.)                                                                     |                                                         |                                                          |                                                          |

Table 50 - Implementation Table for Series B and Series C controllers

|                               |                                                        | Request DNP3 Master could issue Controller must parse                    | Request DNP3 Master could issue Controller must parse   | Response DNP3 Master must parse Controller could issue   | Response DNP3 Master must parse Controller could issue   |
|-------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                               |                                                        | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) |                                                         | Function Codes (dec)                                     | Qualifier Codes (hex)                                    |
| 0 211…239 241…243 248…250 252 | Device Attribute                                       | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               | 129 (response)                                           | 00 (start-stop)                                          |
| 0  240 245…247                | Device Attribute                                       | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               | 129 (response)                                           | 00 (start-stop)                                          |
| 0  240 245…247                | Device Attribute                                       | 2 (write)                                                                | 00, 01 (start-stop)                                     |                                                          |                                                          |
| 0 254                         | Device Attribute – Non-specific all attributes request | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          |                                                          |
| 0 255                         | Device Attributes – List of attribute variations       | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               | 129 (response)                                           | 00 (start-stop)                                          |
|                               | 1 0 Binary Input – Any Variation 1 (read)              |                                                                          | 00, 01 (start-stop)                                     |                                                          |                                                          |
|                               | 1 0 Binary Input – Any Variation 1 (read)              |                                                                          | 06 (no range, or all)                                   |                                                          |                                                          |
|                               | 1 1 Binary Input – Packed format                       | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                               | 1 2 Binary Input – With flags                          | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                               | 2 0 Binary Input Event – Any Variation 1 (read)        |                                                                          | 06 (no range, or all) 07, 08 (limited qty)              |                                                          |                                                          |
|                               | 2 1 Binary Input Event – Without time 1 (read)         |                                                                          | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 2 2                           | Binary Input Event – With absolute time                | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |

Table 50 - Implementation Table for Series B and Series C controllers (Continued)

| DNP Object Group & Variation   | DNP Object Group & Variation                         | Request DNP3 Master could issue Controller must parse                    | Request DNP3 Master could issue Controller must parse    | Response DNP3 Master must parse Controller could issue   | Response DNP3 Master must parse Controller could issue   |
|--------------------------------|------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                |                                                      | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) |                                                          | Function Codes (dec)                                     | Qualifier Codes (hex)                                    |
|                                | 2 3 Binary Input Event – With relative time 1 (read) |                                                                          | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 3 0 Double-bit Binary Input – Any Variation 1 (read) |                                                                          | 00, 01 (start-stop) 06 (no range, or all)                |                                                          |                                                          |
| 3 1                            | Double-bit Binary Input – Packed format              | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                | 3 2 Double-bit Binary Input – With flags             | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                | 129 (response)                                           | 00, 01 (start-stop)                                      |
| 4 0                            | Double-bit Binary Input Event – Any Variation        | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                          |
| 4 1                            | Double-bit Binary Input Event – Without time         | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 4 2                            | Double-bit Binary Input Event – With absolute time   | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 4 3                            | Double-bit Binary Input Event – With relative time   | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 10 0 Binary Output – Any Variation 1 (read)          |                                                                          | 00, 01 (start-stop) 06 (no range, or all)                |                                                          |                                                          |
| 10 2                           | Binary Output – Output status with flags             | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                |                                                          | 129 (response) 00, 01 (start-stop)                       |
| 12 1                           | Binary Command – Control relay output block (CROB)   | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack)                 |                                                          |                                                          | 17, 28 (index) 129 (response) echo of request            |
|                                | 20 0 Counter – Any Variation 1 (read)                |                                                                          | 00, 01 (start-stop) 06 (no range, or all)                |                                                          |                                                          |
|                                | 20 1 Counter – 32-bit with flag                      | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 20 1 Counter – 32-bit with flag                      | 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)         | 06 (no range, or all)                                    |                                                          |                                                          |
|                                | 20 2 Counter – 16-bit with flag                      | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 20 2 Counter – 16-bit with flag                      | 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)         | 06 (no range, or all)                                    |                                                          |                                                          |
|                                | 20 5 Counter – 32-bit without flag                   | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 20 5 Counter – 32-bit without flag                   | 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)         | 06 (no range, or all)                                    |                                                          |                                                          |
|                                | 20 6 Counter – 16-bit without flag                   | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 20 6 Counter – 16-bit without flag                   | 7 (freeze) 8 (freeze noack) 9 (freeze clear) 10 (frz. cl. noack)         | 06 (no range, or all)                                    |                                                          |                                                          |
|                                | 21 0 Frozen Counter – Any Variation 1 (read)         |                                                                          | 00, 01 (start-stop) 06 (no range, or all)                |                                                          |                                                          |
|                                | 21 1 Frozen Counter – 32-bit with flag               | 1 (read)                                                                 | 06 (no range, or all) 129 (response) 00, 01 (start-stop) |                                                          |                                                          |
|                                | 21 2 Frozen Counter – 16-bit with flag               | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                |                                                          | 129 (response) 00, 01 (start-stop)                       |
| 21 5                           | Frozen Counter – 32-bit with flag and time           | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                | 129 (response)                                           | 00, 01 (start-stop)                                      |

Table 50 - Implementation Table for Series B and Series C controllers (Continued)

| DNP Object Group & Variation   | DNP Object Group & Variation                          | Request DNP3 Master could issue Controller must parse                    | Request DNP3 Master could issue Controller must parse   | Response DNP3 Master must parse Controller could issue   | Response DNP3 Master must parse Controller could issue   |
|--------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                |                                                       | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) |                                                         | Function Codes (dec)                                     | Qualifier Codes (hex)                                    |
| 21 6                           | Frozen Counter – 16-bit with flag and time            | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                | 21 9 Frozen Counter – 32-bit without flag             | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 21 10 Frozen Counter – 16-bit without flag            | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 22 0 Counter Event – Any Variation 1 (read)           |                                                                          | 06 (no range, or all) 07, 08 (limited qty)              |                                                          |                                                          |
|                                | 22 1 Counter Event – 32-bit with flag                 | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 22 2 Counter Event – 16-bit with flag                 | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 22 5                           | Counter Event – 32-bit with flag and time             | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 22 6                           | Counter Event – 16-bit with flag and time             | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 23 0 Frozen Counter Event – Any Variation             | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              |                                                          |                                                          |
| 23 1                           | Frozen Counter Event – 32-bit with flag               | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 23 2 Frozen Counter Event – 16-bit with flag 1 (read) |                                                                          | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 23 5                           | Frozen Counter Event – 32-bit with flag and time      | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 23 6                           | Frozen Counter Event – 16-bit with flag and time      | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 30 0 Analog Input – Any Variation 1 (read)            |                                                                          | 00, 01 (start-stop) 06 (no range, or all)               |                                                          |                                                          |
|                                | 30 1 Analog Input – 32-bit with flag                  | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 30 2 Analog Input – 16-bit with flag                  | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 30 3 Analog Input – 32-bit without flag               | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
|                                | 30 4 Analog Input – 16-bit without flag               | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               |                                                          | 129 (response) 00, 01 (start-stop)                       |
| 30 5                           | Analog Input – Single-prec flt-pt with flag           | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)               | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                | 32 0 Analog Input Event – Any Variation 1 (read)      |                                                                          | 06 (no range, or all) 07, 08 (limited qty)              |                                                          |                                                          |
| 32 1                           | Analog Input Event – 32-bit without time              | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 32 2                           | Analog Input Event – 16-bit without time              | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 32 3 Analog Input Event – 32-bit with time            | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 32 4 Analog Input Event – 16-bit with time            | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 32 5                           | Analog Input Event – Single-prec flt-pt without time  | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
| 32 7                           | Analog Input Event – Single-prec flt-pt with time     | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)              | 129 (response) 130 (unsol. resp)                         | 17, 28 (index)                                           |
|                                | 40 0 Analog Output Status – Any Variation 1 (read)    |                                                                          | 00, 01 (start-stop) 06 (no range, or all)               |                                                          |                                                          |
|                                | 40 1 Analog Output Status – 32-bit with flag 1 (read) |                                                                          | 00, 01 (start-stop) 06 (no range, or all)               | 129 (response)                                           | 00, 01 (start-stop)                                      |

Table 50 - Implementation Table for Series B and Series C controllers (Continued)

| DNP Object Group & Variation   | DNP Object Group & Variation                                     | Request DNP3 Master could issue Controller must parse                    | Request DNP3 Master could issue Controller must parse        | Response DNP3 Master must parse Controller could issue   | Response DNP3 Master must parse Controller could issue   |
|--------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                |                                                                  | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) |                                                              | Function Codes (dec)                                     | Qualifier Codes (hex)                                    |
|                                | 40 2 Analog Output Status – 16-bit with flag 1 (read)            |                                                                          | 00, 01 (start-stop) 06 (no range, or all)                    |                                                          | 129 (response) 00, 01 (start-stop)                       |
| 40 3                           | Analog Output Status – Single-prec flt pt with flag                                                                  | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all)                    | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                | 41 1 Analog Output – 32-bit                                      | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack)                 | 17, 27, 28 (index)                                           | 129 (response)                                           | echo of request                                          |
|                                | 41 2 Analog Output – 16-bit                                      | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack)                 |                                                              |                                                          | 17, 27, 28 (index) 129 (response) echo of request        |
|                                | 41 3 Analog Output – Single-prec flt-pt                          | 3 (select) 4 (operate) 5 (direct op) 6 (dir. op, no ack)                 | 17, 27, 28 (index)                                           | 129 (response)                                           | echo of request                                          |
|                                | 50 1 Time and Date – Absolute time                               | 1 (read)                                                                 | 07 (limited qty = 1)                                         | 129 (response)                                           | 07 (limited qty) (qty = 1)                               |
|                                |                                                                  |                                                                          | 2 (write) 07 (limited qty = 1)                               |                                                          |                                                          |
| 50 3                           | Time and Date – Absolute time at last recorded time              | 2 (write)                                                                | 07 (limited qty = 1)                                         |                                                          |                                                          |
| 51 1                           | Time and Date CTO – Absolute time, synchronized                  |                                                                          |                                                              | 129 (response) 130 (unsol. resp)                         | 07 (limited qty) (qty = 1)                               |
| 51 2                           | Time and Date CTO – Absolute time, unsynchronized                |                                                                          |                                                              | 129 (response) 130 (unsol. resp)                         | 07 (limited qty) (qty = 1)                               |
|                                |                                                                  |                                                                          | 52 2 Time Delay – Fine 129 (response)                        |                                                          | 07 (limited qty) (qty = 1)                               |
|                                | 60 1 Class Objects – Class 0 data 1 (read) 06 (no range, or all) |                                                                          |                                                              |                                                          |                                                          |
|                                | 60 2 Class Objects – Class 1 data                                | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty) 20 (enbl. unsol.) |                                                          |                                                          |
|                                | 60 3 Class Objects – Class 2 data 1 (read)                       |                                                                          | 06 (no range, or all) 07, 08 (limited qty)                   |                                                          |                                                          |
|                                | 60 4 Class Objects – Class 3 data                                | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)                   |                                                          |                                                          |
|                                |                                                                  | 20 (enbl. unsol.) 21 (dab. unsol.)                                       | 06 (no range, or all)                                        |                                                          |                                                          |
|                                | 70 2 File-Control – authentication                               | 29 (authenticate file)                                                   | 5B (free format)                                             | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 3 File Control – file command                                 | 25 (open file)                                                           | 5B (free format)                                             |                                                          |                                                          |
|                                | 70 3 File Control – file command                                 | 27 (delete file)                                                         | 5B (free format)                                             |                                                          |                                                          |
|                                | 70 4 File Control – file command status                          | 26 (close file)                                                          | 5B (free format)                                             | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 4 File Control – file command status                          | 30 (close file)                                                          | 5B (free format)                                             | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 5 File Control – file transport                               | 1 (read file)                                                            | 5B (free format)                                             | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 5 File Control – file transport                               | 2 (write file)                                                           | 5B (free format)                                             | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 6 File Control – file transport status                        |                                                                          |                                                              | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 7 File-Control – file descriptor                              | 28 (get file info)                                                       | 5B (free format)                                             | 129 (response)                                           | 5B (free format)                                         |
|                                | 70 8 File-Control – file specification string                    | 31 (activate config)                                                     | 5B (free format)                                             |                                                          |                                                          |
|                                |                                                                  | 1 (read)                                                                 | 00, 01 (start-stop)                                          | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                | 80 1 Internal Indications – Packed format                        | 2 (write)                                                                | 00 (start-stop) index=7                                      |                                                          |                                                          |
|                                | 85 0 Data-Set Prototype                                          | 1 (read)                                                                 | 06 (no range, or all)                                        |                                                          |                                                          |
|                                | 85 1 Data-Set Prototype                                          | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all) 17, 28 (index)     | 129 (response)                                           | 5B (free format)                                         |

Table 50 - Implementation Table for Series B and Series C controllers (Continued)

| DNP Object Group & Variation                            | DNP Object Group & Variation                            | Request DNP3 Master could issue Controller must parse                    | Request DNP3 Master could issue Controller must parse    | Response DNP3 Master must parse Controller could issue   | Response DNP3 Master must parse Controller could issue   |
|---------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                                         |                                                         | Group Num Var Num Description Function Codes (dec) Qualifier Codes (hex) |                                                          | Function Codes (dec)                                     | Qualifier Codes (hex)                                    |
|                                                         | 86 1 Data-Set Descriptor – Contents                     | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all) 17, 28 (index) | 129 (response)                                           | 5B (free format)                                         |
|                                                         | 86 2 Data-Set Descriptor – Characteristics              | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all) 17, 28 (index) | 129 (response)                                           | 5B (free format)                                         |
|                                                         | 87 0 Data-Set – Present Value                           | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all) 17, 28 (index) |                                                          |                                                          |
|                                                         | 87 1 Data-Set – Present Value                           | 1 (read)                                                                 | 00, 01 (start-stop) 06 (no range, or all) 17, 28 (index) | 129 (response)                                           | 5B (free format)                                         |
|                                                         | 88 0 Data-Set Event                                     | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)               |                                                          |                                                          |
|                                                         | 88 1 Data-Set Event – Snapshot                          | 1 (read)                                                                 | 06 (no range, or all) 07, 08 (limited qty)               | 129 (response) 130 (unsol. resp)                         | 5B (free format)                                         |
|                                                         | 90 1 Application – Identifier                           | 16 (init. appl.) 17 (start appl.) 18 (stop appl.)                        | 06 (no range, or all) 5B (free format)                   |                                                          |                                                          |
|                                                         | 91 1 Status of Requested Operation                      |                                                                          |                                                          | 129 (response)                                           | 07 (limited qty) (qty = 1)                               |
| 101 0                                                   | Binary Coded Decimal Integers – Any Variation           | 1 (read)                                                                 | 06 (no range, or all)                                    |                                                          |                                                          |
|                                                         | 101 1 Binary Coded Decimal Integers – Small 1 (read)    |                                                                          | 06 (no range, or all)                                    | 129 (response)                                           | 00, 01 (start-stop)                                      |
|                                                         |                                                         |                                                                          |                                                          | 130 (unsol. resp)                                        | 17, 28 (index)                                           |
|                                                         | 120 1 Authentication – Challenge                        | 32 (Auth Request)                                                        | 5B (free format)                                         | 131 (Auth. resp)                                         | 5B (free format)                                         |
|                                                         | 120 2 Authentication – Reply                            | 32 (Auth Request)                                                        | 5B (free format)                                         | 131 (Auth. resp)                                         | 5B (free format)                                         |
| 120 3                                                   | Authentication – Aggressive Mode Request                | Any requests                                                             | 07 (limited qty)                                         | 129 (response)                                           | 07 (limited qty)                                         |
| 120 3                                                   | Authentication – Aggressive Mode Request                |                                                                          |                                                          | 130 (unsol. resp)                                        | 07 (limited qty)                                         |
| 120 4                                                   | Authentication – Session Key Status Request             | 32 (Auth Request)                                                        | 07 (limited qty)                                         |                                                          |                                                          |
|                                                         | 120 5 Authentication – Session Key Status               |                                                                          |                                                          | 131 (Auth. resp)                                         | 5B (free format)                                         |
|                                                         | 120 6 Authentication – Session Key Change               | 32 (Auth Request)                                                        | 5B (free format)                                         |                                                          |                                                          |
|                                                         | 120 7 Authentication – Error                            | 33 (Auth Request, no ack) 5B (free format)                               |                                                          | 131 (Auth. resp)                                         | 5B (free format)                                         |
|                                                         | 120 7 Authentication – Error                            | 1 (read)                                                                 | 06 (no range, or all)                                    | 129 (response)                                           | 5B (free format)                                         |
|                                                         | 120 9 Authentication – HMAC                             | Any requests                                                             | 5B (free format)                                         | 129 (response)                                           | 5B (free format)                                         |
|                                                         | 120 9 Authentication – HMAC                             |                                                                          |                                                          | 130 (unsol. resp)                                        | 5B (free format)                                         |
| No Object (function code only) 13 (cold restart)        | No Object (function code only) 13 (cold restart)        | No Object (function code only) 13 (cold restart)                         |                                                          |                                                          |                                                          |
| No Object (function code only)                          | No Object (function code only)                          | 14 (warm restart)                                                        |                                                          |                                                          |                                                          |
| No Object (function code only) 23 (delay meas.)         | No Object (function code only) 23 (delay meas.)         | No Object (function code only) 23 (delay meas.)                          |                                                          |                                                          |                                                          |
| No Object (function code only) 24 (record current time) | No Object (function code only) 24 (record current time) | No Object (function code only) 24 (record current time)                  |                                                          |                                                          |                                                          |

## MicroLogix 1400 Controllers and Ethernet Communication

## MicroLogix 1400 Performance Considerations

<!-- image -->

## Connect to Networks Via Ethernet Interface

Ethernet is a local area network that provides communication between various devices @ 10…100 Mbps. The physical communication media options for the MicroLogix 1400 are:

- Built-in
- Twisted-pair (10/100Base-T)
- With media converters or hubs
- Fiber-optic
- Broadband
- Thick-wire coaxial cable (10Base-5)
- Thin-wire coaxial cable (10Base-2)

See the following page for more information on Ethernet physical media.

The MicroLogix 1400 supports Ethernet communication via the Ethernet communication channel 1 shown.

<!-- image -->

Actual performance of a MicroLogix 1400 controller varies according to:

- Size of Ethernet messages
- Frequency of Ethernet messages
- Network loading
- The implementation of and performance of your processor application program

Table 51 - Optimal Performance: MicroLogix 1400 controller to MicroLogix 1100 Series B and Series C OS FRN 4 Controller (2-node Ethernet network)

|                    | Operation Words MSG per Second Words per Second   |
|--------------------|---------------------------------------------------|
| Single Typed Read  | 1 20 20                                           |
| Single Typed Reads | 20 20 400                                         |
| Single Typed Reads | 100 20 2000                                       |

## MicroLogix 1400 and PC Connections to the Ethernet Network

Table 52 - Optimal Performance: MicroLogix 1400 controller to RSLinx

|             | Operation Words MSG per Second Words per Second   |
|-------------|---------------------------------------------------|
| 1 25 25     | Single Typed Read                                 |
| 20 25 500   | Single Typed Reads                                |
| 100 25 2500 | Single Typed Reads                                |

Table 53 - Optimal Performance: MicroLogix 1400 to MicroLogix 1400 Controller

|           | Operation Words MSG per Second Words per Second   |
|-----------|---------------------------------------------------|
| 1 20 20   | Single Typed Read                                 |
| 20 20 400 | Single Typed Reads                                |
|           | Single Typed Reads  100 20 2000                   |

The MicroLogix 1400 Ethernet connector conforms to ISO/IEC 8802-3 STD 802.3 and uses 10/100Base-T media. Connections are made directly from the MicroLogix 1400 to an Ethernet hub or switch. The network setup is simple and cost-effective. Typical network topology is pictured in Figure 81 on page 268 .

Figure 81 - Ethernet Network Topology

<!-- image -->

## IMPORTANT

The MicroLogix 1400 controller contains a 10/100Base-T, RJ45 Ethernet connector that connects to standard Ethernet hubs or switches via 8-wire twisted-pair straight-through cable. To access other Ethernet mediums, use 10/100Base-T media converters or Ethernet hubs or switches that can be connected together via fiber, thin-wire, or thick-wire coaxial cables, or any other physical media commercially available with Ethernet hubs or switches.

## Connecting an Ethernet switch on the Ethernet Network

The MicroLogix 1400 Ethernet port supports the following Ethernet settings:

- 10 Mbps half-duplex or full-duplex
- 100 Mbps half-duplex or full-duplex

Mode selection can be automatic, based on the IEEE 802.3 auto negotiation protocol. In most cases, using the auto negotiation function results in proper operation between a switch port and MicroLogix 1400 Ethernet port.

With RSLogix 500/RSLogix Micro programming software version 8.10.00 or later, you can manually set the communication rate and duplex mode of an Ethernet port you have connected to the switch port. The settings of the Ethernet port and the switch port must match.

## IMPORTANT

When connecting the MicroLogix 1400 Ethernet port to a 10/100Base-T Ethernet switch, note the following recommendations:

- Use the auto negotiation function for both the switch port and the MicroLogix 1400 Ethernet port
- If you want to force to a specific speed/duplex mode, you must force both the MicroLogix 1400 Ethernet port and the switch port to the same setting.

## Cables

Shielded and non-shielded twisted-pair 10/100Base-T cables with RJ45 connectors are supported. The maximum cable length between a MicroLogix 1400 Ethernet port and a 10/100Base-T port on an Ethernet hub or switch (without repeaters or fiber) is 100 m (323 ft). However, in an industrial application, keep the cable length to a minimum.

<!-- image -->

The Ethernet cabling with straight-through method is recommended as shown in Table 54. Do not make the incorrect connection.

Table 54 - Straight-through Cabling

| Pin Pin Name Cable color              |
|---------------------------------------|
| 1 Tx+ Orange/white                    |
| 2 Tx- Orange                          |
| 3 Rx+ Green/white                     |
| 4 No used by 10/100Base-T Blue        |
| 5 No used by 10/100Base-T Blue/white  |
| 6 Rx- Green                           |
| 7 No used by 10/100Base-T Brown/white |
| 8 No used by 10/100Base-T Brown       |

The standard Ethernet cable is ended in accordance with EIA/TIA 568B on both ends. The crossover cable is ended to EIA/TIA 568B at one end and EIA/TIA 568A at the other, exactly as shown in the two color-coded plugs.

Figure 82 and Figure 83 show how the TIA/EIA 568A and 568B are to be ended. There are four pairs of wires that are contained in a CAT5 UTP cable. These pairs of cables are color-coded white blue/ blue, white orange/orange, white green/green, white brown/brown, they are also numbered one to four in the order shown.

Figure 82 - EIA/TIA 568A and 568B Ethernet Cable

<!-- image -->

Figure 83 - EIA/TIA 568A and 568B Termination

<!-- image -->

## Ethernet Connections

## Duplicate IP Address Detection

<!-- image -->

The most common wiring for RJ45 cables is the straight through cable that means that pin 1 of the plug on one end is connected to pin 1 of the plug on the other end. The straight-through RJ45 cable is commonly used to connect network cards with hubs on 10Base-T and 100Base-Tx networks. On network cards, pair 1…2 is the transmitter, and pair 3…6 is the receiver. The other two pairs are not used. On hub pairs 1…2 is the receiver and 3…6 the transmitter. Wire your cables with the same color sequence. In this cable layout, all pins are wired one-for-one to the other side. The pins on the RJ45 connector are assigned in pairs, and every pair carries one differential signal. Each line pair has to be twisted.

In small networks where only two Ethernet devices must be connected together pointto-point, you could require a cross-over RJ45 cable, where the transmit and receive lines on both JR45 connectors are cross connected. The color coding for the cross over RJ45 cable have been defined in the EIA/TIA 568A standard. In a cross-over cable layout, remember that one end is normal, and the other end has the cross-over configuration.

However, because the MicroLogix 1400 Ethernet port implements auto-crossover (also called Automatic MDI/MDI-X Configuration), you can use a straight through cable even for direct point-to-point connections between the MicroLogix 1400 and another Ethernet device.

TCP/IP is the mechanism that is used to transport Ethernet messages. On top of TCP, EtherNet/IP and/or Modbus TCP protocol is required to establish sessions and to send the MSG commands. You can initiate connections by either a client program (RSLinx application) or a processor.

The client program or processor must first establish a connection to the MicroLogix 1400 to enable the MicroLogix 1400 to receive solicited messages from a client program or another processor.

To send an outgoing message, the MicroLogix 1400 must first establish a connection with the destination node at a specified IP address on the Ethernet network. A connection is established when a MSG instruction executes and no previous connection exists.

When an MSG instruction executes, the MicroLogix 1400 checks to see whether a connection has been established with the destination node. If a connection has not been established, the MicroLogix 1400 attempts to establish a connection of the peer type.

To receive messages from another device on Ethernet, an "incoming" connection must be established. This incoming connection is made by the sending processor and uses one incoming connection in the receiving processor.

The MicroLogix 1400 supports a maximum of 32 EtherNet/IP connections and 32 Modbus TCP connections, allowing a maximum of 32 outgoing and a maximum of 32 incoming simultaneous connections with up to 64 other devices or applications. The connections are dedicated as follows:

| Number of Connections(1)        | Dedicated to:                                                   |
|---------------------------------|-----------------------------------------------------------------|
|                                 | 16 Incoming EtherNet/IP connections                             |
|                                 | 16 (Series B and Series C only) Incoming Modbus TCP connections |
|                                 | 16 Outgoing EtherNet/IP connections                             |
| 16 (Series B and Series C only) | Outgoing Modbus TCP connections                                 |

## IMPORTANT

For outgoing connections, no more that one connection per destination node is established. If multiple MSG instructions use the same destination node, they share connection.

The MicroLogix 1400 firmware supports duplicate IP address detection. In Series B and Series C, duplicate IP address detection can be disabled in the Channel 1 configuration to eliminate this source of broadcast traffic for low-bandwidth applications.

## Configure the Ethernet Channel on the MicroLogix 1400

Table 55 - Configuration Parameters

|                       | Parameter Description                                                                                                                                                                                                                                                                                                                  | Default Status                       |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
|                       | Hardware Address The MicroLogix 1400 Ethernet hardware address.                                                                                                                                                                                                                                                                        | Ethernet hardware address  Read-only |
| IP Address            | The MicroLogix 1400 Internet address (in network byte order). The Internet address must be specified to connect to the TCP/IP network.                                                                                                                                                                                                 | 0 (undefined) Read/write             |
| Subnet Mask           | The MicroLogix 1400 subnet mask (in network byte order). The Subnet Mask is used to interpret IP addresses when the internet is divided into subnets. A Subnet Mask of all zeros indicates that no subnet mask has been configured. In this case, the controller assumes a Subnet Mask of 255.255.255.0.                               | 0 (undefined) Read/write             |
| Gateway Address       | The address of a gateway (in network byte order) that provides a connection to another IP network. A Gateway Address of all zeros indicates that no gateway has been configured. In this case, the controller assumes a Gateway Address of aaa.bbb.ccc.001, where aaa.bbb.ccc are the first three octets of the configured IP address. | 0 (undefined) Read/write             |
| Default Domain Name   | The default domain name can have the following formats: ’a.b.c’, ’a.b’ or ’a’, where a, b, c must start with a letter, end with a letter or digit, and have as interior characters only letters, digits, or hyphens. The maximum length is 63 characters.                                                                              | NULL (undefined)  Read/write         |
|                       | Primary Name Server The IP address of the computer acting as the local Ethernet network Primary Domain Name System (DNS) server. 0 (undefined) Read/write                                                                                                                                                                              |                                      |
| Secondary Name Server | The IP address of the computer acting as the local Ethernet network Secondary Domain Name System (DNS) server. 0 (undefined) Read/write                                                                                                                                                                                                |                                      |
| BOOTP Enable          | The BOOTP enable switch. When BOOTP is enabled, the MicroLogix 1400 attempts to learn its network-related parameters at power-up via a BOOTP request. There must be a BOOTP server on the network that can respond to the BOOTP request. When both BOOTP and DHCP are disabled, the MicroLogix 1400 uses the locally configured network related parameters (IP address, Subnet Mask, Broadcast Address, and so on).                                                                                                                                                                                                                                                                                                                                        | 1 (enabled) Read/write               |
| DHCP Enable           | The DHCP auto configuration enable the switch. When DHCP is enabled, a DHCP server automatically assigns network related parameters to the MicroLogix 1400 when it signs in a TCP/IP network. There must be a DHCP server on the network capable of allocating network addresses and configuring parameters to the newly attached device. When both BOOTP and DHCP are disabled, the MicroLogix 1400 uses the locally configured network-related parameters (IP address, Subnet Mask, Broadcast Address, and so on).                                                                                                                                                                                                                                                                                                                                        | 0 (disabled) Read/write              |
|                       | SNMP Server Enable SNMP enable switch. Select to enable SNMP (Simple Network Management Protocol). 1 (enabled) Read/write                                                                                                                                                                                                              |                                      |

When you change the IP address or connect one of the MicroLogix to an EtherNet/IP network, the MicroLogix 1400 controller checks to make sure that the IP address that is assigned to this device does not match the address of any other network device. The MicroLogix 1400 checks every 2 minutes for a duplicate IP address on the network. If the MicroLogix 1400 determines that there is a conflict (another device on the network with a matching IP address), the following message gets posted on the LCD display.

<!-- image -->

To correct this conflict, use the instructions in this chapter to change the IP address of the EtherNet/IP device. Then cycle power to the device or reset the device (such as disconnecting the Ethernet cable and reconnecting the cable).

There is also the possibility that two EtherNet/IP devices can detect a conflict simultaneously. If this occurs, remove the device with the incorrect IP address or correct its conflict. To get the second device out of conflict mode, cycle power to the module or disconnect its Ethernet cable and reconnect the cable. The MicroLogix 1400 checks every 2 minutes for a duplicate IP address on the network.

There are three ways to configure the MicroLogix 1400 Ethernet channel 1.

- Via a BOOTP or DHCP request at the controller power-up
- Manually setting the configuration parameters using RSLogix 500/RSLogix Micro Programming Software
- Via LCD display (see Configure the Ethernet Port and Configure Ethernet Protocol Setup)

The configuration parameters are shown on the following page, and the configuration procedures follow.

Table 55 - Configuration Parameters (Continued)

|                                          | Parameter Description                                                                                                                                                                                                                                                                                                                                                                    | Default Status                                                                           |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| SMTP Client Enable                       | The SMTP Client service enable switch. When SMTP is enabled, MicroLogix 1400 can transmit email messages that are generated by a 485CIF write message with a string element. There must be an SMTP process email service. This provides an versatile mechanism to report alarms, status, and other data-related functions.                                                               | 0 (disabled) Read/write                                                                  |
| Auto Negotiate and Port Setting          | When Auto Negotiate is disabled (unchecked), the Ethernet speed/duplex is forced to either 10 Mbps/Half-duplex, 10 Mbps/Full-duplex, 100 Mbps/Half-duplex, or 100 Mbps/Full-duplex, as selected in the Port Setting field. When Auto Negotiate is enabled (checked), the Port Setting Field allows you to select the range of speed/duplex settings that the MicroLogix 1400 negotiates. | Auto Negotiate enabled and Port Setting. 10/100 Mbps Full Duplex/ Half Duplex Read/write |
| MSG Connection Timeout                   | The amount of time (in ms) allowed for an MSG instruction to establish a connection with the destination node. The MSG Connection Timeout has 250 ms resolution and a range from 250…65,500.                                                                                                                                                                                             | 15,000 ms Read/write                                                                     |
| MSG Reply Timeout                        | The amount of time (in ms) that the MicroLogix 1400 waits for a reply to a command that it has initiated via an MSG instruction. The MSG Reply Timeout has 250 ms resolution and a range from 250…65,500.                                                                                                                                                                                | 3000 ms Read/write                                                                       |
| Inactivity Timeout                       | The amount of time (in minutes) that an MSG connection could remain inactive before it is ended. The Inactivity Timeout has a 1 minute resolution and a range from 1…65,500 minutes.                                                                                                                                                                                                     | 30 minutes. Read/write                                                                   |
|                                          | Contact The Contact string that the SNMP client specifies. The maximum length is 63 characters. Read-only                                                                                                                                                                                                                                                                                |                                                                                          |
|                                          | Location The Location string that the SNMP client specifies. The maximum length is 63 characters. Read-only                                                                                                                                                                                                                                                                              |                                                                                          |
| Network Link ID                          | The Link ID assigned to the MicroLogix 1400 controller by either an RSLinx OPC topic or by the routing table in a 1756-DHRIO or 1756-DH485 module. The range is 0…199.                                                                                                                                                                                                                   | 0 Read/write                                                                             |
| Starting Data File Number                | The first ASCII (A) file number in a contiguous block of 4…32 ASCII files (4 per User Provided Web Page). The range is 9…252 (or 0 for disable).                                                                                                                                                                                                                                         | 0 Read/write                                                                             |
|                                          | Number of Pages The number of User Provided Web Pages, provided the Starting Data File Number is nonzero. The range is 1…8. 1 Read/write                                                                                                                                                                                                                                                 |                                                                                          |
| DNP3 over IP Enable                      | When DNP3 over IP is enabled (checked), the MicroLogix 1400 enables DNP3 over IP feature on the Ethernet channel. You must power cycle for the changes to take effect.                                                                                                                                                                                                                   | 0 (disable) Read/write                                                                   |
| Modbus TCP Enable                        | When Modbus TCP is enabled (checked), the MicroLogix 1400 enables the Modbus TCP feature on the Ethernet channel. You must power cycle for the changes to take effect.                                                                                                                                                                                                                   | 0 (disable) Read/write                                                                   |
| Disable EtherNet/IP Incoming Connections | When EtherNet/IP Incoming Connections is disabled (checked), the MicroLogix 1400 does not allow the incoming EtherNet/IP connection. However, MicroLogix 1400 can send the outgoing EtherNet/IP commands to other EtherNet/IP devices. You must power cycle for the changes to take effect.                                                                                              | 0 (disable) Read/write                                                                   |
| Disable Duplicate IP address Detection   | When Duplicate IP address Detection is disabled (checked), the MicroLogix 1400 does not send any packets to the network to detect Duplicate IP on the same network.                                                                                                                                                                                                                      | 0 (disable) Read/write                                                                   |

## Configure Using RSLogix 500/RSLogix Micro Programming Software

## Configure Using BOOTP

See the online documentation provided with your programming software.

Bootstrap Protocol (BOOTP) is a low-level protocol that TCP/IP nodes use to obtain startup information. By default, the MicroLogix 1400 broadcasts BOOTP requests at power-up. The BOOTP Valid parameter remains clear until a BOOTP reply has been received. BOOTP lets you dynamically assign IP addresses to processors on the Ethernet Link.

To use BOOTP, a BOOTP Server must exist on the local Ethernet subnet. The server is a computer that has BOOTP Server software that is installed and reads a text file containing the network information for individual nodes on the network.

The host system's BOOTP configuration file must be updated to service requests from MicroLogix 1400 controllers. The following parameters must be configured:

Table 56 - Configuration Parameters

|             | Parameter Description                                                                                                            |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|
|             | IP address A unique IP address for the MicroLogix 1400 controller.                                                               |
| Subnet Mask | Specifies the net and local subnet mask as per the standard on subnetting RFC 950, Internet Standard Subnetting Procedure.       |
| Gateway     | Specifies the IP address of a gateway on the same subnet as the MicroLogix 1400 that provides connections to another IP network. |

When BOOTP is enabled, the following events occur at power-up:

- The processor broadcasts a BOOTP-request message containing its hardware address over the local network or subnet.

- The BOOTP server compares the hardware address with the addresses in its look-up table.
- The BOOTP server sends a message back to the processor with the IP address and other network information that corresponds to the hardware address it received.

With all hardware and IP addresses in one location, you can easily change IP addresses in the BOOTP configuration file if your network must be changed.

The BOOTP request can be disabled by clearing the BOOTP Enable parameter in the channel configuration file. When both BOOTP Enable and DHCP are cleared (disabled), the MicroLogix 1400 uses the existing channel configuration data.

## IMPORTANT

If BOOTP is disabled, or no BOOTP server exists on the network, you must use RSLogix 500/RSLogix Micro programming software to enter/change the IP address for each processor or you must use DHCP instead of it.

## Using the Rockwell Automation BOOTP/DHCP Utility

The Rockwell Automation BOOTP/DHCP server utility is a standalone program that incorporates the functionality of standard BOOTP software with a user-friendly graphical interface. It is located in the Utils directory on the RSLogix 500/RSLogix Micro installation CD.

The newest version of the utility can be downloaded from the Product Compatibility and Download Center at rok.auto/pcdc. The device must have BOOTP enabled (factory default) or DHCP enabled to use the utility.

To configure your device using the BOOTP utility, perform the following steps.

1. Run the BOOTP/DHCP server utility software. It asks you to configure your network settings before using the BOOTP/DHCP server tool. Enter your Ethernet settings for Subnet Mask and Gateway. If you are not sure about it, get a help from your system administrator. Just leave Primary DNS, Secondary DNS, and Domain Name. If the corresponding information is allocated to the PC where the BOOTP/DHCP server utility is installed, enter the same information.

<!-- image -->

2. In the Request History panel you see the hardware addresses of devices that issue BOOTP or DHCP requests.
3. Double-click the hardware address of the device that you want to configure. You see the New Entry pop-up window with the device MAC address.
4. Enter the IP address and Description that you want to assign to the device, and select OK. Leave Hostname blank.

<!-- image -->

<!-- image -->

The device is added to the Relation List, and displays the MAC address and corresponding IP address, Subnet Mask, and Gateway (if applicable).

<!-- image -->

## Use a DHCP Server To Configure Your Processor

A DHCP server automatically assigns IP addresses to client stations logging on to a TCP/IP network. DHCP is based on BOOTP and maintains some backward compatibility. The main difference is that BOOTP was designed for manual configuration, while DHCP allows for dynamic allocation of network addresses and configurations to newly attached devices.

<!-- image -->

ATTENTION: The processor must be assigned a fixed network address. The IP address of the processor must not be dynamically provided. Failure to observe this precaution may result in unintended machine motion or loss of process control.

Subnet Masks and Gateways Configure subnet masks and gateways using the Ethernet Channel 1 configuration screen.

| IMPORTANT   | If BOOTP is enabled, you can’t change any of the advanced Ethernet communications characteristics.   |
|-------------|------------------------------------------------------------------------------------------------------|

If your network is divided into subnetworks that use gateways or routers, you must indicate the following information when configuring Channel 1:

- Subnet mask
- Gateway address

A subnet mask is a filter that a node applies to IP addresses to determine if an address is on the local subnet or on another subnet. If an address is on another subnetwork, messages are routed through a local gateway to be transferred to the destination subnetwork.

If your network is not divided into subnets, then leave the subnet mask field at the default.

| If you Then                                                      |                                                                                                                                |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Manually configure Channel 1 and have a network with subnets     | • Verify that the BOOTP enable field is disabled • Use your programming software to enter the subnet mask and gateway address. |
| Use BOOTP to configure Channel 1 and have a network with subnets | • Verify that BOOTP is enabled • Include the subnet masks and gateway addresses                                                |

## Manually Configure Channel 1 for Controllers on Subnets

If you manually configure Channel 1 for a MicroLogix 1400 controller on a subnet, clear the checkbox for both of the BOOTP Enable and DHCP Enable options, as shown in the figure.

Table 57 - Subnet and Gateway Address Fields

|                 |                                                                                                                                                                       | This field: Specifies: Configure by Doing the Following:                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Subnet Mask     | The controller’s subnet mask. The subnet mask is used to interpret IP addresses when the Internet is divided into subnets.                                            | Enter an address of the following form: a.b.c.d Where: a, b, c, d are between 0...255 (decimal) If your network is not divided into subnets, then leave the subnet mask field at the default. If you change the default and must reset it, type 0.0.0.0. |
| Gateway Address | The IP address of the gateway that provides a connection to another IP network. This field is required when you communicate with other devices not on a local subnet. | Enter an address of the following form: a.b.c.d Where: a, b, c, d are between 0...255 (decimal) The default address is No Gateway.                                                                                                                       |

## MicroLogix 1400 Embedded Web Server Capability

MicroLogix 1400 controllers include not only the embedded web server that allows viewing of module information, TCP/IP configuration, and diagnostic information, but the capabilities that also allow viewing of the data file via Ethernet using a standard web browser.

For more information on MicroLogix 1400 embedded web server capability, see MicroLogix 1400 Embedded Web Server User Manual, publication 1766-UM002 .

Disable the Ethernet Channel Disable the Ethernet channel by performing the following steps:

1. From the status file, set the status bit S:36/0 from 0 to 1.

Figure 84 - Channel 1 Configuration

<!-- image -->

See Table 57 to configure the Subnet Mask and Gateway Address fields for each controller via your programming software.

IMPORTANT You can only change the status bit S:36/0 in an offline project.

<!-- image -->

2. Download the project to the MicroLogix 1400 controller.
3. Perform a power cycle in order for the changes to take effect.

## IMPORTANT

## IMPORTANT

Consider the following when you enable or disable the Ethernet channel using the status bit S:36/0:

- To enable or disable the Ethernet channel, a power cycle on the controller is required for the change of status to take effect.
- If the Ethernet channel is set to disable, the other Ethernet-related protocols must also be set to disable (except for BOOTP as it returns to enable mode even if you set it to disable), in order for the user project to download successfully.
- If the Ethernet channel is in Disable mode (after a power cycle), you cannot set the Ethernet channel and the other Ethernet-related protocols (except for BOOTP) back to Enable mode simultaneously. To do so, you must set the Ethernet channel to enable and perform a power cycle on the controller first before you can enable the other Ethernet-related protocols.
- If the Ethernet channel is disabled and you configured the MSG instruction for channel 1, the instruction indicates an error as the channel is shut down during RUN mode.

At least 1 of the 3 channels must be active to enable communication with the RSLogix 500 software. You cannot disable the Ethernet channel if both serial channels are already configured as disabled. If you attempt to change the status bit S:36/0 from 0 to 1, it reverts to enable (0) after the power cycle.

See also Appendix F for information on how to disable the Incoming EtherNet/IP Connections.

## System Loading Calculations

<!-- image -->

## System Loading and Heat Dissipation

<!-- image -->

A maximum of seven 1762 I/O modules, in any combination, can be connected to a MicroLogix 1400 controller. You can use this appendix to determine the power supply load and heat dissipation for your system.

The MicroLogix 1400 controller is designed to support up to any seven 1762 expansion I/O modules.

When you connect MicroLogix accessories and expansion I/O, an electrical load is placed on the controller power supply. This section shows how to calculate the load of your control system.

The following example is provided to illustrate system loading calculation. The system calculation procedure accounts for the amount of 5V DC and 24V DC current that is consumed by controller, expansion I/O, and user-supplied equipment. Use the System Loading Worksheet to calculate your controller configuration.

## System Loading Example Calculations

Current Loading

Table 58 - Calculating the Current for Expansion I/O

|                                                | n A B n x A n x B                                         |                                                      |
|------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------|
| Catalog Number (1)                             | Device Current Requirements (Max) Calculated Current      | Device Current Requirements (Max) Calculated Current |
| Number of Modules                              | at 5V DC (mA) at 24V DC (mA) at 5V DC (mA) at 24V DC (mA) |                                                      |
| 1762-IA8 2 50 0 100 0                          |                                                           |                                                      |
| 1762-IF4 40 50                                 |                                                           |                                                      |
| 1762-IF2OF2 40 105                             |                                                           |                                                      |
| 1762-IQ8 50 0                                  |                                                           |                                                      |
| 1762-IQ16  70 (2)                              | 0                                                         |                                                      |
| 1762-IQ32T 170 0                               |                                                           |                                                      |
| 1762-IR4 40 50                                 |                                                           |                                                      |
| 1762-IT4 40 50                                 |                                                           |                                                      |
| 1762-OA8 115 0                                 |                                                           |                                                      |
| 1762-OB8 115 0                                 |                                                           |                                                      |
| 1762-OB16 175 0                                |                                                           |                                                      |
| 1762-OB32T 175 0                               |                                                           |                                                      |
| 1762-OF4 40 165                                |                                                           |                                                      |
| 1762-OV32T 175 0                               |                                                           |                                                      |
| 1762-OW8 2 80 90 160 180                       |                                                           |                                                      |
| 1762-OW16 140 2 1802                           |                                                           |                                                      |
| 1762-OX6I 110 110                              |                                                           |                                                      |
| 1762-IQ8OW6 110 80                             |                                                           |                                                      |
| Total Modules (7 maximum): 4 Subtotal: 260 180 |                                                           |                                                      |

## Validating the System

The example systems that are shown in Table 59 and Table 60 are verified to be acceptable configurations. The systems are valid because:

- Calculated Current Values &lt; Maximum Allowable Current Values
- Calculated System Loading &lt; Maximum Allowable System Loading

Table 59 - Validating Systems using 1766-L32AWA, or 1766-L32BXB

| Maximum Allowable Values Calculated Values   | Maximum Allowable Values Calculated Values                                                      |                                                                             |
|----------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Current: Current (Subtotal from Table 58.):  | Current: Current (Subtotal from Table 58.):                                                     |                                                                             |
|                                              | 1225 mA @ 5V DC 1155 mA @ 24V DC 0 mA + 260 mA = 260 mA @ 5V DC 0 mA + 180 mA = 180 mA @ 24V DC |                                                                             |
| System Loading: System Loading:              | System Loading: System Loading:                                                                 |                                                                             |
| 33.845 W                                     | = (260 mA x 5V) + (180 mA x 24V) = (1300 mW) + (4320 mW) = 5620 mW = 5.62 W                     | = (260 mA x 5V) + (180 mA x 24V) = (1300 mW) + (4320 mW) = 5620 mW = 5.62 W |

Table 60 - Validating Systems using 1766-L32BWA

| Maximum Allowable Values Calculated Values                                                               |                                                                                                          |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Sum of all sensor currents                                                                               | Sum of all sensor currents                                                                               |
| 250 mA @ 24V DC 140 mA @ 24V DC (example sensor value)                                                   | 250 mA @ 24V DC 140 mA @ 24V DC (example sensor value)                                                   |
| Current for MicroLogix Accessories and Expansion I/O: Current Values (Subtotal from Table 58):           | Current for MicroLogix Accessories and Expansion I/O: Current Values (Subtotal from Table 58):           |
|                                                                                                          | 1225 mA @ 5V DC 1155 mA @ 24V DC 0 mA + 260 mA = 260 mA @ 5V DC 0 mA + 180 mA = 180 mA @ 24V DC          |
| System Loading: System Loading:                                                                          | System Loading: System Loading:                                                                          |
| = (140 mA x 24V) + (260 mA x 5V) + (180 mA x 24V) = (3360 mW) + (1300 mW) + (4320 mW) = 8980 mW = 8.98 W | = (140 mA x 24V) + (260 mA x 5V) + (180 mA x 24V) = (3360 mW) + (1300 mW) + (4320 mW) = 8980 mW = 8.98 W |

## System Loading Worksheet

Table 61 , Table 62, and Table 63 are provided for system loading validation. See System Loading Example Calculations .

## Current Loading

Table 61 - Calculating the Current for Expansion I/O

|                    | n A B n x A n x B                                     |                                                |
|--------------------|-------------------------------------------------------|------------------------------------------------|
| Number of Modules  | Device Current Requirements Calculated Current        | Device Current Requirements Calculated Current |
|                    | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                |
| 1762-IA8 50 0      |                                                       |                                                |
| 1762-IF4 40 50     |                                                       |                                                |
| 1762-IF2OF2 40 105 |                                                       |                                                |
| 1762-IQ8 50 0      |                                                       |                                                |
| 1762-IQ16 70 0     |                                                       |                                                |
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

| 1762-OX6I 110 110                    |
|--------------------------------------|
| 1762-IQ8OW6 110 80                   |
| Total Modules (7 maximum): Subtotal: |

1762-OX6I 110 110

1762-IQ8OW6 110 80

## Total Modules (7 maximum): Subtotal:

- (1) See your expansion I/O Installation Instructions for Current Requirements not listed in this table.

- [ ] (2) Only applicable for Series B and Series C I/O modules.

## Table 61 - Calculating the Current for Expansion I/O (Continued)

## Table 62 - Validating Systems using 1766-L32AWA or 1766-L32BXB

## Maximum Allowable Values Calculated Values

Current: Current (Subtotal from Table 61):

1225 mA at 5V DC 1155 mA at 24V DC mA @ 5V DC mA @ 24V DC

System Loading: System Loading:

33.845 W

= (\_\_\_\_\_\_\_\_ mA x 5V) + (\_\_\_\_\_\_\_\_ mA x 24V)

- [ ] = \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW

- [ ] = \_\_\_\_\_\_\_\_\_\_ mW

- [ ] = \_\_\_\_\_\_\_\_\_\_ W

## Table 63 - Validating Systems using 1766-L32BWA

## Maximum Allowable Values Calculated Values

Current for Devices Connected to the +24V DC Sensor Supply: Sum of all sensor currents

250 mA @ 24V DC mA @ 24V DC

Current for MicroLogix Accessories and Expansion I/O: Current (Subtotal from Table 61.)

1225 mA @ 5V DC 1155 mA @ 24V DC mA @ 5V DC mA @ 24V DC

System Loading: System Loading:

39.845 W

= (\_\_\_\_\_\_\_\_ mA x 24V) + (\_\_\_\_\_\_\_\_ mA x 5V) + (\_\_\_\_\_\_\_\_ mA x 24V)

- [ ] = \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW

- [ ] = \_\_\_\_\_\_\_\_\_\_ mW

= \_\_\_\_\_\_\_\_\_\_ W

## Calculating Heat Dissipation

Table 64 - Heat Dissipation

| Heat Dissipation                                                                                                                                            | Heat Dissipation   | Heat Dissipation   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|
| Catalog Number  Equation or Constant Calculation Sub-Total                                                                                                  |                    |                    |
| 1766-L32AWA 15.2 W + (0.4 x System Loading) 15.2 W + (0.4 x ______ W) W                                                                                     |                    |                    |
| 1766-L32BWA 15.7 W + (0.4 x System Loading) 15.7 W + (0.4 x ______ W) W                                                                                     |                    |                    |
| 1766-L32BXB 17.0 W + (0.3 x System Loading) 17.0 W + (0.3 x ______ W) W                                                                                     |                    |                    |
| 1762-IA8 2.0 W x number of modules 2.0 W x _________ W                                                                                                      |                    |                    |
| 1762-IF4 2.0 W x number of modules 2.0 W x _________ W                                                                                                      |                    |                    |
| 1762-IF2OF2 2.6 W x number of modules 2.6 W x _________ W                                                                                                   |                    |                    |
| 1762-IQ8 3.7 W x number of modules 3.7 W x _________ W                                                                                                      |                    |                    |
| 1762-IQ16 5.4 W1 x number of modules 5.4 W1 x _________ W                                                                                                   |                    |                    |
| 1762-IQ32T  6.8 W x number of modules (@ 30.0V DC) 5.4 W x number of modules (@ 26.4V DC) 6.8 W x _________ (@ 30.0V DC) 5.4 W x _________ (@ 26.4V DC) W W |                    |                    |
| 1762-IR4 1.5 W x number of modules 1.5 W x _________ W                                                                                                      |                    |                    |
| 1762-IT4 1.5 W x number of modules 1.5 W x _________ W                                                                                                      |                    |                    |
| 1762-OA8 2.9 W x number of modules 2.9 W x _________ W                                                                                                      |                    |                    |
| 1762-OB8 1.6 W x number of modules 1.6 W x _________ W                                                                                                      |                    |                    |
| 1762-OB16 2.9 W x number of modules 2.9 W x _________ W                                                                                                     |                    |                    |
| 1762-OB32T 3.4 W x number of modules 3.4 W x _________ W                                                                                                    |                    |                    |
| 1762-OF4 3.8 W x number of modules 3.8 W x _________ W                                                                                                      |                    |                    |
| 1762-OV32T 2.7 W x number of modules 2.7 W x _________ W                                                                                                    |                    |                    |
| 1762-OW8 2.9 W x number of modules 2.9 W x _________ W                                                                                                      |                    |                    |
| 1762-OW16  6.1 W(1) x number of modules  6.1 W1 x _________ W                                                                                               |                    |                    |
| 1762-OX6I 2.8 W x number of modules 2.8 W x _________ W                                                                                                     |                    |                    |
| 1762-IQ8OW6 4.4 W x number of modules 4.4 W x _________ W                                                                                                   |                    |                    |

.

Use the following table when you must determine the heat dissipation of your system for installation in an enclosure. For System Loading, take the value from the appropriate system loading worksheets on pages 280 or 281 .

The following terms and abbreviations are used throughout this manual.

address

A character string that uniquely identifies a memory location. For example, I:1/0 is the memory address for the data located in the Input file location word1, bit 0.

AIC+ Advanced Interface Converter

A device that provides a communication link between various networked devices. (Catalog Number 1761-NET-AIC.)

application 1) A machine or process monitored and controlled by a controller.

- 2) The use of computer- or processor-based routines for specific purposes.

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

control profile The means by which a controller determines which outputs turn on under what conditions.

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

1) A rotary device that transmits position information.

- 2) A device that transmits a fixed number of pulses for each revolution.

executing mode Any run or test mode.

<!-- image -->

expansion I/O

Expansion I/O is I/O that is connected to the controller via a bus or cable. MicroLogix 1400 controllers use Bulletin 1762 expansion I/O.

false

The status of an instruction that does not provide a continuous logical path on a ladder rung.

FIFO (First-In-First-Out)

The order that data is entered into and retrieved from a file.

file

A collection of information organized into one group.

full-duplex A bidirectional mode of communication where data may be transmitted and received simultaneously (contrast with half-duplex).

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

negative logic The use of binary logic in such a way that "0" represents the voltage level normally associated with logic 1 (for example, 0 = +5V, 1 = 0V). Positive is more conventional (for example, 1 = +5V, 0 = 0V).

network

A series of stations (nodes) connected by some type of communication medium. A network may be made up of a single link or multiple links.

nominal input current The current at nominal input voltage.

normally closed normally open

Contacts on a relay or switch that are closed when the relay is de-energized or the switch is deactivated; they are open when the relay is energized or the switch is activated. In ladder programming, a symbol that allows logic continuity (flow) if the referenced input is logic "0" when evaluated.

Contacts on a relay or switch that are open when the relay is de-energized or the switch is deactivated. (They are closed when the relay is energized or the switch is activated.) In ladder programming, a symbol that allows logic continuity (flow) if the referenced input is logic "1" when evaluated.

off-delay time The OFF delay time is a measure of the time required for the controller logic to recognize that a signal has been removed from the input terminal of the controller. The time is determined by circuit component delays and by any filter adjustment applied.

offline

Describes devices not under direct communication.

offset

The steady-state deviation of a controlled variable from a fixed point.

off-state leakage current When an ideal mechanical switch is opened (off-state) no current flows through the switch. Practical semiconductor switches, and the transient suppression components which are sometimes used to protect switches, allow a small current to flow when the switch is in the off state. This current is referred to as the off-state leakage current. To ensure reliable operation, the off-state leakage current rating of a switch should be less than the minimum operating current rating of the load that is connected to the switch.

on-delay time The ON delay time is a measure of the time required for the controller logic to recognize that a signal has been presented at the input terminal of the controller.

one-shot online

operating voltage

A programming technique that sets a bit for only one program scan.

Describes devices under direct communication. For example, when RSLogix 500/RSLogix Micro is monitoring the program file in a controller.

For inputs, the voltage range needed for the input to be in the On state. For outputs, the allowable range of user-supplied voltage.

output device A device, such as a pilot light or a motor starter coil, that is controlled by the controller.

processor

A Central Processing Unit. See CPU (Central Processing Unit) .

processor file The set of program and data files used by the controller to control output devices. Only one processor file may be stored in the controller at a time.

program file The area within a processor file that contains the ladder logic program.

program mode When the controller is not executing the processor file and all outputs are de-energized.

program scan

A part of the controller's operating cycle. During the scan the ladder program is executed and the output data file is updated based on the program and the input data file.

programming device protocol

Executable programming package used to develop ladder diagrams.

The packaging of information that is transmitted across a network.

read To acquire data from a storage place. For example, the processor READs information from the input data file to solve the ladder program.

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

watchdog timer

A timer that monitors a cyclical process and is cleared at the conclusion of each cycle. If the watchdog runs past its programmed time period, it causes a fault.

workspace The main storage available for programs and data and allocated for working storage.

write To copy data to a storage device. For example, the processor WRITEs the information from the output data file to the output modules.

| Numerics                                                              | before calling for assistance  155                       |
|-----------------------------------------------------------------------|----------------------------------------------------------|
| 1747-BA battery  25                                                   | bit  283                                                 |
| 1762 expansion I/O dimensions  29                                     | bit file monitoring  83                                  |
| 1762-24AWA wiring diagram  40                                         | block diagrams  283                                      |
| 1762-IA8 wiring diagram  45                                           | Boolean operators  283                                   |
| 1762-IF2OF2                                                           | BOOTP                                                    |
| input type selection  52                                              | using the Rockwell Utility  273                          |
| output type selection  52                                             | branch  283                                              |
| terminal block layout  52                                             | buttons  79                                              |
| wiring  52                                                            |                                                          |
| input type selection  53                                              | C                                                        |
| 1762-IF4                                                              |                                                          |
| terminal block layout  54 1762-IQ16 wiring diagram  46                | cable pinout                                             |
| 1762-IQ32T wiring diagram  47                                         | MicroLogix controller channel 0 to modem cable  62 ,  69 |
| 1762-IQ8 wiring diagram  45                                           | cables                                                   |
| 1762-IQ8OW6 wiring diagram  51                                        | planning routes for DH-485 connections  174              |
| 1762-OA8 wiring diagram  47                                           | selection guide for the AIC+  70                         |
| 1762-OB16 wiring diagram  48                                          | calling for assistance  155                              |
| 1762-OB32T wiring diagram  49                                         | changing communication configuration  58                 |
| 1762-OB8 wiring diagram  48                                           | changing mode switch position  94                        |
| 1762-OV32T wiring diagram  49                                         | collision avoidance  241                                 |
| 1762-OW16 wiring diagram  50                                          | common mode rejection ratio                              |
| 1762-OW8 wiring diagram  50                                           | specification  141                                       |
| 1762-OX6I wiring diagram  51                                          | communication                                            |
| 5/05 processors                                                       | DeviceNet  73                                            |
| Ethernet communications                                               | Ethernet  73 communication connections                   |
| 267                                                                   | 57 communication options  17                             |
| A                                                                     | communication protocols ASCII  178                       |
| address  283                                                          |                                                          |
|                                                                       | DF1 Full-Duplex  169 DF1 Half-Duplex  170                |
| Advanced Interface Converter. See AIC+ advanced LCD configuration  96 | DH-485  172                                              |
| AIC+                                                                  | DNP3  178 Ethernet                                       |
| 72                                                                    |                                                          |
| applying power to                                                     | 267 Modbus  178                                          |
| attaching to the network  72 connecting  69                           | supported  57                                            |
| definition  283 72                                                    | communication scan  283                                  |
| installing                                                            | communications toggle push button 58                     |
| recommended user supplied components  71 safety consideration  72     | using                                                    |
| selecting cable  70                                                   | component descriptions  14 1762 expansion I/O  15        |
| analog cable grounding  44                                            | communication cables  15                                 |
| analog channel wiring guidelines                                      | memory module  14                                        |
| 43 analog expansion I/O  152                                          | real-time clock  14 154                                  |
|                                                                       | configuration errors                                     |
| module operation vs. channel operation  153                           | configuring 98                                           |
| diagnostics  152 152 power-up diagnostics                             |                                                          |
| system wiring guidelines  51                                          | Ethernet network  IP address  99                         |
| troubleshooting  152                                                  | configuring the Ethernet channel  271                    |
| analog inputs                                                         | connecting expansion I/O  30                             |
| analog channel wiring guidelines  283                                 | connecting the system                                    |
| 43 application                                                        | AIC+  69 72                                              |
|                                                                       | ,  DeviceNet network  73                                 |
| B                                                                     | DF1 Full-Duplex protocol  60 DH-485 network  65          |
|                                                                       | DF1 isolated point-to-point connection  60               |
| battery  119                                                          | k  63                                                    |
| baud rate                                                             | connecting to DF1 Half-Duplex network                    |
| 283                                                                   |                                                          |

## connecting to networks via RS-232/RS-485

interface 169 connections to the Ethernet network k 268 control profile 283 ControlFLASH error messages 166 firmware upgrade 160 missing or corrupt OS state 168 using 157 controller 283 grounding 36 I/O wiring 42 installation 19 minimizing electrical noise 42 mounting 27 mounting dimensions 26 mounting on DIN rail 27 mounting on panel 28 preventing excessive heat 22 status indicator error conditions 151 status indicator normal operation 151 status indicators 149 controller modes 93 controller overhead 283 controller spacing 27 counter r 283 cursor display 80 D data table 283 default communication configuration 57 DeviceNet Communications 73 DeviceNet network connecting 73 DF1 Full-Duplex protocol connecting 60 description 169 example system configuration 169 using a modem 61 , 171 DF1 Half-Duplex protocol description 170 DH-485 communication protocol configuration parameters 65 , 173 DH-485 network configuration parameters 174 connecting 65 devices that use the network 173 example system configuration 176 installation 67 planning considerations 173 DIN rail 283 disable Ethernet channel 276 EtherNet/IP Incoming Connections 198 serial channels 178 disconnecting main power r 20

Distributed Network Protocol (DNP3) 178

## DNP3

analog input object 217 analog output object 220 BCD object 221 binary input object 209 binary output object 210 counter object 213 device attribute object 232 diagnostics 247 double bit binary input object 212 frozen counter object 215 objects 203 slave application layer 199 slave application layer configuration parameters 189 double integer file monitoring 89 download 283 download a user program via DNP3 network DTE (Data Terminal Equipment) 283 duplicate IP address detection 270 E Electronics Industries Association (EIA) 169 EMI 283 encoder 283 error recovery model 151 errors configuration 154 critical 153 extended error information field 153 hardware 154 module error field 153 non-critical 153 Ethernet messaging 267 processor performance 267 using the SLC 5/05 processors 267 Ethernet channel disable 276 Ethernet communication 267 Ethernet connections 270 Ethernet network configuration 98 Ethernet protocol setup 103 EtherNet/IP Incoming Connections disable 198 event generation control 238 executing mode 283 expansion I/O 1762-IF2OF2 input type selection 52 1762-IF2OF2 output type selection 52 expansion I/O mounting 29 , 30 mounting on DIN rail 29

k 2 242

expansion I/O specifications 134

| expansion I/O wiring  45                                  | isolated link coupler                                                                   |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------|
| 1762-IA8 wiring diagram  45                               | installing  67                                                                          |
| 1762-IF2OF2 wiring  52                                    | isolation transformers                                                                  |
| 1762-IF4 terminal block layout                            |                                                                                         |
| 54 1762-IQ16 wiring diagram  46                           | power considerations  21                                                                |
| 1762-IQ32T wiring diagram  47                             |                                                                                         |
| 1762-IQ8 wiring diagram  45                               | J                                                                                       |
| 1762-IQ8OW6 wiring diagram  51                            |                                                                                         |
| 1762-OA8 wiring diagram  47                               | jump  284                                                                               |
| 1762-OB16 wiring diagram  48                              |                                                                                         |
| 1762-OB32T wiring diagram  49 1762-OB8 wiring diagram  48 | L                                                                                       |
| 1762-OV32T wiring diagram  49                             | ladder logic  284                                                                       |
| 1762-OW16 wiring diagram  50 50                           | LCD                                                                                     |
| 1762-OW8 wiring diagram  51                               | 96                                                                                      |
| 1762-OX6I wiring diagram                                  | configuring advanced settings                                                           |
| analog wiring guidelines  51                              | I/O status indicators  80 ,  150 108                                                    |
| 153                                                       | loading communication EEPROM  main menu  78                                             |
| extended error information field                          | menu structure tree  76 saving communication EEPROM  108                                |
| F                                                         | setup  110 status indicators  150 95                                                    |
| false  284                                                |                                                                                         |
| FIFO (First-In-First-Out)  284                            | user defined screen  107                                                                |
| file  284                                                 | viewing fault code                                                                      |
| file authentication rules  244                            | viewing system information  107 least significant bit (LSB)  284                        |
| Full-Duplex  60                                           | LED (Light Emitting Diode)  284                                                         |
| full-duplex  284                                          | LIFO (Last-In-First-Out)  284                                                           |
| G                                                         | link layer configuration parameters  183 lithium battery (1747-BA)                      |
| general considerations  19                                | disposing  146                                                                          |
| generating DNP3 events  234                               | handling  145 installing                                                                |
| grounding the controller  r  36                           | 145 storing  146                                                                        |
|                                                           | transporting                                                                            |
|                                                           | 146 loading communication EEPROM  108                                                   |
|                                                           | logic  284                                                                              |
| H                                                         |                                                                                         |
| Half-Duplex  63 half-duplex                               | low byte  284                                                                           |
| 284 hard disk  284                                        | M                                                                                       |
| hardware errors  154                                      | 22                                                                                      |
| hardware features  13                                     | master control relay                                                                    |
| heat dissipation                                          | emergency-stop switches  23 using ANSI/CSA symbols schematic  24                        |
| calculating  282 22                                       | using IEC symbols schematic  23                                                         |
| heat protection  284                                      | Master Control Relay (MCR)  284 master control relay circuit                            |
| high byte                                                 |                                                                                         |
|                                                           | periodic tests  21                                                                      |
| I I/O (Inputs and Outputs)                                | memory module  14 data file protection  information file  121                           |
| 284                                                       | 120 operation  120                                                                      |
| I/O status indicators  80                                 |                                                                                         |
| implementation table  259                                 | program and data download  121 121                                                      |
| initialize user program  247 input device  284            | program and data upload  program compare  120                                           |
| input states on power down                                | 121                                                                                     |
|                                                           | program/data/recipe backup  120 removal/installation under power  write protection  121 |
| 21 inrush current  284                                    | menu structure  76                                                                      |
|                                                           | menu structure tree  76                                                                 |
| installing                                                |                                                                                         |
| battery wire connector  25                                |                                                                                         |
| ControlFLASH software  157                                | minimizing electrical noise                                                             |
| memory module  24                                         | 42 minimizing electrical noise on analog channels                                       |
| your controller  19                                       | 44                                                                                      |
| 284                                                       | mnemonic  284                                                                           |
| instruction  instruction set  284                         |                                                                                         |
|                                                           | Modbus communication protocol  178                                                      |

126

mode switch 93 modem cable constructing your own 62 modems using with MicroLogix controllers 171 modes 284 module error field 153 monitoring user defined target files 82 motor starters (bulletin 509) surge suppressors 36 N negative logic 285 network 285 nominal input current 285 normally closed 285 normally open 285 null modem cable 62 O object quality flags 230 oerformance considerations 267 offline 285 offset 285 off-state leakage current 285 one-shot 285 online 285 Online Editing Terms 123 online editing 123 edit functions in program online editing edit functions in runtime online editing 126 types 125 operating buttons 79 operating voltage 285 output device 285 P performance Ethernet processor 267 planning considerations for a network k 173 power considerations input states on power down 21 isolation transformers 21 loss of power source 21 other line conditions 22 overview 21 power supply inrush 21 power distribution 20 power source loss of 21 power supply inrush power considerations 21 preparing for upgrade 157 preventing excessive heat 22 processor 285 processor file 285 program file 285

21

```
program mode 285 program scan 285 programming 16 protocol 285 R read 286 real-time clock 14 battery operation 119 operation 119 removal/installation under power 119 writing data 119 relay 286 relay logic 286 remote packet support 175 replacement battery 145 disposing 146 handling 145 installing 145 storing 146 transporting 146 replacement kits 145 replacement parts 145 reporting event by polled response 239 reporting event by unsolicited response 239 reserved bit 286 restore 286 retentive data 286 RS-232 286 RS-232 communication interface 169 RS-485 communication interface 169 rules for downloading a user program 245 rules for file authentication 244 rules for initializing a user program 246 rules for uploading a user program 246 rules for uploading communication status files 246 run mode 286 rung 286 S safety circuits 20 safety considerations 19 disconnecting main power 20 hazardous location 19 master control relay circuit periodic tests 21 periodic tests of master control relay circuit 2 power distribution 20 safety circuits 20 save 286 saving communication EEPROM 108 scan time 286 serial channels disable 178 sinking 286 sinking and sourcing wiring diagrams 40 sinking wiring diagram 1762-24BWA 40 sourcing 286
```

## sourcing wiring diagram

```
1762-24BWA 41 , 42 1766-L32BWA 41 specifications 129 starting and stopping user programs (mode change) via DNP3 network k 246 status 286 status indicators 149 supported communication protocols 57 surge suppressors for motor starters 36 recommended 35 using 34 system configuration DF1 Full-Duplex examples 169 DH-485 connection examples 176 system loading example calculations 279 limitations 279 worksheet 280 system loading and heat dissipation 279 T target user defined file number 82 terminal 286 terminal block layouts 1762-IF2OF2 52 1762-IF4 54 controllers 37 throughput 286 time synchronization 241 trim pot information function file 105 trim pot operation 105 trim pots 105 changing values 105 configuring in LCD function file 106 error conditions 106 location 105 using 105 troubleshooting 149 true 286 TUF 82 U unsupported connections 16 upload 286 user defined LCD screen 95 using communications toggle functionality 58 using communications toggle push button 58 using emergency-stop switches 23 using memory modules 119 using real-time clock k 119 using the battery 25 using trim pots 105 V viewing fault code 107 viewing system information 107
```

## W

```
wiring analog channels 43 wiring diagram 1762-IA8 45 1762-IF2OF2 differential sensor r 53 1762-IF2OF2 single-ended sensor 53 1762-IQ16 46 1762-IQ32T 47 1762-IQ8 45 1762-IQ8OW6 51 1762-OA8 47 1762-OB16 48 1762-OB32T 49 1762-OB8 48 1762-OV32T 49 1762-OW16 50 1762-OW8 50 1762-OX6I 51 1766-L32AWA input 40 1766-L32AWA output 42 1766-L32BWA output 42 1766-L32BWA sinking 41 1766-L32BWA sourcing 41 1766-L32BXB output 42 1766-L32BXB sinking 41 1766-L32BXB sourcing 42 terminal block layouts 37 , 52 , 54 wiring diagrams 37 wiring recommendation 33 wiring with spade lugs 34 wiring without spade lugs 33 wiring your controller 33 working voltage 133 workspace 286 write 286
```

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

Allen-Bradley, ControlFLASH, Data-Set, Data Highway Plus, DH+, DTAM Micro, DTAM Plus, expanding human possibility, FactoryTalk, INTERCHANGE, MicroLogix, PanelView, PLC-5, Rockwell Automation, RSLinx, RSLogix, RSLogix 500, RSLogix Micro, SLC, SLC 5/03, SLC 500, and TechConnect are trademarks of Rockwell Automation, Inc .

CIP, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility?

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:(1)414.382.2000 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 ASIAPACIFIC:RockwellAutomationSEAPteLtd,2CorporationRoad,#04-05,MainLobby,CorporationPlace,Singapore618494,Tel:(65)65106608 UNITEDKINGD0M:RockwellAutomationLtd.,Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800