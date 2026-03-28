<!-- image -->

## MicroLogix 1200 Programmable Controllers

Bulletin 1762 Controllers and Expansion I/O Modules

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

| Preface                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------|
| Purpose of this Manual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7     |
| Download Firmware, AOP, EDS, and Other Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7                        |
| Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7      |
| Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7    |
| Chapter 1                                                                                                                               |
| Hardware Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9   |
| Component Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10         |
| MicroLogix 1200 Memory Module and/or Real-time Clock . . . . . . . . . . . . . . . . . . . . 10                                         |
| 1762 Expansion I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10                  |
| Communication Cables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |
| Programming. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 |
| Communication Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |
| Chapter 2                                                                                                                               |
| Installation Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13        |
| Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13      |
| Hazardous Location Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13                         |
| Disconnect Main Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14                |
| Safety Circuits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14       |
| Power Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14           |
| Periodic Tests of Master Control Relay Circuit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14                             |
| Power Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15       |
| Isolation Transformers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15              |
| Power Supply Inrush . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15            |
| Loss of Power Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15              |
| Input States on Power Down . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                   |
| Other Types of Line Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                   |
| Help Prevent Excessive Heat. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15           |
| Master Control Relay. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16    |
| Emergency Stop Switches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16                  |
| Install a Memory Module or Real-time Clock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                     |
| Controller Mounting Dimensions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20              |
| Controller and                                                                                                                          |
| Expansion I/O Spacing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20      |
| Mount the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20    |
| DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21          |
| Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22         |
| 1762 Expansion I/O Module Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23                   |
| Mount 1762 Expansion I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23         |
| DIN Rail Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23          |
| Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24         |
| Connect Expansion I/O Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24              |

| Chapter 3                                                                                                                                  | Chapter 3   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Wiring Requirements . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   27      |             |
| Wiring Recommendation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                     |             |
| Wire without Spade Lugs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28                   |             |
| Wire with Spade Lugs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28                |             |
| Use Surge Suppressors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29           |             |
| Recommended Surge Suppressors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30                              |             |
| Ground the Controller. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30        |             |
| Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31     |             |
| Terminal Block Layouts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31                  |             |
| Terminal Groupings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33                |             |
| Sinking and Sourcing Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34                      |             |
| 1762-L24AWA, 1762-L24BWA, 1762-L24BXB, 1762-L24AWAR, 1762-L24BWAR and 1762-                                                                |             |
| L24BXBR Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                     |             |
| 1762-L40AWA, 1762-L40BWA, 1762-L40BXB, 1762-L40AWAR, 1762-L40BWAR and 1762-                                                                |             |
| L40BXBR Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37                     |             |
| Controller I/O Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40      |             |
| Minimize Electrical Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                 |             |
| Expansion I/O Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40        |             |
| Discrete Wiring Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                    |             |
| Analog Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47          |             |
| Chapter 4                                                                                                                                  |             |
| Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53 |             |
| Supported Communication Protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                       |             |
| Default Communication Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                       |             |
| Use the Communications Toggle Push Button . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54                             |             |
| Connect to the RS-232 Port . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54            |             |
| Make a DF1 Point-to-Point Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                            |             |
| Use a Modem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55           |             |
| Isolated Modem Connection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                      |             |
| Connect to a DH-485 Network. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                |             |
| Recommended Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                   |             |
| DH-485 Communication Cable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                         |             |
| Connect the Communication Cable to the DH-485 Connector. . . . . . . . . . . . . . . . . 60                                                |             |
| Ground and Terminate the DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61                                   |             |
| Connect the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61      |             |
| Cable Selection Guide. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62                |             |
| Recommended User-supplied Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                                      |             |
| Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                 |             |
| Install and Attach the AIC+. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                  |             |
| Power the AIC+ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65            |             |
| Chapter 5                                                                                                                                  |             |
| Trimpot Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67       |             |
| Trimpot Information Function File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67                         |             |
| Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67            |             |

| Chapter 6                                                                                                                          | Chapter 6   |
|------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Real-time Clock Operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69    |             |
| Removal/Insertion Under Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69                 |             |
| Write Data to the Real-time Clock. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69                |             |
| RTC Battery Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70         |             |
| Memory Module Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70     |             |
| User Program and Data Back-up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70                   |             |
| Program Compare. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70        |             |
| Data File Download Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71               |             |
| Memory Module Write Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                  |             |
| Removal/Insertion Under Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                 |             |
| Appendix A                                                                                                                         |             |
| Controller Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73 |             |
| Expansion I/O Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77      |             |
| Discrete I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77       |             |
| Analog Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82    |             |
| Appendix B                                                                                                                         |             |
| MicroLogix 1200 RTB Replacement Kit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87             |             |
| Appendix C                                                                                                                         |             |
| Understand the Controller Status Indicators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                |             |
| Normal Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90      |             |
| Error Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90    |             |
| Controller Error Recovery Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91       |             |
| Analog Expansion I/O Diagnostics and Troubleshooting . . . . . . . . . . . . . . . . . . . . . . . . . 92                          |             |
| Module Operation and Channel Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92                        |             |
| Power-up Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92          |             |
| Critical and Non-critical Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92            |             |
| Module Error Definition Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92             |             |
| Error Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93 |             |
| Call Rockwell Automation for Assistance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94              |             |
| Appendix D                                                                                                                         |             |
| Prepare for Firmware Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95       |             |
| Install ControlFLASH Software. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95              |             |
| Prepare the Controller for Firmware Update. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                         |             |
| Sequence of Operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96  |             |
| Missing or Corrupt OS LED Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96         |             |
| Appendix E                                                                                                                         |             |
| RS-232 Communication Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97           |             |
| DF1 Full-duplex Protocol. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97 |             |
| DF1 Half-duplex Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98  |             |
| Use Modems with MicroLogix Programmable Controllers . . . . . . . . . . . . . . . . . . . . 99                                     |             |
| DH-485 Communication Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99           |             |

| DH-485 Configuration Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Devices that use the DH-485 Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100                                    |
| Important DH-485 Network Planning Considerations. . . . . . . . . . . . . . . . . . . . . . . 101                                                |
| Example DH-485 Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                               |
| Modbus Communication Protocol. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104                           |
| ASCII . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104  |
| Appendix F                                                                                                                                       |
| System Loading Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                      |
| System Loading Example Calculations (24-point Controller). . . . . . . . . . . . . . . . . 105                                                   |
| System Loading Example Calculations (40-point Controller) . . . . . . . . . . . . . . . . 106                                                    |
| System Loading Worksheet for 24-point Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                      |
| Current Loading. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                   |
| System Loading Worksheet for 40-point Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                                      |
| Current Loading. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                   |
| Calculating Heat Dissipation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                   |
| Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113           |
| Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   . . 117 |

## About This Publication

## Purpose of this Manual

## Download Firmware, AOP, EDS, and Other Files

## Summary of Changes

## Additional Resources

## Additional Resources

|                                                                                                                       | Resource Description                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 | Information on the MicroLogix 1200 and MicroLogix 1500 controllers instruction set.                           |
| AIC+ Advanced Interface Converter User Manual, publication 1761-UM004                                                 | A description on how to install and connect an AIC+. This manual also contains information on network wiring. |
| DeviceNet Interface User Manual, publication 1761-UM005                                                               | Information on how to install, configure, and commission a DeviceNet™ Interface (DNI).                        |
| DF1 Protocol and Command Set Reference Manual, publication 1770-6.5.16                                                | Information on DF1 open protocol.                                                                             |
| Modbus Protocol Specifications, available from www.modbus.org                                                         | Information about the Modbus protocol.                                                                        |
| EtherNet/IP Network Devices User Manual, publication ENET-UM006                                                       | Describes how to configure and use EtherNet/IP™ devices to communicate on the EtherNet/ IP network.           |
| Ethernet Reference Manual, publication ENET-RM002                                                                     | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                    |

Use this manual if you are responsible for designing, installing, programming, or troubleshooting control systems that use MicroLogix™ 1200 controllers.

You should have a basic understanding of electrical circuitry and familiarity with relay logic. If you do not, obtain the proper training before using this product.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This manual is a reference guide for MicroLogix 1200 controllers and expansion I/O. It describes the procedures that you use to install, wire, and troubleshoot your controller. This manual:

- Explains how to install and wire your controllers
- Gives you an overview of the MicroLogix 1200 controller system

See MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001, for the MicroLogix 1200 and MicroLogix 1500 instruction set and for application examples to show the instruction set in use. See your RSLogix 500® programming software user documentation for more information on programming your MicroLogix 1200 controller.

Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes from the Product Compatibility and Download Center at rok.auto/pcdc .

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

| Topic  Page                                                                              |
|------------------------------------------------------------------------------------------|
| Updated template throughout                                                              |
| Added inclusive language acknowledgment 7                                                |
| Updated Input Specifications – 1762-IA8, 1762-IQ8, 1762-IQ16, 1762-IQ32T, 1762-IQ8OW6 77 |
| Updated Output Specifications – 1762-OW8, 1762-OW16, 1762-OX6I, 1762-IQ8OW6 79           |
| Updated Environmental Specifications 77, 81, 86                                          |
| Updated Certifications 82, 86                                                            |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

## Additional Resources (Continued)

|                                                                                                                    | Resource Description                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System Security Design Guidelines Reference Manual, publication SECURE-RM001                                       | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                                                                   |
| UL Standards Listing for Industrial Control Products, publication CMPNTS-SR002                                     | Assists original equipment manufacturers (OEMs) with construction of panels, to help ensure that they conform to the requirements of Underwriters Laboratories.                                                                                                                 |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002 | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1   | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                        | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications                                                            | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

## Hardware Features

## Hardware Overview

The MicroLogix 1200 programmable controller contains a power supply, input and output circuits, and a processor. The controller is available in 24 I/O points and 40 I/O points configurations.

Figure 1 - Controller Hardware Features

<!-- image -->

## Controller Description

|                                                                             | Description Description                                                            |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 1  Terminal blocks (Removable terminal blocks on 40-point controllers only) | 7 Terminal doors and labels                                                        |
| 2 Bus connector interface to expansion I/O 8 Trimpots                       |                                                                                    |
|                                                                             | 3 Input LEDs 9 Communications Toggle push button                                   |
| 4 Output LEDs 10                                                            | Memory module port cover (1)  or memory module and/or real-time clock (2)          |
| 5 Communication port/Channel 0 11 DIN rail latches                          |                                                                                    |
|                                                                             | 6 Status LEDs 12 Programmer/HMI port (Equipped with 1762-LxxxxxR controllers only) |

## Controller Input Power and Embedded I/O

| Catalog Number                                            |                         |                                               |
|-----------------------------------------------------------|-------------------------|-----------------------------------------------|
| Catalog Number                                            |                         | Input Power Inputs Outputs                    |
| 1762-L24AWA, 1762-L24AWAR 120/240V AC 14 120V AC 10 relay |                         |                                               |
| 1762-L24BWA, 1762-L24BWAR 120/240V AC                     | 10 24V DC 4 fast 24V DC | 10 relay                                      |
| 1762-L24BXB, 1762-L24BXBR 24V DC                          | 10 24V DC 4 fast 24V DC | 5 relay, 4 24V DC FET 1 high-speed 24V DC FET |

<!-- image -->

## Component Descriptions

## Controller Input Power and Embedded I/O (Continued)

| Catalog Number                                            |                         |                                               |
|-----------------------------------------------------------|-------------------------|-----------------------------------------------|
| Catalog Number                                            |                         | Input Power Inputs Outputs                    |
| 1762-L40AWA, 1762-L40AWAR 120/240V AC 24 120V AC 16 relay |                         |                                               |
| 1762-L40BWA, 1762-L40BWAR 120/240V AC                     | 20 24V DC 4 fast 24V DC | 16 relay                                      |
| 1762-L40BXB, 1762-L40BXBR 24V DC                          | 20 24V DC 4 fast 24V DC | 8 relay, 7 24V DC FET 1 high-speed 24V DC FET |

## MicroLogix 1200 Memory Module and/or Real-time Clock

The controller is shipped with a memory module port cover in place. You can order a memory module, real-time clock, or memory module and real-time clock as an accessory.

<!-- image -->

## Memory Module and/or Real-time Clock

| Catalog Number Description                    |
|-----------------------------------------------|
| 1762-MM1 Memory module only                   |
| 1762-RTC Real-time clock only                 |
| 1762-MM1RTC Memory module and real-time clock |

## 1762 Expansion I/O Modules

1762 expansion I/O modules can be connected to the MicroLogix 1200 controller, as shown in Figure 2 .

<!-- image -->

A maximum of six I/O modules, in certain combinations, may be connected to a controller. See System Loading and Heat Dissipation on page 105 to determine valid combinations.

Figure 2 - 1762 Expansion I/O Modules

1762 expansion I/O module 1762 expansion I/O module connected to a MicroLogix 1200 controller

<!-- image -->

## Communication Cables

## Programming

## Communication Options

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

Use only the following communication cables with the MicroLogix 1200 controllers:

- 1761-CBL-PM02, series C or later
- 1761-CBL-HM02, series C or later
- 1761-CBL-AM00, series C or later
- 1761-CBL-AP00, series C or later
- 1761-CBL-PH02, series A or later
- 1761-CBL-AH02, series A or later
- 2707-NC8, series A or later
- 2702-NC9, series B or later
- 2707-NC10, series B or later
- 2707-NC11, series B or later

Program the MicroLogix 1200 controller using RSLogix 500 software, version 4.00.00 or later. To use the new features of the series B MicroLogix 1200 controllers, including the full ASCII instruction set, you must use RSLogix 500 software, version 4.50.00 or later. Communication cables for programming are available separately from the controller and software.

The MicroLogix 1200 can be connected to a personal computer. It can also be connected to a DH-485 network, or a Modbus network as an RTU master or RTU slave with an Advanced Interface Converter (1761-NET-AIC). The controller can also be connected to DF1 Half-duplex networks as an RTU master or RTU slave. Series B controllers may also be connected to serial devices using ASCII.

See Communication Connections on page 53 for more information on connecting to the available communication options.

The 1762-LxxxxxR controllers provide an additional communication port called the Programmer/HMI Port. This port supports DF1 Full-duplex protocol only. The controller cannot

initiate messages through this port. It can only respond to messages sent to it. All communication parameters are fixed and cannot be changed by a user.

See Default Communication Configuration on page 53 for the configuration settings.

## Installation Considerations

## Safety Considerations

## Install Your Controller

Most applications require installation in an industrial enclosure (Pollution Degree 2(a)) to reduce the effects of electrical interference (Over Voltage Category II (b) ) and environmental exposure. Locate your controller as far as possible from power lines, load lines, and other sources of electrical noise such as hard-contact switches, relays, and AC motor drives. For more information on proper grounding guidelines, see the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

<!-- image -->

<!-- image -->

ATTENTION: Vertical mounting of the controller is not recommended due to heat build-up considerations.

ATTENTION: Be careful of metal chips when drilling mounting holes for your controller or other equipment within the enclosure or panel. Drilled fragments that fall into the controller or I/O modules could cause damage. Do not drill holes above a mounted controller if the protective debris shields are removed or the processor is installed.

Safety considerations are an important element of proper system installation. Actively thinking about the safety of yourself and others, as well as the condition of your equipment, is of primary importance. We recommend reviewing the following safety considerations.

## Hazardous Location Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D or non-hazardous locations only. The following WARNING statement applies to use in hazardous locations.

<!-- image -->

## WARNING: EXPLOSION HAZARD

- Substitution of components may impair suitability for Class I Division 2.
- Do not replace components or disconnect equipment unless power has been switched off.
- Do not connect or disconnect components unless power has been switched off.
- This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.
- All wiring must comply with N.E.C. article 501-4(b).
- The interior of the enclosure must be accessible only by the use of a tool.
- For applicable equipment (for example, relay modules), exposure to some chemicals may degrade the sealing properties of the materials used in these devices:
- – Relays, epoxy
- It is recommended that you periodically inspect these devices for any degradation of properties and replace the module if degradation is found.

(a) Pollution Degree 2 is an environment where normally only non-conductive pollution occurs except that occasionally temporary conductivity caused by condensation shall be expected.

(b) Overvoltage Category II is the load level section of the electrical distribution system. At this level, transient voltages are controlled and do not exceed the impulse voltage capability of the products insulation.

<!-- image -->

Use only the communication cables that are listed in Table 1 in Class I Division 2 hazardous locations.

Table 1 - Communication Cables for Class I Division 2 Hazardous Locations

| Catalog Number Catalog Number                                 |
|---------------------------------------------------------------|
| 1761-CBL-PM02, series C or later 2707-NC8, series A or later  |
| 1761-CBL-HM02, series C or later 2707-NC9, series B or later  |
| 1761-CBL-AM00, series C or later 2707-NC10, series B or later |
| 1761-CBL-AP00, series C or later 2707-NC11, series B or later |
| 1761-CBL-PH02, series A or later —                            |
| 1761-CBL-AH02, series A or later —                            |

## Disconnect Main Power

<!-- image -->

## WARNING: EXPLOSION HAZARD

Do not replace components or disconnect equipment unless power has been switched off.

The main power disconnect switch should be located where operators and maintenance personnel have quick and easy access to it. In addition to disconnecting electrical power, all other sources of power (pneumatic and hydraulic) should be de-energized before working on a machine or process that is controlled by a controller.

## Safety Circuits

<!-- image -->

## WARNING: EXPLOSION HAZARD

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

During power-up, the MicroLogix 1200 power supply allows a brief inrush current to charge internal capacitors. Many power lines and control transformers can supply inrush current for a brief time. If the power source cannot supply this inrush current, the source voltage could sag momentarily.

The only effect of limited inrush current and voltage sag on the MicroLogix 1200 controller is that the power supply capacitors charge more slowly. However, consider the effect of a voltage sag on other equipment. For example, a deep voltage sag could reset a computer that is connected to the same power source. The following considerations determine whether the power source is required to supply high inrush current:

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

A hard-wired master control relay (MCR) provides a reliable means for emergency machine shutdown. Since the master control relay allows the placement of several emergency stop switches in different locations, its installation is important from a safety standpoint. Overtravel limit switches or mushroom-head push buttons are wired in series so that when any of them opens, the master control relay is de-energized. This removes power to input and output device circuits. See Figure 3 and Figure 4 .

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

Figure 3 and Figure 4 show the master control relay wired in a grounded system.

<!-- image -->

In most applications input circuits do not require MCR protection; however, if you must remove power from all field devices, you must include MCR contacts in series with input power wiring.

Figure 3 - Schematic (Using IEC Symbols)

<!-- image -->

Figure 4 - Schematic (Using ANSI/CSA Symbols)

<!-- image -->

## Install a Memory Module or Real-time Clock

To install a memory module, do as follows:

1. Remove the memory module port cover.
2. Align the connector on the memory module with the connector pins on the controller.
3. Firmly seat the memory module into the controller.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Controller Mounting Dimensions

Figure 5 - Controller Dimensions

<!-- image -->

1762-L24AWA, 1762-L24BWA, 1762-L24BXB 1762-L24AWAR, 1762-L24BWAR, 1762-L24BXBR

<!-- image -->

1762-L40AWA, 1762-L40BWA, 1762-L40BXB

1762-L40AWAR, 1762-L40BWAR, 1762-L40BXBR

| Dimension   | 1762-L24AWA 1762-L24AWAR   | 1762-L24BWA 1762-L24BWAR   | 1762-L24BXB 1762-L24BXBR            | 1762-L40AWA 1762-L40AWAR   | 1762-L40BWA 1762-L40BWAR   | 1762-L40BXB 1762-L40BXBR   |
|-------------|----------------------------|----------------------------|-------------------------------------|----------------------------|----------------------------|----------------------------|
| A           |                            |                            | 90 mm (3.5 in.) 90 mm (3.5 in.)     |                            |                            |                            |
| B           |                            |                            | 110 mm (4.33 in.) 160 mm (6.30 in.) |                            |                            |                            |
| C           |                            |                            | 87 mm (3.43 in.) 87 mm (3.43 in.)   |                            |                            |                            |

## Controller and Expansion I/O Spacing

## Mount the Controller

The controller mounts horizontally, with the expansion I/O extending to the right of the controller. Allow 50 mm (2 in.) of space on all sides of the controller system for adequate ventilation. Maintain spacing from enclosure walls, wireways, and adjacent equipment, as shown in Figure 6 .

Figure 6 - Controller and Expansion I/O Spacing

<!-- image -->

MicroLogix 1200 controllers are suitable for use in an industrial environment when installed in accordance with these instructions. Specifically, this equipment is intended for use in clean, dry environments (Pollution degree 2 (a) ) and to circuits not exceeding Over Voltage Category II(b) (IEC 60664-1)(c) .

(a) Pollution Degree 2 is an environment where, normally, only non-conductive pollution occurs except that occasionally a temporary conductivity caused by condensation shall be expected.

(b) Over Voltage Category II is the load level section of the electrical distribution system. At this level transient voltages are controlled and do not exceed the impulse voltage capability of the product's insulation.

(c) Pollution Degree 2 and Over Voltage Category II are International Electrotechnical Commission (IEC) designations.

<!-- image -->

ATTENTION: Do not remove the protective debris shield until after the controller and all other equipment in the panel near the controller are mounted and wiring is complete. Once wiring is complete, remove protective debris shield. Failure to remove shield before operating can cause overheating.

<!-- image -->

<!-- image -->

ATTENTION: Electrostatic discharge can damage semiconductor devices inside the controller. Do not touch the connector pins or other sensitive areas.

<!-- image -->

For environments with greater vibration and shock concerns, use the panel mounting method described on Panel Mounting on page 22, rather than DIN rail mounting.

## DIN Rail Mounting

The maximum extension of the latch is 14 mm (0.55 in.) in the open position. A flat-blade screwdriver is required for removal of the controller. The controller can be mounted to EN 50022 - 35 x 7.5 or EN 50022 - 35 x 15 DIN rails. DIN rail mounting dimensions are shown in Figure 7 .

Figure 7 - DIN Rail Mounting Dimensions

<!-- image -->

To install your controller on the DIN rail, do as follows:

1. Mount your DIN rail. Make sure that the placement of the controller on the DIN rail meets the recommended spacing requirements, see Controller and Expansion I/O Spacing on page 20 .
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

## Panel Mounting

Mount to panel using #8 or M4 screws. To install your controller using mounting screws:

1. Secure the template to the mounting surface. Make sure your controller is spaced properly. See Controller and Expansion I/O Spacing on page 20 .
2. Drill holes through the template.
3. Remove the mounting template.
4. Mount the controller.
5. Leave the protective debris shield in place until you are finished wiring the controller and any other devices.

<!-- image -->

<!-- image -->

## 1762 Expansion I/O Module Dimensions

## Mount 1762 Expansion I/O

<!-- image -->

Figure 8 - 1762 Expansion I/O Module Dimensions

| Dimension Expansion I/O Module   |
|----------------------------------|
| A 90 mm (3.5 in.)                |
| B 40 mm (1.57 in.)               |
| C 87 mm (3.43 in.)               |

<!-- image -->

ATTENTION: During panel or DIN rail mounting of all devices, be sure that all debris such as metal chips and wire stands, is kept from falling into the module. Debris that falls into the module could cause damage when the module is under power.

## DIN Rail Mounting

The module can be mounted using the following DIN rails:

- 35 x 7.5 mm (EN 50022 - 35 x 7.5)
- 35 x 15 mm (EN 50022 - 35 x 15)

Before mounting the module on a DIN rail, close the DIN rail latch. Press the DIN rail mounting area of the module against the DIN rail. The latch momentarily opens and locks into place.

Use DIN rail end anchors (Allen-Bradley part number 1492-EA35 or 1492-EAH35) for vibration or shock environments. Figure 9 shows the location of the end anchors.

Figure 9 - Location of End Achors

<!-- image -->

## Connect Expansion I/O Modules

<!-- image -->

1762 expansion I/O modules must be mounted horizontally as illustrated.

<!-- image -->

For environments with greater vibration and shock concerns, use the panel mounting method described below, instead of DIN rail mounting.

## Panel Mounting

Use the dimensional template shown in Figure 10 to mount the module. The preferred mounting method is to use two M4 or #8 panhead screws per module. Mounting screws are required on every module.

## Figure 10 - Dimensional Template

For more than 2 modules: (number of modules - 1) x 40 mm (1.58 in.)

A = 95.86mm (3.774 in.)

1762-L24AWA, 1762-L24BWA, 1762-L24BXB

1762-L24AWAR, 1762-L24BWAR, 1762-L24BXBR

B = 145.8 mm (5.739 in.)

1762-L40AWA, 1762-L40BWA, 1762-L40BXB 1762-L40AWAR, 1762-L40BWAR, 1762-L40BXBR

All dimensions are in mm (inches). Hole spacing tolerance: ±0.4 mm (0.016 in.).

<!-- image -->

The expansion I/O module is attached to the controller or another I/O module by means of a flat ribbon cable after mounting, as shown in Figure 11 .

Figure 11 - Attach Expansion I/O Modules

<!-- image -->

<!-- image -->

<!-- image -->

Use the pull loop on the connector to disconnect modules. Do not pull on the ribbon cable.

You can connect up to six expansion I/O modules to a controller depending upon the power supply loading.

<!-- image -->

<!-- image -->

ATTENTION: Remove power before removing or inserting an I/O module. When you remove or insert a module with power applied, an electric arc may occur. An electric arc can cause personal injury or property damage by:

- Sending an erroneous signal to your system's field devices, causing the controller to fault
- Causing an explosion in a hazardous environment

Electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts may create electrical resistance, reducing product reliability.

## WARNING: EXPLOSION HAZARD

In Class I Division 2 applications, the bus connector must be fully seated and the bus connector cover must be snapped in place.

In Class I Division 2 applications, all modules must be mounted in direct contact with each other as shown in Connect Expansion I/O Modules on page 24. If DIN rail mounting is used, an end stop must be installed ahead of the controller and after the last 1762 I/O module.

## Notes:

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

Do not run signal or communication wiring and power wiring in the same conduit. Wires with different signal characteristics should be routed by separate paths.

- Separate wiring by signal type. Bundle wiring with similar electrical characteristics together.
- Separate input wiring from output wiring.
- Label wiring to all devices in the system. Use tape, shrink-tubing, or other dependable means for labeling purposes. In addition to labeling, use colored insulation to identify wiring based on signal characteristics. For example, you may use blue for DC wiring and red for AC wiring.

Table 2 - Wire Requirements

| Wire Type                  | Wire Size (2 wire maximum per terminal screw)(1)   |
|----------------------------|----------------------------------------------------|
| Solid Cu-90 °C (194 °F)    | 0.34…2.5 mm2  (14…22 AWG)                                                    |
| Stranded Cu-90 °C (194 °F) | 1.5…2.5 mm2  (16…22 AWG)                                                    |

<!-- image -->

## Wire without Spade Lugs

When wiring without spade lugs, we recommend that you keep the finger-safe covers in place. Loosen the terminal screw and route the wires through the opening in the finger-safe cover. Tighten the terminal screw making sure the pressure plate secures the wire.

<!-- image -->

## Wire with Spade Lugs

The diameter of the terminal screw head is 5.5 mm (0.22 in.). The input and output terminals of the MicroLogix 1200 controller are designed for a 6.35 mm (0.25 in.) wide spade (standard for #6 screw for up to 14 AWG) or a 4 mm (metric #4) fork terminal.

When using spade lugs, use a small, flat-blade screwdriver to pry the finger-safe cover from the terminal blocks as shown below. Then loosen the terminal screw.

<!-- image -->

## Use Surge Suppressors

Because of the potentially high current surges that occur when switching inductive load devices, such as motor starters and solenoids, the use of some type of surge suppression to protect and extend the operating life of the controllers output contacts is required. Switching inductive loads without surge suppression can significantly reduce the life expectancy of relay contacts. By adding a suppression device directly across the coil of an inductive device, you prolong the life of the output or relay contacts. You also reduce the effects of voltage transients and electrical noise from radiating into adjacent systems.

Figure 12 shows an output with a suppression device. We recommend that you locate the suppression device as close as possible to the load device.

Figure 12 - Output with Suppression Device Example

<!-- image -->

If the outputs are DC, we recommend that you use an 1N4004 diode for surge suppression, as shown below. For inductive DC load devices, a diode is suitable. A 1N4004 diode is acceptable for most applications. A surge suppressor can also be used. See Table 3 for recommended suppressors. As shown in Figure 13, these surge suppression circuits connect directly across the load device.

Figure 13 - Relay or Solid-state DC Output with Suppression Device Example

<!-- image -->

Suitable surge suppression methods for inductive AC load devices include a varistor, an RC network, or an Allen-Bradley surge suppressor, shown in Figure 14. These components must be appropriately rated to suppress the switching transient characteristic of the particular inductive device. See Table 3 for recommended suppressors.

## Ground the Controller

Figure 14 - Surge Suppression for Inductive AC Load Devices

<!-- image -->

## Recommended Surge Suppressors

Use the Allen-Bradley surge suppressors shown in the following table for use with relays, contactors, and starters.

Table 3 - Recommended Surge Suppressors

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

In solid-state control systems, grounding and wire routing helps limit the effects of noise due to electromagnetic interference (EMI). Run the ground connection from the ground screw of the controller to the ground bus prior to connecting any devices. Use 2.5 mm 2 (14 AWG) wire. For AC-powered controllers, this connection must be made for safety purposes.

<!-- image -->

ATTENTION: All devices connected to the RS-232 communication port must be referenced to controller ground, or be floating (not referenced to a potential other than ground). Failure to follow this procedure may result in property damage or personal injury.

- For 1762-L24BWA, 1762-L40BWA, 1762-L24BWAR, and 1762-L40BWAR controllers:

The COM of the sensor supply is also connected to chassis ground internally. The 24V DC sensor power source should not be used to power output circuits. It should only be used to power input devices.

- For 1762-L24BXB, 1762-L40BXB, 1762-L24BXBR, and 1762-L40BXBR controllers: The VDC NEUT or common terminal of the power supply is also connected to chassis ground internally.

## Wiring Diagrams

This product is intended to be mounted to a well grounded mounting surface such as a metal panel. See the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional information. Additional grounding connections from the mounting tab or DIN rail, if used, are not required unless the mounting surface cannot be grounded.

<!-- image -->

Use all four mounting positions for panel mounting installation.

<!-- image -->

<!-- image -->

ATTENTION: Remove the protective debris strip before applying power to the controller. Failure to remove the strip may cause the controller to overheat.

The following illustrations show the wiring diagrams for the MicroLogix 1200 controllers. Controllers with DC inputs can be wired as either sinking or sourcing inputs. Sinking and sourcing does not apply to AC inputs. See the various diagrams described in Sinking and Sourcing Wiring Diagrams on page 34 .

The controller terminal block layouts are shown in Terminal Block Layouts. The shading on the labels indicates how the terminals are grouped. A detail of the groupings is shown in the tables in Terminal Groupings on page 33 .

<!-- image -->

This symbol denotes a protective earth ground terminal which provides a low impedance path between electrical circuits and earth for safety purposes and provides noise immunity improvement. This connection must be made for safety purposes on AC-powered controllers.

This symbol denotes a functional earth ground terminal which provides a low impedance path between electrical circuits and earth for non-safety purposes, such as noise immunity improvement.

## Terminal Block Layouts

Figure 15 - 1762-L24AWA and 1762-L24AWAR

<!-- image -->

Figure 16 - 1762-L24BWA and 1762-L24BWAR

<!-- image -->

<!-- image -->

ATTENTION: The 24V DC sensor supply of the 1762-L24BWA and 1762-L24BWAR should not be used to power output circuits. It should only be used to power input devices (for example sensors and switches). See Master Control Relay on page 16 for information on MCR wiring in output circuits.

Figure 17 - 1762-L24BXB and 1762-L24BXBR

<!-- image -->

Figure 18 - 1762-L40AWA and 1762-L40AWAR

<!-- image -->

Figure 19 - 1762-L40BWA and 1762-L40BWAR

<!-- image -->

<!-- image -->

ATTENTION: The 24V DC sensor supply of the 1762-L40BWA and 1762-L40BWAR should not be used to power output circuits. It should only be used to power input devices (for example sensors and switches). See Master Control Relay on page 16 for information on MCR wiring in output circuits.

Figure 20 - 1762-L40BXB and 1762-L40BXBR

<!-- image -->

## Terminal Groupings

Table 4 - Input Terminal Grouping

| Controller               | Inputs                                     | Inputs   | Inputs   |
|--------------------------|--------------------------------------------|----------|----------|
| Controller               | Input Group Common Terminal Input Terminal |          |          |
| 1762-L24AWA 1762-L24AWAR | Group 0 AC COM 0 I/0…I/3                   |          |          |
| 1762-L24AWA 1762-L24AWAR | Group 1 AC COM 1 I/4…I/13                  |          |          |
| 1762-L24BWA 1762-L24BWAR | Group 0 DC COM 0 I/0…I/3                   |          |          |
| 1762-L24BWA 1762-L24BWAR | Group 1 DC COM 1 I/4…I/13                  |          |          |
| 1762-L24BXB 1762-L24BXBR | Group 0 DC COM 0 I/0…I/3                   |          |          |
| 1762-L24BXB 1762-L24BXBR | Group 1 DC COM 1 I/4…I/13                  |          |          |
| 1762-L40AWA 1762-L40AWAR | Group 0 AC COM 0 I/0…I/3                   |          |          |
| 1762-L40AWA 1762-L40AWAR | Group 1 AC COM 1 I/4…I/7                   |          |          |
| 1762-L40AWA 1762-L40AWAR | Group 2 AC COM 2 I/8…I/23                  |          |          |
| 1762-L40BWA 1762-L40BWAR | Group 0 DC COM 0 I/0…I/3                   |          |          |
| 1762-L40BWA 1762-L40BWAR | Group 1 DC COM 1 I/4…I/7                   |          |          |
| 1762-L40BWA 1762-L40BWAR | Group 2 DC COM 2 I/8…I/23                  |          |          |
| 1762-L40BXB 1762-L40BXBR | Group 0 DC COM 0 I/0…I/3                   |          |          |
| 1762-L40BXB 1762-L40BXBR | Group 1 DC COM 1 I/4…I/7                   |          |          |
| 1762-L40BXB 1762-L40BXBR | Group 2 DC COM 2 I/8…I/23                  |          |          |

## Sinking and Sourcing Wiring Diagrams

Table 5 - Output Terminal Grouping

| Controller   | Outputs   | Outputs                       | Outputs                        | Outputs                                          |
|--------------|-----------|-------------------------------|--------------------------------|--------------------------------------------------|
| Controller   |           | Output Group Voltage Terminal | Output Terminal Description    |                                                  |
|              | Group 0   | VAC/VDC 0                     | O/0                            | Isolated Relay outputs                           |
|              |           | Group 1 VAC/VDC 1 O/1         |                                | Isolated Relay outputs                           |
|              | Group 2   | VAC/VDC 2                     | O/2…O/3                        | Isolated Relay outputs                           |
|              |           | Group 3 VAC/VDC 3 O4…O/5      |                                | Isolated Relay outputs                           |
|              | Group 4   | VAC/VDC 4                     | O/6…O/9                        | Isolated Relay outputs                           |
|              |           | Group 0 VAC/VDC 0 O/0         |                                | Isolated Relay outputs                           |
|              | Group 1   | VAC/VDC 1                     | O/1                            | Isolated Relay outputs                           |
|              |           | Group 2 VAC/VDC 2 O/2…O/3     |                                | Isolated Relay outputs                           |
|              | Group 3   | VAC/VDC 3                     | O/4…O/5                        | Isolated Relay outputs                           |
|              |           | Group 4 VAC/VDC 4 O/6…O/9     |                                | Isolated Relay outputs                           |
|              | Group 0   | VAC/VDC 0                     | O/0                            | Isolated Relay outputs                           |
|              |           | Group 1 VAC/VDC 1 O/1         |                                | Isolated Relay outputs                           |
|              | Group 2   | VDC 2, VDC COM 2              | O/2…O/6                        | Isolated FET outputs                             |
|              |           |                               |                                | Group 3 VAC/VDC 3 O/7…O/9 Isolated Relay outputs |
|              | Group 0   | VAC/VDC 0                     | O/0                            | Isolated Relay outputs                           |
|              |           | Group 1 VAC/VDC 1 O/1         |                                | Isolated Relay outputs                           |
|              | Group 2   | VAC/VDC 2                     | O/2…O/3                        | Isolated Relay outputs                           |
|              |           | Group 3 VAC/VDC 3 O/4…O/7     |                                | Isolated Relay outputs                           |
|              | Group 4   | VAC/VDC 4                     | O/8…O/11                       | Isolated Relay outputs                           |
|              |           | Group 5 VAC/VDC 5 O/12…O/15   |                                | Isolated Relay outputs                           |
|              | Group 0   | VAC/VDC 0                     | O/0                            | Isolated Relay outputs                           |
|              |           | Group 1 VAC/VDC 1 O/1         |                                | Isolated Relay outputs                           |
|              | Group 2   | VAC/VDC 2                     | Isolated Relay outputs O/2…O/3 | Isolated Relay outputs                           |
|              |           | Group 3 VAC/VDC 3 O/4…O/7     |                                | Isolated Relay outputs                           |
|              | Group 4   | VAC/VDC 4                     | O/8…O/11                       | Isolated Relay outputs                           |
|              |           | Group 5 VAC/VDC 5 O/12…O/15   |                                | Isolated Relay outputs                           |
|              | Group 0   | VAC/VDC 0                     | O/0                            | Isolated Relay outputs                           |
|              |           | Group 1 VAC/VDC 1 O/1         |                                | Isolated Relay outputs                           |
|              | Group 2   | VDC 2, VDC COM 2              | O/2…O/9                        | Isolated FET outputs                             |
|              |           | Group 3 VAC/VDC 3 O/10…O/11   |                                | Isolated Relay outputs                           |
|              | Group 4   | VAC/VDC 4                     | O/12…O/15                      | Isolated Relay outputs                           |

Any of the MicroLogix 1200 controller DC embedded input groups can be configured as sinking or sourcing depending on how the DC COM is wired on the group.

|                | Type Definition                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sinking Input  | The input energizes when high-level voltage is applied to the input terminal (active high). Connect the power supply VDC (-) to the input group’s COM terminal. |
| Sourcing Input | The input energizes when low-level voltage is applied to the input terminal (active low). Connect the power supply VDC (+) to the input group’s COM terminal.   |

<!-- image -->

ATTENTION: The 24V DC sensor power source must not be used to power output circuits. It should only be used to power input devices (for example sensors and switches). See Master Control Relay on page 16 for information on MCR wiring in output circuits.

## 1762-L24AWA, 1762-L24BWA, 1762-L24BXB, 1762-L24AWAR, 1762-L24BWAR and 1762-L24BXBR Wiring Diagrams

<!-- image -->

In Figure 21 to Figure 34, lower case alphabetic subscripts are appended to common-terminal connections to indicate that different power sources may be used for different isolated groups, if desired.

Figure 21 - 1762-L24AWA and 1762-L24AWAR Input Wiring Diagram (1)

<!-- image -->

- (1) "NC" terminals are not intended for use as connection points.

Figure 22 - 1762-L24BWA and 1762-L24BWAR Sinking Input Wiring Diagram

<!-- image -->

Figure 23 - 1762-L24BWA and 1762-L24BWAR Sourcing Input Wiring Diagram

<!-- image -->

Figure 24 - 1762-L24BXB and 1762-L24BXBR Sinking Input Wiring Diagram

<!-- image -->

Figure 25 - 1762-L24BXB and 1762-L24BXBR Sourcing Input Wiring Diagram

<!-- image -->

Figure 26 - 1762-L24AWA, 1762-L24BWA, 1762-L24AWAR, and 1762-L24BWAR Output Wiring Diagram

<!-- image -->

Figure 27 - 1762-L24BXB and 1762-L24BXBR Output Wiring Diagram

<!-- image -->

1762-L40AWA, 1762-L40BWA, 1762-L40BXB, 1762-L40AWAR, 1762-L40BWAR and 1762-L40BXBR Wiring Diagrams

Figure 28 - 1762-L40AWA and 1762-L40AWAR Input Wiring Diagram

<!-- image -->

Figure 29 - 1762-L40BWA and 1762-L40BWAR Sinking Input Wiring Diagram

<!-- image -->

Figure 30 - 1762-L40BWA and 1762-L40BWAR Sourcing Input Wiring Diagram

<!-- image -->

Figure 31 - 1762-L40BXB and 1762-L40BXBR Sinking Input Wiring Diagram

<!-- image -->

Figure 32 - 1762-L40BXB and 1762-L40BXBR Sourcing Input Wiring Diagram

<!-- image -->

Figure 33 - 1762-L40AWA, 1762-L40BWA, 1762-L40AWAR, and 1762-L40BWAR Output Wiring Diagram

<!-- image -->

Figure 34 - 1762-L40BXB and 1762-L40BXBR Output Wiring Diagram

<!-- image -->

## Controller I/O Wiring

## Expansion I/O Wiring

## Minimize Electrical Noise

Because of the variety of applications and environments where controllers are installed and operating, it is impossible to ensure that all environmental noise will be removed by input filters. To help reduce the effects of environmental noise, install the MicroLogix 1200 system in a properly rated (for example, NEMA) enclosure. Make sure that the MicroLogix 1200 system is properly grounded.

A system may malfunction due to a change in the operating environment after a period of time. We recommend periodically checking system operation, particularly when new machinery or other noise sources are installed near the Micrologix 1200 system.

Figure 35 to Figure 47 show the discrete and analog expansion I/O wiring diagrams.

## Discrete Wiring Diagrams

Figure 35 - 1762-IA8 Wiring Diagram

<!-- image -->

Figure 36 - 1762-IQ8 Wiring Diagram

<!-- image -->

Figure 37 - 1762-IQ16 Wiring Diagram

<!-- image -->

Figure 38 - 1762-IQ32T Wiring Diagram

<!-- image -->

Figure 39 - 1762-OA8 Wiring Diagram

<!-- image -->

Figure 40 - 1762-OB8 Wiring Diagram

<!-- image -->

Figure 41 - 1762-OB16 Wiring Diagram

<!-- image -->

Figure 42 - 1762-OB32T Wiring Diagram

<!-- image -->

<!-- image -->

Figure 43 - 1762-OV32T Wiring Diagram

<!-- image -->

<!-- image -->

Figure 44 - 1762-OW8 Wiring Diagram

<!-- image -->

Figure 45 - 1762-OW16 Wiring Diagram

<!-- image -->

Figure 46 - 1762-OX6I Wiring Diagram

<!-- image -->

Figure 47 - 1762-IQ8OW6 Wiring Diagram

<!-- image -->

## Analog Wiring

## System Wiring Guidelines

Consider the following when wiring your analog modules:

- The analog common (COM) is not connected to earth ground inside the module. All terminals are electrically isolated from the system.
- Channels are not isolated from each other.
- Use Belden 8761 or equivalent shielded wire.
- Under normal conditions, the drain wire (shield) should be connected to the metal mounting panel (earth ground). Keep the shield connection to earth ground as short as possible.
- To ensure optimum accuracy for voltage type inputs, limit overall cable impedance by keeping all analog cables as short as possible. Locate the I/O system as close to your voltage type sensors or actuators as possible.
- The module does not provide loop power for analog inputs. Use a power supply that matches the input transmitter specifications.

## 1762-IF2OF2 Input Type Selection

Select the input type, current or voltage, using the switches located on the module's circuit board and the input type/range selection bits in the Configuration Data File. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001. You can access the switches through the ventilation slots on the top of the module. Switch 1 controls channel 0; switch 2 controls channel 1. The factory default setting for both switch 1 and switch 2 is Current. Switch positions are shown in Figure 48 .

Figure 48 - 1762-IF2OF2 Switch Positions

1762-IF2OF2 Output Type Selection

<!-- image -->

The output type selection, current or voltage, is made by wiring to the appropriate terminals, Iout or Vout, and by the type/range selection bits in the Configuration Data File. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

<!-- image -->

ATTENTION: Analog outputs may fluctuate for less than a second when power is applied or removed. This characteristic is common to most analog outputs. While the majority of loads will not recognize this short signal, it is recommended that preventive measures be taken to ensure that connected equipment is not affected.

<!-- image -->

## 1762-IF2OF2 Wiring

Figure 49 shows the 1762-IF2OF2 analog expansion I/O terminal block.

Figure 49 - 1762-IF2OF2 Terminal Block Layout

<!-- image -->

Figure 50 - Differential Sensor Transmitter Types

<!-- image -->

Figure 51 - Single-ended Sensor/Transmitter Types

<!-- image -->

(1) All power supplies rated N.E.C. Class 2

1762-IF4 Input Type Selection

Select the input type, current or voltage, using the switches located on the module's circuit board and the input type/range selection bits in the Configuration Data File. See the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001. You can access the switches through the ventilation slots on the top of the module.

Figure 52 - 1762-IF4 Switch Positions

<!-- image -->

Figure 53 - 1762-IF4 Terminal Block Layout

<!-- image -->

Figure 54 - Differential Sensor Transmitter Types

<!-- image -->

<!-- image -->

Grounding the cable shield at the module end only usually provides sufficient noise immunity. However, for best cable shield performance, earth ground the shield at both ends, using a 0.01 µF capacitor at one end to block AC power ground currents, if necessary.

Figure 55 - Sensor/Transmitter Types

<!-- image -->

## 1762-OF4 Output Type Selection

The output type selection, current or voltage, is made by wiring to the appropriate terminals, Iout or Vout, and by the type/range selection bits in the Configuration Data File.

Figure 56 - 1762-OF4 Terminal Block Layout

<!-- image -->

Figure 57 - 1762-OF4 Wiring

<!-- image -->

## Notes:

## Introduction

## Supported Communication Protocols

## Default Communication Configuration

## Communication Connections

The method you use and cabling required to connect your controller depends on what type of system you are employing. This chapter also describes how the controller establishes communication with the appropriate network.

MicroLogix 1200 controllers with the additional communications port (1762-L24AWAR, 1762-L24BWAR, 1762-L24BXBR, 1762-L40AWAR, 1762-L40BWAR, 1762-L40BXBR) offer advanced communications options, providing a clean, cost effective solution for applications requiring a network connection and HMI.

The additional communications port (Programmer/HMI Port) enables two communication devices to be connected to the controller simultaneously. For example, it provides local connectivity of an operator interface or programming terminal such as DF1 PanelView™ HMI, IBM-compatible personal computer using RSLogix 500 programming software, or 1747-PSD program storage device, and also allows the primary port (Channel 0) to be connected to either a network, a modem, or an ASCII device such as a barcode reader or weigh scale.

MicroLogix 1200 controllers support the following communication protocols from the primary RS-232 communication channel, Channel 0:

- DH-485
- DF1 Full-duplex
- DF1 Half-duplex master and slave
- DF1 Radio modem
- Modbus RTU master and slave
- ASCII

The 1762-L24AWAR, 1762-L24BWAR, 1762-L24BXBR, 1762-L40AWAR, 1762-L40BWAR, and 1762-L40BXBR controllers are equipped with an additional RS-232 communication channel called the Programmer/HMI port, which supports DF1 Full-duplex only. The controller cannot initiate messages through this port. It can only respond to messages sent to it. All communication parameters are fixed and cannot be changed by a user.

See Default Communication Configuration on page 53 for the configuration settings.

For more information on MicroLogix 1200 communications, see MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

The MicroLogix 1200 has the following default communication configuration. The same default configuration is applied for both Channel 0 and the Programmer/HMI Port (for 1762-LxxxxxR only). The configurations for the Programmer/HMI Port are fixed and you cannot change them.

<!-- image -->

For Channel 0, the default configuration is present when:

- The controller is powered-up for the first time
- The Communications Toggle push button specifies default communications (the DCOMM LED is on)
- An OS upgrade is completed

See Connect to Networks via RS-232 Interface on page 97 for more information on communicating.

<!-- image -->

## Use the Communications Toggle Push Button

## Connect to the RS-232 Port

Table 6 - DF1 Full-duplex Default Configuration Parameters

| Parameter Default           |
|-----------------------------|
| Baud Rate 19.2K             |
| Parity none                 |
| Source ID (Node Address) 1  |
| Control Line no handshaking |
| Stop Bits 1                 |

The Communications Toggle push button is located on the processor under the processor door (if installed), as shown below.

Use the Communications Toggle push button to change from the user-defined communication configuration to the default communications mode and back on Channel 0. The parameters of the Programmer/HMI Port are fixed at the default communications configuration. The Default Communications (DCOMM) LED operates to show when the controller is in the default communications mode (settings shown in Table 6).

<!-- image -->

<!-- image -->

The Communications Toggle push button must be pressed and held for one second to activate.

The Communications Toggle push button only affects the communication configuration of Channel 0.

There are two ways to connect the MicroLogix 1200 programmable controller to your computer using the DF1 protocol: using a point-to-point connection, or using a modem. Descriptions of these methods follow.

<!-- image -->

ATTENTION: All devices connected to the RS-232 communication port must be referenced to controller ground, or be floating (not referenced to a potential other than ground). Failure to follow this procedure may result in property damage or personal injury.

- For 1762-L24BWA, 1762-L40BWA, 1762-L24BWAR and 1762-L40BWAR controllers: The COM of the sensor supply is also connected to chassis ground internally. The 24V DC sensor power source should not be used to power output circuits. It should only be used to power input devices.
- For 1762-L24BXB, 1762-L40BXB, 1762-L24BXBR and 1762-L40BXBR controllers: The VDC NEUT or common terminal of the power supply is also connected to chassis ground internally.

Table 7 - Available Communication Cables

| Communication Cables Length                      |
|--------------------------------------------------|
| 1761-CBL-PM02 series C or later 2 m (6.5 ft.)    |
| 1761-CBL-HM02 series C or later 2 m (6.5 ft.)    |
| 1761-CBL-AM00 series C or later 45 cm (17.7 in.) |
| 1761-CBL-AP00 series C or later 45 cm (17.7 in.) |
| 1761-CBL-PH02 series A or later 2 m (6.5 ft.)    |
| 1761-CBL-AH02 series A or later 2 m (6.5 ft.)    |
| 2707-NC8 series A or later 2 m (6.5 ft.)         |
| 2707-NC9 series B or later 15 m (49.2 ft.)       |
| 2707-NC10 series B or later 2 m (6.5 ft.)        |
| 2707-NC11 series B or later 2 m (6.5 ft.)        |

## Make a DF1 Point-to-Point Connection

You can connect the MicroLogix 1200 programmable controller to your computer using a serial cable (1761-CBL-PM02) from your personal computer's serial port to the controller's Channel 0 and/or the Programmer/HMI port (for 1762-LxxxxxR only). The recommended protocol for this configuration is DF1 Full-duplex.

We recommend using an Advanced Interface Converter (AIC+), catalog number 1761-NET-AIC, as your optical isolator, as shown on the following page. See Cable Selection Guide on page 62 for specific AIC+ cabling information.

<!-- image -->

## Use a Modem

You can use modems to connect a computer to one MicroLogix 1200 controller (using DF1 Fullduplex protocol), to multiple controllers (using DF1 Half-duplex protocol), or Modbus RTU slave protocol via Channel 0, as shown in Figure 58. See Connect to Networks via RS-232 Interface on page 97 for information on types of modems you can use with the micro controllers.

## IMPORTANT

Do not attempt to use DH-485 protocol through modems under any circumstance. The communication timing using the DH-485 protocol is not supported by modem communications.

<!-- image -->

We recommend using an AIC+, catalog number 1761-NET-AIC, as your optical isolator. See Cable Selection Guide on page 62 for specific AIC+ cabling information.

## Isolated Modem Connection

Using an AIC+ to isolate the modem is illustrated in Figure 59 .

Figure 59 - Isolated Modem Connection Example

<!-- image -->

(1) Series C or later cables are required.

For additional information on connections using the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

## Construct Your Own Modem Cable

If you construct your own modem cable, the maximum cable length is 15.24 m (50 ft.) with a 25-pin or 9-pin connector. See Figure 60 for constructing a straight-through cable.

Figure 60 - Straight-through Cable Typical Pinout

<!-- image -->

| DTE Device (AIC+, MicroLogix, SLC™, PLC)   | DCE Device (Modem, PanelView)   | DCE Device (Modem, PanelView)   |
|--------------------------------------------|---------------------------------|---------------------------------|
| 9-pin 25-pin 9-pin                         | 3 TXD TXD 2 3                   |                                 |
|                                            | 2 RXD RXD 3 2                   |                                 |
|                                            | 5 GND GND 7 5                   |                                 |
|                                            | 1 DCD DCD 8 1                   |                                 |
|                                            | 4 DTR DTR 20 4                  |                                 |
|                                            | 6 DSR DSR 6 6                   |                                 |
|                                            | 8 CTS CTS 5 8                   |                                 |
|                                            | 7 RTS RTS 4 7                   |                                 |

## Construct Your Own Null Modem Cable

If you construct your own null modem cable, the maximum cable length is 15.24 m (50 ft.) with a 25-pin or 9-pin connector. See Figure 61 for constructing a null modem cable.

Figure 61 - Null Modem Cable Typical Pinout

<!-- image -->

| DTE Device (AIC+, MicroLogix, SLC, PLC)   | DTE Device (AIC+, MicroLogix, SLC, PLC)   |
|-------------------------------------------|-------------------------------------------|
|                                           | 9-pin 25-pin 9-pin                        |
|                                           | 3 TXD TXD 2 3                             |
|                                           | 2 RXD RXD 3 2                             |
|                                           | 5 GND GND 7 5                             |
|                                           | 1 DCD DCD 8 1                             |
|                                           | 4 DTR DTR 20 4                            |
|                                           | 6 DSR DSR 6 6                             |
|                                           | 8 CTS CTS 5 8                             |
|                                           | 7 RTS RTS 4 7                             |

## DF1 Half-duplex Master/Slave Network

Use Figure 62 for DF1 Half-duplex master/slave protocol without hardware handshaking.

Figure 62 - DF1 Half-duplex Master/Slave Protocol

<!-- image -->

- (1) DB-9 RS-232 port
- (2) mini-DIN 8 RS-232 port
- (3) RS-485 port
- (4) Series C or later cables are required.

## Connect to a DH-485 Network

Figure 63 shows how to connect to a DH-485 network.

Figure 63 - Connect to a DH-485 Network

<!-- image -->

- (1) DB-9 RS-232 port
- (2) mini-DIN 8 RS-232 port
- (3) RS-485 port
- (4) Series C or later cables are required.

## Recommended Tools

To connect a DH-485 network, you need tools to strip the shielded cable and to attach the cable to the AIC+ Advanced Interface Converter. We recommend the following equipment (or equivalent):

Table 8 - Working with Cable for DH-485 Network

| Description Part Number Manufacturer                   |
|--------------------------------------------------------|
| Shielded Twisted Pair Cable #3106A or #9842 Belden     |
| Stripping Tool Not applicable Not applicable           |
| 1/8” Slotted Screwdriver Not applicable Not applicable |

## DH-485 Communication Cable

The suggested DH-485 communication cable is either Belden #3106A or #9842. The cable is jacketed and shielded with one or two twisted-wire pairs and a drain wire.

One pair provides a balanced signal line and one additional wire is used for a common reference line between all nodes on the network. The shield reduces the effect of electrostatic noise from the industrial environment on network communication.

The communication cable consists of a number of cable segments daisy-chained together. The total length of the cable segments cannot exceed 1219 m (4000 ft.). However, two segments can be used to extend the DH-485 network to 2438 m (8000 ft.). For additional information on connections using the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

When cutting cable segments, make them long enough to route them from one AIC+ to the next, with sufficient slack to prevent strain on the connector. Allow enough extra cable to prevent chafing and kinking in the cable.

Use these instructions for wiring the Belden #3106A or #9842 cable. See Cable Selection Guide on page 62 if you are using standard Allen-Bradley cables.

## Connect the Communication Cable to the DH-485 Connector

<!-- image -->

We recommend a daisy-chained network. Do not make the incorrect connection that is shown in Figure 64 .

Figure 64 - Daisy-chained Cables Connection Example

<!-- image -->

Single Cable Connection

When connecting a single cable to the DH-485 connector, use Figure 65 .

Figure 65 - Single Cable Connection Example

<!-- image -->

Multiple Cable Connection

When connecting multiple cables to the DH-485 connector, use Figure 66 .

Figure 66 - Multiple Cable Connection Examples

<!-- image -->

Table 9 - Connections using Belden #3106A Cable

| For This Wire/Pair Connect This Wire To This Terminal   |                                               |
|---------------------------------------------------------|-----------------------------------------------|
|                                                         | Shield/drain Non-jacketed Terminal 2 - Shield |
|                                                         | Blue Blue Terminal 3 - Common                 |
| White/orange                                            | White with orange stripe Terminal 4 - Data B  |
| White/orange                                            | Orange with white stripe Terminal 5 - Data A  |

## Connect the AIC+

Table 10 - Connections using Belden #9842 Cable

|              | For This Wire/Pair Connect This Wire To This Terminal   |
|--------------|---------------------------------------------------------|
|              | Shield/drain Non-jacketed Terminal 2 - Shield           |
| Blue/white   | White with blue stripe  Cut back - no connection(1)     |
| Blue/white   | Blue with white stripe Terminal 3 - Common              |
| White/orange | White with orange stripe Terminal 4 - Data B            |
| White/orange | Orange with white stripe Terminal 5 - Data A            |

## Ground and Terminate the DH-485 Network

Only one connector at the end of the link must have Terminals 1 and 2 jumpered together. This provides an earth ground connection for the shield of the communication cable.

Both ends of the network must have Terminals 5 and 6 jumpered together, as shown in Figure 67. This connects the termination impedance (of 120 Ω) that is built into each AIC+ as required by the DH-485 specification.

Figure 67 - End-of-Line Termination

<!-- image -->

The AIC+, catalog number 1761-NET-AIC, enables a MicroLogix 1200 controller to connect to a DH-485 network. The AIC+ has two RS-232 ports and one isolated RS-485 port. Typically, there is one AIC+ for each MicroLogix 1200 controller. When two MicroLogix controllers are closely positioned, you can connect a controller to each of the RS-232 ports on the AIC+.

The AIC+ can also be used as an RS-232 isolator, providing an isolation barrier between the MicroLogix 1200 communications port and any equipment connected to it (for example a computer or modem).

Figure 68 shows the external wiring connections and specifications of the AIC+.

Figure 68 - AIC+ External Wiring Connections

<!-- image -->

| Item Description                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------|
| 1 Port 1 - DB-9 RS-232, DTE                                                                                            |
| 2 Port 2 - mini-DIN 8 RS-232 DTE                                                                                       |
| 3 Port 3 - RS-485 Phoenix plug                                                                                         |
| 4  DC Power Source selector switch (Cable = Port 2 power source, External = External power source connected to item 5) |
| 5 Terminals for external 24V DC power supply and chassis ground                                                        |

For additional information on connecting the AIC+, see the AIC+ Advanced Interface Converter User Manual, publication 1761-UM004 .

## Cable Selection Guide

<!-- image -->

|                                                 |                                              | Cable Length Connections From To AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | SLC 5/03 or SLC 5/04 processors, ch 0 Port 2 Yes External                   |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | MicroLogix 1000, 1200, or 1500 Port 1 Yes External                          |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | PanelView 550 through NULL modem adapter Port 2 Yes External                |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | DTAM™ Plus / DTAM Micro™ Port 2 Yes External                                |                                      |
| 1761-CBL-AP00(2) 1761-CBL-PM02(2) 1761-CBL-PH02 | 45 cm (17.7 in.) 2 m (6.5 ft.) 2 m (6.5 ft.) | PC COM port Port 2 Yes External                                             |                                      |

(1) An external power supply is required unless the AIC+ is powered by the device connected to port 2, then the selection switch should be set to cable.

(2) Series C or later cables are required.

<!-- image -->

|                                                 |                             | Cable Length Connections From To AIC+          | External Power Supply Required (1)   | Power Selection Switch Settings   |
|-------------------------------------------------|-----------------------------|------------------------------------------------|--------------------------------------|-----------------------------------|
| 1761-CBL-AM00(2) 1761-CBL-HM02(2) 1761-CBL-AH02 | 45 cm (17.7 in.)            | MicroLogix 1000, 1200, or 1500 Port 2 No Cable |                                      |                                   |
|                                                 | 2 m (6.5 ft.) 2 m (6.5 ft.) | To port 2 on another AIC+ Port 2 Yes External  |                                      |                                   |

(1) An external power supply is required unless the AIC+ is powered by the device connected to port 2, then the selection switch should be set to cable.

(2) Series C or later cables are required.

<!-- image -->

|                           |                                | Cable Length Connections From To AIC+  External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|---------------------------|--------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | SLC 5/03 or SLC 5/04 processor, channel 0 Port 1 Yes External               |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | PC COM port Port 1 Yes External                                             |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | PanelView 550 through NULL modem adapter Port 1 Yes External                |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | DTAM Plus / DTAM Micro Port 1 Yes External                                  |                                      |
| 1747-CP3 1761-CBL-AC00(2) | 3 m (9.8 ft.) 45 cm (17.7 in.) | Port 1 on another AIC+ Port 1 Yes External                                  |                                      |

<!-- image -->

| Cable Length Connections From To AIC+                                              | External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|------------------------------------------------------------------------------------|--------------------------------------|--------------------------------------|
| Straight 9-pin to 25-pin — Modem or other communication device Port 1 Yes External |                                      |                                      |

<!-- image -->

|                             |                                 | Cable Length Connections From To AIC+                       | External Power Supply Required (1)   | Power Selection Switch Setting (1)   |
|-----------------------------|---------------------------------|-------------------------------------------------------------|--------------------------------------|--------------------------------------|
| 1761-CBL-AS03 1761-CBL-AS09 | 3 m (9.8 ft.) 9.5 m (31.17 ft.) | SLC™ 500 Fixed, SLC 5/01, SLC 5/02, and SLC 5/03 processors |                                      | Port 3 Yes External                  |
| 1761-CBL-AS03 1761-CBL-AS09 | 3 m (9.8 ft.) 9.5 m (31.17 ft.) | PanelView 550 RJ45 port Port 3 Yes External                 |                                      |                                      |

1761-CBL-PM02 Series C (or equivalent) Cable Wiring Diagram

<!-- image -->

<!-- image -->

## Recommended User-supplied Components

These components can be purchased from your local electronics supplier.

Table 11 - User-supplied Components

| Component Recommended Model                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|
| External power supply and chassis ground Power supply rated for 20.4…28.8V DC                                     |
| NULL modem adapter Standard AT                                                                                    |
| Straight 9-pin to 25-pin RS-232 cable  See Figure 69 and Table 12 for port information if making your own cables. |

Figure 69 - Port Pinout

<!-- image -->

Table 12 - Cable Assignment

| Pin Port 1: DB-9 RS-232  Port 2(1): (1761-CBL-PM02 cable) Port 3: RS-485 Connector   |
|--------------------------------------------------------------------------------------|
| 1 Received line signal detector (DCD) 24V DC Chassis ground                          |
| 2 Received data (RxD) Ground (GND) Cable shield                                      |
| 3 Transmitted data (TxD) Request to send (RTS) Signal ground                         |
| 4  DTE ready (DTR) (2) Received data (RxD)(3) DH-485 data B                          |
| 5 Signal common (GND) Received line signal detector (DCD) DH-485 data A              |
| 6  DCE ready (DSR)(2)  Clear to send (CTS)(3)  Termination                           |
| 7 Request to send (RTS) Transmitted data (TxD) Not applicable                        |
| 8 Clear to send (CTS) Ground (GND) Not applicable                                    |
| 9 Not applicable Not applicable Not applicable                                       |

## Safety Considerations

This equipment is suitable for use in Class I Division 2, Groups A, B, C, D or non-hazardous locations only.

<!-- image -->

## WARNING: EXPLOSION HAZARD

AIC+ must be operated from an external power source.

This product must be installed in an enclosure. All cables connected to the product must remain in the enclosure or be protected by conduit or other means.

See Safety Considerations on page 13 for additional information.

## Install and Attach the AIC+

1. Take care when installing the AIC+ in an enclosure so that the cable connecting the MicroLogix controller to the AIC+ does not interfere with the enclosure door.

<!-- image -->

<!-- image -->

2. Carefully plug the terminal block into the RS-485 port on the AIC+ you are putting on the network. Allow enough cable slack to prevent stress on the plug.
3. Provide strain relief for the Belden cable after it is wired to the terminal block. This guards against breakage of the Belden cable wires.

## Power the AIC+

In normal operation with the MicroLogix programmable controller connected to port 2 of the AIC+, the controller powers the AIC+. Any AIC+ not connected to a MicroLogix controller requires a 24V DC power supply. The AIC+ requires 120 mA at 24V DC.

If both the controller and external power are connected to the AIC+, the power selection switch determines what device powers the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if a higher voltage supply is used.

Set the DC Power Source selector switch to EXTERNAL before connecting the power supply to the AIC+. Figure 70 shows where to connect external power for the AIC+.

Figure 70 - External Power for AIC+

<!-- image -->

ATTENTION: Always connect the CHS GND (chassis ground) terminal to the nearest earth ground. This connection must be made whether or not an external 24V DC supply is used.

<!-- image -->

Power Options

There are two options for powering the AIC+:

- Use the 24V DC user power supply built into the MicroLogix 1200 controller. The AIC+ is powered through a hard-wired connection using a communication cable (1761-CBL-HM02, or equivalent) connected to port 2.
- Use an external DC power supply with the following specifications:
- Operating voltage: 24V DC (-15%/+20%)
- Output current: 150 mA minimum
- Rated NEC Class 2

Make a hard-wired connection from the external supply to the screw terminals on the bottom of the AIC+.

<!-- image -->

ATTENTION: If you use an external power supply, it must be 24V DC (-15%/+20%). Permanent damage results if miswired with the wrong power source.

## Notes:

## Trimpot Operation

## Use Trimpots

The processor has two trimming potentiometers (trimpots) which allow modification of data within the controller. Adjustments to the trimpots change the value in the corresponding Trimpot Information (TPI) register. The data value of each trimpot can be used throughout the control program as timer, counter, or analog presets depending upon the requirements of the application.

The trimpots are located below the memory module port cover and to the right of the communications port, as shown in Figure 71 .

Figure 71 - Location of Trimpots

<!-- image -->

Use a small flathead screwdriver to turn the trimpots. Adjusting their value causes data to change within a range of 0…250 (fully clockwise). The maximum rotation of each trimpot is three-quarters, as shown in Figure 72. Trimpot stability over time and temperature is typically ±2 counts.

Figure 72 - Maximum Rotation of Trimpot

<!-- image -->

Trimpot file data is updated continuously whenever the controller is powered up.

## Trimpot Information Function File

The composition of the TPI Function File is described in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

## Error Conditions

Error conditions of the TPI Function File are described in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

<!-- image -->

## Notes:

## Real-time Clock Operation

<!-- image -->

## Use Real-time Clock and Memory Modules

<!-- image -->

For more information on 'Real-time Clock Function File' and 'Memory Module Information File', see the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

Three modules with different levels of functionality are available for use with the MicroLogix 1200 controller.

| Catalog Number Function                       |
|-----------------------------------------------|
| 1762-RTC Real-time Clock                      |
| 1762-MM1 Memory Module                        |
| 1762-MM1RTC Memory Module and Real-time Clock |

## Removal/Insertion Under Power

At power-up and when the controller enters a run or test mode, the controller determines if a real-time clock module (RTC) is present. If an RTC is present, its values (date, time, and status) are written to the RTC Function File in the controller.

The RTC module can be installed or removed at any time without risk of damage to either the module or the controller. If an RTC is installed while the MicroLogix 1200 controller is in a run or test mode, the module is not recognized until either a power cycle occurs or until the controller is placed in a non-executing mode (program mode, suspend mode, or fault condition).

Removal of the RTC during run mode is detected within one program scan. Removal of the RTC while in run mode causes the controller to write zeros to the RTC Function File.

Table 13 indicates the accuracy of the RTC for various temperatures.

Table 13 - RTC Accuracy

| Ambient Temperature  Accuracy(1)         |
|------------------------------------------|
| 0 °C (+32 °F) +34…-70 seconds/month      |
| +25 °C (+77 °F) +36…-68 seconds/month    |
| +40 °C (+104 °F) +29…-75 seconds/month   |
| +55 °C (+131 °F) -133…-237 seconds/month |

## Write Data to the Real-time Clock

When valid data is sent to the real-time clock from the programming device or another controller, the new values take effect immediately.

The real-time clock does not allow you to load or store invalid date or time data.

Use the Disable Clock button in your RSLogix programming software to disable the real-time clock before storing a module. This decreases the drain on the RTC battery during storage.

## Memory Module Operation

## RTC Battery Operation

The real-time clock has an internal battery that is not replaceable. The RTC Function File features a battery low indicator bit (RTC:0/BL), which shows the status of the RTC battery. When the battery is low, the indicator bit is set (1). This means that the battery may fail within 14 days and the real-time clock module needs to be replaced. When the battery low indicator bit is clear (0), the battery level is acceptable or a real-time clock is not attached.

If the RTC battery is low and the controller is powered, the RTC operates normally. If the controller power is removed and the RTC battery is low, RTC data is lost.

| Life Span Operating Temperature   | Storage Temperature(1)                               |
|-----------------------------------|------------------------------------------------------|
|                                   | 5 years 0…40 °C (32…104 °F) -40…+60 °C (-40…+140 °F) |

(1) Stored for six months.

<!-- image -->

ATTENTION: Operating with a low battery indication for more than 14 days may result in invalid RTC data unless power is on continuously.

The memory module supports the following features:

- User Program and Data Back-up
- User Program Compare
- Data File Download Protection
- Memory Module Write Protection
- Removal/Insertion Under Power

<!-- image -->

ATTENTION: Electrostatic discharge can damage the memory module. Do not touch the connector pins or other sensitive areas.

## User Program and Data Back-up

The memory module provides a simple and flexible program/data transport mechanism, allowing the user to transfer the program and data to the controller without the use of a personal computer and programming software.

The memory module can store one user program at a time.

During program transfers to or from the memory module, the controller's RUN LED flashes.

## Program Compare

The memory module can also provide application security, allowing you to specify that if the program stored in the memory module does not match the program in the controller, the controller will not enter an executing (run or test) mode. To enable this feature, set the S:2/9 bit in the system status file. See 'Status System File' in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for more information.

## Data File Download Protection

The memory module supports data file download protection. This allows user data to be saved (not overwritten) during a download.

<!-- image -->

Data file download protection is only functional if the processor does not have a fault, size of all protected data files in the memory module exactly match the size of protected data files within the controller, and all protected data files are of the same type. See 'Protecting Data Files During Download' in the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

## Memory Module Write Protection

The memory module supports write-once, read-many behavior. Write protection is enabled using your programming software.

## IMPORTANT

Once set, write protection cannot be removed. A change cannot be made to the control program stored in a write-protected memory module. If a change is required, use a different memory module.

## Removal/Insertion Under Power

The memory module can be installed or removed at any time without risk of damage to either the memory module or the controller, except during a data transaction. If the memory module is removed during a data transaction, data corruption can occur.

If a memory module is installed while the MicroLogix 1200 controller is executing, the memory module is not recognized until either a power cycle occurs, or until the controller is placed in a non-executing mode (program mode, suspend mode, or fault condition).

## Notes:

## Controller Specifications

## General Specifications

| Attribute                                                       | 1762-L24AWA 1762-L24AWAR                                                                                           | 1762-L24BWA 1762-L24BWAR                                                                                           | 1762-L24BXB 1762-L24BXBR                                                                                           | 1762-L40AWA 1762-L40AWAR                                                                                           | 1762-L40BWA 1762-L40BWAR                                                                                           | 1762-L40BXB 1762-L40BXBR                                                                                           |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Dimensions                                                      | Height: 90 mm (3.54 in.), 104 mm (4.09 in.) (with DIN latch open) Width: 110 mm (4.33 in.) Depth: 87 mm (3.42 in.) | Height: 90 mm (3.54 in.), 104 mm (4.09 in.) (with DIN latch open) Width: 110 mm (4.33 in.) Depth: 87 mm (3.42 in.) | Height: 90 mm (3.54 in.), 104 mm (4.09 in.) (with DIN latch open) Width: 110 mm (4.33 in.) Depth: 87 mm (3.42 in.) | Height: 90 mm (3.54 in.), 104 mm (4.09 in.) (with DIN latch open) Width: 160 mm (6.30 in.) Depth: 87 mm (3.42 in.) | Height: 90 mm (3.54 in.), 104 mm (4.09 in.) (with DIN latch open) Width: 160 mm (6.30 in.) Depth: 87 mm (3.42 in.) | Height: 90 mm (3.54 in.), 104 mm (4.09 in.) (with DIN latch open) Width: 160 mm (6.30 in.) Depth: 87 mm (3.42 in.) |
|                                                                 | Shipping weight 0.9 kg (2.0 lbs) 1.1 kg (2.4 lbs)                                                                  | Shipping weight 0.9 kg (2.0 lbs) 1.1 kg (2.4 lbs)                                                                  | Shipping weight 0.9 kg (2.0 lbs) 1.1 kg (2.4 lbs)                                                                  |                                                                                                                    |                                                                                                                    |                                                                                                                    |
|                                                                 | Number of I/O 14 inputs, 10 outputs 24 inputs, 16 outputs                                                          | Number of I/O 14 inputs, 10 outputs 24 inputs, 16 outputs                                                          | Number of I/O 14 inputs, 10 outputs 24 inputs, 16 outputs                                                          |                                                                                                                    |                                                                                                                    |                                                                                                                    |
| Power supply voltage                                            | 100…240V AC (-15%, +10%) @ 47…63 Hz                                                                                | 100…240V AC (-15%, +10%) @ 47…63 Hz                                                                                | 24V DC (-15%, +10%) Class 2, SELV                                                                                  | 100…240V AC (-15%, +10%) @ 47…63 Hz                                                                                | 100…240V AC (-15%, +10%) @ 47…63 Hz                                                                                | 24V DC (-15%, +10%) Class 2, SELV                                                                                  |
| Heat dissipation 15.2 W 15.7 W 17.0 W 21.0 W 22.0 W 27.9 W      | Heat dissipation 15.2 W 15.7 W 17.0 W 21.0 W 22.0 W 27.9 W                                                         |                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |
| Power supply inrush current                                     | 120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                                                                      | 120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                                                                      | 24V DC: 15 A for 20 ms                                                                                             | 120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                                                                      | 120V AC: 25 A for 8 ms 240V AC: 40 A for 4 ms                                                                      | 24V DC: 15 A for 30 ms                                                                                             |
| Power supply usage 68VA 70VA 27 W 80VA 82VA 40 W                | Power supply usage 68VA 70VA 27 W 80VA 82VA 40 W                                                                   |                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |
| Power supply output                                             | 5V DC 400 mA                                                                                                       | 400 mA(1)                                                                                                          |                                                                                                                    | 400 mA 600 mA                                                                                                      | 600 mA(2)                                                                                                          | 600 mA                                                                                                             |
| Power supply output                                             | 24V DC 350 mA                                                                                                      | 350 mA(1)                                                                                                          |                                                                                                                    | 350 mA 500 mA                                                                                                      | 500 mA(2)                                                                                                          | 500 mA                                                                                                             |
| Sensor power output none                                        | Sensor power output none                                                                                           | 250 mA @ 24V DC AC Ripple < 500 mV peak-to-peak 400 µF max. (1)                                                    |                                                                                                                    | none none                                                                                                          | 400 mA @ 24V DC AC Ripple < 500 mV peak to-peak 400 µF max. (2)                                                                                                                    | none                                                                                                               |
| Input circuit type 120V AC                                      | Input circuit type 120V AC                                                                                         | 24V DC sinking/sourcing                                                                                            | 24V DC sinking/sourcing                                                                                            | 120V AC                                                                                                            | 24V DC sinking/sourcing                                                                                            | 24V DC sinking/sourcing                                                                                            |
| Output circuit type Relay Relay Relay/FET Relay Relay Relay/FET | Output circuit type Relay Relay Relay/FET Relay Relay Relay/FET                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |                                                                                                                    |

Terminal screw torque 0.791 N·m (7 lb·in) rated

(1) Do not allow the total load power consumed by the 5V DC, 24V DC, and sensor power outputs to exceed 12 W.

(2) Do not allow the total load power consumed by the 5V DC, 24V DC, and sensor power outputs to exceed 16 W.

See System Loading and Heat Dissipation on page 105 for system validation worksheets.

## Input Specifications

| Attribute                                           | 1762-L24AWA 1762-L40AWA 1762-L24AWAR              | 1762-L24BWA, 1762-L24BXB, 1762-L40BWA, 1762-L40BXB 1762-L24BWAR, 1762-L24BXBR, 1762-L40BWAR, 1762-L40BXBR   | 1762-L24BWA, 1762-L24BXB, 1762-L40BWA, 1762-L40BXB 1762-L24BWAR, 1762-L24BXBR, 1762-L40BWAR, 1762-L40BXBR   |
|-----------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|                                                     | 1762-L40AWAR                                      |                                                                                                             | Inputs 0…3 Inputs 4 and Higher                                                                              |
| On-state voltage range 79…132V AC                   |                                                   | 14…24V DC (+10% @ 55 °C/131 °F) (+25% @ 30 °C/86 °F)                                                        | 10…24V DC (+10% @ 55 °C/131 °F) (+25% @ 30 °C/86 °F)                                                        |
| Off-state voltage range 0…20V AC 0…5V DC            |                                                   |                                                                                                             |                                                                                                             |
| Operating frequency 47…63 Hz 0 Hz…20 kHz            |                                                   |                                                                                                             | 0 Hz…1 kHz (scan time dependent)                                                                            |
| On-state current: Minimum Nominal Maximum           | 5.0 mA @ 79V AC 12 mA @ 120V AC 16.0 mA @ 132V AC | 2.5 mA @ 14V DC 7.3 mA @ 24V DC 12.0 mA @ 30V DC                                                            | 2.0 mA @ 10V Dc 8.9 mA @ 24V Dc 12.0 mA @ 30V DC                                                            |
| Off-state leakage current                           | 2.5 mA max. 1.5 mA min.                           |                                                                                                             |                                                                                                             |
| Nominal impedance                                   | 12 kΩ @ 50 Hz 10 kΩ @ 60 Hz                       | 3.3 kΩ                                                                                                      | 2.7 kΩ                                                                                                      |
| Inrush current @ 120V AC, max 250 mA Not applicable |                                                   |                                                                                                             |                                                                                                             |

## Specifications

<!-- image -->

## Output Specifications

| Attribute                                   | 1762-L24AWA 1762-L24BWA 1762-L24AWAR 1762-L24BWAR              | 1762-L24BXB 1762-L24BXBR                                       | 1762-L40AWA 1762-L40BWA 1762-L40AWAR 1762-L40BWAR              | 1762-L40BXB 1762-L40BXBR                                       |
|---------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Relay and FET Outputs                       |                                                                |                                                                |                                                                |                                                                |
| Controlled load, max 1440VA – 1440VA 1440VA |                                                                |                                                                |                                                                |                                                                |
| Continuous current, max                     |                                                                |                                                                |                                                                |                                                                |
| Current per group common 8 A 7.5 A 8 A 8 A  |                                                                |                                                                |                                                                |                                                                |
| Current per controller                      | @ 150V max 30 A or total of per-point loads, whichever is less | @ 150V max 30 A or total of per-point loads, whichever is less | @ 150V max 30 A or total of per-point loads, whichever is less | @ 150V max 30 A or total of per-point loads, whichever is less |
| Current per controller                      | @ 240V max 20 A or total of per-point loads, whichever is less | @ 240V max 20 A or total of per-point loads, whichever is less | @ 240V max 20 A or total of per-point loads, whichever is less | @ 240V max 20 A or total of per-point loads, whichever is less |
| Relay Outputs                               |                                                                |                                                                |                                                                |                                                                |
| Turn on time/Turn off time, min             | 10 ms(1)                                                       | 10 ms(1)                                                       | 10 ms(1)                                                       | 10 ms(1)                                                       |
| Relay life - Electrical See Figure 73       |                                                                |                                                                |                                                                |                                                                |
| Relay life - Mechanical 20,000,000 cycles   |                                                                |                                                                |                                                                |                                                                |
| Load current, min 10 mA                     |                                                                |                                                                |                                                                |                                                                |

## Relay Contact Ratings

| Maximum Volts        | Amperes   | Amperes Continuous Continuous Make Break Make Break          | Voltamperes   |
|----------------------|-----------|----------|---------------|
| 240V AC 7.5 A 0.75 A |           | 2.5 A(1) | 1800VA 180VA  |
| 120V AC 15 A 1.5 A   |           | 2.5 A(1) | 1800VA 180VA  |
| 125V DC              | 0.22 A(2) | 1.0 A    |               |
| 24V DC               | 1.2 A(2)  | 2.0 A    | 28VA          |

<!-- image -->

ATTENTION: Do not exceed the "Current per group common" specification.

## Figure 73 - Relay Life Chart

<!-- image -->

## BXB FET Output Specifications

|                                                                         | Attribute General Operation              | High Speed Operation (1) (Output 2 Only)   |
|-------------------------------------------------------------------------|------------------------------------------|--------------------------------------------|
|                                                                         | Power supply voltage 24V DC (-15%, +10%) |                                            |
| On-state voltage drop: At maximum load current At maximum surge current | 1V DC 2.5V DC                            | Not applicable Not applicable              |
| Current rating per point: Maximum load Minimum load Maximum leakage     | See graphs below. 1.0 mA 1.0 mA          | 100 mA 10 mA 1.0 mA                        |

Maximum output current (temperature dependent):

<!-- image -->

FET Total Current

(1762-L40BXB and L40BXBR)

<!-- image -->

| Surge current per point: Peak current Maximum surge duration g Maximum rate of repetition @ 30 °C (86 °F) °° p Maximum rate of repetition @ 55 °C (131 °F)                                        | 4.0 A 10 ms Once every second Once every 2 seconds   | Not applicable Not applicable Not applicable Not applicable   |
|----------------------------------------|------------------------------------------------------|---------------------------------------------------------------|
| Turn-on time, max 0.1 ms 6 µs          |                                                      |                                                               |
| Turn-off time, max 1.0 ms 18 µs        |                                                      |                                                               |
| Repeatability, max Not applicable 2 µs |                                                      |                                                               |
|                                        |                                                      | Drift, max Not applicable 1 µs per 5 °C (41 °F)               |

## AC Input Filter Settings

|                             | On-delay (ms) Off-delay (ms)   | On-delay (ms) Off-delay (ms)    |
|-----------------------------|--------------------------------|---------------------------------|
| Nominal Filter Setting (ms) |                                | Minimum Maximum Minimum Maximum |
|                             |                                | 8 2 20 10 20                    |

## Fast DC Input Filter Settings (Inputs 0…3)

| Nominal Filter Setting (ms)   | On-delay (ms) Off-delay (ms)    | Maximum Counter Frequency 50% Duty Cycle   |
|-------------------------------|---------------------------------|--------------------------------------------|
|                               | Minimum Maximum Minimum Maximum | Maximum Counter Frequency 50% Duty Cycle   |
|                               |                                 | 0.025 0.005 0.025 0.005 0.025 20.0 kHz     |
|                               |                                 | 0.075 0.040 0.075 0.045 0.075 6.7 kHz      |
|                               |                                 | 0.100 0.050 0.100 0.060 0.100 5.0 kHz      |
|                               |                                 | 0.250 0.170 0.250 0.210 0.250 2.0 kHz      |
|                               |                                 | 0.500 0.370 0.500 0.330 0.500 1.0 kHz      |
|                               |                                 | 1.00 0.700 1.000 0.800 1.000 0.5 kHz       |
|                               |                                 | 2.000 1.700 2.000 1.600 2.000 250 Hz       |

## Fast DC Input Filter Settings (Inputs 0…3) (Continued)

| Nominal Filter Setting (ms)   | On-delay (ms) Off-delay (ms)             | On-delay (ms) Off-delay (ms)    | Maximum Counter Frequency 50% Duty Cycle   |
|-------------------------------|------------------------------------------|---------------------------------|--------------------------------------------|
|                               |                                          | Minimum Maximum Minimum Maximum |                                            |
|                               |                                          |                                 | 4.000 3.400 4.000 3.600 4.000 125 Hz       |
| 8.000(1)                      |                                          |                                 | 6.700 8.000 7.300 8.000 63 Hz              |
|                               | 16.000 14.000 16.000 14.000 16.000 31 Hz |                                 |                                            |

## Normal DC Input Filter Settings (Inputs 4 and Higher)

| Nominal Filter Setting (ms)   | On-delay (ms) Off-delay (ms)             | Maximum Frequency 50% Duty Cycle      |
|-------------------------------|------------------------------------------|---------------------------------------|
|                               | Minimum Maximum Minimum Maximum          |                                       |
|                               |                                          | 0.500 0.090 0.500 0.020 0.500 1.0 kHz |
|                               |                                          | 1.000 0.500 1.000 0.400 1.000 0.5 kHz |
|                               |                                          | 2.000 1.100 2.000 1.300 2.000 250 Hz  |
|                               |                                          | 4.000 2.800 4.000 2.700 4.000 125 Hz  |
| 8.000(1)                      |                                          | 5.800 8.000 5.300 8.000 63 Hz         |
|                               | 16.000 11.000 16.000 10.000 16.000 31 Hz |                                       |

## Working Voltage – 1762-L24AWA, 1762-L40AWA, 1762-L24AWAR, 1762-L40AWAR

| Attribute Value                           |                                                                                                                                                                                                           |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power supply input to backplane isolation | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                             |
| Input group to backplane isolation        | Verified by one of the following dielectric tests: 1517V AC for 1 second or 2145V DC for 1 second 132V AC Working Voltage (IEC Class 2 reinforced insulation)                                             |
| Input group to input group isolation      | Verified by one of the following dielectric tests: 1517V ACfor 1 second or 2145V DC for 1 second 132V AC Working Voltage (basic insulation)                                                               |
| Output group to backplane isolation       | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                             |
| Output group to output group isolation    | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (basic insulation) 150V AC Working Voltage (IEC Class 2 reinforced insulation). |

## Working Voltage – 1762-L24BWA, 1762-L40BWA, 1762-L24BWAR, 1762-L40BWAR

| Attribute Value                                                             |                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power supply input to backplane isolation                                   | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V AC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 second or 1697V DC for 1 second 75V DC Working Voltage (IEC Class 2 reinforced insulation)                                          |
| Output group to backplane isolation                                         | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation)                                         |
| Output group to output group isolation                                      | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage – 1762-L24BXB, 1762-L40BXB, 1762-L24BXBR, 1762-L40BXBR

| Attribute Value                                                             |                                                                                                                                                              |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input group to backplane isolation and input group to input group isolation | Verified by one of the following dielectric tests: 1200V AC for 1 second or 1697V DC for 1 second 75V DC Working Voltage (IEC Class 2 reinforced insulation) |
| FET output group to backplane isolation                                     | Verified by one of the following dielectric tests: 1200V AC for 1 second or 1697V DC for 1 second 75V DC Working Voltage (IEC Class 2 reinforced insulation) |

## Working Voltage – 1762-L24BXB, 1762-L40BXB, 1762-L24BXBR, 1762-L40BXBR (Continued)

| Attribute Value                                                         |                                                                                                                                                                                                       |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Relay output group to backplane isolation                               | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (IEC Class 2 reinforced insulation).                                        |
| Relay output group to relay output group and FET output group isolation | Verified by one of the following dielectric tests: 1836V AC for 1 second or 2596V DC for 1 second 265V AC Working Voltage (basic insulation) 150V Working Voltage (IEC Class 2 reinforced insulation) |

## Environmental Specifications

| Attribute            | 1762-L24AWA 1762-L24AWAR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1762-L24BWA 1762-L24BWAR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1762-L24BXB 1762-L24BXBR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1762-L40AWA 1762-L40AWAR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1762-L40BWA 1762-L40BWAR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1762-L40BXB 1762-L40BXBR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | Temperature, operating 0…55 °C (32…131 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Temperature, operating 0…55 °C (32…131 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Temperature, operating 0…55 °C (32…131 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Temperature, operating 0…55 °C (32…131 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Temperature, operating 0…55 °C (32…131 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Temperature, operating 0…55 °C (32…131 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                      | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Temperature, storage -40…+85 °C (-40…+185 °F) ambient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                      | Operating humidity 5…95% relative humidity (non-condensing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Operating humidity 5…95% relative humidity (non-condensing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Operating humidity 5…95% relative humidity (non-condensing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Operating humidity 5…95% relative humidity (non-condensing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Operating humidity 5…95% relative humidity (non-condensing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Operating humidity 5…95% relative humidity (non-condensing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Vibration            | Operating: 10…500 Hz, 5 G, 0.030 in. max. peak-to-peak, 2 hours each axis Relay Operation: 1.5 G                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operating: 10…500 Hz, 5 G, 0.030 in. max. peak-to-peak, 2 hours each axis Relay Operation: 1.5 G                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operating: 10…500 Hz, 5 G, 0.030 in. max. peak-to-peak, 2 hours each axis Relay Operation: 1.5 G                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operating: 10…500 Hz, 5 G, 0.030 in. max. peak-to-peak, 2 hours each axis Relay Operation: 1.5 G                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operating: 10…500 Hz, 5 G, 0.030 in. max. peak-to-peak, 2 hours each axis Relay Operation: 1.5 G                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Operating: 10…500 Hz, 5 G, 0.030 in. max. peak-to-peak, 2 hours each axis Relay Operation: 1.5 G                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Shock                | Operating: 30 G; 3 pulses each direction, each axis Relay Operation: 7 G Non-Operating: 50 G panel mounted (40 G DIN Rail mounted); 3 pulses each direction, each axis                                                                                                                                                                                                                                                                                                                                                                                            | Operating: 30 G; 3 pulses each direction, each axis Relay Operation: 7 G Non-Operating: 50 G panel mounted (40 G DIN Rail mounted); 3 pulses each direction, each axis                                                                                                                                                                                                                                                                                                                                                                                            | Operating: 30 G; 3 pulses each direction, each axis Relay Operation: 7 G Non-Operating: 50 G panel mounted (40 G DIN Rail mounted); 3 pulses each direction, each axis                                                                                                                                                                                                                                                                                                                                                                                            | Operating: 30 G; 3 pulses each direction, each axis Relay Operation: 7 G Non-Operating: 50 G panel mounted (40 G DIN Rail mounted); 3 pulses each direction, each axis                                                                                                                                                                                                                                                                                                                                                                                            | Operating: 30 G; 3 pulses each direction, each axis Relay Operation: 7 G Non-Operating: 50 G panel mounted (40 G DIN Rail mounted); 3 pulses each direction, each axis                                                                                                                                                                                                                                                                                                                                                                                            | Operating: 30 G; 3 pulses each direction, each axis Relay Operation: 7 G Non-Operating: 50 G panel mounted (40 G DIN Rail mounted); 3 pulses each direction, each axis                                                                                                                                                                                                                                                                                                                                                                                            |
| Agency certification | UL 508 C-UL under CSA C22.2 no. 142 Class I Div. 2, Groups A, B, C, D (UL 1604, C-UL under CSA C22.2 no. 213) CE/RCM compliant for all applicable directives                                                                                                                                                                                                                                                                                                                                                                                                      | UL 508 C-UL under CSA C22.2 no. 142 Class I Div. 2, Groups A, B, C, D (UL 1604, C-UL under CSA C22.2 no. 213) CE/RCM compliant for all applicable directives                                                                                                                                                                                                                                                                                                                                                                                                      | UL 508 C-UL under CSA C22.2 no. 142 Class I Div. 2, Groups A, B, C, D (UL 1604, C-UL under CSA C22.2 no. 213) CE/RCM compliant for all applicable directives                                                                                                                                                                                                                                                                                                                                                                                                      | UL 508 C-UL under CSA C22.2 no. 142 Class I Div. 2, Groups A, B, C, D (UL 1604, C-UL under CSA C22.2 no. 213) CE/RCM compliant for all applicable directives                                                                                                                                                                                                                                                                                                                                                                                                      | UL 508 C-UL under CSA C22.2 no. 142 Class I Div. 2, Groups A, B, C, D (UL 1604, C-UL under CSA C22.2 no. 213) CE/RCM compliant for all applicable directives                                                                                                                                                                                                                                                                                                                                                                                                      | UL 508 C-UL under CSA C22.2 no. 142 Class I Div. 2, Groups A, B, C, D (UL 1604, C-UL under CSA C22.2 no. 213) CE/RCM compliant for all applicable directives                                                                                                                                                                                                                                                                                                                                                                                                      |
| Electrical/EMC       | The controller has passed testing at the following levels: EN 61000-4-2: 4 kV contact, 8 kV air, 4 kV indirect EN 61000-4-3: 10V/m, 80 to 1000 MHz, 80% amplitude modulation, +900 MHz keyed carrier EN 61000-4-4: 2 kV, 5 kHz; communications cable: 1 kV, 5 kHz EN 61000-4-5: communications cable 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC Power Supply: 4 kV CM (common mode), 2 kV DM (differential mode) DC Power Supply: 500V CM (common mode), 500V DM (differential mode) EN 61000-4-6: 10V, communications cable 3V | The controller has passed testing at the following levels: EN 61000-4-2: 4 kV contact, 8 kV air, 4 kV indirect EN 61000-4-3: 10V/m, 80 to 1000 MHz, 80% amplitude modulation, +900 MHz keyed carrier EN 61000-4-4: 2 kV, 5 kHz; communications cable: 1 kV, 5 kHz EN 61000-4-5: communications cable 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC Power Supply: 4 kV CM (common mode), 2 kV DM (differential mode) DC Power Supply: 500V CM (common mode), 500V DM (differential mode) EN 61000-4-6: 10V, communications cable 3V | The controller has passed testing at the following levels: EN 61000-4-2: 4 kV contact, 8 kV air, 4 kV indirect EN 61000-4-3: 10V/m, 80 to 1000 MHz, 80% amplitude modulation, +900 MHz keyed carrier EN 61000-4-4: 2 kV, 5 kHz; communications cable: 1 kV, 5 kHz EN 61000-4-5: communications cable 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC Power Supply: 4 kV CM (common mode), 2 kV DM (differential mode) DC Power Supply: 500V CM (common mode), 500V DM (differential mode) EN 61000-4-6: 10V, communications cable 3V | The controller has passed testing at the following levels: EN 61000-4-2: 4 kV contact, 8 kV air, 4 kV indirect EN 61000-4-3: 10V/m, 80 to 1000 MHz, 80% amplitude modulation, +900 MHz keyed carrier EN 61000-4-4: 2 kV, 5 kHz; communications cable: 1 kV, 5 kHz EN 61000-4-5: communications cable 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC Power Supply: 4 kV CM (common mode), 2 kV DM (differential mode) DC Power Supply: 500V CM (common mode), 500V DM (differential mode) EN 61000-4-6: 10V, communications cable 3V | The controller has passed testing at the following levels: EN 61000-4-2: 4 kV contact, 8 kV air, 4 kV indirect EN 61000-4-3: 10V/m, 80 to 1000 MHz, 80% amplitude modulation, +900 MHz keyed carrier EN 61000-4-4: 2 kV, 5 kHz; communications cable: 1 kV, 5 kHz EN 61000-4-5: communications cable 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC Power Supply: 4 kV CM (common mode), 2 kV DM (differential mode) DC Power Supply: 500V CM (common mode), 500V DM (differential mode) EN 61000-4-6: 10V, communications cable 3V | The controller has passed testing at the following levels: EN 61000-4-2: 4 kV contact, 8 kV air, 4 kV indirect EN 61000-4-3: 10V/m, 80 to 1000 MHz, 80% amplitude modulation, +900 MHz keyed carrier EN 61000-4-4: 2 kV, 5 kHz; communications cable: 1 kV, 5 kHz EN 61000-4-5: communications cable 1 kV galvanic gun I/O: 2 kV CM (common mode), 1 kV DM (differential mode) AC Power Supply: 4 kV CM (common mode), 2 kV DM (differential mode) DC Power Supply: 500V CM (common mode), 500V DM (differential mode) EN 61000-4-6: 10V, communications cable 3V |

## Expansion I/O Specifications

## Discrete I/O Modules

General Specifications – Discrete I/O Modules

| Attribute Value                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions Height: 90 mm (3.54 in.), 110 mm (4.33 in.) (including mounting tabs) Width: 87 mm (3.43 in.) Depth: 40.4 mm (1.59 in.) |
| Enclosure type rating None (open-style)                                                                                            |

## Input Specifications – 1762-IA8, 1762-IQ8, 1762-IQ16, 1762-IQ32T, 1762-IQ8OW6

|                                                |                                                                                         |                                  |                                  | Attribute 1762-IA8 1762-IQ8 1762-IQ16 1762-IQ32T 1762-IQ8OW6   |
|------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------|----------------------------------|----------------------------------------------------------------|
| Shipping weight, approx. (with carton)         | 209 g (0.46 lbs.) 200 g (0.44 lbs.) 230 g (0.51 lbs.) 200g (0.44 lbs.) 280g (0.62 lbs.) |                                  |                                  |                                                                |
| Voltage category 100/120V AC                   | 24V DC (sinking/ sourcing)( )(1)                                                        | 24V DC (sinking/ sourcing)( )(1) | 24V DC (sinking/ sourcing)( )(1) | 24V DC (sinking/sourcing)( )(1)                                |
| Operating voltage range 79…132V AC at 47…63 Hz | 10…30V DC at 30 °C (86 °F) 10…26.4V DC at 55 °C (131 °F)                                | 10…30V DC 10…26.4V DC(2)(3)      | 10…30V DC (24 points) at °° 30 °C (86 °F) 10…26.4V DC (23 points) at °° 60 °C (140 °F)                                  | 10…30V DC at 30 °C (86 °F) 10…26.4V DC at 65 °C (149 °F)       |
| Number of inputs 8 8 16 32 8                   |                                                                                         |                                  |                                  |                                                                |
|                                                | Bus current draw, max 50 mA at 5V DC (0.25 W) 50 mA at 5V DC (0.25 W)                   | 70 mA at 5V DC (0.35 W) (3)      | 170 mA at 5V DC 0 mA at 24V DC   | 110 mA at 5V DC 80 mA at 24V DC                                |

## Input Specifications – 1762-IA8, 1762-IQ8, 1762-IQ16, 1762-IQ32T, 1762-IQ8OW6 (Continued)

|                                                                                                                                                     |                                                                                                                                                      |                                                                                                                                                    |                                                                                                                                                                                       | Attribute 1762-IA8 1762-IQ8 1762-IQ16 1762-IQ32T 1762-IQ8OW6                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Heat dissipation, max 2.0 W 3.7 W                                                                                                                   |                                                                                                                                                      | 4.3 W at 26.4V DC 5.4 W at 30V DC(3)                                                                                                               | 5.4 W at 26.4V DC 6.8 W at 30V DC                                                                                                                                                     | 5.0 W at 30V DC 4.4 W at 26.4V DC  (The Watts per point, plus the min W, with all points energized)                                                |
| On delay: 20.0 ms Off delay: 20.0 ms                                                                                                                | On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                   | On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                 | Signal delay, max  On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                                 | On delay: 8.0 ms Off delay: 8.0 ms                                                                                                                 |
| Off-state voltage, max 20V AC 5V DC 5V DC 5V DC 5V DC                                                                                               |                                                                                                                                                      |                                                                                                                                                    |                                                                                                                                                                                       |                                                                                                                                                    |
|                                                                                                                                                     |                                                                                                                                                      |                                                                                                                                                    | Off-state current, max 2.5 mA 1.5 mA 1.5 mA 1.0 mA 1.5 mA                                                                                                                             |                                                                                                                                                    |
| On-state voltage, min 79V AC (min) 132V AC (max) 10V DC 10V DC 10V DC 10V DC                                                                        |                                                                                                                                                      |                                                                                                                                                    |                                                                                                                                                                                       |                                                                                                                                                    |
| 5.0 mA min at 79V AC 47 Hz 12.0 mA nom. at 120V AC 60 Hz 16.0 mA max at 132V AC 63 Hz                                                               | 2.0 mA min at 10V DC 8.0 mA nom. at 24V DC 12.0 mA max at 30V DC                                                                                     | 2.0 mA min at 10V DC 8.0 mA nom. at 24V DC 12.0 mA max at 30V DC                                                                                   | On-state current 1.6 mA min at 10V DC 2.0 mA min at 15V DC 5.7 mA max at 26.4V DC 6.5 mA max at 30.0V DC                                                                              | 10 mA at 5V DC                                                                                                                                     |
|                                                                                                                                                     | Inrush current, max 250 mA Not applicable Not applicable Not applicable 250 mA                                                                       |                                                                                                                                                    |                                                                                                                                                                                       |                                                                                                                                                    |
| 12 kΩ at 50 Hz 10 kΩ at 60 Hz                                                                                                                       | 3 kΩ                                                                                                                                                 | 3 kΩ                                                                                                                                               | Nominal impedance  4.7 kΩ                                                                                                                                                             | 3 kΩ                                                                                                                                               |
| IEC input compatibility Type 1+ Type 1+ Type 1+ Type 1 Type 1+                                                                                      |                                                                                                                                                      |                                                                                                                                                    |                                                                                                                                                                                       |                                                                                                                                                    |
| Group 1: inputs 0…7 (internally connected commons)                                                                                                  | Group 1: inputs 0…7 (internally connected commons)                                                                                                   | Group 1: inputs 0…7; Group 2: inputs 8…15                                                                                                          | Isolated groups  Group 1: Inputs 0…7; Group 2: Inputs 8…15; Group 3: Inputs 16…23; Group 4: Inputs 24…31                                                                              | Group 1: inputs 0…3; Group 2: inputs 4…7                                                                                                           |
| Verified by one of the following dielectric tests: 1517V AC for 1 s or 2145V DC for 1 s 132V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V ACAC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Input group to backplane isolation Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Vendor ID code 1                                                                                                                                    | Vendor ID code 1                                                                                                                                     | Vendor ID code 1                                                                                                                                   | Vendor ID code 1                                                                                                                                                                      | Vendor ID code 1                                                                                                                                   |
| Product type code 7                                                                                                                                 | Product type code 7                                                                                                                                  | Product type code 7                                                                                                                                | Product type code 7                                                                                                                                                                   | Product type code 7                                                                                                                                |
|                                                                                                                                                     |                                                                                                                                                      |                                                                                                                                                    | Product code 114 96 97 99 98                                                                                                                                                          |                                                                                                                                                    |

## Output Specifications – 1762-OA8, 1762-OB8, 1762-OB16, 1762-OB32T, 1762-OV32T

|                                                                                            |                                                                                                        |                                                    |                                                                                      | Attribute 1762-OA8 1762-OB8 1762-OB16 1762-OB32T 1762-OV32T   |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------|
| Shipping weight, approx. (with carton)                                                     |                                                                                                        |                                                    | 215 g (7.58 oz.) 210 g (7.41 oz.) 235 g (8.29 oz.) 200 g (7.05 oz.) 200 g (7.05 oz.) |                                                               |
| Voltage category 100…240V AC 24V DC 24V DC 24V DC sourcing 24V DC sinking                  |                                                                                                        |                                                    |                                                                                      |                                                               |
|                                                                                            | Operating voltage range 85…265V AC at 47…63 Hz 20.4…26.4V DC 20.4…26.4V DC 10.2…26.4V DC 10.2…26.4V DC |                                                    |                                                                                      |                                                               |
| Number of outputs 8 8 16 32 32                                                             |                                                                                                        |                                                    |                                                                                      |                                                               |
| Bus current draw, max                                                                      | 115 mA at 5V DC (0.575 W)                                                                              | 115 mA at 5V DC (0.575 W) 175 mA at 5V DC (0.88 W) | 175 mA at 5V DC 0 mA at 24V DC                                                       | 175 mA at 5V DC 0 mA at 24V DC                                |
| Heat dissipation, max 2.9 W 1.61 W                                                         |                                                                                                        |                                                    | 2.9 W at 30 °C (86 °F) 2.1 W at 55 °C (131 °F)                                       | 3.4 W at 26.4 DC 2.7 W at 26.4V DC                            |
| Signal delay, max – resistive load                                                         | On delay: 1/2 cycle Off delay: 1/2 cycle                                                               | On delay: 0.1 ms Off delay: 1.0 ms                 | On delay: 0.1 ms Off delay: 1.0 ms On delay: 0.5 ms Off delay: 4.0 ms                | On delay: 0.5 ms Off delay: 4.0 ms                            |
| Off-state leakage current, max                                                             | 2 mA at 132V 2.5 mA at 265V                                                                            |                                                    |                                                                                      | 1.0 mA 1.0 mA 0.1 mA at 26.4V DC 0.1 mA at 26.4V DC           |
| On-state current, min 10 mA 1.0 mA 1.0 mA 1.0 mA 1.0 mA                                    |                                                                                                        |                                                    |                                                                                      |                                                               |
| On-state voltage drop, max 1.5V at 0.5 A 1.0V DC 1.0V DC 0.3V DC at 0.5 A 0.3V DC at 0.5 A |                                                                                                        |                                                    |                                                                                      |                                                               |
| Continuous current per point, max                                                          | 0.25 A at 55 °C (131 °F) 0.5 A at 30 °C (86 °F)                                                        | 0.5 A at 55 °C (131 °F) 1.0 A at 30 °C (86 °F)     | 0.5 A at 55 °C (131 °F) 1.0 A at 30 °C (86 °F)                                       | 0.5 A at 60 °C (140 °F) 0.5 A at 60 °C (140 °F)               |
| Continuous current per common, max                                                         | 1.0 A at 55 °C (131 °F) 2.0 A at 30 °C (86 °F)                                                         | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)     | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                       | 2.0 A at 60 °C (140 °F) 2.0 A at 60 °C (140 °F)               |

## Output Specifications – 1762-OA8, 1762-OB8, 1762-OB16, 1762-OB32T, 1762-OV32T (Continued)

|                                        |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    | Attribute 1762-OA8 1762-OB8 1762-OB16 1762-OB32T 1762-OV32T                                                                                        |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Continuous current per module, max     | 2.0 A at 55 °C (131 °F) 4.0 A at 30 °C (86 °F)                                                                                                      | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                     | 4.0 A at 55 °C (131 °F) 8.0 A at 30 °C (86 °F)                                                                                                     |                                                                                                                                                    | 4.0 A at 60 °C (140 °F) 4.0 A at 60 °C (140 °F)                                                                                                    |
| Surge current, max                     | 5.0 A (Repeatability is once every 2 s for a duration of 25 ms.                                                                                     | 2.0 A (Repeatability is once °° py  every 2 s at 55 °C (131 °F), ° y  once every second at 30 °C ° y  (86 °F) for a duration of 10 ms.)                                                                                                                                                    | 2.0 A (Repeatability is once °° py  every 2 s at 55 °C (131 °F), ° y  once every second at 30 °C ° y  (86 °F) for a duration of 10 ms.)                                                                                                                                                    | 2.0 A (Repeatability is once °° py  every 2 s at 60 °C (140 °F) for 10 ms)                                                                                                                                                    | 2.0 A (Repeatability is once °° py  every 2 s at 60 °C (140 °F) for 10 ms)                                                                                                                                                    |
| Isolated groups                        | Group 1: Outputs 0…3 Group 2: Outputs 4…7                                                                                                           |                                                                                                                                                    | Group 1: Outputs 0…7 Group 1: Outputs 0…15                                                                                                         | Group 1: Outputs 0…15 Group 2: Outputs 16…31 (internally connected to common)                                                                      | Group 1: Outputs 0…15 Group 2: Outputs 16…31 (internally connected to common)                                                                      |
| Output group to backplane isolation    | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 1 s or 1697V DC for 1 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Output group to output group isolation | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Not applicable                                                                                                                                     | Not applicable                                                                                                                                     | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1200V AC for 2 s or 1697V DC for 2 s 75V DC working voltage (IEC Class 2 reinforced insulation) |
| Vendor ID code 1                       |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| Product type code 7                    |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    |
| Product code 119 101 103               |                                                                                                                                                     |                                                                                                                                                    |                                                                                                                                                    |                                                                                                                                                    | 100 102                                                                                                                                            |

## Output Specifications – 1762-OW8, 1762-OW16, 1762-OX6I, 1762-IQ8OW6

|                                                       |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     | Attribute 1762-OW8 1762-OW16 1762-OX6I 1762-IQ8OW6                                                                                                  |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Shipping weight, approx. (with carton)                |                                                                                                                                                     | 228 g (0.50 lbs.) 285 g (0.63 lbs.) 220 g (0.485 lbs) 280 g (0.62 lbs.)                                                                             |                                                                                                                                                     |                                                                                                                                                     |
|                                                       |                                                                                                                                                     | Voltage category AC/DC normally open relay AC/DC normally open relay AC/DC Type C Relay AC/DC normally open relay                                   |                                                                                                                                                     |                                                                                                                                                     |
| Operating voltage range                               | 5…265V AC 5…125V DC                                                                                                                                 | 5…265V AC 5…125V DC                                                                                                                                 | 5…265V AC 5…125V DC                                                                                                                                 | 5…265V AC 5…125V DC                                                                                                                                 |
| Number of outputs 8 16 6 6                            |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| Bus current draw, max                                 | 80 mA at 5V DC (0.40 W) 90 mA at 24V DC (2.16 W)                                                                                                    | 140 mA at 5V DC (0.70 W)(1) 180 mA at 24V DC (4.32 W) (1)                                                                                           | 110 mA at 5V DC (0.55 W) 110 mA at 24V DC (2.64 W)                                                                                                  | 110 mA at 5V DC 80 mA at 24V DC                                                                                                                     |
| Heat dissipation, max 2.9 W                           |                                                                                                                                                     | 6.1 W(1)                                                                                                                                            | 2.8 W                                                                                                                                               | 5.0 W at 30V DC 4.4 W at 26.4V DC (The Watts per point, plus the min W, with all points energized)                                                  |
| Signal delay, max – resistive load                    | On Delay: 10 ms Off Delay: 10 ms                                                                                                                    | On Delay: 10 ms Off Delay: 10 ms                                                                                                                    | On Delay: 10 ms (max) 6 ms (typical) Off Delay: 20 ms (max) 12 ms (typical)                                                                         | On-delay: 10 ms (max) Off-delay: 10 ms (max)                                                                                                        |
| Off-state leakage, max 0 mA 0 mA 0 mA 0 mA            |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| On-state current, min 10 mA 10 mA 100 mA 10 mA        |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| On-state voltage drop, max Not Applicable             |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |                                                                                                                                                     |
| Continuous current per point, max 2.5 A. See Table 14 |                                                                                                                                                     |                                                                                                                                                     | 7 A See Table 15 .                                                                                                                                  | 2.5 A See Table 14 .                                                                                                                                |
| Continuous current per common, max                    |                                                                                                                                                     | 8 A 8 A                                                                                                                                             | 7 A See Table 15 .                                                                                                                                  | 8 A                                                                                                                                                 |
| Continuous current per module, max 16 A 16 A          |                                                                                                                                                     |                                                                                                                                                     | 30 A See Table 16 .                                                                                                                                 | 8 A                                                                                                                                                 |
|                                                       | Surge current, max See Table 14. See Table 15. See Table 14                                                                                         | Surge current, max See Table 14. See Table 15. See Table 14                                                                                         |                                                                                                                                                     | .                                                                                                                                                   |
| Isolated groups                                       | Group 1: Outputs 0…3 Group 2: Outputs 4…7                                                                                                           | Group 1: Outputs 0…7 Group 2: Outputs 8…15                                                                                                          | All 6 Outputs Individually Isolated.                                                                                                                | Group 3: Outputs 0…5                                                                                                                                |
| Output group to backplane isolation                   | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s 265V AC working voltage (IEC Class 2 reinforced insulation) |

## Output Specifications – 1762-OW8, 1762-OW16, 1762-OX6I, 1762-IQ8OW6 (Continued)

|                                        |                                                                                                        | Attribute 1762-OW8 1762-OW16 1762-OX6I 1762-IQ8OW6                                      |
|----------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Output group to output group isolation | 265V AC working voltage (basic insulation) 150V AC working voltage (IEC Class 2 reinforced insulation) | Verified by one of the following dielectric tests: 1836V AC for 1 s or 2596V DC for 1 s |
| Vendor ID code 1                       |                                                                                                        |                                                                                         |
| Product type code 7                    |                                                                                                        |                                                                                         |
| Product code 120                       | 121                                                                                                    | 124 98                                                                                  |

## Table 14 - Relay Contact Ratings – 1762-OW8, 1762-OW16, and 1762-IQ8OW6

|               | Maximum Volts Amperes Continuous   | Amperes Voltamperes   | Amperes Voltamperes       |
|---------------|------------------------------------|-----------------------|---------------------------|
|               | Maximum Volts Amperes Continuous   |                       | Make Break Make Break     |
| 240V AC       | 2.5 A(1)                           |                       | 7.5 A 0.75 A 1800VA 180VA |
| 120V AC       | 2.5 A(1)                           |                       | 15 A 1.5 A 1800VA 180VA   |
| 125V DC 1.0 A |                                    | 0.22 A(2)             |                           |
| 24V DC 2.0 A  |                                    | 1.2 A(2)              | 28VA                      |

Table 15 - Relay Contact Ratings – 1762-OX6I

| Maximum Volts            | Continuous Amps per Point (Max)(1)   | Amperes (2)   | Amperes (2)           | Voltamperes   | Voltamperes   |
|--------------------------|--------------------------------------|---------------|-----------------------|---------------|---------------|
|                          |                                      |               | Make Break Make Break |               |               |
| 240V AC 5.0 A 15 A 1.5 A |                                      |               |                       | 3600VA 360VA  |               |
| 120V AC                  | 7.0 A(3)                             |               | 30 A 3.0 A            | 3600VA 360VA  |               |
| 125V DC 2.5 A 0.4 A      |                                      |               |                       | 50VA(4)       |               |
| 24V DC                   | 7.0 A(3)                             | 7.0 A         |                       | 168VA(4)      |               |

Table 16 - Module Load Ratings – 1762-OX6I

|                | Volts (Max) Controlled Load (Current) per Module (Max)   |
|----------------|----------------------------------------------------------|
| 240V AC 6 A    |                                                          |
| 120V AC        | 12 A(1)                                                  |
| 125V DC 11.5 A |                                                          |
| 24V DC         | 30 A(2)                                                  |

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
| ESD immunity                                     | EC 61000-4-2: 4 kV contact discharges 8 kV air discharges                                                                                                                                                                     |
| Radiated RF immunity                             | IEC 61000-4-3: 10V/m with 1 kHz sine wave 80% AM from 80…6000 MHz                                                                                                                                                             |
| EFT/B immunity                                   | IEC 61000-4-4: ±2 kV @ 5 kHz on power ports ±2 kV @ 5 kHz on signal ports ±1 kV @ 5 kHz on communication ports                                                                                                                |
| Surge transient immunity                         | IEC 61000-4-5: ±2 kV line-line(DM) and ±4 kV line-earth(CM) on AC power ports ±500V line-line(DM) and ±1 kV line-earth(CM) on signal ports ±1 kV line-earth(CM) on shielded ports ±2 kV line-earth(CM) on communication ports |
| Conducted RF immunity                            | IEC 61000-4-6: 10V rms with 1 kHz sine wave 80% AM from 150 kHz…80 MHz                                                                                                                                                        |

Figure 74 - Relays Used vs. Maximum Current per Relay (24V DC) 1762-OX6I

<!-- image -->

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us                                      | UL Listed Industrial Control Equipment, certified for U.S. and Canada. See UL File E322657. UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for U.S. and Canada. See UL File E334470.                                                                                                                                                                                                                  |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61326-1; Meas./Control/Lab., Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) European Union 2014/35/EU LVD, compliant with: EN 61131-2; Programmable Controllers (Clause 11) European Union 2011/62/EU RoHS, compliant with: EN IEC 63000; Technical Documentation |
| RCM                                          | Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emmissions                                                                                                                                                                                                                                                                                                                                                 |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                                                                                                                                                             |
| UKCA                                         | 2016 No. 1091 – Electromagnetic Compatibility Regulations 2016 No. 1101 – Electrical Equipment (Safety) Regulations 2012 No. 3032 – Restriction of the Use of Certain Hazardous Substances in Electrical and Electronic Equipment Regulations                                                                                                                                                                                           |

## Analog Modules

## Common Specifications – 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4, 1762-OF4

|                   | Attribute 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4, 1762-OF4                                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions HxWxD  | 90 x 87 x 40 mm Height including mounting tabs is 110 mm (3.54 x 3.43 x 1.58 in.) Height including mounting tabs is 4.33 in.                                                           |
|                   | Module power status indicator On: Indicates power is applied                                                                                                                           |
| Recommended cable | Belden 8761 (shielded) For 1762-IT4, shielded thermocouple extension wire for the specific type of thermocouple you are using. Follow the thermocouple manufacturer’s recommendations. |

## General Specifications – 1762-IF2OF2, 1762-IF4, 1762-OF4, 1762-IR4, 1762-IT4

|                                            | Attribute 1762-IF2OF2 1762-IF4 1762-OF4 1762-IR4 1762-IT4                                                                                        |                                                                                                                                                  |                                                                                                                    |                                                                                                                                                          |                                                                        |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Shipping weight, approx. (with carton)     |                                                                                                                                                  | 240 g (0.53 lbs.) 235 g (0.517 lbs.) 260 g (0.57 lbs.) 220 g (0.53 lbs.)                                                                         |                                                                                                                    |                                                                                                                                                          |                                                                        |
| Bus current draw, max                      | 40 mA at 5V DC 105 mA at 24V DC                                                                                                                  | 40 mA at 5V DC 50 mA at 24V DC                                                                                                                   | 40 mA at 5V DC 165 mA at 24V DC                                                                                    | 40 mA at 5V DC 50 mA at 24V DC                                                                                                                           | 40 mA at 5V DC 50 mA at 24V DC                                         |
| Analog normal operating range              | Voltage: 0…10V DC Current: 4…20 mA                                                                                                               | Voltage: -10…+10V DC Current: 4…20 mA                                                                                                            | Voltage 0…10V DC Current: 4…20 mA                                                                                  |                                                                                                                                                          | NA NA                                                                  |
| Full scale(1) analog ranges                | Voltage: 0…10.5V DC Current: 0…21 mA                                                                                                             | Voltage: -10.5…+10.5V DC Current: -21…+21 mA                                                                                                     | Voltage: 0…10.5V DC Current: 0…21 mA                                                                               |                                                                                                                                                          | NA NA                                                                  |
|                                            | Resolution 12 bits (unipolar)                                                                                                                    | 15 bits (bipolar) (2)                                                                                                                            | 12 bits (unipolar)                                                                                                 | Input filter and configuration dependent                                                                                                                 | 15 bits plus sign                                                      |
| Repeatability (3)                          | ±0.12% (2)                                                                                                                                       | ±0.12% (2)                                                                                                                                       | ±0.12% (2)                                                                                                         | ±0.1 °C (±0.18 °F) for Ni and NiFe ±0.2 °C (±0.36 °F)…±0.2 °C (±0.36 °F) for other RTD inputs ±0.04 Ω for 150 Ω resistances ±0.2 Ω for other resistances | See Table 17                                                           |
| Input and output group to system isolation | 30V AC/30V DC rated working voltage (4) (N.E.C. Class 2 required) (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC rated working voltage (4) (N.E.C. Class 2 required) (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC rated working voltage (IEC Class 2 reinforced insulation) type test: 500V AC or 707V DC for 1 minute | 30V AC/30V DC working voltage type test: 500V AC or 707V DC for 1 minute                                                                                 | 30V AC/30V DC working voltage qualification test: 720V DC for 1 minute |

## General Specifications – 1762-IF2OF2, 1762-IF4, 1762-OF4, 1762-IR4, 1762-IT4 (Continued)

|                                  | Attribute 1762-IF2OF2 1762-IF4 1762-OF4 1762-IR4 1762-IT4   |
|----------------------------------|-------------------------------------------------------------|
| Vendor ID code 1 1 1 1 1         |                                                             |
| Product type code 10 10 10 10 10 |                                                             |
| Product code 75 67 66 65 64      |                                                             |

## Input Specifications – 1762-IF2OF2, 1762-IF4, 1762-IR4, 1762-IT4

|                                              | Attribute 1762-IF2OF2 1762-IF4 1762-IR4 1762-IT4                                  |                                                                                              |                                                                                   |                                                                                   |
|----------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
|                                              | Number of inputs 2 differential (unipolar) 4 differential (bipolar) 4             |                                                                                              |                                                                                   | 4 input channels plus 1 CJC sensor                                                |
| Update time (typical) 2.5 ms                 |                                                                                   | 130, 250, 290, 450, 530 ms (selectable)                                                      | Input filter and configuration dependent                                          | NA                                                                                |
|                                              |                                                                                   | A/D converter type Successive approximation Successive approximation Delta-Sigma Delta-Sigma |                                                                                   |                                                                                   |
| Common mode voltage range (1)                |                                                                                   | ±27V ±27V NA ±10V                                                                            |                                                                                   |                                                                                   |
| Common mode rejection (2)                    |                                                                                   | > 55 dB at 50 Hz and 60 Hz > 55 dB at 50 Hz and 60 Hz                                        | >110 dB at 50 Hz (with 10 Hz or 60 Hz filter)                                     | >110 dB at 50 Hz (with 10 Hz or 60 Hz filter)                                     |
| Non-linearity (in percent full scale)        | ±0.12% (3)                                                                        | ±0.12% (2)                                                                                   | ±0.05% NA                                                                         |                                                                                   |
| Typical overall accuracy (4)                 | ±0.55% full scale at - 20…+65 °C(2) ±0.3% full scale at 25 °C                     | ±0.32% full scale at -20…+65 °C (2) ±0.24% full scale at 25 °C                               | ±0.5 °C ( °F) for Pt 385 NA                                                       |                                                                                   |
| Input impedance                              | Voltage Terminal: 200 kΩ Current Terminal: 250 Ω                                  | Voltage Terminal: 200 kΩ Current Terminal: 275 Ω                                             | >10 MΩ                                                                            | >10 MΩ                                                                            |
| Current input protection ±32 mA ±32 mA NA NA |                                                                                   |                                                                                              |                                                                                   |                                                                                   |
| Voltage input protection ±30V ±30V NA NA     |                                                                                   |                                                                                              |                                                                                   |                                                                                   |
| Channel diagnostics                          | Over or under range or open circuit condition by bit reporting for analog inputs. | Over or under range or open circuit condition by bit reporting for analog inputs.            | Over or under range or open circuit condition by bit reporting for analog inputs. | Over or under range or open circuit condition by bit reporting for analog inputs. |

## Input Specifications 1762-IR4

|                             | Attribute 1762-IR4                                                                                                                                                                                                                                                              |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input types                 | 100 Ω Platinum 385 200 Ω Platinum 385 500 Ω Platinum 385 1000 Ω Platinum 385 100 Ω Platinum 3916 200 Ω Platinum 3916 500 Ω Platinum 3916 1000 Ω Platinum 3916 10 Ω Copper 426 120 Ω Nickel 672 120 Ω Nickel 618 604 Ω Nickel-Iron 518 0...150 Ω 0...500 Ω 0...1000 Ω 0...3000 Ω |
|                             | Heat dissipation 1.5 Total Watts (The Watts per point, plus the minimum Watts, with all points enabled)                                                                                                                                                                         |
| Normal mode rejection ratio | 70 dB minimum at 50 Hz with the 10 Hz or 50 Hz filter selected 70 dB minimum at 60 Hz with the 10 Hz or 60 Hz filter selected                                                                                                                                                   |

## Input Specifications 1762-IR4 (Continued)

|                                                                        | Attribute 1762-IR4                                                                                                                                                                                                       |                                                                                                |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Typical accuracy (Auto-calibration enabled) °° ypy  at 25 °C (77 °F) ambient with module operating temperature at 25 °C (77 °F)( )(1)                                                                        | ±0.5 °C ( °F) for Pt 385 ±0.4 °C ( °F) for Pt 3916 ±0.2 °C ( °F) for Ni ±0.3 °C ( °F) for NiFe ±0.6 °C ( °F) for Cu                                                                                                      | ±0.15 Ω for 150 Ω range ±0.5 Ω for 500 Ω range ±1.0 Ω for 1000 Ω range ±1.5 Ω for 3000 Ω range |
| Typical accuracy (Auto-calibration enabled) at 0…55 ° C (32…131 °F)(1) | ±0.9 °C ( °F) for Pt 385 ±0.8 °C ( °F) for Pt 3916 ±0.4 °C ( °F) for Ni ±0.5 °C ( °F) for NiFe ±1.1 °C ( °F) for Cu                                                                                                      | ±0.25 Ω for 150 Ω range ±0.8 Ω for 500 Ω range ±1.5 Ω for 1000 Ω range ±2.5 Ω for 3000 Ω range |
| Accuracy drift at 0…55 ° C (32…131 °F)                                 | ±0.026 °C/°C (0.026 °F/°F) for Pt 385 ±0.023 °C/°C (0.023 °F/°F) for Pt 3916 ±0.012 °C/°C (0.012 °F/°F) for Ni ±0.015 °C/°C (0.015 °F/°F) for NiFe ±0.032 °C/°C (0.032 °F/°F) for Cu                                     | ±0.007 Ω/ °C (0.012 Ω/ °F) for 150 Ω range °° g ±0.023 Ω/ °C (0.041 Ω/ °F) for 500 Ω range °° g ±0.043 Ω/ °C (0.077 Ω/ °F) for 1000 Ω range °° g ±0.07 Ω/ °C (0.130 Ω/ °F) for 3000 Ω range                                                                                                |
|                                                                        | Excitation current source 0.5 mA and 1.0 mA selectable per channel                                                                                                                                                       |                                                                                                |
| Open-circuit detection time (2)                                        | 6…1212 ms                                                                                                                                                                                                                |                                                                                                |
| Input channel configuration                                            | Via configuration software screen or the user program (by writing a unique bit pattern into the module’s configuration file). See your controller’s user manual to determine if user program configuration is supported. |                                                                                                |
| Calibration                                                            | The module performs auto-calibration on channel enable and on a configuration change between channels. You can also program the module to calibrate every 5 minutes.                                                     |                                                                                                |
| Maximum overload at input terminals ±35V DC continuous                 |                                                                                                                                                                                                                          |                                                                                                |
|                                                                        | Cable impedance, max 25 Ω − Operating with >25 Ω reduces accuracy.                                                                                                                                                       |                                                                                                |
| Channel to channel isolation ±10V DC                                   |                                                                                                                                                                                                                          |                                                                                                |

## Input Specifications 1762-IT4

| Attribute Value                     |                                                                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|                                     | Heat dissipation 1.5 Total Watts (The Watts per point, plus the minimum Watts, with all points energized)                                           |
|                                     | Response speed per channel Input filter and configuration dependent                                                                                 |
| Rated working voltage (1)           | 30V AC/30V DC                                                                                                                                       |
| Normal mode rejection ratio         | 85 dB (minimum) at 50 Hz (with 10 Hz or 50 Hz filter) 85 dB (minimum) at 60 Hz (with 10 Hz or 60 Hz filter)                                         |
|                                     | Cable impedance, max 25 Ω (for specified accuracy)                                                                                                  |
| Open-circuit detection time         | 7 ms…1.515 s(2)                                                                                                                                     |
| Calibration                         | The module performs auto-calibration upon power-up and whenever a channel is enabled. You can also program the module to calibrate every 5 minutes. |
|                                     | CJC accuracy ±1.3 °C (±2.34 °F)                                                                                                                     |
| Maximum overload at input terminals | ±35V DC continuous(3)                                                                                                                               |
| Input channel configuration         | Via configuration software screen or the user program (by writing a unique bit pattern into the module’s configuration file)                        |

Table 17 - 1762-IT4 Repeatability at 25°C (77°F) (1)(2)

| Input Type Repeatability for 10 Hz Filter                         |
|-------------------------------------------------------------------|
| Thermocouple J ±0.1 °C [±0.18 °F]                                 |
| Thermocouple N (-110…+1300 °C [-166…+2372 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple N (-210…+110 °C [-346…+166 °F]) ±0.25 °C [±0.45 °F]  |
| Thermocouple T (-170…+400 °C [-274…+752 °F]) ±0.1 °C [±0.18 °F]   |
| Thermocouple T (-270…+170 °C [-454…+274 °F]) ±1.5 °C [±2.7 °F]    |

## Table 18 - 1762-IT4 Accuracy

| Input Type (1)                                                                                                   | With Autocalibration Enabled Without Autocalibration                             |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
|                                                                                                                  | Maximum Temperature Drift(2)                                                     |
| @ 25 °C (77 °F) Ambient @ 0…60 °C (32…140 °F) Ambient                                                            | @ 0…60 °C (32…140 °F) Ambient                                                    |
| Thermocouple J (-210…+1200 °C [-346…+2192 °F]) ±0.6 °C [±1.1 °F] ±0.9 °C [±1.7 °F] ±0.0218 °C/°C [±0.0218 °F/°F] |                                                                                  |
| Thermocouple N (-200…+1300 °C [-328…+2372 °F]) ±1 °C [±1.8 °F] ±1.5 °C [±2.7 °F] ±0.0367 °C/°C [±0.0367 °F/°F]   |                                                                                  |
| Thermocouple N (-210…-200 °C [-346…-328 °F]) ±1.2 °C [±2.2 °F] ±1.8 °C [±3.3 °F] ±0.0424 °C/°C [±0.0424 °F/°F]   |                                                                                  |
| Thermocouple T (-230…+400 °C [-382…+752 °F]) ±1 °C [±1.8 °F] ±1.5 °C [±2.7 °F] ±0.0349 °C/°C [±0.0349 °F/°F]     |                                                                                  |
| Thermocouple T (-270…-230 °C [-454…-382 °F]) ±5.4 °C [±9.8 °F] ±7.0 °C [±12.6 °F] ±0.3500 °C/°C [±0.3500 °F/°F]  |                                                                                  |
| Thermocouple K (-230…+1370 °C [-382…+2498 °F]) ±1 °C [±1.8 °F] ±1.5 °C [±2.7 °F] ±0.4995 °C/°C [±0.4995 °F/°F]   |                                                                                  |
| Thermocouple K (-270…-225°C [-454…-373°F]) ±7.5°C [±13.5°F] ±10°C [±18 °F] ±0.0378°C/°C [±0.0378°F/°F]           |                                                                                  |
| Thermocouple E (-210…+1000°C [-346…+1832°F]) ±0.5°C [±0.9°F] ±0.8°C [±1.5 °F] ±0.0199°C/°C [±0.0199°F/°F]        |                                                                                  |
| Thermocouple E (-270…-210 °C [-454…-346 °F]) ±4.2 °C [±7.6 °F] ±6.3 °C [±11.4 °F] ±0.2698 °C/°C [±0.2698 °F/°F]  |                                                                                  |
|                                                                                                                  | Thermocouple R ±1.7 °C [±3.1 °F] ±2.6 °C [±4.7 °F] ±0.0613 °C/°C [±0.0613 °F/°F] |
|                                                                                                                  | Thermocouple S ±1.7 °C [±3.1 °F] ±2.6 °C [±4.7 °F] ±0.0600 °C/°C [±0.0600 °F/°F] |
|                                                                                                                  | Thermocouple C ±1.8 °C [±3.3 °F] ±3.5 °C [±6.3 °F] ±0.0899 °C/°C [±0.0899 °F/°F] |
|                                                                                                                  | Thermocouple B ±3.0 °C [±5.4 °F] ±4.5 °C [±8.1 °F] ±0.1009 °C/°C [±0.1009 °F/°F] |
|                                                                                                                  | ±50 mV ±15 µV ±25 µV ±0.44 µV/°C [±0.80 µV/°F]                                   |
| ±100 mV ±20 µV ±30 µV                                                                                            | ±0.69 µV/°C [±01.25  µV/°F]                                                      |

<!-- image -->

Table 19 - Output Specifications – 1762-IF2OF2, 1762-OF4

| Specification 1762-IF2OF2 1762-OF4                         |                                                                                                                                                                    |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Number of outputs 2 single-ended (unipolar)                | 4 single-ended (unipolar)(2)                                                                                                                                       |
| Update time (typical) 4.5 ms 2.5 ms                        |                                                                                                                                                                    |
|                                                            | D/A converter type Resistor string R-2R ladder voltage switching                                                                                                   |
|                                                            | Resistive load on current output 0…500 Ω (includes wire resistance) 0…500 Ω (includes wire resistance)                                                             |
| Load range on voltage output > 1 kΩ                        | > 1 kΩ                                                                                                                                                             |
| Reactive load, current output < 0.1 mH < 0.1 mH            |                                                                                                                                                                    |
| Reactive load, voltage output < 1 µF < 1 µF                |                                                                                                                                                                    |
| Typical overall accuracy (1)                               | ±1.17% full scale @ -20…+65 °C (-4…+149 °F)( )(2) ±0.5% full scale @ 25 °C (77 °F) ±1.17% full scale @ -20…+65 °C (-4…+149 °F)(2) ±0.5% full scale @ 25 °C (77 °F) |
| Output ripple range 0 to 500 Hz (referred to output range) | < ±0.1% < ±0.1%                                                                                                                                                    |

For more detailed 1762-IT4 accuracy information, see the MicroLogix 1200 Thermocouple/mV Input Module User Manual, publication 1762-UM002 .

Table 17 - 1762-IT4 Repeatability at 25°C (77°F) (1)(2) (Continued)

| Input Type Repeatability for 10 Hz Filter                         |
|-------------------------------------------------------------------|
| Thermocouple K (-270…+1370 °C [-454…+2498 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple K (-270…+170 °C [-454…+274 °F]) ±2.0 °C [±3.6 °F]    |
| Thermocouple E (-220…+1000 °C [-364…+1832 °F]) ±0.1 °C [±0.18 °F] |
| Thermocouple E (-270…+220 °C [-454…+364 °F]) ±1.0 °C [±1.8 °F]    |
| Thermocouples S and R ±0.4 °C [±0.72 °F]                          |
| Thermocouple C ±0.2 °C [±0.36 °F]                                 |
| Thermocouple B ±0.7 °C [±1.26 °F]                                 |
| ±50 mV ±6 µV                                                      |
| ±100 mV ±6 µV                                                     |

Table 19 - Output Specifications – 1762-IF2OF2, 1762-OF4 (Continued)

| Specification 1762-IF2OF2 1762-OF4                      |             |
|---------------------------------------------------------|-------------|
| Non-linearity (in percent full scale)  < ±0.59%(2)      | < ±0.59%(2) |
| Open and short-circuit protection Continuous Continuous |             |
| Output protection ±32 mA ±32 mA                         |             |
| Heat dissipation 2.6 W 2.8 W                            |             |

Table 20 - Valid Input/Output Data Word Formats/Ranges for 1762-IF2OF2

| Normal Operating Range Full Scale Range RAW/Proportional Data Scaled-for-PID   |                      |
|--------------------------------------------------------------------------------|----------------------|
| 0…0V DC                                                                        | 10.5V DC 32760 16380 |
| 0…0V DC                                                                        | 0.0V DC 0 0          |
| 4… 20 mA                                                                       | 21.0 mA 32760 16380  |
| 4… 20 mA                                                                       | 20.0 mA 31200 15600  |
| 4… 20 mA                                                                       | 4.0 mA 6240 3120     |
| 4… 20 mA                                                                       | 0.0 mA 0 0           |

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

## Certifications

| Certification (when product is marked) (1)   | Value                                                                                                                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                              | UL UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations                                                                                                                  |
|                                              | cUL UL Listed for Class I Division 2 Group A, B, C, D Hazardous Locations, certified for Canada.                                                                                          |
| CE                                           | European Union 2014/30/EU EMC Directive, compliant with: EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
| RCM                                          | Australian Radiocommunications Act, compliant with: AS/NZS CISPR 11; Industrial Emissions                                                                                                 |
| KC                                           | Korean Registration of Broadcasting and Communications Equipment, compliant with: Article 58-2 of Radio Waves Act, Clause 3                                                               |

## MicroLogix 1200 RTB Replacement Kit

## 1762 Replacement Parts

The 40-point controller removable terminal blocks kit (catalog number 1762-RPLRTB40) consists of:

- One 25-point double row terminal block
- One 29-point double row terminal block

Both are terminal blocks for a 40-point controller.

<!-- image -->

## Notes:

## Understand the Controller Status Indicators

## Troubleshoot Your System

The controller status indicators provide a mechanism to determine the current status of the controller if a programming device is not present or available.

Figure 75 - Controller Status Indicator Location

<!-- image -->

Table 21 - Controller Status Indicators

| Status Indicator Color Indicates   |                                                     |
|------------------------------------|-----------------------------------------------------|
| POWER                              | Off No input power or power error condition         |
| POWER                              | Steady green Power on                               |
| RUN                                | Off Not executing the user program                  |
| RUN                                | Steady green Executing the user program in run mode |
| RUN                                | Flashing green Memory module transfer occurring     |
| FAULT                              | Off No fault detected                               |
| FAULT                              | Flashing red Application fault detected             |
| FAULT                              | Steady red Controller hardware faulted              |
| FORCE                              | Off No forces installed                             |
| FORCE                              | Steady amber Forces installed                       |
| COMM 0(1)                          | Off Not transmitting via RS-232 port                |
| COMM 0(1)                          | Steady green Transmitting via RS-232 port           |
| DCOMM(2)                           | Off Configured communications                       |
| DCOMM(2)                           | Steady green Default communications                 |
| INPUTS                             | Off Input is not energized                          |
| INPUTS                             | Steady amber Input is energized (terminal status)   |
| OUTPUTS                            | Off Output is not energized                         |
| OUTPUTS                            | Steady amber Output is engerized (logic status)     |

<!-- image -->

Table 22 - List of Error Conditions

|                                         | If the LEDS Indicate The Following Error Exists Probable Cause Recommended Action   |                                        |                                                                                                                                                                          |
|-----------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All LEDs off                            | No input power or power supply error                                                |                                        | No line power Verify proper line voltage and connections to the controller.                                                                                              |
| All LEDs off                            | No input power or power supply error                                                | Power supply overloaded                | This problem can occur intermittently if power supply is overloaded when output loading and temperature varies.                                                          |
| Power and FAULT LEDs on solid           | Hardware faulted                                                                    |                                        | Processor hardware error Cycle power. Contact your local Allen-Bradley representative if the error persists.                                                             |
| Power and FAULT LEDs on solid           | Hardware faulted                                                                    |                                        | Loose wiring Verify connections to the controller.                                                                                                                       |
| Power LED on and FAULT LED flashing     | Application fault                                                                   | Hardware/software major fault detected | For error codes and Status File information, see MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 . |
| RUN, FORCE, and FAULT LEDs all flashing | Operating system fault                                                              | Missing or corrupt operating system    | See Missing or Corrupt OS LED Pattern on page 96 .                                                                                                                       |

## Normal Operation

The POWER and RUN status indicators are On. If a force condition is active, the FORCE status indicator turns on and remains on until all forces are removed.

## Error Conditions

If an error exists within the controller, the controller LEDs operate as described in Table 22 .

## Controller Error Recovery Model

Figure 76 helps you diagnose software and hardware problems in the micro controller. The model provides common questions you might ask to help troubleshoot your system. See the recommended pages within the model for further help.

Figure 76 - Controller Error Recovery Model

<!-- image -->

## Analog Expansion I/O Diagnostics and Troubleshooting

## Table 24 - Module Error Table

|                                                 | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   | “Don’t Care” Bits Module Error Extended Error Information   |
|-------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
|                                                 | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                       |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
|                                                 |                                                             | 0000000000000000                                            |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |
| Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1 | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             | Hex Digit 4 Hex Digit 3 Hex Digit 2 Hex Digit 1             |                                                             |                                                             |                                                             |                                                             |                                                             |                                                             |

## Module Error Field

The purpose of the module error field is to classify module errors into three distinct groups, as described in Table 25. The type of error determines what kind of information exists in the extended error information field. These types of module errors are typically reported in the controller's I/O status file. See MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for more information.

## Module Operation and Channel Operation

The module performs operations at two levels:

- Module level
- Channel level

Module-level operations include functions such as power-up, configuration, and communication with the controller.

Internal diagnostics are performed at both levels of operation. Both module hardware and channel configuration error conditions are reported to the controller. Channel overrange or underrange conditions are reported in the module's input data table. Module hardware errors are reported in the controller's I/O status file. See MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for more information.

When a fault condition is detected, the analog outputs are reset to zero.

## Power-up Diagnostics

At module power-up, a series of internal diagnostic tests are performed.

Table 23 - Module Status LED State Table

| If Module Status LED is Indicated Condition Corrective Action                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------|
| On Proper Operation No action is required.                                                                                             |
| Off Module Fault  Cycle power. If condition persists, replace the module. Call your local distributor or Allen-Bradley for assistance. |

## Critical and Non-critical Errors

Non-critical module errors are recoverable. Channel errors (overrange or underrange errors) are non-critical. Non-critical error conditions are indicated in the module input data table. Non-critical configuration errors are indicated by the extended error code.

Critical module errors are conditions that prevent normal or recoverable operation of the system. When these types of errors occur, the system leaves the run mode of operation.

Critical and non-critical module errors are indicated in Table 26 .

## Module Error Definition Table

Analog module errors are expressed in two fields as four-digit Hex format with the most significant digit as "don't care" and irrelevant. The two fields are "Module Error" and "Extended Error Information". The structure of the module error data is shown in Table 24 .

Table 25 - Module Error Types

| Error Type  Module Error Field Value Bits 11 through 09 (Binary)   | Description                                                                                                                                                                                          |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                    | No Errors 000 No error is present. The extended error field holds no additional information.                                                                                                         |
|                                                                    | Hardware Errors 001 General and specific hardware error codes are specified in the extended error information field.                                                                                 |
| Configuration Errors 010                                           | Module-specific error codes are indicated in the extended error field. These error codes correspond to options that you can change directly. For example, the input range or input filter selection. |

## Extended Error Information Field

Check the extended error information field when a non-zero value is present in the module error field. See Table 26 and Table 27 .

<!-- image -->

If no errors are present in the module error field, the extended error information field is set to zero.

## Hardware Errors

General or module-specific hardware errors are indicated by module error code 2. See Table 26 and Table 27 .

## Configuration Errors

If you set the fields in the configuration file to invalid or unsupported values, the module ignores the invalid configuration, generates a non-critical error, and keeps operating with the previous configuration.

Table 26 and Table 27 lists the configuration error codes defined for the module.

## Error Codes

Table 26 - Extended Error Codes for 1762-IF2OF2

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

(1) X represents “Don’t Care”.

Table 27 - Extended Error Codes for 1762-IF4 and 1762-OF4

| Error Type  Module Error Code                         | Hex Equivalent (1) Extended Error Information Code  Binary Binary   | Error Description                                                      |
|-------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
|                                                       | No Error X000 000 0 0000 0000 No error                              |                                                                        |
| General Common Hardware Error                         |                                                                     | X200 001 0 0000 0000 General hardware error; no additional information |
| General Common Hardware Error                         |                                                                     | X201 001 0 0000 0001 Power-up reset state                              |
| Hardware-specific Error X300 001 1 0000 0000 Reserved |                                                                     |                                                                        |

.

Table 27 - Extended Error Codes for 1762-IF4 and 1762-OF4 (Continued)

| Error Type   | Error Description                                                        |
|--------------|--------------------------------------------------------------------------|
| Error Type   | Error Description                                                        |
|              | X401 010 0 0000 0001 Invalid range select (Channel 0)                    |
|              | X402 010 0 0000 0010 Invalid range select (Channel 1)                    |
|              | X403 010 0 0000 0011 Invalid range select (Channel 2)                    |
|              | X404 010 0 0000 0100 Invalid range select (Channel 3)                    |
|              | X405 010 0 0000 0101 Invalid filter select (Channel 0)  –  1762-IF4 only |
|              | X406 010 0 0000 0110 Invalid filter select (Channel 1)  –  1762-IF4 only |
|              | X407 010 0 0000 0111 Invalid filter select (Channel 2)  –  1762-IF4 only |
|              | X408 010 0 0000 1000 Invalid filter select (Channel 3)  –  1762-IF4 only |
|              | X409 010 0 0000 1001 Invalid format select (Channel 0)                   |
|              | X40A 010 0 0000 1010 Invalid format select (Channel 1)                   |
|              | X40B 010 0 0000 1011 Invalid format select (Channel 2)                   |
|              | X40C 010 0 0000 1100 Invalid format select (Channel 3)                   |

(1) X represents ‘Don’t Care’.

## Call Rockwell Automation for Assistance

If you need to contact Rockwell Automation or local distributor for assistance, it is helpful to obtain the following (prior to calling):

- Controller type, series letter, revision letter, and firmware (FRN) number of the controller
- Controller LED status
- Controller error codes (See MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 for error code information.)

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

Installing a new operating system deletes the user program. After the operating system upgrade is successful, you must transfer your control program back to the controller. The communication parameters are described in Table 6 .

## Install ControlFLASH Software

To install ControlFLASH properly, see the Install ControlFLASH section in ControlFLASH User Manual, publication 1756-UM105 .

If a ControlFLASH directory does not exist, one is created in your Program Files directory.

For 1762-Lxxxxx controllers, double-click the 1762-LSC-FRNxx.exe file to install the operating system upgrade (where xx is the firmware revision number).

For 1762-LxxxxxR controllers, double-click the 1762-LRC-FRNxx.exe file to install the operating system upgrade.

## Prepare the Controller for Firmware Update

Controller Configuration

The controller must be configured for default communications (use Communications Toggle push button; DCOMM LED on) and be in the Program mode to allow the download of a new operating system.

## Sequence of Operation

## Missing or Corrupt OS LED Pattern

The following steps detail the key events in the upgrade process.

1. Controller mode and communications parameters are checked.
2. Download begins.
3. During the download, the Force, Battery, and Comms LEDs perform a walking bit pattern.
4. When the download is complete, the integrity of the new OS is checked. If the new OS is corrupt, the controller sends an error message to the download tool and flashes the Missing or Corrupt OS LED pattern. See Missing or Corrupt OS LED Pattern on page 96 .
5. Following a successful transfer, the Power, Force, and Battery LEDs flash on and remain on for five seconds. Then the controller resets.

When an operating system download is not successful or if the controller does not contain a valid operating system, the controller flashes the Run, Force, and Fault LEDs on and off.

## RS-232 Communication Interface

## DF1 Full-duplex Protocol

<!-- image -->

## Connect to Networks via RS-232 Interface

The following protocols are supported from the RS-232 communication channel (Channel 0):

- DF1 Full-duplex
- DF1 Half-duplex master/slave
- DR1 Radio modem
- DH-485
- Modbus RTU master/slave
- ASCII

The communications port on the MicroLogix 1200 controller utilizes an RS-232 interface. RS-232 is an Electronics Industries Association (EIA) standard that specifies the electrical and mechanical characteristics for serial binary communication. They provide various system configuration possibilities. RS-232 defines electrical connection characteristics; not protocols.

One of the biggest benefits of an RS-232 interface is that it lets you integrate telephone and radio modems into your control system (using the appropriate DF1 protocol only, not DH-485 protocol), but it is for point-to-point connections only between two devices.

DF1 Full-duplex protocol provides a point-to-point connection between two devices. DF1 Fullduplex protocol combines data transparency (American National Standards Institute ANSI X3.28-1976 specification subcategory D1) and 2-way simultaneous transmission with embedded responses (subcategory F1).

MicroLogix 1200 controllers support the DF1 Full-duplex protocol via RS-232 connection to external devices, such as computers, or other controllers that support DF1 Full-duplex.

DF1 is an open protocol. See the DF1 Protocol and Command Set Reference Manual, publication 1770-RM516, for more information.

DF1 Full-duplex protocol (also referred to as DF1 point-to-point protocol) is useful where RS-232 point-to-point communication is required. DF1 protocol controls message flow, detects and signals errors, and retries if errors are detected.

## Example DF1 Full-duplex Connections

For information about required network connecting equipment, see Communication Connections on page 53 .

## DF1 Half-duplex Protocol

Figure 77 - Example of DF1 Full-duplex Connections

<!-- image -->

We recommend using an AIC+, catalog number 1761-NET-AIC, as your optical isolator.

DF1 Half-duplex protocol is a multi-drop single master/multiple slave network. DF1 Half-duplex protocol supports data transparency (American National Standards Institute ANSI - X3.28-1976 specification subcategory D1). In contrast to DF1 Full-duplex, communication takes place in one direction at a time. You can use the RS-232 port on the MicroLogix 1200 controller as both a Half-duplex programming port and a Half-duplex peer-to-peer messaging port.

A MicroLogix 1200 controller can act as the master or as a slave on a Half-duplex network. When the MicroLogix 1200 controller is a slave device, a master device is required to 'run' the network. Several other Allen-Bradley products support the DF1 Half-duplex master protocol. They include the SLC 5/03 and higher processors, enhanced PLC-5® processors and RSLinx® software (version 2.x or later).

DF1 Half-duplex supports up to 255 devices (address 0…254) with address 255 reserved for master broadcasts. As a DF1 Half-duplex slave device, the MicroLogix 1200 controller supports broadcast reception. As a DF1 Half-duplex master, the MicroLogix 1200 controller supports both the reception and initiation of broadcast write commands (via the MSG instruction). The MicroLogix 1200 controller also supports Half-duplex modems using RTS/CTS hardware handshaking.

Figure 78 - Example of DF1 Half-duplex Connections

<!-- image -->

Rockwell Automation Publication 1762-UM001I-EN-P - May 2024

## DH-485 Communication Protocol

## Use Modems with MicroLogix Programmable Controllers

The types of modems you can use with MicroLogix controllers include the following:

- Dial-up phone modems

A MicroLogix 1200 controller, on the receiving end of the dial-up connection, can be configured for DF1 Full-duplex protocol with or without handshaking. The modem connected to the MicroLogix controller should support auto-answer. The MicroLogix 1200 controller supports ASCII out communications. Therefore, it can cause a modem to initiate or disconnect a phone call.

- Leased-line modems

Leased-line modems are used with dedicated phone lines that are typically leased from the local phone company. The dedicated lines can be in a point-to-point topology to support Full-duplex communications between two modems or in a multi-drop topology supporting Half-duplex communications between three or more modems.

- Radio modems

Radio modems may be implemented in a point-to-point topology supporting either Halfduplex or Full-duplex communications, or in a multi-drop topology supporting Halfduplex communications between three or more modems. MicroLogix 1200 also supports DF1 Radio Modem protocol.

- Line drivers

Line drivers, also called short-haul modems, do not actually modulate the serial data, but rather condition the electrical signals to operate reliably over long transmission distances (up to several miles). Line drivers are available in Full-duplex and Half-duplex models. Allen-Bradley's AIC+ Advanced Interface Converter is a Half-duplex line driver that converts an RS-232 electrical signal into an RS-485 electrical signal, increasing the signal transmission distance from 15…1219 m (50…4000 ft.) (2438 m (8000 ft.) when bridged).

For point-to-point Full-duplex modem connections that do not require any modem handshaking signals to operate, use DF1 Full-duplex protocol with no handshaking. For pointto-point Full-duplex modem connections that require RTS/CTS handshaking, use DF1 Fullduplex protocol with handshaking.

For radio modem connections, use DF1 Radio Modem protocol, especially if store and forward capability is required.

For general multi-drop modem connections, or for point-to-point modem connections that require RTS/CTS handshaking, use DF1 Half-duplex slave protocol. In this case, one (and only one) of the other devices must be configured for DF1 Half-duplex master protocol.

## IMPORTANT

Never attempt to use DH-485 protocol through modems under any circumstance.

<!-- image -->

All MicroLogix 1200 controllers support RTS/CTS modem handshaking when configured for DF1 Full-duplex protocol with the control line parameter set to Fullduplex Modem Handshaking or DF1 Half-duplex slave protocol with the control line parameter set to 'Half-duplex Modem'. No other modem handshaking lines (Data Set Ready, Carrier Detect, and Data Terminal Ready) is supported by any MicroLogix 1200 controllers.

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

Table 28 - DF1 Full-duplex Configuration Parameters

| Parameter Options              |
|--------------------------------|
| Communication Rate 9600, 19.2K |
| Node Address 1…31 decimal      |
| Token Hold Factor 1…4          |

See Software Considerations on page 102 for tips on setting the parameters listed above.

## Devices that use the DH-485 Network

In addition to the MicroLogix 1200 controllers, the devices that are shown in Table 29 also support the DH-485 network.

Table 29 - Devices that Support a DH-485 Network

| Catalog Number Description Installation Function Publication                                                                       |                                                    |                                                                                                                                                                                                   |                                  |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
|                                                                                                                                    |                                                    | Bulletin 1763 MicroLogix 1100 Series A or later These controllers support DH-485 communications.                                                                                                  | 1763-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1764 MicroLogix 1500 Series A or later These controllers support DH-485 communications.                                                                                                  | 1764-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1766 MicroLogix 1400 Series A or later These controllers support DH-485 communications.                                                                                                  | 1766-UM001                       |
|                                                                                                                                    |                                                    | Bulletin 1747 Processors SLC 500 Processors SLC Chassis These processors support a variety of I/O requirements and functionality.                                                                 | 1747-UM011                       |
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

· Type of process being controlled

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

The following example shows how to send messages from a device on the DH+ network to a MicroLogix controller on the DH-485 network. This method uses an SLC 5/04 processor as the bridge connection.

When using this method as shown in Figure 79:

- PLC-5 devices can send read and write commands to MicroLogix controllers.
- MicroLogix controllers can respond to MSG instructions received.
- MicroLogix controllers can initiate MSG instructions to devices on the DH+ network.
- The computer can send read and write commands to MicroLogix controllers.
- The computer can do remote programming of MicroLogix controllers.

Figure 79 - Communication Between DH-485 and DH+ Networks with MicroLogix Controllers

<!-- image -->

## Example DH-485 Connections

The following network diagrams provide examples of how to connect MicroLogix 1200 controllers to the DH-485 network using the AIC+ Advanced Interface Converter, 1761-NET-AIC.

Figure 80 - DH-485 Network with a MicroLogix 1200 Controller

<!-- image -->

<!-- image -->

Series C or later cables are required.

Figure 81 - Typical 3-Node Network

<!-- image -->

<!-- image -->

- This 3-node network is not expandable.

Figure 82 - Networked Operator Interface Device and MicroLogix Controllers

<!-- image -->

## Modbus Communication Protocol

## ASCII

Modbus is a Half-duplex, master-slave communications protocol. The Modbus network master reads and writes coils and registers. Modbus protocol allows a single master to communicate with a maximum of 247 slave devices. MicroLogix 1200 controllers support Modbus RTU master and Modbus RTU slave protocol.

For more information on how to configure your MicroLogix 1200 controller for Modbus protocol, see the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001. For more information about the Modbus protocol, see the Modbus Protocol Specifications (available from www.modbus.org).

ASCII provides connection to other ASCII devices, such as barcode readers, weigh scales, serial printers, and other intelligent devices.

You can use ASCII by configuring the RS-232 port, channel 0 for the ASCII driver. For detailed configuration information, see the MicroLogix 1200 and MicroLogix 1500 Programmable Controllers Instruction Set Reference Manual, publication 1762-RM001 .

## System Loading Calculations

<!-- image -->

## System Loading and Heat Dissipation

When you connect MicroLogix accessories and expansion I/O, an electrical load is placed on the controller power supply. This section shows how to calculate the load of your control system.

The following example is provided to illustrate system loading calculation. The system calculation procedure accounts for the amount of 5V DC and 24V DC current that is consumed by the controller, expansion I/O, and user-supplied equipment.

Use the System Loading Worksheet for 24-point Controllers on page 107 to calculate your specific 24-point controller configuration.

Use the System Loading Worksheet for 40-point Controllers on page 109 to calculate your specific 40-point controller.

Current consumed by the processor, memory modules, and the real-time clock modules has already been factored into the calculations. A system is valid if the current and power requirements are satisfied.

## System Loading Example Calculations (24-point Controller)

Current Loading

Table 30 - Calculating the Current for MicroLogix Accessories

| Catalog Number                                                                                        | Device Current Requirements Calculated Current   | Device Current Requirements Calculated Current   |                                                       |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
|                                                                                                       |                                                  |                                                  | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |
| 1761-NET-AIC(1) when powered by the base unit communications port, selector switch in the up position |                                                  |                                                  | 0 120 0 120                                           |
| Subtotal 1:                                                                                           | Subtotal 1:                                      | 0                                                | 120                                                   |

Table 31 - Calculating the Current for Expansion I/O

|                    | n A B n x A n x B                                     |                                                      |
|--------------------|-------------------------------------------------------|------------------------------------------------------|
| Number of Modules  | Device Current Requirements (max) Calculated Current  | Device Current Requirements (max) Calculated Current |
|                    | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                      |
|                    | 1762-IA8 2 50 0 100 0                                 |                                                      |
| 1762-IF4 40 50     |                                                       |                                                      |
| 1762-IF2OF2 40 105 |                                                       |                                                      |
| 1762-IQ8 50 0      |                                                       |                                                      |
| 1762-IQ32T 170 0   |                                                       |                                                      |
| 1762-IR4 40 50     |                                                       |                                                      |
| 1762-IT4 40 50     |                                                       |                                                      |
| 1762-OA8 115 0     |                                                       |                                                      |
| 1762-OB8 115 0     |                                                       |                                                      |
| 1762-OB16 175 0    |                                                       |                                                      |
| 1762-OB32T 175 0   |                                                       |                                                      |
| 1762-OF4 40 165    |                                                       |                                                      |
| 1762-OV32T 175 0   |                                                       |                                                      |
|                    | 1762-OW8 2 80 90 160 180                              |                                                      |

Table 31 - Calculating the Current for Expansion I/O (Continued)

|                                      |                                                      |                                                       | n A B n x A n x B   |
|--------------------------------------|------------------------------------------------------|-------------------------------------------------------|---------------------|
| Catalog Number (1) Number of Modules | Device Current Requirements (max) Calculated Current | Device Current Requirements (max) Calculated Current  |                     |
|                                      |                                                      | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                     |
| 1762-OW16                            | 140(2)                                               | 180(2)                                                |                     |
| 1762-OX6I 110 110                    |                                                      |                                                       |                     |
| 1762-IQ8OW6 110 80                   |                                                      |                                                       |                     |
|                                      | Total Modules (6 maximum): 4 Subtotal 2: 260 180     | Total Modules (6 maximum): 4 Subtotal 2: 260 180      |                     |

## Validate the System

The example systems that are shown in Table 32 and Table 33 are verified to be acceptable configurations. The systems are valid because:

- Calculated Current Values &lt; Maximum Allowable Current Values
- Calculated System Loading &lt; Maximum Allowable System Loading

Table 32 - Validating Systems Using 1762-L24AWA, 1762-L24BXB, 1762-L24AWAR or 1762-L24BXBR

| Maximum Allowable Values Calculated Values                                          |                                                                                                 |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Current Current (Subtotal 1 from Table 30 + Subtotal 2 from Table 31)               |                                                                                                 |
|                                                                                     | 400 mA @ 5V DC 350 mA @ 24V DC 0 mA + 260 mA = 260 mA @ 5V DC 120 mA + 180 mA = 300 mA @ 24V DC |
| System Loading System Loading                                                       |                                                                                                 |
| 10.4 W = (260 mA x 5V) + (300 mA x 24 V) = (1300 mW) + (7200 mW) = 8500 mW = 8.50 W |                                                                                                 |

Table 33 - Validating Systems using 1762-L24BWA or 1762-L24BWAR

| Maximum Allowable Values Calculated Values                                            | Maximum Allowable Values Calculated Values                                                                                |                                                                                                                           |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Current for Devices Connected to the +24V DC Sensor Supply Sum of all sensor currents | Current for Devices Connected to the +24V DC Sensor Supply Sum of all sensor currents                                     |                                                                                                                           |
| 250 mA @ 24V DC 140 mA @ 24V DC (example sensor value)                                | 250 mA @ 24V DC 140 mA @ 24V DC (example sensor value)                                                                    |                                                                                                                           |
|                                                                                       | Current for MicroLogix Accessories and Expansion I/O Current Values (Subtotal 1 from Table 30 + Subtotal 2 from Table 31) | Current for MicroLogix Accessories and Expansion I/O Current Values (Subtotal 1 from Table 30 + Subtotal 2 from Table 31) |
|                                                                                       |                                                                                                                           | 400 mA @ 5V DC 350 mA @ 24V DC 0 mA + 260 mA = 260 mA @ 5V DC 120 mA + 180 mA = 300 mA @ 24V DC                           |
| System Loading System Loading                                                         | System Loading System Loading                                                                                             |                                                                                                                           |
| 12 W                                                                                  | = (140 mA x 24 V) + (260 mA x 5 V) + (300 mA x 24 V) = (3360 mW) + (1300 mW) + (7200 mW) = 11,860 mW = 11.9 W             | = (140 mA x 24 V) + (260 mA x 5 V) + (300 mA x 24 V) = (3360 mW) + (1300 mW) + (7200 mW) = 11,860 mW = 11.9 W             |

## System Loading Example Calculations (40-point Controller)

Current Loading

Table 34 - Calculating the Current for MicroLogix Accessories

| Catalog Number                                                                                        | Device Current Requirements Calculated Current   | Device Current Requirements Calculated Current   |                                                       |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
|                                                                                                       |                                                  |                                                  | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |
| 1761-NET-AIC(1) when powered by the base unit communications port, selector switch in the up position |                                                  |                                                  | 0 120 0 120                                           |
| Subtotal 1:                                                                                           | Subtotal 1:                                      | 0                                                | 120                                                   |

Table 35 - Calculating the Current for Expansion I/O

|                    | n A B n x A n x B                                     |                                                      |
|--------------------|-------------------------------------------------------|------------------------------------------------------|
| Number of Modules  | Device Current Requirements (max) Calculated Current  | Device Current Requirements (max) Calculated Current |
|                    | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                      |
| 1762-IA8 50 0      |                                                       |                                                      |
| 1762-IF4 40 50     |                                                       |                                                      |
|                    | 1762-IF2OF2 1 40 105 40 105                           |                                                      |
| 1762-IQ8 50 0      |                                                       |                                                      |
| 1762-IQ16 2        | 70(2)  0  140(2)  0                                   |                                                      |
| 1762-IQ32T 170 0   |                                                       |                                                      |
| 1762-IR4 40 50     |                                                       |                                                      |
| 1762-IT4 40 50     |                                                       |                                                      |
|                    | 1762-OA8 1 115 0 115 0                                |                                                      |
| 1762-OB8 115 0     |                                                       |                                                      |
| 1762-OB16 175 0    |                                                       |                                                      |
| 1762-OB32T 175 0   |                                                       |                                                      |
| 1762-OF4 40 165    |                                                       |                                                      |
| 1762-OV32T 175 0   |                                                       |                                                      |
| 1762-OW8 80 90     |                                                       |                                                      |
| 1762-OW16 1        | 140(2)  180(2)  140(2)  180(2)                        |                                                      |
| 1762-OX6I 110 110  |                                                       |                                                      |
| 1762-IQ8OW6 110 80 |                                                       |                                                      |
|                    | Total Modules (6 maximum): 5 Subtotal 2: 435 285      |                                                      |

## Validate the System

The example systems that are shown in Table 36 and Table 41 are verified to be acceptable configurations. The systems are valid because:

- Calculated Current Values &lt; Maximum Allowable Current Values
- Calculated System Loading &lt; Maximum Allowable System Loading

Table 36 - Validating Systems using 1762-L40AWA, 1762-L40BXB, 1762-L40AWAR or 1762-L40BXBR

| Maximum Allowable Values Calculated Values                                          |                                                                                                 |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Current Current (Subtotal 1 from Table 34 + Subtotal 2 from Table 35)               |                                                                                                 |
|                                                                                     | 600 mA @ 5V DC 500 mA @ 24V DC 0 mA + 435 mA = 435 mA @ 5V DC 120 mA + 285 mA = 405 mA @ 24V DC |
| System Loading System Loading                                                       |                                                                                                 |
| 15 W = (4.5 mA x 5V) + (405 mA x 24V) = (2175 mW) + (9720 mW) = 11,895 mW = 11.90 W |                                                                                                 |

## System Loading Worksheet for 24-point Controllers

Table 37 , Table 38 , Table 39, and Table 40 are provided for system loading validation for 24-point controllers. See System Loading Example Calculations (24-point Controller) on page 105 .

## Current Loading

Table 37 - Calculating the Current for MicroLogix Accessories

| Catalog Number                                                                                        | Device Current Requirements Calculated Current   | Device Current Requirements Calculated Current        |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
|                                                                                                       |                                                  | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |
| 1761-NET-AIC(1) when powered by the base unit communications port, selector switch in the up position | 0 120                                            |                                                       |
| Subtotal 1:                                                                                           |                                                  |                                                       |

Table 38 - Calculating the Current for Expansion I/O

| Catalog Number (1)                     | n A B n x A n x B                                     |                                                      |
|----------------------------------------|-------------------------------------------------------|------------------------------------------------------|
| Catalog Number (1)                     | Device Current Requirements (max) Calculated Current  | Device Current Requirements (max) Calculated Current |
| Number of Modules                      | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                      |
| 1762-IA8 50 0                          |                                                       |                                                      |
| 1762-IF4 40 50                         |                                                       |                                                      |
| 1762-IF2OF2 40 105                     |                                                       |                                                      |
| 1762-IQ8 50 0                          |                                                       |                                                      |
| 1762-IQ16  70(2)                       | 0                                                     |                                                      |
| 1762-IQ32T 170 0                       |                                                       |                                                      |
| 1762-IR4 40 50                         |                                                       |                                                      |
| 1762-IT4 40 50                         |                                                       |                                                      |
| 1762-OA8 115 0                         |                                                       |                                                      |
| 1762-OB8 115 0                         |                                                       |                                                      |
| 1762-OB16 175 0                        |                                                       |                                                      |
| 1762-OB32T 175 0                       |                                                       |                                                      |
| 1762-OF4 40 165                        |                                                       |                                                      |
| 1762-OV32T 175 0                       |                                                       |                                                      |
| 1762-OW8 80 90                         |                                                       |                                                      |
| 1762-OW16  140(2)                      | 180(2)                                                |                                                      |
| 1762-OX6I 110 110                      |                                                       |                                                      |
| 1762-IQ8OW6 110 80                     |                                                       |                                                      |
| Total Modules (6 maximum): Subtotal 2: |                                                       |                                                      |

Table 39 - Validating Systems using 1762-L24AWA, 1762-L24BXB, 1762-L24AWAR or 1762-L24BXBR

| Maximum Allowable Values Calculated Values                                                                       |
|------------------------------------------------------------------------------------------------------------------|
| Current Current (Subtotal 1 from Table 37 + Subtotal 2 from Table 38)                                            |
| 400 mA @ 5V DC 350 mA @ 24V DC mA @ 5V DC mA @ 24V DC                                                            |
| System Loading System Loading                                                                                    |
| 10.4 W = (________ mA x 5V) + (________ mA x 24V) = __________ mW + __________ mW = __________ mW = __________ W |

Table 40 - Validating Systems using 1762-L24BWA or 1762-L24BWAR

| Maximum Allowable Values Calculated Values                 | Maximum Allowable Values Calculated Values                                                                                                        |                                                                                                                                                   |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Current for Devices Connected to the +24V DC Sensor Supply | Sum of all sensor currents Include 1761-NET-AIC here rather than in Table 37, if it is powered externally by the sensor supply.                   | Sum of all sensor currents Include 1761-NET-AIC here rather than in Table 37, if it is powered externally by the sensor supply.                   |
| 250 mA @ 24V DC mA @ 24V DC                                | 250 mA @ 24V DC mA @ 24V DC                                                                                                                       |                                                                                                                                                   |
|                                                            | Current for MicroLogix Accessories and Expansion I/O Current (Subtotal 1 from Table 37 + Subtotal 2 from Table 38)                                | Current for MicroLogix Accessories and Expansion I/O Current (Subtotal 1 from Table 37 + Subtotal 2 from Table 38)                                |
| 400 mA @ 5V DC 350 mA @ 24V DC mA @ 5V DC mA @ 24V DC      |                                                                                                                                                   |                                                                                                                                                   |
| System Loading System Loading                              | System Loading System Loading                                                                                                                     |                                                                                                                                                   |
| 12 W                                                       | = (________ mA x 24 V) + (________ mA x 5V) + (________ mA x 24 V) = __________ mW + __________ mW + __________ mW = __________ mW = __________ W | = (________ mA x 24 V) + (________ mA x 5V) + (________ mA x 24 V) = __________ mW + __________ mW + __________ mW = __________ mW = __________ W |

Table 41 - Validating Systems using 1762-L40BWA or 1762-L40BWAR

| Maximum Allowable Values Calculated Values                                            | Maximum Allowable Values Calculated Values                                                                         |                                                                                                                    |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Current for Devices Connected to the +24V DC Sensor Supply Sum of all current sensors | Current for Devices Connected to the +24V DC Sensor Supply Sum of all current sensors                              |                                                                                                                    |
| 400 mA @ 24V DC 150 mA @ 24V DC (example sensor value)                                | 400 mA @ 24V DC 150 mA @ 24V DC (example sensor value)                                                             |                                                                                                                    |
|                                                                                       | Current for MicroLogix Accessories and Expansion I/O Current (Subtotal 1 from Table 34 + Subtotal 2 from Table 35) | Current for MicroLogix Accessories and Expansion I/O Current (Subtotal 1 from Table 34 + Subtotal 2 from Table 35) |
|                                                                                       |                                                                                                                    | 600 mA @ 5V DC 500 mA @ 24V DC 0 mA + 435 mA = 435 mA @ 5V DC 120 mA + 285 mA = 405 mA @ 24V DC                    |
| System Loading System Loading                                                         | System Loading System Loading                                                                                      |                                                                                                                    |
| 16 W                                                                                  | = (150 mA x 24V) + (435 mA x 5V) + (405 mA x 24V) = (3600 mW) + (2175 mW) + (9720 mW) = 15,495 W = 15.50 W         | = (150 mA x 24V) + (435 mA x 5V) + (405 mA x 24V) = (3600 mW) + (2175 mW) + (9720 mW) = 15,495 W = 15.50 W         |

## System Loading Worksheet for 40-point Controllers

Table 42 , Table 43 , Table 44, and Table 45 are provided for system loading validation for 40-point Controllers. See System Loading Example Calculations (40-point Controller) on page 106 .

## Current Loading

Table 42 - Calculating the Current for MicroLogix Accessories

| Catalog Number                                                                                        | Device Current Requirements Calculated Current   | Device Current Requirements Calculated Current        |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
|                                                                                                       |                                                  | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |
| 1761-NET-AIC(1) when powered by the base unit communications port, selector switch in the up position | 0 120                                            |                                                       |
| Subtotal 1:                                                                                           |                                                  |                                                       |

Table 43 - Calculating the Current for Expansion I/O

|                    | n A B n x A n x B                                     |                                                      |
|--------------------|-------------------------------------------------------|------------------------------------------------------|
| Number of Modules  | Device Current Requirements (max) Calculated Current  | Device Current Requirements (max) Calculated Current |
|                    | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                      |
| 1762-IA8 50 0      |                                                       |                                                      |
| 1762-IF4 40 50     |                                                       |                                                      |
| 1762-IF2OF2 40 105 |                                                       |                                                      |
| 1762-IQ8 50 0      |                                                       |                                                      |
| 1762-IQ32T 170 0   |                                                       |                                                      |
| 1762-IR4 40 50     |                                                       |                                                      |
| 1762-IT4 40 50     |                                                       |                                                      |
| 1762-OA8 115 0     |                                                       |                                                      |
| 1762-OB8 115 0     |                                                       |                                                      |
| 1762-OB16 175 0    |                                                       |                                                      |

## Table 43 - Calculating the Current for Expansion I/O (Continued)

|                                        | n A B n x A n x B                                     |                                                      |
|----------------------------------------|-------------------------------------------------------|------------------------------------------------------|
| Catalog Number (1) Number of Modules   | Device Current Requirements (max) Calculated Current  | Device Current Requirements (max) Calculated Current |
|                                        | @ 5V DC (mA) @ 24V DC (mA) @ 5V DC (mA) @ 24V DC (mA) |                                                      |
| 1762-OB32T 175 0                       |                                                       |                                                      |
| 1762-OF4 40 165                        |                                                       |                                                      |
| 1762-OV32T 175 0                       |                                                       |                                                      |
| 1762-OW8 80 90                         |                                                       |                                                      |
| 1762-OW16  140(2)                      | 180(2)                                                |                                                      |
| 1762-OX6I 110 110                      |                                                       |                                                      |
| 1762-IQ8OW6 110 80                     |                                                       |                                                      |
| Total Modules (6 maximum): Subtotal 2: |                                                       |                                                      |

## Table 44 - Validating Systems using 1762-L40AWA, 1762-L40BXB, 1762-L40AWAR or 1762-L40BXBR

## Maximum Allowable Values Calculated Values

Current Current (Subtotal 1 from Table 42 + Subtotal 2 from Table 43)

600 mA @ 5V DC 500 mA @ 24V DC mA @ 5V DC mA @ 24V DC

System Loading System Loading

= (\_\_\_\_\_\_\_\_ mA x 5V) + (\_\_\_\_\_\_\_\_ mA x 24V)

= \_\_\_\_\_\_\_\_\_\_ mW + \_\_\_\_\_\_\_\_\_\_ mW

= \_\_\_\_\_\_\_\_\_\_ mW

= \_\_\_\_\_\_\_\_\_\_ W

## Table 45 - Validating Systems using 1762-L40BWA or 1762-L40BWAR

| Maximum Allowable Values Calculated Values                 | Maximum Allowable Values Calculated Values                                                                                                      |                                                                                                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Current for Devices Connected to the +24V DC Sensor Supply | Sum of all sensor currents Include 1761-NET-AIC here rather than in Table 42, if it is powered externally by the sensor supply.                 | Sum of all sensor currents Include 1761-NET-AIC here rather than in Table 42, if it is powered externally by the sensor supply.                 |
| 400 mA @ 24V DC mA @ 24V DC                                | 400 mA @ 24V DC mA @ 24V DC                                                                                                                     |                                                                                                                                                 |
|                                                            | Current for MicroLogix Accessories and Expansion I/O Current (Subtotal 1 from Table 42 + Subtotal 2 from Table 43)                              | Current for MicroLogix Accessories and Expansion I/O Current (Subtotal 1 from Table 42 + Subtotal 2 from Table 43)                              |
| 600 mA @ 5V DC 500 mA @ 24V DC mA @ 5 V DC mA @ 24V DC     |                                                                                                                                                 |                                                                                                                                                 |
| System Loading System Loading                              | System Loading System Loading                                                                                                                   |                                                                                                                                                 |
| 16 Watts                                                   | = (________ mA x 24V) + (________ mA x 5V) + (________ mA x 24V) = __________ mW + __________ mW + __________ mW = __________ mW = __________ W | = (________ mA x 24V) + (________ mA x 5V) + (________ mA x 24V) = __________ mW + __________ mW + __________ mW = __________ mW = __________ W |

Calculating Heat Dissipation Use Table 46 when you must determine the heat dissipation of your system for installation in
SifiSi an enclosure. For System Loading, take the value from the appropriate System Loading Worksheet for 24-point Controllers on page 107 or System Loading Worksheet for 40-point Controllers on page 109 .

## Table 46 - Heat Dissipation

| Heat Dissipation                                                                             | Heat Dissipation   | Heat Dissipation   |
|----------------------------------------------------------------------------------------------|--------------------|--------------------|
| Catalog Number  Equation or Constant Calculation Sub-Total                                   |                    |                    |
| 1762-L24AWA, 1762-L24AWAR 15.2 W + (0.4 x System Loading) 15.2 W + (0.4 x ______ W) ______ W |                    |                    |
| 1762-L24BWA, 1762-L24BWAR 15.7 W + (0.4 x System Loading) 15.7 W + (0.4 x ______ W) ______ W |                    |                    |
| 1762-L24BXB, 1762-L24BXBR 17.0 W + (0.3 x System Loading) 17.0 W + (0.3 x ______ W) ______ W |                    |                    |
| 1762-L40AWA, 1762-L40AWAR 21.0 W + (0.4 x System Loading) 21.0 W + (0.4 x ______ W) ______ W |                    |                    |
| 1762-L40BWA, 1762-L40BWAR 22.0 W + (0.4 x System Loading) 22.0 W + (0.4 x ______ W) ______ W |                    |                    |
| 1762-L40BXB, 1762-L40BXBR 27.9 W + (0.3 x System Loading) 27.9 W + (0.3 x ______ W) ______ W |                    |                    |
| 1762-IA8 2.0 W x number of modules 2.0 W x _________ ______ W                                |                    |                    |
| 1762-IF4 2.0 W x number of modules 2.0 W x _________ ______ W                                |                    |                    |
| 1762-IF2OF2 2.6 W x number of modules 2.6 W x _________ ______ W                             |                    |                    |

15 W

Table 46 - Heat Dissipation (Continued)

| Heat Dissipation                                                                                                                                    | Heat Dissipation   | Heat Dissipation   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------|
| Catalog Number  Equation or Constant Calculation Sub-Total                                                                                          |                    |                    |
| 1762-IQ8 3.7 W x number of modules 3.7 W x _________ ______ W                                                                                       |                    |                    |
| 1762-IQ16  5.1 W(1) x number of modules 5.1 W(1) x _________                                                                                        | ______ W           |                    |
| 1762-IQ32T  6.8 W x number of modules (@ 30V DC) 5.4 W x number of modules (@ 26.4V DC) 6.8 W x _________ (@ 30V DC) 5.4 W x _________ (@ 26.4V DC) | ______ W ______ W  |                    |
| 1762-IR4 1.5 W x number of modules 1.5 W x _________ ______ W                                                                                       |                    |                    |
| 1762-IT4 1.5 W x number of modules 1.5 W x _________ ______ W                                                                                       |                    |                    |
| 1762-OA8 2.9 W x number of modules 2.9 W x _________ ______ W                                                                                       |                    |                    |
| 1762-OB8 1.6 W x number of modules 1.6 W x _________ ______ W                                                                                       |                    |                    |
| 1762-OB16 2.9 W x number of modules 2.9 W x _________ ______ W                                                                                      |                    |                    |
| 1762-OB32T 3.4 W x number of modules 3.4 W x _________ ______ W                                                                                     |                    |                    |
| 1762-OF4 2.8 W x number of modules 2.8 W x _________ ______ W                                                                                       |                    |                    |
| 1762-OV32T 2.7 W x number of modules 2.7 W x _________ ______ W                                                                                     |                    |                    |
| 1762-OW8 2.9 W x number of modules 2.9 W x _________ ______ W                                                                                       |                    |                    |
| 1762-OW16  6.1 W(1) x number of modules 6.1 W(1) x _________                                                                                        | ______ W           |                    |
| 1762-OX6I 2.8 W x number of modules 2.8 W x _________ ______ W                                                                                      |                    |                    |
| 1762-IQ8OW6  5.0 W x number of modules (@ 30V DC) 4.4 W x number of modules (@ 26.4V DC) 5.0 W x _________ 4.4 W x _________                        | ______ W ______ W  |                    |
| Add Subtotals to Determine Heat Dissipation                                                                                                         | ______  W          |                    |

## Notes:

The following terms and abbreviations are used throughout this manual.

address

A character string that uniquely identifies a memory location. For example, I:1/0 is the memory address for the data located in the Input file location word1, bit 0.

AIC+ Advanced Interface Converter

A device that provides a communication link between various networked devices. 1761-NET-AIC.

- application 1) A machine or process monitored and controlled by a controller.

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

1) A rotary device that transmits position information.

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

A Central Processing Unit. See CPU (Central Processing Unit) on page 113 .

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

| 1762-24AWA wiring diagram  35 1762-40BWA sourcing wiring diagram  37 1762-IA8 wiring diagram  40   |
|----------------------------------------------------------------------------------------------------|
| 1762-IF2OF2                                                                                        |
| input type selection  47 output type selection  47                                                 |
| terminal block layout  48 wiring  48                                                               |
| 1762-IF4 input type selection  49 50                                                               |
| terminal block layout                                                                              |
| 1762-IQ16 wiring diagram  41                                                                       |
| 1762-IQ32T wiring diagram  42 40                                                                   |
| 1762-IQ8 wiring diagram                                                                            |
| 1762-IQ80W6 wiring diagram  46 1762-OA8 wiring diagram  42                                         |
| 1762-OB16 wiring diagram  43                                                                       |
| 1762-OB32T wiring diagram                                                                          |
| 44 43                                                                                              |
| 1762-OB8 wiring diagram  1762-OV32T wiring diagram  44                                             |
| 1762-OW16 wiring diagram  45 45                                                                    |
| 1762-OW8 wiring diagram  1762-OX6I wiring diagram  46                                              |
| A address  113                                                                                     |
| Advanced Interface Converter. See AIC+ AIC+ 65                                                     |
| apply power to  attach to the network  64                                                          |
| connect  61 connecting                                                                             |
| isolated modem  56 definition  113                                                                 |
| install  64 modem connections                                                                      |
| 56 64                                                                                              |
| recommended user supplied components                                                               |
| safety consideration  64                                                                           |
| select cable  62 92                                                                                |
| analog expansion I/O  diagnostics  92                                                              |
| module operation vs. channel operation  92 power-up diagnostics  92 system wiring guidelines  47   |
| troubleshooting  92                                                                                |
| 113                                                                                                |
| application                                                                                        |
| battery  70 baud rate  113                                                                         |
| bit  113                                                                                           |
| block diagrams                                                                                     |
| 113 Boolean operators                                                                              |
| 113                                                                                                |
| branch  113                                                                                        |
| B                                                                                                  |

## C

| cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               | cables                                                               |
|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           | planning routes for DH485 connections  101                           |
| call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              | call for assistance  94                                              |
| common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          | common mode rejection ratio                                          |
| specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    | specification  84                                                    |
| communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        | communication connections  53                                        |
| communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       | communication options  communication protocols                       |
| 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   | 97                                                                   |
| DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 | DF1 Full-duplex  DF1 Half-duplex  98                                 |
| DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            | DH485  99                                                            |
| Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  | Modbus  104 communication scan  113                                  |
| communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    | communications toggle push button                                    |
| use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              | use  54                                                              |
| component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           | component descriptions  10                                           |
| 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      | 1762 expansion I/O  10 communication cables  11                      |
| memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    | memory module  10                                                    |
| real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  | real-time clock  10                                                  |
| configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             | configuration errors  93                                             |
| connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            | connect expansion I/O  24                                            |
| connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   | connect the system                                                   |
| AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    | AIC+  61 ,  64 54                                                    |
| DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 | DF1 Full-Duplex protocol  DF1 isolated point-to-point connection  55 |
| DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    | DH485 network  59                                                    |
| connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               | connect to DF1 Half-Duplex network  58                               |
| contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         | contactors (bulletin 100), surge suppressors                         |
| for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              | for  30                                                              |
| control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 | control profile  113                                                 |
| ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         | ControlFLASH                                                         |
| missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   | missing/corrupt OS LED pattern  96                                   |
| sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    | sequence of operation  96 use  95                                    |
| controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      | controller  113                                                      |
| ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           | ground  30                                                           |
| I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       | I/O wiring  40                                                       |
| LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       | LED status  89                                                       |
| LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      | LED status error conditions  90                                      |
| LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        | LED status normal operation  90 minimize electrical noise  40        |
| mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      | mount  20 mount on DIN rail  21                                      |
| mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           | mount on panel  22 mounting dimensions  20                           |
| prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           | prevent excessive heat  15                                           |
| controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             | controller overhead  113                                             |
| controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               | controller spacing  20                                               |
| counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     | counter  113 113                                                     |
| CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        | CPU (Central Processing Unit)                                        |
| D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    | D                                                                    |
| data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   | data table  113 53                                                   |
| default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  | default communication configuration                                  |

```
DF1 Full-Duplex protocol connect 54 , 55 DF1 Full-duplex protocol description 97 example system configuration 97 use a modem 55 using a modem 99 DF1 Half-Duplex protocol description 98 DH485 communication protocol configuration parameters 100 DH485 network configuration parameters 102 connect 59 devices that use the network 100 example system configuration 103 installation 59 planning considerations 101 DIN rail 113 disconnect main power 14 download 113 DTE (Data Terminal Equipment) 113 E Electronics Industries Association (EIA) ) 97 EMI 113 encoder 113 error recovery model 91 errors configuration 93 critical 92 extended error information field 93 hardware 93 module error field 92 non-critical 92 executing mode 114 expansion I/O 1762-IF2OF2 input type selection 47 1762-IF2OF2 output type selection 47 expansion I/O mount 24 expansion I/O wiring 40 1762-IA8 wiring diagram 40 1762-IF2OF2 wiring 48 1762-IF4 terminal block layout 50 1762-IQ16 wiring diagram 41 1762-IQ32T wiring diagram 42 1762-IQ8 wiring diagram 40 1762-IQ80W6 wiring diagram 46 1762-OA8 wiring diagram 42 1762-OB16 wiring diagram 43 1762-OB32T wiring diagram 44 1762-OB8 wiring diagram 43 1762-OV32T wiring diagram 44 1762-OW16 wiring diagram 45 1762-OW8 wiring diagram 45 1762-OX6I wiring diagram 46 analog wiring guidelines 47 extended error information field 93 F false 114 FIFO (First-In-First-Out) ) 114 file 114
```

Full-duplex

55

```
full-duplex 114 G general considerations 13 ground the controller 30 H Half-duplex 58 , 114 hard disk 114 hardware errors 93 hardware features 9 heat dissipation calculating 110 heat protection 15 high byte 114 I I/O (Inputs and Outputs) 114 input device 114 input states on power down 15 inrush current 114 install ControlFLASH software 95 memory module 19 install real-time clock 19 instruction 114 instruction set 114 isolated link coupler install 59 isolation transformers power considerations 15 J jump 114 L ladder logic 114 least significant bit (LSB) ) 114 LED (Light Emitting Diode) 114 LIFO (Last-In-First-Out) ) 114 logic 114 low byte 114 M master control relay 16 emergency-stop switches 16 using ANSI/CSA symbols schematic 18 using IEC symbols schematic 17 Master Control Relay (MCR) ) 114 master control relay circuit periodic tests 14
```

## memory module

data file protection 71 operation 70 program compare 70 program/data backup 70 removal/installation under power 71 write protection 71 minimize electrical noise 40 mnemonic 114 Modbus communication protocol 104 modem 114 modem cable construct your own 57 modems use with MicroLogix controllers 99 modes 115 module error field 92 motor starters (bulletin 509) surge suppressors 30 motor starters (bulletin 709) surge suppressors 30 mount expansion I/O 23 mount on DIN rail 23 N negative logic 115 network 115 nominal input current 115 normally closed 115 normally open 115 null modem cable 57 O offline 115 offset 115 off-state leakage current 115 one-shot 115 online 115 operating voltage 115 output device 115 P planning considerations for a network 101 power considerations input states on power down 15 isolation transformers 15 loss of power source 15 other line conditions 15 overview 15 power supply inrush 15 power distribution 14 power source loss of 15 power supply inrush power considerations 15

prepare for upgrade 95

prevent excessive heat 15

processor 115

processor file 115

program 11

program file 115 program mode 115 program scan 115 programming device 115 protocol 116 R read 116 real-time clock battery operation 70 disable 69 operation 69 removal/installation under power 69 write data 69 relay 116 relay logic 116 relays surge suppressors for 30 remote packet support 102 replacement parts 87 reserved bit 116 restore 116 retentive data 116 RS-232 116 RS-232 communication interface 97 run mode 116 rung 116 S safety circuits 14 safety considerations 13 disconnect main power 14 hazardous location 13 master control relay circuit periodic tests 14 periodic tests of master control relay circuit 14 power distribution 14 safety circuits 14 save 116 scan time 116 sinking 116 sinking and sourcing wiring diagrams 34 sinking wiring diagram 1762-24BWA 35 sourcing 116 sourcing wiring diagram 1762-24BWA 36 status 116 surge suppressors for contactor 30 for motor starters 30 for relays 30 recommended 30 use 29 system configuration DF1 Full-duplex examples 97 DH485 connection examples 103

## system loading

calculations 105

example calculations worksheet 107

105

system loading and heat dissipation 105

## T

terminal 116

## terminal block layouts

1762-IF2OF2 48

1762-IF4 50 controllers 31 terminal groupings terminal groupings 33

throughput 116

Trimpot Information Function File 67

trimpot operation 67

trimpots 67

adjustment 67 error conditions 67 location 67

troubleshoot your system 89

true 116

## U

upload 116 use communications toggle push button 54 use emergency-stop switches 16 use memory modules 69 use real-time clock 69 use trimpots 67

## W

wire your controller 27

33

## wiring diagram

1762-IA8 40

1762-IF2OF2 differential sensor 48

1762-IF2OF2 single-ended sensor 49

1762-IQ16 41

1762-IQ32T 42

1762-IQ8 40

1762-IQ80W6 46

1762-L24AWA input 35

1762-L24AWA output 37

1762-L24BWA output 37

1762-L24BWA sinking 35

1762-L24BWA sourcing 36

1762-L24BXB output 37

1762-L24BXB sinking 36

1762-L24BXB sourcing 36

1762-L40AWA input 37

1762-L40AWA output 39

1762-L40BWA output 39

1762-L40BWA sourcing 38

1762-L40BXB output 39

1762-L40BXB sinking 38

1762-L40BXB sourcing 39

1762-OA8 42

1762-OB16 43

1762-OB32T 44

1762-OB8 43

1762-OV32T 44

1762-OW16 45

1762-OW8 45

1762-OX6I 46

terminal block layouts 31 , 48 , 50

wiring diagrams 31

workspace 116

write 116

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

Allen-Bradley, ControlFLASH, DH+, DTAM Micro, DTAM Plus, expanding human possibility, FactoryTalk, MicroLogix, PanelView, PLC-5, Rockwell Automation, RSLinx, RSLogix 500, SLC, SLC 5/03, SLC 500, and TechConnect are trademarks of Rockwell Automation, Inc.

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