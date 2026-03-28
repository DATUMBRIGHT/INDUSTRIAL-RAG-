<!-- image -->

## POINT I/O Digital and Analog Modules and POINTBlock I/O Modules

Catalog Numbers 1734-IA2, 1734-IA4, 1734-IA4K, 1734-IB2, 1734-IB4, 1734-IB4K, 1734-IB8, 1734-IB8K,

1734-IB4D, 1734-IM2, 1734-IM4, 1734-IV2, 1734-IV4, 1734-IV8, 1734-IV8K, 1734-OA2, 1734-OA4,

1734-OA4K, 1734-OB2, 1734-OB2EP, 1734-OB2E, 1734-OB4, 1734-OB4K, 1734-OB4E, 1734-OB8,

1734-OB8K, 1734-OB8E, 1734-OB8EK, 1734-OV2E, 1734-OV4E, 1734-OV8E, 1734-OV8EK, 1734-OW2,

1734-OW4, 1734-OW4K, 1734-OX2, 1734-IE2C, 1734-IE2CK, 1734-IE2V, 1734-OE2C, 1734-OE2CK,

1734-OE2V, 1734-OE2VK, 1734D-IA16, 1734D-IA8XOA8, 1734D-IA8XOW8, 1734D-IB16, 1734D-IB8XOB8E, 1734D-IB8XOW8

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

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

## Table of Contents

|                                 | Preface                                                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|                                 | About This Publication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7     |
|                                 | Who Should Use This Manual. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7            |
|                                 | Summary of Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7       |
|                                 | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8     |
|                                 | Chapter 1                                                                                                                                |
| About the Modules               | Digital Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 |
|                                 | Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |
|                                 | Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12          |
|                                 | Relay Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12              |
|                                 | Analog Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13  |
|                                 | Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13         |
|                                 | Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14          |
|                                 | Specialty Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14   |
|                                 | Power Supplies, Wiring Base Assemblies, and Miscellaneous Modules . . . . . . . . . . . . . 14                                           |
|                                 | Secure Access to the System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14             |
|                                 | Chapter 2                                                                                                                                |
| Configure POINT I/O Modules     | Use the Help Button . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17     |
| Using Studio 5000 Logix         | Configure Digital Modules . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17       |
| Designer Application            | About Fault/Program Action and Configuration Dialogs . . . . . . . . . . . . . . . . . . . . . 19                                        |
|                                 | Understand Data and Connection Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19                                |
|                                 | Understand Transition to Hard Run Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                                |
|                                 | Work with Dialogs for Digital Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20                             |
|                                 | Work with Dialogs for Digital Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                              |
|                                 | Configure Analog Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24          |
|                                 | Understand Data and Connection Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                                |
|                                 | Work with Dialogs for Analog Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25                              |
|                                 | Work with Dialogs for Analog Output Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                                |
|                                 | Chapter 3                                                                                                                                |
| Configure POINT I/O Modules for | Commissioning a Node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35          |
| DeviceNet Networks              | Using the RSNetWorx Commissioning Tool . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                                |
|                                 | Use Sequential Auto Addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                      |
|                                 | Using Third-party Configuration Software. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                             |
|                                 | Configure Digital Modules Using RSNetWorx Software . . . . . . . . . . . . . . . . . . . . . . . . . . 36                                |
|                                 | Configure Analog Modules Using RSNetWorx Software . . . . . . . . . . . . . . . . . . . . . . . . . . 47                                 |
|                                 | Chapter 4                                                                                                                                |
| POINT I/O Module Data           | Digital Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53     |
|                                 | Digital DC Input Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53               |
|                                 | Digital AC Input Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55               |
|                                 | Digital Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55      |

Calibrate Your Analog Modules

Troubleshoot with the

Indicators

| Digital DC Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                |
|-----------------------------------------------------------------------------------------------------------------------------------------|
| Digital AC Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                |
| Relay Output Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57     |
| Analog Input Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58     |
| Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58 |
| Communicate with Your Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                       |
| Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59  |
| Channel Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59         |
| Latch Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60       |
| Alarm Disable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60       |
| Calibration Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60         |
| Digital Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61   |
| Update Rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61      |
| Notch Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61     |
| Alarms. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61  |
| Range Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62       |
| Channel Indicator Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62                 |
| Analog Output Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62       |
| Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 |
| Operational Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63            |
| Scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64  |
| Fault and Idle/Program Mode Action . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                         |
| Channel Status . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64         |
| Low and High Clamps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65              |
| Latch Alarms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65       |
| Alarm Disable. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65       |
| Channel Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66           |
| POINTBlock I/O Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66        |
| Chapter 5                                                                                                                               |
| Tools Required to Calibrate Your Analog Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                          |
| Calibrate the Analog Current Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72                    |
| Calibrate the Analog Current Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                     |
| Calibrate the Analog Voltage Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                    |
| Calibrate the Analog Voltage Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                     |
| Chapter 6                                                                                                                               |
| About Module Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87         |
| Network and Module Status Indications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88                    |
| Troubleshoot Digital Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89           |
| 1734-IB2, 1734-IB4, 1734-IB4K, 1734-IB8, 1734-IB8K Sink Input Module . . . . . . . . . . 89                                             |
| 1734-IB4D Sink Input Module with Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                               |
| 1734-OB2E, 1734-OB4E, 1734-OB8E, 1734-OB8EK Source Output Modules . . . . . . . . 90                                                    |
| 1734-OB2, 1734-OB4, 1734-OB4K, 1734-OB8, 1734-OB8K Source Output Modules . . 90                                                         |
| 1734-OB2EP Protected Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91                           |
| 1734-IV2, 1734-IV4, 1734-IV8, 1734-IV8K Source Input Module . . . . . . . . . . . . . . . . . 91                                        |
| 1734-OV2E, 1734-OV4E, 1734-OV8E, 1734-OV8EK Protected Sink Output Module . . 92                                                         |
| 1734-OW2, 1734-OW4, 1734-OW4K Relay Output Module . . . . . . . . . . . . . . . . . . . . . . 92                                        |
| 1734-OX2 Relay Output Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93                    |

|                   | 1734-IA2, 1734-IA4, 1734-IA4K 120V AC Input Module . . . . . . . . . . . . . . . . . . . . . . . . . 93                                                        |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | 1734-OA2, 1734-OA4, 1734-OA4K 120/220V AC Output Module . . . . . . . . . . . . . . . . . . 94                                                                 |
|                   | 1734-IM2, 1734-IM4 220V AC Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94                                                   |
|                   | Troubleshoot Analog Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95                                   |
|                   | 1734-IE2C, 1734-IE2CK Analog Current Input Module. . . . . . . . . . . . . . . . . . . . . . . . . 95                                                          |
|                   | 1734-OE2C, 1734-OE2CK Analog Current Output Module . . . . . . . . . . . . . . . . . . . . . . 95                                                              |
|                   | 1734-IE2V, 1734-IE2VK Analog Voltage Input Module . . . . . . . . . . . . . . . . . . . . . . . . . 96                                                         |
|                   | 1734-OE2V, 1734-OE2VK Analog Voltage Output Module . . . . . . . . . . . . . . . . . . . . . . 97                                                              |
|                   | Troubleshoot I/O Communication Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97                                              |
|                   | 1734-PDN DeviceNet Communication Interface Module . . . . . . . . . . . . . . . . . . . . . . 97                                                               |
|                   | 1734-ADN, 1734-ADNX DeviceNet Adapter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98                                                    |
|                   | 1734-ACNR ControlNet Adapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100                                             |
|                   | 1734-APB PROFIBUS Adapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102                                            |
|                   | 1734-AENT EtherNet/IP Adapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103                                              |
|                   | Appendix A                                                                                                                                                     |
| Default Data Maps | Digital Module Default Data Maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                                     |
|                   | 1734-IB2 Sink Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105                                         |
|                   | 1734-IB4, 1734-IB4K Sink Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                                |
|                   | 1734-IB8, 1734-IB8K Sink Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                                |
|                   | 1734-IB4D Sink Input Module with Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106                                                       |
|                   | 1734-IV2 Source Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                           |
|                   | 1734-IV4 Source Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                           |
|                   | 1734-IV8, 1734-IV8K Source Input Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                                   |
|                   | 1734-IA2 Input Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                     |
|                   | 1734-IA4, 1734-IA4K Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107                                             |
|                   | 1734-IM2 Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                                      |
|                   | 1734-IM4 Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                                      |
|                   | 1734-OA2 Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                                       |
|                   | 1734-OA4, 1734-OA4K Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108                                                |
|                   | 1734-OB2E, 1734-OB2 Electronically Protected Output Module. . . . . . . . . . . . . . . . 108                                                                  |
|                   | 1734-OB4E, 1734-OB4, 1734-OB4K Electronically Protected Output Module . . . . . 109 1734-OB8E, 1734-OB8EK, 1734-OB8, 1734-OB8K Electronically Protected Output |
|                   | Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109                           |
|                   | 1734-OB2EP Protected Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                                                   |
|                   | 1734-OV2E Output Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                                         |
|                   | 1734-OV4E Output Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                                         |
|                   | 1734-OV8E, 1734-OV8EK Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                                                    |
|                   | 1734-OW2 Relay Sink/Source Output Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                                                     |
|                   | 1734-OW4, 1734-OW4K Relay Sink/Source Output Module . . . . . . . . . . . . . . . . . . . . 111                                                                |
|                   | 1734-OX2 Relay Output Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                                          |
|                   | Analog Module Default Data Maps. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111                                     |
|                   | 1734-IE2C, 1734-IE2CK Analog Current Input Module. . . . . . . . . . . . . . . . . . . . . . . . . 111                                                         |
|                   | 1734-IE2V Analog Voltage Input Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112                                                  |
|                   | 1734-OE2C, 1734-OE2CK Analog Current Output Module . . . . . . . . . . . . . . . . . . . . . 112                                                               |

|                     | Appendix B                                                                                                                          |         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------|
| Mounting Dimensions | POINT I/O Module with a 1734-ADN, 1734-ACNR, 1734-AENT, or 1734-APB Adapter. . . . 113                                              |         |
|                     | POINT I/O Module with a 1734-PDN Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114                   |         |
|                     | POINTBlock Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115 |         |
|                     | Index                                                                                                                               |         |
|                     |                                                                                                                                     | . . 117 |
|                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     |         |

## About This Publication

## Who Should Use This Manual

## Summary of Changes

This manual describes how to configure, calibrate, and troubleshoot your POINT I/O™ modules.

The POINT I/O modules in this manual are DeviceNet® ready. Each module can exist on the DeviceNet network as one of the following:

- As an individual node
- With an adapter (catalog number 1734-ADN or 1734-ADNX) as a single node

When you use these POINT I/O modules with an adapter, use this manual with the user manual of the adapter which you are using. See Table 1 for user manual reference of your adapter.

Table 1 - Adapter User Manual Reference Based On Network Type You Use

| When You Use POINT I/O Modules on This Network     |                    | See the User Manual for Catalog Number Publication Number   |
|----------------------------------------------------|--------------------|-------------------------------------------------------------|
| DeviceNet network DeviceNet adapter                | 1734-ADN 1734-ADNX | 1734-UM002                                                  |
| ControlNet® network ControlNet adapter 1734-ACNR   |                    | 1734-UM008                                                  |
| EtherNet/IP™ network EtherNet/IP adapter 1734-AENT |                    | 1734-UM011                                                  |
| EtherNet/IP network EtherNet/IP adapter 1734-AENTR |                    | 1734-UM017                                                  |
| PROFIBUS network PROFIBUS adapter 1734-APB         |                    | 1734-UM005                                                  |

For applications that use these modules in a network with a 1734-PDN DeviceNet communication interface, or a 1734D-xx POINTBlock I/O module, this user manual is the primary documentation.

This manual is intended for qualified personnel. We assume that:

- You know how to use the software RSNetWorx™ for DeviceNet and Studio 5000 Logix Designer® application (1) for ControlNet and EtherNet/IP networks or similar configuration software to set up and calibrate these modules.
- You have the capability to download and use electronic data sheet (EDS) files.

If you do not qualify, see your software documentation or online help before attempting to use these modules.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

™

| Topic  Page                                                                     |
|---------------------------------------------------------------------------------|
| Updated template Throughout                                                     |
| Added Inclusive Language acknowledgment  Important User Info                    |
| Added catalog numbers that ends with letter K Throughout                        |
| Updated Additional Resources 8                                                  |
| Added topic Secure Access to the System 14 and 15                               |
| Removed chapters Install POINT I/O Modules and Install POINTBlock I/O Modules — |

## Additional Resources

## Additional Resources

| Resource Description                                                                                             |                                                                                             |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Analog Modules                                                                                                   |                                                                                             |
| POINT I/O 2 Current and 2 Voltage Input Analog Modules Installation Instructions, publication 1734-IN027         | Provides installation information for 2 current and 2 voltage input analog modules.         |
| POINT I/O 2 Current Output and 2 Voltage Output Analog Modules Installation Instructions, publication 1734-IN002 | Provides installation information for 2 current output and 2 voltage output analog modules. |
| Communication Devices                                                                                            |                                                                                             |
| POINT I/O ControlNet Adapter Installation Instructions, publication 1734-IN582                                   | Provides installation information for ControlNet adapters.                                  |
| POINT I/O ControlNet Adapter User Manual, publication 1734-UM008                                                 | Describes how to configure and troubleshoot your ControlNet adapters.                       |
| POINT I/O DeviceNet Communication Interface Module Installation Instructions, publication 1734-IN057             | Provides installation information for DeviceNet communication interface modules.            |
| POINT I/O DeviceNet Adapter Installation Instructions, publication 1734-IN026                                    | Provides installation information for DeviceNet adapters.                                   |
| POINT I/O DeviceNet Adapter User Manual, publication 1734-UM002                                                  | Describes how to install, configure, and troubleshoot your DeviceNet adapters.              |
| POINT I/O EtherNet/IP Adapter Installation Instructions, publication 1734-IN590                                  | Provides installation information for EtherNet/IP adapters.                                 |
| POINT I/O EtherNet/IP Adapter User Manual, publication 1734-UM011                                                | Describes how to install, configure, and troubleshoot your EtherNet/IP adapters.            |
| POINT I/O and ArmorPOINT I/O Dual-port EtherNet/IP Adapters User Manual, publication 1734-UM017                  | Describes how to configure and troubleshoot your dual-port EtherNet/IP adapters.            |
| POINT I/O PROFIBUS Adapter Installation Instructions, publication 1734-IN014                                     | Provides installation information for PROFIBUS adapters.                                    |
| POINT I/O PROFIBUS Adapter Module User Manual, publication 1734-UM005                                            | Describes how to install, configure, and troubleshoot your PROFIBUS adapters.               |
| POINT I/O Dual Port EtherNet/IP Adapter Installation Instructions, publication 1734-IN041                        | Provides installation information for dual port EtherNet/IP adapter.                        |
| POINT I/O EtherNet/IP Adapter Installation Instructions, publication 1734-IN042                                  | Provides installation information for EtherNet/IP adapter.                                  |
| Digital AC Input Modules                                                                                         |                                                                                             |
| POINT I/O 220V AC Input Modules Installation Instructions, publication 1734-IN008                                | Provides installation information for 220V AC input modules.                                |
| POINT I/O 120V AC Input Modules Installation Instructions, publication 1734-IN010                                | Provides installation information for 120V AC input modules.                                |
| Digital AC Output Modules                                                                                        |                                                                                             |
| POINT I/O 120V and 220V AC Output Modules Installation Instructions, publication 1734-IN009                      | Provides installation information for 120V and 220V AC output modules.                      |
| Digital DC Input Modules                                                                                         |                                                                                             |
| POINT I/O Input Modules Installation Instructions, publication 1734-IN051                                        | Provides installation information for DC input modules.                                     |
| POINT I/O Source Input Modules Installation Instructions, publication 1734-IN052                                 | Provides installation information for source input modules.                                 |
| Digital DC Output Modules                                                                                        |                                                                                             |
| POINT I/O Protected Output Module Installation Instructions, publication 1734-IN586                              | Provides installation information for the protected output module.                          |
| POINT I/O Protected Sink Output Modules Installation Instructions, publication 1734-IN585                        | Provides installation information for protected sink output modules.                        |
| POINT I/O Protected Output Module Installation Instructions, publication 1734-IN056                              | Provides installation information for the protected source output module.                   |
| POINT I/O Output Modules Installation Instructions, publication 1734-IN018                                       | Provides installation information for source output modules.                                |
| POINTBlock Modules                                                                                               |                                                                                             |
| POINTBlock AC 8 Input/8 Output Module Installation Instructions, publication 1734-IN022                          | Provides installation information for AC 8 input/8 output module.                           |
| POINTBlock AC 8 Input/8 Relay Output Module Installation Instructions, publication 1734-IN023                    | Provides installation information for AC 8 input/8 relay output module.                     |
| POINTBlock DC 8 Input/8 Output Module Installation Instructions, publication 1734-IN020                          | Provides installation information for DC 8 input/8 output module.                           |
| POINTBlock DC 8 Input/8 Relay Output Module Installation Instructions, publication 1734-IN021                    | Provides installation information for DC 8 input/8 relay output module.                     |
| POINTBlock AC 16 Input Module Installation Instructions, publication 1734D-IN001                                 | Provides installation information for AC 16 input module.                                   |
| POINTBlock DC 16 Input Module Installation Instructions, publication 1734D-IN002                                 | Provides installation information for DC 16 input module.                                   |
| Relay Modules                                                                                                    |                                                                                             |
| POINT I/O 2 and 4 Relay Output Modules Installation Instructions, publication 1734-IN055                         | Provides installation information for 2 and 4 relay output modules.                         |
| POINT I/O 2 Relay Output Module Installation Instructions, publication 1734-IN587                                | Provides installation information for 2 relay output module.                                |

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

## Additional Resources (Continued)

|                                                                                                                                                      | Resource Description                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Specialty Modules                                                                                                                                    |                                                                                                                                                                                                                                                                                 |
| POINT I/O 5V and 24V Encoder/Counter Modules Installation Instructions, publication 1734-IN005                                                       | Provides installation information for 5V and 24V encoder/counter modules.                                                                                                                                                                                                       |
| POINT I/O Encoder/Counter Modules User Manual, publication 1734-UM006                                                                                | Describes how to configure and troubleshoot your encoder/counter modules.                                                                                                                                                                                                       |
| POINT I/O 5V DC and 24V DC Very High Speed Counter Module Installation Instructions, publication 1734-IN003                                          | Provides installation information for 5V DC and 24V DC very high speed counter module.                                                                                                                                                                                          |
| POINT I/O Very High-speed Counter Modules User Manual, publication 1734-UM003                                                                        | Describes how to use, configure, and troubleshoot your very high-speed counter modules.                                                                                                                                                                                         |
| POINT I/O Address Reserve Module Installation Instructions, publication 1734-IN019                                                                   | Provides installation information for the address reserve module.                                                                                                                                                                                                               |
| POINT I/O RS-232 and RS-485 ASCII Modules Installation Instructions, publication 1734-IN588                                                          | Provides installation information for RS-232 and RS-485 ASCII modules.                                                                                                                                                                                                          |
| POINT I/O ASCII Modules User Manual, publication 1734-UM009                                                                                          | Describes how to use, configure, and troubleshoot your modules.                                                                                                                                                                                                                 |
| POINT I/O RTD and Isolated Thermocouple Input Modules Installation Instructions, publication 1734-IN011                                              | Provides installation information for RTD and isolated thermocouple input modules.                                                                                                                                                                                              |
| POINT I/O Thermocouple and RTD Modules User Manual, publication 1734-UM004                                                                           | Describes how to use, configure, and troubleshoot your modules.                                                                                                                                                                                                                 |
| POINT I/O Synchronous Serial Interface Absolute Encoder Module Installation Instructions, publication 1734-IN581                                     | Provides installation information for synchronous serial interface encoder modules                                                                                                                                                                                              |
| POINT I/O Synchronous Serial Interface Absolute Encoder Module User Manual, publication 1734-UM007                                                   | Describes how to use, configure, and troubleshoot your modules.                                                                                                                                                                                                                 |
| Power Supplies, Wiring Base Assemblies, and Miscellaneous                                                                                            |                                                                                                                                                                                                                                                                                 |
| POINT I/O Cold Junction Compensation Wiring Base Assembly Installation Instructions, publication 1734-IN583                                          | Provides installation information for cold junction compensation wiring base assembly.                                                                                                                                                                                          |
| POINT I/O Field Potential Distributor Module Installation Instructions, publication 1734-IN059                                                       | Provides installation information for field potential distributor module.                                                                                                                                                                                                       |
| POINT I/O 24V DC Expansion Power Supply Installation Instructions, publication 1734-IN058                                                            | Provides installation information for 24V DC expansion power supply modules.                                                                                                                                                                                                    |
| POINT I/O 120/240V AC Expansion Power Supply Installation Instructions, publication 1734-IN017                                                       | Provides installation information for I/O 120/240V AC expansion power supply modules.                                                                                                                                                                                           |
| POINT I/O Common Terminal Module and Voltage Terminal Module Installation Instructions, publication 1734-IN024                                       | Provides installation information for common terminal module and voltage terminal module.                                                                                                                                                                                       |
| POINT I/O Wiring Base Assembly Installation Instructions, publication 1734-IN511                                                                     | Provides installation information for wiring base assemblies 1734-TB and 1734-TBS.                                                                                                                                                                                              |
| POINT I/O Wiring Base Assembly Installation Instructions, publication 1734-IN013                                                                     | Provides installation information for wiring base assemblies 1734-TB3, 1734-TB3S, 1734-RTB, 1734-RTBS, 1734-RTB3, and 1734-RTB3S.                                                                                                                                               |
| POINT I/O One-piece Terminal Bases Installation Instructions, publication 1734-IN028 Provides installation information for one-piece terminal bases. |                                                                                                                                                                                                                                                                                 |
| General                                                                                                                                              |                                                                                                                                                                                                                                                                                 |
| Ethernet Reference Manual, publication ENET-RM002                                                                                                    | Describes basic Ethernet concepts, infrastructure components, and infrastructure features.                                                                                                                                                                                      |
| System Security Design Guidelines Reference Manual, publication SECURE-RM001                                                                         | Provides guidance on how to conduct security assessments, implement Rockwell Automation products in a secure system, harden the control system, manage user access, and dispose of equipment.                                                                                   |
| Industrial Components Preventive Maintenance, Enclosures, and Contact Ratings Specifications, publication IC-TD002                                   | Provides a quick reference tool for Allen-Bradley industrial automation controls and assemblies.                                                                                                                                                                                |
| Safety Guidelines for the Application, Installation, and Maintenance of Solid-state Control, publication SGI-1.1                                     | Designed to harmonize with NEMA Standards Publication No. ICS 1.1-1987 and provides general guidelines for the application, installation, and maintenance of solid-state control in the form of individual devices or packaged assemblies incorporating solid-state components. |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                                                          | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                                                             |
| Product Certifications website, rok.auto/certifications                                                                                              | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                                                             |

## Notes:

## Digital Modules

## About the Modules

This chapter introduces the following POINT I/O and related modules:

- Digital modules
- Relay output modules
- Analog modules
- Specialty modules
- Power supplies, wiring base assemblies, and miscellaneous modules

Table 2 - POINT I/O Digital Modules

| Digital Module Description Catalog Number                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| 2, 4, and 8 sink input modules  1734-IB2, 1734-IB4, 1734-IB4K, 1734-IB8, 1734-IB8K, 1734-IB4D                                               |
| 2, 4, and 8 source input modules 1734-IV2, 1734-IV4, 1734-IV8, 1734-IV8K                                                                    |
| 2, 4, and 8 sink output modules 1734-OV2E, 1734-OV4E, 1734-OV8E, 1734-OV8EK                                                                 |
| 2, 4, and 8 protected source output modules 1734-OB2, 1734-OB4, 1734-OB4K, 1734-OB8, 1734-OB8K, 1734-OB2E, 1734-OB4E, 1734-OB8E, 1734-OB8EK |
| 2 protected source output modules 1734-OB2EP                                                                                                |
| 2 and 4 relay output modules 1734-OW2, 1734-OW4, 1734-OW4K                                                                                  |
| 2 relay output modules 1734-OX2                                                                                                             |
| 2 and 4 120/220V AC output modules 1734-OA2, 1734-OA4, 1734-OA4K                                                                            |
| 2 and 4 120V AC input modules 1734-IA2, 1734-IA4, 1734-IA4K                                                                                 |
| 2 and 4 220V AC input modules 1734-IM2, 1734-IM4                                                                                            |

Table 3 - POINTBlock Modules

| POINTBlock Module Description Catalog Number                       |
|--------------------------------------------------------------------|
| 8 AC input and 8 AC output modules 1734D-IA8XOA8, 1734-IA8XOA8S    |
| 8 AC input and 8 relay output modules 1734D-IA8XOW8, 1734-IA8XOW8S |
| 8 DC input and 8 DC output modules 1734D-IB8XOB8E, 1734-IB8XOB8ES  |
| 8 DC input and 8 relay output modules 1734D-IB8XOW8, 1734-IB8XOW8S |
| 16 AC input modules 1734D-IA16, 1734-IA16S                         |
| 16 DC input modules 1734D-IB16, 1734-IB16S                         |

## Input Modules

For DC input modules, the DC inputs are 24V DC nominal with an input range of 10…28.8V DC, and are offered with 2, 4, or 8 sinking/sourcing style inputs.

- Sinking input modules - 1734-IB2, 1734-IB4, 1734-IB4D, and 1734-IB8
- Sourcing input modules - 1734-IV2, 1734-IV4, and 1734-IV8

For AC input modules, the AC inputs are 120V AC nominal with an input range of 85…132V AC, or 220V AC nominal with an input range of 159…264V AC, and offered with sinking inputs.

The features of all input modules are as follows:

- Autobaud (matches the communication rate of existing devices on the network)
- Selectable input filter times (0…65 ms with 1 ms default)
- Sequential auto addressing

<!-- image -->

## Output Modules

The 1734-OB2, 1734-OB4, 1734-OB8, 1734-OB2E, 1734-OB4E, and 1734-OB8E DC output modules have current limited sourcing outputs, which source a positive voltage of up to 1 A with respect to their DC return per channel. The 1734-OB2EP sources a positive voltage of up to 2 A with respect to its DC return per channel. The outputs are not isolated from each other. For these modules, DC outputs are 24V DC nominal, with a range of 10…28.8V DC. A number of output diagnostic features are incorporated to assist in troubleshooting .

The features of 1734-OB2E, 1734-OB2EP, 1734-OB4E, and 1734-OB8E modules are:

- Output diagnostics (short circuit and wire-off indication and reporting bits per channel)
- Current limited outputs
- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

The 1734-OV2E, 1734-OV4E, and 1734-OV8E modules are protected sink output modules protected to 1 A. The outputs are not isolated from each other. For these modules, DC outputs are 24V DC nominal, with a range of 10…28.8V DC. A number of output diagnostic features are incorporated to assist in troubleshooting . The 1734-OV2E, 1734-OV4E, and 1734-OV8E modules have no wire-off indication.

The features of 1734-OV2E, 1734-OV4E, and 1734-OV8E modules are:

- Output diagnostics (short circuit and reporting bits per channel)
- Current limited outputs
- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

The 1734-OA2 and 1734-OA4 AC output modules have sourcing outputs, which source a voltage of up to 0.75 A per channel. The outputs are not isolated from each other. For this module, AC outputs are 120/220V AC nominal, with a range of 74…264V AC.

The features of 1734-OA2 and 1734-OA4 modules are:

- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

## Relay Output Modules

The two versions of relay modules are:

- 1734-OW2 and 1734-OW4 relay module
- 1734-OX2 relay module

The 1734-OW2 and 1734-OW4 relay outputs are Type A (Normally Open), the 1734-OX2 relay outputs are Type 2 Form C. Both modules outputs sink or source current with respect to power or return. Contact outputs are isolated from each other. Each output is rated 5…240V rms at 2 A (current is load-dependent).

The features of these modules are:

- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

## Analog Modules

The 1734 analog modules consist of input modules (1734-IE2C and 1734-IE2V) and output modules (1734-OE2C and 1734-OE2V). Each module has two single-ended, non-isolated channels.

| Catalog Number Module Type   | Number of Channels  Resolution                             |
|------------------------------|------------------------------------------------------------|
| 1734-IE2C, 1734-IE2CK        | Analog Input 2 16 bits across 0…21 mA                      |
|                              | 1734-IE2V Analog Input 2 15 bits plus sign across -10…+10V |
| 1734-OE2C, 1734-OE2CK        | Analog Output 2 13 bits across 0…21 mA                     |
| 1734-OE2V, 1734-OE2VK        | Analog Output 2 14 bits across -10…+10V                    |

The features of the analog modules depend on the type of analog module (input or output). The features that are common to both input and output modules are:

- Data - The current input and output modules operate in unipolar mode only. The voltage input and output modules operate in unipolar or bipolar modes. You can scale the data returned from the module to any 16 bit signed integer (–32,768…+32,767). Input modules produce 6 bytes of data:
- Channel 0 Data (2 bytes)
- Channel 1 Data (2 bytes)
- Channel 0 Status (1 byte)
- Channel 1 Status (1 byte)

Output modules consume 4 bytes of data:

- Channel 0 Data (2 bytes)
- Channel 1 Data (2 bytes)

Output modules produce 2 bytes of data:

- Channel 0 Status (1 byte)
- Channel 1 Status (1 byte)
- Operational modes (current and voltage)
- Current - Two modes
- 0…20 mA
- 4…20 mA (default mode)
- Voltage - Two modes
- 0…10V (default mode)
- -10…+10V
- Individually set channel mode
- Scaling - Conversion to engineering units

## Input Modules

The following features are available in the input modules:

- Latching alarms, when set, latch low and high-alarm status information. Available alarms include:
- Low
- Low Low
- High
- High High
- Disable alarms - Disables all channel alarms and faults so they are not reported in the channel status field. Four different alarms are available.
- Settable update rate determines how often an input channel is scanned.

## Specialty Modules

## Power Supplies, Wiring Base Assemblies, and Miscellaneous Modules

## Secure Access to the System

- Notch filter is selectable for both inputs (50 Hz, 60 Hz, 250 Hz, and 500 Hz).
- Digital filter sets a time constant.

## Output Modules

The following features are available in the output modules:

- Latching alarms, when set, latch low and high clamp alarm status information.
- Low and high clamps can be set individually or on a channel basis. When the output value reaches clamp value, a status bit is set, indicating the output is clamped.
- Disable alarms - Disables all channel alarms and faults so that they are not reported in the channel status field.
- Fault and Idle mode action let you select what happens to the output if a fault occurs or if the module is in Idle mode. The choices are the following:
- Hold Last State
- Low Clamp
- High Clamp
- User-defined value

For more information about the following POINT I/O specialty modules, see the installation instructions and user manuals listed in Additional Resources on page 8 .

| Module Description Catalog Number                        |
|----------------------------------------------------------|
| 5V Encoder/Counter Module 1734-IJ                        |
| 24V Encoder/Counter Module 1734-IK                       |
| 24V Very High-speed Counter Module 1734-VHSC24           |
| 5V Very High-speed Counter Module 1734-VHSC5             |
| ASCII RS-232 and RS-485 Modules 1734-232ASC, 1734-485ASC |
| Isolated Thermocouple Input Module 1734-IT2I             |
| RTD Input Modules 1734-IR2, 1734-IR2E                    |
| Synchronous Serial Interface Encoder Module 1734-SSI     |

For more information about the following modules, see the installation instructions and user manuals listed in Additional Resources on page 8 .

| Module Description Catalog Number                                                                          |
|------------------------------------------------------------------------------------------------------------|
| Cold Junction Wiring Base Assembly 1734-TBCJC                                                              |
| Field Potential Distributor 1734-FPD                                                                       |
| POINT I/O 24V DC Expansion Power Supply 1734-EP24DC                                                        |
| POINT I/O Common Terminal Module 1734-CTM                                                                  |
| POINT I/O Voltage Terminal Module 1734-VTM                                                                 |
| Wiring Base Assemblies  1734-TB, 1734-TBS, 1734-TB3, 1734-TB3S, 1734-TOP, 1734-TOPS, 1734-TOP3, 1734-TOP3S |
| Address Reserve Module 1734-ARM                                                                            |

To secure access to a Logix 5000 controller and POINT I/O digital and analog modules by authorized users only, consider the following options:

- Follow the guidelines provided in the System Security Design Guidelines Reference Manual, publication SECURE-RM001 .
- Password protect the source and execution of the control program.
- Deploy EtherNet/IP devices in accordance with recommended architectures and concepts. See the Converged Plantwide Ethernet (CPwE) Design and Implementation Guide, publication ENET-TD001 .
- Implement physical barriers, such as locked cabinets.

To secure access to the system, consider the following options:

- Follow industry best practices to harden your PCs and servers, including antivirus/ antimalware and application allow list solutions.
- The recommendations are published at the Rockwell Automation technical support center in Knowledgebase article. See Rockwell Automation Customer Hardening Guidelines, Answer ID 546987. To access technical support center, go to rok.auto/ knowledgebase .
- Develop and deploy backup and disaster recovery policies and procedures. Test backups on a regular schedule.
- Minimize network exposure for all control system devices and systems, and make sure that they are not accessible from the Internet.
- Locate control system networks and devices behind firewalls and isolate them from the business network.
- Subscribe to Knowledgebase article Industrial Security Advisory Index, Answer ID 54102 at the Rockwell Automation technical support center so you have access to information about security matters that affect Rockwell Automation products. To access technical support center, go to rok.auto/knowledgebase .

## Notes:

## Use the Help Button

## Configure Digital Modules

<!-- image -->

## Configure POINT I/O Modules Using Studio 5000 Logix Designer Application

This chapter covers the instructions about how to configure digital and analog POINT I/O modules, using Studio 5000 Logix Designer application with one of the following:

- ControlNet network using a 1734-ACNR adapter
- EtherNet/IP network using a 1734-AENT adapter

The screen captures used in the procedure are for RSLogix 5000 software and it may not be exactly the same for Studio 5000 Logix Designer application.

From the dialogs you use to configure the digital and analog POINT I/O modules, select Help at the bottom of the dialog for information about how to complete entries on the dialogs.

From a warning dialog, select Help at the bottom of the dialog to get information about that specific error.

To configure POINT I/O digital modules in Studio 5000 Logix Designer application, using a ControlNet or EtherNet/IP network, proceed as follows:

1. Configure your adapter, referring to the user manual for your 1734-AENT adapter for EtherNet/IP networks or 1734-ACNR adapter for ControlNet networks with information on how to select a controller and communication module.
2. Add a digital module according to the instructions in your 1734-AENT or 1734-ACNR adapter user manual.

As an example, if you add 1734-OB2E, the New Module dialog appears.

<!-- image -->

3. Select the Connection tab at the top of the dialog.
4. Leave the following options unchecked:
- Inhibit Module
- Major Fault On Controller If Connection Fails While in Run Mode
5. Complete the entry for Requested Packet Interval (RPI) as per the following table, if the field is selectable:
6. Select the Module Info tab to see the module identification and status information.
7. See the section About Fault/Program Action and Configuration Dialogs for information about the following tabs and dialogs, which you can see based on the module you have added:
- Fault/Program Action
- Configuration

<!-- image -->

<!-- image -->

<!-- image -->

## About Fault/Program Action and Configuration Dialogs

You can see Fault/Program Action and Configuration dialogs based on the module and connection types. See the following table:

|        | For Module Type With Connection Type   | You See These Tabs(1)              | You See These Tabs(1)   |
|--------|----------------------------------------|------------------------------------|-------------------------|
|        | For Module Type With Connection Type   | Fault/Program Action Configuration |                         |
| Input  |                                        | Data x                             |                         |
| Input  | Listen Only                            |                                    |                         |
| Input  | Listen Only - Rack Optimization        |                                    |                         |
| Input  |                                        | Rack Optimization x                |                         |
| Output | Data x x                               |                                    |                         |
| Output | Listen Only                            |                                    |                         |
| Output | Listen Only - Rack Optimization        |                                    |                         |
| Output | Rack Optimization x x                  |                                    |                         |

## Understand Data and Connection Formats

For digital modules, the choices for data format and connection type are as follows:

- Data Format
- Integer
- Connection Type
- Data
- Listen Only
- Listen Only - Rack Optimization
- Rack Optimization

When you change the entries for data format and connection type, note the following:

- You do not delete the existing module.
- You do not create a new module.
- You bring forward configuration data for the new settings.
- Any configuration data you do not bring forward sets to the default value.

After you apply new settings for data format and connection, note the following:

- This is the base configuration for the next change in connection and data format settings.
- You lose all configuration data from previous data formats.

The choices for connection type for modules depend on the communication type format for the parent adapter as per the following table:

| Adapter Communication           |                                       | Output Module                                     | Output Module   | Output Module   |
|---------------------------------|---------------------------------------|---------------------------------------------------|-----------------|-----------------|
| Adapter Communication           |                                       | 1734-OA2, 1734-OW2, 1734-OW4, 1734-OW4K, 1734-OX2 |                 |                 |
| Listen Only - Rack Optimization | Data (default) x x x x                |                                                   |                 |                 |
| Listen Only - Rack Optimization |                                       | Listen Only x x                                   |                 |                 |
| Listen Only - Rack Optimization | Listen Only - Rack Optimization x x x |                                                   |                 |                 |
| None                            | Data (default) x x x x                |                                                   |                 |                 |
| None                            |                                       | Listen Only x x                                   |                 |                 |
| Rack Optimization               | Data (default) x x x x                |                                                   |                 |                 |
| Rack Optimization               | Listen Only x                         |                                                   |                 |                 |
| Rack Optimization               | Rack Optimization x x x x             |                                                   |                 |                 |

## Understand Transition to Hard Run Behavior

While online with a controller in Remote Run mode, change fields on the dialogs you select from the New Module dialog.

<!-- image -->

When you switch the controller to Hard Run, note the following:

- You disable all controls except for the Description field on the General dialog, which remains active in all modes.
- You revert to each control that contains an edited value, including the Description field on the General dialog, to include the following dialogs:
- General
- Connection
- Fault/Program Action
- Configuration

## Work with Dialogs for Digital Input Modules

To complete entries for the dialogs for input modules, proceed as follows:

1. Add an input module with these entries for connection type:
- Data
- Rack Optimization
2. From the top of the General dialog, select Configuration tab.

The Configuration dialog appears where you can configure the filter for input points for the following:

- Off to On
- On to Off

The Configuration dialog displays configuration data for each channel in individual rows in a table. Input modules support separate filter times for Off to On and On to Off transitions. The number of input channels varies based on the type of module as in these examples.

- The1734-IA2 module has 2 input channels (0…1).
- The 1734-IB4 module has 4 input channels (0…3).

See Figure 1 for a Configuration dialog of an 8-point input module.

Figure 1 - Configuration Dialog for 8-point Input Module

<!-- image -->

3. Complete the entries in Configuration dialog. See the following table for information about how to make entries.
4. From the Configuration dialog, perform one of the following:
- Select another tab at the top of the dialog.
- Select OK to save changes and close the dialog.
- Select Cancel to return to default values.
- Select Apply to save changes you made on any of the dialogs and it continues to display the dialog. The Apply button gets enabled only when you make changes to any of the dialogs.

<!-- image -->

|                        | Feature Description                                                                                                                                                                                                                                                                                            |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        | Channel Displays channels you use to set channel configuration parameters                                                                                                                                                                                                                                      |
| Input Filter Time (ms) | Displays Off to On or On to Off transition filter constant • A high signal must be present for this amount of time before the module reports an On. • A low signal must be present for this amount of time before the module reports an Off. • Enter a value in milliseconds. • The default is 1 ms (1000 µs). |

## Work with Dialogs for Digital Output Modules

Read this section to complete the Fault/Program Action and Configuration dialogs for output modules. You typically select these dialogs from the General dialog, when you add an output module with the following entries for connection type:

- Data
- Rack Optimization

Enter values for the Fault/Program Action and Configuration dialogs based on the following output modules:

- Without diagnostic status
- With overload diagnostic status
- With overload and open load diagnostic status

## Enter Values on the Fault/Program Action Dialog

Enter values on this dialog to configure the module output state for output modules when the controller mode changes to Program or Fault mode. To complete the entries on this dialog, proceed as follows:

1. From the General dialog, select Fault/Program Action tab.

The Fault/Program Action dialog appears. See Figure 2 for the Fault/Program Action dialog for an 8-point output module. The dialogs for 2-point and 4-point output modules are identical except for the number of points you can configure. Use this dialog to configure the Program Mode and Fault Mode for channels for the following modules:

- Without diagnostic status
- With overload diagnostic status
- With overload and open load diagnostic status
2. Complete the entries in Fault/Program Action dialog. See the following table for information about how to make entries.
3. From the Fault/Program Action dialog, perform one of the following:
- Select another tab at the top of the dialog.
- Select OK, which closes the dialog.
- Select Cancel to return to default values.
- Select Apply to save changes you made on any of the dialogs and it continues to display the dialog. The Apply button gets enabled only when you make changes to any of the dialogs.

Figure 2 - Fault/Program Action Dialog for 8-point Output Module

<!-- image -->

<!-- image -->

| Feature Description                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Point Displays the channel numbers.                                                                                                                                                                                                                                              |
| Program Mode • Select a value to determine the behavior of each output when the controller transitions to the Program Mode. • Make a selection from the available values for each channel: – Off (default) – On – Hold • In Hard Run only, you can disable editing this feature. |
| Fault Mode • Select a value to determine the behavior of each output when communication with the controller fails. • Select from the available values for each channel: – Off (default) – On – Hold • In Hard Run only, you can disable editing this feature.                    |

Enter Values on the Configuration dialog

Enter values on this dialog based on the type of module with the following:

- Overload diagnostic status
- Overload and open load diagnostic status

To complete the entries on this dialog proceed as follows:

1. From the General dialog, select Configuration tab.

The Configuration dialog appears, which displays configuration data for each channel in individual rows in a table. The number of output channels varies based on the type of module as in the following examples:

- The 1734-OB2E module has two output channels (0…1).
- The 1734-OB4E module has four output channels (0…3).
- The 1734-OB8E module has eight output channels (0…7).

See Figure 3 for a Configuration dialog of a 4-point output module. The 2-point and 8-point output modules are identical except for the number of point you can configure.

Figure 3 - Configuration Dialog for 4-point Output Module

<!-- image -->

2. Complete the entries in Configuration dialog. See the following table for information about how to complete entries with No Load Detection.

<!-- image -->

|              | Feature Description                                                                                                                                                                                     | Feature Description                                                                                                                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | Point Displays the channel numbers.                                                                                                                                                                     | Point Displays the channel numbers.                                                                                                                                                                     |
| Latch Faults | • Use to determine how a status bit acts after the cause of the fault is removed. • Use latching for tracking transient or momentary faults. • You do not affect status LEDs when using latched alarms. | • Use to determine how a status bit acts after the cause of the fault is removed. • Use latching for tracking transient or momentary faults. • You do not affect status LEDs when using latched alarms. |
| Latch Faults | If You Select Then                                                                                                                                                                                      |                                                                                                                                                                                                         |
| Latch Faults | Latch Faults (checked)                                                                                                                                                                                  | Alarm bits stay faulted if an alarm occurs. Clear the fault by using the clear latched alarm service for the channel (Reset pushbutton).                                                                |
| Latch Faults | Reset Latch Faults (unchecked)                                                                                                                                                                          | Alarm bits reflect the present state.                                                                                                                                                                   |
| Auto Restart | • The Reset mode defines the action of the output during a short circuit or overload. • A fault also occurs if you turn on an output when you do not apply field power to it.                           | • The Reset mode defines the action of the output during a short circuit or overload. • A fault also occurs if you turn on an output when you do not apply field power to it.                           |
| Auto Restart |                                                                                                                                                                                                         | Select If you want the output to                                                                                                                                                                        |
| Auto Restart | Latched Off (unchecked) Shut off                                                                                                                                                                        |                                                                                                                                                                                                         |
| Auto Restart |                                                                                                                                                                                                         | Auto Restart (checked) Continually try to turn on                                                                                                                                                       |
| Point Fault  | • Select to clear latched alarms. • A blue arrow denotes the use of explicit messaging.                                                                                                                 | • Select to clear latched alarms. • A blue arrow denotes the use of explicit messaging.                                                                                                                 |

## Configure Analog Modules

3. From the Configuration dialog, complete the following header checkboxes:
- No Load Detection
- Latch Faults
- Auto Restart

See Figure 4 as an example, if you want to configure all of the channels the same way, you check the No Load Detection header. This checks all the checkboxes in the column and enables the bit for all the channels in the module.

Figure 4 - Configuration Dialog for 8 point Output Module

<!-- image -->

4. From the Configuration dialog, perform one of the following:
- Select another tab at the top of the dialog.
- Select OK, which closes the dialog.
- Select Cancel to return to default values.
- Select Apply to save changes you made on any of the dialogs and it continues to display the dialog. The Apply button gets enabled only when you make changes to any of the dialogs.

To configure POINT I/O analog modules in Studio 5000 Logix Designer application, proceed as follows:

1. Configure your adapter, referring to the user manual for your adapter for information on how to:
- Configure the adapter
- Add modules to the I/O configuration
- Select a controller and communication module
2. According to the instructions in your adapter user manual, add an analog module and display the General dialog.
3. From the top of the General dialog, select Connection.
4. From the Connection dialog, leave the following unchecked:
- Inhibit Module
- Major Fault On Controller If Connection Fails While in Run Mode
5. From the Connection dialog, enter a value for Requested Packet Interval (RPI), if the field is selectable, per the table.
6. From the Connection dialog, select Choose Module Info from the top of the dialog to see a dialog that provides identification and status information.

<!-- image -->

| Adapter Configuration RPI Default Value for Analog Module Type   |
|------------------------------------------------------------------|
| Direct Connection 50 ms                                          |
| Rack Optimization RPI is not selectable                          |

7. For information about the Fault/Program Action, Configuration, Alarm Configuration and Calibration tabs and dialogs, see the sections Work with Dialogs for Analog Input Modules and Work with Dialogs for Analog Output Modules. You can see these tabs based on the module you have added.

## Understand Data and Connection Formats

For analog modules, the choices for data format and connection type are as follows:

- Data Format
- Integer
- Connection Type
- Data
- Listen Only
- Listen Only - Rack Optimization
- Rack Optimization

When you change the entries for data format and connection type, note the following:

- You do not delete the existing module.
- You do not create a new module.
- You bring forward configuration data for the new settings.
- Any configuration data you do not bring forward sets to the default value.

After you apply new settings for data format and connection, note the following:

- This is the base configuration for the next change in connection and data format settings.
- You lose all configuration data from previous data formats.

The choices for connection type for modules depend on the communication type format for the parent adapter, as explained in the user manual for the adapter.

## Work with Dialogs for Analog Input Modules

Read this section for information about how to complete entries on the following dialogs for analog input modules:

- Configuration
- Alarm Configuration
- Calibration

To display the dialogs, you typically select Configuration, Alarm Configuration, or Calibration at the top of the General dialog.

Work with the Configuration Dialog

This dialog does not appear for Listen Only connections. To complete the entries on this dialog, proceed as follows:

1. From the top of the General dialog, select Configuration.

The Configuration dialog appears for a current or voltage module, based on the type of module you have added. See Figure 5 for a Configuration dialog for a current input module.

Figure 5 - Configuration Dialog for a Current Input Module

<!-- image -->

2. From the Configuration dialog, complete the entries. See the following table for information on how to make entries.

|                                        | For This Value Select Comments                                                                                    |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| High Engineering -32,768…+32,767       | The default for 1734-IE2C analog input module is 16,383. The default for 1734-IE2V analog input module is 10,000. |
| Low Engineering -32,768…+32,767        | The default for 1734-IE2C analog input module is 3,277. The default for 1734-IE2V analog input module is 0.       |
|                                        | Digital Filter (ms) 0…10,000 The default is 0.                                                                    |
| Current Range  4…0 mA 0…20 mA          | The default is 4…20 mA.                                                                                           |
| Voltage Range  -10…+10V 0…10V          | Default is 0…10V                                                                                                  |
| Real Time Sample (ms) 0…10,000         | The default is 100. See Table 4 for the relationship between Notch Filter and Real Time Sample.                   |
| Notch Filter 50 Hz 60 Hz 250 Hz 500 Hz | The default is 60 Hz. See Table 4 for the relationship between Notch Filter and Real Time Sample.                 |

Table 4 - Real Time Sample Values

<!-- image -->

| Real Time Sample   | Notch Filter Setting          | Notch Filter Setting      | Notch Filter Setting   | Notch Filter Setting   |
|--------------------|-------------------------------|---------------------------|------------------------|------------------------|
|                    |                               | 50 Hz 60 Hz 250 Hz 500 Hz |                        |                        |
|                    | Min 120 ms 100 ms 24 ms 12 ms |                           |                        |                        |

3. From the bottom of the Configuration dialog, perform one of the following:
- Select another tab at the top of the dialog.
- Select OK to save changes and close the dialog.
- Select Cancel to return to default values.
- Select Apply to save changes you made on any of the dialogs and it continues to display the dialog. The Apply button gets enabled only when you make changes to any of the dialogs.

Work with the Alarm Configuration Dialog

This dialog does not appear for Listen Only connections. To complete the entries on this dialog, proceed as follows:

1. From the top of the General dialog, select Alarm Configuration.

An Alarm Configuration dialog appears for a current or voltage module, based on the type of module you have added. See Figure 6 for the Alarm Configuration dialog of a 1734-IE2C module. See the Table 5 for the list of default values.

Figure 6 - Alarm Configuration Dialog for 1734-IE2C Module

<!-- image -->

Table 5 - Alarm Configuration Dialog Default Values

| Alarms                 |
|------------------------|
| High High 16,793 9,800 |
| High 16,547 9,500      |
| Low 3,113 500          |
| Low Low 2,867 200      |

2. From the Alarm Configuration dialog, perform the following:
- a. Select a channel button (for example, 0 or 1) for which you want to configure the alarms. The channel 0 is selected in Figure 6 .
- b. Set the values for Low, High, Low Low, and High High alarms in one of the following ways:
- Enter the exact numerical value in the field against the corresponding alarm. You can use the up/down arrow to adjust the value.
- Drag the pointer on the corresponding alarm slider control to set the desired value.
- c. Choose one of the following unlatch options:
- Select Unlatch next to an individual alarm to unlatch each alarm one by one.
- Select Unlatch All to unlatch all the alarms at once.

- d. Select the following checkboxes, if necessary:
- Disable All Alarms - If you select the Disable All Alarms checkbox, the module does not report any alarms. This is disabled in Hard Run mode only.
- Latch Process Alarms - If you select the Latch Process Alarms checkbox, this lets you latch the transient alarm conditions. This is disabled in Hard Run mode only.
- e. Select OK.

Work with the Calibration Dialog

To complete entries on this dialog proceed as follows. Perform calibration in Hard Run or Remote mode. For information about the tools and steps for calibration, see Calibrate Your Analog Modules on page 71 .

1. From the General dialog, select Calibration.

The Calibration dialog appears for a current or voltage input module, depending on the module type.

See Figure 7 for a Calibration dialog for a current input module.

Figure 7 - Calibration Dialog for a Current Input Module

<!-- image -->

2. Select the Calibrate checkbox to specify which channel to calibrate.
3. Under Calibrate Channels, select the option One At a Time.
4. Select Start Calibration, which is active when the system is online, and you have selected at least one of the channels.

When you press the F1 button on your keyboard or select Help from the wizards and warning messages that appear during calibration, you get detailed information about related procedures.

A warning dialog appears.

<!-- image -->

5. From the warning dialog, for a module not currently used for control, select OK. The Low Value dialog appears.
6. From the Low Value dialog, select Next to start calibration. The High Value dialog appears.
7. From the High Value dialog, select Next to start calibration. The Calibration Completed dialog appears. This dialog shows you the changed calibration constants of the channel that is saved.

<!-- image -->

<!-- image -->

<!-- image -->

## Work with Dialogs for Analog Output Modules

Read this section for information about how to complete entries on the following dialogs for analog output modules:

- Configuration
- Alarm Configuration
- Fault/Program Action
- Calibration

To display the dialogs, you typically select Fault/Program Action, Configuration, Alarm Configuration, or Calibration at the top of the General dialog.

## Work with the Configuration Dialog

This dialog does not appear for Listen Only connections. To complete the entries on this dialog, proceed as follows.

1. From the top of the General dialog, select Configuration.

The Configuration dialog appears for a current or voltage module, based on the type of module you have added.

See Figure 8 that shows configuration parameters for each channel in individual rows on the grid with, for example, 1734-OE2C having two output channels.

Figure 8 - Configuration Dialog of 1734-OE2C Module

<!-- image -->

2. From the Configuration dialog, complete the entries. See the following table for information about how to make entries.
3. From the Configuration dialog, perform one of the following:
- Select another tab at the top of the dialog.
- Select OK to save changes and close the dialog.
- Select Cancel to return to default values.
- Select Apply to save changes you made on any of the dialogs and it continues to display the dialog. The Apply button gets enabled only when you make changes to any of the dialogs.

| For This Value Select Comments   |                                 |                                                                                                                    |
|----------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------|
| High Engineering -32,768…+32,767 |                                 | The default for 1734-OE2C analog output module is 8,191. The default for 1734-OE2V analog output module is 10,000. |
|                                  | Low Engineering -32,768…+32,767 | The default for 1734-OE2C analog output module is 1,638. The default for 1734-OE2V analog output module is 0.      |
| Current Range                    | 4…20 mA 0…20 mA                 | The default is 4…20 mA.                                                                                            |
| Voltage Range                    | -10…+10V 0…10V                  | The default is 0…10V.                                                                                              |

## Work with Alarm Configuration Dialog

This dialog does not appear for Listen Only connections. To complete the entries on this dialog, proceed as follows:

1. From the top of the General dialog, select Alarm Configuration.

An Alarm Configuration dialog appears for a current or voltage module, based on the type of module you have added. See Figure 9 for the Alarm Configuration dialog of a 1734-OE2C module. See the Table 6 for the list of default values.

Figure 9 - Alarm Configuration Dialog for 1734-OE2C Module

<!-- image -->

Table 6 - Alarm Configuration Dialog Default Values and Range

| Alarms Default Value Range   |                    |
|------------------------------|--------------------|
| High +32,767                 | -32,768 to +32,767 |
| Low -32,768                  | -32,768 to +32,767 |

2. From the Alarm Configuration dialog, perform the following:
- a. Select a channel button (for example, 0 or 1) for which you want to configure the alarms. The channel 0 is selected in Figure 9 .
- b. Set the values for Low and High alarms in one of the following ways:
- Enter the exact numerical value in the field against the corresponding alarm. You can use the up/down arrow to adjust the value, if necessary.
- Drag the pointer on the corresponding alarm slider control to set the desired value.
- c. Choose one of the following unlatch options:
- Select Unlatch next to an individual alarm to unlatch each alarm one by one.
- Select Unlatch All to unlatch all the alarms at once.
- d. Select the following checkboxes, if necessary:
- Disable All Alarms - If you select the Disable All Alarms checkbox, the module does not report any alarms. This is disabled in Hard Run mode only.
- Latch Process Alarms - If you select the Latch Process Alarms checkbox, this lets you latch the transient alarm conditions. This is disabled in Hard Run mode only.
- e. Select OK.

Work with the Fault/Program Action Dialog

Use this dialog to configure and display the parameters controlling output states during Fault and Program conditions. This dialog does not appear for Listen Only connections. To complete the entries on the dialog, proceed as follows:

1. From the top of the General dialog, select Fault/Program Action tab.

A Fault/Program Action dialog appears.

<!-- image -->

2. From the Fault/Program Action dialog, complete entries. See the following table for information about how to make entries.
3. From the bottom of the dialog, perform one of the following:
- Select another tab at the top of the dialog.
- Select OK to save changes and close the dialog.
- Select Cancel to return to default values.
- Select Apply to save changes you made on any of the dialogs and it continues to display the dialog. The Apply button gets enabled only when you make changes to any of the dialogs.

| For This Value Select Comments   |                                                                    |                                 |
|----------------------------------|--------------------------------------------------------------------|---------------------------------|
| Fault Mode                       | Hold Last State Go to Low Clamp Go to High Clamp Use Program Value | The default is Go to Low Clamp. |
|                                  | Fault Value -32,768…+32,767 The default is 0.                      |                                 |
| Program Mode                     | Hold Last State Go to Low Clamp Go to High Clamp Use Program Value | The default is Go to Low Clamp. |
|                                  | Program Value -32,768…+32,767 The default is 0.                    |                                 |

## Work with the Calibration Dialog

To complete entries on this dialog, proceed as follows. Perform calibration in Hard Run or Remote mode. For information about the tools and steps for calibration, see Calibrate Your Analog Modules on page 71 .

1. From the General dialog, select Calibration.

The Calibration dialog appears for a current or voltage output module, depending on the module type.

<!-- image -->

2. From the Calibration dialog, select one of these:
- In Groups
- One At a Time
3. From the Calibration dialog, check the Calibrate checkbox to specify which channel to calibrate.
4. From the Calibration dialog, select Start Calibration, which is active when:
- The system is online, and
- You selected at least one of the channels

When you press the F1 button on your keyboard or select Help from the wizards and warning messages that appear during calibration, you get detailed information about related procedures.

A warning dialog appears.

<!-- image -->

5. From the warning dialog, for a module not currently used for control, select OK. A Low Value dialog appears.
6. Follow the instructions that you see in the Low Value dialog, and select Next. The High Value dialog appears.

<!-- image -->

<!-- image -->

7. Follow the instructions that you see in the High Value dialog and select Next to start calibration.
8. When the calibration completes successfully, the Calibration Completed dialog appears.

<!-- image -->

If calibration fails, the Results dialog appears with the channels list that are failed in calibration.

<!-- image -->

9. When the calibration is successful, select Finish. If calibration is failed, from the Results dialog, select Retry to calibrate the channel that did not calibrate successfully and repeat the process until calibration is successful.
10. Repeat calibration for each channel, if applicable.

## Commissioning a Node

<!-- image -->

## Configure POINT I/O Modules for DeviceNet Networks

This chapter covers the instructions on how to configure POINT I/O modules in a DeviceNet network. If you are using a ControlNet, EtherNet/IP, or PROFIBUS network, see the appropriate user manual:

- POINT I/O ControlNet Adapter User Manual, publication 1734-UM008
- POINT I/O EtherNet/IP Adapter Module User Manual, publication 1734-UM011
- POINT I/O and ArmorPOINT I/O Dual-port EtherNet/IP Adapters User Manual, publication 1734-UM017
- POINT I/O PROFIBUS Adapter Module User Manual, publication 1734-UM005

To configure POINT I/O modules, use RSNetWorx™ software to identify the network and configure the I/O modules with electronic data sheet (EDS) files. To obtain EDS files for use in configuration, go to rok.auto/pcdc .

Methods for commissioning nodes are the following:

- RSNetWorx commissioning pull-down
- Sequential auto addressing feature
- Third-party configuration software

## Using the RSNetWorx Commissioning Tool

The RSNetWorx commissioning tool lets you commission devices (set the node address and the data rate parameters) that are either connected to a DeviceNet network or connected via a point-to-point connection.

The node commissioning tool works through RSLinx software. The RSNetWorx software does not have to be online when performing the operation.

Before you can add any device to a DeviceNet network, you must commission it. This means you must program into the device a node address and data rate. Some devices are precommissioned, meaning a node address (usually set to 63) and a data rate (usually set to 125 Kbps) are programmed into the device at the factory prior to shipment. You need to commission other devices in the field. Once a device has been commissioned and attached to a network, you can use the RSNetWorx for DeviceNet node commissioning tool to edit the node address and data rate that were set previously.

Exercise caution while editing node addresses when on a network. When you apply a new node address, it immediately overwrites the node address data in the device currently specified. If you decide to reassign node addresses, you should first determine the order in which this needs to be done so that all devices still have unique node addresses when you finish.

For example, if two of the devices on your network are a photoelectric sensor and a hand controller and you accidentally change the node address of the hand controller to be the same as that of the photoelectric sensor, then the photoelectric sensor no longer has a unique address. This means it is not able to provide data to the scanner. If you cannot access a device, because you have used its node address for another device, you have to remove it from the network, recommission it, then reinstall it on the network.

## Configure Digital Modules Using RSNetWorx Software

<!-- image -->

ATTENTION: Do not change the data rate of devices while they are connected to a network. Erratic operation may result. We recommend that if you need to change the data rate of a device, you should remove it from the network, establish a point-to-point connection between the PC, which hosts the RSNetWorx for DeviceNet software, and the target device, recommission it, and then reconnect it to the network.

## Use Sequential Auto Addressing

Sequential Auto Addressing (SAA) reassigns the node address of every module to the right of the one you select on the POINTBus™ network. Each module changes its node address to one greater than its neighbor.

## IMPORTANT

Make sure that the node address of the selected module is the desired value before issuing the SAA command.

When this command is set, each module to the right gets a new address one greater than its neighbor. The addressing ripples through a line of POINT I/O modules, assigning a node number to each module installed in a mounting base on the same POINTBus network.

Follow these steps to Auto Address a line of POINT I/O modules.

1. Set the address of the first module you want to address.
2. Set the Auto Address command to Sequential Address.

All modules in line reset with new sequential addresses.

For example, assume you have five POINT I/O modules in a line, and the address of the first module is 10. After the Sequential Address command is sent to the first module, the node addresses of the modules in line are 10, 11, 12, 13, and 14.

## Using Third-party Configuration Software

When using third-party configuration software, load the EDS files into the software and follow the designers instructions.

The input modules use dialogs similar to 1734-IB4 module used in this procedure. To configure digital input modules, proceed as follows:

1. Open your RSNetWorx for DeviceNet software.
2. Use the selections on the left to construct your system. If your network is up, select Browse.

<!-- image -->

3. After setting up your system, double-click on the module icon which you want to configure. If you are online, upload the configuration. A dialog similar to the following appears.

<!-- image -->

4. Select the Device Parameters tab to get the dialog for setting the parameters.

## Configure Input Modules

Figure 10 shows the Device Parameters dialog for 1734-IB4 input module. All digital input modules have parameters similar to 1734-IB4 input module.

In Device Parameters dialog, you can see all the parameters for the module. These include filters, autobaud, sequential addressing, and communication rate (if you are not using autobaud).

Figure 10 - Device Parameters Dialog for 1734-IB4 Input Module

<!-- image -->

The Groups dropdown list include the following:

- All parameters
- I/O
- Configuration
- POINTBus

To complete entries in the Device Parameters dialog, proceed with following procedure:

1. From the Groups dropdown list, select Configuration and the parameters you want.
2. Select one of the following options:
- Single — Select this option to change or configure parameters one at a time.
- All — Select this option to change all selections at once.

<!-- image -->

If autobaud is selected, the communication rate of this module automatically matches the communication rate of the existing devices on the network, and you are prevented from selecting a specific communication rate.

<!-- image -->

3. Select the filter of your choice and enter the filter time. Each input channel can have its own time selection.
4. Select Download To Device.

<!-- image -->

## Configure Output Modules

All output modules use dialogs similar to the 1734-OB4E output module used in this procedure. To configure output modules, proceed with following procedure:

1. From the General Parameters dialog, select Device Parameters to get the dialog for setting parameters.
2. From the Device Parameters dialog, set parameters for the module to include sequential addressing and autobaud or communication rate (if you are not using autobaud).

<!-- image -->

<!-- image -->

The Groups dropdown list include the following:

- All parameters
- I/O output value
- I/O output status
- Reset services
- POINTBus
- Configuration

3. From the Groups dropdown list, select Configuration and the parameters you want.
4. Select one of the following options:
- Single — Select this option to change or configure parameters one at a time.
- All — Select this option to change all selections at once.

<!-- image -->

The configurable parameters include the following:

- Fault Value - Off/On

<!-- image -->

r

- Fault Action - Fault Value/Hold Last State

<!-- image -->

- Idle Value - Off/On
- Idle Action - Idle Value/Hold Last State
- Enable Latching Alarms - Latching Enabled/Latching Disabled

<!-- image -->

<!-- image -->

<!-- image -->

- Enable No Load - No Load Enabled/No Load Disabled
- Reset Mode - Latch Off/Auto Restart
- Autobaud - Enable/Disable

<!-- image -->

<!-- image -->

<!-- image -->

If autobaud is selected, the communication rate of this module automatically matches the communication rate of the existing devices on the network and you are locked out from selecting a communication rate.

5. From the Device Parameters dialog, select Download To Device.

To configure the 1734-OW2 relay output module, proceed with following procedure:

1. From the General dialog, select Device Parameters to get the dialog for setting parameters.
2. The EDS Editor dialog appears. From the EDS Editor dialog, select Upload to load the latest information.
3. From the Device Parameters dialog, select Configuration from the Groups dropdown list to set the parameters for the module to include sequential addressing, autobaud, or the communication rate (if you are not using autobaud).

<!-- image -->

<!-- image -->

<!-- image -->

The Groups dropdown list include the following:

- All parameters
- I/O
- POINTBus
- Configuration - Select to set the parameters

Configurable parameters include the following:

- Fault Action - Fault Value/Hold Last State
- Fault Value - Off/On

<!-- image -->

<!-- image -->

- Idle Action - Idle Value/Hold Last State
- Idle Value - Off/On
- Run/Idle Command - Idle/Run
- Autobaud - Enable/Disable
4. From the Device Parameters dialog, Groups dropdown list:
- Select All parameters to display each item.
- Select POINTBus to display only the Run/Idle Command and Autobaud.
5. To monitor the output, select Start Monitor from the Device Parameters dialog. Consider the following:
- The output value is displayed for each scan.
- Select All to scan all values.
- The Start Monitor button turns to Stop Monitor during monitoring.
- Select Stop Monitor to stop monitoring the selected parameters.
- Identify monitoring by the ball appearing momentarily next to the selected item during each scan.

<!-- image -->

<!-- image -->

## Configure Analog Modules Using RSNetWorx Software

<!-- image -->

In the following procedure, the 1734-IE2C analog current input module and 1734-OE2C analog current output module are used as a representative for all input and output analog modules. The actual dialogs for your particular module may not be identical to the one shown in this procedure.

To configure analog input modules, proceed as follows:

1. Open your RSNetWorx for DeviceNet software. The RSNetWorx for DeviceNet dialog appears.
2. From the RSNetworx for DeviceNet dialog, use the selections in the window on the left to construct your system, or if your network is up, select Browse.

<!-- image -->

3. Double-click on your module icon. The General dialog appears for your module.
4. From the General dialog, select Device Parameters tab to configure and set the parameters.
5. An EDS Editor dialog appears. From the EDS Editor dialog, select Upload to load the existing parameters from the device.
6. In the Device Parameters dialog, select Configuration from the Groups dropdown list to select parameters.
7. Select one of the following options:
- Single - Select this option to change or configure parameters one at a time.
- All - Select this option to change all selections at once.

<!-- image -->

<!-- image -->

<!-- image -->

8. Change the configuration or apply the uploaded parameters.

Select Download To Device to change the parameters.

<!-- image -->

To configure the analog output module, proceed with the following procedure:

1. Double-click on your module icon.

The General dialog appears.

<!-- image -->

2. From the General dialog, select Device Parameters to set parameters.

The EDS Editor dialog appears.

<!-- image -->

3. From the EDS Editor dialog, select Upload to load the existing parameters from the device.

4. From the Device Parameters dialog, at the Groups dropdown list, select Configuration.
5. From the Device Parameters dialog, set the Group Run/Idle Command parameter to Idle or Run. Any parameter with a lock symbol indicates that it is nonchangeable.
6. Select values for current or voltage.
- For current, select 0…20 mA or 4…20 mA.
- For voltage, select 0…10V or -10…+10V

<!-- image -->

<!-- image -->

<!-- image -->

Fault states include the following:

- Hold Last State
- Go to Low Clamp
- Go to High Clamp
- Go to Fault Value
7. For parameter Enable Alarm Latch, select Disable or Enable Latching Alarms from the dropdown list.

<!-- image -->

<!-- image -->

8. For parameter Disable Alarms, select Alarms Enabled or Alarms Disabled from the dropdown list.
9. For parameter Autobaud, select Enable or Disable from the dropdown list.

<!-- image -->

<!-- image -->

With current or voltage modules if you change range values, it affects the range or scaling of the module.

## Digital Input Modules

## POINT I/O Module Data

Read this chapter for information about module status, input, output, configuration data, and default data maps for POINT I/O modules to include the following:

- Digital input modules
- Digital output modules
- Relay output modules
- Analog input modules
- Analog output modules
- POINTBlock I/O modules

Read this section for information about digital input modules.

## Digital DC Input Modules

The POINT I/O digital DC input modules feature the following:

- 24V DC nominal DC inputs
- Input range of 10…28.8V DC
- 2, 4, or 8 sinking or sourcing style inputs
- Autobaud (matches the communication rate of existing devices on the network)
- Selectable input filter times (0…65 ms with 1 ms default)
- Sequential auto addressing

I/O messages are sent to (consumer) and received from (producer) these POINT I/O modules. These messages are mapped into the processor memory (a) . These POINT I/O modules produce 1 byte of input data (scanner Rx). They do not consume I/O data (scanner Tx).

Default Data Map – 1734-IB2 and 1734-IV2

## Message Size: 1 Byte

|                                                                      | 7654321 0                                                            |                                                                      |                                                                      |                                                                      |                                                                      |                                                                      |                                                                      |
|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                |                                                                      |                                                                      |
| Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                |
| Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On |

Default Data Map – 1734-IB4, 1734-IB4K, and 1734-IV4

## Message Size: 1 Byte

|                                                                                                             | 7654321 0                                                                                                   |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               | Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               | Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               | Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       |
| Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On |

<!-- image -->

## Default Data Map – 1734-IB8, 1734-IB8K, 1734-IV8, and 1734-IV8K

## Message Size: 1 Byte

|                                                                                                                                                                                                         | 7654321 0                                                                                                                                                                                               |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                         | Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0                                                                                                                                                    |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |
| Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   |
| Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On |

## Default Data Map – 1734-IB4D – Produced Assembly Instance 101

## Message Size: 2 Bytes

|                                                                               | 7 6 5 43 2 1 0                                                                |                                                                                |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|                                                                               |                                                                               | Produce 0 (Rx) Fault 3 Fault 2 Fault 1 Fault 0 Input 3 Input 2 Input 1 Input 0 |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
|                                                                               |                                                                               |                                                                                | Produce 1 (Rx) SC 3 SC 2 SC 1 SC 0 OW 3 OW 2 OW 1 OW 0                        |                                                                               |                                                                               |                                                                               |                                                                               |
| Consume (Tx) No consumed data                                                 | Consume (Tx) No consumed data                                                 | Consume (Tx) No consumed data                                                  | Consume (Tx) No consumed data                                                 | Consume (Tx) No consumed data                                                 | Consume (Tx) No consumed data                                                 | Consume (Tx) No consumed data                                                 | Consume (Tx) No consumed data                                                 |
| Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit  | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit |

## Default Data Map – 1734-IB4D - Produced Assembly Instance 23

## Message Size: 1 Byte

|                                           | 76 54 3 2 1 0                             |                                                                                |                                           |                                           |                                           |                                           |                                           |
|-------------------------------------------|-------------------------------------------|--------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
|                                           |                                           | Produce 0 (Rx) Fault 3 Fault 2 Fault 1 Fault 0 Input 3 Input 2 Input 1 Input 0 |                                           |                                           |                                           |                                           |                                           |
| Consume (Tx) No consumed data             | Consume (Tx) No consumed data             | Consume (Tx) No consumed data                                                  | Consume (Tx) No consumed data             | Consume (Tx) No consumed data             | Consume (Tx) No consumed data             | Consume (Tx) No consumed data             | Consume (Tx) No consumed data             |
| Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit                                      | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit |

## Default Data Map – 1734-IB4D – Configuration Assembly Instance 103

## Message Size: 18 Bytes

|                                                                         | 7 6543 2 1 0                               |                                            |                                            |                                            |                                            |                                            |                                            |
|-------------------------------------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| Consume 0 Input 0 Off to On Filter Byte 0                               | Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  |
| Consume 1 Input 0 Off to On Filter Byte 1                               | Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  |
| Consume 2 Input 0 On to Off Filter Byte 0                               | Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  |
| Consume 3 Input 0 On to Off Filter Byte 1                               | Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  |
| Consume 4 Input 1 Off to On Filter Byte 0                               | Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  |
| Consume 5 Input 1 Off to On Filter Byte 1                               | Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  |
| Consume 6 Input 1 On to Off Filter Byte 0                               | Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  |
| Consume 7 Input 1 On to Off Filter Byte 1                               | Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  |
| Consume 8 Input 2 Off to On Filter Byte 0                               | Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  |
| Consume 9 Input 2 Off to On Filter Byte 1                               | Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  |
| Consume 10 Input 2 On to Off Filter Byte 0                              | Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 |
| Consume 11 Input 2 On to Off Filter Byte 1                              | Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 |
| Consume 12 Input 3 Off to On Filter Byte 0                              | Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 |
| Consume 13 Input 3 Off to On Filter Byte 1                              | Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 |
| Consume 14 Input 3 On to Off Filter Byte 0                              | Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 |
| Consume 15 Input 3 On to Off Filter Byte 1                              | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 |
| Consume 16 Autobaud Disable Enable OW3 Enable OW2 Enable OW1 Enable OW0 |                                            |                                            |                                            |                                            |                                            |                                            |                                            |
| Consume 17 Produced Assembly Instance                                   | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      |
| Produce (Rx) No produced data                                           | Produce (Rx) No produced data              | Produce (Rx) No produced data              | Produce (Rx) No produced data              | Produce (Rx) No produced data              | Produce (Rx) No produced data              | Produce (Rx) No produced data              | Produce (Rx) No produced data              |
| Where: OW = Open wire                                                   | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      |

## Digital Output Modules

## Digital AC Input Modules

The 1734 digital AC input modules feature the following:

- 120/220V AC nominal are AC inputs
- Input range of 65…132 for 120V AC inputs; 159…264 for 220V AC inputs
- Two sinking style inputs
- Autobaud (matches the communication rate of existing devices on the network)
- Selectable input filter times (0…65 ms with 1 ms default)
- Sequential auto addressing

I/O messages are sent to (consumer) and received from (producer) these POINT I/O modules. These messages are mapped into the processor memory (a) . These POINT I/O modules produce 1 byte of input data (scanner Rx). They do not consume I/O data (scanner Tx).

## Default Data Map – 1734-IA2 and 1734-IM2

## Message Size: 1 Byte

|                                                          | 7654321 0                                                |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                                          | Produce (scanner Rx) Ch1 Ch0                             |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |
| Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    |
| Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On |

Default Data Map – 1734-IA4, 1734-IA4K, and 1734-IM4

## Message Size: 1 Byte

|                                                                                            | 7654321 0                                                                                  |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Produce (scanner Rx) Ch3 Ch2 Ch1 Ch0                                                       |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |
| Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      | Consume (scanner Tx) No consumed data                                                      |
| Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On |

Read this section for information about digital output modules.

## Digital DC Output Modules

The features of DC output modules include the following:

- 24V DC outputs with a range of 10…28.8V DC
- Output diagnostic features are incorporated to assist in troubleshooting
- Current limited outputs of up to 2 A with respect to their DC return
- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

I/O messages are sent to (consumer) and received from (producer) these POINT I/O modules. These messages are mapped into the processor memory (a) . These POINT I/O modules produce 1 byte of input data (scanner Rx). They consume 1 byte of output data (scanner Tx).

(a) These are mapped through scan lists in DeviceNet networks and Direct, Listen Only, or Rack-optimized connections in ControlNet and EtherNet/IP networks.

## Default Data Map – 1734-OB2, 1734-OB2E, and 1734-OV2E

## Default Data Map – 1734-OB4, 1734-OB4K, 1734-OB4E, and 1734-OV4E

Default Data Map – 1734-OB8, 1734-OB8K, 1734-OB8E, 1734-OB8EK, 1734-OV8E, and 1734-OV8EK

## Default Data Map – 1734-OB2EP

## Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) Not used Ch1 Ch0

Channel status

(1734-OB2E module only) (1)

(1) The 1734-OB2, 1734-OB4, 1734-OB4K, 1734-OB8, and 1734-OB8K digital DC output modules produce 1 byte of data (scanner RX), but it is always zero.

Where: 0 = No error, 1 = Error

## Message Size: 1 Byte

76543 2 1 0

Consume (scanner Tx) Not used Ch1 Ch0 Channel state

Where: 0 = Off, 1 = On

## Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0

Channel status

(1734-OB4E module only)( )(1)

(1) The 1734-OB2, 1734-OB4, 1734-OB4K, 1734-OB8, and 1734-OB8K digital DC output modules produce 1 byte of data (scanner RX), but it is always zero.

Where: 0 = No error, 1 = Error

## Message Size: 1 Byte

76543 2 1 0

Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state

Where: 0 = Off, 1 = On

## Message Size: 1 Byte

76543 21 0

Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0

Channel status

(1734-OB8E and1734-OB8EK

module only)( )(1)

(1) The 1734-OB2, 1734-OB4, 1734-OB4K, 1734-OB8, and 1734-OB8K digital DC output modules produce 1 byte of data (scanner RX), but it is always zero.

Where: 0 = No error, 1 = Error

## Message Size: 1 Byte

76543 21 0

Consume (scanner Tx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Channel state

Where: 0 = Off, 1 = On

## Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) Not used Ch1 Ch0 Channel status

Where: 0 = No error, 1 = Error

## Message Size: 1 Byte

76543 2 1 0

Consume (scanner Tx) Not used Ch1 Ch0 Channel state

Where: 0 = Off, 1 = On

## Relay Output Modules

## Digital AC Output Modules

The 1734-OA2 AC output module features include the following:

- 120V AC outputs with a range of 74…264V AC (120/220V AC nominal)
- Each output is rated at 0.10 A minimum to 0.75 A maximum
- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

## Default Data Map – 1734-OA2

|                                                     | 76543 2 1 0                                         |                                                     |                                                     |                                                     |                                                     |                                       |                                       |                        |
|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|---------------------------------------|---------------------------------------|------------------------|
| Produce (scanner Rx) No produced data               | Produce (scanner Rx) No produced data               | Produce (scanner Rx) No produced data               | Produce (scanner Rx) No produced data               | Produce (scanner Rx) No produced data               | Produce (scanner Rx) No produced data               | Produce (scanner Rx) No produced data | Produce (scanner Rx) No produced data |                        |
| Consume (scanner Tx) Not used Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch1 Ch0 Channel state |                                       |                                       |                        |
| Where: 0 = Off, 1 = On                              | Where: 0 = Off, 1 = On                              | Where: 0 = Off, 1 = On                              | Where: 0 = Off, 1 = On                              | Where: 0 = Off, 1 = On                              | Where: 0 = Off, 1 = On                              | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On |

## Default Data Map – 1734-OA4 and 1734-OA4K

|                                                             | 76543 2 1 0                                                 |                                                             |                                                             |                                       |                                       |                                       |                                       |                                       |                        |
|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|------------------------|
| Produce (scanner Rx) No produced data                       | Produce (scanner Rx) No produced data                       | Produce (scanner Rx) No produced data                       | Produce (scanner Rx) No produced data                       | Produce (scanner Rx) No produced data | Produce (scanner Rx) No produced data | Produce (scanner Rx) No produced data | Produce (scanner Rx) No produced data | Produce (scanner Rx) No produced data |                        |
| Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state |                                       |                                       |                                       |                                       |                                       |                        |
| Where: 0 = Off, 1 = On                                      | Where: 0 = Off, 1 = On                                      | Where: 0 = Off, 1 = On                                      | Where: 0 = Off, 1 = On                                      | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On                | Where: 0 = Off, 1 = On |

The relay output modules consist of 1734-OW2, 1734-OW4, and 1734-OX2 relay output modules. Features of the 1734-OW2 and 1734-OW4 relay modules include the following:

- Type A normally open relays
- Sink or source current with respect to power or return
- Contact outputs isolated from each other
- Each output rated 5…240V DC/V rms at 2 A (current is load-dependent)
- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

Features of the 1734-OX2 relay modules include the following:

- Two Form C isolated (normally open; normally closed) electromechanical relays
- Sink or source current with respect to power or return
- Contact outputs isolated from each other
- Each output rated 5…240V DC/V rms at 2 A (current is load-dependent)
- Autobaud (matches the communication rate of existing devices on the network)
- Sequential auto addressing

I/O messages are sent to (consumer) and received from (producer) these POINT I/O modules. These messages are mapped into the processor memory.

## Default Data Map – 1734-OW2

| Message Size: 1 Byte                                | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|-----------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                                                     | 76543 2 1 0            |                        |                        |                        |                        |                        |                        |                        |                        |
| Produce (scanner Rx) No produced data               |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Consume (scanner Tx) Not used Ch1 Ch0 Channel state |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where: 0 = Off, 1 = On                              |                        |                        |                        |                        |                        |                        |                        |                        |                        |

## Analog Input Modules

## Default Data Map - 1734-OW4 and 1734-OW4K

## Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) No produced data

Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state

Where: 0 = Off, 1 = On

## Default Data Map - 1734-OX2

Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) No produced data

Consume (scanner Tx) Not used Ch1 Ch0 Channel state

Where:

0 = Normally open contact Off, Normally closed contact On

1 = Normally open contact On, Normally closed contact Off

<!-- image -->

The 1734-IE2C analog input module is a two-channel module that converts an analog input current to a digital value. The module resolution is 16 bits across 0…21 mA. The module has two modes:

- 0…20 mA
- 4…20 mA (default mode)
- Scaling to any 16-bit signed integer (–32,768…+32,767) - Default for 1734-IE2C scalers are 3277 @ 4 mA for low and 16,383 @ 20 mA for high
- Operates in Unipolar mode

The 1734-IE2V analog input module is a two-channel module that converts an analog input voltage to a digital value. The module resolution is 16 bits across -10…+10V. The module has two modes.

- 0…10V DC (default mode)
- ±10V DC
- Scaling to any 16-bit signed integer (–32,768…+32,767) - Default for 1734-IE2V scalers are 0 @ 0V for low and 10,000 @ 100V for high
- Operates in Unipolar or Bipolar modes

## Data

The 1734-IE2C module operates in unipolar mode only. The 1734-IE2V module operates in unipolar or bipolar modes. Data returned from the module is scaled by the user to any 16-bit signed integer (–32,768…+32,767). The 6 bytes of data are read from the 1734-IE2C and 1734-IE2V modules. No data is written to the input modules.

- Channel 0 Data (2 bytes)
- Channel 1 Data (2 bytes)
- Channel 0 Status (1 byte)
- Channel 1 Status (1 byte)

## Communicate with Your Module

I/O messages are sent to (consumer) and received from (producer) the POINT I/O modules. These messages are mapped into the processor's memory (a) . These POINT I/O input modules produce 6 bytes of input data (scanner Rx) and fault status data. It does not consume output data (scanner Tx).

(a) These are mapped through scan lists in DeviceNet networks and Direct, Listen Only, or Rack-optimized connections in ControlNet and EtherNet/IP networks.

## Default Data Map - 1734-IE2C and 1734-IE2CK

| Message Size: 6 Bytes   | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         |                                                                                                                                                                                                                                                                                                                                                                          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)    | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)    | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)    | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)    |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          | OR UR HHA LLA HA LA CM CF OR UR HHA LLA HA LA CM CF                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
|                         | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    | Consume (scanner Tx) No consumed data                                                                                                                                                                                                                                                                                                                                    |
| Where:                  | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault |

## Default Data Map - 1734-IE2V

| Message Size: 6 Bytes                 | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    | Message Size: 6 Bytes                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)                  | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)                  | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)                  | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx)                  |                                                                                                                                                                                                                                                                                                                                                                          | OR UR HHA LLA HA LA CM CF OR UR HHA LLA HA LA CM CF                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Consume (scanner Tx) No consumed data |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Where:                                | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault LA = Low Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode HA = High Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault |

## Scaling

Select scaling for each channel by making the selection on the configuration dialog. Scaling is the conversion of unscaled data to engineering units.

The high and low scalers (Engineering Units) are signed integers. There are no restrictions on these units.

- Defaults for 1734-IE2C scalers are 3277 @ 4 mA for low and 16,383 @ 20 mA for high.
- Defaults for 1734-IE2V scalers are 0 @ 0V for low and 10,000 @ 100V for high.

Set each scaler individually or on a per channel basis.

The 1734-IE2C module reads a current input between 0 mA or 4 mA (low) and 20 mA (high) dependent on the mode selected. The 1734-IE2V module reads a voltage input between -10V or 0V (low) and +10V (high) dependent on mode selected.

## Channel Status

| Channel Status Byte   | Channel Status Byte   | Channel Status Byte   | Channel Status Byte                             | Channel Status Byte   | Channel Status Byte   | Channel Status Byte   | Channel Status Byte   |
|-----------------------|-----------------------|-----------------------|-------------------------------------------------|-----------------------|-----------------------|-----------------------|-----------------------|
|                       |                       |                       | Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |                       |                       |                       |                       |
| Overrange Underrange  | High High Alarm       | Low Low Alarm         | High Alarm Low Alarm CAL Mode Channel Fault     |                       |                       |                       |                       |

- Channel Fault Description - General channel health bit indicates whether the module is operating with or without faults. If any alarms or faults are detected, this bit is set. Channel Status can be read on a per channel basis or by reading the Channel Status Byte (Bit 0) in the Module Produce Assembly.
- Calibration Mode Bit - This bit (Channel Status Bit 1) is set when you begin calibration. See the chapter Calibrate Your Analog Modules on page 71 for calibration details. When set, the channel status indicator flashes green.
- Low Alarm Value Bit - When the input signal is less than the Low Alarm value, this bit (Channel Status Bit 2) is set. The default value for this alarm is as follows:
- 1734-IE2C module is 3113 counts (3.8 mA)
- 1734-IE2V module is 500 counts = 500 mV (0.5V)
- High Alarm Value Bit - When the input signal is more than the High High Alarm value, this bit (Channel Status Bit 3) is set. The default value for this alarm is as follows:
- 1734-IE2C module is 16,547 counts (20.2 mA)
- 1734-IE2V module is 9500 counts = 9500 mV (9.5V)
- Low Low Alarm Value Bit - When the input signal is less than the Low Low Alarm value, this bit (Channel Status Bit 4) is set. The default value for this alarm is as follows:
- 1734-IE2C module is 2867 counts (3.5 mA)
- 1734-IE2V module is 200 counts = 200 mV (0.2V)
- High High Alarm Value Bit - When the input signal is more than the High Alarm value, this bit (Channel Status Bit 5) is set. The default value for this alarm is as follows:
- 1734-IE2C module is 16,792 counts (20.5 mA)
- 1734-IE2V module is 9800 counts = 9800 mV (9.8V)
- Underrange Status Bit - This bit (Channel Status Bit 6) is set when the module returned data is at a minimum. 1734-IE2C module is 98 counts (around 120 µA); 1734-IE2V module is -0.25 or -10.25V, depending on range. When set, the channel status indicator flashes red.
- Overrange Status Bit - This bit (Channel Status Bit 7) is set when the module returned data is at a maximum. 1734-IE2C module is around 21 mA. 1734-IE2V module is +10.25V. When set, the channel status indicator flashes red.

## Latch Alarms

The latch alarms let low and high alarm status information to be latched when an alarm is set. Even if an alarm is momentarily set, the status bit stays set until a reset latch service is issued. The default setting is Unlatched. Each channel can be configured individually.

## Alarm Disable

This function disables all channel alarms and faults so they are not reported in the channel status field. The channel indicator stays steady green, alarms are ignored. The default state is Alarms Enabled. Each channel can be configured individually.

## Calibration Status

This status bit is set when the channel is in Calibration mode. At Begin Calibration, the module is put into Calibration mode. This bit is reset when the Accept Low Calibration, or Accept High Calibration, commands are sent. This is not the Bad Calibration Status bit, which is set if the module is not calibrated.

## Digital Filter

A digital filter is available on the input modules. You set a time constant that is used in the equation:

<!-- formula-not-decoded -->

Where:

Yn = New data

Yn-1 = Old data

dt = Channel update rate in milliseconds

T A = Digital filter time constant

Xn = Present unfiltered data

T A can be an integer from 0…10,000 ms. If set to 0, the filter is disabled.

The default setting is disabled. This is done by setting the time constant (TA) to zero. Each channel can be configured individually for time constant but the update rate (dt) is done on a per module basis.

## Update Rate

The update rate determines how often a channel is scanned. The maximum rate is determined by the notch filter setting. The minimum update rate is 10,000 ms.

- 120 ms maximum update rate - 50 Hz
- 100 ms update rate - 60 Hz
- 24 ms update rate - 250 Hz
- 12 ms update rate - 500 Hz

## Notch Filter

Select a notch filter. The notch filter is for both inputs. Valid settings are the following:

- 50 Hz - 120 ms maximum update rate
- 60 Hz - 100 ms update rate
- 250 Hz - 24 ms update rate
- 500 Hz - 12 ms update rate

The update rate determines the rate at which the inputs are sampled. The maximum update rate is determined by the notch filter setting. The notch filter parameter is used to select the fastest possible rate. The minimum update rate is 10,000 ms.

## Alarms

Available alarms include the following:

- Low
- Low Low
- High
- High High

Each alarm has one status bit, which is set to indicate when the input goes beyond its setpoint. All Alarm Status bits can be read individually or from the Channel Status Byte (bits 2…5).

You can configure each channel alarm individually.

## Analog Output Modules

## Range Status

The module reports both Underrange and Overrange status.

- Underrange Status - This bit (Channel Status Bit 6) is set when the module returned data is at a minimum.
- For the 1734-IE2C module, the value is 98 counts (around 120 µA).
- For the 1734-IE2V module, the value is -0.25 or -10.25V, depending on mode.
- When set, the channel status indicator flashes red.
- On the 1734-IE2C module, a wire-off condition sets this bit.
- Overrange Status - This bit (Channel Status Bit 7) is set when the module returned data is at a maximum.
- For the 1734-IE2C module, the value is around 21 mA.
- For the 1734-IE2V module, the value is +10.25V.
- When set, the channel status indicator flashes red.
- On the 1734-IE2V module, a wire-off condition sets this bit.

## Channel Indicator Behavior

See the table for a listing of channel indicator states for given module conditions.

| Indication Probable Cause                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------|
| Off The module is in CAL mode.                                                                                                     |
| Steady green Normal (channel scanning inputs)                                                                                      |
| Flashing green The channel is being calibrated.                                                                                    |
| Steady red No power or major channel fault                                                                                         |
| Flashing red Channel is at the end of range: For 1734-IE2C module: 0 mA or 21 mA For 1734-IE2V module: -0.25V, -10.25V, or +10.25V |

The 1734-OE2C analog output module is a two-channel module that converts a digital code to an analog output current. The module resolution is 13 bits across 0…21 mA.

The 1734-OE2V analog output module is a two-channel module that converts a digital code to an analog output voltage. The module resolution is 14 bits across -10…+10V.

## Data

The 1734-OE2C module operates in Unipolar mode; the 1734-OE2V module operates in Unipolar or Bipolar modes. Data sent to the module is scaled by the user to any 16-bit number. All data sent to the module is signed integer, ranging from –32,768…+32,767 counts.

The 1734-OE2C module:

- Consumes 4 bytes of data (scanner Tx) in this format:
- Channel 0 Data (2 bytes)
- Channel 1 Data (2 bytes)
- Produces 2 bytes of data (scanner Rx) in this format:
- Channel 0 Status (1 byte)
- Channel 1 Status (1 byte)

## Default Data Map – 1734-OE2C and 1734-OE2CK

<!-- image -->

| Message Size: 4 Bytes   | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     | Message Size: 4 Bytes                                                                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         |                                                                                                                                                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|                         | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Message Size: 2 Bytes   | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     |
|                         |                                                                                                                                                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Produce (Rx)            | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  | High Byte - Channel 1 Status Low Byte - Channel 0 Status                                                                                                                                                  |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|                         | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Where:                  | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault |

## The 1734-OE2V module:

- Consumes 4 bytes of data (scanner Tx) in this format:
- Channel 0 Data (2 bytes)
- Channel 1 Data (2 bytes)
- Produces 2 bytes of data (scanner Rx) in this format:
- Channel 0 Status (1 byte)
- Channel 1 Status (1 byte)

## Default Data Map – 1734-OE2V and 1734-OE2VK

<!-- image -->

| Message Size: 4 bytes   | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     | Message Size: 4 bytes                                                                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         |                                                                                                                                                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte                                                                                                                                         |
|                         | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      | Output Channel 1 High Byte Output Channel 1 Low Byte                                                                                                                                                      |
| Message Size: 2 Bytes   | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     | Message Size: 2 Bytes                                                                                                                                                                                     |
|                         |                                                                                                                                                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Produce (Rx)            | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      | High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                                      |
|                         |                                                                                                                                                                                                           |                                                                                                                                                                                                           | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Where:                  | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault |

## Operational Modes

The 1734-OE2C module has these modes:

- 0…20 mA
- 4…20 mA (Default mode)

The 1734-OE2V module has these modes:

- 0… 10V DC (Default mode)
- -10…+10V DC

You can set Channel Mode individually. The effective difference in the two modes is how you apply the scalers. There is no internal offset, meaning that the resolution is not changed.

For the 1734-OE2C module, in both modes, you assign the high scaler the value of 20 mA. For the low scaler you assign the following:

- In 0…20 mA mode, the value of 0 mA
- In 4…20 mA mode, the value of 4 mA

For the 1734-OE2V module, in both modes, you assign the high scaler the value of +10V. For the lower scaler you assign the following:

- In 0…10V mode, the value of 0V
- In ±10V mode, the value of -10V

## Scaling

Scaling is the conversion of unscaled data to engineering units. The high and low scalers (engineering units) are Signed Integers. There are no restrictions on these units.

Default scaling points are 1638 @ 4 mA and 8191 @ 20 mA counts for the 1734-OE2C module and 0 and 10,000 for the 1734-OE2V module. Each scaler can be set individually and on a per-channel basis.

The 1734-OE2C module calculates and outputs a current between 0 mA or 4 mA (low scaler) and 20 mA (high scaler); the 1734-OE2V module calculates and outputs a voltage between -10V or 0V (low scaler) and +10V (high scaler).

Since scalers have no restrictions, use care when configuring the module. If the lower scaler is set to –32,768 and the module is in 4…20 mA (or -10V…+10V) mode, the module is incapable of setting the output to 0 mA (or less than -10V on the 1734-OE2V module) because that requires a number smaller than –32,768. –32,768 is the smallest number that you can represent with a signed integer.

## Fault and Idle/Program Mode Action

You can select what happens to the output if a fault occurs or if the module is in Idle/Program mode. The choices are the following:

- Hold Last State
- Low Clamp
- High Clamp
- User Defined Value

The module default for both Fault and Idle/Program state is Low Clamp. All values are scaled. You can set each action individually and on a per channel basis. For an example of what would happen if the module lost communication, see the table.

| Channel Configuration When A Fault Occurs                                                                                                                                              |                                                    | When the Module is in Idle/Program Mode        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|------------------------------------------------|
| Module Mode = 4…20 mA with Scalers set at 0 and 8191 counts Low Clamp = 0 counts High Clamp = 8191 counts Fault State = User Defined Idle State = Low Clamp Fault Value = 4095 counts  | Channel 0 goes to 4095 counts, which equals 12 mA. | Channel 0 goes to 0 counts, which equals 4 mA. |
| Module Mode = 0…10V with Scalers set at 0 and 10,000 counts Low Clamp = 0 counts High Clamp = 10000 counts Fault State = User Defined Idle State = Low Clamp Fault Value = 5000 counts | Channel 0 goes to 5000 counts, which equals 5V.    | Channel 0 goes to 0 counts, which equals 0V.   |

## Channel Status

The module status bits included in each Channel Status Byte are the following:

- Channel Fault
- CAL Mode
- Low Clamp
- High Clamp

Channel Status can be read individually using RSNetWorx software or by reading the Channel Status Byte in the Module Produce Assembly.

| Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                                      |
|---------------------------------------------------|------------------------------------------------------|
|                                                   | Not Used High Clamp Low Clamp CAL Mode Channel Fault |

- Channel Fault Bit - This general channel health bit (Channel Status Bit 0) indicates that the module is operating with or without faults. If any alarms or faults are detected, this bit is set.
- Calibration Status Bit - This status bit (Channel Status Bit 1) is set when the channel is in Calibration mode. At Begin Calibration, the module is put into Calibration mode. This bit does not get set until the Output Low Reference or Output High Reference commands are sent. Do not confuse this bit with the Bad Calibration Status bit, which is set if the module is not calibrated.
- Low Clamp Status Bit - This status bit (Channel Status Bit 2) is set when the output data is clamped to its minimum level. The default value is -32,768 counts. Low Clamp Status can be read on a per-channel basis or by reading the Module Produce Assembly.
- High Clamp Status Bit - This status bit (Channel Status Bit 3) is set when the output data is clamped to its maximum level. The default value is 32,767 counts. High Clamp Status can be read on a per channel basis or by reading the Module Produce Assembly.

Open-wire Detection (1734-OE2C and 1734-OE2CK only)

This condition has no unique status bit, but if an open-wire condition exists, the general Channel Status bit is set. The module cannot determine what the condition is: open wire or loss of field power. The channel indicators flash red.

Power Fail Detection (1734-OE2V and 1734-OE2VK only)

This condition has no unique status bit, but if a power failure condition exists, the general Channel Status bit is set. The Channel indicators go to steady red.

## Low and High Clamps

The clamps define the maximum and minimum values of the output. These default to the following with the data scaled:

- -32,768 counts (0 mA or 4 mA) and +32,767 counts (21 mA) for the 1734-OE2C module
- -32,768 counts (0 or -10V) and +32,767 counts (+10V) for the 1734-OE2V module

Each clamp can be set individually and on a per-channel basis. When the output value reaches the clamp value, a status bit is set, indicating the output has been clamped. The clamps are absolute. Regardless of what is sent to the module or what the fault state values are, the module does not operate outside these settings.

## Latch Alarms

The latched alarms let low and high clamp status information to be latched. If an output is clamped momentarily, the clamp status bit stays set until a reset latch service is issued. The default setting is Unlatched. Each channel can be configured individually. You can enable the Latch on a per-channel basis.

## Alarm Disable

This function disables all channel alarms and faults so they are not reported in the channel status field. The channel status indicator stays steady green, and Latch Alarms are ignored. Change of state has no effect on module behavior. The default state is Alarms Enabled. Each channel can be configured individually. You can disable Alarms on a per channel basis or they can be set with the Module Configuration Assembly.

## POINTBlock I/O Modules

## Channel Indicators

See the table for channel indicator states for a given module condition.

| Indication     | Probable Cause                                                | Probable Cause                                                |
|----------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Indication     |                                                               | 1734-OE2C, 1734-OE2CK 1734-OE2V, 1734-OE2VK                   |
| Channel Status | Channel Status                                                | Channel Status                                                |
|                | Off The module is in CAL mode.                                | Off The module is in CAL mode.                                |
|                | Steady green The channel is actively controlling the outputs. | Steady green The channel is actively controlling the outputs. |
|                | Flashing green The channel is calibrating.                    | Flashing green The channel is calibrating.                    |
|                | Flashing red Open wire or no power Low/High Clamp alarm       |                                                               |
| Steady red     | Unrecoverable fault - May require device replacement          | Loss of field power                                           |

Mount the 1734D input/output modules on DIN rail with an integrated DeviceNet communication interface, 8 inputs and 8 outputs, removable terminations, and a POINTBus expansion port.

The modules include a non-isolated DeviceNet communication interface. The 24V DC from the DeviceNet connection powers a non-isolated DC/DC converter that generates +5V DC that powers the POINTBlock electronics and connects to the POINTBus port to power the expansion I/O electronics.

| Module            |                         | Voltage   |
|-------------------|-------------------------|-----------|
|                   | Cage Clamp Spring Clamp |           |
| 1734D-IB8XOB8E X  |                         | 12/24V DC |
| 1734D-IB8XOB8ES X |                         | 12/24V DC |
| 1734D-IB8XOW8 X   |                         | 12/24V DC |
| 1734D-IB8XOW8S X  |                         | 12/24V DC |
| 1734D-IA8XOA8 X   |                         | 120V AC   |
| 1734D-IA8XOA8S X  |                         | 120V AC   |
| 1734D-IA8XOW8 X   |                         | 120V AC   |
| 1734D-IA8XOW8S X  |                         | 120V AC   |
| 1734D-IA16 X      |                         | 120V AC   |
| 1734D-IA16S X     |                         | 120V AC   |
| 1734D-IB16 X      |                         | 12/24V DC |
| 1734D-IB16S X     |                         | 12/24V DC |

<!-- image -->

<!-- image -->

## ATTENTION:

- Whatever field power you supply is connected to the internal field power bus. For example, if 120V AC is applied to the power connections, there will be 120V AC applied to the modules through the internal field power bus.
- POINT I/O modules to the right of the module will also have that internal power bus voltage applied, unless you use a 1734-FPD, 1734-EP24DC, or 1734-EPAC module to interrupt and change the field power bus voltage.

I/O messages are sent to (consumer) and received from (producer) the POINT I/O modules. These messages are mapped into the processor's memory.

The 1734D-IB8XOB8E module produces 1 byte of input data (scanner Rx) status. It consumes 1 byte of output data (scanner Tx).

## Default Data Map – 1734D-IB8XOB8E

| Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte                                   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|------------------------|------------------------|------------------------|--------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                        |                        | 76543 21 0             |                                                        |                        |                        |                        |                        |                        |                        |
| Produce (scanner Rx)   |                        |                        | Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Input Data             |                        |                        |                        |                        |                        |                        |
|                        | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On                                 | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On |
| Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte                                   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|                        |                        | 76543 21 0             |                                                        |                        |                        |                        |                        |                        |                        |
| Consume (scanner Tx)   |                        |                        | Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Output Data (or State) |                        |                        |                        |                        |                        |                        |
|                        | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On                                 | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On | Where: 0 = Off, 1 = On |

The 1734D-IB8XOW8 module produces 1 byte of input data (scanner Rx) status. It consumes 1 byte of output data (scanner Tx).

## Default Data Map – 1734D-IB8XOW8

| Message Size: 1 Byte                                             | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|------------------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                                                                  | 76543 21 0             |                        |                        |                        |                        |                        |                        |                        |                        |
| Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Input Data  |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where: 0 = Off, 1 = On                                           |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Message Size: 1 Byte                                             | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|                                                                  |                        | 765432 1 0             |                        |                        |                        |                        |                        |                        |                        |
| Consume (scanner Tx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Output Data |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where 0 = Off, 1 = On                                            |                        |                        |                        |                        |                        |                        |                        |                        |                        |

The 1734D-IA8XOA8 module produces 1 byte of input data (scanner Rx) status. It consumes 1 byte of output data (scanner Tx).

## Default Data Map - 1734D-IA8XOA8

| Message Size: 1 Byte                                             | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|------------------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                                                                  | 7654321 0              |                        |                        |                        |                        |                        |                        |                        |                        |
| Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Input Data  |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where: 0 = Off, 1 = On                                           |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Message Size: 1 Byte                                             | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|                                                                  | 7654321 0              |                        |                        |                        |                        |                        |                        |                        |                        |
| Consume (scanner Tx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Output Data |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where: 0 = Off, 1 = On                                           |                        |                        |                        |                        |                        |                        |                        |                        |                        |

The 1734D-IA8XOW8 module produces 1 byte of input data (scanner Rx) status) It consumes 1 byte of output data (scanner Tx).

## Default Data Map - 1734D-IA8XOW8

| Message Size: 1 Byte                                             | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|------------------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                                                                  | 7654321 0              |                        |                        |                        |                        |                        |                        |                        |                        |
| Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Input Data  |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where: 0 = Off, 1 = On                                           |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Message Size: 1 Byte                                             | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   | Message Size: 1 Byte   |
|                                                                  | 7654321 0              |                        |                        |                        |                        |                        |                        |                        |                        |
| Consume (scanner Tx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Output Data |                        |                        |                        |                        |                        |                        |                        |                        |                        |
| Where: 0 = Off, 1 = On                                           |                        |                        |                        |                        |                        |                        |                        |                        |                        |

The 1734D-IA16 module produces 2 bytes of input data (scanner Rx). It does not consume output data (scanner Tx).

## Default Data - 1734D-IA16

| Message Size: 2 Bytes   | Message Size: 2 Bytes                  | Message Size: 2 Bytes                                 | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  | Message Size: 2 Bytes                  |
|-------------------------|----------------------------------------|-------------------------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|                         |                                        | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                 |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |
| Produce (scanner Rx)    |                                        | I15 I14 I13 I12 I11 I10 I9 I8 I7 I6 I5 I4 I3 I2 I1 I0 |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |
| Consume (scanner Tx)    | No consumed data                       | No consumed data                                      | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       |
|                         | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On                | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On |

For 1734D-IB16 modules, I/O messages are sent to (consumer) and received from (producer) the POINTBlock I/O modules. These messages are mapped into the processors memory. This module produces 2 bytes of input data (scanner Rx) and does not consume output data (scanner Tx).

## Default Data - 1734D-IB16

| Message Size: 2 bytes   | Message Size: 2 bytes                  | Message Size: 2 bytes                                 | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  | Message Size: 2 bytes                  |
|-------------------------|----------------------------------------|-------------------------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
|                         |                                        | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                 |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |
| Produce (scanner Rx)    |                                        | I15 I14 I13 I12 I11 I10 I9 I8 I7 I6 I5 I4 I3 I2 I1 I0 |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |                                        |
| Consume (scanner Tx)    | No consumed data                       | No consumed data                                      | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       | No consumed data                       |
|                         | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On                | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On | Where: Ix = Channel x; 0 = Off, 1 = On |

## Notes:

## Tools Required to Calibrate Your Analog Modules

## Calibrate Your Analog Modules

Read this chapter for information about how to calibrate analog modules. Your analog I/O module is factory-calibrated. You may choose to recalibrate your module in your system to increase its accuracy for your specific application. This chapter covers the following:

- Tools required to calibrate analog modules
- How to calibrate analog current input modules
- How to calibrate analog current output modules
- How to calibrate analog voltage input modules
- How to calibrate analog voltage output modules

You do not have to configure a module before you calibrate it. If you decide to calibrate your analog I/O modules first, you can configure it at the same time.

## IMPORTANT

Analog I/O modules can be calibrated on a channel by channel basis or with the channels grouped together. Regardless of which option you choose, we recommend you calibrate all channels on your module each time you calibrate. This helps you maintain consistent calibration readings and improve module accuracy.

Calibration is meant to correct any hardware inaccuracies that may be present on a particular channel or in your system. The calibration procedure compares a known standard, either input signal or recorded output, with the channels performance and then calculates a linear correction factor between the measured and the ideal.

The linear correction factor is applied on every input or output in the same manner to obtain maximum accuracy.

When you calibrate input modules, use current or voltage calibrators to send a signal to the module to calibrate it.

When you calibrate output modules, use a digital multimeter to measure the signal that the module is sending out.

To maintain your modules accuracy specifications, we recommend you use calibration instruments with specific ranges. See Table 7 for a list of the recommended instruments for each module.

Table 7 - Calibration Instruments for Your Analog Modules

| Module Recommended Instrument Range                           |
|---------------------------------------------------------------|
| 1734-IE2C or 1734-IE2CK 1…20 mA (±0.15 µA) current source     |
| 1734-OE2C or 1734-OE2CK Digital multimeter better than 0.6 µA |
| 1734-IE2V Voltage source 0…10V (±0.3 mV)                      |
| 1734-OE2V Digital multimeter better than 0.5 mV               |

You must be online to calibrate your analog I/O modules. We recommend the module not be actively controlling a process when you calibrate it.

| IMPORTANT   | The module ignores output data sent to the module until after calibration ends. This could be hazardous if active control were attempted during calibration.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|

Input calibration consists of the following steps for an example of 2 channels:

<!-- image -->

## Calibrate the Analog Current Input Module

1. Connect the calibration system.
2. Allow the system to warm up for at least 10 minutes.
3. Connect a current or voltage source to channel 0 by applying 4 mA (current) or 0V (voltage).
4. Begin the calibration.
5. Select both channels.
6. Accept Low Calibration for channel 0 (both status indicators flash).
7. Set the current or voltage source to a high value (20 mA current; or +10V voltage).
8. Accept High Calibration for channel 0 (channel 0 status indicator turns off if calibration was good, but channel 1 status indicator still flashing).
9. Connect a current or voltage source to channel 1.
10. With High Calibration now applied to channel 1, accept High Calibration for channel 1.
11. Set the current or voltage source to Low value.
12. Accept Low Calibration for channel 1.

To calibrate your current input module, connect the module in a system similar to that shown in the below figure.

## IMPORTANT

Apply power to the power supply and module for at least 10 minutes before calibrating the module. This allows the internal temperatures to stabilize and reduces drift errors.

<!-- image -->

1. Double-click the icon to bring up the General parameter dialog.

<!-- image -->

From the General parameter dialog, select Device Parameters tab. The EDS Editor dialog appears.

<!-- image -->

2. From the EDS Editor dialog, select Upload to load the configuration from the device.
3. The Device Parameters dialog appears. From the Groups dropdown list, select Calibration.

<!-- image -->

4. Select Calibration Command from the Parameter column, then set its value to Begin Calibration. Make sure that Single is selected.
5. Select Download To Device.

<!-- image -->

Both channel status indicators turn off.

6. Select Calibration Channel Select from the Parameter column, then set its value to a channel which you want to calibrate.
7. Select Download To Device.
8. Set current source to 4.00 mA.
9. Select Calibration Command from Parameter column and set its value to Accept Low Calibration from the dropdown list.

<!-- image -->

<!-- image -->

## Calibrate the Analog Current Output Module

10. Select Download To Device.

The status indicator for the channel being calibrated flashes.

11. Set the current source to 20 mA.
12. Select Calibration Command from Parameter column and set its value to Accept High Calibration from the dropdown list.
13. Select Download To Device.

Calibration is complete when High and Low calibration for the selected channels are done successfully.

14. Repeat the above steps to calibrate the other channels, noting that both high and low inputs must be accepted in order for the module to finish calibration.

Calibration is now complete. If the module does not accept calibration (the status indicator still flashing), select Abort Calibration option from the dropdown list and start over.

To calibrate your output module, connect the module in a DeviceNet system similar to the one shown in the figure, and follow this procedure.

## IMPORTANT

Apply power to the power supply and module for at least 10 minutes before calibrating the module. This allows internal temperatures to stabilize and reduces drift errors.

<!-- image -->

1. Double-click the icon to bring up the General parameter dialog.

<!-- image -->

2. From the General parameter dialog, select Device Parameters tab. The EDS editor dialog appears.
3. From the EDS editor dialog, select Upload to load the configuration from the device.
4. The Device Parameters dialog appears. From the Groups dropdown list, select Calibration.
5. Select Calibration Command from Parameter column and set its value to Begin Calibration.
6. Select Download To Device.
7. Select Calibration Channel Select from the Parameter column and set its value to a channel which you want to calibrate.

<!-- image -->

<!-- image -->

<!-- image -->

8. Select Download To Device.
9. Select Calibration Command from the Parameter column and set its value to Output Low Reference.
10. Select Download To Device.

<!-- image -->

The selected channel status indicator flashes green.

<!-- image -->

11. Enter the value shown on your digital voltmeter (DVM) for the Channel Low Value (4.044 in the example).

<!-- image -->

12. Select Calibration Command from the Parameter column and set its value to Output High Reference.
13. Select Download To Device.
14. Enter the value shown on the DVM (which is 20.231 in this example) for Channel High Value parameter.
15. Repeat these steps for the other channel.
16. From the Device Parameters dialog, select All.

<!-- image -->

Select Calibration Command from Parameter column and set its value to Finish Calibration to complete the calibration process.

17. From the Device Parameters dialog, select Apply.
18. The EDS Editor dialog appears. From the EDS Editor dialog, select Yes to download the configuration to the device.

<!-- image -->

<!-- image -->

## Calibrate the Analog Voltage Input Module

If calibration is done, the value of the Bad Cal Status reflects Good Calibration.

<!-- image -->

Your module is now calibrated.

To calibrate your voltage input module, connect the module in a DeviceNet system similar to that shown in the below figure.

## IMPORTANT

Apply power to the power supply and module for at least 10 minutes before calibrating the module. This allows internal temperatures to stabilize and reduces drift errors.

You can calibrate both voltage input channels at the same time using one voltage source.

<!-- image -->

1. Double-click the icon to bring up the General parameter dialog.
2. Select Device Parameters to view the parameters.
3. From the EDS Editor dialog, select Upload to load the configuration from the device.
4. The Device Parameters dialog appears. Select Calibration from the Groups dropdown list.

The EDS Editor dialog appears.

<!-- image -->

<!-- image -->

<!-- image -->

5. Select Calibration Channel Select from the Parameter column and set its value to a channel you want to calibrate.
6. Select Calibration Command from the Parameter column and set its value to Begin Calibration from the dropdown list.

<!-- image -->

## Select Apply.

<!-- image -->

7. Select Download To Device. Both channel status indicators turn off.
8. Apply 0.0V to the input.
9. From Device Parameters dialog, change the Calibration Command value to Accept Low Calibration.
10. Select Download To Device.

The status indicator for the channel being calibrated flashes.

<!-- image -->

## Calibrate the Analog Voltage Output Module

11. Set the voltage source to +10.0V.
12. From Device Parameters dialog, change the Calibration Command value to Accept High Calibration.
13. Select Download To Device.

Calibration is complete as soon as High and Low calibration for the selected channels

- are done successfully.
14. Repeat these steps to calibrate the other channels, if necessary. Both high and low inputs must be accepted in order for the module to finish calibration. Calibration is now complete. If the module does not accept calibration (the status indicator is still flashing), from the Device Parameters dialog, change the Calibration
- Command value to Abort Calibration and do this procedure again.

To calibrate your output module, connect the module in a DeviceNet system similar to that shown in the below figure and use this procedure.

## IMPORTANT

Apply power to the power supply and module for at least 10 minutes before calibrating the module. This allows internal temperatures to stabilize and reduces drift errors.

<!-- image -->

1. Double-click the icon to bring up the General parameter dialog.
2. From General parameter dialog, select Device Parameters tab.

<!-- image -->

3. The EDS Editor dialog appears. From the EDS Editor dialog, select Upload to load the configuration from the device.
4. The Device Parameters dialog appears. Select Calibration from the Groups dropdown list.
5. Select Calibration Channel Select from the Parameter column and set its value to a channel you want to calibrate.
6. Select Calibration Command and set its value to Begin Calibration, then select Apply.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

7. Select Download To Device.

The channel status indicator turns off.

8. Select a channel.
9. Select Download To Device.
10. Change the Calibration Command value to Output Low Reference, then select Download To Device.

The selected channel status indicator flashes green.

<!-- image -->

11. Enter the value shown on your DVM (-10.1234 in the example) for the Channel Low Value.
12. Change the Calibration Command value to Output High Reference, then select Download To Device.

<!-- image -->

13. Enter the value shown on the DVM (10.0057 in this example) for the Channel High Value.
14. Repeat these steps for the other channels.
15. From the Device Parameters dialog, select All.

<!-- image -->

Change the Calibration Command value to Finish Calibration, then select Apply to complete the calibration process.

<!-- image -->

The EDS Editor dialog appears.

16. From the EDS Editor dialog, select Yes to download the configuration to the module.

<!-- image -->

If calibration is done, the Bad Cal Status reflects Good Calibration.

<!-- image -->

Your module is now calibrated.

## About Module Diagnostics

<!-- image -->

## Troubleshoot with the Indicators

Read this chapter for information about troubleshooting with the following indicators:

- Module status
- Network status
- Power indication
- Calibration status
- I/O point status (On/Off/Fault or Diagnostic)

See each module's individual indicators for detailed information.

All status and diagnostic information (strobed, polled, cyclic, or change of state) is reported back over the network communication adapter. A single point of failure is detected and reported at the module and to the control system.

<!-- image -->

## Network and Module Status Indications

## Network and Module Status Indications

|                    |                                                                                                                                                                                                                                       | Indication Probable Cause Recommended Action                                                 |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Module Status      |                                                                                                                                                                                                                                       |                                                                                              |
|                    | Off No power is applied to the device. Apply power to the device.                                                                                                                                                                     |                                                                                              |
|                    | Steady green The device is operating normally. None                                                                                                                                                                                   |                                                                                              |
| Flashing green     | The device needs commissioning due to configuration missing, incomplete, or incorrect.                                                                                                                                                | Configure the device properly.                                                               |
| Flashing red       | A recoverable fault is present. The device did not pass the internal test.                                                                                                                                                            | 1. Cycle power to the device. 2. If the condition persists, replace the device.              |
|                    | Steady red An unrecoverable fault - May require device replacement Replace the device.                                                                                                                                                |                                                                                              |
|                    | Flashing red/green The device is in self-test. None                                                                                                                                                                                   |                                                                                              |
| Network Status     |                                                                                                                                                                                                                                       |                                                                                              |
| Off                | The device is not online. – The device has not completed Autobaud detection because there is no network traffic. – The device has not completed the dup_MAC_id test. – The device is not powered - Check the module status indicator. | Apply power to the device, wait for the MAC_id to complete, and correct, as needed.          |
|                    | Flashing green The device is online but has no connections in the established state. None - The device is in Idle or Program mode                                                                                                     | .                                                                                            |
|                    | Steady green The device is online and has connections in the established state. None                                                                                                                                                  |                                                                                              |
|                    | Flashing red One or more I/O connections are in a timed-out state. Check for I/O module failure, and correct, as needed.                                                                                                              |                                                                                              |
| Steady red         | Critical link failure is present with a failed communication device. The device has detected an error that prevents it from communicating on the network.                                                                             | Verify that the adapter and terminal bases are properly installed, and reinstall, as needed. |
| Flashing red/green | Communication faulted device - The device has detected a network access error and is in a communication faulted state. The device has received and accepted an Identify Communication Faulted Request - Long protocol message.        | Verify that the adapter is properly installed, and reinstall, as needed.                     |

The network and module status indications are the same for all modules.

<!-- image -->

## Troubleshoot Digital Modules

The I/O status indicators provide input and output indications for each module. Individual meanings are indicated in the tables.

## 1734-IB2, 1734-IB4, 1734-IB4K, 1734-IB8, 1734-IB8K Sink Input Module

<!-- image -->

| Indication Probable Cause Recommended Action   |
|------------------------------------------------|
| I/O Status                                     |
| Off Input is in the Off state. None            |
| Yellow Input is in the On state. None          |

## 1734-IB4D Sink Input Module with Diagnostics

<!-- image -->

| Indication Probable Cause Recommended Action                           |            |
|------------------------------------------------------------------------|------------|
| I/O Status                                                             | I/O Status |
| Off Input is in the Off state. None                                    |            |
| Yellow Input is in the On state. None                                  |            |
| Red A short circuit is detected. Check I/O wiring or terminal base.    |            |
| Flashing red Open wire is detected. Check I/O wiring or terminal base. |            |

## 1734-OB2E, 1734-OB4E, 1734-OB8E, 1734-OB8EK Source Output Modules

<!-- image -->

| Indication Probable Cause Recommended Action                                                                     |
|------------------------------------------------------------------------------------------------------------------|
| Off All outputs are inactive. None                                                                               |
| Yellow  One or more outputs are active and under control.  None                                                  |
| Flashing red Open circuit is detected - No load (Off state only). Connect the load or disable no load detection. |
| Steady red A short circuit is detected (On state only). Remove the short or overloaded circuit.                  |

## 1734-OB2, 1734-OB4, 1734-OB4K, 1734-OB8, 1734-OB8K Source Output Modules

<!-- image -->

| Indication Probable Cause Recommended Action                  |
|---------------------------------------------------------------|
| I/O Status                                                    |
| Off All outputs are inactive. None                            |
| Yellow One or more outputs are active and under control. None |

## 1734-OB2EP Protected Output Module

<!-- image -->

| Indication Probable Cause Recommended Action                                                                     |
|------------------------------------------------------------------------------------------------------------------|
| Off All outputs are inactive. None                                                                               |
| Yellow  One or more outputs are active and under control.  None                                                  |
| Flashing red Open circuit is detected - No load (Off state only). Connect the load or disable no load detection. |
| Steady red A short circuit is detected (On state only). Remove the short or overloaded circuit.                  |

## 1734-IV2, 1734-IV4, 1734-IV8, 1734-IV8K Source Input Module

<!-- image -->

| Indication Probable Cause Recommended Action   |
|------------------------------------------------|
| I/O Status                                     |
| Off Input is in the Off state. None            |
| Yellow Input is in the On state. None          |

## 1734-OV2E, 1734-OV4E, 1734-OV8E, 1734-OV8EK Protected Sink Output Module

<!-- image -->

|            |                                                                                          | Indication Probable Cause Recommended Action   |
|------------|------------------------------------------------------------------------------------------|------------------------------------------------|
| I/O Status | I/O Status                                                                               |                                                |
|            | Off All outputs are inactive. None                                                       |                                                |
| Yellow     | One or more outputs are active and under control.                                        | None                                           |
|            | Red A short circuit is detected (On state only). Remove the short or overloaded circuit. |                                                |

## 1734-OW2, 1734-OW4, 1734-OW4K Relay Output Module

## 1734-OW2

<!-- image -->

## 1734-OW4, 1734-OW4K

<!-- image -->

| Indication Probable Cause Recommended Action   |
|------------------------------------------------|
| I/O Status                                     |
| Off Output is Off (contacts open) None         |
| Yellow Output is On (contacts closed) None     |

## 1734-OX2 Relay Output Module

<!-- image -->

| Indication Probable Cause Recommended Action   |
|------------------------------------------------|
| I/O Status                                     |
| Off Output is Off None                         |
| Yellow Output is On None                       |

## 1734-IA2, 1734-IA4, 1734-IA4K 120V AC Input Module

<!-- image -->

| Indication Probable Cause Recommended Action   |
|------------------------------------------------|
| I/O Status                                     |
| Off Input is in the Off state. None            |
| Yellow Input is in the On state. None          |

## 1734-OA2, 1734-OA4, 1734-OA4K 120/220V AC Output Module

<!-- image -->

| Indication Probable Cause Recommended Action                  |
|---------------------------------------------------------------|
| I/O Status                                                    |
| Off All outputs are inactive. None                            |
| Yellow One or more outputs are active and under control. None |

## 1734-IM2, 1734-IM4 220V AC Input Module

<!-- image -->

| Indication Probable Cause Recommended Action   |
|------------------------------------------------|
| I/O Status                                     |
| Off Input is in the Off state. None            |
| Yellow Input is in the On state. None          |

## Troubleshoot Analog Modules

Each analog module has I/O indicators to show the status of the inputs/outputs. See the individual module for I/O status information.

## 1734-IE2C, 1734-IE2CK Analog Current Input Module

<!-- image -->

|                |                                                           | Indication Probable Cause Recommended Action        |
|----------------|-----------------------------------------------------------|-----------------------------------------------------|
| Channel Status | Channel Status                                            | Channel Status                                      |
|                | Off The module is in CAL mode. None                       |                                                     |
| Steady green   | Normal operation is present with channel scanning inputs. | None                                                |
| Flashing green | The channel is being calibrated. None                     |                                                     |
|                | Steady red No power or major channel fault is present.    | Apply field power or replace the module, as needed. |
| Flashing red   | The channel is at the end of the range (0 mA or 21 mA).   | Operate within the normal range.                    |

## 1734-OE2C, 1734-OE2CK Analog Current Output Module

<!-- image -->

|                |                                                                    | Indication Probable Cause Recommended Action                  |
|----------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| Channel Status | Channel Status                                                     | Channel Status                                                |
|                | Off The module is in CAL mode. None                                |                                                               |
|                | Steady green The channel is actively controlling the outputs. None |                                                               |
| Flashing green | The channel is calibrating. None                                   |                                                               |
| Steady red     | An unrecoverable fault - May require device replacement            | Replace the device.                                           |
|                | Flashing red No power or open wire is present.                     | Apply power or verify wiring to load, and correct, as needed. |

## 1734-IE2V, 1734-IE2VK Analog Voltage Input Module

<!-- image -->

|                |                                                                       | Indication Probable Cause Recommended Action        |
|----------------|-----------------------------------------------------------------------|-----------------------------------------------------|
| Channel Status | Channel Status                                                        | Channel Status                                      |
|                | Off The module is in CAL mode. None                                   |                                                     |
| Steady green   | Normal operation is present with channel scanning inputs.             | None                                                |
| Flashing green | The channel is being calibrated. None                                 |                                                     |
|                | Steady red No power or major channel fault is present.                | Apply field power or replace the module, as needed. |
| Flashing red   | The channel is at the end of the range (-0.25V, -10.25V, or +10.25V). | Operate within the normal range.                    |

## Troubleshoot I/O Communication Modules

## 1734-OE2V, 1734-OE2VK Analog Voltage Output Module

<!-- image -->

|                                                                                   | Indication Probable Cause Recommended Action   |
|-----------------------------------------------------------------------------------|------------------------------------------------|
| Off The module is in CAL mode. None                                               |                                                |
| Steady green  Normal operation present with channel actively controlling outputs. | None                                           |
| Flashing green The channel is being calibrated. None                              |                                                |
| Flashing red A Low or High Clamp alarm is present.                                | Operate within the normal range.               |
| Steady red No field power is present. Apply the field power.                      |                                                |

The status indicators on the communication modules provide system power and DeviceNet power indications.

## 1734-PDN DeviceNet Communication Interface Module

<!-- image -->

|                 |       |                                                                                                  | Indicator Indication Probable Cause Recommended Action                                                                                                               |
|-----------------|-------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| System Power    | Off   | • The device is not active. • DeviceNet power is Off, or the DC-DC converter problem is present. | 1. Verify that DeviceNet power is On, and apply the power, if needed. 2. Verify that backplane power is not exceeded, and correct, as needed. 3. Replace the module. |
| System Power    | Green | • System power is On. • DC-DC converter is active (5V).                                          | None                                                                                                                                                                 |
| DeviceNet Power | Off   | • The device is not active. • DeviceNet power is Off.                                            | Apply 24V power to the DeviceNet.                                                                                                                                    |
| DeviceNet Power | Green | Power is On with 24V present.                                                                    | None                                                                                                                                                                 |

## 1734-ADN, 1734-ADNX DeviceNet Adapter

<!-- image -->

## Adapter Status

|                     |                                                                                        | Indication Probable Cause Recommended Action                                                                                 |
|---------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|                     | Off No power is applied to the device. Apply power to the device.                      |                                                                                                                              |
|                     | Steady green The device is operating normally. None                                    |                                                                                                                              |
| Flashing green      | The device needs commissioning due to configuration missing, incomplete, or incorrect. | Check the configuration and recommission the adapter.                                                                        |
|                     | Flashing red A recoverable fault is present.                                           | 1. Make sure that the adapter does not need a FLASH update. 2. Verify that the MAC_id switch has not changed since power-up. |
| Steady red          | An unrecoverable fault - May require device replacement                                | Replace the adapter.                                                                                                         |
| Flashing red/ green |                                                                                        | The device is in self-test. Wait for the self-test to finish.                                                                |

## DeviceNet Status

|                     |                                                                                                                                                                                                                            | Indication Probable Cause Recommended Action                                                 |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Off                 | The device is not online. • The device has not completed the Dup_MAC_ID test. • The device is not powered - Check the module status indicator.                                                                             | Apply power to the device, wait for no duplicate MAC_id to complete, and correct, as needed. |
| Flashing green      | The device is online, but has no connections in the established state.                                                                                                                                                     | None - The device is in Idle or Program mode.                                                |
| Steady green        | The device is online and has connections in the established state.                                                                                                                                                         | None                                                                                         |
|                     | Flashing red One or more I/O connections are in a timed-out state.                                                                                                                                                         | Check for I/O module failure, and correct, as needed.                                        |
| Steady red          | Critical link failure is present with a failed communication device. The device has detected an error that prevents it from communicating on the network.                                                                  | Verify that the adapter and terminal bases are properly installed, and reinstall, as needed. |
| Flashing red/ green | Communication faulted device - The device has detected a network access error and is in a communication faulted state. The device received and accepted an Identify Communication Faulted Request - Long protocol message. | Verify that the adapter is properly installed, and reinstall, as needed.                     |

## Subnet and POINTBus Status

|                |                                                                                                                                                      | Indication Probable Cause Recommended Action                                                                                                              |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off            | The device is not online. • The device has not completed the Dup_MAC_ID test. • The device is not powered - Check the module status indicator.       | Check the adapter status indicator to determine if more time is needed to complete the dup_MAC_id test or if the adapter needs to be powered.             |
| Flashing green | The device is online but has no connections in the established state.                                                                                | None                                                                                                                                                      |
| Steady green   | The device is online and has connections in the established state.                                                                                   | None                                                                                                                                                      |
|                | Flashing red No scan list is available. I/O module is missing.                                                                                       | 1. Make sure all I/O modules are connected and using the correct MAC IDs. 2. Check the Cycling Node Status parameter in RSNetWorx for DeviceNet software. |
| Steady red     | Critical link failure - Failed communication device is present. The device has detected an error that prevents it from communicating on the network. | 1. Make sure an I/O module is not using a MAC ID = 0. 2. Make sure that all backplane modules are communicating at the proper communication rate.         |

## System Power

|                                                                    | Indication Probable Cause Recommended Action                                                                             |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Off  Field power is Off or DC-DC converter problem is present.     | 1. Verify that field power is On. 2. Verify that backplane power (load current) is not exceeded. 3. Replace the adapter. |
| Green System power is On. The DC-DC converter is active (5V). None |                                                                                                                          |

## Field Power

| Indication Probable Cause Recommended Action     |
|--------------------------------------------------|
| Off Field power is Off. Turn on the field power. |
| Green Power is On with 24V present. None         |

## Module Status

|                                                                                                                                              | Indication Probable Cause Recommended Action                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Off No power is applied to the device. Apply power to the device.                                                                            |                                                                                                                        |
| Alternating red/green LED power cycle test (module self-test) is present. None                                                               |                                                                                                                        |
| Flashing red Recoverable fault has occurred: • Firmware (NVS) update • MAC ID changed • CPU load exceeded                                    | • Complete firmware update. • Return the module to correct the node address. • Reduce the CPU load.                    |
| Steady red Unrecoverable fault has occurred: • Self-test failure (checksum failure or ramtest failure at power cycle) • Firmware fatal error | Replace the adapter.                                                                                                   |
|                                                                                                                                              | Flashing green Waiting for the connection or ControlNet cable break Check the cable and make the connection as needed. |
| Steady green The module is operating correctly (normal mode). None                                                                           |                                                                                                                        |

## POINTBus Status

|                |                                                                                                                                                                                           | Indication Probable Cause Recommended Action                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|                | Off The device is not powered - Check the module status indicator. Apply power to the device.                                                                                             |                                                                                                                                                    |
|                | Alternating red/green LED power cycle test is present. None                                                                                                                               |                                                                                                                                                    |
| Flashing red   | Recoverable fault has occurred: • At power-up the number of expected modules does not equal the number of modules present • A module is missing • Node fault (I/O connection timeout)     | • Change chassis size to match the number of modules present. • Replace the missing module. • Check for I/O Module failure and correct, as needed. |
| Flashing green | Adapter online with no connections established • Adapter chassis size has not been configured. • The controller is in Program/Idle mode. • ControlNet cable break • Firmware (NVS) update | • Set the adapter chassis size. • None • Check the cable and connect, as needed. • Complete the firmware update.                                   |
| Steady green   | Adapter is online with connections established (normal operation, in run mode).                                                                                                           | None                                                                                                                                               |
|                | Steady red An unrecoverable fault has occurred - The adapter is bus off.                                                                                                                  | 1. Cycle power to the device. 2. If the condition persists, replace the device.                                                                    |

## 1734-ACNR ControlNet Adapter

<!-- image -->

## ControlNet A or B Status

|                              |                                                                                               | Indication Probable Cause Recommended Action                                                                                          |
|------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Viewed Together (A and B)    | Viewed Together (A and B)                                                                     | Viewed Together (A and B)                                                                                                             |
|                              | Both steady Off Reset, no power, or entire network interface deactivated None or cycle power. |                                                                                                                                       |
|                              | Alternating red/green Self-test mode is present. None                                         |                                                                                                                                       |
|                              |                                                                                               | Alternating red/Off Incorrect configuration is present. Check network address and other ControlNet configuration parameters.          |
|                              | Both steady red Faulted unit is present.                                                      | Cycle power or reset the unit. If the fault persists, contact Allen-Bradley representative or distributor.                            |
| Viewed Individually (A or B) | Viewed Individually (A or B)                                                                  | Viewed Individually (A or B)                                                                                                          |
|                              |                                                                                               | Steady Off The channel is disabled. Program network for redundant media, if necessary.                                                |
|                              | Flashing red/green Incorrect network configuration is present.                                | Cycle power or reset the unit. If the fault persists, contact Allen-Bradley representative or distributor.                            |
| Flashing red/Off             | • Media fault • No other nodes are present on the network.                                    | • Check media for items such as broken cables, loose connectors, and missing terminators. • Add other nodes to the network.           |
| Flashing green/Off           | • Temporary channel errors are present. • The node is not configured to go on line.           | Make sure that the configuration manager node is present and working and the selected address is not greater than selected UMAX (1) . |
| Steady green                 | Normal operation - MAC frames are being received without detected errors.                     | None                                                                                                                                  |

## System Power

|                                                                             | Indication Probable Cause Recommended Action                                                                             |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Off  Not active - Field power is Off or DC-DC converter problem is present. | 1. Verify that field power is On. 2. Verify that backplane power (load current) is not exceeded. 3. Replace the adapter. |
| Green System power is On and the DC-DC converter is active (5V). None       |                                                                                                                          |

## Field Power

| Indication Probable Cause Recommended Action                    |
|-----------------------------------------------------------------|
| Off Not active - Field power is Off. Apply power to the device. |
| Green Power is On - 24V is present. None                        |

## Adapter Status

|                                                                                               | Indication Probable Cause Recommended Action                 |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Off • No power is supplied. • Hardware check is in progress. • Initialization is in progress. | 1. Apply the power. 2. Wait for power self-test to complete. |
| Green Operation is normal. None                                                               |                                                              |
| Red Hardware check fault is present. Replace the device.                                      |                                                              |

## PROFIBUS Status

|              |                                                                                                                                                                                                                                                                                            | Indication Probable Cause Recommended Action                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Off          | No power is supplied. The bus is offline.                                                                                                                                                                                                                                                  | Apply power, verify the network cabling, and correct, as needed.                  |
|              | Steady green Bus is online (data exchange). None                                                                                                                                                                                                                                           |                                                                                   |
|              | Flashing green Adapter received a CLEAR command from the master. None                                                                                                                                                                                                                      |                                                                                   |
| Steady red   | Error in PROFIBUS initialization is present. No modules are installed in the backplane.                                                                                                                                                                                                    | Verify the configuration, proper installation of modules, and correct, as needed. |
| Flashing red | 1 Hz - Check_Configuration telegram is rejected. The maximum number of POINT I/O modules in master configuration are overridden. 2 Hz - SetPrm telegram is rejected. The first byte in user parameter data does not equal zero. The maximum number of user parameter bytes are overridden. | Check the configuration.                                                          |

## POINTBus Status

|              |                                                                                                 | Indication Probable Cause Recommended Action                                                              |
|--------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Off          | • No power is supplied. • Hardware check is in progress. • Initialization is in progress.       | Apply the power.                                                                                          |
|              | Steady green Normal operation is present. None                                                  |                                                                                                           |
| Flashing red | 1 Hz - Incorrect POINT I/O module is installed. POINT I/O module is removed from the backplane. | Verify the module installation, no modules removed, and correct, as needed.                               |
|              |                                                                                                 | Steady red Critical link failure (BUS_OFF) is present. Check the network cabling, and correct, as needed. |

## 1734-APB PROFIBUS Adapter

<!-- image -->

## System Power

| Indication Probable Cause Recommended Action                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off System power is not applied. 1. Verify that the field power is On. 2. Verify that the backplane power (load current) is not exceeded. 3. Replace the adapter. |
| Green System power (5V) is present. None                                                                                                                          |

## Field Power

| Indication Probable Cause Recommended Action                 |
|--------------------------------------------------------------|
| Off Field power is not applied. Apply the field power (24V). |
| Green Field power (24V) is applied. None                     |

## 1734-AENT EtherNet/IP Adapter

<!-- image -->

## Module Status

|                                                                                                                                                                          | Indication Probable Cause Recommended Action                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| Off No power is applied to the device. Apply power to the device.                                                                                                        |                                                                |
| Flashing red/green LED power cycle test (module self-test) is present. None                                                                                              |                                                                |
| Steady green The device is operating normally. None                                                                                                                      |                                                                |
| Flashing red A recoverable fault has occurred. • Firmware (NVS) update is present. • Address switches have changed.                                                      | • Complete the firmware update. • Verify the address switches. |
| Steady red An unrecoverable fault has occurred. • Self-test failure is present (checksum failure, or ramtest failure at power cycle). • Firmware fatal error is present. | Replace the adapter.                                           |

## POINTBus Status

|                                                                                                                                                                                                                     | Indication Probable Cause Recommended Action                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Off The device is not powered - Check the module status indicator. Apply power to the device.                                                                                                                       |                                                                                                                                         |
| Flashing red/green LED power cycle test is present. None                                                                                                                                                            |                                                                                                                                         |
| Flashing red A recoverable fault occurred: • At power cycle the number of expected modules does not equal the number of modules present. • A module is missing. • Node fault (I/O connection timeout) has occurred. | • Configure the chassis size. • Check for missing module and reinstall as needed. • Check for I/O module failure and correct as needed. |
| Steady red An unrecoverable fault has occurred - The adapter is bus off.                                                                                                                                            | 1. Cycle power to the device. 2. If the condition persists, replace the device.                                                         |
| Flashing green Firmware (NVS) update is in progress. None                                                                                                                                                           |                                                                                                                                         |
| Steady green  Adapter is online with connections established (normal operation, Run mode).                                                                                                                          | None                                                                                                                                    |

## System Power

| Indication Probable Cause Recommended Action                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Not active - The field power is Off or DC-DC converter problem is present. 1. Verify that power is On, and apply power if needed. 2. Verify that backplane power is not exceeded, and correct, as needed. 3. Replace the adapter. |
| Green System power is On. The DC-DC converter is active (5V). None                                                                                                                                                                    |

## Field Power

| Indication Probable Cause Recommended Action                    |
|-----------------------------------------------------------------|
| Off Not active - The field power is Off. Apply the field power. |
| Green Power is On. 24V is present. None                         |

## Network Activity

| Indication Probable Cause Recommended Action                                    |
|---------------------------------------------------------------------------------|
| Off No link is established. Verify the network cabling, and correct, as needed. |
| Flashing green/Off Transmit or receive activity is present. None                |
| Steady green Link is established. None                                          |

## Network Status

|                                                                                                                             | Indication Probable Cause Recommended Action                                                         |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Off The device is not initialized. The module does not have an IP address.                                                  | Apply power to the device, verify the IP address, and correct, as needed.                            |
| Flashing green  No CIP™ connections are present. The device has an IP address, but no CIP connections are established.      | None                                                                                                 |
| Steady green  CIP connections are present. The device is online and has an IP address, and CIP connections are established. | None                                                                                                 |
| Flashing red One or more CIP connections have timed out.                                                                    | Check for I/O module failure and controller operation, and correct, as needed.                       |
|                                                                                                                             | Steady red A duplicate IP address is detected. Verify the IP address setting and correct, as needed. |
| Flashing red/green The module is performing a self-test (which only occurs during the power cycle test). None               |                                                                                                      |

## Digital Module Default Data Maps

## Default Data Maps

Read this appendix for a list of default data maps for POINT I/O modules.

| For the Default Data Map of See Page                                                  |
|---------------------------------------------------------------------------------------|
| Digital Modules                                                                       |
| 1734-IB2 Sink Input Module 105                                                        |
| 1734-IB4, 1734-IB4K Sink Input Module 106                                             |
| 1734-IB8, 1734-IB8K Sink Input Module 106                                             |
| 1734-IV2 Source Input Module 107                                                      |
| 1734-IB4D Sink Input Module with Diagnostics 106                                      |
| 1734-IV4 Source Input Module 107                                                      |
| 1734-IV8, 1734-IV8K Source Input Module 107                                           |
| 1734-IA2 Input Module 107                                                             |
| 1734-IA4, 1734-IA4K Input Module 107                                                  |
| 1734-IM2 Input Module 108                                                             |
| 1734-IM4 Input Module 108                                                             |
| 1734-OA2 Output Module 108                                                            |
| 1734-OA4, 1734-OA4K Output Module 108                                                 |
| 1734-OB2E, 1734-OB2 Electronically Protected Output Module 108                        |
| 1734-OB4E, 1734-OB4, 1734-OB4K Electronically Protected Output Module 109             |
| 1734-OB8E, 1734-OB8EK, 1734-OB8, 1734-OB8K Electronically Protected Output Module 109 |
| 1734-OB2EP Protected Output Module 110                                                |
| 1734-OV2E Output Module 110                                                           |
| 1734-OV4E Output Module 110                                                           |
| 1734-OV8E, 1734-OV8EK Output Module 110                                               |
| 1734-OW2 Relay Sink/Source Output Module 111                                          |
| 1734-OW4, 1734-OW4K Relay Sink/Source Output Module 111                               |
| 1734-OX2 Relay Output Module 111                                                      |
| Analog Modules                                                                        |
| 1734-IE2C, 1734-IE2CK Analog Current Input Module 111                                 |
| 1734-IE2V Analog Voltage Input Module 112                                             |
| 1734-OE2C, 1734-OE2CK Analog Current Output Module 112                                |
| 1734-OE2V, 1734-OE2VK Analog Voltage Output Module 112                                |

I/O messages are sent to (consumer) and received from (producer) the POINT I/O modules. You map these messages into the processor memory.

## 1734-IB2 Sink Input Module

## Message Size: 1 Byte

|                                                                      | 7654321 0                                                            |                                                                      |                                                                      |                                                                      |                                                                      |                                                                      |                                                                      |
|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                | Produce (scanner Rx) Not used Ch1 Ch0                                |                                                                      |                                                                      |
| Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                | Consume (scanner Tx) No consumed data                                |
| Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Where: Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On |

<!-- image -->

## 1734-IB4, 1734-IB4K Sink Input Module

## Message Size: 1 Byte

|                                                                                                             | 7654321 0                                                                                                   |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               | Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               | Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               | Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0                                                               |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       | Consume (scanner Tx) No consumed data                                                                       |
| Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On |

## 1734-IB8, 1734-IB8K Sink Input Module

## Message Size: 1 Byte

|                                                                                                                                                                                                         | 7654321 0                                                                                                                                                                                               |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                         | Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0                                                                                                                                                    |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |                                                                                                                                                                                                         |
| Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   | Consume (scanner Tx) No consumed data                                                                                                                                                                   |
| Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off, 1 = On |

## 1734-IB4D Sink Input Module with Diagnostics

## Default Data Map - Produced Assembly Instance 101

## Message Size: 2 Bytes

|                                                                               | 7 6 5 43 2 1 0                                                                         |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|                                                                               | Produce 0 (scanner Rx) Fault 3 Fault 2 Fault 1 Fault 0 Input 3 Input 2 Input 1 Input 0 |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
|                                                                               |                                                                                        | Produce 1 (scanner Rx) SC 3 SC 2 SC 1 SC 0 OW 3 OW 2 OW 1 OW 0                |                                                                               |                                                                               |                                                                               |                                                                               |                                                                               |
| Consume (scanner Tx) No consumed data                                         | Consume (scanner Tx) No consumed data                                                  | Consume (scanner Tx) No consumed data                                         | Consume (scanner Tx) No consumed data                                         | Consume (scanner Tx) No consumed data                                         | Consume (scanner Tx) No consumed data                                         | Consume (scanner Tx) No consumed data                                         | Consume (scanner Tx) No consumed data                                         |
| Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit          | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit | Where: OW = Open wire, SC = Short circuit, Fault = Open wire or short circuit |

## Data Map - Produced Assembly Instance 23

## Message Size: 1 Byte

|                                                                                        | 7 6 5 4 32 1 0                            |                                           |                                           |                                           |                                           |                                           |                                           |
|----------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| Produce 0 (scanner Rx) Fault 3 Fault 2 Fault 1 Fault 0 Input 3 Input 2 Input 1 Input 0 |                                           |                                           |                                           |                                           |                                           |                                           |                                           |
| Consume (scanner Tx) No consumed data                                                  | Consume (scanner Tx) No consumed data     | Consume (scanner Tx) No consumed data     | Consume (scanner Tx) No consumed data     | Consume (scanner Tx) No consumed data     | Consume (scanner Tx) No consumed data     | Consume (scanner Tx) No consumed data     | Consume (scanner Tx) No consumed data     |
| Where: Fault = Open wire or short circuit                                              | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit | Where: Fault = Open wire or short circuit |

## Default Data Map - Configuration Assembly Instance 103

|                                            | 7 6 5 43 2 1 0                             |
|--------------------------------------------|--------------------------------------------|
| Consume 0 Input 0 Off to On Filter Byte 0  | Consume 0 Input 0 Off to On Filter Byte 0  |
| Consume 1 Input 0 Off to On Filter Byte 1  | Consume 1 Input 0 Off to On Filter Byte 1  |
| Consume 2 Input 0 On to Off Filter Byte 0  | Consume 2 Input 0 On to Off Filter Byte 0  |
| Consume 3 Input 0 On to Off Filter Byte 1  | Consume 3 Input 0 On to Off Filter Byte 1  |
| Consume 4 Input 1 Off to On Filter Byte 0  | Consume 4 Input 1 Off to On Filter Byte 0  |
| Consume 5 Input 1 Off to On Filter Byte 1  | Consume 5 Input 1 Off to On Filter Byte 1  |
| Consume 6 Input 1 On to Off Filter Byte 0  | Consume 6 Input 1 On to Off Filter Byte 0  |
| Consume 7 Input 1 On to Off Filter Byte 1  | Consume 7 Input 1 On to Off Filter Byte 1  |
| Consume 8 Input 2 Off to On Filter Byte 0  | Consume 8 Input 2 Off to On Filter Byte 0  |
| Consume 9 Input 2 Off to On Filter Byte 1  | Consume 9 Input 2 Off to On Filter Byte 1  |
| Consume 10 Input 2 On to Off Filter Byte 0 | Consume 10 Input 2 On to Off Filter Byte 0 |
| Consume 11 Input 2 On to Off Filter Byte 1 | Consume 11 Input 2 On to Off Filter Byte 1 |
| Consume 12 Input 3 Off to On Filter Byte 0 | Consume 12 Input 3 Off to On Filter Byte 0 |
| Consume 13 Input 3 Off to On Filter Byte 1 | Consume 13 Input 3 Off to On Filter Byte 1 |
| Consume 14 Input 3 On to Off Filter Byte 0 | Consume 14 Input 3 On to Off Filter Byte 0 |

## Default Data Map - Configuration Assembly Instance 103 (Continued)

| Message Size: 18 Bytes   | Message Size: 18 Bytes                     | Message Size: 18 Bytes                     | Message Size: 18 Bytes                     | Message Size: 18 Bytes                     | Message Size: 18 Bytes                      | Message Size: 18 Bytes                     | Message Size: 18 Bytes                     | Message Size: 18 Bytes                     |
|--------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|---------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
|                          |                                            | 7 6                                        | 5                                          | 4                                          |                                             | 3 210                                      |                                            |                                            |
|                          | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1  | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 | Consume 15 Input 3 On to Off Filter Byte 1 |
|                          | Consume 16 Autobaud Disable                |                                            |                                            |                                            | Enable OW3 Enable OW2 Enable OW1 Enable OW0 |                                            |                                            |                                            |
|                          | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance       | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      | Consume 17 Produced Assembly Instance      |
| Produce (scanner Tx)     | No produced data                           | No produced data                           | No produced data                           | No produced data                           | No produced data                            | No produced data                           | No produced data                           | No produced data                           |
|                          | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                       | Where: OW = Open wire                      | Where: OW = Open wire                      | Where: OW = Open wire                      |

## 1734-IV2 Source Input Module

## Message Size: 1 Byte

|                      |                                                               | 7654321 0                                                     |                                                               |                                                               |                                                               |                                                               |                                                               |                                                               |
|----------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Produce (scanner Rx) | Not used                                                      | Not used                                                      | Ch1 Ch0                                                       |                                                               |                                                               |                                                               |                                                               |                                                               |
| Consume (scanner Tx) | No consumed data                                              | No consumed data                                              |                                                               |                                                               |                                                               |                                                               |                                                               |                                                               |
| Where:               | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1; 0 = Off, 1 = On |

## 1734-IV4 Source Input Module

## Message Size: 1 Byte

|                      |                                                                                                             | 7654321 0                                                                                                   |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx) | Not used                                                                                                    | Not used                                                                                                    | Ch3 Ch1 Ch1 Ch0                                                                                             | Not used                                                                                                    |                                                                                                             |                                                                                                             |                                                                                                             |                                                                                                             |
| Consume (scanner Tx) | No consumed data                                                                                            | No consumed data                                                                                            | No consumed data                                                                                            | No consumed data                                                                                            | No consumed data                                                                                            | No consumed data                                                                                            | No consumed data                                                                                            | No consumed data                                                                                            |
| Where:               | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3; 0 = Off, 1 = On |

## 1734-IV8, 1734-IV8K Source Input Module

## Message Size: 1 Byte

|                      |                                                                                                                                                                                                           | 7654321 0                                                                                                                                                                                                 |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx) |                                                                                                                                                                                                           | Ch7 Ch6 Ch5 Ch4 Ch3 Ch1 Ch1 Ch0                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Consume (scanner Tx) | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          | No consumed data                                                                                                                                                                                          |
| Where:               | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On | Ch0 = Input channel 0, Ch1 = Input channel 1, Ch2 = Input channel 2, Ch3 = Input channel 3, Ch4 = Input channel 4, Ch5 = Input channel 5, Ch6 = Input channel 6, Ch7 = Input channel 7; 0 = Off ,  1 = On |

## 1734-IA2 Input Module

## Message Size: 1 Byte

|                      |                                                   | 7654321 0                                         |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
|----------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Produce (scanner Rx) |                                                   |                                                   | Ch1 Ch0                                           |                                                   |                                                   |                                                   |                                                   |                                                   |
| Consume (scanner Tx) | No consumed data                                  | No consumed data                                  | No consumed data                                  | No consumed data                                  | No consumed data                                  | No consumed data                                  | No consumed data                                  | No consumed data                                  |
| Where:               | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On |

## 1734-IA4, 1734-IA4K Input Module

## Message Size: 1 Byte

|                      |                                                                                     | 76543 2 1 0                                                                         |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |
|----------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Produce (scanner Rx) |                                                                                     |                                                                                     | Ch3 Ch2 Ch1 Ch0                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |
| Consume (scanner Tx) | No consumed data                                                                    | No consumed data                                                                    | No consumed data                                                                    | No consumed data                                                                    | No consumed data                                                                    | No consumed data                                                                    | No consumed data                                                                    | No consumed data                                                                    |
| Where:               | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On |

## 1734-IM2 Input Module

## Message Size: 1 Byte

|                                                          | 7654321 0                                                |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                                                          | Produce (scanner Rx) Ch1 Ch0                             |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |
| Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    | Consume (scanner Tx) No consumed data                    |
| Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On |

## 1734-IM4 Input Module

## Message Size: 1 Byte

|                                                                                     | 76543 2 1 0                                                                         |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Produce (scanner Rx) Ch3 Ch2 Ch1 Ch0                                                |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |                                                                                     |
| Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               | Consume (scanner Tx) No consumed data                                               |
| Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Ch0 = Channel 0, Ch1 = Channel 1, Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On |

## 1734-OA2 Output Module

## Message Size: 1 Byte

|                                                          | 7654321 0                                                |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    | Produce (scanner Rx) No produced data                    |                                                          |
| Consume (scanner Tx) Not used Ch1 Ch0 Channel state      | Consume (scanner Tx) Not used Ch1 Ch0 Channel state      | Consume (scanner Tx) Not used Ch1 Ch0 Channel state      | Consume (scanner Tx) Not used Ch1 Ch0 Channel state      | Consume (scanner Tx) Not used Ch1 Ch0 Channel state      | Consume (scanner Tx) Not used Ch1 Ch0 Channel state      |                                                          |                                                          |                                                          |                                                          |
| Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; 0 = Off, 1 = On |

## 1734-OA4, 1734-OA4K Output Module

## Message Size: 1 Byte

|                                                                                            | 76543 2 1 0                                                                                |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      | Produce (scanner Rx) No produced data                                                      |                                                                                            |
| Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state                                | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state                                | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state                                | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state                                |                                                                                            |                                                                                            |                                                                                            |                                                                                            |                                                                                            |
| Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On | Where: Ch0 = Channel 0, Ch1 = Channel 1; Ch2 = Channel 2, Ch3 = Channel 3; 0 = Off, 1 = On |

## 1734-OB2E, 1734-OB2 Electronically Protected Output Module

## Message Size: 1 Byte

|        |                                       | 7 6 54 3 2 1 0                        |                                 |                                       |                                       |                                       |                        |                        |                        |
|--------|---------------------------------------|---------------------------------------|---------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|------------------------|------------------------|------------------------|
|        | Produce (scanner Rx) Not used Ch1 Ch0 | Produce (scanner Rx) Not used Ch1 Ch0 | Channel status (1734-OB2E only) | Produce (scanner Rx) Not used Ch1 Ch0 | Produce (scanner Rx) Not used Ch1 Ch0 | Produce (scanner Rx) Not used Ch1 Ch0 |                        |                        |                        |
| Where: | 0 = No error 1 = Error                | 0 = No error 1 = Error                | 0 = No error 1 = Error          | 0 = No error 1 = Error                | 0 = No error 1 = Error                | 0 = No error 1 = Error                | 0 = No error 1 = Error | 0 = No error 1 = Error | 0 = No error 1 = Error |

## Message Size: 1 Byte

|                                                     |                | 7654321 0   |
|-----------------------------------------------------|----------------|-------------|
| Consume (scanner Tx) Not used Ch1 Ch0 Channel state |                |             |
| Where:                                              | 0 = Off 1 = On |             |

## 1734-OB4E, 1734-OB4, 1734-OB4K Electronically Protected Output Module

## 1734-OB8E, 1734-OB8EK, 1734-OB8, 1734-OB8K Electronically Protected Output Module

## Message Size: 1 Byte

7 65 43 2 1 0

Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0

Channel status

(1734-OB4E only)

Where:

0 = No error

1 = Error

## Message Size: 1 Byte

7654321 0

Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state

Where:

0 = Off

1 = On

## Message Size: 1 Byte

7 6 5 4 3 21 0

Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0

Channel status

(1734-OB8E and 1734-OB8EK

only)

Where:

0 = No error

1 = Error

## Message Size: 1 Byte

7654321 0

Consume (scanner Tx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Channel state

Where:

0 = Off

1 = On

## 1734-OB2EP Protected Output Module

## Message Size: 1 Byte

## 1734-OV2E Output Module

## 1734-OV4E Output Module

## 1734-OV8E, 1734-OV8EK Output Module

76543 2 1 0

Produce (scanner Rx) Not used Ch1 Ch0 Channel status

Where:

0 = No error

1 = Error

## Message Size: 1 Byte

76543 2 1 0

Consume (scanner Tx) Not used Ch1 Ch0 Channel state

Where:

0 = Off

1 = On

## Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) Not used Ch1 Ch0 Channel status

Where:

0 = No error

1 = Error

## Message Size: 1 Byte

76543 2 1 0

Consume (scanner Tx) Not used Ch1 Ch0 Channel state

Where:

0 = Off

1 = On

## Message Size: 1 Byte

76543 2 1 0

Produce (scanner Rx) Not used Ch3 Ch2 Ch1 Ch0 Channel status

Where:

0 = No error

1 = Error

## Message Size: 1 Byte

76543 2 1 0

Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state

Where:

0 = Off

1 = On

## Message Size: 1 Byte

7 6 5 4 3 21 0

Produce (scanner Rx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0 Channel status

Where:

0 = No error

1 = Error

## Message Size: 1 Byte

7 65 4 3 2 1 0

Consume (scanner Tx) Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0

Channel

state

Where:

0 = No error

1 = Error

## Analog Module Default Data Maps

## 1734-OW2 Relay Sink/Source Output Module

## Message Size: 1 Byte

|                                       |                | 7654321 0   |               |
|---------------------------------------|----------------|-------------|---------------|
| Consume (scanner Tx) Not used Ch1 Ch0 |                |             | Channel state |
| Where:                                | 0 = Off 1 = On |             |               |

## 1734-OW4, 1734-OW4K Relay Sink/Source Output Module

## Message Size: 1 Byte

|        |                                                             | 7654321 0                                                   |                                                             |                                                             |
|--------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
|        | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state | Consume (scanner Tx) Not used Ch3 Ch2 Ch1 Ch0 Channel state |
| Where: | 0 = Off 1 = On                                              |                                                             |                                                             |                                                             |

## 1734-OX2 Relay Output Module

## Message Size: 1 Byte

|        |                                                                     | 76543 2 1 0                                                         |                                                                     |                                                                     |                                                                     |                                                                     |                                                                     |                                                                     |                                                                     |
|--------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
|        | Consume (scanner Tx) Not used Ch1 Ch0 Channel state                 | Consume (scanner Tx) Not used Ch1 Ch0 Channel state                 | Consume (scanner Tx) Not used Ch1 Ch0 Channel state                 | Consume (scanner Tx) Not used Ch1 Ch0 Channel state                 | Consume (scanner Tx) Not used Ch1 Ch0 Channel state                 | Consume (scanner Tx) Not used Ch1 Ch0 Channel state                 |                                                                     |                                                                     |                                                                     |
| Where: | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off | 0 = NO contact Off, NC contact On 1 = NO contact On, NC contact Off |

I/O messages are sent to (consumer) and received from (producer) the POINT I/O modules. You map these messages into the processor memory.

## 1734-IE2C, 1734-IE2CK Analog Current Input Module

## Message Size: 6 Bytes

|                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx) | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx) | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx) | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Produce (scanner Rx) |                                                                                                                                                                                                                                                                                                                                                                          | OR UR HHA LLA HA LA CM CF OR UR HHA LLA HA LA CM CF                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                          |
| Consume (scanner Tx) | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         | No consumed data                                                                                                                                                                                                                                                                                                                                                         |
| Where:               | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault OR = Overrange; 0 = No error, 1 = Fault |

## Channel Status

| Channel Status Bytes   | Channel Status Bytes                            | Channel Status Bytes                                      | Channel Status Bytes   | Channel Status Bytes   | Channel Status Bytes   | Channel Status Bytes   | Channel Status Bytes   |
|------------------------|-------------------------------------------------|-----------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                        | Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |                                                           |                        |                        |                        |                        |                        |
| Overrange Underrange   | High High Alarm                                 | Low Low Alarm High Alarm Low Alarm CAL Mode Channel Fault |                        |                        |                        |                        |                        |

## 1734-IE2V Analog Voltage Input Module

## Message Size: 6 Bytes

|                                       |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx)                  | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 0 High Byte Input Channel 0 Low Byte                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
| Produce (scanner Rx)                  | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               | Input Channel 1 High Byte Input Channel 1 Low Byte                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
| Produce (scanner Rx)                  | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              | Status Byte for Channel 1 Status Byte for Channel 0                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
| Produce (scanner Rx)                  |                                                                                                                                                                                                                                                                                                                                  | OR UR HHA LLA HA LA CM CF OR UR HHA LLA HA LA CM CF                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
| Consume (scanner Tx) No consumed data |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                  |
| Where:                                | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LA = Low Alarm; 0 = No error, 1 = Fault HA = High Alarm; 0 = No error, 1 = Fault LLA = Low/Low Alarm; 0 = No error, 1 = Fault HHA = High/High Alarm; 0 = No error, 1 = Fault UR = Underrange; 0 = No error, 1 = Fault |

## 1734-OE2C, 1734-OE2CK Analog Current Output Module

## Message Size: 4 bytes

|                                                                   | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                   |                                                                   |                                                                   |                                                                   |                                                                   |                                                                   |                                                                   |
|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (Tx) Output Channel 0 High Byte Output Channel 0 Low Byte |
| Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              | Output Channel 1 High Byte Output Channel 1 Low Byte              |

## Message Size: 2 Bytes

|        |                                                                                                                                                                                                           |                                                                                                                                                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         | Produce (Rx) High Byte Channel 1 Status Low Byte Channel 0 Status                                                                                                                                         |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|        |                                                                                                                                                                                                           | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Where: | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault |

## Channel Status

| Channel Status Bytes   | Channel Status Bytes                            | Channel Status Bytes                                 | Channel Status Bytes   | Channel Status Bytes   | Channel Status Bytes   | Channel Status Bytes   | Channel Status Bytes   |
|------------------------|-------------------------------------------------|------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
|                        | Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0 |                                                      |                        |                        |                        |                        |                        |
|                        |                                                 | Not used High Clamp Low Clamp CAL Mode Channel Fault |                        |                        |                        |                        |                        |

## 1734-OE2V, 1734-OE2VK Analog Voltage Output Module

## Message Size: 4 bytes

|                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                           |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte | Consume (scanner Tx) Output Channel 0 High Byte Output Channel 0 Low Byte |
| Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      | Output Channel 1 High Byte Output Channel 1 Low Byte                      |

## Message Size: 2 Bytes

|                      |                                                                                                                                                                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produce (scanner Rx) | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      | Channel 1 Status High Byte Channel 0 Status Low Byte                                                                                                                                                      |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Produce (scanner Rx) | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             | Not used HCA LCA CM CF Not used HCA LCA CM CF                                                                                                                                                             |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |                                                                                                                                                                                                           |
| Where:               | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault | CF = Channel Fault status; 0 = No error, 1 = Fault CM = Calibration Mode; 0 = Normal, 1 = Calibration mode LCA = Low Clamp Alarm; 0 = No error, 1 = Fault HCA = High Clamp Alarm; 0 = No error, 1 = Fault |

## POINT I/O Module with a 1734-ADN, 1734-ACNR, 1734-AENT, or 1734-APB Adapter

## Mounting Dimensions

Read this appendix for mounting dimensions for the following:

- POINT I/O module with a 1734-ADN, 1734-ACNR, 1734-AENT, or 1734-APB adapter
- POINT I/O module with a 1734-PDN module
- POINTBlock I/O modules

See the figure for mounting dimensions for a POINT I/O module with a network adapter. The example figure shows a 1734-ADN adapter.

<!-- image -->

Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.).

<!-- image -->

## POINT I/O Module with a 1734-PDN Module

See the figure for mounting dimensions for POINT I/O module with a 1734-PDN DeviceNet Communication Interface module.

Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.).

<!-- image -->

## POINTBlock Module

## See the figure for mounting dimensions for a 1734D POINTBlock module.

<!-- image -->

Secure DIN rail to mounting surface approximately every 200 mm (7.8 in.).

## Notes:

## Numerics

## 1734D-IA16 module

about 11

## 1734D-IA8XOA8 module

about 11

## 1734D-IA8XOW8 module

about 11

## 1734D-IB16 module

about 11

## 1734D-IB8XOB module

about 11

## 1734D-IB8XOW8 module

about 11

## 1734-IA2 module

about 11 default data map 107 troubleshoot 93

## 1734-IA4, 1734-IA4K module

about 11 default data map 107 troubleshoot 93

## 1734-IB2 module

about 11 default data map 105 troubleshoot 89

## 1734-IB4, 1734-IB4K module

about 11 default data map 106 troubleshoot 89

## 1734-IB4D module

about 11 default data map 106 troubleshoot 89

## 1734-IB8, 1734-IB8K module

about 11 default data map 106 troubleshoot 89

## 1734-IE2C, 1734-IE2CK module

about 13 default data map 111 troubleshoot 95

## 1734-IE2V module

about 13 default data map 112

## 1734-IE2V, 1734-IE2VK module

troubleshoot 96

## 1734-IM module

about 11 default data map 108 troubleshoot 94

## 1734-IV2 module

about 11 default data map 107 troubleshoot 91

## 1734-IV4 module

about 11 default data map 107 troubleshoot 91

## 1734-IV8, 1734-IV8K module

about 11 default data map 107 troubleshoot 91

## 1734-OA2 module

about 11 default data map 108 troubleshoot 94

## 1734-OA4, 1734-OA4K module

about 11 default data map 108 troubleshoot 94

## 1734-OB2 module

about 11 default data map 108 troubleshoot 90

## 1734-OB2E module

about 11 default data map 108 troubleshoot 90

## 1734-OB2EP module

about 11 default data map 110 troubleshoot 91

## 1734-OB4, 1734-OB4K module

about 11 default data map 109 troubleshoot 90

## 1734-OB4E module

about 11 default data map 109 troubleshoot 90

## 1734-OB8, 1734-OB8K module

about 11 default data map 109 troubleshoot 90

## 1734-OB8E, 1734-OB8EK module

about 11 default data map 109 troubleshoot 90

## 1734-OE2C, 1734-OE2CK module

about 13 default data map 112 troubleshoot 95

## 1734-OE2V, 1734-OE2VK module

about 13 default data map 112 troubleshoot 97

## 1734-OV2E module

about 11 default data map 110 troubleshoot 92

## 1734-OV4E module

about 11 default data map 110 troubleshoot 92

## 1734-OV8E, 1734-OV8EK module

about 11 default data map 110 troubleshoot 92

## 1734-OW2 module

about 11 default data map 111 troubleshoot 92

## 1734-OW4, 1734-OW4K module

about 11 default data map 111 troubleshoot 92

## 1734-OX2 module

about 11 default data map 111 troubleshoot 93

## A

## about

analog input modules 13

analog output modules digital input modules 11 digital output module 12 relay output modules 12

14

alarm 60 , 61

configuration dialog 27 disable 60 , 65 latch 60

## analog

input modules 13 , 58 modules 13 , 58 , 62 , 71 output modules 14 , 62

## C

## calibrating

analog current input module 72 analog current output module 75 analog modules 71

analog voltage input module 79

analog voltage output module 82

## calibration

dialog 28 , 32 instruments 71 status bit 60

status indicators 87

channel indicator states 62 , 66

## channel status

analog input modules 59 analog output modules 64

## clamps

cage 66 high 14 , 51 , 65 low 14 , 51 , 65 66

spring

## commissioning

nodes 35

tool 35

## configure analog modules

using RSLogix 5000 software 24

## configure digital modules

using RSLogix 5000 software 17 using RSNetWorx software 36

configure the module 53

ControlNet network 7 , 35

## D

data maps 53 , 105 - 112

default data maps 53 , 105 - 112

DeviceNet network 7 , 35

diagnostics, module 87

## digital

ac input modules 55

ac output modules dc input modules 53 dc output modules filter 61

57

55

dimensions for mounting 113

disable alarms 60 , 65

## E

EDS, electronic data sheet 35 , 36

electronic data sheet 35

EtherNet/IP network 7 , 35

## F

fault and idle mode state 64

filter notch 26 , 61

## H

high alarm

27 , 31 , 61

high high alarm 27 , 61

## I

indicators, LED 87

## L

latch alarms 60 , 65

LED indicators 87

low alarm 27 , 31 , 61

low low alarm 27 , 61

## M

## module

status 53

module diagnostics 87

module status indicator 87

## mounting

dimensions POINT I/O module with a 1734ADN adapter 113 dimensions POINT I/O module with a 1734PDN DeviceNet Communication Interface module 114

dimensions POINTBlock module 115

## N

## network

DeviceNet 35 PROFIBUS 7

network status indicator 87

node commissioning tool notch filter 26 61

,

## O

over range status 62

## P

POINTBus 36

power indicator

87

PROFIBUS network 7

## R

range status 62

relay module 12

output modules 57

RSNetWorx software

35

for DeviceNet node commissioning tool 35

## S

SAA, sequential auto addressing 36 scaling analog input modules 59 64

analog output modules sequential auto addressing 36

specialty modules 14

## T

third party configuration software 36

35

## troubleshoot

1734-IB4, 1734-IB4K module 89

1734-IB8, 1734-IB8K module 89

1734-IE2C, 1734-IE2CK module 95

1734-IV8, 1734-IV8K module 91

1734-OB4, 1734-OB4K module 90

1734-OB8, 1734-OB8K module 90

1734-OB8E, 1734-OB8EK module 90

1734-OE2C, 1734-OE2CK module 95

1734-OE2V, 1734-OE2VK module 97

1734-OW4, 1734-OW4K module 92

1734-ACNR adapter 100 1734-ADN adapter 98 1734-AENT adapter 103 1734-APB adapter 102 1734-IA2 module 93 1734-IB2 module 89 1734-IE2V module 96 1734-IM2 module 94 1734-IV2 module 91 1734-IV4 module 91 1734-OA2 module 94 1734-OB2 module 90 1734-OB2EP module 91 1734-OB4E module 90 1734-OV2E module 92 1734-OV4E module 92 1734-OW2 module 92 1734-OX2 module 93 analog modules 95 digital modules 89

I/O communications modules 97

## U

under range status 62 update rate 61

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

Allen-Bradley, expanding human possibility, FactoryTalk, Logix 5000, POINT I/O, POINTBus, RSNetWorx, RSNetWorx for DeviceNet, RSLogix 5000, Rockwell Automation, Studio 5000 Logix Designer, and TechConnect are trademarks of Rockwell Automation, Inc.

CIP, ControlNet, DeviceNet, and EtherNet/IP are trademarks of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility?

AMERICAS:RockwellAutomation,1201SouthSec0ndStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000 EUROPE/MIDDLEEAST/AFRICA:Rockwell AutomationNV,Pegasus Park,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600 UNITEDKINGD0M:RockwellAutomationLtd.,Pitfield,KilnFarm,MiltonKeynes,MK113DR,UnitedKingdom,Tel:(44)(1908)838-800